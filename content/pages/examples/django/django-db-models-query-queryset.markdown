title: django.db.models.query QuerySet Example Code
category: page
slug: django-db-models-query-queryset-examples
sortorder: 500011243
toc: False
sidebartitle: django.db.models.query QuerySet
meta: Python example code for the QuerySet class from the django.db.models.query module of the Django project.


QuerySet is a class within the django.db.models.query module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / publisher / query.py**](https://github.com/divio/django-cms/blob/develop/cms/publisher/query.py)

```python
# query.py
~~from django.db.models.query import QuerySet


~~class PublisherQuerySet(QuerySet):
    def drafts(self):
        return self.filter(publisher_is_draft=True)

    def public(self):
        return self.filter(publisher_is_draft=False)



## ... source file continues with no further QuerySet examples...

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
~~from django.db.models.query import QuerySet
from django.utils.encoding import smart_str
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


## ... source file abbreviated to get to QuerySet examples ...


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
                    or_queries = [models.Q(**{construct_search(smart_str(field_name)): smart_str(bit)}) for field_name in search_fields.split(',')]
~~                    other_qs = QuerySet(model)
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
        return None


## ... source file continues with no further QuerySet examples...

```


## Example 3 from django-guardian
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
~~from django.db.models.query import QuerySet
from django.utils.encoding import force_str

from guardian.conf import settings as guardian_settings
from guardian.ctypes import get_content_type
from guardian.utils import get_group_obj_perms_model, get_identity, get_user_obj_perms_model


def _get_pks_model_and_ctype(objects):

~~    if isinstance(objects, QuerySet):
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

    def __init__(self, user_or_group=None):
        self.user, self.group = get_identity(user_or_group)
        self._obj_perms_cache = {}

    def has_perm(self, perm, obj):
        if self.user and not self.user.is_active:
            return False
        elif self.user and self.user.is_superuser:


## ... source file continues with no further QuerySet examples...

```


## Example 4 from django-import-export
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
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.core.management.color import no_style
from django.core.paginator import Paginator
from django.db import DEFAULT_DB_ALIAS, connections
from django.db.models.fields.related import ForeignObjectRel
~~from django.db.models.query import QuerySet
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
    from django.db.models.fields import FieldDoesNotExist


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


## ... source file abbreviated to get to QuerySet examples ...


        method = getattr(self, 'dehydrate_%s' % field_name, None)
        if method is not None:
            return method(obj)
        return field.export(obj)

    def get_export_fields(self):
        return self.get_fields()

    def export_resource(self, obj):
        return [self.export_field(field, obj) for field in self.get_export_fields()]

    def get_export_headers(self):
        headers = [
            force_str(field.column_name) for field in self.get_export_fields()]
        return headers

    def get_user_visible_headers(self):
        headers = [
            force_str(field.column_name) for field in self.get_user_visible_fields()]
        return headers

    def get_user_visible_fields(self):
        return self.get_fields()

    def iter_queryset(self, queryset):
~~        if not isinstance(queryset, QuerySet):
            yield from queryset
        elif queryset._prefetch_related_lookups:
            if not queryset.query.order_by:
                queryset = queryset.order_by('pk')
            paginator = Paginator(queryset, self.get_chunk_size())
            for index in range(paginator.num_pages):
                yield from paginator.get_page(index + 1)
        else:
            yield from queryset.iterator(chunk_size=self.get_chunk_size())

    def export(self, queryset=None, *args, **kwargs):

        self.before_export(queryset, *args, **kwargs)

        if queryset is None:
            queryset = self.get_queryset()
        headers = self.get_export_headers()
        data = tablib.Dataset(headers=headers)

        for obj in self.iter_queryset(queryset):
            data.append(self.export_resource(obj))

        self.after_export(queryset, data, *args, **kwargs)



## ... source file continues with no further QuerySet examples...

```


## Example 5 from django-jsonfield
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

~~from django.db.models.query import QuerySet
from django.utils import timezone
from django.utils.encoding import force_str
from django.utils.functional import Promise


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):  # noqa: C901
        if isinstance(obj, Promise):
            return force_str(obj)
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
~~        elif isinstance(obj, QuerySet):
            return tuple(obj)
        elif isinstance(obj, bytes):
            return obj.decode()
        elif hasattr(obj, 'tolist'):
            return obj.tolist()
        elif hasattr(obj, '__getitem__'):
            cls = (list if isinstance(obj, (list, tuple)) else dict)
            try:
                return cls(obj)
            except Exception:
                pass
        elif hasattr(obj, '__iter__'):
            return tuple(item for item in obj)
        return super().default(obj)



## ... source file continues with no further QuerySet examples...

```


## Example 6 from django-model-utils
[django-model-utils](https://github.com/jazzband/django-model-utils)
([project documentation](https://django-model-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-model-utils/))
provides useful mixins and utilities for working with
[Django ORM](/django-orm.html) models in your projects.

The django-model-utils project is open sourced under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/jazzband/django-model-utils/blob/master/LICENSE.txt).

[**django-model-utils / model_utils / managers.py**](https://github.com/jazzband/django-model-utils/blob/master/model_utils/./managers.py)

```python
# managers.py
import django
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from django.db import models
from django.db.models.constants import LOOKUP_SEP
from django.db.models.fields.related import OneToOneField, OneToOneRel
from django.db.models.query import ModelIterable
~~from django.db.models.query import QuerySet
from django.db.models.sql.datastructures import Join


class InheritanceIterable(ModelIterable):
    def __iter__(self):
        queryset = self.queryset
        iter = ModelIterable(queryset)
        if getattr(queryset, 'subclasses', False):
            extras = tuple(queryset.query.extra.keys())
            subclasses = sorted(queryset.subclasses, key=len, reverse=True)
            for obj in iter:
                sub_obj = None
                for s in subclasses:
                    sub_obj = queryset._get_sub_obj_recurse(obj, s)
                    if sub_obj:
                        break
                if not sub_obj:
                    sub_obj = obj

                if getattr(queryset, '_annotated', False):
                    for k in queryset._annotated:
                        setattr(sub_obj, k, getattr(obj, k))

                for k in extras:


## ... source file abbreviated to get to QuerySet examples ...


            if levels or levels is None:
                parent_model = related.model
                parent_link = parent_model._meta.get_ancestor_link(
                    self.model)
            else:
                parent_link = None
        return LOOKUP_SEP.join(ancestry)

    def _get_sub_obj_recurse(self, obj, s):
        rel, _, s = s.partition(LOOKUP_SEP)

        try:
            node = getattr(obj, rel)
        except ObjectDoesNotExist:
            return None
        if s:
            child = self._get_sub_obj_recurse(node, s)
            return child
        else:
            return node

    def get_subclass(self, *args, **kwargs):
        return self.select_subclasses().get(*args, **kwargs)


~~class InheritanceQuerySet(InheritanceQuerySetMixin, QuerySet):
    def instance_of(self, *models):



        where_queries = []
        for model in models:
            where_queries.append('(' + ' AND '.join([
                '"{}"."{}" IS NOT NULL'.format(
                    model._meta.db_table,
                    field.attname,  # Should this be something else?
                ) for field in model._meta.parents.values()
            ]) + ')')

        return self.select_subclasses(*models).extra(where=[' OR '.join(where_queries)])


class InheritanceManagerMixin:
    _queryset_class = InheritanceQuerySet

    def get_queryset(self):
        return self._queryset_class(self.model)

    def select_subclasses(self, *subclasses):
        return self.get_queryset().select_subclasses(*subclasses)


## ... source file abbreviated to get to QuerySet examples ...


            self._q = models.Q(**kwargs)
        self._order_by = None
        super().__init__()

    def order_by(self, *args):
        self._order_by = args
        return self

    def get_queryset(self):
        qs = super().get_queryset().filter(self._q)
        if self._order_by is not None:
            return qs.order_by(*self._order_by)
        return qs


class QueryManager(QueryManagerMixin, models.Manager):
    pass


class SoftDeletableQuerySetMixin:

    def delete(self):
        self.update(is_removed=True)


~~class SoftDeletableQuerySet(SoftDeletableQuerySetMixin, QuerySet):
    pass


class SoftDeletableManagerMixin:
    _queryset_class = SoftDeletableQuerySet

    def get_queryset(self):
        kwargs = {'model': self.model, 'using': self._db}
        if hasattr(self, '_hints'):
            kwargs['hints'] = self._hints

        return self._queryset_class(**kwargs).filter(is_removed=False)


class SoftDeletableManager(SoftDeletableManagerMixin, models.Manager):
    pass


class JoinQueryset(models.QuerySet):

    def get_quoted_query(self, query):
        query, params = query.sql_with_params()

        params = [


## ... source file continues with no further QuerySet examples...

```


## Example 7 from django-rest-framework
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

[**django-rest-framework / rest_framework / relations.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./relations.py)

```python
# relations.py
import sys
from collections import OrderedDict
from urllib import parse

from django.core.exceptions import ImproperlyConfigured, ObjectDoesNotExist
from django.db.models import Manager
~~from django.db.models.query import QuerySet
from django.urls import NoReverseMatch, Resolver404, get_script_prefix, resolve
from django.utils.encoding import smart_str, uri_to_iri
from django.utils.translation import gettext_lazy as _

from rest_framework.fields import (
    Field, empty, get_attribute, is_simple_callable, iter_options
)
from rest_framework.reverse import reverse
from rest_framework.settings import api_settings
from rest_framework.utils import html


def method_overridden(method_name, klass, instance):
    method = getattr(klass, method_name)
    default_method = getattr(method, '__func__', method)  # Python 3 compat
    return default_method is not getattr(instance, method_name).__func__


class ObjectValueError(ValueError):


class ObjectTypeError(TypeError):




## ... source file abbreviated to get to QuerySet examples ...


        )
        kwargs.pop('many', None)
        kwargs.pop('allow_empty', None)
        super().__init__(**kwargs)

    def __new__(cls, *args, **kwargs):
        if kwargs.pop('many', False):
            return cls.many_init(*args, **kwargs)
        return super().__new__(cls, *args, **kwargs)

    @classmethod
    def many_init(cls, *args, **kwargs):
        list_kwargs = {'child_relation': cls(*args, **kwargs)}
        for key in kwargs:
            if key in MANY_RELATION_KWARGS:
                list_kwargs[key] = kwargs[key]
        return ManyRelatedField(**list_kwargs)

    def run_validation(self, data=empty):
        if data == '':
            data = None
        return super().run_validation(data)

    def get_queryset(self):
        queryset = self.queryset
~~        if isinstance(queryset, (QuerySet, Manager)):
            queryset = queryset.all()
        return queryset

    def use_pk_only_optimization(self):
        return False

    def get_attribute(self, instance):
        if self.use_pk_only_optimization() and self.source_attrs:
            try:
                attribute_instance = get_attribute(instance, self.source_attrs[:-1])
                value = attribute_instance.serializable_value(self.source_attrs[-1])
                if is_simple_callable(value):
                    value = value().pk
                return PKOnlyObject(pk=value)
            except AttributeError:
                pass

        return super().get_attribute(instance)

    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            return {}



## ... source file continues with no further QuerySet examples...

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

[**django-wiki / src/wiki / managers.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/./managers.py)

```python
# managers.py
from django.db import models
from django.db.models import Count
from django.db.models import Q
from django.db.models.query import EmptyQuerySet
~~from django.db.models.query import QuerySet
from mptt.managers import TreeManager


~~class ArticleQuerySet(QuerySet):
    def can_read(self, user):
        if user.has_perm("wiki.moderator"):
            return self
        if user.is_anonymous:
            q = self.filter(other_read=True)
        else:
            q = self.filter(
                Q(other_read=True)
                | Q(owner=user)
                | (Q(group__user=user) & Q(group_read=True))
            ).annotate(Count("id"))
        return q

    def can_write(self, user):
        if user.has_perm("wiki.moderator"):
            return self
        if user.is_anonymous:
            q = self.filter(other_write=True)
        else:
            q = self.filter(
                Q(other_write=True)
                | Q(owner=user)
                | (Q(group__user=user) & Q(group_write=True))
            )


## ... source file abbreviated to get to QuerySet examples ...


class ArticleFkManager(models.Manager):
    def get_empty_query_set(self):
        return self.get_queryset().none()

    def get_queryset(self):
        return ArticleFkQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def can_read(self, user):
        return self.get_queryset().can_read(user)

    def can_write(self, user):
        return self.get_queryset().can_write(user)


class URLPathEmptyQuerySet(EmptyQuerySet, ArticleFkEmptyQuerySetMixin):
    def select_related_common(self):
        return self

    def default_order(self):
        return self


~~class URLPathQuerySet(QuerySet, ArticleFkQuerySetMixin):
    def select_related_common(self):
        return self.select_related(
            "parent", "article__current_revision", "article__owner"
        )

    def default_order(self):
        return self.order_by("article__current_revision__title")


class URLPathManager(TreeManager):
    def get_empty_query_set(self):
        return self.get_queryset().none()

    def get_queryset(self):
        return URLPathQuerySet(self.model, using=self._db).order_by(
            self.tree_id_attr, self.left_attr
        )

    def select_related_common(self):
        return self.get_queryset().common_select_related()

    def active(self):
        return self.get_queryset().active()

        if user.is_anonymous:
            q = self.filter(article__other_write=True)
        else:
            q = self.filter(
                Q(article__other_write=True)
                | Q(article__owner=user)
                | (Q(article__group__user=user) & Q(article__group_write=True))
            ).annotate(Count("id"))
        return q

    def active(self):
        return self.filter(article__current_revision__deleted=False)


class ArticleFkEmptyQuerySetMixin:
    def can_read(self, user):
        return self

    def can_write(self, user):
        return self

    def active(self):
        return self


~~class ArticleFkQuerySet(ArticleFkQuerySetMixin, QuerySet):
    pass


class ArticleFkEmptyQuerySet(ArticleFkEmptyQuerySetMixin, EmptyQuerySet):
    pass


class ArticleManager(models.Manager):
    def get_empty_query_set(self):
        return self.get_queryset().none()

    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def can_read(self, user):
        return self.get_queryset().can_read(user)

    def can_write(self, user):
        return self.get_queryset().can_write(user)




## ... source file continues with no further QuerySet examples...

```


## Example 9 from elasticsearch-django
[elasticsearch-django](https://github.com/yunojuno/elasticsearch-django)
([PyPI package information](https://pypi.org/project/elasticsearch-django/))
is a [Django](/django.html) app for managing
[ElasticSearch](https://github.com/elastic/elasticsearch) indexes
populated by [Django ORM](/django-orm.html) models. The project is
available as open source under the
[MIT license](https://github.com/yunojuno/elasticsearch-django/blob/master/LICENSE).

[**elasticsearch-django / elasticsearch_django / models.py**](https://github.com/yunojuno/elasticsearch-django/blob/master/elasticsearch_django/./models.py)

```python
# models.py
from __future__ import annotations

import logging
import time
import warnings
from typing import TYPE_CHECKING, Any, List, Optional, Tuple, Union

from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.core.cache import cache
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.db.models.expressions import RawSQL
from django.db.models.fields import CharField
~~from django.db.models.query import QuerySet
from django.utils.timezone import now as tz_now
from elasticsearch_dsl import Search

from .settings import (
    get_client,
    get_model_index_properties,
    get_model_indexes,
    get_setting,
)

if TYPE_CHECKING:
    from django.contrib.auth.models import AbstractBaseUser

logger = logging.getLogger(__name__)

UPDATE_STRATEGY_FULL = "full"
UPDATE_STRATEGY_PARTIAL = "partial"
UPDATE_STRATEGY = get_setting("update_strategy", UPDATE_STRATEGY_FULL)


class SearchDocumentManagerMixin(models.Manager):

    def get_search_queryset(self, index: str = "_all") -> QuerySet:
        raise NotImplementedError(


## ... source file continues with no further QuerySet examples...

```

