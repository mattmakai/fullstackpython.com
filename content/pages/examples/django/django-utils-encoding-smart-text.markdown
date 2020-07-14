title: django.utils.encoding smart_text Example Code
category: page
slug: django-utils-encoding-smart-text-examples
sortorder: 500011449
toc: False
sidebartitle: django.utils.encoding smart_text
meta: Python example code for the smart_text callable from the django.utils.encoding module of the Django project.


smart_text is a callable within the django.utils.encoding module of the Django project.


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
from django.core.exceptions import FieldDoesNotExist
from django.db import models, DEFAULT_DB_ALIAS
from django.db.models import QuerySet, Q
from django.utils import formats, timezone
~~from django.utils.encoding import python_2_unicode_compatible, smart_text
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
~~            kwargs.setdefault('object_repr', smart_text(instance))

            if isinstance(pk, integer_types):
                kwargs.setdefault('object_id', pk)

            get_additional_data = getattr(instance, 'get_additional_data', None)
            if callable(get_additional_data):
                kwargs.setdefault('additional_data', get_additional_data())

            if kwargs.get('action', None) is LogEntry.Action.CREATE:
                if kwargs.get('object_id', None) is not None and self.filter(content_type=kwargs.get('content_type'), object_id=kwargs.get('object_id')).exists():
                    self.filter(content_type=kwargs.get('content_type'), object_id=kwargs.get('object_id')).delete()
                else:
                    self.filter(content_type=kwargs.get('content_type'), object_pk=kwargs.get('object_pk', '')).delete()
            db = instance._state.db
            return self.create(**kwargs) if db is None or db == '' else self.using(db).create(**kwargs)
        return None

    def get_for_object(self, instance):
        if not isinstance(instance, models.Model):
            return self.none()

        content_type = ContentType.objects.get_for_model(instance.__class__)
        pk = self._get_pk_value(instance)



## ... source file abbreviated to get to smart_text examples ...



    def __str__(self):
        if self.action == self.Action.CREATE:
            fstring = _("Created {repr:s}")
        elif self.action == self.Action.UPDATE:
            fstring = _("Updated {repr:s}")
        elif self.action == self.Action.DELETE:
            fstring = _("Deleted {repr:s}")
        else:
            fstring = _("Logged {repr:s}")

        return fstring.format(repr=self.object_repr)

    @property
    def changes_dict(self):
        try:
            return json.loads(self.changes)
        except ValueError:
            return {}

    @property
~~    def changes_str(self, colon=': ', arrow=smart_text(' \u2192 '), separator='; '):
        substrings = []

        for field, values in iteritems(self.changes_dict):
~~            substring = smart_text('{field_name:s}{colon:s}{old:s}{arrow:s}{new:s}').format(
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
            except FieldDoesNotExist:
                changes_display_dict[field_name] = values
                continue
            values_display = []
            choices_dict = None
        if isinstance(pk, integer_types):
            return self.filter(content_type=content_type, object_id=pk)
        else:
~~            return self.filter(content_type=content_type, object_pk=smart_text(pk))

    def get_for_objects(self, queryset):
        if not isinstance(queryset, QuerySet) or queryset.count() == 0:
            return self.none()

        content_type = ContentType.objects.get_for_model(queryset.model)
        primary_keys = list(queryset.values_list(queryset.model._meta.pk.name, flat=True))

        if isinstance(primary_keys[0], integer_types):
            return self.filter(content_type=content_type).filter(Q(object_id__in=primary_keys)).distinct()
        elif isinstance(queryset.model._meta.pk, models.UUIDField):
            primary_keys = [smart_text(pk) for pk in primary_keys]
            return self.filter(content_type=content_type).filter(Q(object_pk__in=primary_keys)).distinct()
        else:
            return self.filter(content_type=content_type).filter(Q(object_pk__in=primary_keys)).distinct()

    def get_for_model(self, model):
        if not issubclass(model, models.Model):
            return self.none()

        content_type = ContentType.objects.get_for_model(model)

        return self.filter(content_type=content_type)



## ... source file abbreviated to get to smart_text examples ...


        get_latest_by = 'timestamp'
        ordering = ['-timestamp']
        verbose_name = _("log entry")
        verbose_name_plural = _("log entries")


## ... source file continues with no further smart_text examples...

```


## Example 2 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / templatetags / cms_tags.py**](https://github.com/divio/django-cms/blob/develop/cms/templatetags/cms_tags.py)

```python
# cms_tags.py
from collections import namedtuple, OrderedDict
from copy import copy
from datetime import datetime

from django import template
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import mail_managers
from django.db.models import Model
from django.middleware.common import BrokenLinkEmailsMiddleware
from django.template.loader import render_to_string
from django.urls import reverse
~~from django.utils.encoding import force_text, smart_text
from django.utils.html import escape
from django.utils.http import urlencode
from django.utils.translation import (
    get_language,
    override as force_language,
    ugettext_lazy as _,
)

from six import string_types, integer_types

from classytags.arguments import (Argument, MultiValueArgument,
                                  MultiKeywordArgument)
from classytags.core import Options, Tag
from classytags.helpers import InclusionTag, AsTag
from classytags.parser import Parser
from classytags.utils import flatten_context
from classytags.values import ListValue, StringValue

from cms.cache.page import get_page_url_cache, set_page_url_cache
from cms.exceptions import PlaceholderNotFound
from cms.models import Page, Placeholder as PlaceholderModel, CMSPlugin, StaticPlaceholder
from cms.plugin_pool import plugin_pool
from cms.toolbar.utils import get_toolbar_from_request
from cms.utils import get_current_site, get_language_from_request, get_site_id


## ... source file abbreviated to get to smart_text examples ...


    def render_tag(self, context, **kwargs):
        context.push()
        template = self.get_template(context, **kwargs)
        data = self.get_context(context, **kwargs)
        output = render_to_string(template, flatten_context(data)).strip()
        context.pop()
        if kwargs.get('varname'):
            context[kwargs['varname']] = output
            return ''
        else:
            return output

    def _get_editable_context(self, context, instance, language, edit_fields,
                              view_method, view_url, querystring, editmode=True):
        request = context['request']
        if hasattr(request, 'toolbar'):
            lang = request.toolbar.toolbar_language
        else:
            lang = get_language()
        opts = instance._meta
        if getattr(instance, '_deferred', False):
            opts = opts.proxy_for_model._meta
        with force_language(lang):
            extra_context = {}
            if edit_fields == 'changelist':
~~                instance.get_plugin_name = u"%s %s list" % (smart_text(_('Edit')), smart_text(opts.verbose_name))
                extra_context['attribute_name'] = 'changelist'
            elif editmode:
~~                instance.get_plugin_name = u"%s %s" % (smart_text(_('Edit')), smart_text(opts.verbose_name))
                if not context.get('attribute_name', None):
                    extra_context['attribute_name'] = '-'.join(edit_fields) \
                                                        if not isinstance('edit_fields', string_types) else edit_fields
            else:
~~                instance.get_plugin_name = u"%s %s" % (smart_text(_('Add')), smart_text(opts.verbose_name))
                extra_context['attribute_name'] = 'add'
            extra_context['instance'] = instance
            extra_context['generic'] = opts
            if view_method:
                method = getattr(instance, view_method)
                if callable(method):
                    url_base = method(context['request'])
                else:
                    url_base = method
            else:
                if not editmode:
                    view_url = 'admin:%s_%s_add' % (
                        opts.app_label, opts.model_name)
                    url_base = reverse(view_url)
                elif not edit_fields:
                    if not view_url:
                        view_url = 'admin:%s_%s_change' % (
                            opts.app_label, opts.model_name)
                    if isinstance(instance, Page):
                        url_base = reverse(view_url, args=(instance.pk, language))
                    else:
                        url_base = reverse(view_url, args=(instance.pk,))
                else:
                    if not view_url:


## ... source file continues with no further smart_text examples...

```


## Example 3 from django-jet
[django-jet](https://github.com/geex-arts/django-jet)
([project documentation](https://jet.readthedocs.io/en/latest/),
[PyPI project page](https://pypi.org/project/django-jet/) and
[more information](http://jet.geex-arts.com/))
is a fancy [Django](/django.html) Admin panel replacement.

The django-jet project is open source under the
[GNU Affero General Public License v3.0](https://github.com/geex-arts/django-jet/blob/dev/LICENSE).

[**django-jet / jet / utils.py**](https://github.com/geex-arts/django-jet/blob/dev/jet/./utils.py)

```python
# utils.py
import datetime
import json
from django.template import Context
from django.utils import translation
from jet import settings
from jet.models import PinnedApplication

try:
    from django.apps.registry import apps
except ImportError:
    try:
        from django.apps import apps # Fix Django 1.7 import issue
    except ImportError:
        pass
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
try:
    from django.core.urlresolvers import reverse, resolve, NoReverseMatch
except ImportError: # Django 1.11
    from django.urls import reverse, resolve, NoReverseMatch

from django.contrib.admin import AdminSite
~~from django.utils.encoding import smart_text
from django.utils.text import capfirst
from django.contrib import messages
from django.utils.encoding import force_text
from django.utils.functional import Promise
from django.contrib.admin.options import IncorrectLookupParameters
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict  # Python 2.6


class JsonResponse(HttpResponse):

    def __init__(self, data, encoder=DjangoJSONEncoder, safe=True, **kwargs):
        if safe and not isinstance(data, dict):
            raise TypeError('In order to allow non-dict objects to be '
                'serialized set the safe parameter to False')
        kwargs.setdefault('content_type', 'application/json')
        data = json.dumps(data, cls=encoder)
        super(JsonResponse, self).__init__(content=data, **kwargs)


## ... source file abbreviated to get to smart_text examples ...


        for func_closure in index_resolver.func.__closure__:
            if isinstance(func_closure.cell_contents, AdminSite):
                return func_closure.cell_contents
    except:
        pass

    return admin.site


def get_admin_site_name(context):
    return get_admin_site(context).name


class LazyDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, Promise):
            return force_text(obj)
        return self.encode(obj)


def get_model_instance_label(instance):
    if getattr(instance, "related_label", None):
        return instance.related_label()
~~    return smart_text(instance)


class SuccessMessageMixin(object):
    success_message = ''

    def form_valid(self, form):
        response = super(SuccessMessageMixin, self).form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data


def get_model_queryset(admin_site, model, request, preserved_filters=None):
    model_admin = admin_site._registry.get(model)

    if model_admin is None:
        return

    try:
        changelist_url = reverse('%s:%s_%s_changelist' % (


## ... source file continues with no further smart_text examples...

```


## Example 4 from django-pipeline
[django-pipeline](https://github.com/jazzband/django-pipeline)
([project documentation](https://django-pipeline.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-pipeline/))
is a code library for handling and compressing
[static content assets](/static-content.html) when handling requests in
[Django](/django.html) web applications.

The django-pipeline project is open sourced under the
[MIT License](https://github.com/jazzband/django-pipeline/blob/master/LICENSE)
and it is maintained by the developer community group
[Jazzband](https://jazzband.co/).

[**django-pipeline / pipeline / utils.py**](https://github.com/jazzband/django-pipeline/blob/master/pipeline/./utils.py)

```python
# utils.py
try:
    import fcntl
except ImportError:
    fcntl = None

import importlib
import mimetypes
import posixpath
import os
import sys

from urllib.parse import quote

~~from django.utils.encoding import smart_text

from pipeline.conf import settings


def to_class(class_str):
    if not class_str:
        return None

    module_bits = class_str.split('.')
    module_path, class_name = '.'.join(module_bits[:-1]), module_bits[-1]
    module = importlib.import_module(module_path)
    return getattr(module, class_name, None)


def filepath_to_uri(path):
    if path is None:
        return path
    return quote(smart_text(path).replace("\\", "/"), safe="/-!*()'#?")


def guess_type(path, default=None):
    for type, ext in settings.MIMETYPES:
        mimetypes.add_type(type, ext)
    mimetype, _ = mimetypes.guess_type(path)
    if not mimetype:
        return default
~~    return smart_text(mimetype)


def relpath(path, start=posixpath.curdir):
    if not path:
        raise ValueError("no path specified")

    start_list = posixpath.abspath(start).split(posixpath.sep)
    path_list = posixpath.abspath(path).split(posixpath.sep)

    i = len(posixpath.commonprefix([start_list, path_list]))

    rel_list = [posixpath.pardir] * (len(start_list) - i) + path_list[i:]
    if not rel_list:
        return posixpath.curdir
    return posixpath.join(*rel_list)


def set_std_streams_blocking():
    if not fcntl:
        return
    for f in (sys.__stdout__, sys.__stderr__):
        fileno = f.fileno()
        flags = fcntl.fcntl(fileno, fcntl.F_GETFL)
        fcntl.fcntl(fileno, fcntl.F_SETFL, flags & -os.O_NONBLOCK)


## ... source file continues with no further smart_text examples...

```

