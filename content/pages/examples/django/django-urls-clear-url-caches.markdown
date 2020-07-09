title: django.urls clear_url_caches Example Code
category: page
slug: django-urls-clear-url-caches-examples
sortorder: 500011402
toc: False
sidebartitle: django.urls clear_url_caches
meta: Python example code for the clear_url_caches callable from the django.urls module of the Django project.


clear_url_caches is a callable within the django.urls module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / signals / apphook.py**](https://github.com/divio/django-cms/blob/develop/cms/signals/apphook.py)

```python
# apphook.py
import logging
import sys

from django.core.management import color_style
from django.core.signals import request_finished
~~from django.urls import clear_url_caches

from cms.utils.apphook_reload import mark_urlconf_as_changed


logger = logging.getLogger(__name__)

DISPATCH_UID = 'cms-restart'


def trigger_server_restart(**kwargs):
    mark_urlconf_as_changed()


def set_restart_trigger():
    request_finished.connect(trigger_restart, dispatch_uid=DISPATCH_UID)


def trigger_restart(**kwargs):
    from cms.signals import urls_need_reloading

    request_finished.disconnect(trigger_restart, dispatch_uid=DISPATCH_UID)
    urls_need_reloading.send(sender=None)


def debug_server_restart(**kwargs):
    from cms.appresolver import clear_app_resolvers
    if 'runserver' in sys.argv or 'server' in sys.argv:
        clear_app_resolvers()
~~        clear_url_caches()
        import cms.urls
        try:
            reload(cms.urls)
        except NameError: #python3
            from imp import reload
            reload(cms.urls)
    if not 'test' in sys.argv:
        msg = 'Application url changed and urls_need_reloading signal fired. ' \
              'Please reload the urls.py or restart the server.\n'
        styles = color_style()
        msg = styles.NOTICE(msg)
        sys.stderr.write(msg)



## ... source file continues with no further clear_url_caches examples...

```

