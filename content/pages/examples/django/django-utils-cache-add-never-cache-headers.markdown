title: django.utils.cache add_never_cache_headers Example Code
category: page
slug: django-utils-cache-add-never-cache-headers-examples
sortorder: 500011424
toc: False
sidebartitle: django.utils.cache add_never_cache_headers
meta: Python example code for the add_never_cache_headers callable from the django.utils.cache module of the Django project.


add_never_cache_headers is a callable within the django.utils.cache module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / middleware / toolbar.py**](https://github.com/divio/django-cms/blob/develop/cms/middleware/toolbar.py)

```python
# toolbar.py
from django import forms
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE
from django.core.exceptions import ValidationError
from django.urls import resolve

from cms.toolbar.toolbar import CMSToolbar
from cms.toolbar.utils import get_toolbar_from_request
from cms.utils.conf import get_cms_setting
from cms.utils.compat.dj import MiddlewareMixin
from cms.utils.request_ip_resolvers import get_request_ip_resolver


get_request_ip = get_request_ip_resolver()


class ToolbarMiddleware(MiddlewareMixin):

    def is_cms_request(self, request):
        toolbar_hide = get_cms_setting('TOOLBAR_HIDE')
        internal_ips = get_cms_setting('INTERNAL_IPS')

        if internal_ips:
            client_ip = get_request_ip(request)
            try:
                client_ip = forms.GenericIPAddressField().clean(client_ip)
            except ValidationError:
                return False
            else:
                if client_ip not in internal_ips:
                    return False

        if not toolbar_hide:
            return True

        try:


## ... source file abbreviated to get to add_never_cache_headers examples ...



        if edit_enabled and show_toolbar and not request.session.get('cms_edit'):
            request.session['cms_edit'] = True
            request.session['cms_preview'] = False

        if edit_disabled or not show_toolbar and request.session.get('cms_edit'):
            request.session['cms_edit'] = False

        if 'preview' in request.GET and not request.session.get('cms_preview'):
            request.session['cms_preview'] = True

        if request.user.is_staff:
            try:
                request.cms_latest_entry = LogEntry.objects.filter(
                    user=request.user,
                    action_flag__in=(ADDITION, CHANGE)
                ).only('pk').order_by('-pk')[0].pk
            except IndexError:
                request.cms_latest_entry = -1
        request.toolbar = CMSToolbar(request)

    def process_response(self, request, response):
        if not self.is_cms_request(request):
            return response

~~        from django.utils.cache import add_never_cache_headers

        toolbar = get_toolbar_from_request(request)

        if toolbar._cache_disabled:
~~            add_never_cache_headers(response)

        if hasattr(request, 'user') and request.user.is_staff and response.status_code != 500:
            try:
                if hasattr(request, 'cms_latest_entry'):
                    pk = LogEntry.objects.filter(
                        user=request.user,
                        action_flag__in=(ADDITION, CHANGE)
                    ).only('pk').order_by('-pk')[0].pk

                    if request.cms_latest_entry != pk:
                        request.session['cms_log_latest'] = pk
            except IndexError:
                pass
        return response



## ... source file continues with no further add_never_cache_headers examples...

```

