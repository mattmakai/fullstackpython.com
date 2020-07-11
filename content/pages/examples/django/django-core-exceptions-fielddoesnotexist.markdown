title: django.core.exceptions FieldDoesNotExist Example Code
category: page
slug: django-core-exceptions-fielddoesnotexist-examples
sortorder: 500011099
toc: False
sidebartitle: django.core.exceptions FieldDoesNotExist
meta: Python example code for the FieldDoesNotExist class from the django.core.exceptions module of the Django project.


FieldDoesNotExist is a class within the django.core.exceptions module of the Django project.


## Example 1 from AuditLog
[Auditlog](https://github.com/jjkester/django-auditlog)
([project documentation](https://django-auditlog.readthedocs.io/en/latest/))
is a [Django](/django.html) app that logs changes to Python objects,
similar to the Django admin's logs but with more details and
output formats. Auditlog's source code is provided as open source under the
[MIT license](https://github.com/jjkester/django-auditlog/blob/master/LICENSE).

[**AuditLog / src / auditlog / models.py**](https://github.com/jjkester/django-auditlog/blob/master/src/auditlog/models.py)

```python
# models.py
from __future__ import unicode_literals

import json
import ast

from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
~~from django.core.exceptions import FieldDoesNotExist
from django.db import models, DEFAULT_DB_ALIAS
from django.db.models import QuerySet, Q
from django.utils import formats, timezone
from django.utils.encoding import python_2_unicode_compatible, smart_text
from django.utils.six import iteritems, integer_types
from django.utils.translation import ugettext_lazy as _

from jsonfield.fields import JSONField
from dateutil import parser
from dateutil.tz import gettz


class LogEntryManager(models.Manager):

    def log_create(self, instance, **kwargs):
        changes = kwargs.get('changes', None)
        pk = self._get_pk_value(instance)

        if changes is not None:
            kwargs.setdefault('content_type', ContentType.objects.get_for_model(instance))
            kwargs.setdefault('object_pk', pk)
            kwargs.setdefault('object_repr', smart_text(instance))

            if isinstance(pk, integer_types):


## ... source file abbreviated to get to FieldDoesNotExist examples ...


    @property
    def changes_str(self, colon=': ', arrow=smart_text(' \u2192 '), separator='; '):
        substrings = []

        for field, values in iteritems(self.changes_dict):
            substring = smart_text('{field_name:s}{colon:s}{old:s}{arrow:s}{new:s}').format(
                field_name=field,
                colon=colon,
                old=values[0],
                arrow=arrow,
                new=values[1],
            )
            substrings.append(substring)

        return separator.join(substrings)

    @property
    def changes_display_dict(self):
        from auditlog.registry import auditlog
        model = self.content_type.model_class()
        model_fields = auditlog.get_model_fields(model._meta.model)
        changes_display_dict = {}
        for field_name, values in iteritems(self.changes_dict):
            try:
                field = model._meta.get_field(field_name)
~~            except FieldDoesNotExist:
                changes_display_dict[field_name] = values
                continue
            values_display = []
            choices_dict = None
            if hasattr(field, 'choices') and len(field.choices) > 0:
                choices_dict = dict(field.choices)
            if hasattr(field, 'base_field') and getattr(field.base_field, 'choices', False):
                choices_dict = dict(field.base_field.choices)

            if choices_dict:
                for value in values:
                    try:
                        value = ast.literal_eval(value)
                        if type(value) is [].__class__:
                            values_display.append(', '.join([choices_dict.get(val, 'None') for val in value]))
                        else:
                            values_display.append(choices_dict.get(value, 'None'))
                    except ValueError:
                        values_display.append(choices_dict.get(value, 'None'))
                    except:
                        values_display.append(choices_dict.get(value, 'None'))
            else:
                try:
                    field_type = field.get_internal_type()


## ... source file continues with no further FieldDoesNotExist examples...

```


## Example 2 from django-allauth
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
~~from django.core.exceptions import FieldDoesNotExist, ImproperlyConfigured
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
from django.utils.encoding import force_bytes, force_str


MAX_USERNAME_SUFFIX_LENGTH = 7
USERNAME_SUFFIX_CHARS = (
    [string.digits] * 4 +
    [string.ascii_letters] * (MAX_USERNAME_SUFFIX_LENGTH - 4))


def _generate_unique_username_base(txts, regex=None):
    from .account.adapter import get_adapter
    adapter = get_adapter()
    username = None


## ... source file abbreviated to get to FieldDoesNotExist examples ...


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
                v = force_str(base64.b64encode(v))
            elif isinstance(field, FileField):
                if v and not isinstance(v, str):
                    v = v.name
            try:
                json.dumps(v, cls=DjangoJSONEncoder)
            except TypeError:
                v = field.get_prep_value(v)
                k = SERIALIZED_DB_FIELD_PREFIX + k
~~        except FieldDoesNotExist:
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
                if isinstance(f, DateTimeField):
                    v = dateparse.parse_datetime(v)
                elif isinstance(f, TimeField):
                    v = dateparse.parse_time(v)
                elif isinstance(f, DateField):
                    v = dateparse.parse_date(v)
                elif isinstance(f, BinaryField):
                    v = force_bytes(
                        base64.b64decode(
                            force_bytes(v)))
                elif is_db_value:
                    try:
                        if django.VERSION < (3, 0):
                            v = f.from_db_value(v, None, None, None)
                        else:
                            v = f.from_db_value(v, None, None)
                    except Exception:
                        raise ImproperlyConfigured(
                            "Unable to auto serialize field '{}', custom"
                            " serialization override required".format(k)
                        )
~~            except FieldDoesNotExist:
                pass
        setattr(ret, k, v)
    return ret


def set_form_field_order(form, field_order):
    if field_order is None:
        return
    fields = OrderedDict()
    for key in field_order:
        try:
            fields[key] = form.fields.pop(key)
        except KeyError:  # ignore unknown fields
            pass
    fields.update(form.fields)  # add remaining fields in original order
    form.fields = fields


def build_absolute_uri(request, location, protocol=None):
    from .account import app_settings as account_settings

    if request is None:
        site = Site.objects.get_current()
        bits = urlsplit(location)


## ... source file continues with no further FieldDoesNotExist examples...

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

[**django-filter / django_filters / utils.py**](https://github.com/carltongibson/django-filter/blob/master/django_filters/./utils.py)

```python
# utils.py
import warnings
from collections import OrderedDict

from django.conf import settings
~~from django.core.exceptions import FieldDoesNotExist, FieldError
from django.db import models
from django.db.models.constants import LOOKUP_SEP
from django.db.models.expressions import Expression
from django.db.models.fields.related import ForeignObjectRel, RelatedField
from django.utils import timezone
from django.utils.encoding import force_str
from django.utils.text import capfirst
from django.utils.translation import gettext as _

from .exceptions import FieldLookupError


def deprecate(msg, level_modifier=0):
    warnings.warn(msg, MigrationNotice, stacklevel=3 + level_modifier)


class MigrationNotice(DeprecationWarning):
    url = 'https://django-filter.readthedocs.io/en/master/guide/migration.html'

    def __init__(self, message):
        super().__init__('%s See: %s' % (message, self.url))


class RenameAttributesBase(type):


## ... source file abbreviated to get to FieldDoesNotExist examples ...




def get_all_model_fields(model):
    opts = model._meta

    return [
        f.name for f in sorted(opts.fields + opts.many_to_many)
        if not isinstance(f, models.AutoField) and
        not (getattr(f.remote_field, 'parent_link', False))
    ]


def get_model_field(model, field_name):
    fields = get_field_parts(model, field_name)
    return fields[-1] if fields else None


def get_field_parts(model, field_name):
    parts = field_name.split(LOOKUP_SEP)
    opts = model._meta
    fields = []

    for name in parts:
        try:
            field = opts.get_field(name)
~~        except FieldDoesNotExist:
            return None

        fields.append(field)
        if isinstance(field, RelatedField):
            opts = field.remote_field.model._meta
        elif isinstance(field, ForeignObjectRel):
            opts = field.related_model._meta

    return fields


def resolve_field(model_field, lookup_expr):
    query = model_field.model._default_manager.all().query
    lhs = Expression(model_field)
    lookups = lookup_expr.split(LOOKUP_SEP)

    assert len(lookups) > 0

    try:
        while lookups:
            name = lookups[0]
            args = (lhs, name)
            if len(lookups) == 1:
                final_lookup = lhs.get_lookup(name)


## ... source file continues with no further FieldDoesNotExist examples...

```


## Example 4 from django-guardian
[django-guardian](https://github.com/django-guardian/django-guardian)
([project documentation](https://django-guardian.readthedocs.io/en/stable/)
and
[PyPI page](https://pypi.org/project/django-guardian/))
provides per-object permissions in [Django](/django.html) projects
by enhancing the existing authentication backend. The project's code
is open source under the
[MIT license](https://github.com/django-guardian/django-guardian/blob/devel/LICENSE).

[**django-guardian / guardian / managers.py**](https://github.com/django-guardian/django-guardian/blob/devel/guardian/./managers.py)

```python
# managers.py
~~from django.core.exceptions import FieldDoesNotExist
from django.db import models
from django.db.models import Q
from guardian.core import ObjectPermissionChecker
from guardian.ctypes import get_content_type
from guardian.exceptions import ObjectNotPersisted
from django.contrib.auth.models import Permission

import warnings


class BaseObjectPermissionManager(models.Manager):

    @property
    def user_or_group_field(self):
        try:
            self.model._meta.get_field('user')
            return 'user'
~~        except FieldDoesNotExist:
            return 'group'

    def is_generic(self):
        try:
            self.model._meta.get_field('object_pk')
            return True
~~        except FieldDoesNotExist:
            return False

    def assign_perm(self, perm, user_or_group, obj):
        if getattr(obj, 'pk', None) is None:
            raise ObjectNotPersisted("Object %s needs to be persisted first"
                                     % obj)
        ctype = get_content_type(obj)
        if not isinstance(perm, Permission):
            permission = Permission.objects.get(content_type=ctype, codename=perm)
        else:
            permission = perm

        kwargs = {'permission': permission, self.user_or_group_field: user_or_group}
        if self.is_generic():
            kwargs['content_type'] = ctype
            kwargs['object_pk'] = obj.pk
        else:
            kwargs['content_object'] = obj
        obj_perm, _ = self.get_or_create(**kwargs)
        return obj_perm

    def bulk_assign_perm(self, perm, user_or_group, queryset):
        if isinstance(queryset, list):
            ctype = get_content_type(queryset[0])


## ... source file continues with no further FieldDoesNotExist examples...

```


## Example 5 from django-import-export
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
import django
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, ValidationError
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
~~    from django.core.exceptions import FieldDoesNotExist
else:
    from django.db.models.fields import FieldDoesNotExist


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

USE_TRANSACTIONS = getattr(settings, 'IMPORT_EXPORT_USE_TRANSACTIONS', True)
CHUNK_SIZE = getattr(settings, 'IMPORT_EXPORT_CHUNK_SIZE', 1)


def get_related_model(field):
    if hasattr(field, 'related_model'):
        return field.related_model
    if field.rel:
        return field.rel.to


class ResourceOptions:

    model = None
    fields = None

    exclude = None


## ... source file abbreviated to get to FieldDoesNotExist examples ...


                    continue

                field = new_class.field_from_django_field(f.name, f,
                                                          readonly=False)
                field_list.append((f.name, field, ))

            new_class.fields.update(OrderedDict(field_list))

            if opts.fields is not None:
                field_list = []
                for field_name in opts.fields:
                    if field_name in declared_fields:
                        continue
                    if field_name.find('__') == -1:
                        continue

                    model = opts.model
                    attrs = field_name.split('__')
                    for i, attr in enumerate(attrs):
                        verbose_path = ".".join([opts.model.__name__] + attrs[0:i+1])

                        try:
                            f = model._meta.get_field(attr)
~~                        except FieldDoesNotExist as e:
                            logger.debug(e, exc_info=e)
~~                            raise FieldDoesNotExist(
                                "%s: %s has no field named '%s'" %
                                (verbose_path, model.__name__, attr))

                        if i < len(attrs) - 1:
                            if isinstance(f, ForeignObjectRel):
                                model = get_related_model(f)
                            else:
                                if get_related_model(f) is None:
                                    raise KeyError(
                                        '%s is not a relation' % verbose_path)
                                model = get_related_model(f)

                    if isinstance(f, ForeignObjectRel):
                        f = f.field

                    field = new_class.field_from_django_field(field_name, f,
                                                              readonly=True)
                    field_list.append((field_name, field))

                new_class.fields.update(OrderedDict(field_list))

        return new_class


                    continue
                if f.name in declared_fields:


## ... source file continues with no further FieldDoesNotExist examples...

```


## Example 6 from django-rest-framework
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

[**django-rest-framework / rest_framework / serializers.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./serializers.py)

```python
# serializers.py
import copy
import inspect
import traceback
from collections import OrderedDict, defaultdict
from collections.abc import Mapping

~~from django.core.exceptions import FieldDoesNotExist, ImproperlyConfigured
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models
from django.db.models.fields import Field as DjangoModelField
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from rest_framework.compat import postgres_fields
from rest_framework.exceptions import ErrorDetail, ValidationError
from rest_framework.fields import get_error_detail, set_value
from rest_framework.settings import api_settings
from rest_framework.utils import html, model_meta, representation
from rest_framework.utils.field_mapping import (
    ClassLookupDict, get_field_kwargs, get_nested_relation_kwargs,
    get_relation_kwargs, get_url_kwargs
)
from rest_framework.utils.serializer_helpers import (
    BindingDict, BoundField, JSONBoundField, NestedBoundField, ReturnDict,
    ReturnList
)
from rest_framework.validators import (
    UniqueForDateValidator, UniqueForMonthValidator, UniqueForYearValidator,
    UniqueTogetherValidator
)


## ... source file abbreviated to get to FieldDoesNotExist examples ...


            extra_kwargs[key] = value

        return extra_kwargs, hidden_fields

    def _get_model_fields(self, field_names, declared_fields, extra_kwargs):
        model = getattr(self.Meta, 'model')
        model_fields = {}

        for field_name in field_names:
            if field_name in declared_fields:
                field = declared_fields[field_name]
                source = field.source or field_name
            else:
                try:
                    source = extra_kwargs[field_name]['source']
                except KeyError:
                    source = field_name

            if '.' in source or source == '*':
                continue

            try:
                field = model._meta.get_field(source)
                if isinstance(field, DjangoModelField):
                    model_fields[source] = field
~~            except FieldDoesNotExist:
                pass

        return model_fields


    def get_validators(self):
        validators = getattr(getattr(self, 'Meta', None), 'validators', None)
        if validators is not None:
            return list(validators)

        return (
            self.get_unique_together_validators() +
            self.get_unique_for_date_validators()
        )

    def get_unique_together_validators(self):
        model_class_inheritance_tree = (
            [self.Meta.model] +
            list(self.Meta.model._meta.parents)
        )

        field_sources = OrderedDict(
            (field.field_name, field.source) for field in self._writable_fields
            if (field.source != '*') and ('.' not in field.source)


## ... source file continues with no further FieldDoesNotExist examples...

```


## Example 7 from django-tables2
[django-tables2](https://github.com/jieter/django-tables2)
([projection documentation](https://django-tables2.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-tables2/))
is a code library for [Django](/django.html) that simplifies creating and
displaying tables in [Django templates](/django-templates.html),
especially with more advanced features such as pagination and sorting.
The project and its code are
[available as open source](https://github.com/jieter/django-tables2/blob/master/LICENSE).

[**django-tables2 / django_tables2 / utils.py**](https://github.com/jieter/django-tables2/blob/master/django_tables2/./utils.py)

```python
# utils.py
import inspect
import warnings
from collections import OrderedDict
from functools import total_ordering
from itertools import chain

~~from django.core.exceptions import FieldDoesNotExist
from django.db import models
from django.utils.html import format_html_join


class Sequence(list):

    def expand(self, columns):
        ellipses = self.count("...")
        if ellipses > 1:
            raise ValueError("'...' must be used at most once in a sequence.")
        elif ellipses == 0:
            self.append("...")

        columns = list(columns)  # take a copy and exhaust the generator
        head = []
        tail = []
        target = head  # start by adding things to the head
        for name in self:
            if name == "...":
                target = tail
                continue
            target.append(name)
            if name in columns:
                columns.pop(columns.index(name))


## ... source file abbreviated to get to FieldDoesNotExist examples ...


                    if safe and getattr(current, "alters_data", False):
                        raise ValueError(self.ALTERS_DATA_ERROR_FMT.format(method=repr(current)))
                    if not getattr(current, "do_not_call_in_templates", False):
                        current = current()
                if current is None:
                    break
            return current
        except Exception:
            if not quiet:
                raise

    @property
    def bits(self):
        if self == "":
            return ()
        return self.split(self.SEPARATOR)

    def get_field(self, model):
        if not hasattr(model, "_meta"):
            return

        field = None
        for bit in self.bits:
            try:
                field = model._meta.get_field(bit)
~~            except FieldDoesNotExist:
                break

            if hasattr(field, "remote_field"):
                rel = getattr(field, "remote_field", None)
                model = getattr(rel, "model", model)

        return field

    def penultimate(self, context, quiet=True):
        path, _, remainder = self.rpartition(self.SEPARATOR)
        return A(path).resolve(context, quiet=quiet), remainder


A = Accessor  # alias


class AttributeDict(OrderedDict):

    blacklist = ("th", "td", "_ordering", "thead", "tbody", "tfoot")

    def _iteritems(self):
        for key, v in self.items():
            value = v() if callable(v) else v
            if key not in self.blacklist and value is not None:


## ... source file continues with no further FieldDoesNotExist examples...

```


## Example 8 from django-wiki
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

[**django-wiki / src/wiki / forms_account_handling.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/./forms_account_handling.py)

```python
# forms_account_handling.py
import random
import string

import django.contrib.auth.models
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
~~from django.core.exceptions import FieldDoesNotExist
from django.db.models.fields import CharField
from django.db.models.fields import EmailField
from django.utils.translation import gettext_lazy as _
from wiki.conf import settings


def _get_field(model, field):
    try:
        return model._meta.get_field(field)
~~    except FieldDoesNotExist:
        return


User = get_user_model()


def check_user_field(user_model):
    return isinstance(_get_field(user_model, user_model.USERNAME_FIELD), CharField)


def check_email_field(user_model):
    return isinstance(
        _get_field(user_model, user_model.get_email_field_name()), EmailField
    )


CustomUser = (
    User
    if (
        settings.ACCOUNT_HANDLING and check_user_field(User) and check_email_field(User)
    )
    else django.contrib.auth.models.User
)



## ... source file continues with no further FieldDoesNotExist examples...

```


## Example 9 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / admin / edit_handlers.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/admin/edit_handlers.py)

```python
# edit_handlers.py
import functools
import re

from django import forms
~~from django.core.exceptions import FieldDoesNotExist, ImproperlyConfigured
from django.db.models.fields import CharField, TextField
from django.forms.formsets import DELETION_FIELD_NAME, ORDERING_FIELD_NAME
from django.forms.models import fields_for_model
from django.template.loader import render_to_string
from django.utils.functional import cached_property
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy
from taggit.managers import TaggableManager

from wagtail.admin import compare, widgets
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.core.utils import camelcase_to_underscore, resolve_model_string
from wagtail.utils.decorators import cached_classmethod

from .forms.models import (  # NOQA
    DIRECT_FORM_FIELD_OVERRIDES, FORM_FIELD_OVERRIDES, WagtailAdminModelForm, formfield_for_dbfield)
from .forms.pages import WagtailAdminPageForm


def widget_with_script(widget, script):
    return mark_safe('{0}<script>{1}</script>'.format(widget, script))




## ... source file abbreviated to get to FieldDoesNotExist examples ...


    def get_comparison_class(self):
        widget_override = self.widget_overrides().get(self.field_name, None)
        if widget_override and widget_override.is_hidden:
            return

        try:
            field = self.db_field

            if field.choices:
                return compare.ChoiceFieldComparison

            if field.is_relation:
                if isinstance(field, TaggableManager):
                    return compare.TagsFieldComparison
                elif field.many_to_many:
                    return compare.M2MFieldComparison

                return compare.ForeignObjectComparison

            if isinstance(field, RichTextField):
                return compare.RichTextFieldComparison

            if isinstance(field, (CharField, TextField)):
                return compare.TextFieldComparison

~~        except FieldDoesNotExist:
            pass

        return compare.FieldComparison

    def get_comparison(self):
        comparator_class = self.get_comparison_class()

        if comparator_class:
            try:
                return [functools.partial(comparator_class, self.db_field)]
~~            except FieldDoesNotExist:
                return []
        return []

    @cached_property
    def db_field(self):
        try:
            model = self.model
        except AttributeError:
            raise ImproperlyConfigured("%r must be bound to a model before calling db_field" % self)

        return model._meta.get_field(self.field_name)

    def on_form_bound(self):
        self.bound_field = self.form[self.field_name]
        self.heading = self.heading or self.bound_field.label
        self.help_text = self.bound_field.help_text

    def __repr__(self):
        return "<%s '%s' with model=%s instance=%s request=%s form=%s>" % (
            self.__class__.__name__, self.field_name,
            self.model, self.instance, self.request, self.form.__class__.__name__)


class RichTextFieldPanel(FieldPanel):


## ... source file continues with no further FieldDoesNotExist examples...

```

