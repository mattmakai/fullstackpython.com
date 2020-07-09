title: django.utils.encoding force_str Example Code
category: page
slug: django-utils-encoding-force-str-examples
sortorder: 500011443
toc: False
sidebartitle: django.utils.encoding force_str
meta: Python example code for the force_str callable from the django.utils.encoding module of the Django project.


force_str is a callable within the django.utils.encoding module of the Django project.


## Example 1 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / utils.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/./utils.py)

```python
# utils.py
import base64
import importlib
import json
import random
import re
import string
import unicodedata
from collections import OrderedDict
from urllib.parse import urlsplit

import django
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core.exceptions import FieldDoesNotExist, ImproperlyConfigured
from django.core.serializers.json import DjangoJSONEncoder
from django.core.validators import ValidationError, validate_email
from django.db.models import FileField
from django.db.models.fields import (
    BinaryField,
    DateField,
    DateTimeField,
    EmailField,
    TimeField,
)
from django.utils import dateparse
~~from django.utils.encoding import force_bytes, force_str


MAX_USERNAME_SUFFIX_LENGTH = 7
USERNAME_SUFFIX_CHARS = (
    [string.digits] * 4 +
    [string.ascii_letters] * (MAX_USERNAME_SUFFIX_LENGTH - 4))


def _generate_unique_username_base(txts, regex=None):
    from .account.adapter import get_adapter
    adapter = get_adapter()
    username = None
    regex = regex or r'[^\w\s@+.-]'
    for txt in txts:
        if not txt:
            continue
~~        username = unicodedata.normalize('NFKD', force_str(txt))
        username = username.encode('ascii', 'ignore').decode('ascii')
~~        username = force_str(re.sub(regex, '', username).lower())
        username = username.split('@')[0]
        username = username.strip()
        username = re.sub(r'\s+', '_', username)
        try:
            username = adapter.clean_username(username, shallow=True)
            break
        except ValidationError:
            pass
    return username or 'user'


def get_username_max_length():
    from .account.app_settings import USER_MODEL_USERNAME_FIELD
    if USER_MODEL_USERNAME_FIELD is not None:
        User = get_user_model()
        max_length = User._meta.get_field(USER_MODEL_USERNAME_FIELD).max_length
    else:
        max_length = 0
    return max_length


def generate_username_candidate(basename, suffix_length):
    max_length = get_username_max_length()
    suffix = ''.join(


## ... source file abbreviated to get to force_str examples ...


    assert isinstance(path, str)
    pkg, attr = path.rsplit('.', 1)
    ret = getattr(importlib.import_module(pkg), attr)
    return ret


def import_callable(path_or_callable):
    if not hasattr(path_or_callable, '__call__'):
        ret = import_attribute(path_or_callable)
    else:
        ret = path_or_callable
    return ret


SERIALIZED_DB_FIELD_PREFIX = '_db_'


def serialize_instance(instance):
    data = {}
    for k, v in instance.__dict__.items():
        if k.startswith('_') or callable(v):
            continue
        try:
            field = instance._meta.get_field(k)
            if isinstance(field, BinaryField):
~~                v = force_str(base64.b64encode(v))
            elif isinstance(field, FileField):
                if v and not isinstance(v, str):
                    v = v.name
            try:
                json.dumps(v, cls=DjangoJSONEncoder)
            except TypeError:
                v = field.get_prep_value(v)
                k = SERIALIZED_DB_FIELD_PREFIX + k
        except FieldDoesNotExist:
            pass
        data[k] = v
    return json.loads(json.dumps(data, cls=DjangoJSONEncoder))


def deserialize_instance(model, data):
    ret = model()
    for k, v in data.items():
        is_db_value = False
        if k.startswith(SERIALIZED_DB_FIELD_PREFIX):
            k = k[len(SERIALIZED_DB_FIELD_PREFIX):]
            is_db_value = True
        if v is not None:
            try:
                f = model._meta.get_field(k)


## ... source file continues with no further force_str examples...

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

[**django-extensions / django_extensions / validators.py**](https://github.com/django-extensions/django-extensions/blob/master/django_extensions/./validators.py)

```python
# validators.py
import unicodedata
import binascii


from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
~~from django.utils.encoding import force_str
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
~~        value = force_str(value)
        whitelist = self.whitelist
        category = unicodedata.category
        for character in value:
            if whitelist and character in whitelist:
                continue
            if category(character)[0] == "C":
                params = {'value': value, 'whitelist': whitelist}
                raise ValidationError(self.message, code=self.code, params=params)

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
~~        value = force_str(value)
        if value != value.strip():
            params = {'value': value}
            raise ValidationError(self.message, code=self.code, params=params)

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
~~        value = force_str(value)
        if self.length and len(value) != self.length:
            raise ValidationError(self.messages['length'], code='hex_only_length', params={'length': self.length})
        if self.min_length and len(value) < self.min_length:
            raise ValidationError(self.messages['min_length'], code='hex_only_min_length', params={'min': self.min_length})
        if self.max_length and len(value) < self.max_length:
            raise ValidationError(self.messages['max_length'], code='hex_only_max_length', params={'max': self.max_length})

        try:
            binascii.unhexlify(value)
        except (TypeError, binascii.Error):
            raise ValidationError(self.messages['invalid'], code='hex_only')

    def __eq__(self, other):
        return (
            isinstance(other, HexValidator) and
            (self.message == other.message) and
            (self.code == other.code)
        )



## ... source file continues with no further force_str examples...

```


## Example 3 from django-filter
[django-filter](https://github.com/carltongibson/django-filter)
([project documentation](https://django-filter.readthedocs.io/en/master/)
and
[PyPI page](https://pypi.org/project/django-filter/2.2.0/))
makes it easier to filter down querysets from the
[Django ORM](/django-orm.html) by providing common bits of boilerplate
code. django-filter is provided as
[open source](https://github.com/carltongibson/django-filter/blob/master/LICENSE).

[**django-filter / django_filters / fields.py**](https://github.com/carltongibson/django-filter/blob/master/django_filters/./fields.py)

```python
# fields.py
from collections import namedtuple
from datetime import datetime, time

from django import forms
from django.utils.dateparse import parse_datetime
~~from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _

from .conf import settings
from .constants import EMPTY_VALUES
from .utils import handle_timezone
from .widgets import (
    BaseCSVWidget,
    CSVWidget,
    DateRangeWidget,
    LookupChoiceWidget,
    RangeWidget
)


class RangeField(forms.MultiValueField):
    widget = RangeWidget

    def __init__(self, fields=None, *args, **kwargs):
        if fields is None:
            fields = (
                forms.DecimalField(),
                forms.DecimalField())
        super().__init__(fields, *args, **kwargs)



## ... source file abbreviated to get to force_str examples ...


        empty_label = kwargs.pop('empty_label', settings.EMPTY_CHOICE_LABEL)
        fields = (field, ChoiceField(choices=lookup_choices, empty_label=empty_label))
        widget = LookupChoiceWidget(widgets=[f.widget for f in fields])
        kwargs['widget'] = widget
        kwargs['help_text'] = field.help_text
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if len(data_list) == 2:
            value, lookup_expr = data_list
            if value not in EMPTY_VALUES:
                if lookup_expr not in EMPTY_VALUES:
                    return Lookup(value=value, lookup_expr=lookup_expr)
                else:
                    raise forms.ValidationError(
                        self.error_messages['lookup_required'],
                        code='lookup_required')
        return None


class IsoDateTimeField(forms.DateTimeField):
    ISO_8601 = 'iso-8601'
    input_formats = [ISO_8601]

    def strptime(self, value, format):
~~        value = force_str(value)

        if format == self.ISO_8601:
            parsed = parse_datetime(value)
            if parsed is None:  # Continue with other formats if doesn't match
                raise ValueError
            return handle_timezone(parsed)
        return super().strptime(value, format)


class BaseCSVField(forms.Field):
    base_widget_class = BaseCSVWidget

    def __init__(self, *args, **kwargs):
        widget = kwargs.get('widget') or self.widget
        kwargs['widget'] = self._get_widget_class(widget)

        super().__init__(*args, **kwargs)

    def _get_widget_class(self, widget):
        if isinstance(widget, BaseCSVWidget) or (
                isinstance(widget, type) and
                issubclass(widget, BaseCSVWidget)):
            return widget



## ... source file continues with no further force_str examples...

```


## Example 4 from django-floppyforms
[django-floppyforms](https://github.com/jazzband/django-floppyforms)
([project documentation](https://django-floppyforms.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-floppyforms/))
is a [Django](/django.html) code library for better control
over rendering HTML forms in your [templates](/template-engines.html).

The django-floppyforms code is provided as
[open source](https://github.com/jazzband/django-floppyforms/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-floppyforms / floppyforms / widgets.py**](https://github.com/jazzband/django-floppyforms/blob/master/floppyforms/./widgets.py)

```python
# widgets.py
import datetime
import re
from itertools import chain

import django
from django import forms
from django.conf import settings
from django.forms.widgets import FILE_INPUT_CONTRADICTION
from django.template import loader
from django.utils import datetime_safe, formats
from django.utils.dates import MONTHS
~~from django.utils.encoding import force_str
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .compat import MULTIVALUE_DICT_TYPES, flatten_contexts


from django.forms.utils import to_current_timezone


RE_DATE = re.compile(r'(\d{4})-(\d\d?)-(\d\d?)$')


__all__ = (
    'TextInput', 'PasswordInput', 'HiddenInput', 'ClearableFileInput',
    'FileInput', 'DateInput', 'DateTimeInput', 'TimeInput', 'Textarea',
    'CheckboxInput', 'Select', 'NullBooleanSelect', 'SelectMultiple',
    'RadioSelect', 'CheckboxSelectMultiple', 'SearchInput', 'RangeInput',
    'ColorInput', 'EmailInput', 'URLInput', 'PhoneNumberInput', 'NumberInput',
    'IPAddressInput', 'MultiWidget', 'Widget', 'SplitDateTimeWidget',
    'SplitHiddenDateTimeWidget', 'MultipleHiddenInput', 'SelectDateWidget',
    'SlugInput',
)



## ... source file abbreviated to get to force_str examples ...


        def format_value(self, value):
            return self._format_value(value)


class Input(Widget):
    template_name = 'floppyforms/input.html'
    input_type = None
    datalist = None

    def __init__(self, *args, **kwargs):
        datalist = kwargs.pop('datalist', None)
        if datalist is not None:
            self.datalist = datalist
        template_name = kwargs.pop('template_name', None)
        if template_name is not None:
            self.template_name = template_name
        super(Input, self).__init__(*args, **kwargs)
        self.context_instance = None

    def get_context_data(self):
        return {}

    def format_value(self, value):
        if self.is_localized:
            value = formats.localize_input(value)
~~        return force_str(value)

    def get_context(self, name, value, attrs=None):
        context = {
            'widget': self,
            'type': self.input_type,
            'name': name,
            'hidden': self.is_hidden,
            'required': self.is_required,
            'True': True,
        }

        if self.is_hidden:
            context['hidden'] = True

        if value is None:
            value = ''

        if value != '':
            context['value'] = self.format_value(value)

        context.update(self.get_context_data())
        context['attrs'] = self.build_attrs(attrs)

        for key, attr in context['attrs'].items():


## ... source file abbreviated to get to force_str examples ...




class HiddenInput(Input):
    template_name = 'floppyforms/hidden.html'
    input_type = 'hidden'


class MultipleHiddenInput(HiddenInput):
    def __init__(self, attrs=None, choices=()):
        super(MultipleHiddenInput, self).__init__(attrs)
        self.choices = choices

    def render(self, name, value, attrs=None, choices=(), renderer=None):
        if value is None:
            value = []

        final_attrs = self.build_attrs(attrs)
        id_ = final_attrs.get('id', None)
        inputs = []
        for i, v in enumerate(value):
            input_attrs = final_attrs.copy()
            if id_:
                input_attrs['id'] = '%s_%s' % (id_, i)
            input_ = HiddenInput()
            input_.is_required = self.is_required
~~            inputs.append(input_.render(name, force_str(v), input_attrs, renderer=renderer))
        return mark_safe("\n".join(inputs))

    def value_from_datadict(self, data, files, name):
        if isinstance(data, MULTIVALUE_DICT_TYPES):
            return data.getlist(name)
        return data.get(name, None)


class SlugInput(TextInput):
    template_name = 'floppyforms/slug.html'

    def get_context(self, name, value, attrs):
        context = super(SlugInput, self).get_context(name, value, attrs)
        context['attrs']['pattern'] = r"[-\w]+"
        return context


class IPAddressInput(TextInput):
    template_name = 'floppyforms/ipaddress.html'

    ip_pattern = (r"(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25"
                  r"[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}")

    def get_context(self, name, value, attrs):


## ... source file abbreviated to get to force_str examples ...




def boolean_check(v):
    return not (v is False or v is None or v == '')


class CheckboxInput(Input, forms.CheckboxInput):
    template_name = 'floppyforms/checkbox.html'
    input_type = 'checkbox'

    def __init__(self, attrs=None, check_test=None):
        super(CheckboxInput, self).__init__(attrs)
        self.check_test = boolean_check if check_test is None else check_test

    def get_context(self, name, value, attrs):
        result = self.check_test(value)
        context = super(CheckboxInput, self).get_context(name, value, attrs)
        if result:
            context['attrs']['checked'] = True
        return context

    def format_value(self, value):
        if value in ('', True, False, None):
            value = None
        else:
~~            value = force_str(value)
        return value

    def value_from_datadict(self, data, files, name):
        return forms.CheckboxInput.value_from_datadict(self, data, files, name)

    if django.VERSION < (1, 6):
        def _has_changed(self, initial, data):
            if initial == 'False':
                initial = False
            return bool(initial) != bool(data)


class Select(Input):
    allow_multiple_selected = False
    template_name = 'floppyforms/select.html'

    def __init__(self, attrs=None, choices=()):
        super(Select, self).__init__(attrs)
        self.choices = list(choices)

    def get_context(self, name, value, attrs=None, choices=()):
        if not hasattr(value, '__iter__') or isinstance(value,
                                                        str):
            value = [value]
        context = super(Select, self).get_context(name, value, attrs)

        if self.allow_multiple_selected:
            context['attrs']['multiple'] = "multiple"

        groups = []
        for option_value, option_label in chain(self.choices, choices):
            if isinstance(option_label, (list, tuple)):
                group = []
                for val, lab in option_label:
                    group.append((force_str(val), lab))
                groups.append((option_value, group))
            else:
~~                option_value = force_str(option_value)
                if groups and groups[-1][0] is None:
                    groups[-1][1].append((option_value, option_label))
                else:
                    groups.append((None, [(option_value, option_label)]))
        context["optgroups"] = groups
        return context

    def format_value(self, value):
        if len(value) == 1 and value[0] is None:
            return []
        return set(force_str(v) for v in value)


class NullBooleanSelect(Select):
    def __init__(self, attrs=None):
        choices = (('1', _('Unknown')),
                   ('2', _('Yes')),
                   ('3', _('No')))
        super(NullBooleanSelect, self).__init__(attrs, choices)

    def format_value(self, value):
        value = value[0]
        try:
            value = {True: '2', False: '3', '2': '2', '3': '3'}[value]


## ... source file abbreviated to get to force_str examples ...


    template_name = 'floppyforms/radio.html'


class CheckboxSelectMultiple(SelectMultiple):
    template_name = 'floppyforms/checkbox_select.html'


class MultiWidget(forms.MultiWidget):
    @property
    def is_hidden(self):
        return all(w.is_hidden for w in self.widgets)

    def build_attrs(self, base_attrs, extra_attrs=None, **kwargs):
        attrs = dict(self.attrs, **kwargs)
        attrs.update(base_attrs)
        if extra_attrs:
            attrs.update(extra_attrs)
        return attrs

    if django.VERSION < (1, 11):
        def format_value(self, value):
            if value == '' or value is None:
                return None
            if self.is_localized:
                return formats.localize_input(value)
~~            return force_str(value)

        def get_context(self, name, value, attrs):
            context = {}
            context['widget'] = {
                'name': name,
                'is_hidden': self.is_hidden,
                'required': self.is_required,
                'value': self.format_value(value),
                'attrs': self.build_attrs(self.attrs, attrs),
                'template_name': self.template_name,
            }
            if self.is_localized:
                for widget in self.widgets:
                    widget.is_localized = self.is_localized
            if not isinstance(value, list):
                value = self.decompress(value)

            final_attrs = context['widget']['attrs']
            input_type = final_attrs.pop('type', None)
            id_ = final_attrs.get('id')
            subwidgets = []
            for i, widget in enumerate(self.widgets):
                if input_type is not None:
                    widget.input_type = input_type


## ... source file continues with no further force_str examples...

```


## Example 5 from django-guardian
[django-guardian](https://github.com/django-guardian/django-guardian)
([project documentation](https://django-guardian.readthedocs.io/en/stable/)
and
[PyPI page](https://pypi.org/project/django-guardian/))
provides per-object permissions in [Django](/django.html) projects
by enhancing the existing authentication backend. The project's code
is open source under the
[MIT license](https://github.com/django-guardian/django-guardian/blob/devel/LICENSE).

[**django-guardian / guardian / core.py**](https://github.com/django-guardian/django-guardian/blob/devel/guardian/./core.py)

```python
# core.py
from itertools import chain

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.db.models.query import QuerySet
~~from django.utils.encoding import force_str

from guardian.conf import settings as guardian_settings
from guardian.ctypes import get_content_type
from guardian.utils import get_group_obj_perms_model, get_identity, get_user_obj_perms_model


def _get_pks_model_and_ctype(objects):

    if isinstance(objects, QuerySet):
        model = objects.model
        pks = [force_str(pk) for pk in objects.values_list('pk', flat=True)]
        ctype = get_content_type(model)
    else:
        pks = []
        for idx, obj in enumerate(objects):
            if not idx:
                model = type(obj)
                ctype = get_content_type(model)
            pks.append(force_str(obj.pk))

    return pks, model, ctype


class ObjectPermissionChecker:


## ... source file abbreviated to get to force_str examples ...


            return []

        if guardian_settings.AUTO_PREFETCH:
            self._prefetch_cache()

        ctype = get_content_type(obj)
        key = self.get_local_cache_key(obj)
        if key not in self._obj_perms_cache:
            if guardian_settings.AUTO_PREFETCH:
                return []
            if self.user and self.user.is_superuser:
                perms = list(chain(*Permission.objects
                                   .filter(content_type=ctype)
                                   .values_list("codename")))
            elif self.user:
                user_perms = self.get_user_perms(obj)
                group_perms = self.get_group_perms(obj)
                perms = list(set(chain(user_perms, group_perms)))
            else:
                perms = list(set(self.get_group_perms(obj)))
            self._obj_perms_cache[key] = perms
        return self._obj_perms_cache[key]

    def get_local_cache_key(self, obj):
        ctype = get_content_type(obj)
~~        return (ctype.id, force_str(obj.pk))

    def prefetch_perms(self, objects):
        if self.user and not self.user.is_active:
            return []

        User = get_user_model()
        pks, model, ctype = _get_pks_model_and_ctype(objects)

        if self.user and self.user.is_superuser:
            perms = list(chain(
                *Permission.objects
                .filter(content_type=ctype)
                .values_list("codename")))

            for pk in pks:
~~                key = (ctype.id, force_str(pk))
                self._obj_perms_cache[key] = perms

            return True

        group_model = get_group_obj_perms_model(model)

        if self.user:
            fieldname = 'group__{}'.format(
                User.groups.field.related_query_name(),
            )
            group_filters = {fieldname: self.user}
        else:
            group_filters = {'group': self.group}

        if group_model.objects.is_generic():
            group_filters.update({
                'content_type': ctype,
                'object_pk__in': pks,
            })
        else:
            group_filters.update({
                'content_object_id__in': pks
            })



## ... source file abbreviated to get to force_str examples ...


                    'content_type': ctype,
                    'object_pk__in': pks
                })
            else:
                user_filters.update({
                    'content_object_id__in': pks
                })

            user_perms_qs = model.objects.filter(**user_filters).select_related('permission')
            group_perms_qs = group_model.objects.filter(**group_filters).select_related('permission')
            perms = chain(user_perms_qs, group_perms_qs)
        else:
            perms = chain(
                *(group_model.objects.filter(**group_filters).select_related('permission'),)
            )

        for obj in objects:
            key = self.get_local_cache_key(obj)
            if key not in self._obj_perms_cache:
                self._obj_perms_cache[key] = []

        for perm in perms:
            if type(perm).objects.is_generic():
                key = (ctype.id, perm.object_pk)
            else:
~~                key = (ctype.id, force_str(perm.content_object_id))

            self._obj_perms_cache[key].append(perm.permission.codename)

        return True

    @staticmethod
    def _init_obj_prefetch_cache(obj, *querysets):
        cache = {}
        for qs in querysets:
            perms = qs.select_related('permission__codename').values_list('content_type_id', 'object_pk',
                                                                          'permission__codename')
            for p in perms:
                if p[:2] not in cache:
                    cache[p[:2]] = []
                cache[p[:2]] += [p[2], ]
        obj._guardian_perms_cache = cache
        return obj, cache

    def _prefetch_cache(self):
        from guardian.utils import get_user_obj_perms_model, get_group_obj_perms_model
        UserObjectPermission = get_user_obj_perms_model()
        GroupObjectPermission = get_group_obj_perms_model()
        if self.user:
            obj = self.user


## ... source file continues with no further force_str examples...

```


## Example 6 from django-haystack
[django-haystack](https://github.com/django-haystack/django-haystack)
([project website](http://haystacksearch.org/) and
[PyPI page](https://pypi.org/project/django-haystack/))
is a search abstraction layer that separates the Python search code
in a [Django](/django.html) web application from the search engine
implementation that it runs on, such as
[Apache Solr](http://lucene.apache.org/solr/),
[Elasticsearch](https://www.elastic.co/)
or [Whoosh](https://whoosh.readthedocs.io/en/latest/intro.html).

The django-haystack project is open source under the
[BSD license](https://github.com/django-haystack/django-haystack/blob/master/LICENSE).

[**django-haystack / haystack / models.py**](https://github.com/django-haystack/django-haystack/blob/master/haystack/./models.py)

```python
# models.py

from django.core.exceptions import ObjectDoesNotExist
~~from django.utils.encoding import force_str
from django.utils.text import capfirst

from haystack.constants import DEFAULT_ALIAS
from haystack.exceptions import NotHandled, SpatialError
from haystack.utils import log as logging
from haystack.utils.app_loading import haystack_get_model

try:
    from geopy import distance as geopy_distance
except ImportError:
    geopy_distance = None


class SearchResult(object):

    def __init__(self, app_label, model_name, pk, score, **kwargs):
        self.app_label, self.model_name = app_label, model_name
        self.pk = pk
        self.score = score
        self._object = None
        self._model = None
        self._verbose_name = None
        self._additional_fields = []
        self._point_of_origin = kwargs.pop("_point_of_origin", None)
        self._distance = kwargs.pop("_distance", None)
        self.stored_fields = None
        self.log = self._get_log()

        for key, value in kwargs.items():
            if key not in self.__dict__:
                self.__dict__[key] = value
                self._additional_fields.append(key)

    def _get_log(self):
        return logging.getLogger("haystack")

    def __repr__(self):
        return "<SearchResult: %s.%s (pk=%r)>" % (
            self.app_label,
            self.model_name,
            self.pk,
        )

    def __str__(self):
~~        return force_str(self.__repr__())

    def __getattr__(self, attr):
        if attr == "__getnewargs__":
            raise AttributeError

        return self.__dict__.get(attr, None)

    def _get_searchindex(self):
        from haystack import connections

        return connections[DEFAULT_ALIAS].get_unified_index().get_index(self.model)

    searchindex = property(_get_searchindex)

    def _get_object(self):
        if self._object is None:
            if self.model is None:
                self.log.error("Model could not be found for SearchResult '%s'.", self)
                return None

            try:
                try:
                    self._object = self.searchindex.read_queryset().get(pk=self.pk)
                except NotHandled:


## ... source file abbreviated to get to force_str examples ...


                )

            po_lng, po_lat = self._point_of_origin["point"].coords
            location_field = getattr(self, self._point_of_origin["field"])

            if location_field is None:
                return None

            lf_lng, lf_lat = location_field.coords
            self._distance = Distance(
                km=geopy_distance.distance((po_lat, po_lng), (lf_lat, lf_lng)).km
            )

        return self._distance

    def _set_distance(self, dist):
        self._distance = dist

    distance = property(_get_distance, _set_distance)

    def _get_verbose_name(self):
        if self.model is None:
            self.log.error("Model could not be found for SearchResult '%s'.", self)
            return ""

~~        return force_str(capfirst(self.model._meta.verbose_name))

    verbose_name = property(_get_verbose_name)

    def _get_verbose_name_plural(self):
        if self.model is None:
            self.log.error("Model could not be found for SearchResult '%s'.", self)
            return ""

~~        return force_str(capfirst(self.model._meta.verbose_name_plural))

    verbose_name_plural = property(_get_verbose_name_plural)

    def content_type(self):
        if self.model is None:
            self.log.error("Model could not be found for SearchResult '%s'.", self)
            return ""

        return str(self.model._meta)

    def get_additional_fields(self):
        additional_fields = {}

        for fieldname in self._additional_fields:
            additional_fields[fieldname] = getattr(self, fieldname)

        return additional_fields

    def get_stored_fields(self):
        if self._stored_fields is None:
            from haystack import connections

            try:
                index = connections[DEFAULT_ALIAS].get_unified_index().get_index(self.model)


## ... source file continues with no further force_str examples...

```


## Example 7 from django-import-export
[django-import-export](https://github.com/django-import-export/django-import-export)
([documentation](https://django-import-export.readthedocs.io/en/latest/)
and [PyPI page](https://pypi.org/project/django-import-export/))
is a [Django](/django.html) code library for importing and exporting data
from the Django Admin. The tool supports many export and import formats
such as CSV, JSON and YAML. django-import-export is open source under the
[BSD 2-Clause "Simplified" License](https://github.com/django-import-export/django-import-export/blob/master/LICENSE).

[**django-import-export / import_export / widgets.py**](https://github.com/django-import-export/django-import-export/blob/master/import_export/./widgets.py)

```python
# widgets.py
import json
from datetime import date, datetime
from decimal import Decimal

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.utils import datetime_safe, timezone
from django.utils.dateparse import parse_duration
~~from django.utils.encoding import force_str, smart_str


class Widget:
    def clean(self, value, row=None, *args, **kwargs):
        return value

    def render(self, value, obj=None):
~~        return force_str(value)


class NumberWidget(Widget):

    def is_empty(self, value):
        if isinstance(value, str):
            value = value.strip()
        return value is None or value == ""

    def render(self, value, obj=None):
        return value


class FloatWidget(NumberWidget):

    def clean(self, value, row=None, *args, **kwargs):
        if self.is_empty(value):
            return None
        return float(value)


class IntegerWidget(NumberWidget):

    def clean(self, value, row=None, *args, **kwargs):
        if self.is_empty(value):
            return None
        return int(float(value))


class DecimalWidget(NumberWidget):

    def clean(self, value, row=None, *args, **kwargs):
        if self.is_empty(value):
            return None
        return Decimal(force_str(value))


class CharWidget(Widget):

    def render(self, value, obj=None):
~~        return force_str(value)


class BooleanWidget(Widget):
    TRUE_VALUES = ["1", 1, True, "true", "TRUE", "True"]
    FALSE_VALUES = ["0", 0, False, "false", "FALSE", "False"]
    NULL_VALUES = ["", None, "null", "NULL", "none", "NONE", "None"]

    def render(self, value, obj=None):
        if value in self.NULL_VALUES:
            return ""
        return self.TRUE_VALUES[0] if value else self.FALSE_VALUES[0]

    def clean(self, value, row=None, *args, **kwargs):
        if value in self.NULL_VALUES:
            return None
        return True if value in self.TRUE_VALUES else False


class DateWidget(Widget):

    def __init__(self, format=None):
        if format is None:
            if not settings.DATE_INPUT_FORMATS:
                formats = ("%Y-%m-%d",)


## ... source file continues with no further force_str examples...

```


## Example 8 from django-jsonfield
[django-jsonfield](https://github.com/dmkoch/django-jsonfield)
([jsonfield on PyPi](https://pypi.org/project/jsonfield/)) is a
[Django](/django.html) code library that makes it easier to store validated
JSON in a [Django object-relational mapper (ORM)](/django-orm.html) database
model.

The django-jsonfield project is open source under the
[MIT license](https://github.com/dmkoch/django-jsonfield/blob/master/LICENSE).

[**django-jsonfield / src/jsonfield / encoder.py**](https://github.com/dmkoch/django-jsonfield/blob/master/src/jsonfield/./encoder.py)

```python
# encoder.py
import datetime
import decimal
import json
import uuid

from django.db.models.query import QuerySet
from django.utils import timezone
~~from django.utils.encoding import force_str
from django.utils.functional import Promise


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):  # noqa: C901
        if isinstance(obj, Promise):
~~            return force_str(obj)
        elif isinstance(obj, datetime.datetime):
            representation = obj.isoformat()
            if representation.endswith('+00:00'):
                representation = representation[:-6] + 'Z'
            return representation
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, datetime.time):
            if timezone and timezone.is_aware(obj):
                raise ValueError("JSON can't represent timezone-aware times.")
            representation = obj.isoformat()
            return representation
        elif isinstance(obj, datetime.timedelta):
            return str(obj.total_seconds())
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        elif isinstance(obj, uuid.UUID):
            return str(obj)
        elif isinstance(obj, QuerySet):
            return tuple(obj)
        elif isinstance(obj, bytes):
            return obj.decode()
        elif hasattr(obj, 'tolist'):
            return obj.tolist()


## ... source file continues with no further force_str examples...

```


## Example 9 from django-oauth-toolkit
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

[**django-oauth-toolkit / oauth2_provider / validators.py**](https://github.com/jazzband/django-oauth-toolkit/blob/master/oauth2_provider/./validators.py)

```python
# validators.py
import re
from urllib.parse import urlsplit

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
~~from django.utils.encoding import force_str


class URIValidator(URLValidator):
    scheme_re = r"^(?:[a-z][a-z0-9\.\-\+]*)://"

    dotless_domain_re = r"(?!-)[A-Z\d-]{1,63}(?<!-)"
    host_re = "|".join((
        r"(?:" + URLValidator.host_re,
        URLValidator.ipv4_re,
        URLValidator.ipv6_re,
        dotless_domain_re + ")"
    ))
    port_re = r"(?::\d{2,5})?"
    path_re = r"(?:[/?#][^\s]*)?"
    regex = re.compile(scheme_re + host_re + port_re + path_re, re.IGNORECASE)


class RedirectURIValidator(URIValidator):
    def __init__(self, allowed_schemes, allow_fragments=False):
        super().__init__(schemes=allowed_schemes)
        self.allow_fragments = allow_fragments

    def __call__(self, value):
        super().__call__(value)
~~        value = force_str(value)
        scheme, netloc, path, query, fragment = urlsplit(value)
        if fragment and not self.allow_fragments:
            raise ValidationError("Redirect URIs must not contain fragments")



class WildcardSet(set):
    def __contains__(self, item):
        return True



## ... source file continues with no further force_str examples...

```


## Example 10 from django-rest-framework
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

[**django-rest-framework / rest_framework / metadata.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./metadata.py)

```python
# metadata.py
from collections import OrderedDict

from django.core.exceptions import PermissionDenied
from django.http import Http404
~~from django.utils.encoding import force_str

from rest_framework import exceptions, serializers
from rest_framework.request import clone_request
from rest_framework.utils.field_mapping import ClassLookupDict


class BaseMetadata:
    def determine_metadata(self, request, view):
        raise NotImplementedError(".determine_metadata() must be overridden.")


class SimpleMetadata(BaseMetadata):
    label_lookup = ClassLookupDict({
        serializers.Field: 'field',
        serializers.BooleanField: 'boolean',
        serializers.NullBooleanField: 'boolean',
        serializers.CharField: 'string',
        serializers.UUIDField: 'string',
        serializers.URLField: 'url',
        serializers.EmailField: 'email',
        serializers.RegexField: 'regex',
        serializers.SlugField: 'slug',
        serializers.IntegerField: 'integer',
        serializers.FloatField: 'float',


## ... source file abbreviated to get to force_str examples ...


        return actions

    def get_serializer_info(self, serializer):
        if hasattr(serializer, 'child'):
            serializer = serializer.child
        return OrderedDict([
            (field_name, self.get_field_info(field))
            for field_name, field in serializer.fields.items()
            if not isinstance(field, serializers.HiddenField)
        ])

    def get_field_info(self, field):
        field_info = OrderedDict()
        field_info['type'] = self.label_lookup[field]
        field_info['required'] = getattr(field, 'required', False)

        attrs = [
            'read_only', 'label', 'help_text',
            'min_length', 'max_length',
            'min_value', 'max_value'
        ]

        for attr in attrs:
            value = getattr(field, attr, None)
            if value is not None and value != '':
~~                field_info[attr] = force_str(value, strings_only=True)

        if getattr(field, 'child', None):
            field_info['child'] = self.get_field_info(field.child)
        elif getattr(field, 'fields', None):
            field_info['children'] = self.get_serializer_info(field)

        if (not field_info.get('read_only') and
            not isinstance(field, (serializers.RelatedField, serializers.ManyRelatedField)) and
                hasattr(field, 'choices')):
            field_info['choices'] = [
                {
                    'value': choice_value,
~~                    'display_name': force_str(choice_name, strings_only=True)
                }
                for choice_value, choice_name in field.choices.items()
            ]

        return field_info



## ... source file continues with no further force_str examples...

```


## Example 11 from django-tables2
[django-tables2](https://github.com/jieter/django-tables2)
([projection documentation](https://django-tables2.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-tables2/))
is a code library for [Django](/django.html) that simplifies creating and
displaying tables in [Django templates](/django-templates.html),
especially with more advanced features such as pagination and sorting.
The project and its code are
[available as open source](https://github.com/jieter/django-tables2/blob/master/LICENSE).

[**django-tables2 / django_tables2 / tables.py**](https://github.com/jieter/django-tables2/blob/master/django_tables2/./tables.py)

```python
# tables.py
import copy
from collections import OrderedDict
from itertools import count

from django.conf import settings
from django.core.paginator import Paginator
from django.db import models
from django.template.loader import get_template
~~from django.utils.encoding import force_str

from . import columns
from .config import RequestConfig
from .data import TableData
from .rows import BoundRows
from .utils import Accessor, AttributeDict, OrderBy, OrderByTuple, Sequence


class DeclarativeColumnsMetaclass(type):

    def __new__(mcs, name, bases, attrs):
        attrs["_meta"] = opts = TableOptions(attrs.get("Meta", None), name)

        cols, remainder = [], {}
        for attr_name, attr in attrs.items():
            if isinstance(attr, columns.Column):
                attr._explicit = True
                cols.append((attr_name, attr))
            else:
                remainder[attr_name] = attr
        attrs = remainder

        cols.sort(key=lambda x: x[1].creation_counter)



## ... source file abbreviated to get to force_str examples ...


        return

    def as_html(self, request):
        self._counter = count()
        template = get_template(self.template_name)

        context = {"table": self, "request": request}

        self.before_render(request)
        return template.render(context)

    def as_values(self, exclude_columns=None):
        if exclude_columns is None:
            exclude_columns = ()

        columns = [
            column
            for column in self.columns.iterall()
            if not (column.column.exclude_from_export or column.name in exclude_columns)
        ]

        yield [force_str(column.header, strings_only=True) for column in columns]

        for row in self.rows:
            yield [
~~                force_str(row.get_cell_value(column.name), strings_only=True) for column in columns
            ]

    def has_footer(self):
        return self.show_footer and any(column.has_footer() for column in self.columns)

    @property
    def show_header(self):
        return self._show_header if self._show_header is not None else self._meta.show_header

    @show_header.setter
    def show_header(self, value):
        self._show_header = value

    @property
    def order_by(self):
        return self._order_by

    @order_by.setter
    def order_by(self, value):
        order_by = () if not value else value
        order_by = order_by.split(",") if isinstance(order_by, str) else order_by
        valid = []

        for alias in order_by:


## ... source file continues with no further force_str examples...

```


## Example 12 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / core / fields.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/core/fields.py)

```python
# fields.py
import json
from html import unescape

from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
~~from django.utils.encoding import force_str
from django.utils.html import strip_tags

from wagtail.core.blocks import Block, BlockField, StreamBlock, StreamValue


class RichTextField(models.TextField):
    def __init__(self, *args, **kwargs):
        self.editor = kwargs.pop('editor', 'default')
        self.features = kwargs.pop('features', None)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from wagtail.admin.rich_text import get_rich_text_editor_widget
        defaults = {'widget': get_rich_text_editor_widget(self.editor, features=self.features)}
        defaults.update(kwargs)
        return super().formfield(**defaults)

    def get_searchable_content(self, value):
~~        source = force_str(value)
        return [unescape(strip_tags(source))]


class Creator:
    def __init__(self, field):
        self.field = field

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        field_name = self.field.name

        if field_name not in obj.__dict__:
            obj.refresh_from_db(fields=[field_name])
        return obj.__dict__[field_name]

    def __set__(self, obj, value):
        obj.__dict__[self.field.name] = self.field.to_python(value)


class StreamField(models.Field):
    def __init__(self, block_types, **kwargs):
        super().__init__(**kwargs)
        if isinstance(block_types, Block):


## ... source file continues with no further force_str examples...

```

