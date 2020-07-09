title: django.utils.translation activate Example Code
category: page
slug: django-utils-translation-activate-examples
sortorder: 500011499
toc: False
sidebartitle: django.utils.translation activate
meta: Python example code for the activate callable from the django.utils.translation module of the Django project.


activate is a callable within the django.utils.translation module of the Django project.


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


## ... source file abbreviated to get to activate examples ...


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
                slug = slugify(force_text(normalize_name(p.__class__.__name__)))
                url_patterns += [
                    url(r'^plugin/%s/' % (slug,), include(p.plugin_urls)),
                ]
        finally:
~~            activate(lang)

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
        plugin_classes = [cls for cls in self.registered_plugins
                          if cls._has_extra_placeholder_menu_items]
        return plugin_classes




## ... source file continues with no further activate examples...

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


## ... source file abbreviated to get to activate examples ...


    register_items_hook(None)  # Reset.


def test_i18n(build_tree, template_render_tag, template_context):

    from sitetree.toolbox import register_i18n_trees

    build_tree(
        {'alias': 'i18tree'},
        [{'title': 'My title', 'url': '/url_default/'}],
    )
    build_tree(
        {'alias': 'i18tree_ru'},
        [{'title': 'Заголовок', 'url': '/url_ru/'}],
    )
    build_tree(
        {'alias': 'i18tree_pt-br'},
        [{'title': 'Meu Título', 'url': '/url_pt-br/'}],
    )
    build_tree(
        {'alias': 'i18tree_zh-hans'},
        [{'title': '我蒂特', 'url': '/url_zh-hans/'}],
    )
    register_i18n_trees(['i18tree'])

~~    activate('en')
    result = template_render_tag('sitetree', 'sitetree_tree from "i18tree"', template_context())

    assert '/url_default/' in result
    assert 'My title' in result

~~    activate('ru')
    result = template_render_tag('sitetree', 'sitetree_tree from "i18tree"', template_context())

    assert '/url_ru/' in result
    assert 'Заголовок' in result

~~    activate('pt-br')
    result = template_render_tag('sitetree', 'sitetree_tree from "i18tree"', template_context())

    assert '/url_pt-br/' in result
    assert 'Meu Título' in result

~~    activate('zh-hans')
    result = template_render_tag('sitetree', 'sitetree_tree from "i18tree"', template_context())

    assert '/url_zh-hans/' in result
    assert '我蒂特' in result

    deactivate_all()


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



## ... source file continues with no further activate examples...

```

