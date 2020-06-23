title: django.contrib.admin.sites NotRegistered code examples
category: page
slug: django-contrib-admin-sites-notregistered-examples
sortorder: 500011026
toc: False
sidebartitle: django.contrib.admin.sites NotRegistered
meta: Python example code for the NotRegistered class from the django.contrib.admin.sites module of the Django project.


NotRegistered is a class within the django.contrib.admin.sites module of the Django project.


## Example 1 from django-sitetree
[django-sitetree](https://github.com/idlesign/django-sitetree)
([project documentation](https://django-sitetree.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-sitetree/))
is a [Django](/django.html) extension that makes it easier for
developers to add site trees, menus and breadcrumb navigation elements
to their web applications.

The django-sitetree project is provided as open source under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/idlesign/django-sitetree/blob/master/LICENSE).

[**django-sitetree / sitetree / admin.py**](https://github.com/idlesign/django-sitetree/blob/master/sitetree/./admin.py)

```python
# admin.py
from typing import Tuple, Type, Optional

from django import forms
from django.conf import settings as django_settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib import messages
~~from django.contrib.admin.sites import NotRegistered
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.urls import get_urlconf, get_resolver
from django.utils.translation import gettext_lazy as _

from .fields import TreeItemChoiceField
from .settings import MODEL_TREE, MODEL_TREE_ITEM
from .utils import get_tree_model, get_tree_item_model, get_app_n_model

if False:  # pragma: nocover
    from .models import TreeItemBase, TreeBase  # noqa


SMUGGLER_INSTALLED = 'smuggler' in django_settings.INSTALLED_APPS

MODEL_TREE_CLASS = get_tree_model()
MODEL_TREE_ITEM_CLASS = get_tree_item_model()

_TREE_ADMIN = lambda: TreeAdmin
_ITEM_ADMIN = lambda: TreeItemAdmin


def get_model_url_name(model_nfo: Tuple[str, str], page: str, with_namespace: bool = False) -> str:
    prefix = ''
    if with_namespace:


## ... source file continues with no further NotRegistered examples...

```

