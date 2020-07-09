title: django.utils.translation deactivate_all Example Code
category: page
slug: django-utils-translation-deactivate-all-examples
sortorder: 500011500
toc: False
sidebartitle: django.utils.translation deactivate_all
meta: Python example code for the deactivate_all callable from the django.utils.translation module of the Django project.


deactivate_all is a callable within the django.utils.translation module of the Django project.


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


## ... source file abbreviated to get to deactivate_all examples ...


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

        lang = get_language()
~~        deactivate_all()

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
    def plugins_with_extra_menu(self):


## ... source file continues with no further deactivate_all examples...

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

[**django-sitetree / sitetree / tests / test_templatetags.py**](https://github.com/idlesign/django-sitetree/blob/master/sitetree/tests/test_templatetags.py)

```python
# test_templatetags.py
import pytest
from django.template.base import TemplateSyntaxError
~~from django.utils.translation import activate, deactivate_all

from sitetree.exceptions import SiteTreeError
from sitetree.settings import ALIAS_THIS_ANCESTOR_CHILDREN, ALIAS_THIS_CHILDREN, ALIAS_THIS_PARENT_SIBLINGS, \
    ALIAS_THIS_SIBLINGS, ALIAS_TRUNK


def test_items_hook(template_render_tag, template_context, common_tree):

    from sitetree.toolbox import register_items_hook

    with pytest.raises(SiteTreeError):
        register_items_hook(lambda: [])

    def my_processor(tree_items, tree_sender):
        for item in tree_items:
            item.hint = f'hooked_hint_{item.title}'
        return tree_items

    register_items_hook(my_processor)
    result = template_render_tag('sitetree', 'sitetree_tree from "mytree"', template_context())

    assert 'hooked_hint_Darwin' in result
    assert 'hooked_hint_Australia' in result
    assert 'hooked_hint_China' in result


## ... source file abbreviated to get to deactivate_all examples ...



    activate('en')
    result = template_render_tag('sitetree', 'sitetree_tree from "i18tree"', template_context())

    assert '/url_default/' in result
    assert 'My title' in result

    activate('ru')
    result = template_render_tag('sitetree', 'sitetree_tree from "i18tree"', template_context())

    assert '/url_ru/' in result
    assert 'Заголовок' in result

    activate('pt-br')
    result = template_render_tag('sitetree', 'sitetree_tree from "i18tree"', template_context())

    assert '/url_pt-br/' in result
    assert 'Meu Título' in result

    activate('zh-hans')
    result = template_render_tag('sitetree', 'sitetree_tree from "i18tree"', template_context())

    assert '/url_zh-hans/' in result
    assert '我蒂特' in result

~~    deactivate_all()


def test_restricted(user_create, template_render_tag, template_context, common_tree):
    context = template_context()
    result = template_render_tag('sitetree', 'sitetree_tree from "mytree"', context)

    assert '"/contacts/australia/darwin/"' in result
    assert '"/contacts/australia/alice/"' not in result

    context = template_context(user=user_create())
    result = template_render_tag('sitetree', 'sitetree_tree from "mytree"', context)

    assert '"/contacts/australia/darwin/"' not in result
    assert '"/contacts/australia/alice/"' in result


def test_permissions(user_create, build_tree, template_render_tag, template_context):

    from sitetree.models import TreeItem

    build_tree(
        {'alias': 'restricted_tree'},
        [
            {'title': 'Minjilang', 'access_restricted': True, 'url': '/contacts/australia/minjilang/'},


## ... source file continues with no further deactivate_all examples...

```

