title: django.core.exceptions ObjectDoesNotExist Example Code
category: page
slug: django-core-exceptions-objectdoesnotexist-examples
sortorder: 500011104
toc: False
sidebartitle: django.core.exceptions ObjectDoesNotExist
meta: Python example code for the ObjectDoesNotExist class from the django.core.exceptions module of the Django project.


ObjectDoesNotExist is a class within the django.core.exceptions module of the Django project.


## Example 1 from AuditLog
[Auditlog](https://github.com/jjkester/django-auditlog)
([project documentation](https://django-auditlog.readthedocs.io/en/latest/))
is a [Django](/django.html) app that logs changes to Python objects,
similar to the Django admin's logs but with more details and
output formats. Auditlog's source code is provided as open source under the
[MIT license](https://github.com/jjkester/django-auditlog/blob/master/LICENSE).

[**AuditLog / src / auditlog / diff.py**](https://github.com/jjkester/django-auditlog/blob/master/src/auditlog/diff.py)

```python
# diff.py
from __future__ import unicode_literals

from django.conf import settings
~~from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Model, NOT_PROVIDED, DateTimeField
from django.utils import timezone
from django.utils.encoding import smart_text


def track_field(field):
    from auditlog.models import LogEntry
    if field.many_to_many:
        return False

    if getattr(field, 'remote_field', None) is not None and field.remote_field.model == LogEntry:
        return False

    elif getattr(field, 'rel', None) is not None and field.rel.to == LogEntry:
        return False

    return True


def get_fields_in_model(instance):
    assert isinstance(instance, Model)

    use_api = hasattr(instance._meta, 'get_fields') and callable(instance._meta.get_fields)

    if use_api:
        return [f for f in instance._meta.get_fields() if track_field(f)]
    return instance._meta.fields


def get_field_value(obj, field):
    if isinstance(field, DateTimeField):
        try:
            value = field.to_python(getattr(obj, field.name, None))
            if value is not None and settings.USE_TZ and not timezone.is_naive(value):
                value = timezone.make_naive(value, timezone=timezone.utc)
~~        except ObjectDoesNotExist:
            value = field.default if field.default is not NOT_PROVIDED else None
    else:
        try:
            value = smart_text(getattr(obj, field.name, None))
~~        except ObjectDoesNotExist:
            value = field.default if field.default is not NOT_PROVIDED else None

    return value


def model_instance_diff(old, new):
    from auditlog.registry import auditlog

    if not(old is None or isinstance(old, Model)):
        raise TypeError("The supplied old instance is not a valid model instance.")
    if not(new is None or isinstance(new, Model)):
        raise TypeError("The supplied new instance is not a valid model instance.")

    diff = {}

    if old is not None and new is not None:
        fields = set(old._meta.fields + new._meta.fields)
        model_fields = auditlog.get_model_fields(new._meta.model)
    elif old is not None:
        fields = set(get_fields_in_model(old))
        model_fields = auditlog.get_model_fields(old._meta.model)
    elif new is not None:
        fields = set(get_fields_in_model(new))
        model_fields = auditlog.get_model_fields(new._meta.model)


## ... source file continues with no further ObjectDoesNotExist examples...

```


## Example 2 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / test_utils / testcases.py**](https://github.com/divio/django-cms/blob/develop/cms/test_utils/testcases.py)

```python
# testcases.py
import json
import sys
import warnings

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser, Permission
from django.contrib.sites.models import Site
from django.core.cache import cache
~~from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.template import engines
from django.template.context import Context
from django.test import testcases
from django.test.client import RequestFactory
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.timezone import now
from django.utils.translation import activate
from menus.menu_pool import menu_pool

from six.moves.urllib.parse import unquote, urljoin

from cms.api import create_page
from cms.constants import (
    PUBLISHER_STATE_DEFAULT,
    PUBLISHER_STATE_DIRTY,
    PUBLISHER_STATE_PENDING,
)
from cms.plugin_rendering import ContentRenderer, StructureRenderer
from cms.models import Page
from cms.models.permissionmodels import (
    GlobalPagePermission,
    PagePermission,


## ... source file abbreviated to get to ObjectDoesNotExist examples ...


        page_data['pagepermission_set-2-TOTAL_FORMS'] = 0
        page_data['pagepermission_set-2-INITIAL_FORMS'] = 0
        page_data['pagepermission_set-2-MAX_NUM_FORMS'] = 0
        return page_data

    def print_page_structure(self, qs):
        for page in qs.order_by('path'):
            ident = "  " * page.level
            print(u"%s%s (%s), path: %s, depth: %s, numchild: %s" % (ident, page,
            page.pk, page.path, page.depth, page.numchild))

    def print_node_structure(self, nodes, *extra):
        def _rec(nodes, level=0):
            ident = level * '  '
            for node in nodes:
                raw_attrs = [(bit, getattr(node, bit, node.attr.get(bit, "unknown"))) for bit in extra]
                attrs = ', '.join(['%s: %r' % data for data in raw_attrs])
                print(u"%s%s: %s" % (ident, node.title, attrs))
                _rec(node.children, level + 1)

        _rec(nodes)

    def assertObjectExist(self, qs, **filter):
        try:
            return qs.get(**filter)
~~        except ObjectDoesNotExist:
            pass
        raise self.failureException("ObjectDoesNotExist raised for filter %s" % filter)

    def assertObjectDoesNotExist(self, qs, **filter):
        try:
            qs.get(**filter)
~~        except ObjectDoesNotExist:
            return
        raise self.failureException("ObjectDoesNotExist not raised for filter %s" % filter)

    def copy_page(self, page, target_page, position=0, target_site=None):
        from cms.utils.page import get_available_slug

        if target_site is None:
            target_site = target_page.node.site

        data = {
            'position': position,
            'target': target_page.pk,
            'source_site': page.node.site_id,
            'copy_permissions': 'on',
            'copy_moderation': 'on',
        }
        source_translation = page.title_set.all()[0]
        parent_translation = target_page.title_set.all()[0]
        language = source_translation.language
        copied_page_path = source_translation.get_path_for_base(parent_translation.path)
        new_page_slug = get_available_slug(target_site, copied_page_path, language)

        with self.settings(SITE_ID=target_site.pk):
            response = self.client.post(URL_CMS_PAGE + "%d/copy-page/" % page.pk, data)


## ... source file continues with no further ObjectDoesNotExist examples...

```


## Example 3 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / fields / folder.py**](https://github.com/divio/django-filer/blob/develop/filer/fields/folder.py)

```python
# folder.py
from __future__ import absolute_import

import warnings

from django import forms
from django.contrib.admin.sites import site
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
~~from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.safestring import mark_safe

from ..models import Folder
from ..utils.compatibility import truncate_words
from ..utils.model_label import get_model_label


class AdminFolderWidget(ForeignKeyRawIdWidget):
    choices = None
    input_type = 'hidden'
    is_hidden = False

    def render(self, name, value, attrs=None, renderer=None):
        obj = self.obj_for_value(value)
        css_id = attrs.get('id')
        css_id_folder = "%s_folder" % css_id
        css_id_description_txt = "%s_description_txt" % css_id
        if attrs is None:
            attrs = {}
        related_url = None


## ... source file abbreviated to get to ObjectDoesNotExist examples ...


        context = {
            'hidden_input': hidden_input,
            'lookup_url': '%s%s' % (related_url, url),
            'lookup_name': name,
            'span_id': css_id_description_txt,
            'object': obj,
            'clear_id': '%s_clear' % css_id,
            'descid': css_id_description_txt,
            'noimg': 'filer/icons/nofile_32x32.png',
            'foldid': css_id_folder,
            'id': css_id,
        }
        html = render_to_string('admin/filer/widgets/admin_folder.html', context)
        return mark_safe(html)

    def label_for_value(self, value):
        obj = self.obj_for_value(value)
        return '&nbsp;<strong>%s</strong>' % truncate_words(obj, 14)

    def obj_for_value(self, value):
        if not value:
            return None
        try:
            key = self.rel.get_related_field().name
            obj = self.rel.model._default_manager.get(**{key: value})
~~        except ObjectDoesNotExist:
            obj = None
        return obj

    class Media(object):
        js = (
            'filer/js/addons/popup_handling.js',
        )


class AdminFolderFormField(forms.ModelChoiceField):
    widget = AdminFolderWidget

    def __init__(self, rel, queryset, to_field_name, *args, **kwargs):
        self.rel = rel
        self.queryset = queryset
        self.limit_choices_to = kwargs.pop('limit_choices_to', None)
        self.to_field_name = to_field_name
        self.max_value = None
        self.min_value = None
        kwargs.pop('widget', None)
        forms.Field.__init__(self, widget=self.widget(rel, site), *args, **kwargs)

    def widget_attrs(self, widget):
        widget.required = self.required


## ... source file continues with no further ObjectDoesNotExist examples...

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

[**django-guardian / guardian / utils.py**](https://github.com/django-guardian/django-guardian/blob/devel/guardian/./utils.py)

```python
# utils.py
import logging
import os
from itertools import chain

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME, get_user_model
from django.contrib.auth.models import AnonymousUser, Group
~~from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.db.models import Model, QuerySet
from django.http import HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import render
from guardian.conf import settings as guardian_settings
from guardian.ctypes import get_content_type
from guardian.exceptions import NotUserNorGroup

logger = logging.getLogger(__name__)
abspath = lambda *p: os.path.abspath(os.path.join(*p))


def get_anonymous_user():
    User = get_user_model()
    lookup = {User.USERNAME_FIELD: guardian_settings.ANONYMOUS_USER_NAME}
    return User.objects.get(**lookup)


def get_identity(identity):
    if isinstance(identity, AnonymousUser):
        identity = get_anonymous_user()

    if isinstance(identity, QuerySet):
        identity_model_type = identity.model
        if identity_model_type == get_user_model():


## ... source file abbreviated to get to ObjectDoesNotExist examples ...


    redirect_field_name = redirect_field_name or REDIRECT_FIELD_NAME


    has_permissions = False
    if accept_global_perms:
        has_permissions = all(request.user.has_perm(perm) for perm in perms)
    if not has_permissions:
        has_permissions = all(request.user.has_perm(perm, obj)
                              for perm in perms)

    if not has_permissions:
        if return_403:
            if guardian_settings.RENDER_403:
                response = render(request, guardian_settings.TEMPLATE_403)
                response.status_code = 403
                return response
            elif guardian_settings.RAISE_403:
                raise PermissionDenied
            return HttpResponseForbidden()
        if return_404:
            if guardian_settings.RENDER_404:
                response = render(request, guardian_settings.TEMPLATE_404)
                response.status_code = 404
                return response
            elif guardian_settings.RAISE_404:
~~                raise ObjectDoesNotExist
            return HttpResponseNotFound()
        else:
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(request.get_full_path(),
                                     login_url,
                                     redirect_field_name)


from django.apps import apps as django_apps
from django.core.exceptions import ImproperlyConfigured

def get_obj_perm_model_by_conf(setting_name):
    try:
        setting_value = getattr(guardian_settings, setting_name)
        return django_apps.get_model(setting_value, require_ready=False)
    except ValueError as e:
        raise ImproperlyConfigured("{} must be of the form 'app_label.model_name'".format(setting_value)) from e
    except LookupError as e:
        raise ImproperlyConfigured(
            "{} refers to model '{}' that has not been installed".format(setting_name, setting_value)
        ) from e


def clean_orphan_obj_perms():


## ... source file continues with no further ObjectDoesNotExist examples...

```


## Example 5 from django-haystack
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

~~from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import force_str
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


## ... source file abbreviated to get to ObjectDoesNotExist examples ...


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
                    self.log.warning(
                        "Model '%s.%s' not handled by the routers.",
                        self.app_label,
                        self.model_name,
                    )
                    self._object = self.model._default_manager.get(pk=self.pk)
~~            except ObjectDoesNotExist:
                self.log.error(
                    "Object could not be found in database for SearchResult '%s'.", self
                )
                self._object = None

        return self._object

    def _set_object(self, obj):
        self._object = obj

    object = property(_get_object, _set_object)

    def _get_model(self):
        if self._model is None:
            try:
                self._model = haystack_get_model(self.app_label, self.model_name)
            except LookupError:
                pass

        return self._model

    def _set_model(self, obj):
        self._model = obj



## ... source file continues with no further ObjectDoesNotExist examples...

```


## Example 6 from django-import-export
[django-import-export](https://github.com/django-import-export/django-import-export)
([documentation](https://django-import-export.readthedocs.io/en/latest/)
and [PyPI page](https://pypi.org/project/django-import-export/))
is a [Django](/django.html) code library for importing and exporting data
from the Django Admin. The tool supports many export and import formats
such as CSV, JSON and YAML. django-import-export is open source under the
[BSD 2-Clause "Simplified" License](https://github.com/django-import-export/django-import-export/blob/master/LICENSE).

[**django-import-export / import_export / fields.py**](https://github.com/django-import-export/django-import-export/blob/master/import_export/./fields.py)

```python
# fields.py
~~from django.core.exceptions import ObjectDoesNotExist
from django.db.models.fields import NOT_PROVIDED
from django.db.models.manager import Manager

from . import widgets


class Field:
    empty_values = [None, '']

    def __init__(self, attribute=None, column_name=None, widget=None,
                 default=NOT_PROVIDED, readonly=False, saves_null_values=True):
        self.attribute = attribute
        self.default = default
        self.column_name = column_name
        if not widget:
            widget = widgets.Widget()
        self.widget = widget
        self.readonly = readonly
        self.saves_null_values = saves_null_values

    def __repr__(self):
        path = '%s.%s' % (self.__class__.__module__, self.__class__.__name__)
        column_name = getattr(self, 'column_name', None)
        if column_name is not None:


## ... source file abbreviated to get to ObjectDoesNotExist examples ...


        try:
            value = data[self.column_name]
        except KeyError:
            raise KeyError("Column '%s' not found in dataset. Available "
                           "columns are: %s" % (self.column_name, list(data)))

        value = self.widget.clean(value, row=data)

        if value in self.empty_values and self.default != NOT_PROVIDED:
            if callable(self.default):
                return self.default()
            return self.default

        return value

    def get_value(self, obj):
        if self.attribute is None:
            return None

        attrs = self.attribute.split('__')
        value = obj

        for attr in attrs:
            try:
                value = getattr(value, attr, None)
~~            except (ValueError, ObjectDoesNotExist):
                return None
            if value is None:
                return None

        if callable(value) and not isinstance(value, Manager):
            value = value()
        return value

    def save(self, obj, data, is_m2m=False):
        if not self.readonly:
            attrs = self.attribute.split('__')
            for attr in attrs[:-1]:
                obj = getattr(obj, attr, None)
            cleaned = self.clean(data)
            if cleaned is not None or self.saves_null_values:
                if not is_m2m:
                    setattr(obj, attrs[-1], cleaned)
                else:
                    getattr(obj, attrs[-1]).set(cleaned)

    def export(self, obj):
        value = self.get_value(obj)
        if value is None:
            return ""


## ... source file continues with no further ObjectDoesNotExist examples...

```


## Example 7 from django-model-utils
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
~~from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from django.db import models
from django.db.models.constants import LOOKUP_SEP
from django.db.models.fields.related import OneToOneField, OneToOneRel
from django.db.models.query import ModelIterable
from django.db.models.query import QuerySet
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


## ... source file abbreviated to get to ObjectDoesNotExist examples ...


    def _get_ancestors_path(self, model, levels=None):
        if not issubclass(model, self.model):
            raise ValueError(
                "{!r} is not a subclass of {!r}".format(model, self.model))

        ancestry = []
        parent_link = model._meta.get_ancestor_link(self.model)
        if levels:
            levels -= 1
        while parent_link is not None:
            related = parent_link.remote_field
            ancestry.insert(0, related.get_accessor_name())
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
~~        except ObjectDoesNotExist:
            return None
        if s:
            child = self._get_sub_obj_recurse(node, s)
            return child
        else:
            return node

    def get_subclass(self, *args, **kwargs):
        return self.select_subclasses().get(*args, **kwargs)


class InheritanceQuerySet(InheritanceQuerySetMixin, QuerySet):
    def instance_of(self, *models):



        where_queries = []
        for model in models:
            where_queries.append('(' + ' AND '.join([
                '"{}"."{}" IS NOT NULL'.format(
                    model._meta.db_table,
                    field.attname,  # Should this be something else?
                ) for field in model._meta.parents.values()
            ]) + ')')


## ... source file continues with no further ObjectDoesNotExist examples...

```


## Example 8 from django-oauth-toolkit
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

[**django-oauth-toolkit / oauth2_provider / oauth2_validators.py**](https://github.com/jazzband/django-oauth-toolkit/blob/master/oauth2_provider/./oauth2_validators.py)

```python
# oauth2_validators.py
import base64
import binascii
import http.client
import logging
from collections import OrderedDict
from datetime import datetime, timedelta
from urllib.parse import unquote_plus

import requests
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
~~from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import Q
from django.utils import timezone
from django.utils.timezone import make_aware
from django.utils.translation import gettext_lazy as _
from oauthlib.oauth2 import RequestValidator

from .exceptions import FatalClientError
from .models import (
    AbstractApplication, get_access_token_model,
    get_application_model, get_grant_model, get_refresh_token_model
)
from .scopes import get_scopes_backend
from .settings import oauth2_settings


log = logging.getLogger("oauth2_provider")

GRANT_TYPE_MAPPING = {
    "authorization_code": (AbstractApplication.GRANT_AUTHORIZATION_CODE, ),
    "password": (AbstractApplication.GRANT_PASSWORD, ),
    "client_credentials": (AbstractApplication.GRANT_CLIENT_CREDENTIALS, ),
    "refresh_token": (
        AbstractApplication.GRANT_AUTHORIZATION_CODE,


## ... source file abbreviated to get to ObjectDoesNotExist examples ...


            scope=" ".join(request.scopes),
            code_challenge=request.code_challenge or "",
            code_challenge_method=request.code_challenge_method or ""
        )

    def _create_refresh_token(self, request, refresh_token_code, access_token):
        return RefreshToken.objects.create(
            user=request.user,
            token=refresh_token_code,
            application=request.client,
            access_token=access_token
        )

    def revoke_token(self, token, token_type_hint, request, *args, **kwargs):
        if token_type_hint not in ["access_token", "refresh_token"]:
            token_type_hint = None

        token_types = {
            "access_token": AccessToken,
            "refresh_token": RefreshToken,
        }

        token_type = token_types.get(token_type_hint, AccessToken)
        try:
            token_type.objects.get(token=token).revoke()
~~        except ObjectDoesNotExist:
            for other_type in [_t for _t in token_types.values() if _t != token_type]:
                list(map(lambda t: t.revoke(), other_type.objects.filter(token=token)))

    def validate_user(self, username, password, client, request, *args, **kwargs):
        u = authenticate(username=username, password=password)
        if u is not None and u.is_active:
            request.user = u
            return True
        return False

    def get_original_scopes(self, refresh_token, request, *args, **kwargs):
        rt = request.refresh_token_instance
        if not rt.access_token_id:
            return AccessToken.objects.get(source_refresh_token_id=rt.id).scope

        return rt.access_token.scope

    def validate_refresh_token(self, refresh_token, client, request, *args, **kwargs):

        null_or_recent = Q(revoked__isnull=True) | Q(
            revoked__gt=timezone.now() - timedelta(
                seconds=oauth2_settings.REFRESH_TOKEN_GRACE_PERIOD_SECONDS
            )
        )


## ... source file continues with no further ObjectDoesNotExist examples...

```


## Example 9 from django-rest-framework
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
~~from django.core.exceptions import ObjectDoesNotExist
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


## ... source file abbreviated to get to ObjectDoesNotExist examples ...


    if inspect.isbuiltin(obj):
        raise BuiltinSignatureError(
            'Built-in function signatures are not inspectable. '
            'Wrap the function call in a simple, pure Python function.')

    if not (inspect.isfunction(obj) or inspect.ismethod(obj) or isinstance(obj, functools.partial)):
        return False

    sig = inspect.signature(obj)
    params = sig.parameters.values()
    return all(
        param.kind == param.VAR_POSITIONAL or
        param.kind == param.VAR_KEYWORD or
        param.default != param.empty
        for param in params
    )


def get_attribute(instance, attrs):
    for attr in attrs:
        try:
            if isinstance(instance, Mapping):
                instance = instance[attr]
            else:
                instance = getattr(instance, attr)
~~        except ObjectDoesNotExist:
            return None
        if is_simple_callable(instance):
            try:
                instance = instance()
            except (AttributeError, KeyError) as exc:
                raise ValueError('Exception raised in callable attribute "{}"; original exception was: {}'.format(attr, exc))

    return instance


def set_value(dictionary, keys, value):
    if not keys:
        dictionary.update(value)
        return

    for key in keys[:-1]:
        if key not in dictionary:
            dictionary[key] = {}
        dictionary = dictionary[key]

    dictionary[keys[-1]] = value


def to_choices_dict(choices):


## ... source file continues with no further ObjectDoesNotExist examples...

```

