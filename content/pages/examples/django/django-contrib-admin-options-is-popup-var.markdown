title: django.contrib.admin.options IS_POPUP_VAR code examples
category: page
slug: django-contrib-admin-options-is-popup-var-examples
sortorder: 500011022
toc: False
sidebartitle: django.contrib.admin.options IS_POPUP_VAR
meta: Python example code for the IS_POPUP_VAR class from the django.contrib.admin.options module of the Django project.


IS_POPUP_VAR is a class within the django.contrib.admin.options module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / admin / pageadmin.py**](https://github.com/divio/django-cms/blob/develop/cms/admin/pageadmin.py)

```python
# pageadmin.py
from collections import namedtuple
import copy
import json
import sys
import uuid


import django
from django.contrib.admin.helpers import AdminForm
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin, messages
from django.contrib.admin.models import LogEntry, CHANGE
~~from django.contrib.admin.options import IS_POPUP_VAR
from django.contrib.admin.utils import get_deleted_objects
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.core.exceptions import (ObjectDoesNotExist,
                                    PermissionDenied, ValidationError)
from django.db import router, transaction
from django.db.models import Q, Prefetch
from django.http import (
    HttpResponseRedirect,
    HttpResponse,
    Http404,
    HttpResponseBadRequest,
    HttpResponseForbidden,
)
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import escape
from django.template.loader import get_template
from django.template.response import SimpleTemplateResponse, TemplateResponse
from django.utils.encoding import force_text
from django.utils.translation import ugettext, ugettext_lazy as _, get_language
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.http import QueryDict



## ... source file continues with no further IS_POPUP_VAR examples...

```


## Example 2 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / admin / tools.py**](https://github.com/divio/django-filer/blob/develop/filer/admin/tools.py)

```python
# tools.py
from __future__ import absolute_import, unicode_literals

~~from django.contrib.admin.options import IS_POPUP_VAR
from django.core.exceptions import PermissionDenied
from django.utils.http import urlencode


ALLOWED_PICK_TYPES = ('folder', 'file')


def check_files_edit_permissions(request, files):
    for f in files:
        if not f.has_edit_permission(request):
            raise PermissionDenied


def check_folder_edit_permissions(request, folders):
    for f in folders:
        if not f.has_edit_permission(request):
            raise PermissionDenied
        check_files_edit_permissions(request, f.files)
        check_folder_edit_permissions(request, f.children.all())


def check_files_read_permissions(request, files):
    for f in files:
        if not f.has_read_permission(request):


## ... source file abbreviated to get to IS_POPUP_VAR examples ...


    params = params or {}
    if popup_status(request):
        params[IS_POPUP_VAR] = '1'
    pick_type = popup_pick_type(request)
    if pick_type:
        params['_pick'] = pick_type
    return params


def admin_url_params_encoded(request, first_separator='?', params=None):
    params = urlencode(
        sorted(admin_url_params(request, params=params).items())
    )
    if not params:
        return ''
    return '{0}{1}'.format(first_separator, params)


class AdminContext(dict):
    def __init__(self, request):
        super(AdminContext, self).__init__()
        self.update(admin_url_params(request))

    def __missing__(self, key):
        if key == 'popup':
~~            return self.get(IS_POPUP_VAR, False) == '1'
        elif key == 'pick':
            return self.get('_pick', '')
        elif key.startswith('pick_'):
            return self.get('_pick', '') == key.split('pick_')[1]

    def __getattr__(self, name):
        if name in ('popup', 'pick') or name.startswith('pick_'):
            return self.get(name)
        raise AttributeError



## ... source file continues with no further IS_POPUP_VAR examples...

```

