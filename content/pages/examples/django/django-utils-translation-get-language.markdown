title: django.utils.translation get_language Example Code
category: page
slug: django-utils-translation-get-language-examples
sortorder: 500011501
toc: False
sidebartitle: django.utils.translation get_language
meta: Python example code for the get_language callable from the django.utils.translation module of the Django project.


get_language is a callable within the django.utils.translation module of the Django project.


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
from django.conf.urls import url, include
from django.template.defaultfilters import slugify
from django.utils.encoding import force_text
from django.utils.functional import cached_property
from django.utils.module_loading import autodiscover_modules
~~from django.utils.translation import get_language, deactivate_all, activate
from django.template import TemplateDoesNotExist, TemplateSyntaxError

from six import string_types, text_type

from cms.exceptions import PluginAlreadyRegistered, PluginNotRegistered
from cms.plugin_base import CMSPluginBase
from cms.utils.conf import get_cms_setting
from cms.utils.helpers import normalize_name


class PluginPool(object):

    def __init__(self):
        self.plugins = {}
        self.discovered = False

    def _clear_cached(self):
        if 'registered_plugins' in self.__dict__:
            del self.__dict__['registered_plugins']

        if 'plugins_with_extra_menu' in self.__dict__:
            del self.__dict__['plugins_with_extra_menu']

        if 'plugins_with_extra_placeholder_menu' in self.__dict__:


## ... source file abbreviated to get to get_language examples ...



        if allowed_plugins:
            plugins = (plugin for plugin in plugins if plugin.__name__ in allowed_plugins)

        if excluded_plugins:
            plugins = (plugin for plugin in plugins if plugin.__name__ not in excluded_plugins)

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

~~        lang = get_language()
        deactivate_all()

        try:
            url_patterns = []
            for plugin in self.registered_plugins:
                p = plugin()
                slug = slugify(force_text(normalize_name(p.__class__.__name__)))
                url_patterns += [
                    url(r'^plugin/%s/' % (slug,), include(p.plugin_urls)),
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


## ... source file continues with no further get_language examples...

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
from django.core.cache import cache
from django.db.models import signals, QuerySet
from django.template.base import (
    FilterExpression, Lexer, Parser, Token, Variable, VariableDoesNotExist, VARIABLE_TAG_START, Context)
from django.template.defaulttags import url as url_tag
from django.template.loader import get_template
from django.utils import module_loading
from django.utils.http import urlquote
~~from django.utils.translation import get_language

from .compat import TOKEN_BLOCK, TOKEN_TEXT, TOKEN_VAR
from .exceptions import SiteTreeError
from .settings import (
    ALIAS_TRUNK, ALIAS_THIS_CHILDREN, ALIAS_THIS_SIBLINGS, ALIAS_THIS_PARENT_SIBLINGS, ALIAS_THIS_ANCESTOR_CHILDREN,
    UNRESOLVED_ITEM_MARKER, RAISE_ITEMS_ERRORS_ON_DEBUG, CACHE_TIMEOUT, DYNAMIC_ONLY, ADMIN_APP_NAME, SITETREE_CLS)
from .utils import get_tree_model, get_tree_item_model, import_app_sitetree_module, generate_id_for

if False:  # pragma: nocover
    from django.contrib.auth.models import User  # noqa
    from .models import TreeItemBase, TreeBase

TypeDynamicTrees = Dict[str, Union[Dict[str, List['TreeBase']], List['TreeBase']]]

MODEL_TREE_CLASS = get_tree_model()
MODEL_TREE_ITEM_CLASS = get_tree_item_model()


_ITEMS_PROCESSOR: Optional[Callable] = None

_ITEMS_PROCESSOR_ARGS_LEN: int = 0

_I18N_TREES: List[str] = []



## ... source file abbreviated to get to get_language examples ...



    def get_entry(self, entry_name: str, key) -> Any:
        return self.cache[entry_name].get(key, False)

    def update_entry_value(self, entry_name: str, key: str, value: Any):
        if key not in self.cache[entry_name]:
            self.cache[entry_name][key] = {}

        self.cache[entry_name][key].update(value)

    def set_entry(self, entry_name: str, key: str, value: Any):
        self.cache[entry_name][key] = value


class SiteTree:

    cache_cls = Cache  # Allow customizations.

    def __init__(self):
        self.init(context=None)

    def init(self, context: Optional[Context]):
        self.cache = self.cache_cls()
        self.current_page_context = context
        self.current_request = context.get('request', None) if context else None
~~        self.current_lang = get_language()

        self._current_app_is_admin = None
        self._current_user_permissions = _UNSET
        self._items_urls = {}  # Resolved urls are cache for a request.
        self._current_items = {}

    def resolve_tree_i18n_alias(self, alias: str) -> str:
        if alias not in _I18N_TREES:
            return alias

        current_language_code = self.current_lang
        i18n_tree_alias = f'{alias}_{current_language_code}'
        trees_count = self.cache.get_entry('tree_aliases', i18n_tree_alias)

        if trees_count is False:
            trees_count = MODEL_TREE_CLASS.objects.filter(alias=i18n_tree_alias).count()
            self.cache.set_entry('tree_aliases', i18n_tree_alias, trees_count)

        if trees_count:
            alias = i18n_tree_alias

        return alias

    @staticmethod


## ... source file continues with no further get_language examples...

```


## Example 3 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / users / models.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/users/models.py)

```python
# models.py
import os
import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
~~from django.utils.translation import get_language


def upload_avatar_to(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'avatar_images',
        'avatar_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wagtail_userprofile'
    )

    submitted_notifications = models.BooleanField(
        verbose_name=_('submitted notifications'),
        default=True,
        help_text=_("Receive notification when a page is submitted for moderation")
    )

    approved_notifications = models.BooleanField(
        verbose_name=_('approved notifications'),


## ... source file abbreviated to get to get_language examples ...


    preferred_language = models.CharField(
        verbose_name=_('preferred language'),
        max_length=10,
        help_text=_("Select language for the admin"),
        default=''
    )

    current_time_zone = models.CharField(
        verbose_name=_('current time zone'),
        max_length=40,
        help_text=_("Select your current time zone"),
        default=''
    )

    avatar = models.ImageField(
        verbose_name=_('profile picture'),
        upload_to=upload_avatar_to,
        blank=True,
    )

    @classmethod
    def get_for_user(cls, user):
        return cls.objects.get_or_create(user=user)[0]

    def get_preferred_language(self):
~~        return self.preferred_language or get_language()

    def get_current_time_zone(self):
        return self.current_time_zone or settings.TIME_ZONE

    def __str__(self):
        return self.user.get_username()

    class Meta:
        verbose_name = _('user profile')
        verbose_name_plural = _('user profiles')



## ... source file continues with no further get_language examples...

```

