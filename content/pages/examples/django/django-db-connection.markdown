title: django.db connection Example Code
category: page
slug: django-db-connection-examples
sortorder: 500011164
toc: False
sidebartitle: django.db connection
meta: Python example code for the connection callable from the django.db module of the Django project.


connection is a callable within the django.db module of the Django project.


## Example 1 from django-guardian
[django-guardian](https://github.com/django-guardian/django-guardian)
([project documentation](https://django-guardian.readthedocs.io/en/stable/)
and
[PyPI page](https://pypi.org/project/django-guardian/))
provides per-object permissions in [Django](/django.html) projects
by enhancing the existing authentication backend. The project's code
is open source under the
[MIT license](https://github.com/django-guardian/django-guardian/blob/devel/LICENSE).

[**django-guardian / guardian / shortcuts.py**](https://github.com/django-guardian/django-guardian/blob/devel/guardian/./shortcuts.py)

```python
# shortcuts.py
import warnings
from collections import defaultdict
from functools import partial
from itertools import groupby

from django.apps import apps
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
~~from django.db import connection
from django.db.models import Count, Q, QuerySet
from django.shortcuts import _get_queryset
from django.db.models.expressions import Value
from django.db.models.functions import Cast, Replace
from django.db.models import (
    AutoField,
    BigIntegerField,
    CharField,
    ForeignKey,
    IntegerField,
    PositiveIntegerField,
    PositiveSmallIntegerField,
    SmallIntegerField,
    UUIDField,
)
from guardian.core import ObjectPermissionChecker
from guardian.ctypes import get_content_type
from guardian.exceptions import MixedContentTypeError, WrongAppError, MultipleIdentityAndObjectError
from guardian.utils import get_anonymous_user, get_group_obj_perms_model, get_identity, get_user_obj_perms_model
GroupObjectPermission = get_group_obj_perms_model()
UserObjectPermission = get_user_obj_perms_model()


def assign_perm(perm, user_or_group, obj=None):


## ... source file abbreviated to get to connection examples ...



    values = values.values_list(field_pk, flat=True)
    return queryset.filter(pk__in=values)


def _handle_pk_field(queryset):
    pk = queryset.model._meta.pk

    if isinstance(pk, ForeignKey):
        return _handle_pk_field(pk.target_field)

    if isinstance(
        pk,
        (
            IntegerField,
            AutoField,
            BigIntegerField,
            PositiveIntegerField,
            PositiveSmallIntegerField,
            SmallIntegerField,
        ),
    ):
        return partial(Cast, output_field=BigIntegerField())

    if isinstance(pk, UUIDField):
~~        if connection.features.has_native_uuid_field:
            return partial(Cast, output_field=UUIDField())
        return partial(
            Replace,
            text=Value('-'),
            replacement=Value(''),
            output_field=CharField(),
        )

    return None



## ... source file continues with no further connection examples...

```


## Example 2 from django-push-notifications
[django-push-notifications](https://github.com/jazzband/django-push-notifications)
is a [Django](/django.html) app for storing and interacting with
push notification services such as
[Google's Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/)
and
[Apple Notifications](https://developer.apple.com/notifications/).
The django-push-notification project's source code is available
open source under the
[MIT license](https://github.com/jazzband/django-push-notifications/blob/master/LICENSE).

[**django-push-notifications / push_notifications / fields.py**](https://github.com/jazzband/django-push-notifications/blob/master/push_notifications/./fields.py)

```python
# fields.py
import re
import struct

from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
~~from django.db import connection, models
from django.utils.translation import ugettext_lazy as _


__all__ = ["HexadecimalField", "HexIntegerField"]

UNSIGNED_64BIT_INT_MIN_VALUE = 0
UNSIGNED_64BIT_INT_MAX_VALUE = 2 ** 64 - 1


hex_re = re.compile(r"^(([0-9A-f])|(0x[0-9A-f]))+$")
signed_integer_engines = [
	"django.db.backends.postgresql",
	"django.db.backends.postgresql_psycopg2",
	"django.contrib.gis.db.backends.postgis",
	"django.db.backends.sqlite3"
]


def _using_signed_storage():
~~	return connection.settings_dict["ENGINE"] in signed_integer_engines


def _signed_to_unsigned_integer(value):
	return struct.unpack("Q", struct.pack("q", value))[0]


def _unsigned_to_signed_integer(value):
	return struct.unpack("q", struct.pack("Q", value))[0]


def _hex_string_to_unsigned_integer(value):
	return int(value, 16)


def _unsigned_integer_to_hex_string(value):
	return hex(value).rstrip("L")


class HexadecimalField(forms.CharField):
	def __init__(self, *args, **kwargs):
		self.default_validators = [
			RegexValidator(hex_re, _("Enter a valid hexadecimal number"), "invalid")
		]
		super(HexadecimalField, self).__init__(*args, **kwargs)

	def prepare_value(self, value):
		if value and not isinstance(value, str) \
~~			and connection.vendor in ("mysql", "sqlite"):
			value = _unsigned_integer_to_hex_string(value)
		return super(forms.CharField, self).prepare_value(value)


class HexIntegerField(models.BigIntegerField):

	validators = [
		MinValueValidator(UNSIGNED_64BIT_INT_MIN_VALUE),
		MaxValueValidator(UNSIGNED_64BIT_INT_MAX_VALUE)
	]

	def db_type(self, connection):
~~		engine = connection.settings_dict["ENGINE"]
		if "mysql" in engine:
			return "bigint unsigned"
		elif "sqlite" in engine:
			return "UNSIGNED BIG INT"
		else:
			return super(HexIntegerField, self).db_type(connection=connection)

	def get_prep_value(self, value):
		if value is None or value == "":
			return None
		if isinstance(value, str):
			value = _hex_string_to_unsigned_integer(value)
		if _using_signed_storage():
			value = _unsigned_to_signed_integer(value)
		return value

	def from_db_value(self, value, *args):
		if value is None:
			return value
		if _using_signed_storage():
			value = _signed_to_unsigned_integer(value)
		return value

	def to_python(self, value):


## ... source file continues with no further connection examples...

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

[**django-rest-framework / rest_framework / views.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./views.py)

```python
# views.py
from django.conf import settings
from django.core.exceptions import PermissionDenied
~~from django.db import connection, models, transaction
from django.http import Http404
from django.http.response import HttpResponseBase
from django.utils.cache import cc_delim_re, patch_vary_headers
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from rest_framework import exceptions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.schemas import DefaultSchema
from rest_framework.settings import api_settings
from rest_framework.utils import formatting


def get_view_name(view):
    name = getattr(view, 'name', None)
    if name is not None:
        return name

    name = view.__class__.__name__
    name = formatting.remove_trailing_string(name, 'View')
    name = formatting.remove_trailing_string(name, 'ViewSet')
    name = formatting.camelcase_to_spaces(name)

    suffix = getattr(view, 'suffix', None)
    if suffix:
        name += ' ' + suffix

    return name


def get_view_description(view, html=False):
    description = getattr(view, 'description', None)
    if description is None:
        description = view.__class__.__doc__ or ''

    description = formatting.dedent(smart_str(description))
    if html:
        return formatting.markup_description(description)
    return description


def set_rollback():
~~    atomic_requests = connection.settings_dict.get('ATOMIC_REQUESTS', False)
~~    if atomic_requests and connection.in_atomic_block:
        transaction.set_rollback(True)


def exception_handler(exc, context):
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, (list, dict)):
            data = exc.detail
        else:
            data = {'detail': exc.detail}

        set_rollback()
        return Response(data, status=exc.status_code, headers=headers)



## ... source file continues with no further connection examples...

```


## Example 4 from django-sql-explorer
[django-sql-explorer](https://github.com/groveco/django-sql-explorer)
([PyPI page](https://pypi.org/project/django-sql-explorer/0.2/)),
also referred to as "SQL Explorer",
is a code library for the [Django](/django.html) Admin that allows
approved, authenticated users to view and execute direct database SQL
queries. The tool keeps track of executed queries so users can share them
with each other, as well as export results to downloadable formats.
django-sql-explorer is provided as open source under the
[MIT license](https://github.com/groveco/django-sql-explorer/blob/master/LICENSE).

[**django-sql-explorer / explorer / apps.py**](https://github.com/groveco/django-sql-explorer/blob/master/explorer/./apps.py)

```python
# apps.py
from django.apps import AppConfig
~~from django.db import connections as djcs
from django.core.exceptions import ImproperlyConfigured


class ExplorerAppConfig(AppConfig):

    name = 'explorer'

    def ready(self):
        from explorer.schema import build_async_schemas
        _validate_connections()
        build_async_schemas()


def _get_default():
    from explorer.app_settings import EXPLORER_DEFAULT_CONNECTION
    return EXPLORER_DEFAULT_CONNECTION


def _get_explorer_connections():
    from explorer.app_settings import EXPLORER_CONNECTIONS
    return EXPLORER_CONNECTIONS


def _validate_connections():

    if _get_default() not in _get_explorer_connections().values():
        raise ImproperlyConfigured(
            'EXPLORER_DEFAULT_CONNECTION is %s, but that alias is not present in the values of EXPLORER_CONNECTIONS'
            % _get_default())

    for name, conn_name in _get_explorer_connections().items():
        if conn_name not in djcs:
            raise ImproperlyConfigured(
~~                'EXPLORER_CONNECTIONS contains (%s, %s), but %s is not a valid Django DB connection.'
                % (name, conn_name, conn_name))



## ... source file continues with no further connection examples...

```


## Example 5 from django-taggit
[django-taggit](https://github.com/jazzband/django-taggit/)
([PyPI page](https://pypi.org/project/django-taggit/)) provides a way
to create, store, manage and use tags in a [Django](/django.html) project.
The code for django-taggit is
[open source](https://github.com/jazzband/django-taggit/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-taggit / taggit / managers.py**](https://github.com/jazzband/django-taggit/blob/master/taggit/./managers.py)

```python
# managers.py
import uuid
from operator import attrgetter

from django import VERSION
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
~~from django.db import connections, models, router
from django.db.models import signals
from django.db.models.fields.related import (
    ManyToManyRel,
    OneToOneRel,
    RelatedField,
    lazy_related_operation,
)
from django.db.models.query_utils import PathInfo
from django.utils.text import capfirst
from django.utils.translation import gettext_lazy as _

from taggit.forms import TagField
from taggit.models import (
    CommonGenericTaggedItemBase,
    GenericUUIDTaggedItemBase,
    TaggedItem,
)
from taggit.utils import require_instance_manager


class ExtraJoinRestriction:

    contains_aggregate = False



## ... source file abbreviated to get to connection examples ...


            kwargs = extra_filters if extra_filters else {}
            return self.through.tags_for(self.model, self.instance, **kwargs)

    def get_prefetch_queryset(self, instances, queryset=None):
        if queryset is not None:
            raise ValueError("Custom queryset can't be used for this lookup.")

        instance = instances[0]
        db = self._db or router.db_for_read(type(instance), instance=instance)

        fieldname = (
            "object_id"
            if issubclass(self.through, CommonGenericTaggedItemBase)
            else "content_object"
        )
        fk = self.through._meta.get_field(fieldname)
        query = {
            "%s__%s__in"
            % (self.through.tag_relname(), fk.name): {
                obj._get_pk_val() for obj in instances
            }
        }
        join_table = self.through._meta.db_table
        source_col = fk.column
        connection = connections[db]
~~        qn = connection.ops.quote_name
        qs = (
            self.get_queryset(query)
            .using(db)
            .extra(
                select={
                    "_prefetch_related_val": "{}.{}".format(
                        qn(join_table), qn(source_col)
                    )
                }
            )
        )

        if issubclass(self.through, GenericUUIDTaggedItemBase):

            def uuid_rel_obj_attr(v):
                value = attrgetter("_prefetch_related_val")(v)
                if value is not None and not isinstance(value, uuid.UUID):
                    input_form = "int" if isinstance(value, int) else "hex"
                    value = uuid.UUID(**{input_form: value})
                return value

            rel_obj_attr = uuid_rel_obj_attr
        else:
            rel_obj_attr = attrgetter("_prefetch_related_val")


## ... source file continues with no further connection examples...

```

