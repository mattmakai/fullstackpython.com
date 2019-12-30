title: django.conf settings Example Code
category: page
slug: django-conf-settings-examples
sortorder: 500010050
toc: False
sidebartitle: django.conf settings
meta: Python code examples for Django settings files.


The [Django](/django.html) 
[settings](https://docs.djangoproject.com/en/dev/topics/settings/)
file contains all of the configuration for a web application.


## Example 1 from django-easy-timezones
[django-easy-timezones](https://github.com/Miserlou/django-easy-timezones)
([project website](https://www.gun.io/blog/django-easy-timezones))
is a [Django](/django.html) 
[middleware](https://docs.djangoproject.com/en/stable/topics/http/middleware/)
[code library](https://pypi.org/project/django-easy-timezones/)
to simplify handling time data in your applications using
users' geolocation data.

This example shows how to import the configuration from your Django 
`settings.py` file into a different part of your web application.

[**django-easy-timezones/easy_timezones/middleware.py**](https://github.com/Miserlou/django-easy-timezones/blob/master/easy_timezones/middleware.py)

```python
import django
~~from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured
from django.utils import timezone
import pytz
import pygeoip
import os

from .signals import detected_timezone
from .utils import get_ip_address_from_request, is_valid_ip, is_local_ip


db_loaded = False
db = None
db_v6 = None

def load_db_settings():
~~    GEOIP_DATABASE = getattr(settings, 'GEOIP_DATABASE', 'GeoLiteCity.dat')

    if not GEOIP_DATABASE:
        raise ImproperlyConfigured("GEOIP_DATABASE setting has not been " + \
                                   "properly defined.")

    if not os.path.exists(GEOIP_DATABASE):
        raise ImproperlyConfigured("GEOIP_DATABASE setting is defined, " + \
                                   "but file does not exist.")

~~    GEOIPV6_DATABASE = getattr(settings, 'GEOIPV6_DATABASE', 
~~                               'GeoLiteCityv6.dat')

    if not GEOIPV6_DATABASE:
        raise ImproperlyConfigured("GEOIPV6_DATABASE setting has not " + \
                                   "been properly defined.")

    if not os.path.exists(GEOIPV6_DATABASE):
        raise ImproperlyConfigured("GEOIPV6_DATABASE setting is " + \
                                   "defined, but file does not exist.")

    return (GEOIP_DATABASE, GEOIPV6_DATABASE)

load_db_settings()

def load_db():

    GEOIP_DATABASE, GEOIPV6_DATABASE = load_db_settings()

    global db
    db = pygeoip.GeoIP(GEOIP_DATABASE, pygeoip.MEMORY_CACHE)

    global db_v6
    db_v6 = pygeoip.GeoIP(GEOIPV6_DATABASE, pygeoip.MEMORY_CACHE)

    global db_loaded
    db_loaded = True


if django.VERSION >= (1, 10):
    from django.utils.deprecation import MiddlewareMixin
    middleware_base_class = MiddlewareMixin
else:
    middleware_base_class = object


class EasyTimezoneMiddleware(middleware_base_class):
    def process_request(self, request):
        """
        If we can get a valid IP from the request,
        look up that address in the database to get the appropriate 
        timezone and activate it. Else, use the default.
        """

        if not request:
            return

        if not db_loaded:
            load_db()

        tz = request.session.get('django_timezone')

        if not tz:
            # use the default timezone (settings.TIME_ZONE) for localhost
            tz = timezone.get_default_timezone()

            client_ip = get_ip_address_from_request(request)
            ip_addrs = client_ip.split(',')
            for ip in ip_addrs:
                if is_valid_ip(ip) and not is_local_ip(ip):
                    if ':' in ip:
                        tz = db_v6.time_zone_by_addr(ip)
                        break
                    else:
                        tz = db.time_zone_by_addr(ip)
                        break

        if tz:
            timezone.activate(tz)
            request.session['django_timezone'] = str(tz)
~~            if getattr(settings, 'AUTH_USER_MODEL', 
~~                       None) and getattr(request, 'user', None):
                detected_timezone.send(sender=get_user_model(), 
                                       instance=request.user, 
                                       timezone=tz)
        else:
            timezone.deactivate()
```


## Example 2 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images 
in Django's admin interface. The project's code is available under the 
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

This example code file shows how to set many parts of the configuration
within a `setttings.py` file.

[**django-filer / filer / settings.py**](https://github.com/divio/django-filer/blob/develop/filer/settings.py)

```python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import logging
import os

~~from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.files.storage import get_storage_class

from .utils.loader import load_object
from .utils.recursive_dictionary import RecursiveDictionaryWithExcludes


logger = logging.getLogger(__name__)

# FILER_IMAGE_MODEL setting is used to swap Image model.
# If such global setting does not exist, it will be created at this 
# point (with default model name).
# This is needed especially when using this setting in migrations.
~~if not hasattr(settings, 'FILER_IMAGE_MODEL'):
~~    setattr(settings, 'FILER_IMAGE_MODEL', 'filer.Image')
~~FILER_IMAGE_MODEL = settings.FILER_IMAGE_MODEL

~~FILER_DEBUG = getattr(settings, 'FILER_DEBUG', False)  # When True makes
~~FILER_SUBJECT_LOCATION_IMAGE_DEBUG = getattr(settings, 
~~                                       'FILER_SUBJECT_LOCATION_IMAGE_DEBUG', 
~~                                       False)
~~FILER_WHITESPACE_COLOR = getattr(settings, 'FILER_WHITESPACE_COLOR', 
~~                                 '#FFFFFF')

~~FILER_0_8_COMPATIBILITY_MODE = getattr(settings, 
~~                                       'FILER_0_8_COMPATIBILITY_MODE', 
~~                                       False)

~~FILER_ENABLE_LOGGING = getattr(settings, 'FILER_ENABLE_LOGGING', 
~~                               False)
~~if FILER_ENABLE_LOGGING:
~~    FILER_ENABLE_LOGGING = (
~~        FILER_ENABLE_LOGGING and (getattr(settings, 'LOGGING')
~~                             and ('' in settings.LOGGING['loggers']
~~                             or 'filer' in settings.LOGGING['loggers'])))

~~FILER_ENABLE_PERMISSIONS = getattr(settings, 'FILER_ENABLE_PERMISSIONS', 
~~                                   False)
~~FILER_ALLOW_REGULAR_USERS_TO_ADD_ROOT_FOLDERS = getattr(settings, 
~~  'FILER_ALLOW_REGULAR_USERS_TO_ADD_ROOT_FOLDERS', False)
~~FILER_IS_PUBLIC_DEFAULT = getattr(settings, 'FILER_IS_PUBLIC_DEFAULT', True)

~~FILER_PAGINATE_BY = getattr(settings, 'FILER_PAGINATE_BY', 20)

~~_ICON_SIZES = getattr(settings, 'FILER_ADMIN_ICON_SIZES', 
~~                      ('16', '32', '48', '64'))
if not _ICON_SIZES:
    raise ImproperlyConfigured('Please, configure FILER_ADMIN_ICON_SIZES')
# Reliably sort by integer value, but keep icon size as string.
# (There is some code in the wild that depends on this being strings.)
FILER_ADMIN_ICON_SIZES = \
  [str(i) for i in sorted([int(s) for s in _ICON_SIZES])]

# Filer admin templates have specific icon sizes hardcoded: 32 and 48.
_ESSENTIAL_ICON_SIZES = ('32', '48')
if not all(x in FILER_ADMIN_ICON_SIZES for x in _ESSENTIAL_ICON_SIZES):
    logger.warn(
        "FILER_ADMIN_ICON_SIZES has not all of the essential icon sizes "
        "listed: {}. Some icons might be missing in admin templates.".format(
            _ESSENTIAL_ICON_SIZES))

# This is an ordered iterable that describes a list of
# classes that I should check for when adding files
~~FILER_FILE_MODELS = getattr(
~~    settings, 'FILER_FILE_MODELS',
~~    (FILER_IMAGE_MODEL, 'filer.File'))

~~DEFAULT_FILE_STORAGE = getattr(settings, 'DEFAULT_FILE_STORAGE', 
~~                               'django.core.files.storage.FileSystemStorage')

MINIMAL_FILER_STORAGES = {
    'public': {
        'main': {
            'ENGINE': None,
            'OPTIONS': {},
        },
        'thumbnails': {
            'ENGINE': None,
            'OPTIONS': {},
        }
    },
    'private': {
        'main': {
            'ENGINE': None,
            'OPTIONS': {},
        },
        'thumbnails': {
            'ENGINE': None,
            'OPTIONS': {},
        },
    },
}


DEFAULT_FILER_STORAGES = {
    'public': {
        'main': {
            'ENGINE': DEFAULT_FILE_STORAGE,
            'OPTIONS': {},
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX': 'filer_public',
        },
        'thumbnails': {
            'ENGINE': DEFAULT_FILE_STORAGE,
            'OPTIONS': {},
            'THUMBNAIL_OPTIONS': {
                'base_dir': 'filer_public_thumbnails',
            },
        },
    },
    'private': {
        'main': {
            'ENGINE': 'filer.storage.PrivateFileSystemStorage',
            'OPTIONS': {
~~                'location': os.path.abspath(os.path.join(settings.MEDIA_ROOT, 
~~                    '../smedia/filer_private')),
                'base_url': '/smedia/filer_private/',
            },
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX': '',
        },
        'thumbnails': {
            'ENGINE': 'filer.storage.PrivateFileSystemStorage',
            'OPTIONS': {
~~                'location': os.path.abspath(os.path.join(settings.MEDIA_ROOT, 
~~                    '../smedia/filer_private_thumbnails')),
                'base_url': '/smedia/filer_private_thumbnails/',
            },
            'THUMBNAIL_OPTIONS': {},
        },
    },
}

MINIMAL_FILER_SERVERS = {
    'private': {
        'main': {
            'ENGINE': None,
            'OPTIONS': {},
        },
        'thumbnails': {
            'ENGINE': None,
            'OPTIONS': {},
        },
    },
}

DEFAULT_FILER_SERVERS = {
    'private': {
        'main': {
            'ENGINE': 'filer.server.backends.default.DefaultServer',
            'OPTIONS': {},
        },
        'thumbnails': {
            'ENGINE': 'filer.server.backends.default.DefaultServer',
            'OPTIONS': {},
        },
    },
}

FILER_STORAGES = RecursiveDictionaryWithExcludes(MINIMAL_FILER_STORAGES, 
    rec_excluded_keys=('OPTIONS', 'THUMBNAIL_OPTIONS'))
if FILER_0_8_COMPATIBILITY_MODE:
    user_filer_storages = {
        'public': {
            'main': {
                'ENGINE': DEFAULT_FILE_STORAGE,
                'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
~~                'UPLOAD_TO_PREFIX': getattr(settings, 
~~                                            'FILER_PUBLICMEDIA_PREFIX', 
~~                                            'filer_public'),
            },
            'thumbnails': {
                'ENGINE': DEFAULT_FILE_STORAGE,
                'OPTIONS': {},
                'THUMBNAIL_OPTIONS': {
                    'base_dir': 'filer_public_thumbnails',
                },
            },
        },
        'private': {
            'main': {
                'ENGINE': DEFAULT_FILE_STORAGE,
                'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
~~                'UPLOAD_TO_PREFIX': getattr(settings, 
~~                                            'FILER_PRIVATEMEDIA_PREFIX', 
~~                                            'filer_private'),
            },
            'thumbnails': {
                'ENGINE': DEFAULT_FILE_STORAGE,
                'OPTIONS': {},
                'THUMBNAIL_OPTIONS': {
                    'base_dir': 'filer_private_thumbnails',
                },
            },
        },
    }
else:
~~    user_filer_storages = getattr(settings, 'FILER_STORAGES', {})

FILER_STORAGES.rec_update(user_filer_storages)


def update_storage_settings(user_settings, defaults, s, t):
    if not user_settings[s][t]['ENGINE']:
        user_settings[s][t]['ENGINE'] = defaults[s][t]['ENGINE']
        user_settings[s][t]['OPTIONS'] = defaults[s][t]['OPTIONS']
    if t == 'main':
        if 'UPLOAD_TO' not in user_settings[s][t]:
            user_settings[s][t]['UPLOAD_TO'] = defaults[s][t]['UPLOAD_TO']
        if 'UPLOAD_TO_PREFIX' not in user_settings[s][t]:
            user_settings[s][t]['UPLOAD_TO_PREFIX'] = \
                defaults[s][t]['UPLOAD_TO_PREFIX']
    if t == 'thumbnails':
        if 'THUMBNAIL_OPTIONS' not in user_settings[s][t]:
            user_settings[s][t]['THUMBNAIL_OPTIONS'] = \
                defaults[s][t]['THUMBNAIL_OPTIONS']
    return user_settings


update_storage_settings(FILER_STORAGES, DEFAULT_FILER_STORAGES, 
                        'public', 'main')
update_storage_settings(FILER_STORAGES, DEFAULT_FILER_STORAGES, 
                        'public', 'thumbnails')
update_storage_settings(FILER_STORAGES, DEFAULT_FILER_STORAGES, 
                        'private', 'main')
update_storage_settings(FILER_STORAGES, DEFAULT_FILER_STORAGES, 
                        'private', 'thumbnails')

FILER_SERVERS = RecursiveDictionaryWithExcludes(MINIMAL_FILER_SERVERS, 
    rec_excluded_keys=('OPTIONS',))
~~FILER_SERVERS.rec_update(getattr(settings, 'FILER_SERVERS', {}))


~~def update_server_settings(settings, defaults, s, t):
~~    if not settings[s][t]['ENGINE']:
~~        settings[s][t]['ENGINE'] = defaults[s][t]['ENGINE']
~~        settings[s][t]['OPTIONS'] = defaults[s][t]['OPTIONS']
~~    return settings


# file continues here with a few more settings examples, but nothing 
# too different from what was shown above
```


## Example 3 from django-cors-headers
[django-cors-headers](https://github.com/ottoyiu/django-cors-headers) is
an 
[open source](https://github.com/ottoyiu/django-cors-headers/blob/master/LICENSE)
library for enabling 
[Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) 
handling in your [Django](/django.html) web applications and appropriately
dealing with HTTP headers for CORS requests.

[**django-cors-headers / src / corsheaders / conf.py**](https://github.com/ottoyiu/django-cors-headers/blob/master/src/corsheaders/conf.py)

```python
~~from django.conf import settings

# Kept here for backwards compatibility
from corsheaders.defaults import default_headers, default_methods


class Settings(object):
    """
    Shadow Django's settings with a little logic
    """

    @property
    def CORS_ALLOW_HEADERS(self):
~~        return getattr(settings, "CORS_ALLOW_HEADERS", default_headers)

    @property
    def CORS_ALLOW_METHODS(self):
~~        return getattr(settings, "CORS_ALLOW_METHODS", default_methods)

    @property
    def CORS_ALLOW_CREDENTIALS(self):
~~        return getattr(settings, "CORS_ALLOW_CREDENTIALS", False)

    @property
    def CORS_PREFLIGHT_MAX_AGE(self):
~~        return getattr(settings, "CORS_PREFLIGHT_MAX_AGE", 86400)

    @property
    def CORS_ORIGIN_ALLOW_ALL(self):
~~        return getattr(settings, "CORS_ORIGIN_ALLOW_ALL", False)

    @property
    def CORS_ORIGIN_WHITELIST(self):
~~        return getattr(settings, "CORS_ORIGIN_WHITELIST", ())

    @property
    def CORS_ORIGIN_REGEX_WHITELIST(self):
~~        return getattr(settings, "CORS_ORIGIN_REGEX_WHITELIST", ())

    @property
    def CORS_EXPOSE_HEADERS(self):
~~        return getattr(settings, "CORS_EXPOSE_HEADERS", ())

    @property
    def CORS_URLS_REGEX(self):
~~        return getattr(settings, "CORS_URLS_REGEX", r"^.*$")

    @property
    def CORS_REPLACE_HTTPS_REFERER(self):
~~        return getattr(settings, "CORS_REPLACE_HTTPS_REFERER", False)


conf = Settings()
```


## Example 4 from django-angular
[django-angular](https://github.com/jrief/django-angular) 
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use 
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is 
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

The following example shows how to check if an Django app is specified 
under `INSTALLED_APPS` and if not, throw an exception to let the developer
know their project is not properly configured.

[**django-angular / djng / forms / fields.py**](https://github.com/jrief/django-angular/blob/master/djng/forms/fields.py)

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import mimetypes

~~from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core import signing
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from django.urls import reverse_lazy
from django.forms import fields, models as model_fields, widgets
from django.utils.html import format_html
from django.utils.module_loading import import_string
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _, ungettext_lazy

## ... source code lines cut here for brevity ...


class ImageField(FileFieldMixin, fields.ImageField):
    storage = app_settings.upload_storage
    signer = signing.Signer()

    def __init__(self, *args, **kwargs):
~~        if 'easy_thumbnails' not in settings.INSTALLED_APPS:
~~            raise ImproperlyConfigured("'djng.forms.fields.ImageField' \
~~                requires 'easy-thubnails' to be installed")
        accept = kwargs.pop('accept', 'image/*')
        fileupload_url = kwargs.pop('fileupload_url', 
                                    reverse_lazy('fileupload'))
        area_label = kwargs.pop('area_label', 
                                _("Drop image here or click to upload"))
        attrs = {
            'accept': accept,
            'ngf-pattern': accept,
        }
        kwargs.update(widget=DropImageWidget(area_label, 
                                             fileupload_url, 
                                             attrs=attrs))
        super(ImageField, self).__init__(*args, **kwargs)
```
