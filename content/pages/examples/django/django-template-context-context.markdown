title: django.template.context Context Example Code
category: page
slug: django-template-context-context-examples
sortorder: 500011382
toc: False
sidebartitle: django.template.context Context
meta: Example code for understanding how to use the Context class from the django.template.context module of the Django project.


`Context` is a class within the `django.template.context` module of the Django project.



## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / test_utils / testcases.py**](https://github.com/divio/django-cms/blob/develop/cms/test_utils/testcases.py)

```python
# testcases.py
import json
import sys
import warnings

from urllib.parse import unquote, urljoin

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser, Permission
from django.contrib.sites.models import Site
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.template import engines
~~from django.template.context import Context
from django.test import testcases
from django.test.client import RequestFactory
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.timezone import now
from django.utils.translation import activate
from menus.menu_pool import menu_pool

from cms.api import create_page
from cms.constants import (
    PUBLISHER_STATE_DEFAULT,
    PUBLISHER_STATE_DIRTY,
    PUBLISHER_STATE_PENDING,
)
from cms.plugin_rendering import ContentRenderer, StructureRenderer
from cms.models import Page
from cms.models.permissionmodels import (
    GlobalPagePermission,
    PagePermission,
    PageUser,
)
from cms.test_utils.util.context_managers import UserLoginContext
from cms.utils.conf import get_cms_setting
from cms.utils.permissions import set_current_user


## ... source file abbreviated to get to Context examples ...



    def create_homepage(self, *args, **kwargs):
        homepage = create_page(*args, **kwargs)
        homepage.set_as_homepage()
        return homepage.reload()

    def move_page(self, page, target_page, position="first-child"):
        page.move_page(target_page.node, position)
        return self.reload_page(page)

    def reload_page(self, page):
        return self.reload(page)

    def reload(self, obj):
        return obj.__class__.objects.get(pk=obj.pk)

    def get_pages_root(self):
        return unquote(reverse("pages-root"))

    def get_context(self, path=None, page=None):
        if not path:
            path = self.get_pages_root()
        context = {}
        request = self.get_request(path, page=page)
        context['request'] = request
~~        return Context(context)

    def get_content_renderer(self, request=None):
        request = request or self.get_request()
        return ContentRenderer(request)

    def get_structure_renderer(self, request=None):
        request = request or self.get_request()
        return StructureRenderer(request)

    def get_request(self, path=None, language=None, post_data=None, enforce_csrf_checks=False, page=None, domain=None):
        factory = RequestFactory()

        if not path:
            path = self.get_pages_root()

        if not language:
            if settings.USE_I18N:
                language = settings.LANGUAGES[0][0]
            else:
                language = settings.LANGUAGE_CODE

        if post_data:
            request = factory.post(path, post_data)
        else:


## ... source file continues with no further Context examples...

```


## Example 2 from django-sitetree
[django-sitetree](https://github.com/idlesign/django-sitetree)
([project documentation](https://django-sitetree.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-sitetree/))
is a [Django](/django.html) extension that makes it easier for
developers to add site trees, menus and breadcrumb navigation elements
to their web applications.

The django-sitetree project is provided as open source under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/idlesign/django-sitetree/blob/master/LICENSE).

[**django-sitetree / sitetree / sitetreeapp.py**](https://github.com/idlesign/django-sitetree/blob/master/sitetree/./sitetreeapp.py)

```python
# sitetreeapp.py
import warnings
from collections import defaultdict
from copy import deepcopy
from inspect import getfullargspec
from sys import exc_info
from threading import local
from typing import Callable, List, Optional, Dict, Union, Sequence, Any, Tuple

from django.conf import settings
from django.core.cache import caches
from django.db.models import signals, QuerySet
from django.template.base import (
    FilterExpression, Lexer, Parser, Variable, VariableDoesNotExist, VARIABLE_TAG_START)
~~from django.template.context import Context
from django.template.loader import get_template
from django.urls import reverse, NoReverseMatch
from django.utils import module_loading
from django.utils.encoding import iri_to_uri
from django.utils.translation import get_language

from .compat import TOKEN_TEXT, TOKEN_VAR
from .exceptions import SiteTreeError
from .settings import (
    ALIAS_TRUNK, ALIAS_THIS_CHILDREN, ALIAS_THIS_SIBLINGS, ALIAS_THIS_PARENT_SIBLINGS, ALIAS_THIS_ANCESTOR_CHILDREN,
    UNRESOLVED_ITEM_MARKER, RAISE_ITEMS_ERRORS_ON_DEBUG, CACHE_TIMEOUT, CACHE_NAME, DYNAMIC_ONLY, ADMIN_APP_NAME,
    SITETREE_CLS)
from .utils import get_tree_model, get_tree_item_model, import_app_sitetree_module, generate_id_for

if False:  # pragma: nocover
    from django.contrib.auth.models import User  # noqa
    from .models import TreeItemBase, TreeBase

TypeDynamicTrees = Dict[str, Union[Dict[str, List['TreeBase']], List['TreeBase']]]

MODEL_TREE_CLASS = get_tree_model()
MODEL_TREE_ITEM_CLASS = get_tree_item_model()




## ... source file continues with no further Context examples...

```

