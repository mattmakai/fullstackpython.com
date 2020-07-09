title: django.urls get_resolver Example Code
category: page
slug: django-urls-get-resolver-examples
sortorder: 500011404
toc: False
sidebartitle: django.urls get_resolver
meta: Python example code for the get_resolver callable from the django.urls module of the Django project.


get_resolver is a callable within the django.urls module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / utils / i18n.py**](https://github.com/divio/django-cms/blob/develop/cms/utils/i18n.py)

```python
# i18n.py
from contextlib import contextmanager

from django.conf import settings
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
~~from django.urls import get_resolver

from cms.exceptions import LanguageError
from cms.utils.compat.dj import LocalePrefixPattern
from cms.utils.conf import get_cms_setting, get_site_id


@contextmanager
def force_language(new_lang):
    old_lang = get_current_language()
    if old_lang != new_lang:
        translation.activate(new_lang)
    yield
    translation.activate(old_lang)


def get_languages(site_id=None):
    site_id = get_site_id(site_id)
    result = get_cms_setting('LANGUAGES').get(site_id)
    if not result:
        result = []
        defaults = get_cms_setting('LANGUAGES').get('default', {})
        for code, name in settings.LANGUAGES:
            lang = {'code': code, 'name': _(name)}
            lang.update(defaults)


## ... source file abbreviated to get to get_resolver examples ...



def get_fallback_languages(language, site_id=None):
    try:
        language = get_language_object(language, site_id)
    except LanguageError:
        language = get_languages(site_id)[0]
    return language.get('fallbacks', [])


def get_redirect_on_fallback(language, site_id=None):
    language = get_language_object(language, site_id)
    return language.get('redirect_on_fallback', True)


def hide_untranslated(language, site_id=None):
    obj = get_language_object(language, site_id)
    return obj.get('hide_untranslated', True)


def is_language_prefix_patterns_used():
    return any(
        isinstance(
            getattr(url_pattern, 'pattern', url_pattern),
            LocalePrefixPattern
        )
~~        for url_pattern in get_resolver(None).url_patterns
    )


def is_valid_site_language(language, site_id):
    return language in get_language_list(site_id)



## ... source file continues with no further get_resolver examples...

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

[**django-sitetree / sitetree / admin.py**](https://github.com/idlesign/django-sitetree/blob/master/sitetree/./admin.py)

```python
# admin.py
from typing import Tuple, Type, Optional

from django import forms
from django.conf import settings as django_settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib import messages
from django.contrib.admin.sites import NotRegistered
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
~~from django.urls import get_urlconf, get_resolver
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
        prefix = 'admin:'
    return (f'{prefix}%s_{page}' % '%s_%s' % model_nfo).lower()


## ... source file abbreviated to get to get_resolver examples ...


        elif '_continue' in request.POST:
            return response

        return HttpResponseRedirect('')

    def response_add(self, request, obj, post_url_continue=None, **kwargs):
        if post_url_continue is None:
            post_url_continue = f'../item_{obj.pk}/'

        return self._redirect(request, super().response_add(request, obj, post_url_continue))

    def response_change(self, request, obj, **kwargs):
        return self._redirect(request, super().response_change(request, obj))

    def get_form(self, request, obj=None, **kwargs):
        if obj is not None and obj.parent is not None:
            self.previous_parent = obj.parent

        form = super().get_form(request, obj, **kwargs)
        form.base_fields['parent'].choices_init(self.tree)

        if not getattr(self, 'known_url_names', False):
            self.known_url_names = []
            self.known_url_rules = []

~~            resolver = get_resolver(get_urlconf())

            for ns, (url_prefix, ns_resolver) in resolver.namespace_dict.items():
                if ns != 'admin':
                    self._stack_known_urls(ns_resolver.reverse_dict, ns)

            self._stack_known_urls(resolver.reverse_dict)
            self.known_url_rules = sorted(self.known_url_rules)

        form.known_url_names_hint = _(
            'You are seeing this warning because "URL as Pattern" option is active and pattern entered above '
            'seems to be invalid. Currently registered URL pattern names and parameters: ')

        form.known_url_names = self.known_url_names
        form.known_url_rules = self.known_url_rules

        return form

    def _stack_known_urls(self, reverse_dict, ns=None):
        for url_name, url_rules in reverse_dict.items():
            if isinstance(url_name, str):
                if ns is not None:
                    url_name = f'{ns}:{url_name}'
                self.known_url_names.append(url_name)
                self.known_url_rules.append(f"<b>{url_name}</b> {' '.join(url_rules[0][0][1])}")


## ... source file continues with no further get_resolver examples...

```

