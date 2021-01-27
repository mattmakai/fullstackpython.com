title: django.template.defaultfilters slugify Example Code
category: page
slug: django-template-defaultfilters-slugify-examples
sortorder: 500011386
toc: False
sidebartitle: django.template.defaultfilters slugify
meta: Python example code that shows how to use the slugify callable from the django.template.defaultfilters module of the Django project.


`slugify` is a callable within the `django.template.defaultfilters` module of the Django project.

<a href="/django-template-defaultfilters-escape-examples.html">escape</a>,
<a href="/django-template-defaultfilters-filesizeformat-examples.html">filesizeformat</a>,
<a href="/django-template-defaultfilters-safe-examples.html">safe</a>,
<a href="/django-template-defaultfilters-striptags-examples.html">striptags</a>,
<a href="/django-template-defaultfilters-title-examples.html">title</a>,
and <a href="/django-template-defaultfilters-truncatechars-examples.html">truncatechars</a>
are several other callables with code examples from the same `django.template.defaultfilters` package.

## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / plugin_pool.py**](https://github.com/divio/django-cms/blob/develop/cms/./plugin_pool.py)

```python
# plugin_pool.py
from operator import attrgetter

from django.core.exceptions import ImproperlyConfigured
from django.urls import re_path, include
~~from django.template.defaultfilters import slugify
from django.utils.encoding import force_text
from django.utils.functional import cached_property
from django.utils.module_loading import autodiscover_modules
from django.utils.translation import get_language, deactivate_all, activate
from django.template import TemplateDoesNotExist, TemplateSyntaxError

from cms.exceptions import PluginAlreadyRegistered, PluginNotRegistered
from cms.plugin_base import CMSPluginBase
from cms.utils.conf import get_cms_setting
from cms.utils.helpers import normalize_name


class PluginPool:

    def __init__(self):
        self.plugins = {}
        self.discovered = False

    def _clear_cached(self):
        if 'registered_plugins' in self.__dict__:
            del self.__dict__['registered_plugins']

        if 'plugins_with_extra_menu' in self.__dict__:
            del self.__dict__['plugins_with_extra_menu']


## ... source file abbreviated to get to slugify examples ...


        if placeholder:
            plugins = (plugin for plugin in plugins
                       if not plugin.requires_parent_plugin(placeholder, page))
        return sorted(plugins, key=attrgetter('module'))

    def get_text_enabled_plugins(self, placeholder, page):
        plugins = set(self.get_all_plugins(placeholder, page))
        plugins.update(self.get_all_plugins(placeholder, page, 'text_only_plugins'))
        return sorted((p for p in plugins if p.text_enabled),
                      key=attrgetter('module', 'name'))

    def get_plugin(self, name):
        self.discover_plugins()
        return self.plugins[name]

    def get_patterns(self):
        self.discover_plugins()

        lang = get_language()
        deactivate_all()

        try:
            url_patterns = []
            for plugin in self.registered_plugins:
                p = plugin()
~~                slug = slugify(force_text(normalize_name(p.__class__.__name__)))
                url_patterns += [
                    re_path(r'^plugin/%s/' % (slug,), include(p.plugin_urls)),
                ]
        finally:
            activate(lang)

        return url_patterns

    def get_system_plugins(self):
        self.discover_plugins()
        return [plugin.__name__ for plugin in self.plugins.values() if plugin.system]

    @cached_property
    def registered_plugins(self):
        return self.get_all_plugins()

    @cached_property
    def plugins_with_extra_menu(self):
        plugin_classes = [cls for cls in self.registered_plugins
                          if cls._has_extra_plugin_menu_items]
        return plugin_classes

    @cached_property
    def plugins_with_extra_placeholder_menu(self):


## ... source file continues with no further slugify examples...

```


## Example 2 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / utils / files.py**](https://github.com/divio/django-filer/blob/develop/filer/utils/files.py)

```python
# files.py
from __future__ import absolute_import, unicode_literals

import mimetypes
import os

from django.http.multipartparser import (
    ChunkIter, SkipFile, StopFutureHandlers, StopUpload, exhaust,
)
~~from django.template.defaultfilters import slugify as slugify_django
from django.utils.encoding import force_text
from django.utils.text import get_valid_filename as get_valid_filename_django

from unidecode import unidecode


class UploadException(Exception):
    pass


def handle_upload(request):
    if not request.method == "POST":
        raise UploadException("AJAX request not valid: must be POST")
    if request.is_ajax():
        is_raw = True
        filename = request.GET.get('qqfile', False) or request.GET.get('filename', False) or ''

        try:
            content_length = int(request.META['CONTENT_LENGTH'])
        except (IndexError, TypeError, ValueError):
            content_length = None

        if content_length < 0:
            raise UploadException("Invalid content length: %r" % content_length)


## ... source file abbreviated to get to slugify examples ...


        for i, handler in enumerate(upload_handlers):
            file_obj = handler.file_complete(counters[i])
            if file_obj:
                upload = file_obj
                break
    else:
        if len(request.FILES) == 1:
            upload, filename, is_raw, mime_type = handle_request_files_upload(request)
        else:
            raise UploadException("AJAX request not valid: Bad Upload")
    return upload, filename, is_raw, mime_type


def handle_request_files_upload(request):
    is_raw = False
    upload = list(request.FILES.values())[0]
    filename = upload.name
    _, iext = os.path.splitext(filename)
    mime_type = upload.content_type.lower()
    if iext not in mimetypes.guess_all_extensions(mime_type):
        msg = "MIME-Type '{mimetype}' does not correspond to file extension of {filename}."
        raise UploadException(msg.format(mimetype=mime_type, filename=filename))
    return upload, filename, is_raw, mime_type


~~def slugify(string):
    return slugify_django(unidecode(force_text(string)))


def get_valid_filename(s):
    s = get_valid_filename_django(s)
    filename, ext = os.path.splitext(s)
~~    filename = slugify(filename)
~~    ext = slugify(ext)
    if ext:
        return "%s.%s" % (filename, ext)
    else:
        return "%s" % (filename,)



## ... source file continues with no further slugify examples...

```


## Example 3 from gadget-board
[gadget-board](https://github.com/mik4el/gadget-board) is a
[Django](/django.html),
[Django REST Framework (DRF)](/django-rest-framework-drf.html) and
[Angular](/angular.html) web application that is open source under the
[Apache2 license](https://github.com/mik4el/gadget-board/blob/master/LICENSE).

[**gadget-board / web / gadgets / models.py**](https://github.com/mik4el/gadget-board/blob/master/web/gadgets/models.py)

```python
# models.py
from django.db import models
from django.contrib.postgres.fields import JSONField
~~from django.template.defaultfilters import slugify
from authentication.models import Account


class Gadget(models.Model):
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField()
    users_can_upload = models.ManyToManyField(Account)
    image_name = models.CharField(max_length=140, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def image_url(self):
        if self.image_name != "":
            return "backend/static/media/{}".format(self.image_name)
        else:
            return "backend/static/dashboard_icon_big.png"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
~~            self.slug = slugify(self.name)

        super(Gadget, self).save(*args, **kwargs)


class GadgetData(models.Model):
    gadget = models.ForeignKey(Gadget, db_index=True, on_delete=models.DO_NOTHING)  # Add index on filtered fields
    data = JSONField()
    added_by = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(null=True, blank=True, db_index=True)  # Add index on filtered fields
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {} {}'.format(self.gadget, self.timestamp, self.added_by)



## ... source file continues with no further slugify examples...

```

