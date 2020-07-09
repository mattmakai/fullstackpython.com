title: django.utils.translation ugettext Example Code
category: page
slug: django-utils-translation-ugettext-examples
sortorder: 500011509
toc: False
sidebartitle: django.utils.translation ugettext
meta: Python example code for the ugettext callable from the django.utils.translation module of the Django project.


ugettext is a callable within the django.utils.translation module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / plugin_base.py**](https://github.com/divio/django-cms/blob/develop/cms/./plugin_base.py)

```python
# plugin_base.py
import json
import re

from django.shortcuts import render as render_to_response

from django import forms
from django.contrib import admin
from django.contrib import messages
from django.core.exceptions import (
    ImproperlyConfigured,
    ObjectDoesNotExist,
    ValidationError,
)
from django.utils.encoding import force_text, smart_str
from django.utils.html import escapejs
~~from django.utils.translation import ugettext, ugettext_lazy as _

from six import with_metaclass, python_2_unicode_compatible

from cms import operations
from cms.exceptions import SubClassNeededError
from cms.models import CMSPlugin
from cms.toolbar.utils import get_plugin_tree_as_json, get_plugin_toolbar_info
from cms.utils.conf import get_cms_setting


class CMSPluginBaseMetaclass(forms.MediaDefiningClass):
    def __new__(cls, name, bases, attrs):
        super_new = super(CMSPluginBaseMetaclass, cls).__new__
        parents = [base for base in bases if isinstance(base, CMSPluginBaseMetaclass)]
        if not parents:
            return super_new(cls, name, bases, attrs)
        new_plugin = super_new(cls, name, bases, attrs)
        if not issubclass(new_plugin.model, CMSPlugin):
            raise SubClassNeededError(
                "The 'model' attribute on CMSPluginBase subclasses must be "
                "either CMSPlugin or a subclass of CMSPlugin. %r on %r is not."
                % (new_plugin.model, new_plugin)
            )
        if (not hasattr(new_plugin, 'render_template') and


## ... source file abbreviated to get to ugettext examples ...



    def icon_src(self, instance):
        return ""

    def icon_alt(self, instance):
        return "%s - %s" % (force_text(self.name), force_text(instance))

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(CMSPluginBase, self).get_fieldsets(request, obj)

        for name, data in fieldsets:
            if data.get('fields'):  # if fieldset with non-empty fields is found, return fieldsets
                return fieldsets

        if self.inlines:
            return []  # if plugin has inlines but no own fields return empty fieldsets to remove empty white fieldset

        try:  # if all fieldsets are empty (assuming there is only one fieldset then) add description
            fieldsets[0][1]['description'] = self.get_empty_change_form_text(obj=obj)
        except KeyError:
            pass
        return fieldsets

    @classmethod
    def get_empty_change_form_text(cls, obj=None):
~~        return ugettext('There are no further settings for this plugin. Please press save.')

    @classmethod
    def get_child_class_overrides(cls, slot, page):
        from cms.utils.placeholder import get_placeholder_conf

        template = page.get_template() if page else None

        ph_conf = get_placeholder_conf('child_classes', slot, template, default={})
        return ph_conf.get(cls.__name__, cls.child_classes)

    @classmethod
    def get_child_plugin_candidates(cls, slot, page):
        from cms.plugin_pool import plugin_pool
        return plugin_pool.registered_plugins

    @classmethod
    def get_child_classes(cls, slot, page, instance=None):
        child_classes = cls.get_child_class_overrides(slot, page)

        if child_classes:
            return child_classes

        installed_plugins = cls.get_child_plugin_candidates(slot, page)



## ... source file continues with no further ugettext examples...

```

