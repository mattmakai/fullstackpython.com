title: django.utils.html mark_safe Example Code
category: page
slug: django-utils-html-mark-safe-examples
sortorder: 500011466
toc: False
sidebartitle: django.utils.html mark_safe
meta: Python example code for the mark_safe callable from the django.utils.html module of the Django project.


mark_safe is a callable within the django.utils.html module of the Django project.


## Example 1 from django-rest-framework
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

[**django-rest-framework / rest_framework / renderers.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./renderers.py)

```python
# renderers.py
import base64
from collections import OrderedDict
from urllib import parse

from django import forms
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.paginator import Page
from django.http.multipartparser import parse_header
from django.template import engines, loader
from django.urls import NoReverseMatch
~~from django.utils.html import mark_safe

from rest_framework import VERSION, exceptions, serializers, status
from rest_framework.compat import (
    INDENT_SEPARATORS, LONG_SEPARATORS, SHORT_SEPARATORS, coreapi, coreschema,
    pygments_css, yaml
)
from rest_framework.exceptions import ParseError
from rest_framework.request import is_form_media_type, override_method
from rest_framework.settings import api_settings
from rest_framework.utils import encoders, json
from rest_framework.utils.breadcrumbs import get_breadcrumbs
from rest_framework.utils.field_mapping import ClassLookupDict


def zero_as_none(value):
    return None if value == 0 else value


class BaseRenderer:
    media_type = None
    format = None
    charset = 'utf-8'
    render_style = 'text'



## ... source file abbreviated to get to mark_safe examples ...


            template = loader.get_template(self.template)
            context = self.get_context(data, renderer_context['request'])
            return template.render(context, request=renderer_context['request'])
        else:
            template = loader.get_template(self.error_template)
            context = {
                "data": data,
                "request": renderer_context['request'],
                "response": renderer_context['response'],
                "debug": settings.DEBUG,
            }
            return template.render(context, request=renderer_context['request'])


class SchemaJSRenderer(BaseRenderer):
    media_type = 'application/javascript'
    format = 'javascript'
    charset = 'utf-8'
    template = 'rest_framework/schema.js'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        codec = coreapi.codecs.CoreJSONCodec()
        schema = base64.b64encode(codec.encode(data)).decode('ascii')

        template = loader.get_template(self.template)
~~        context = {'schema': mark_safe(schema)}
        request = renderer_context['request']
        return template.render(context, request=request)


class MultiPartRenderer(BaseRenderer):
    media_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'
    format = 'multipart'
    charset = 'utf-8'
    BOUNDARY = 'BoUnDaRyStRiNg'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        from django.test.client import encode_multipart

        if hasattr(data, 'items'):
            for key, value in data.items():
                assert not isinstance(value, dict), (
                    "Test data contained a dictionary value for key '%s', "
                    "but multipart uploads do not support nested data. "
                    "You may want to consider using format='json' in this "
                    "test case." % key
                )
        return encode_multipart(self.BOUNDARY, data)




## ... source file continues with no further mark_safe examples...

```


## Example 2 from django-tables2
[django-tables2](https://github.com/jieter/django-tables2)
([projection documentation](https://django-tables2.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-tables2/))
is a code library for [Django](/django.html) that simplifies creating and
displaying tables in [Django templates](/django-templates.html),
especially with more advanced features such as pagination and sorting.
The project and its code are
[available as open source](https://github.com/jieter/django-tables2/blob/master/LICENSE).

[**django-tables2 / django_tables2 / columns / manytomanycolumn.py**](https://github.com/jieter/django-tables2/blob/master/django_tables2/columns/manytomanycolumn.py)

```python
# manytomanycolumn.py
from django.db import models
from django.utils.encoding import force_str
~~from django.utils.html import conditional_escape, mark_safe

from .base import Column, LinkTransform, library


@library.register
class ManyToManyColumn(Column):

    def __init__(
        self, transform=None, filter=None, separator=", ", linkify_item=None, *args, **kwargs
    ):
        kwargs.setdefault("orderable", False)
        super().__init__(*args, **kwargs)

        if transform is not None:
            self.transform = transform
        if filter is not None:
            self.filter = filter
        self.separator = separator

        link_kwargs = None
        if callable(linkify_item):
            link_kwargs = dict(url=linkify_item)
        elif isinstance(linkify_item, (dict, tuple)):
            link_kwargs = dict(reverse_args=linkify_item)
        elif linkify_item is True:
            link_kwargs = dict()

        if link_kwargs is not None:
            self.linkify_item = LinkTransform(attrs=self.attrs.get("a", {}), **link_kwargs)

    def transform(self, obj):
        return force_str(obj)

    def filter(self, qs):
        return qs.all()

    def render(self, value):
        if not value.exists():
            return self.default

        items = []
        for item in self.filter(value):
            content = conditional_escape(self.transform(item))
            if hasattr(self, "linkify_item"):
                content = self.linkify_item(content=content, record=item)

            items.append(content)

~~        return mark_safe(conditional_escape(self.separator).join(items))

    @classmethod
    def from_field(cls, field, **kwargs):
        if isinstance(field, models.ManyToManyField):
            return cls(**kwargs)



## ... source file continues with no further mark_safe examples...

```


## Example 3 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / users / forms.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/users/forms.py)

```python
# forms.py
import warnings
from itertools import groupby
from operator import itemgetter

import l18n

from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.password_validation import (
    password_validators_help_text_html, validate_password)
from django.db import transaction
from django.db.models.fields import BLANK_CHOICE_DASH
from django.template.loader import render_to_string
~~from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _

from wagtail.admin.localization import get_available_admin_languages, get_available_admin_time_zones
from wagtail.admin.widgets import AdminPageChooser
from wagtail.core import hooks
from wagtail.core.models import (
    PAGE_PERMISSION_TYPE_CHOICES, PAGE_PERMISSION_TYPES, GroupPagePermission, Page,
    UserPagePermissionsProxy)
from wagtail.users.models import UserProfile

User = get_user_model()

standard_fields = set(['email', 'first_name', 'last_name', 'is_superuser', 'groups'])
if hasattr(settings, 'WAGTAIL_USER_CUSTOM_FIELDS'):
    custom_fields = set(settings.WAGTAIL_USER_CUSTOM_FIELDS)
else:
    custom_fields = set()


class UsernameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if User.USERNAME_FIELD == 'username':
            field = self.fields['username']


## ... source file abbreviated to get to mark_safe examples ...


    }

    email = forms.EmailField(required=True, label=_('Email'))
    first_name = forms.CharField(required=True, label=_('First Name'))
    last_name = forms.CharField(required=True, label=_('Last Name'))

    password1 = forms.CharField(
        label=_('Password'), required=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=_("Leave blank if not changing."))
    password2 = forms.CharField(
        label=_("Password confirmation"), required=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=_("Enter the same password as above, for verification."))

    is_superuser = forms.BooleanField(
        label=_("Administrator"), required=False,
        help_text=_('Administrators have full access to manage any object '
                    'or setting.'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.password_enabled:
            if self.password_required:
~~                self.fields['password1'].help_text = mark_safe(password_validators_help_text_html())
                self.fields['password1'].required = True
                self.fields['password2'].required = True
        else:
            del self.fields['password1']
            del self.fields['password2']

    def _clean_username(self):
        username_field = User.USERNAME_FIELD
        if username_field not in self.cleaned_data:
            return
        username = self.cleaned_data[username_field]

        users = User._default_manager.all()
        if self.instance.pk is not None:
            users = users.exclude(pk=self.instance.pk)
        if users.filter(**{username_field: username}).exists():
            self.add_error(User.USERNAME_FIELD, forms.ValidationError(
                self.error_messages['duplicate_username'],
                code='duplicate_username',
            ))
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")


## ... source file continues with no further mark_safe examples...

```

