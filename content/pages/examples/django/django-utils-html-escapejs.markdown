title: django.utils.html escapejs Example Code
category: page
slug: django-utils-html-escapejs-examples
sortorder: 500011463
toc: False
sidebartitle: django.utils.html escapejs
meta: Python example code for the escapejs callable from the django.utils.html module of the Django project.


escapejs is a callable within the django.utils.html module of the Django project.


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
~~from django.utils.html import escapejs
from django.utils.translation import ugettext, ugettext_lazy as _

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


## ... source file abbreviated to get to escapejs examples ...


    def render_close_frame(self, request, obj, extra_context=None):
        try:
            root = obj.parent.get_bound_plugin() if obj.parent else obj
        except ObjectDoesNotExist:
            root = obj

        plugins = [root] + list(root.get_descendants().order_by('path'))

        child_classes = self.get_child_classes(
            slot=obj.placeholder.slot,
            page=obj.page,
            instance=obj,
        )

        parent_classes = self.get_parent_classes(
            slot=obj.placeholder.slot,
            page=obj.page,
            instance=obj,
        )

        data = get_plugin_toolbar_info(
            obj,
            children=child_classes,
            parents=parent_classes,
        )
~~        data['plugin_desc'] = escapejs(force_text(obj.get_short_description()))

        context = {
            'plugin': obj,
            'is_popup': True,
            'plugin_data': json.dumps(data),
            'plugin_structure': get_plugin_tree_as_json(request, plugins),
        }

        if extra_context:
            context.update(extra_context)
        return render_to_response(
            request, 'admin/cms/page/plugin/confirm_form.html', context
        )

    def save_model(self, request, obj, form, change):
        pl_admin = obj.placeholder._get_attached_admin()

        if pl_admin:
            operation_kwargs = {
                'request': request,
                'placeholder': obj.placeholder,
            }

            if change:


## ... source file continues with no further escapejs examples...

```

