title: django.core.exceptions ValidationError Example Code
category: page
slug: django-core-exceptions-validationerror-examples
sortorder: 500011108
toc: False
sidebartitle: django.core.exceptions ValidationError
meta: Python example code for the ValidationError class from the django.core.exceptions module of the Django project.


ValidationError is a class within the django.core.exceptions module of the Django project.


## Example 1 from AuditLog
[Auditlog](https://github.com/jjkester/django-auditlog)
([project documentation](https://django-auditlog.readthedocs.io/en/latest/))
is a [Django](/django.html) app that logs changes to Python objects,
similar to the Django admin's logs but with more details and
output formats. Auditlog's source code is provided as open source under the
[MIT license](https://github.com/jjkester/django-auditlog/blob/master/LICENSE).

[**AuditLog / src / auditlog_tests / tests.py**](https://github.com/jjkester/django-auditlog/blob/master/src/auditlog_tests/tests.py)

```python
# tests.py
import datetime
import django
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User, AnonymousUser
~~from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.http import HttpResponse
from django.test import TestCase, RequestFactory
from django.utils import dateformat, formats, timezone
from dateutil.tz import gettz

from auditlog.middleware import AuditlogMiddleware
from auditlog.models import LogEntry
from auditlog.registry import auditlog
from auditlog_tests.models import SimpleModel, AltPrimaryKeyModel, UUIDPrimaryKeyModel, \
    ProxyModel, SimpleIncludeModel, SimpleExcludeModel, SimpleMappingModel, RelatedModel, \
    ManyRelatedModel, AdditionalDataIncludedModel, DateTimeFieldModel, ChoicesFieldModel, \
    CharfieldTextfieldModel, PostgresArrayFieldModel, NoDeleteHistoryModel
from auditlog import compat


class SimpleModelTest(TestCase):
    def setUp(self):
        self.obj = SimpleModel.objects.create(text='I am not difficult.')

    def test_create(self):
        obj = self.obj

        self.assertTrue(obj.history.count() == 1, msg="There is one log entry")


## ... source file abbreviated to get to ValidationError examples ...


    def test_request(self):
        request = self.factory.get('/')
        request.user = self.user
        self.middleware.process_request(request)

        self.assertTrue(pre_save.has_listeners(LogEntry))

        self.middleware.process_exception(request, None)

    def test_response(self):
        request = self.factory.get('/')
        request.user = self.user

        self.middleware.process_request(request)
        self.assertTrue(pre_save.has_listeners(LogEntry))  # The signal should be present before trying to disconnect it.
        self.middleware.process_response(request, HttpResponse())

        self.assertFalse(pre_save.has_listeners(LogEntry))

    def test_exception(self):
        request = self.factory.get('/')
        request.user = self.user

        self.middleware.process_request(request)
        self.assertTrue(pre_save.has_listeners(LogEntry))  # The signal should be present before trying to disconnect it.
~~        self.middleware.process_exception(request, ValidationError("Test"))

        self.assertFalse(pre_save.has_listeners(LogEntry))


class SimpeIncludeModelTest(TestCase):

    def test_register_include_fields(self):
        sim = SimpleIncludeModel(label='Include model', text='Looong text')
        sim.save()
        self.assertTrue(sim.history.count() == 1, msg="There is one log entry")

        sim.label = 'Changed label'
        sim.save()
        self.assertTrue(sim.history.count() == 2, msg="There are two log entries")

        sim.text = 'Short text'
        sim.save()
        self.assertTrue(sim.history.count() == 2, msg="There are two log entries")


class SimpeExcludeModelTest(TestCase):

    def test_register_exclude_fields(self):
        sem = SimpleExcludeModel(label='Exclude model', text='Looong text')


## ... source file continues with no further ValidationError examples...

```


## Example 2 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / chair_mail / forms.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/chair_mail/forms.py)

```python
# forms.py
from django import forms
from django.conf import settings
~~from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.template import Template, Context
from django.utils import timezone
from html2text import html2text
from markdown import markdown

from chair_mail.context import get_conference_context, get_user_context, \
    get_submission_context
from chair_mail.mailing_lists import find_list
from chair_mail.utility import get_object_model
from submissions.models import Submission
from users.models import User
from .models import EmailFrame, MSG_TYPE_USER, MSG_TYPE_SUBMISSION, \
    SystemNotification


def parse_mailing_lists(names_string, separator=','):
    names = names_string.split(separator)
    names = [name for name in names if name.strip()]
    return [find_list(name) for name in names]


def parse_objects(obj_class, pks_string, separator=','):
    int_pks = [s for s in pks_string.split(separator) if s.strip()]


## ... source file abbreviated to get to ValidationError examples ...


            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            html_message=html,
        )


class MessageForm(forms.Form):
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea(), required=False)
    lists = forms.CharField(
        required=False, max_length=1000, widget=forms.HiddenInput)
    objects = forms.CharField(
        required=False, max_length=10000, widget=forms.HiddenInput)

    def __init__(self, *args, msg_type=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.msg_type = msg_type
        self.object_type = get_object_model(msg_type)
        self.cleaned_lists = []
        self.cleaned_objects = []

    def clean_lists(self):
        _lists = parse_mailing_lists(self.cleaned_data['lists'])
        for ml in _lists:
            if ml.type != self.msg_type:
~~                raise ValidationError(
                    f'unexpected {ml.type} mailing list {ml.name}')
        self.cleaned_lists = _lists
        return self.cleaned_data['lists']

    def clean_objects(self):
        self.cleaned_objects = parse_objects(
            self.object_type, self.cleaned_data['objects'], ',')
        return self.cleaned_data['objects']

    def clean(self):
        if not self.cleaned_lists and not self.cleaned_objects:
~~            raise ValidationError('You must specify at least one recipient')
        return self.cleaned_data


class PreviewMessageForm(forms.Form):
    subject = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'hidden': True
        })
    )

    body = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'hidden': True
        })
    )

    def get_context(self, conference):
        raise NotImplementedError

    def render_html(self, conference):
        ctx_data = self.get_context(conference)
        context = Context(ctx_data, autoescape=False)


## ... source file continues with no further ValidationError examples...

```


## Example 3 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / socialaccount / fields.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/socialaccount/fields.py)

```python
# fields.py
import json

import django
~~from django.core.exceptions import ValidationError
from django.db import models


class JSONField(models.TextField):
    if django.VERSION < (3, 0):
        def from_db_value(self, value, expression, connection, context):
            return self.to_python(value)
    else:
        def from_db_value(self, value, expression, connection):
            return self.to_python(value)

    def to_python(self, value):
        if self.blank and not value:
            return None
        if isinstance(value, str):
            try:
                return json.loads(value)
            except Exception as e:
~~                raise ValidationError(str(e))
        else:
            return value

    def validate(self, value, model_instance):
        if isinstance(value, str):
            super(JSONField, self).validate(value, model_instance)
            try:
                json.loads(value)
            except Exception as e:
~~                raise ValidationError(str(e))

    def get_prep_value(self, value):
        try:
            return json.dumps(value)
        except Exception as e:
~~            raise ValidationError(str(e))

    def value_from_object(self, obj):
        val = super(JSONField, self).value_from_object(obj)
        return self.get_prep_value(val)



## ... source file continues with no further ValidationError examples...

```


## Example 4 from django-angular
[django-angular](https://github.com/jrief/django-angular)
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / forms / angular_base.py**](https://github.com/jrief/django-angular/blob/master/djng/forms/angular_base.py)

```python
# angular_base.py
from base64 import b64encode
from collections import UserList
import json
import warnings

from django.forms import forms
from django.http import QueryDict
from django.utils.html import format_html, format_html_join, escape, conditional_escape
from django.utils.encoding import force_text
from django.utils.module_loading import import_string
from django.utils.safestring import mark_safe, SafeText, SafeData
~~from django.core.exceptions import ValidationError, ImproperlyConfigured

from .fields import DefaultFieldMixin


class SafeTuple(SafeData, tuple):


class TupleErrorList(UserList, list):
    def __init__(self, initlist=None, error_class=None):
        super(TupleErrorList, self).__init__(initlist)

        if error_class is None:
            self.error_class = 'errorlist'
        else:
            self.error_class = 'errorlist {}'.format(error_class)

    def as_data(self):
~~        return ValidationError(self.data).error_list

    def get_json_data(self, escape_html=False):
        errors = []
        for error in self.as_data():
            message = list(error)[0]
            errors.append({
                'message': escape(message) if escape_html else message,
                'code': error.code or '',
            })
        return errors

    def as_json(self, escape_html=False):
        return json.dumps(self.get_json_data(escape_html))

    def extend(self, iterable):
        for item in iterable:
            if not isinstance(item, str):
                self.append(item)
        return None

    def as_ul(self):
        if not self:
            return SafeText()
        first = self[0]


## ... source file abbreviated to get to ValidationError examples ...


            return ''
        if isinstance(self[0], tuple):
            return '\n'.join(['* %s' % force_text(e[5]) for e in self if bool(e[5])])
        return '\n'.join(['* %s' % force_text(e) for e in self])

    def __str__(self):
        return self.as_ul()

    def __repr__(self):
        if self and isinstance(self[0], tuple):
            return repr([force_text(e[5]) for e in self])
        return repr([force_text(e) for e in self])

    def __contains__(self, item):
        return item in list(self)

    def __eq__(self, other):
        return list(self) == other

    def __ne__(self, other):
        return list(self) != other

    def __getitem__(self, i):
        error = self.data[i]
        if isinstance(error, tuple):
~~            if isinstance(error[5], ValidationError):
                error[5] = list(error[5])[0]
            return error
~~        if isinstance(error, ValidationError):
            return list(error)[0]
        return force_text(error)


class NgWidgetMixin(object):
    def get_context(self, name, value, attrs):
        context = super(NgWidgetMixin, self).get_context(name, value, attrs)
        if callable(getattr(self._field, 'update_widget_rendering_context', None)):
            self._field.update_widget_rendering_context(context)
        return context


class NgBoundField(forms.BoundField):
    @property
    def errors(self):
        if not hasattr(self, '_errors_cache'):
            self._errors_cache = self.form.get_field_errors(self)
        return self._errors_cache

    def css_classes(self, extra_classes=None):
        if hasattr(extra_classes, 'split'):
            extra_classes = extra_classes.split()
        extra_classes = set(extra_classes or [])
        field_css_classes = getattr(self.form, 'field_css_classes', None)


## ... source file continues with no further ValidationError examples...

```


## Example 5 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / api.py**](https://github.com/divio/django-cms/blob/develop/cms/./api.py)

```python
# api.py
import datetime

from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core.exceptions import FieldError
from django.core.exceptions import PermissionDenied
~~from django.core.exceptions import ValidationError
from django.db import transaction
from django.template.defaultfilters import slugify
from django.template.loader import get_template
from django.utils.translation import activate

from six import string_types

from cms import constants
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from cms.constants import TEMPLATE_INHERITANCE_MAGIC
from cms.models.pagemodel import Page
from cms.models.permissionmodels import (PageUser, PagePermission, GlobalPagePermission,
                                         ACCESS_PAGE_AND_DESCENDANTS)
from cms.models.placeholdermodel import Placeholder
from cms.models.pluginmodel import CMSPlugin
from cms.models.titlemodels import Title
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.utils import copy_plugins, get_current_site
from cms.utils.conf import get_cms_setting
from cms.utils.i18n import get_language_list
from cms.utils.page import get_available_slug
from cms.utils.permissions import _thread_locals, current_user


## ... source file abbreviated to get to ValidationError examples ...






def _verify_apphook(apphook, namespace):
    apphook_pool.discover_apps()
    if isinstance(apphook, CMSApp):
        try:
            assert apphook.__class__ in [app.__class__ for app in apphook_pool.apps.values()]
        except AssertionError:
            print(apphook_pool.apps.values())
            raise
        apphook_name = apphook.__class__.__name__
    elif hasattr(apphook, '__module__') and issubclass(apphook, CMSApp):
        return apphook.__name__
    elif isinstance(apphook, string_types):
        try:
            assert apphook in apphook_pool.apps
        except AssertionError:
            print(apphook_pool.apps.values())
            raise
        apphook_name = apphook
    else:
        raise TypeError("apphook must be string or CMSApp instance")
    if apphook_pool.apps[apphook_name].app_name and not namespace:
~~        raise ValidationError('apphook with app_name must define a namespace')
    return apphook_name


def _verify_plugin_type(plugin_type):
    if (hasattr(plugin_type, '__module__') and
            issubclass(plugin_type, CMSPluginBase)):
        plugin_model = plugin_type.model
        assert plugin_type in plugin_pool.plugins.values()
        plugin_type = plugin_type.__name__
    elif isinstance(plugin_type, string_types):
        try:
            plugin_model = plugin_pool.get_plugin(plugin_type).model
        except KeyError:
            raise TypeError(
                'plugin_type must be CMSPluginBase subclass or string'
            )
    else:
        raise TypeError('plugin_type must be CMSPluginBase subclass or string')
    return plugin_model, plugin_type



@transaction.atomic
def create_page(title, template, language, menu_title=None, slug=None,


## ... source file continues with no further ValidationError examples...

```


## Example 6 from django-extensions
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

[**django-extensions / django_extensions / validators.py**](https://github.com/django-extensions/django-extensions/blob/master/django_extensions/./validators.py)

```python
# validators.py
import unicodedata
import binascii


~~from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _


@deconstructible
class NoControlCharactersValidator:
    message = _("Control Characters like new lines or tabs are not allowed.")
    code = "no_control_characters"
    whitelist = None

    def __init__(self, message=None, code=None, whitelist=None):
        if message:
            self.message = message
        if code:
            self.code = code
        if whitelist:
            self.whitelist = whitelist

    def __call__(self, value):
        value = force_str(value)
        whitelist = self.whitelist
        category = unicodedata.category
        for character in value:
            if whitelist and character in whitelist:
                continue
            if category(character)[0] == "C":
                params = {'value': value, 'whitelist': whitelist}
~~                raise ValidationError(self.message, code=self.code, params=params)

    def __eq__(self, other):
        return (
            isinstance(other, NoControlCharactersValidator) and
            (self.whitelist == other.whitelist) and
            (self.message == other.message) and
            (self.code == other.code)
        )


@deconstructible
class NoWhitespaceValidator:
    message = _("Leading and Trailing whitespaces are not allowed.")
    code = "no_whitespace"

    def __init__(self, message=None, code=None, whitelist=None):
        if message:
            self.message = message
        if code:
            self.code = code

    def __call__(self, value):
        value = force_str(value)
        if value != value.strip():
            params = {'value': value}
~~            raise ValidationError(self.message, code=self.code, params=params)

    def __eq__(self, other):
        return (
            isinstance(other, NoWhitespaceValidator) and
            (self.message == other.message) and
            (self.code == other.code)
        )


@deconstructible
class HexValidator:
    messages = {
        'invalid': _("Only a hex string is allowed."),
        'length': _("Invalid length. Must be %(length)d characters."),
        'min_length': _("Ensure that there are more than %(min)s characters."),
        'max_length': _("Ensure that there are no more than %(max)s characters."),
    }
    code = "hex_only"

    def __init__(self, length=None, min_length=None, max_length=None, message=None, code=None):
        self.length = length
        self.min_length = min_length
        self.max_length = max_length
        if message:
            self.message = message
        if code:
            self.code = code

    def __call__(self, value):
        value = force_str(value)
        if self.length and len(value) != self.length:
~~            raise ValidationError(self.messages['length'], code='hex_only_length', params={'length': self.length})
        if self.min_length and len(value) < self.min_length:
~~            raise ValidationError(self.messages['min_length'], code='hex_only_min_length', params={'min': self.min_length})
        if self.max_length and len(value) < self.max_length:
~~            raise ValidationError(self.messages['max_length'], code='hex_only_max_length', params={'max': self.max_length})

        try:
            binascii.unhexlify(value)
        except (TypeError, binascii.Error):
~~            raise ValidationError(self.messages['invalid'], code='hex_only')

    def __eq__(self, other):
        return (
            isinstance(other, HexValidator) and
            (self.message == other.message) and
            (self.code == other.code)
        )



## ... source file continues with no further ValidationError examples...

```


## Example 7 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / admin / forms.py**](https://github.com/divio/django-filer/blob/develop/filer/admin/forms.py)

```python
# forms.py
from __future__ import absolute_import

from django import forms
from django.conf import settings
from django.contrib.admin import widgets
~~from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext as _

from ..models import ThumbnailOption
from ..utils.files import get_valid_filename


class AsPWithHelpMixin(object):
    def as_p_with_help(self):
        "Returns this form rendered as HTML <p>s with help text formated for admin."
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(label)s %(field)s</p>%(help_text)s',
            error_row='%s',
            row_ender='</p>',
            help_text_html='<p class="help">%s</p>',
            errors_on_separate_row=True)


class CopyFilesAndFoldersForm(forms.Form, AsPWithHelpMixin):
    suffix = forms.CharField(required=False, help_text=_("Suffix which will be appended to filenames of copied files."))

    def clean_suffix(self):
        valid = get_valid_filename(self.cleaned_data['suffix'])
        if valid != self.cleaned_data['suffix']:


## ... source file abbreviated to get to ValidationError examples ...


            }
        except KeyError as e:
            raise forms.ValidationError(_('Unknown rename format value key "%(key)s".') % {'key': e.args[0]})
        except Exception as e:
            raise forms.ValidationError(_('Invalid rename format: %(error)s.') % {'error': e})
        return self.cleaned_data['rename_format']


class ResizeImagesForm(forms.Form, AsPWithHelpMixin):
    if 'cmsplugin_filer_image' in settings.INSTALLED_APPS:
        thumbnail_option = models.ForeignKey(
            ThumbnailOption,
            null=True,
            blank=True,
            verbose_name=_("thumbnail option"),
            on_delete=models.CASCADE,
        ).formfield()
    width = models.PositiveIntegerField(_("width"), null=True, blank=True).formfield(widget=widgets.AdminIntegerFieldWidget)
    height = models.PositiveIntegerField(_("height"), null=True, blank=True).formfield(widget=widgets.AdminIntegerFieldWidget)
    crop = models.BooleanField(_("crop"), default=True).formfield()
    upscale = models.BooleanField(_("upscale"), default=True).formfield()

    def clean(self):
        if not (self.cleaned_data.get('thumbnail_option') or ((self.cleaned_data.get('width') or 0) + (self.cleaned_data.get('height') or 0))):
            if 'cmsplugin_filer_image' in settings.INSTALLED_APPS:
~~                raise ValidationError(_('Thumbnail option or resize parameters must be choosen.'))
            else:
~~                raise ValidationError(_('Resize parameters must be choosen.'))
        return self.cleaned_data



## ... source file continues with no further ValidationError examples...

```


## Example 8 from django-guardian
[django-guardian](https://github.com/django-guardian/django-guardian)
([project documentation](https://django-guardian.readthedocs.io/en/stable/)
and
[PyPI page](https://pypi.org/project/django-guardian/))
provides per-object permissions in [Django](/django.html) projects
by enhancing the existing authentication backend. The project's code
is open source under the
[MIT license](https://github.com/django-guardian/django-guardian/blob/devel/LICENSE).

[**django-guardian / guardian / models / models.py**](https://github.com/django-guardian/django-guardian/blob/devel/guardian/models/models.py)

```python
# models.py
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
~~from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from guardian.compat import user_model_label
from guardian.ctypes import get_content_type
from guardian.managers import GroupObjectPermissionManager, UserObjectPermissionManager


class BaseObjectPermission(models.Model):
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return '{} | {} | {}'.format(
            str(self.content_object),
            str(getattr(self, 'user', False) or self.group),
            str(self.permission.codename))

    def save(self, *args, **kwargs):
        content_type = get_content_type(self.content_object)
        if content_type != self.permission.content_type:
~~            raise ValidationError("Cannot persist permission not designed for "
                                  "this class (permission's type is %r and object's type is %r)"
                                  % (self.permission.content_type, content_type))
        return super().save(*args, **kwargs)


class BaseGenericObjectPermission(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_pk = models.CharField(_('object ID'), max_length=255)
    content_object = GenericForeignKey(fk_field='object_pk')

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['content_type', 'object_pk']),
        ]


class UserObjectPermissionBase(BaseObjectPermission):
    user = models.ForeignKey(user_model_label, on_delete=models.CASCADE)

    objects = UserObjectPermissionManager()

    class Meta:
        abstract = True


## ... source file continues with no further ValidationError examples...

```


## Example 9 from django-import-export
[django-import-export](https://github.com/django-import-export/django-import-export)
([documentation](https://django-import-export.readthedocs.io/en/latest/)
and [PyPI page](https://pypi.org/project/django-import-export/))
is a [Django](/django.html) code library for importing and exporting data
from the Django Admin. The tool supports many export and import formats
such as CSV, JSON and YAML. django-import-export is open source under the
[BSD 2-Clause "Simplified" License](https://github.com/django-import-export/django-import-export/blob/master/LICENSE).

[**django-import-export / import_export / resources.py**](https://github.com/django-import-export/django-import-export/blob/master/import_export/./resources.py)

```python
# resources.py
import functools
import logging
import tablib
import traceback
from collections import OrderedDict
from copy import deepcopy

from diff_match_patch import diff_match_patch

import django
from django.conf import settings
~~from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.core.management.color import no_style
from django.core.paginator import Paginator
from django.db import DEFAULT_DB_ALIAS, connections
from django.db.models.fields.related import ForeignObjectRel
from django.db.models.query import QuerySet
from django.db.transaction import (
    TransactionManagementError,
    atomic,
    savepoint,
    savepoint_commit,
    savepoint_rollback
)
from django.utils.encoding import force_str
from django.utils.safestring import mark_safe

from . import widgets
from .fields import Field
from .instance_loaders import ModelInstanceLoader
from .results import Error, Result, RowResult
from .utils import atomic_if_using_transaction

if django.VERSION[0] >= 3:
    from django.core.exceptions import FieldDoesNotExist
else:


## ... source file abbreviated to get to ValidationError examples ...


                else:
                    delete_ids = [o.pk for o in self.delete_instances]
                    self._meta.model.objects.filter(pk__in=delete_ids).delete()
        except Exception as e:
            logger.exception(e)
            if raise_errors:
                raise e
        finally:
            self.delete_instances.clear()

    def validate_instance(self, instance, import_validation_errors=None, validate_unique=True):
        if import_validation_errors is None:
            errors = {}
        else:
            errors = import_validation_errors.copy()
        if self._meta.clean_model_instances:
            try:
                instance.full_clean(
                    exclude=errors.keys(),
                    validate_unique=validate_unique,
                )
~~            except ValidationError as e:
                errors = e.update_error_dict(errors)

        if errors:
~~            raise ValidationError(errors)

    def save_instance(self, instance, using_transactions=True, dry_run=False):
        self.before_save_instance(instance, using_transactions, dry_run)
        if self._meta.use_bulk:
            if instance.pk:
                self.update_instances.append(instance)
            else:
                self.create_instances.append(instance)
        else:
            if not using_transactions and dry_run:
                pass
            else:
                instance.save()
        self.after_save_instance(instance, using_transactions, dry_run)

    def before_save_instance(self, instance, using_transactions, dry_run):
        pass

    def after_save_instance(self, instance, using_transactions, dry_run):
        pass

    def delete_instance(self, instance, using_transactions=True, dry_run=False):
        self.before_delete_instance(instance, dry_run)
        if self._meta.use_bulk:


## ... source file abbreviated to get to ValidationError examples ...


            else:
                instance.delete()
        self.after_delete_instance(instance, dry_run)

    def before_delete_instance(self, instance, dry_run):
        pass

    def after_delete_instance(self, instance, dry_run):
        pass

    def import_field(self, field, obj, data, is_m2m=False):
        if field.attribute and field.column_name in data:
            field.save(obj, data, is_m2m)

    def get_import_fields(self):
        return self.get_fields()

    def import_obj(self, obj, data, dry_run):
        errors = {}
        for field in self.get_import_fields():
            if isinstance(field.widget, widgets.ManyToManyWidget):
                continue
            try:
                self.import_field(field, obj, data)
            except ValueError as e:
~~                errors[field.attribute] = ValidationError(
                    force_str(e), code="invalid")
        if errors:
~~            raise ValidationError(errors)

    def save_m2m(self, obj, data, using_transactions, dry_run):
        if (not using_transactions and dry_run) or self._meta.use_bulk:
            pass
        else:
            for field in self.get_import_fields():
                if not isinstance(field.widget, widgets.ManyToManyWidget):
                    continue
                self.import_field(field, obj, data, True)

    def for_delete(self, row, instance):
        return False

    def skip_row(self, instance, original):
        if not self._meta.skip_unchanged or self._meta.skip_diff:
            return False
        for field in self.get_import_fields():
            try:
                if list(field.get_value(instance).all()) != list(field.get_value(original).all()):
                    return False
            except AttributeError:
                if field.get_value(instance) != field.get_value(original):
                    return False
        return True
        try:
            if len(self.delete_instances) > 0:
                if not using_transactions and dry_run:
                    pass


## ... source file abbreviated to get to ValidationError examples ...


            self.before_import_row(row, **kwargs)
            instance, new = self.get_or_init_instance(instance_loader, row)
            self.after_import_instance(instance, new, **kwargs)
            if new:
                row_result.import_type = RowResult.IMPORT_TYPE_NEW
            else:
                row_result.import_type = RowResult.IMPORT_TYPE_UPDATE
            row_result.new_record = new
            if not skip_diff:
                original = deepcopy(instance)
                diff = self.get_diff_class()(self, original, new)
            if self.for_delete(row, instance):
                if new:
                    row_result.import_type = RowResult.IMPORT_TYPE_SKIP
                    if not skip_diff:
                        diff.compare_with(self, None, dry_run)
                else:
                    row_result.import_type = RowResult.IMPORT_TYPE_DELETE
                    self.delete_instance(instance, using_transactions, dry_run)
                    if not skip_diff:
                        diff.compare_with(self, None, dry_run)
            else:
                import_validation_errors = {}
                try:
                    self.import_obj(instance, row, dry_run)
~~                except ValidationError as e:
                    import_validation_errors = e.update_error_dict(import_validation_errors)
                if self.skip_row(instance, original):
                    row_result.import_type = RowResult.IMPORT_TYPE_SKIP
                else:
                    self.validate_instance(instance, import_validation_errors)
                    self.save_instance(instance, using_transactions, dry_run)
                    self.save_m2m(instance, row, using_transactions, dry_run)
                    row_result.object_id = instance.pk
                    row_result.object_repr = force_str(instance)
                if not skip_diff:
                    diff.compare_with(self, instance, dry_run)

            if not skip_diff:
                row_result.diff = diff.as_html()
            self.after_import_row(row, row_result, **kwargs)

~~        except ValidationError as e:
            row_result.import_type = RowResult.IMPORT_TYPE_INVALID
            row_result.validation_error = e
        except Exception as e:
            row_result.import_type = RowResult.IMPORT_TYPE_ERROR
            if not isinstance(e, TransactionManagementError):
                logger.debug(e, exc_info=e)
            tb_info = traceback.format_exc()
            row_result.errors.append(self.get_error_result_class()(e, tb_info, row))

        if self._meta.use_bulk:
            if len(self.create_instances) == self._meta.batch_size:
                self.bulk_create(using_transactions, dry_run, raise_errors, batch_size=self._meta.batch_size)
            if len(self.update_instances) == self._meta.batch_size:
                self.bulk_update(using_transactions, dry_run, raise_errors, batch_size=self._meta.batch_size)
            if len(self.delete_instances) == self._meta.batch_size:
                self.bulk_delete(using_transactions, dry_run, raise_errors)

        return row_result

    def import_data(self, dataset, dry_run=False, raise_errors=False,
                    use_transactions=None, collect_failed_rows=False, **kwargs):

        if use_transactions is None:
            use_transactions = self.get_use_transactions()


## ... source file continues with no further ValidationError examples...

```


## Example 10 from django-jet
[django-jet](https://github.com/geex-arts/django-jet)
([project documentation](https://jet.readthedocs.io/en/latest/),
[PyPI project page](https://pypi.org/project/django-jet/) and
[more information](http://jet.geex-arts.com/))
is a fancy [Django](/django.html) Admin panel replacement.

The django-jet project is open source under the
[GNU Affero General Public License v3.0](https://github.com/geex-arts/django-jet/blob/dev/LICENSE).

[**django-jet / jet / forms.py**](https://github.com/geex-arts/django-jet/blob/dev/jet/./forms.py)

```python
# forms.py
import json
from django import forms
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
~~from django.core.exceptions import ValidationError
from django.db.models import Q
import operator

from jet.models import Bookmark, PinnedApplication
from jet.utils import get_model_instance_label, user_is_authenticated
from functools import reduce

try:
    from django.apps import apps
    get_model = apps.get_model
except ImportError:
    from django.db.models.loading import get_model


class AddBookmarkForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(AddBookmarkForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Bookmark
        fields = ['url', 'title']

    def clean(self):
        data = super(AddBookmarkForm, self).clean()
        if not user_is_authenticated(self.request.user) or not self.request.user.is_staff:
~~            raise ValidationError('error')
        if not self.request.user.has_perm('jet.change_bookmark'):
~~            raise ValidationError('error')
        return data

    def save(self, commit=True):
        self.instance.user = self.request.user.pk
        return super(AddBookmarkForm, self).save(commit)


class RemoveBookmarkForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(RemoveBookmarkForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Bookmark
        fields = []

    def clean(self):
        data = super(RemoveBookmarkForm, self).clean()
        if not user_is_authenticated(self.request.user) or not self.request.user.is_staff:
~~            raise ValidationError('error')
        if self.instance.user != self.request.user.pk:
~~            raise ValidationError('error')
        return data

    def save(self, commit=True):
        if commit:
            self.instance.delete()


class ToggleApplicationPinForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(ToggleApplicationPinForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PinnedApplication
        fields = ['app_label']

    def clean(self):
        data = super(ToggleApplicationPinForm, self).clean()
        if not user_is_authenticated(self.request.user) or not self.request.user.is_staff:
~~            raise ValidationError('error')
        return data

    def save(self, commit=True):
        if commit:
            try:
                pinned_app = PinnedApplication.objects.get(
                    app_label=self.cleaned_data['app_label'],
                    user=self.request.user.pk
                )
                pinned_app.delete()
                return False
            except PinnedApplication.DoesNotExist:
                PinnedApplication.objects.create(
                    app_label=self.cleaned_data['app_label'],
                    user=self.request.user.pk
                )
                return True


class ModelLookupForm(forms.Form):
    app_label = forms.CharField()
    model = forms.CharField()
    q = forms.CharField(required=False)
    page = forms.IntegerField(required=False)
    page_size = forms.IntegerField(required=False, min_value=1, max_value=1000)
    object_id = forms.IntegerField(required=False)
    model_cls = None

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(ModelLookupForm, self).__init__(*args, **kwargs)

    def clean(self):
        data = super(ModelLookupForm, self).clean()

        if not user_is_authenticated(self.request.user) or not self.request.user.is_staff:
~~            raise ValidationError('error')

        try:
            self.model_cls = get_model(data['app_label'], data['model'])
        except:
~~            raise ValidationError('error')

        content_type = ContentType.objects.get_for_model(self.model_cls)
        permission = Permission.objects.filter(content_type=content_type, codename__startswith='change_').first()

        if not self.request.user.has_perm('{}.{}'.format(data['app_label'], permission.codename)):
~~            raise ValidationError('error')

        return data

    def lookup(self):
        qs = self.model_cls.objects

        if self.cleaned_data['q']:
            if getattr(self.model_cls, 'autocomplete_search_fields', None):
                search_fields = self.model_cls.autocomplete_search_fields()
                filter_data = [Q((field + '__icontains', self.cleaned_data['q'])) for field in search_fields]
                qs = qs.filter(reduce(operator.or_, filter_data)).distinct()
            else:
                qs = qs.none()

        limit = self.cleaned_data['page_size'] or 100
        page = self.cleaned_data['page'] or 1
        offset = (page - 1) * limit

        items = list(map(
            lambda instance: {'id': instance.pk, 'text': get_model_instance_label(instance)},
            qs.all()[offset:offset + limit]
        ))
        total = qs.count()



## ... source file continues with no further ValidationError examples...

```


## Example 11 from django-model-utils
[django-model-utils](https://github.com/jazzband/django-model-utils)
([project documentation](https://django-model-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-model-utils/))
provides useful mixins and utilities for working with
[Django ORM](/django-orm.html) models in your projects.

The django-model-utils project is open sourced under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/jazzband/django-model-utils/blob/master/LICENSE.txt).

[**django-model-utils / model_utils / fields.py**](https://github.com/jazzband/django-model-utils/blob/master/model_utils/./fields.py)

```python
# fields.py
import uuid
from django.db import models
from django.conf import settings
~~from django.core.exceptions import ValidationError
from django.utils.timezone import now

DEFAULT_CHOICES_NAME = 'STATUS'


class AutoCreatedField(models.DateTimeField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('editable', False)
        kwargs.setdefault('default', now)
        super().__init__(*args, **kwargs)


class AutoLastModifiedField(AutoCreatedField):
    def get_default(self):
        if not hasattr(self, "_default"):
            self._default = self._get_default()
        return self._default

    def pre_save(self, model_instance, add):
        value = now()
        if add:
            current_value = getattr(model_instance, self.attname, self.get_default())
            if current_value != self.get_default():


## ... source file abbreviated to get to ValidationError examples ...


        excerpt = get_excerpt(value.content)
        setattr(model_instance, _excerpt_field_name(self.attname), excerpt)
        return value.content

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return value.content

    def get_prep_value(self, value):
        try:
            return value.content
        except AttributeError:
            return value

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['no_excerpt_field'] = True
        return name, path, args, kwargs


class UUIDField(models.UUIDField):

    def __init__(self, primary_key=True, version=4, editable=False, *args, **kwargs):

        if version == 2:
~~            raise ValidationError(
                'UUID version 2 is not supported.')

        if version < 1 or version > 5:
~~            raise ValidationError(
                'UUID version is not valid.')

        if version == 1:
            default = uuid.uuid1
        elif version == 3:
            default = uuid.uuid3
        elif version == 4:
            default = uuid.uuid4
        elif version == 5:
            default = uuid.uuid5

        kwargs.setdefault('primary_key', primary_key)
        kwargs.setdefault('editable', editable)
        kwargs.setdefault('default', default)
        super().__init__(*args, **kwargs)



## ... source file continues with no further ValidationError examples...

```


## Example 12 from django-oauth-toolkit
[django-oauth-toolkit](https://github.com/jazzband/django-oauth-toolkit)
([project website](http://dot.evonove.it/) and
[PyPI package information](https://pypi.org/project/django-oauth-toolkit/1.2.0/))
is a code library for adding and handling [OAuth2](https://oauth.net/)
flows within your [Django](/django.html) web application and
[API](/application-programming-interfaces.html).

The django-oauth-toolkit project is open sourced under the
[FreeBSD license](https://github.com/jazzband/django-oauth-toolkit/blob/master/LICENSE)
and it is maintained by the developer community group
[Jazzband](https://jazzband.co/).

[**django-oauth-toolkit / oauth2_provider / models.py**](https://github.com/jazzband/django-oauth-toolkit/blob/master/oauth2_provider/./models.py)

```python
# models.py
import logging
from datetime import timedelta
from urllib.parse import parse_qsl, urlparse

from django.apps import apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db import models, transaction
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .generators import generate_client_id, generate_client_secret
from .scopes import get_scopes_backend
from .settings import oauth2_settings
from .validators import RedirectURIValidator, WildcardSet


logger = logging.getLogger(__name__)


class AbstractApplication(models.Model):
    CLIENT_CONFIDENTIAL = "confidential"
    CLIENT_PUBLIC = "public"
    CLIENT_TYPES = (
        (CLIENT_CONFIDENTIAL, _("Confidential")),
        (CLIENT_PUBLIC, _("Public")),
    )

    GRANT_AUTHORIZATION_CODE = "authorization-code"
    GRANT_IMPLICIT = "implicit"
    GRANT_PASSWORD = "password"
    GRANT_CLIENT_CREDENTIALS = "client-credentials"
    GRANT_TYPES = (
        (GRANT_AUTHORIZATION_CODE, _("Authorization code")),


## ... source file abbreviated to get to ValidationError examples ...



        assert False, (
            "If you are using implicit, authorization_code"
            "or all-in-one grant_type, you must define "
            "redirect_uris field in your Application model"
        )

    def redirect_uri_allowed(self, uri):
        parsed_uri = urlparse(uri)
        uqs_set = set(parse_qsl(parsed_uri.query))
        for allowed_uri in self.redirect_uris.split():
            parsed_allowed_uri = urlparse(allowed_uri)

            if (parsed_allowed_uri.scheme == parsed_uri.scheme and
                    parsed_allowed_uri.netloc == parsed_uri.netloc and
                    parsed_allowed_uri.path == parsed_uri.path):

                aqs_set = set(parse_qsl(parsed_allowed_uri.query))

                if aqs_set.issubset(uqs_set):
                    return True

        return False

    def clean(self):
~~        from django.core.exceptions import ValidationError

        grant_types = (
            AbstractApplication.GRANT_AUTHORIZATION_CODE,
            AbstractApplication.GRANT_IMPLICIT,
        )

        redirect_uris = self.redirect_uris.strip().split()
        allowed_schemes = set(s.lower() for s in self.get_allowed_schemes())

        if redirect_uris:
            validator = RedirectURIValidator(WildcardSet())
            for uri in redirect_uris:
                validator(uri)
                scheme = urlparse(uri).scheme
                if scheme not in allowed_schemes:
~~                    raise ValidationError(_(
                        "Unauthorized redirect scheme: {scheme}"
                    ).format(scheme=scheme))

        elif self.authorization_grant_type in grant_types:
~~            raise ValidationError(_(
                "redirect_uris cannot be empty with grant_type {grant_type}"
            ).format(grant_type=self.authorization_grant_type))

    def get_absolute_url(self):
        return reverse("oauth2_provider:detail", args=[str(self.id)])

    def get_allowed_schemes(self):
        return oauth2_settings.ALLOWED_REDIRECT_URI_SCHEMES

    def allows_grant_type(self, *grant_types):
        return self.authorization_grant_type in grant_types

    def is_usable(self, request):
        return True


class ApplicationManager(models.Manager):
    def get_by_natural_key(self, client_id):
        return self.get(client_id=client_id)


class Application(AbstractApplication):
    objects = ApplicationManager()



## ... source file continues with no further ValidationError examples...

```


## Example 13 from django-rest-framework
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
import copy
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
~~from django.core.exceptions import ValidationError as DjangoValidationError
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
from django.utils.encoding import is_protected_type, smart_str
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


## ... source file abbreviated to get to ValidationError examples ...


    def run_validators(self, value):
        errors = []
        for validator in self.validators:
            if hasattr(validator, 'set_context'):
                warnings.warn(
                    "Method `set_context` on validators is deprecated and will "
                    "no longer be called starting with 3.13. Instead set "
                    "`requires_context = True` on the class, and accept the "
                    "context as an additional argument.",
                    RemovedInDRF313Warning, stacklevel=2
                )
                validator.set_context(self)

            try:
                if getattr(validator, 'requires_context', False):
                    validator(value, self)
                else:
                    validator(value)
~~            except ValidationError as exc:
                if isinstance(exc.detail, dict):
                    raise
                errors.extend(exc.detail)
            except DjangoValidationError as exc:
                errors.extend(get_error_detail(exc))
        if errors:
~~            raise ValidationError(errors)

    def to_internal_value(self, data):
        raise NotImplementedError(
            '{cls}.to_internal_value() must be implemented for field '
            '{field_name}. If you do not need to support write operations '
            'you probably want to subclass `ReadOnlyField` instead.'.format(
                cls=self.__class__.__name__,
                field_name=self.field_name,
            )
        )

    def to_representation(self, value):
        raise NotImplementedError(
            '{cls}.to_representation() must be implemented for field {field_name}.'.format(
                cls=self.__class__.__name__,
                field_name=self.field_name,
            )
        )

    def fail(self, key, **kwargs):
        try:
            msg = self.error_messages[key]
        except KeyError:
            class_name = self.__class__.__name__
            msg = MISSING_ERROR_MESSAGE.format(class_name=class_name, key=key)
            raise AssertionError(msg)
        message_string = msg.format(**kwargs)
~~        raise ValidationError(message_string, code=key)

    @property
    def root(self):
        root = self
        while root.parent is not None:
            root = root.parent
        return root

    @property
    def context(self):
        return getattr(self.root, '_context', {})

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance._args = args
        instance._kwargs = kwargs
        return instance

    def __deepcopy__(self, memo):
        args = [
            copy.deepcopy(item) if not isinstance(item, REGEX_TYPE) else item
            for item in self._args
        ]
        kwargs = {


## ... source file abbreviated to get to ValidationError examples ...



    def to_internal_value(self, data):
        if html.is_html_input(data):
            data = html.parse_html_list(data, default=[])
        if isinstance(data, (str, Mapping)) or not hasattr(data, '__iter__'):
            self.fail('not_a_list', input_type=type(data).__name__)
        if not self.allow_empty and len(data) == 0:
            self.fail('empty')
        return self.run_child_validation(data)

    def to_representation(self, data):
        return [self.child.to_representation(item) if item is not None else None for item in data]

    def run_child_validation(self, data):
        result = []
        errors = OrderedDict()

        for idx, item in enumerate(data):
            try:
                result.append(self.child.run_validation(item))
~~            except ValidationError as e:
                errors[idx] = e.detail

        if not errors:
            return result
~~        raise ValidationError(errors)


class DictField(Field):
    child = _UnvalidatedField()
    initial = {}
    default_error_messages = {
        'not_a_dict': _('Expected a dictionary of items but got type "{input_type}".'),
        'empty': _('This dictionary may not be empty.'),
    }

    def __init__(self, *args, **kwargs):
        self.child = kwargs.pop('child', copy.deepcopy(self.child))
        self.allow_empty = kwargs.pop('allow_empty', True)

        assert not inspect.isclass(self.child), '`child` has not been instantiated.'
        assert self.child.source is None, (
            "The `source` argument is not meaningful when applied to a `child=` field. "
            "Remove `source=` from the field declaration."
        )

        super().__init__(*args, **kwargs)
        self.child.bind(field_name='', parent=self)

    def get_value(self, dictionary):


## ... source file abbreviated to get to ValidationError examples ...


        if not self.allow_empty and len(data) == 0:
            self.fail('empty')

        return self.run_child_validation(data)

    def to_representation(self, value):
        return {
            str(key): self.child.to_representation(val) if val is not None else None
            for key, val in value.items()
        }

    def run_child_validation(self, data):
        result = {}
        errors = OrderedDict()

        for key, value in data.items():
            key = str(key)

            try:
                result[key] = self.child.run_validation(value)
~~            except ValidationError as e:
                errors[key] = e.detail

        if not errors:
            return result
~~        raise ValidationError(errors)


class HStoreField(DictField):
    child = CharField(allow_blank=True, allow_null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert isinstance(self.child, CharField), (
            "The `child` argument must be an instance of `CharField`, "
            "as the hstore extension stores values as strings."
        )


class JSONField(Field):
    default_error_messages = {
        'invalid': _('Value must be valid JSON.')
    }

    def __init__(self, *args, **kwargs):
        self.binary = kwargs.pop('binary', False)
        self.encoder = kwargs.pop('encoder', None)
        super().__init__(*args, **kwargs)

    def get_value(self, dictionary):
        (is_empty_value, data) = self.validate_empty_values(data)
        if is_empty_value:
            return data
        value = self.to_internal_value(data)
        self.run_validators(value)
        return value



## ... source file abbreviated to get to ValidationError examples ...


            if len(val) > 0:
                return val
            return html.parse_html_list(dictionary, prefix=self.field_name, default=empty)

        return dictionary.get(self.field_name, empty)


## ... source file abbreviated to get to ValidationError examples ...


    def to_internal_value(self, data):
        if html.is_html_input(data):
            data = html.parse_html_dict(data)
        if not isinstance(data, dict):
            self.fail('not_a_dict', input_type=type(data).__name__)


## ... source file continues with no further ValidationError examples...

```


## Example 14 from django-wiki
[django-wiki](https://github.com/django-wiki/django-wiki)
([project documentation](https://django-wiki.readthedocs.io/en/master/),
[demo](https://demo.django-wiki.org/),
and [PyPI page](https://pypi.org/project/django-wiki/))
is a wiki system code library for [Django](/django.html)
projects that makes it easier to create user-editable content.
The project aims to provide necessary core features and then
have an easy plugin format for additional features, rather than
having every exhaustive feature built into the core system.
django-wiki is a rewrite of an earlier now-defunct project
named [django-simplewiki](https://code.google.com/p/django-simple-wiki/).

The code for django-wiki is provided as open source under the
[GNU General Public License 3.0](https://github.com/django-wiki/django-wiki/blob/master/COPYING).

[**django-wiki / src/wiki / models / urlpath.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/models/urlpath.py)

```python
# urlpath.py
import logging
import warnings

from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
~~from django.core.exceptions import ValidationError
from django.db import models
from django.db import transaction
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.urls import reverse
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from wiki import managers
from wiki.conf import settings
from wiki.core.exceptions import MultipleRootURLs
from wiki.core.exceptions import NoRootURL
from wiki.decorators import disable_signal_for_loaddata
from wiki.models.article import Article
from wiki.models.article import ArticleForObject
from wiki.models.article import ArticleRevision

__all__ = [
    "URLPath",
]


log = logging.getLogger(__name__)


## ... source file abbreviated to get to ValidationError examples ...


            raise NoRootURL("You need to create a root article on site '%s'" % site)
        if no_paths > 1:
            raise MultipleRootURLs("Somehow you have multiple roots on %s" % site)
        return root_nodes[0]

    class MPTTMeta:
        pass

    def __str__(self):
        path = self.path
        return path if path else gettext("(root)")

    def delete(self, *args, **kwargs):
        assert not (
            self.parent and self.get_children()
        ), "You cannot delete a root article with children."
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = _("URL path")
        verbose_name_plural = _("URL paths")
        unique_together = ("site", "parent", "slug")

    def clean(self, *args, **kwargs):
        if self.slug and not self.parent:
~~            raise ValidationError(
                _("Sorry but you cannot have a root article with a slug.")
            )
        if not self.slug and self.parent:
~~            raise ValidationError(_("A non-root note must always have a slug."))
        if not self.parent:
            if URLPath.objects.root_nodes().filter(site=self.site).exclude(id=self.id):
~~                raise ValidationError(
                    _("There is already a root node on %s") % self.site
                )

    @classmethod
    def get_by_path(cls, path, select_related=False):


        path = path.lstrip("/")
        path = path.rstrip("/")

        if not path:
            return cls.root()

        slugs = path.split("/")
        level = 1
        parent = cls.root()
        for slug in slugs:
            if settings.URL_CASE_SENSITIVE:
                child = parent.get_children().select_related_common().get(slug=slug)
                child.cached_ancestors = parent.cached_ancestors + [parent]
                parent = child
            else:
                child = (
                    parent.get_children().select_related_common().get(slug__iexact=slug)


## ... source file continues with no further ValidationError examples...

```


## Example 15 from register
[register](https://github.com/ORGAN-IZE/register) is a [Django](/django.html),
[Bootstrap](/bootstrap-css.html), [PostgreSQL](/postgresql.html) project that is
open source under the
[GNU General Public License v3.0](https://github.com/ORGAN-IZE/register/blob/master/LICENSE).
This web application makes it easier for people to register as organ donors.
You can see the application live at
[https://register.organize.org/](https://register.organize.org/).

[**register / registration / forms.py**](https://github.com/ORGAN-IZE/register/blob/master/registration/./forms.py)

```python
# forms.py
from __future__ import unicode_literals

import logging
import re
import collections
import datetime

import django.forms
import django.forms.utils
import django.forms.widgets
import django.core.validators
~~import django.core.exceptions
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

import form_utils.forms
import requests
import dateutil.parser
import validate_email

logger = logging.getLogger(__name__)


REGISTRATION_CONFIGURATION_NAME = 'registration_configuration'

RE_NON_DECIMAL = re.compile(r'[^\d]+')
RE_NON_ALPHA = re.compile('[\W]+')
RE_POSTAL_CODE = re.compile(r'^[0-9]{5}$')
validate_postal_code = django.core.validators.RegexValidator(
    RE_POSTAL_CODE, _("Enter a valid postal code consisting 5 numbers."), 'invalid')


CHOICES_GENDER = (
    ('M', _('Male')),
    ('F', _('Female')),
)


class MultiEmailField(django.forms.CharField):
    message = _('Enter valid email addresses.')
    code = 'invalid'
    widget = django.forms.widgets.TextInput

    def to_python(self, value):
        "Normalize data to a list of strings."
        if not value:
            return []
        return [v.strip() for v in re.findall(validate_email.ADDR_SPEC, value)]

    def validate(self, value):
        "Check if value consists only of valid emails."

        super(MultiEmailField, self).validate(value)
        try:
            for email in value:
                django.core.validators.validate_email(email)
        except django.core.exceptions.ValidationError:
~~            raise django.core.exceptions.ValidationError(self.message, code=self.code)





class StateLookupForm(django.forms.Form):
    email = django.forms.EmailField(label=_('Email'), help_text=_('so we can send you confirmation of your registration'))
    postal_code = django.forms.CharField(
        label=_('Postal Code'),
        max_length=5, min_length=5, validators=[validate_postal_code],
        help_text=_('to determine which series of state-based questions we will ask next'))

    def clean_email(self):
        email = self.cleaned_data['email']
        if settings.DISABLE_EMAIL_VALIDATION:
            logger.warning('Email validation disabled: DISABLE_EMAIL_VALIDATION '
                           'is set')
            return email
        if not hasattr(settings, 'MAILGUN_PUBLIC_API_KEY'):
            logger.warning(
                'Cannot validate email: MAILGUN_PUBLIC_API_KEY not set')
            return email
        r = requests.get(
            'https://api.mailgun.net/v2/address/validate',


## ... source file continues with no further ValidationError examples...

```


## Example 16 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / snippets / tests.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/snippets/tests.py)

```python
# tests.py
import json

from django.contrib.admin.utils import quote
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser, Permission
from django.core import checks
~~from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import HttpRequest, HttpResponse
from django.test import RequestFactory, TestCase
from django.test.utils import override_settings
from django.urls import reverse
from taggit.models import Tag

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.forms import WagtailAdminModelForm
from wagtail.core.models import Page
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import SNIPPET_MODELS, register_snippet
from wagtail.snippets.views.snippets import get_snippet_edit_handler
from wagtail.tests.snippets.forms import FancySnippetForm
from wagtail.tests.snippets.models import (
    AlphaSnippet, FancySnippet, FileUploadSnippet, RegisterDecorator, RegisterFunction,
    SearchableSnippet, StandardSnippet, StandardSnippetWithCustomPrimaryKey, ZuluSnippet)
from wagtail.tests.testapp.models import (
    Advert, AdvertWithCustomPrimaryKey, AdvertWithCustomUUIDPrimaryKey, AdvertWithTabbedInterface,
    SnippetChooserModel, SnippetChooserModelWithCustomPrimaryKey)
from wagtail.tests.utils import WagtailTestUtils



## ... source file abbreviated to get to ValidationError examples ...


        self.assertInHTML('<input id="advert" name="advert" placeholder="" type="hidden" />', empty_form_html)
        self.assertIn('createSnippetChooser("advert", "tests/advert");', empty_form_html)

        test_advert = Advert.objects.get(text='test_advert')
        test_advert_form_html = block.render_form(test_advert, 'advert')
        expected_html = '<input id="advert" name="advert" placeholder="" type="hidden" value="%d" />' % test_advert.id
        self.assertInHTML(expected_html, test_advert_form_html)
        self.assertIn("pick an advert, any advert", test_advert_form_html)

    def test_form_response(self):
        block = SnippetChooserBlock(Advert)
        test_advert = Advert.objects.get(text='test_advert')

        value = block.value_from_datadict({'advert': str(test_advert.id)}, {}, 'advert')
        self.assertEqual(value, test_advert)

        empty_value = block.value_from_datadict({'advert': ''}, {}, 'advert')
        self.assertEqual(empty_value, None)

    def test_clean(self):
        required_block = SnippetChooserBlock(Advert)
        nonrequired_block = SnippetChooserBlock(Advert, required=False)
        test_advert = Advert.objects.get(text='test_advert')

        self.assertEqual(required_block.clean(test_advert), test_advert)
~~        with self.assertRaises(ValidationError):
            required_block.clean(None)

        self.assertEqual(nonrequired_block.clean(test_advert), test_advert)
        self.assertEqual(nonrequired_block.clean(None), None)


class TestSnippetListViewWithCustomPrimaryKey(TestCase, WagtailTestUtils):
    def setUp(self):
        self.login()

        self.snippet_a = StandardSnippetWithCustomPrimaryKey.objects.create(snippet_id="snippet/01", text="Hello")
        self.snippet_b = StandardSnippetWithCustomPrimaryKey.objects.create(snippet_id="snippet/02", text="Hello")
        self.snippet_c = StandardSnippetWithCustomPrimaryKey.objects.create(snippet_id="snippet/03", text="Hello")

    def get(self, params={}):
        return self.client.get(reverse('wagtailsnippets:list',
                                       args=('snippetstests', 'standardsnippetwithcustomprimarykey')),
                               params)

    def test_simple(self):
        response = self.get()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wagtailsnippets/snippets/type_index.html')



## ... source file abbreviated to get to ValidationError examples ...


        self.assertInHTML('<input id="advertwithcustomprimarykey" name="advertwithcustomprimarykey" placeholder="" type="hidden" />', empty_form_html)
        self.assertIn('createSnippetChooser("advertwithcustomprimarykey", "tests/advertwithcustomprimarykey");', empty_form_html)

        test_advert = AdvertWithCustomPrimaryKey.objects.get(pk='advert/01')
        test_advert_form_html = block.render_form(test_advert, 'advertwithcustomprimarykey')
        expected_html = '<input id="advertwithcustomprimarykey" name="advertwithcustomprimarykey" placeholder="" type="hidden" value="%s" />' % test_advert.pk
        self.assertInHTML(expected_html, test_advert_form_html)
        self.assertIn("pick an advert, any advert", test_advert_form_html)

    def test_form_response(self):
        block = SnippetChooserBlock(AdvertWithCustomPrimaryKey)
        test_advert = AdvertWithCustomPrimaryKey.objects.get(pk='advert/01')

        value = block.value_from_datadict({'advertwithcustomprimarykey': str(test_advert.pk)}, {}, 'advertwithcustomprimarykey')
        self.assertEqual(value, test_advert)

        empty_value = block.value_from_datadict({'advertwithcustomprimarykey': ''}, {}, 'advertwithcustomprimarykey')
        self.assertEqual(empty_value, None)

    def test_clean(self):
        required_block = SnippetChooserBlock(AdvertWithCustomPrimaryKey)
        nonrequired_block = SnippetChooserBlock(AdvertWithCustomPrimaryKey, required=False)
        test_advert = AdvertWithCustomPrimaryKey.objects.get(pk='advert/01')

        self.assertEqual(required_block.clean(test_advert), test_advert)
~~        with self.assertRaises(ValidationError):
            required_block.clean(None)

        self.assertEqual(nonrequired_block.clean(test_advert), test_advert)
        self.assertEqual(nonrequired_block.clean(None), None)


class TestSnippetChooserPanelWithCustomPrimaryKey(TestCase, WagtailTestUtils):
    fixtures = ['test.json']

    def setUp(self):
        self.request = RequestFactory().get('/')
        user = AnonymousUser()  # technically, Anonymous users cannot access the admin
        self.request.user = user

        model = SnippetChooserModelWithCustomPrimaryKey
        self.advert_text = 'Test advert text'
        test_snippet = model.objects.create(
            advertwithcustomprimarykey=AdvertWithCustomPrimaryKey.objects.create(
                advert_id="advert/02",
                text=self.advert_text
            )
        )

        self.edit_handler = get_snippet_edit_handler(model)


## ... source file continues with no further ValidationError examples...

```

