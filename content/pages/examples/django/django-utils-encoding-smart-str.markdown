title: django.utils.encoding smart_str Example Code
category: page
slug: django-utils-encoding-smart-str-examples
sortorder: 500011448
toc: False
sidebartitle: django.utils.encoding smart_str
meta: Python example code for the smart_str callable from the django.utils.encoding module of the Django project.


smart_str is a callable within the django.utils.encoding module of the Django project.


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
~~from django.utils.encoding import force_text, smart_str
from django.utils.html import escapejs
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


## ... source file abbreviated to get to smart_str examples ...


    def get_parent_classes(cls, slot, page, instance=None):
        from cms.utils.placeholder import get_placeholder_conf

        template = page.get_template() if page else None

        ph_conf = get_placeholder_conf('parent_classes', slot, template, default={})
        parent_classes = ph_conf.get(cls.__name__, cls.parent_classes)
        return parent_classes

    def get_plugin_urls(self):
        return []

    def plugin_urls(self):
        return self.get_plugin_urls()
    plugin_urls = property(plugin_urls)

    @classmethod
    def get_extra_placeholder_menu_items(self, request, placeholder):
        pass

    @classmethod
    def get_extra_plugin_menu_items(cls, request, plugin):
        pass

    def __repr__(self):
~~        return smart_str(self.name)

    def __str__(self):
        return self.name


class PluginMenuItem(object):

    def __init__(self, name, url, data=None, question=None, action='ajax', attributes=None):
        if not attributes:
            attributes = {}

        if data:
            data = json.dumps(data)

        self.name = name
        self.url = url
        self.data = data
        self.question = question
        self.action = action
        self.attributes = attributes



## ... source file continues with no further smart_str examples...

```


## Example 2 from django-extensions
[django-extensions](https://github.com/django-extensions/django-extensions)
([project documentation](https://django-extensions.readthedocs.io/en/latest/)
and [PyPI page](https://pypi.org/project/django-extensions/))
is a [Django](/django.html) project that adds a bunch of additional
useful commands to the `manage.py` interface. This
[GoDjango video](https://www.youtube.com/watch?v=1F6G3ONhr4k) provides a
quick overview of what you get when you install it into your Python
environment.

The django-extensions project is open sourced under the
[MIT license](https://github.com/django-extensions/django-extensions/blob/master/LICENSE).

[**django-extensions / django_extensions / admin / __init__.py**](https://github.com/django-extensions/django-extensions/blob/master/django_extensions/admin/__init__.py)

```python
# __init__.py
import six
import operator
from functools import update_wrapper
from six.moves import reduce
from typing import Tuple, Dict, Callable  # NOQA

from django.apps import apps
from django.http import HttpResponse, HttpResponseNotFound
from django.conf import settings
from django.db import models
from django.db.models.query import QuerySet
~~from django.utils.encoding import smart_str
from django.utils.translation import gettext as _
from django.utils.text import get_text_list
from django.contrib import admin

from django_extensions.admin.widgets import ForeignKeySearchInput


class ForeignKeyAutocompleteAdminMixin:

    related_search_fields = {}  # type: Dict[str, Tuple[str]]
    related_string_functions = {}  # type: Dict[str, Callable]
    autocomplete_limit = getattr(settings, 'FOREIGNKEY_AUTOCOMPLETE_LIMIT', None)

    def get_urls(self):
        from django.urls import path

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        return [
            path('foreignkey_autocomplete/', wrap(self.foreignkey_autocomplete),
                name='%s_%s_autocomplete' % (self.model._meta.app_label, self.model._meta.model_name))


## ... source file abbreviated to get to smart_str examples ...


        search_fields = request.GET.get('search_fields', None)
        object_pk = request.GET.get('object_pk', None)

        try:
            to_string_function = self.related_string_functions[model_name]
        except KeyError:
            to_string_function = lambda x: x.__str__()

        if search_fields and app_label and model_name and (query or object_pk):
            def construct_search(field_name):
                if field_name.startswith('^'):
                    return "%s__istartswith" % field_name[1:]
                elif field_name.startswith('='):
                    return "%s__iexact" % field_name[1:]
                elif field_name.startswith('@'):
                    return "%s__search" % field_name[1:]
                else:
                    return "%s__icontains" % field_name

            model = apps.get_model(app_label, model_name)

            queryset = model._default_manager.all()
            data = ''
            if query:
                for bit in query.split():
~~                    or_queries = [models.Q(**{construct_search(smart_str(field_name)): smart_str(bit)}) for field_name in search_fields.split(',')]
                    other_qs = QuerySet(model)
                    other_qs.query.select_related = queryset.query.select_related
                    other_qs = other_qs.filter(reduce(operator.or_, or_queries))
                    queryset = queryset & other_qs

                additional_filter = self.get_related_filter(model, request)
                if additional_filter:
                    queryset = queryset.filter(additional_filter)

                if self.autocomplete_limit:
                    queryset = queryset[:self.autocomplete_limit]

                data = ''.join([six.u('%s|%s\n') % (to_string_function(f), f.pk) for f in queryset])
            elif object_pk:
                try:
                    obj = queryset.get(pk=object_pk)
                except Exception:  # FIXME: use stricter exception checking
                    pass
                else:
                    data = to_string_function(obj)
            return HttpResponse(data, content_type='text/plain')
        return HttpResponseNotFound()

    def get_related_filter(self, model, request):


## ... source file continues with no further smart_str examples...

```


## Example 3 from django-rest-framework
[Django REST Framework](https://github.com/encode/django-rest-framework)
([project homepage and documentation](https://www.django-rest-framework.org/),
[PyPI package information](https://pypi.org/project/djangorestframework/)
and [more resources on Full Stack Python](/django-rest-framework-drf.html)),
often abbreviated as "DRF", is a popular [Django](/django.html) extension
for building [web APIs](/application-programming-interfaces.html).
The project has fantastic documentation and a wonderful
[quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)
that serve as examples of how to make it easier for newcomers
to get started.

The project is open sourced under the
[Encode OSS Ltd. license](https://github.com/encode/django-rest-framework/blob/master/LICENSE.md).

[**django-rest-framework / rest_framework / fields.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./fields.py)

```python
# fields.py
import datetime
import decimal
import functools
import inspect
import re
import uuid
import warnings
from collections import OrderedDict
from collections.abc import Mapping

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.validators import (
    EmailValidator, MaxLengthValidator, MaxValueValidator, MinLengthValidator,
    MinValueValidator, ProhibitNullCharactersValidator, RegexValidator,
    URLValidator, ip_address_validators
)
from django.forms import FilePathField as DjangoFilePathField
from django.forms import ImageField as DjangoImageField
from django.utils import timezone
from django.utils.dateparse import (
    parse_date, parse_datetime, parse_duration, parse_time
)
from django.utils.duration import duration_string
~~from django.utils.encoding import is_protected_type, smart_str
from django.utils.formats import localize_input, sanitize_separators
from django.utils.ipv6 import clean_ipv6_address
from django.utils.timezone import utc
from django.utils.translation import gettext_lazy as _
from pytz.exceptions import InvalidTimeError

from rest_framework import (
    ISO_8601, RemovedInDRF313Warning, RemovedInDRF314Warning
)
from rest_framework.exceptions import ErrorDetail, ValidationError
from rest_framework.settings import api_settings
from rest_framework.utils import html, humanize_datetime, json, representation
from rest_framework.utils.formatting import lazy_format
from rest_framework.validators import ProhibitSurrogateCharactersValidator


class empty:
    pass


class BuiltinSignatureError(Exception):
    pass




## ... source file abbreviated to get to smart_str examples ...



        if self.max_digits is not None and self.decimal_places is not None:
            self.max_whole_digits = self.max_digits - self.decimal_places
        else:
            self.max_whole_digits = None

        super().__init__(**kwargs)

        if self.max_value is not None:
            message = lazy_format(self.error_messages['max_value'], max_value=self.max_value)
            self.validators.append(
                MaxValueValidator(self.max_value, message=message))
        if self.min_value is not None:
            message = lazy_format(self.error_messages['min_value'], min_value=self.min_value)
            self.validators.append(
                MinValueValidator(self.min_value, message=message))

        if rounding is not None:
            valid_roundings = [v for k, v in vars(decimal).items() if k.startswith('ROUND_')]
            assert rounding in valid_roundings, (
                'Invalid rounding option %s. Valid values for rounding are: %s' % (rounding, valid_roundings))
        self.rounding = rounding

    def to_internal_value(self, data):

~~        data = smart_str(data).strip()

        if self.localize:
            data = sanitize_separators(data)

        if len(data) > self.MAX_STRING_LENGTH:
            self.fail('max_string_length')

        try:
            value = decimal.Decimal(data)
        except decimal.DecimalException:
            self.fail('invalid')

        if value.is_nan():
            self.fail('invalid')

        if value in (decimal.Decimal('Inf'), decimal.Decimal('-Inf')):
            self.fail('invalid')

        return self.quantize(self.validate_precision(value))

    def validate_precision(self, value):
        sign, digittuple, exponent = value.as_tuple()

        if exponent >= 0:


## ... source file continues with no further smart_str examples...

```

