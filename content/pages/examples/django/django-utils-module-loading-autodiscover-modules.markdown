title: django.utils.module_loading autodiscover_modules Example Code
category: page
slug: django-utils-module-loading-autodiscover-modules-examples
sortorder: 500011480
toc: False
sidebartitle: django.utils.module_loading autodiscover_modules
meta: Python example code for the autodiscover_modules callable from the django.utils.module_loading module of the Django project.


autodiscover_modules is a callable within the django.utils.module_loading module of the Django project.


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
~~from django.utils.module_loading import autodiscover_modules
from django.utils.translation import get_language, deactivate_all, activate
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
            del self.__dict__['plugins_with_extra_placeholder_menu']

    def discover_plugins(self):
        if self.discovered:
            return
        from cms.cache import invalidate_cms_page_cache

        if get_cms_setting("PAGE_CACHE"):
            invalidate_cms_page_cache()

~~        autodiscover_modules('cms_plugins')
        self.discovered = True

    def clear(self):
        self.discovered = False
        self.plugins = {}
        self._clear_cached()

    def validate_templates(self, plugin=None):
        if plugin:
            plugins = [plugin]
        else:
            plugins = self.plugins.values()
        for plugin in plugins:
            if (plugin.render_plugin and not type(plugin.render_plugin) == property
                    or hasattr(plugin.model, 'render_template')
                    or hasattr(plugin, 'get_render_template')):
                if (plugin.render_template is None and
                        not hasattr(plugin, 'get_render_template')):
                    raise ImproperlyConfigured(
                        "CMS Plugins must define a render template, "
                        "a get_render_template method or "
                        "set render_plugin=False: %s" % plugin
                    )
                elif not hasattr(plugin, 'get_render_template'):


## ... source file continues with no further autodiscover_modules examples...

```

