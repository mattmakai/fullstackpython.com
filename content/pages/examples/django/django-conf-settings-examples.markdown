title: django.conf settings Examples
category: page
slug: django-conf-settings-examples
sortorder: 50010
toc: False
sidebartitle: django.conf settings
meta: Python code examples for Django settings files.


# django.conf settings Examples
The [Django](/django.html) 
[settings](https://docs.djangoproject.com/en/dev/topics/settings/)
file contains all of the configuration for a web application.


## Example 1 from django-easy-timezones
[django-easy-timezones](https://github.com/Miserlou/django-easy-timezones)
([project website](https://www.gun.io/blog/django-easy-timezones))
is a [Django](/django.html) 
[middleware](https://docs.djangoproject.com/en/2.2/topics/http/middleware/)
[code library](https://pypi.org/project/django-easy-timezones/)
to simplify handling time data in your applications using
users' geolocation data.

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

