title: django.db models Example Code
category: page
slug: django-db-models-examples
sortorder: 500011167
toc: False
sidebartitle: django.db models
meta: Python example code for the models callable from the django.db module of the Django project.


models is a callable within the django.db module of the Django project.


## Example 1 from AuditLog
[Auditlog](https://github.com/jjkester/django-auditlog)
([project documentation](https://django-auditlog.readthedocs.io/en/latest/))
is a [Django](/django.html) app that logs changes to Python objects,
similar to the Django admin's logs but with more details and
output formats. Auditlog's source code is provided as open source under the
[MIT license](https://github.com/jjkester/django-auditlog/blob/master/LICENSE).

[**AuditLog / src / auditlog_tests / models.py**](https://github.com/jjkester/django-auditlog/blob/master/src/auditlog_tests/models.py)

```python
# models.py
import uuid

from django.contrib.postgres.fields import ArrayField
~~from django.db import models
from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog

from multiselectfield import MultiSelectField


@auditlog.register()
class SimpleModel(models.Model):

~~    text = models.TextField(blank=True)
~~    boolean = models.BooleanField(default=False)
~~    integer = models.IntegerField(blank=True, null=True)
~~    datetime = models.DateTimeField(auto_now=True)

    history = AuditlogHistoryField()


class AltPrimaryKeyModel(models.Model):

~~    key = models.CharField(max_length=100, primary_key=True)

~~    text = models.TextField(blank=True)
~~    boolean = models.BooleanField(default=False)
~~    integer = models.IntegerField(blank=True, null=True)
~~    datetime = models.DateTimeField(auto_now=True)

    history = AuditlogHistoryField(pk_indexable=False)


class UUIDPrimaryKeyModel(models.Model):

~~    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

~~    text = models.TextField(blank=True)
~~    boolean = models.BooleanField(default=False)
~~    integer = models.IntegerField(blank=True, null=True)
~~    datetime = models.DateTimeField(auto_now=True)

    history = AuditlogHistoryField(pk_indexable=False)


class ProxyModel(SimpleModel):

    class Meta:
        proxy = True


class RelatedModel(models.Model):

~~    related = models.ForeignKey(to='self', on_delete=models.CASCADE)

    history = AuditlogHistoryField()


class ManyRelatedModel(models.Model):

~~    related = models.ManyToManyField('self')

    history = AuditlogHistoryField()


@auditlog.register(include_fields=['label'])
class SimpleIncludeModel(models.Model):

~~    label = models.CharField(max_length=100)
~~    text = models.TextField(blank=True)

    history = AuditlogHistoryField()


class SimpleExcludeModel(models.Model):

~~    label = models.CharField(max_length=100)
~~    text = models.TextField(blank=True)

    history = AuditlogHistoryField()


class SimpleMappingModel(models.Model):

~~    sku = models.CharField(max_length=100)
~~    vtxt = models.CharField(verbose_name='Version', max_length=100)
~~    not_mapped = models.CharField(max_length=100)

    history = AuditlogHistoryField()


class AdditionalDataIncludedModel(models.Model):

~~    label = models.CharField(max_length=100)
~~    text = models.TextField(blank=True)
~~    related = models.ForeignKey(to=SimpleModel, on_delete=models.CASCADE)

    history = AuditlogHistoryField()

    def get_additional_data(self):
        object_details = {
            'related_model_id': self.related.id,
            'related_model_text': self.related.text
        }
        return object_details


class DateTimeFieldModel(models.Model):
~~    label = models.CharField(max_length=100)
~~    timestamp = models.DateTimeField()
~~    date = models.DateField()
~~    time = models.TimeField()
~~    naive_dt = models.DateTimeField(null=True, blank=True)

    history = AuditlogHistoryField()


class ChoicesFieldModel(models.Model):
    RED = 'r'
    YELLOW = 'y'
    GREEN = 'g'

    STATUS_CHOICES = (
        (RED, 'Red'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
    )

~~    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    multiselect = MultiSelectField(max_length=3, choices=STATUS_CHOICES, max_choices=3)
~~    multiplechoice = models.CharField(max_length=255, choices=STATUS_CHOICES)

    history = AuditlogHistoryField()


class CharfieldTextfieldModel(models.Model):

~~    longchar = models.CharField(max_length=255)
~~    longtextfield = models.TextField()

    history = AuditlogHistoryField()


class PostgresArrayFieldModel(models.Model):
    RED = 'r'
    YELLOW = 'y'
    GREEN = 'g'

    STATUS_CHOICES = (
        (RED, 'Red'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
    )

    arrayfield = ArrayField(models.CharField(max_length=1, choices=STATUS_CHOICES), size=3)

    history = AuditlogHistoryField()


class NoDeleteHistoryModel(models.Model):
~~    integer = models.IntegerField(blank=True, null=True)

    history = AuditlogHistoryField(delete_related=False)


auditlog.register(AltPrimaryKeyModel)
auditlog.register(UUIDPrimaryKeyModel)
auditlog.register(ProxyModel)
auditlog.register(RelatedModel)
auditlog.register(ManyRelatedModel)
auditlog.register(ManyRelatedModel.related.through)
auditlog.register(SimpleExcludeModel, exclude_fields=['text'])
auditlog.register(SimpleMappingModel, mapping_fields={'sku': 'Product No.'})
auditlog.register(AdditionalDataIncludedModel)
auditlog.register(DateTimeFieldModel)
auditlog.register(ChoicesFieldModel)
auditlog.register(CharfieldTextfieldModel)
auditlog.register(PostgresArrayFieldModel)
auditlog.register(NoDeleteHistoryModel)



## ... source file continues with no further models examples...

```


## Example 2 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / chair / forms.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/chair/forms.py)

```python
# forms.py
from functools import reduce

from django import forms
from django.contrib.auth import get_user_model
~~from django.db import models
from django.db.models import Q, F, Count, Max, Subquery, OuterRef, Value
from django.db.models.functions import Concat
from django.forms import MultipleChoiceField, ChoiceField, Form
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from django_countries import countries

from conferences.models import Conference, ArtifactDescriptor
from gears.widgets import CustomCheckboxSelectMultiple, CustomFileInput
from review.models import Reviewer, Review, ReviewStats
from review.utilities import get_average_score
from submissions.models import Submission, Attachment
from users.models import Profile

User = get_user_model()


def clean_data_to_int(iterable, empty=None):
    return [int(x) if x != '' else None for x in iterable]


def q_or(disjuncts, default=True):
    if disjuncts:


## ... source file abbreviated to get to models examples ...


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert isinstance(self.instance, Conference)
        countries_dict = dict(countries)

        self.fields['countries'].choices = [
            (code, countries_dict[code]) for code in
            Profile.objects.filter(country__isnull=False).values_list(
                'country', flat=True).order_by('country').distinct()]

        self.fields['affiliations'].choices = [
            (aff, aff) for aff in
            Profile.objects.values_list('affiliation', flat=True).order_by(
                'affiliation').distinct() if aff]

    def order_profiles(self, profiles):
        order = self.cleaned_data['order']
        direction = '-' if self.cleaned_data['direction'] == 'DESC' else ''
        if order == self.ORDER_BY_ID or not order:
            return profiles.order_by(f'{direction}pk')

        elif order == self.ORDER_BY_NAME:
            profiles = profiles.annotate(
                full_name=Concat(
                    'last_name', Value(' '), 'first_name',
~~                    output_field=models.CharField()))
            return profiles.order_by(f'{direction}full_name')

        return profiles

    def apply_term(self, profiles):
        term = self.cleaned_data['term']
        for word in term.lower().split():
            profiles = profiles.filter(
                Q(pk__icontains=word) | Q(first_name__icontains=word) |
                Q(last_name__icontains=word) |
                Q(first_name_rus__icontains=word) |
                Q(last_name_rus__icontains=word) |
                Q(middle_name_rus__icontains=word))
        return profiles

    def apply_countries(self, profiles):
        data = self.cleaned_data['countries']
        if data:
            profiles = profiles.filter(country__in=data)
        return profiles

    def apply_affiliations(self, profiles):
        data = self.cleaned_data['affiliations']
        if data:


## ... source file continues with no further models examples...

```


## Example 3 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / tests.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/./tests.py)

```python
# tests.py
from __future__ import unicode_literals

import json
import requests
from datetime import date, datetime

import django
from django.core.files.base import ContentFile
~~from django.db import models
from django.test import RequestFactory, TestCase
from django.utils.http import base36_to_int, int_to_base36
from django.views import csrf

from . import utils


try:
    from unittest.mock import Mock, patch
except ImportError:
    from mock import Mock, patch  # noqa


class MockedResponse(object):
    def __init__(self, status_code, content, headers=None):
        if headers is None:
            headers = {}

        self.status_code = status_code
        self.content = content.encode('utf8')
        self.headers = headers

    def json(self):
        return json.loads(self.text)


## ... source file abbreviated to get to models examples ...



    def test_email_validation(self):
        s = 'this.email.address.is.a.bit.too.long.but.should.still.validate@example.com'  # noqa
        self.assertEqual(s, utils.valid_email_or_none(s))

    def test_serializer(self):

        class SomeValue:
            pass

        some_value = SomeValue()

        class SomeField(models.Field):
            def get_prep_value(self, value):
                return 'somevalue'
            if django.VERSION < (3, 0):
                def from_db_value(
                    self, value, expression, connection, context
                ):
                    return some_value
            else:
                def from_db_value(self, value, expression, connection):
                    return some_value

        class SomeModel(models.Model):
~~            dt = models.DateTimeField()
~~            t = models.TimeField()
~~            d = models.DateField()
~~            img1 = models.ImageField()
~~            img2 = models.ImageField()
~~            img3 = models.ImageField()
            something = SomeField()

        def method(self):
            pass

        instance = SomeModel(dt=datetime.now(),
                             d=date.today(),
                             something=some_value,
                             t=datetime.now().time())
        content_file = ContentFile(b'%PDF')
        content_file.name = 'foo.pdf'
        instance.img1 = content_file
        instance.img2 = 'foo.png'
        instance.method = method
        instance.nonfield = 'hello'
        data = utils.serialize_instance(instance)
        instance2 = utils.deserialize_instance(SomeModel, data)
        self.assertEqual(getattr(instance, 'method', None), method)
        self.assertEqual(getattr(instance2, 'method', None), None)
        self.assertEqual(instance2.something, some_value)
        self.assertEqual(instance2.img1.name, 'foo.pdf')
        self.assertEqual(instance2.img2.name, 'foo.png')
        self.assertEqual(instance2.img3.name, '')
        self.assertEqual(instance.nonfield, instance2.nonfield)
        self.assertEqual(instance.d, instance2.d)
        self.assertEqual(instance.dt.date(), instance2.dt.date())
        for t1, t2 in [(instance.t, instance2.t),
                       (instance.dt.time(), instance2.dt.time())]:
            self.assertEqual(t1.hour, t2.hour)
            self.assertEqual(t1.minute, t2.minute)
            self.assertEqual(t1.second, t2.second)
            self.assertEqual(int(t1.microsecond / 1000),
                             int(t2.microsecond / 1000))

    def test_serializer_binary_field(self):
        class SomeBinaryModel(models.Model):
~~            bb = models.BinaryField()
~~            bb_empty = models.BinaryField()

        instance = SomeBinaryModel(bb=b'some binary data')

        serialized = utils.serialize_instance(instance)
        deserialized = utils.deserialize_instance(SomeBinaryModel, serialized)

        self.assertEqual(serialized['bb'], 'c29tZSBiaW5hcnkgZGF0YQ==')
        self.assertEqual(serialized['bb_empty'], '')
        self.assertEqual(deserialized.bb, b'some binary data')
        self.assertEqual(deserialized.bb_empty, b'')

    def test_build_absolute_uri(self):
        self.assertEqual(
            utils.build_absolute_uri(None, '/foo'),
            'http://example.com/foo')
        self.assertEqual(
            utils.build_absolute_uri(None, '/foo', protocol='ftp'),
            'ftp://example.com/foo')
        self.assertEqual(
            utils.build_absolute_uri(None, 'http://foo.com/bar'),
            'http://foo.com/bar')

    def test_int_to_base36(self):
        n = 55798679658823689999


## ... source file continues with no further models examples...

```


## Example 4 from django-axes
[django-axes](https://github.com/jazzband/django-axes/)
([project documentation](https://django-axes.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-axes/)
is a code library for [Django](/django.html) projects to track failed
login attempts against a web application. The goal of the project is
to make it easier for you to stop people and scripts from hacking your
Django-powered website.

The code for django-axes is
[open source under the MIT license](https://github.com/jazzband/django-axes/blob/master/LICENSE)
and maintained by the group of developers known as
[Jazzband](https://jazzband.co/).

[**django-axes / axes / models.py**](https://github.com/jazzband/django-axes/blob/master/axes/./models.py)

```python
# models.py
~~from django.db import models
from django.utils.translation import gettext_lazy as _


class AccessBase(models.Model):
~~    user_agent = models.CharField(_("User Agent"), max_length=255, db_index=True)

~~    ip_address = models.GenericIPAddressField(_("IP Address"), null=True, db_index=True)

~~    username = models.CharField(_("Username"), max_length=255, null=True, db_index=True)

~~    http_accept = models.CharField(_("HTTP Accept"), max_length=1025)

~~    path_info = models.CharField(_("Path"), max_length=255)

~~    attempt_time = models.DateTimeField(_("Attempt Time"), auto_now_add=True)

    class Meta:
        app_label = "axes"
        abstract = True
        ordering = ["-attempt_time"]


class AccessAttempt(AccessBase):
~~    get_data = models.TextField(_("GET Data"))

~~    post_data = models.TextField(_("POST Data"))

~~    failures_since_start = models.PositiveIntegerField(_("Failed Logins"))

    def __str__(self):
        return f"Attempted Access: {self.attempt_time}"

    class Meta:
        verbose_name = _("access attempt")
        verbose_name_plural = _("access attempts")


class AccessLog(AccessBase):
~~    logout_time = models.DateTimeField(_("Logout Time"), null=True, blank=True)

    def __str__(self):
        return f"Access Log for {self.username} @ {self.attempt_time}"

    class Meta:
        verbose_name = _("access log")
        verbose_name_plural = _("access logs")



## ... source file continues with no further models examples...

```


## Example 5 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / migrations / 0008_auto_20150208_2149.py**](https://github.com/divio/django-cms/blob/develop/cms/migrations/0008_auto_20150208_2149.py)

```python
# 0008_auto_20150208_2149.py
from __future__ import unicode_literals

~~from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_auto_20141028_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='redirect',
~~            field=models.CharField(max_length=2048, null=True, verbose_name='redirect', blank=True),
            preserve_default=True,
        ),
    ]



## ... source file continues with no further models examples...

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
~~from django.db import models
from django.db.models.query import QuerySet
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


## ... source file abbreviated to get to models examples ...


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

    def get_help_text(self, field_name, model_name):
        searchable_fields = self.related_search_fields.get(field_name, None)
        if searchable_fields:
            help_kwargs = {
                'model_name': model_name,
                'field_list': get_text_list(searchable_fields, _('and')),
            }
            return _('Use the left field to do %(model_name)s lookups in the fields %(field_list)s.') % help_kwargs
        return ''

    def formfield_for_dbfield(self, db_field, **kwargs):
~~        if isinstance(db_field, models.ForeignKey) and db_field.name in self.related_search_fields:
            help_text = self.get_help_text(db_field.name, db_field.remote_field.model._meta.object_name)
            if kwargs.get('help_text'):
                help_text = six.u('%s %s' % (kwargs['help_text'], help_text))
            kwargs['widget'] = ForeignKeySearchInput(db_field.remote_field, self.related_search_fields[db_field.name])
            kwargs['help_text'] = help_text
        return super().formfield_for_dbfield(db_field, **kwargs)


class ForeignKeyAutocompleteAdmin(ForeignKeyAutocompleteAdminMixin, admin.ModelAdmin):
    pass


class ForeignKeyAutocompleteTabularInline(ForeignKeyAutocompleteAdminMixin, admin.TabularInline):
    pass


class ForeignKeyAutocompleteStackedInline(ForeignKeyAutocompleteAdminMixin, admin.StackedInline):
    pass



## ... source file continues with no further models examples...

```


## Example 7 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / migrations / 0006_auto_20160623_1627.py**](https://github.com/divio/django-filer/blob/develop/filer/migrations/0006_auto_20160623_1627.py)

```python
# 0006_auto_20160623_1627.py
from __future__ import unicode_literals

import django.db.models.deletion
~~from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0005_auto_20160623_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file_ptr',
~~            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='%(app_label)s_%(class)s_file', serialize=False, to='filer.File'),
        ),
    ]



## ... source file continues with no further models examples...

```


## Example 8 from django-filter
[django-filter](https://github.com/carltongibson/django-filter)
([project documentation](https://django-filter.readthedocs.io/en/master/)
and
[PyPI page](https://pypi.org/project/django-filter/2.2.0/))
makes it easier to filter down querysets from the
[Django ORM](/django-orm.html) by providing common bits of boilerplate
code. django-filter is provided as
[open source](https://github.com/carltongibson/django-filter/blob/master/LICENSE).

[**django-filter / django_filters / filterset.py**](https://github.com/carltongibson/django-filter/blob/master/django_filters/./filterset.py)

```python
# filterset.py
import copy
from collections import OrderedDict

from django import forms
~~from django.db import models
from django.db.models.constants import LOOKUP_SEP
from django.db.models.fields.related import (
    ManyToManyRel,
    ManyToOneRel,
    OneToOneRel
)

from .conf import settings
from .constants import ALL_FIELDS
from .filters import (
    BaseInFilter,
    BaseRangeFilter,
    BooleanFilter,
    CharFilter,
    ChoiceFilter,
    DateFilter,
    DateTimeFilter,
    DurationFilter,
    Filter,
    ModelChoiceFilter,
    ModelMultipleChoiceFilter,
    NumberFilter,
    TimeFilter,
    UUIDFilter


## ... source file abbreviated to get to models examples ...


            if isinstance(obj, Filter)
        ]

        for filter_name, f in filters:
            if getattr(f, 'field_name', None) is None:
                f.field_name = filter_name

        filters.sort(key=lambda x: x[1].creation_counter)

        known = set(attrs)

        def visit(name):
            known.add(name)
            return name

        base_filters = [
            (visit(name), f)
            for base in bases if hasattr(base, 'declared_filters')
            for name, f in base.declared_filters.items() if name not in known
        ]

        return OrderedDict(base_filters + filters)


FILTER_FOR_DBFIELD_DEFAULTS = {
~~    models.AutoField:                   {'filter_class': NumberFilter},
~~    models.CharField:                   {'filter_class': CharFilter},
~~    models.TextField:                   {'filter_class': CharFilter},
~~    models.BooleanField:                {'filter_class': BooleanFilter},
~~    models.DateField:                   {'filter_class': DateFilter},
~~    models.DateTimeField:               {'filter_class': DateTimeFilter},
~~    models.TimeField:                   {'filter_class': TimeFilter},
~~    models.DurationField:               {'filter_class': DurationFilter},
~~    models.DecimalField:                {'filter_class': NumberFilter},
~~    models.SmallIntegerField:           {'filter_class': NumberFilter},
~~    models.IntegerField:                {'filter_class': NumberFilter},
~~    models.PositiveIntegerField:        {'filter_class': NumberFilter},
~~    models.PositiveSmallIntegerField:   {'filter_class': NumberFilter},
~~    models.FloatField:                  {'filter_class': NumberFilter},
~~    models.NullBooleanField:            {'filter_class': BooleanFilter},
~~    models.SlugField:                   {'filter_class': CharFilter},
~~    models.EmailField:                  {'filter_class': CharFilter},
~~    models.FilePathField:               {'filter_class': CharFilter},
~~    models.URLField:                    {'filter_class': CharFilter},
~~    models.GenericIPAddressField:       {'filter_class': CharFilter},
~~    models.CommaSeparatedIntegerField:  {'filter_class': CharFilter},
~~    models.UUIDField:                   {'filter_class': UUIDFilter},

~~    models.OneToOneField: {
        'filter_class': ModelChoiceFilter,
        'extra': lambda f: {
            'queryset': remote_queryset(f),
            'to_field_name': f.remote_field.field_name,
            'null_label': settings.NULL_CHOICE_LABEL if f.null else None,
        }
    },
~~    models.ForeignKey: {
        'filter_class': ModelChoiceFilter,
        'extra': lambda f: {
            'queryset': remote_queryset(f),
            'to_field_name': f.remote_field.field_name,
            'null_label': settings.NULL_CHOICE_LABEL if f.null else None,
        }
    },
~~    models.ManyToManyField: {
        'filter_class': ModelMultipleChoiceFilter,
        'extra': lambda f: {
            'queryset': remote_queryset(f),
        }
    },

    OneToOneRel: {
        'filter_class': ModelChoiceFilter,
        'extra': lambda f: {
            'queryset': remote_queryset(f),
            'null_label': settings.NULL_CHOICE_LABEL if f.null else None,
        }
    },
    ManyToOneRel: {
        'filter_class': ModelMultipleChoiceFilter,
        'extra': lambda f: {
            'queryset': remote_queryset(f),
        }
    },
    ManyToManyRel: {
        'filter_class': ModelMultipleChoiceFilter,
        'extra': lambda f: {
            'queryset': remote_queryset(f),
        }


## ... source file abbreviated to get to models examples ...


            queryset = self._meta.model._default_manager.all()
        model = queryset.model

        self.is_bound = data is not None
        self.data = data or {}
        self.queryset = queryset
        self.request = request
        self.form_prefix = prefix

        self.filters = copy.deepcopy(self.base_filters)

        for filter_ in self.filters.values():
            filter_.model = model
            filter_.parent = self

    def is_valid(self):
        return self.is_bound and self.form.is_valid()

    @property
    def errors(self):
        return self.form.errors

    def filter_queryset(self, queryset):
        for name, value in self.form.cleaned_data.items():
            queryset = self.filters[name].filter(queryset, value)
~~            assert isinstance(queryset, models.QuerySet), \
                "Expected '%s.%s' to return a QuerySet, but got a %s instead." \
                % (type(self).__name__, name, type(queryset).__name__)
        return queryset

    @property
    def qs(self):
        if not hasattr(self, '_qs'):
            qs = self.queryset.all()
            if self.is_bound:
                self.errors
                qs = self.filter_queryset(qs)
            self._qs = qs
        return self._qs

    def get_form_class(self):
        fields = OrderedDict([
            (name, filter_.field)
            for name, filter_ in self.filters.items()])

        return type(str('%sForm' % self.__class__.__name__),
                    (self._meta.form,), fields)

    @property
    def form(self):


## ... source file abbreviated to get to models examples ...


            "%s resolved field '%s' with '%s' lookup to an unrecognized field "
            "type %s. Try adding an override to 'Meta.filter_overrides'. See: "
            "https://django-filter.readthedocs.io/en/master/ref/filterset.html"
            "#customise-filter-generation-with-filter-overrides"
        ) % (cls.__name__, field_name, lookup_expr, field.__class__.__name__)

        return filter_class(**default)

    @classmethod
    def filter_for_lookup(cls, field, lookup_type):
        DEFAULTS = dict(cls.FILTER_DEFAULTS)
        if hasattr(cls, '_meta'):
            DEFAULTS.update(cls._meta.filter_overrides)

        data = try_dbfield(DEFAULTS.get, field.__class__) or {}
        filter_class = data.get('filter_class')
        params = data.get('extra', lambda field: {})(field)

        if not filter_class:
            return None, {}

        if lookup_type == 'exact' and getattr(field, 'choices', None):
            return ChoiceFilter, {'choices': field.choices}

        if lookup_type == 'isnull':
~~            data = try_dbfield(DEFAULTS.get, models.BooleanField)

            filter_class = data.get('filter_class')
            params = data.get('extra', lambda field: {})(field)
            return filter_class, params

        if lookup_type == 'in':
            class ConcreteInFilter(BaseInFilter, filter_class):
                pass
            ConcreteInFilter.__name__ = cls._csv_filter_class_name(
                filter_class, lookup_type
            )

            return ConcreteInFilter, params

        if lookup_type == 'range':
            class ConcreteRangeFilter(BaseRangeFilter, filter_class):
                pass
            ConcreteRangeFilter.__name__ = cls._csv_filter_class_name(
                filter_class, lookup_type
            )

            return ConcreteRangeFilter, params

        return filter_class, params


## ... source file continues with no further models examples...

```


## Example 9 from django-flexible-subscriptions
[django-flexible-subscriptions](https://github.com/studybuffalo/django-flexible-subscriptions)
([project documentation](https://django-flexible-subscriptions.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-flexible-subscriptions/))
provides boilerplate code for adding subscription and recurrent billing
to [Django](/django.html) web applications. Various payment providers
can be added on the back end to run the transactions.

The django-flexible-subscriptions project is open sourced under the
[GNU General Public License v3.0](https://github.com/studybuffalo/django-flexible-subscriptions/blob/master/LICENSE).

[**django-flexible-subscriptions / subscriptions / models.py**](https://github.com/studybuffalo/django-flexible-subscriptions/blob/master/subscriptions/./models.py)

```python
# models.py
from datetime import timedelta
from uuid import uuid4

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.validators import MinValueValidator
~~from django.db import models
from django.utils.translation import gettext_lazy as _


ONCE = '0'
SECOND = '1'
MINUTE = '2'
HOUR = '3'
DAY = '4'
WEEK = '5'
MONTH = '6'
YEAR = '7'
RECURRENCE_UNIT_CHOICES = (
    (ONCE, 'once'),
    (SECOND, 'second'),
    (MINUTE, 'minute'),
    (HOUR, 'hour'),
    (DAY, 'day'),
    (WEEK, 'week'),
    (MONTH, 'month'),
    (YEAR, 'year'),
)


class PlanTag(models.Model):
~~    tag = models.CharField(
        help_text=_('the tag name'),
        max_length=64,
        unique=True,
    )

    class Meta:
        ordering = ('tag',)

    def __str__(self):
        return self.tag


class SubscriptionPlan(models.Model):
~~    id = models.UUIDField(
        default=uuid4,
        editable=False,
        primary_key=True,
        verbose_name='ID',
    )
~~    plan_name = models.CharField(
        help_text=_('the name of the subscription plan'),
        max_length=128,
    )
~~    slug = models.SlugField(
        blank=True,
        help_text=_('slug to reference the subscription plan'),
        max_length=128,
        null=True,
        unique=True,
    )
~~    plan_description = models.CharField(
        blank=True,
        help_text=_('a description of the subscription plan'),
        max_length=512,
        null=True,
    )
~~    group = models.ForeignKey(
        Group,
        blank=True,
        help_text=_('the Django auth group for this plan'),
        null=True,
~~        on_delete=models.SET_NULL,
        related_name='plans',
    )
~~    tags = models.ManyToManyField(
        PlanTag,
        blank=True,
        help_text=_('any tags associated with this plan'),
        related_name='plans',
    )
~~    grace_period = models.PositiveIntegerField(
        default=0,
        help_text=_(
            'how many days after the subscription ends before the '
            'subscription expires'
        ),
    )

    class Meta:
        ordering = ('plan_name',)
        permissions = (
            ('subscriptions', 'Can interact with subscription details'),
        )

    def __str__(self):
        return self.plan_name

    def display_tags(self):
        if self.tags.count() > 3:
            return '{}, ...'.format(
                ', '.join(tag.tag for tag in self.tags.all()[:3])
            )

        return ', '.join(tag.tag for tag in self.tags.all()[:3])


class PlanCost(models.Model):
~~    id = models.UUIDField(
        default=uuid4,
        editable=False,
        primary_key=True,
        verbose_name='ID',
    )
~~    plan = models.ForeignKey(
        SubscriptionPlan,
        help_text=_('the subscription plan for these cost details'),
~~        on_delete=models.CASCADE,
        related_name='costs',
    )
~~    slug = models.SlugField(
        blank=True,
        help_text=_('slug to reference these cost details'),
        max_length=128,
        null=True,
        unique=True,
    )
~~    recurrence_period = models.PositiveSmallIntegerField(
        default=1,
        help_text=_('how often the plan is billed (per recurrence unit)'),
        validators=[MinValueValidator(1)],
    )
~~    recurrence_unit = models.CharField(
        choices=RECURRENCE_UNIT_CHOICES,
        default=MONTH,
        max_length=1,
    )
~~    cost = models.DecimalField(
        blank=True,
        decimal_places=4,
        help_text=_('the cost per recurrence of the plan'),
        max_digits=19,
        null=True,
    )

    class Meta:
        ordering = ('recurrence_unit', 'recurrence_period', 'cost',)

    @property
    def display_recurrent_unit_text(self):
        conversion = {
            ONCE: 'one-time',
            SECOND: 'per second',
            MINUTE: 'per minute',
            HOUR: 'per hour',
            DAY: 'per day',
            WEEK: 'per week',
            MONTH: 'per month',
            YEAR: 'per year',
        }

        return conversion[self.recurrence_unit]


## ... source file abbreviated to get to models examples ...


        if self.recurrence_unit == SECOND:
            delta = timedelta(seconds=self.recurrence_period)
        elif self.recurrence_unit == MINUTE:
            delta = timedelta(minutes=self.recurrence_period)
        elif self.recurrence_unit == HOUR:
            delta = timedelta(hours=self.recurrence_period)
        elif self.recurrence_unit == DAY:
            delta = timedelta(days=self.recurrence_period)
        elif self.recurrence_unit == WEEK:
            delta = timedelta(weeks=self.recurrence_period)
        elif self.recurrence_unit == MONTH:
            delta = timedelta(
                days=30.4368 * self.recurrence_period
            )
        elif self.recurrence_unit == YEAR:
            delta = timedelta(
                days=365.2425 * self.recurrence_period
            )
        else:
            return None

        return current + delta


class UserSubscription(models.Model):
~~    id = models.UUIDField(
        default=uuid4,
        editable=False,
        primary_key=True,
        verbose_name='ID',
    )
~~    user = models.ForeignKey(
        get_user_model(),
        help_text=_('the user this subscription applies to'),
        null=True,
~~        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
~~    subscription = models.ForeignKey(
        PlanCost,
        help_text=_('the plan costs and billing frequency for this user'),
        null=True,
~~        on_delete=models.CASCADE,
        related_name='subscriptions'
    )
~~    date_billing_start = models.DateTimeField(
        blank=True,
        help_text=_('the date to start billing this subscription'),
        null=True,
        verbose_name='billing start date',
    )
~~    date_billing_end = models.DateTimeField(
        blank=True,
        help_text=_('the date to finish billing this subscription'),
        null=True,
        verbose_name='billing start end',
    )
~~    date_billing_last = models.DateTimeField(
        blank=True,
        help_text=_('the last date this plan was billed'),
        null=True,
        verbose_name='last billing date',
    )
~~    date_billing_next = models.DateTimeField(
        blank=True,
        help_text=_('the next date billing is due'),
        null=True,
        verbose_name='next start date',
    )
~~    active = models.BooleanField(
        default=True,
        help_text=_('whether this subscription is active or not'),
    )
~~    cancelled = models.BooleanField(
        default=False,
        help_text=_('whether this subscription is cancelled or not'),
    )

    class Meta:
        ordering = ('user', 'date_billing_start',)


class SubscriptionTransaction(models.Model):
~~    id = models.UUIDField(
        default=uuid4,
        editable=False,
        primary_key=True,
        verbose_name='ID',
    )
~~    user = models.ForeignKey(
        get_user_model(),
        help_text=_('the user that this subscription was billed for'),
        null=True,
~~        on_delete=models.SET_NULL,
        related_name='subscription_transactions'
    )
~~    subscription = models.ForeignKey(
        PlanCost,
        help_text=_('the plan costs that were billed'),
        null=True,
~~        on_delete=models.SET_NULL,
        related_name='transactions'
    )
~~    date_transaction = models.DateTimeField(
        help_text=_('the datetime the transaction was billed'),
        verbose_name='transaction date',
    )
~~    amount = models.DecimalField(
        blank=True,
        decimal_places=4,
        help_text=_('how much was billed for the user'),
        max_digits=19,
        null=True,
    )

    class Meta:
        ordering = ('date_transaction', 'user',)


class PlanList(models.Model):
~~    title = models.TextField(
        blank=True,
        help_text=_('title to display on the subscription plan list page'),
        null=True,
    )
~~    slug = models.SlugField(
        blank=True,
        help_text=_('slug to reference the subscription plan list'),
        max_length=128,
        null=True,
        unique=True,
    )
~~    subtitle = models.TextField(
        blank=True,
        help_text=_('subtitle to display on the subscription plan list page'),
        null=True,
    )
~~    header = models.TextField(
        blank=True,
        help_text=_('header text to display on the subscription plan list page'),
        null=True,
    )
~~    footer = models.TextField(
        blank=True,
        help_text=_('header text to display on the subscription plan list page'),
        null=True,
    )
~~    active = models.BooleanField(
        default=True,
        help_text=_('whether this plan list is active or not.'),
    )

    def __str__(self):
        return self.title


class PlanListDetail(models.Model):
~~    plan = models.ForeignKey(
        SubscriptionPlan,
~~        on_delete=models.CASCADE,
        related_name='plan_list_details',
    )
~~    plan_list = models.ForeignKey(
        PlanList,
~~        on_delete=models.CASCADE,
        related_name='plan_list_details',
    )
~~    html_content = models.TextField(
        blank=True,
        help_text=_('HTML content to display for plan'),
        null=True,
    )
~~    subscribe_button_text = models.CharField(
        blank=True,
        default='Subscribe',
        max_length=128,
        null=True,
    )
~~    order = models.PositiveIntegerField(
        default=1,
        help_text=_('Order to display plan in (lower numbers displayed first)'),
    )

    def __str__(self):
        return 'Plan List {} - {}'.format(
            self.plan_list, self.plan.plan_name
        )



## ... source file continues with no further models examples...

```


## Example 10 from django-guardian
[django-guardian](https://github.com/django-guardian/django-guardian)
([project documentation](https://django-guardian.readthedocs.io/en/stable/)
and
[PyPI page](https://pypi.org/project/django-guardian/))
provides per-object permissions in [Django](/django.html) projects
by enhancing the existing authentication backend. The project's code
is open source under the
[MIT license](https://github.com/django-guardian/django-guardian/blob/devel/LICENSE).

[**django-guardian / guardian / backends.py**](https://github.com/django-guardian/django-guardian/blob/devel/guardian/./backends.py)

```python
# backends.py
from django.contrib.auth import get_user_model
~~from django.db import models
from guardian.conf import settings
from guardian.core import ObjectPermissionChecker
from guardian.ctypes import get_content_type
from guardian.exceptions import WrongAppError


def check_object_support(obj):
~~    return isinstance(obj, models.Model)


def check_user_support(user_obj):
    if not user_obj.is_authenticated:
        if settings.ANONYMOUS_USER_NAME is None:
            return False, user_obj
        User = get_user_model()
        lookup = {User.USERNAME_FIELD: settings.ANONYMOUS_USER_NAME}
        user_obj = User.objects.get(**lookup)

    return True, user_obj


def check_support(user_obj, obj):
    obj_support = check_object_support(obj)
    user_support, user_obj = check_user_support(user_obj)
    return obj_support and user_support, user_obj


class ObjectPermissionBackend:
    supports_object_permissions = True
    supports_anonymous_user = True
    supports_inactive_user = True



## ... source file continues with no further models examples...

```


## Example 11 from django-haystack
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

[**django-haystack / haystack / signals.py**](https://github.com/django-haystack/django-haystack/blob/master/haystack/./signals.py)

```python
# signals.py
~~from django.db import models

from haystack.exceptions import NotHandled


class BaseSignalProcessor(object):

    def __init__(self, connections, connection_router):
        self.connections = connections
        self.connection_router = connection_router
        self.setup()

    def setup(self):
        pass

    def teardown(self):
        pass

    def handle_save(self, sender, instance, **kwargs):
        using_backends = self.connection_router.for_write(instance=instance)

        for using in using_backends:
            try:
                index = self.connections[using].get_unified_index().get_index(sender)
                index.update_object(instance, using=using)
            except NotHandled:
                pass

    def handle_delete(self, sender, instance, **kwargs):
        using_backends = self.connection_router.for_write(instance=instance)

        for using in using_backends:
            try:
                index = self.connections[using].get_unified_index().get_index(sender)
                index.remove_object(instance, using=using)
            except NotHandled:
                pass


class RealtimeSignalProcessor(BaseSignalProcessor):

    def setup(self):
~~        models.signals.post_save.connect(self.handle_save)
~~        models.signals.post_delete.connect(self.handle_delete)

    def teardown(self):
~~        models.signals.post_save.disconnect(self.handle_save)
~~        models.signals.post_delete.disconnect(self.handle_delete)



## ... source file continues with no further models examples...

```


## Example 12 from django-jet
[django-jet](https://github.com/geex-arts/django-jet)
([project documentation](https://jet.readthedocs.io/en/latest/),
[PyPI project page](https://pypi.org/project/django-jet/) and
[more information](http://jet.geex-arts.com/))
is a fancy [Django](/django.html) Admin panel replacement.

The django-jet project is open source under the
[GNU Affero General Public License v3.0](https://github.com/geex-arts/django-jet/blob/dev/LICENSE).

[**django-jet / jet / models.py**](https://github.com/geex-arts/django-jet/blob/dev/jet/./models.py)

```python
# models.py
~~from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Bookmark(models.Model):
~~    url = models.URLField(verbose_name=_('URL'))
~~    title = models.CharField(verbose_name=_('title'), max_length=255)
~~    user = models.PositiveIntegerField(verbose_name=_('user'))
~~    date_add = models.DateTimeField(verbose_name=_('date created'), default=timezone.now)

    class Meta:
        verbose_name = _('bookmark')
        verbose_name_plural = _('bookmarks')
        ordering = ('date_add',)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class PinnedApplication(models.Model):
~~    app_label = models.CharField(verbose_name=_('application name'), max_length=255)
~~    user = models.PositiveIntegerField(verbose_name=_('user'))
~~    date_add = models.DateTimeField(verbose_name=_('date created'), default=timezone.now)

    class Meta:
        verbose_name = _('pinned application')
        verbose_name_plural = _('pinned applications')
        ordering = ('date_add',)

    def __str__(self):
        return self.app_label




## ... source file continues with no further models examples...

```


## Example 13 from django-jsonfield
[django-jsonfield](https://github.com/dmkoch/django-jsonfield)
([jsonfield on PyPi](https://pypi.org/project/jsonfield/)) is a
[Django](/django.html) code library that makes it easier to store validated
JSON in a [Django object-relational mapper (ORM)](/django-orm.html) database
model.

The django-jsonfield project is open source under the
[MIT license](https://github.com/dmkoch/django-jsonfield/blob/master/LICENSE).

[**django-jsonfield / src/jsonfield / fields.py**](https://github.com/dmkoch/django-jsonfield/blob/master/src/jsonfield/./fields.py)

```python
# fields.py
import copy
import json
import warnings

~~from django.db import models
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _

from . import forms
from .encoder import JSONEncoder
from .json import JSONString, checked_loads

DEFAULT_DUMP_KWARGS = {
    'cls': JSONEncoder,
}

DEFAULT_LOAD_KWARGS = {}

INVALID_JSON_WARNING = (
    '{0!s} failed to load invalid json ({1}) from the database. The value has '
    'been returned as a string instead.'
)


class JSONFieldMixin(models.Field):
    form_class = forms.JSONField

    def __init__(self, *args, dump_kwargs=None, load_kwargs=None, **kwargs):
        self.dump_kwargs = DEFAULT_DUMP_KWARGS if dump_kwargs is None else dump_kwargs


## ... source file abbreviated to get to models examples ...


    def get_prep_value(self, value):
        if self.null and value is None:
            return None
        return json.dumps(value, **self.dump_kwargs)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return json.dumps(value, **self.dump_kwargs)

    def formfield(self, **kwargs):
        kwargs.setdefault('form_class', self.form_class)
        if issubclass(kwargs['form_class'], forms.JSONField):
            kwargs.setdefault('dump_kwargs', self.dump_kwargs)
            kwargs.setdefault('load_kwargs', self.load_kwargs)

        return super().formfield(**kwargs)

    def get_default(self):
        if self.has_default():
            if callable(self.default):
                return self.default()
            return copy.deepcopy(self.default)
        return super().get_default()


~~class JSONField(JSONFieldMixin, models.TextField):

    def formfield(self, **kwargs):
        field = super().formfield(**kwargs)
        if isinstance(field, forms.JSONField):
            field.dump_kwargs.setdefault('indent', 4)
            field.dump_kwargs.setdefault('ensure_ascii', False)
        return field


~~class JSONCharField(JSONFieldMixin, models.CharField):



## ... source file continues with no further models examples...

```


## Example 14 from django-model-utils
[django-model-utils](https://github.com/jazzband/django-model-utils)
([project documentation](https://django-model-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-model-utils/))
provides useful mixins and utilities for working with
[Django ORM](/django-orm.html) models in your projects.

The django-model-utils project is open sourced under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/jazzband/django-model-utils/blob/master/LICENSE.txt).

[**django-model-utils / model_utils / models.py**](https://github.com/jazzband/django-model-utils/blob/master/model_utils/./models.py)

```python
# models.py
from django.core.exceptions import ImproperlyConfigured
~~from django.db import models, transaction, router
from django.db.models.signals import post_save, pre_save
from django.utils.translation import gettext_lazy as _

from model_utils.fields import (
    AutoCreatedField,
    AutoLastModifiedField,
    StatusField,
    MonitorField,
    UUIDField,
)
from model_utils.managers import (
    QueryManager,
    SoftDeletableManager,
)

from django.db.models.functions import Now
now = Now()


class TimeStampedModel(models.Model):
    created = AutoCreatedField(_('created'))
    modified = AutoLastModifiedField(_('modified'))

    def save(self, *args, **kwargs):
        if 'update_fields' in kwargs and 'modified' not in kwargs['update_fields']:
            kwargs['update_fields'] += ['modified']
        super().save(*args, **kwargs)
        
    class Meta:
        abstract = True


class TimeFramedModel(models.Model):
~~    start = models.DateTimeField(_('start'), null=True, blank=True)
~~    end = models.DateTimeField(_('end'), null=True, blank=True)

    class Meta:
        abstract = True


class StatusModel(models.Model):
    status = StatusField(_('status'))
    status_changed = MonitorField(_('status changed'), monitor='status')

    class Meta:
        abstract = True


def add_status_query_managers(sender, **kwargs):
    if not issubclass(sender, StatusModel):
        return

    default_manager = sender._meta.default_manager

    for value, display in getattr(sender, 'STATUS', ()):
        if _field_exists(sender, value):
            raise ImproperlyConfigured(
                "StatusModel: Model '%s' has a field named '%s' which "
                "conflicts with a status of the same name."
                % (sender.__name__, value)
            )
        sender.add_to_class(value, QueryManager(status=value))

    sender._meta.default_manager_name = default_manager.name


def add_timeframed_query_manager(sender, **kwargs):
    if not issubclass(sender, TimeFramedModel):
        return
    if _field_exists(sender, 'timeframed'):
        raise ImproperlyConfigured(
            "Model '%s' has a field named 'timeframed' "
            "which conflicts with the TimeFramedModel manager."
            % sender.__name__
        )
    sender.add_to_class('timeframed', QueryManager(
~~        (models.Q(start__lte=now) | models.Q(start__isnull=True))
~~        & (models.Q(end__gte=now) | models.Q(end__isnull=True))
    ))


models.signals.class_prepared.connect(add_status_query_managers)
models.signals.class_prepared.connect(add_timeframed_query_manager)


def _field_exists(model_class, field_name):
    return field_name in [f.attname for f in model_class._meta.local_fields]


class SoftDeletableModel(models.Model):
~~    is_removed = models.BooleanField(default=False)

    class Meta:
        abstract = True

    objects = SoftDeletableManager()
~~    all_objects = models.Manager()

    def delete(self, using=None, soft=True, *args, **kwargs):
        if soft:
            self.is_removed = True
            self.save(using=using)
        else:
            return super().delete(using=using, *args, **kwargs)


class UUIDModel(models.Model):
    id = UUIDField(
        primary_key=True,
        version=4,
        editable=False,
    )

    class Meta:
        abstract = True


class SaveSignalHandlingModel(models.Model):
    class Meta:
        abstract = True



## ... source file continues with no further models examples...

```


## Example 15 from django-oauth-toolkit
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
~~from django.db import models, transaction
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
        (GRANT_IMPLICIT, _("Implicit")),
        (GRANT_PASSWORD, _("Resource owner password-based")),
        (GRANT_CLIENT_CREDENTIALS, _("Client credentials")),
    )

~~    id = models.BigAutoField(primary_key=True)
~~    client_id = models.CharField(
        max_length=100, unique=True, default=generate_client_id, db_index=True
    )
~~    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(app_label)s_%(class)s",
~~        null=True, blank=True, on_delete=models.CASCADE
    )

~~    redirect_uris = models.TextField(
        blank=True, help_text=_("Allowed URIs list, space separated"),
    )
~~    client_type = models.CharField(max_length=32, choices=CLIENT_TYPES)
~~    authorization_grant_type = models.CharField(
        max_length=32, choices=GRANT_TYPES
    )
~~    client_secret = models.CharField(
        max_length=255, blank=True, default=generate_client_secret, db_index=True
    )
~~    name = models.CharField(max_length=255, blank=True)
~~    skip_authorization = models.BooleanField(default=False)

~~    created = models.DateTimeField(auto_now_add=True)
~~    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name or self.client_id

    @property
    def default_redirect_uri(self):
        if self.redirect_uris:
            return self.redirect_uris.split().pop(0)

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



## ... source file abbreviated to get to models examples ...




class ApplicationManager(models.Manager):
    def get_by_natural_key(self, client_id):
        return self.get(client_id=client_id)


class Application(AbstractApplication):
    objects = ApplicationManager()

    class Meta(AbstractApplication.Meta):
        swappable = "OAUTH2_PROVIDER_APPLICATION_MODEL"

    def natural_key(self):
        return (self.client_id,)


class AbstractGrant(models.Model):
    CODE_CHALLENGE_PLAIN = "plain"
    CODE_CHALLENGE_S256 = "S256"
    CODE_CHALLENGE_METHODS = (
        (CODE_CHALLENGE_PLAIN, "plain"),
        (CODE_CHALLENGE_S256, "S256")
    )

~~    id = models.BigAutoField(primary_key=True)
~~    user = models.ForeignKey(
~~        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s"
    )
~~    code = models.CharField(max_length=255, unique=True)  # code comes from oauthlib
~~    application = models.ForeignKey(
~~        oauth2_settings.APPLICATION_MODEL, on_delete=models.CASCADE
    )
~~    expires = models.DateTimeField()
~~    redirect_uri = models.CharField(max_length=255)
~~    scope = models.TextField(blank=True)

~~    created = models.DateTimeField(auto_now_add=True)
~~    updated = models.DateTimeField(auto_now=True)

~~    code_challenge = models.CharField(max_length=128, blank=True, default="")
~~    code_challenge_method = models.CharField(
        max_length=10, blank=True, default="", choices=CODE_CHALLENGE_METHODS)

    def is_expired(self):
        if not self.expires:
            return True

        return timezone.now() >= self.expires

    def redirect_uri_allowed(self, uri):
        return uri == self.redirect_uri

    def __str__(self):
        return self.code

    class Meta:
        abstract = True


class Grant(AbstractGrant):
    class Meta(AbstractGrant.Meta):
        swappable = "OAUTH2_PROVIDER_GRANT_MODEL"


class AbstractAccessToken(models.Model):
~~    id = models.BigAutoField(primary_key=True)
~~    user = models.ForeignKey(
~~        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,
        related_name="%(app_label)s_%(class)s"
    )
~~    source_refresh_token = models.OneToOneField(
~~        oauth2_settings.REFRESH_TOKEN_MODEL, on_delete=models.SET_NULL, blank=True, null=True,
        related_name="refreshed_access_token"
    )
~~    token = models.CharField(max_length=255, unique=True, )
~~    application = models.ForeignKey(
~~        oauth2_settings.APPLICATION_MODEL, on_delete=models.CASCADE, blank=True, null=True,
    )
~~    expires = models.DateTimeField()
~~    scope = models.TextField(blank=True)

~~    created = models.DateTimeField(auto_now_add=True)
~~    updated = models.DateTimeField(auto_now=True)

    def is_valid(self, scopes=None):
        return not self.is_expired() and self.allow_scopes(scopes)

    def is_expired(self):
        if not self.expires:
            return True

        return timezone.now() >= self.expires

    def allow_scopes(self, scopes):
        if not scopes:
            return True

        provided_scopes = set(self.scope.split())
        resource_scopes = set(scopes)

        return resource_scopes.issubset(provided_scopes)

    def revoke(self):
        self.delete()

    @property
    def scopes(self):
        all_scopes = get_scopes_backend().get_all_scopes()
        token_scopes = self.scope.split()
        return {name: desc for name, desc in all_scopes.items() if name in token_scopes}

    def __str__(self):
        return self.token

    class Meta:
        abstract = True


class AccessToken(AbstractAccessToken):
    class Meta(AbstractAccessToken.Meta):
        swappable = "OAUTH2_PROVIDER_ACCESS_TOKEN_MODEL"


class AbstractRefreshToken(models.Model):
~~    id = models.BigAutoField(primary_key=True)
~~    user = models.ForeignKey(
~~        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s"
    )
~~    token = models.CharField(max_length=255)
~~    application = models.ForeignKey(
~~        oauth2_settings.APPLICATION_MODEL, on_delete=models.CASCADE)
~~    access_token = models.OneToOneField(
~~        oauth2_settings.ACCESS_TOKEN_MODEL, on_delete=models.SET_NULL, blank=True, null=True,
        related_name="refresh_token"
    )

~~    created = models.DateTimeField(auto_now_add=True)
~~    updated = models.DateTimeField(auto_now=True)
~~    revoked = models.DateTimeField(null=True)

    def revoke(self):
        access_token_model = get_access_token_model()
        refresh_token_model = get_refresh_token_model()
        with transaction.atomic():
            self = refresh_token_model.objects.filter(
                pk=self.pk, revoked__isnull=True
            ).select_for_update().first()
            if not self:
                return

            try:
                access_token_model.objects.get(id=self.access_token_id).revoke()
            except access_token_model.DoesNotExist:
                pass
            self.access_token = None
            self.revoked = timezone.now()
            self.save()

    def __str__(self):
        return self.token

    class Meta:
        abstract = True


## ... source file continues with no further models examples...

```


## Example 16 from django-push-notifications
[django-push-notifications](https://github.com/jazzband/django-push-notifications)
is a [Django](/django.html) app for storing and interacting with
push notification services such as
[Google's Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/)
and
[Apple Notifications](https://developer.apple.com/notifications/).
The django-push-notification project's source code is available
open source under the
[MIT license](https://github.com/jazzband/django-push-notifications/blob/master/LICENSE).

[**django-push-notifications / push_notifications / models.py**](https://github.com/jazzband/django-push-notifications/blob/master/push_notifications/./models.py)

```python
# models.py
~~from django.db import models
from django.utils.translation import ugettext_lazy as _

from .fields import HexIntegerField
from .settings import PUSH_NOTIFICATIONS_SETTINGS as SETTINGS


CLOUD_MESSAGE_TYPES = (
	("FCM", "Firebase Cloud Message"),
	("GCM", "Google Cloud Message"),
)

BROWSER_TYPES = (
	("CHROME", "Chrome"),
	("FIREFOX", "Firefox"),
	("OPERA", "Opera"),
)


class Device(models.Model):
~~	name = models.CharField(max_length=255, verbose_name=_("Name"), blank=True, null=True)
~~	active = models.BooleanField(
		verbose_name=_("Is active"), default=True,
		help_text=_("Inactive devices will not be sent notifications")
	)
~~	user = models.ForeignKey(
~~		SETTINGS["USER_MODEL"], blank=True, null=True, on_delete=models.CASCADE
	)
~~	date_created = models.DateTimeField(
		verbose_name=_("Creation date"), auto_now_add=True, null=True
	)
~~	application_id = models.CharField(
		max_length=64, verbose_name=_("Application ID"),
		help_text=_(
			"Opaque application identity, should be filled in for multiple"
			" key/certificate access"
		),
		blank=True, null=True
	)

	class Meta:
		abstract = True

	def __str__(self):
		return (
			self.name or
			str(self.device_id or "") or
			"{} for {}".format(self.__class__.__name__, self.user or "unknown user")
		)


class GCMDeviceManager(models.Manager):
	def get_queryset(self):
		return GCMDeviceQuerySet(self.model)




## ... source file abbreviated to get to models examples ...



			app_ids = self.filter(active=True).order_by(
				"application_id"
			).values_list("application_id", flat=True).distinct()
			response = []
			for cloud_type in ("FCM", "GCM"):
				for app_id in app_ids:
					reg_ids = list(
						self.filter(
							active=True, cloud_message_type=cloud_type, application_id=app_id).values_list(
							"registration_id", flat=True
						)
					)
					if reg_ids:
						r = gcm_send_message(reg_ids, data, cloud_type, application_id=app_id, **kwargs)
						response.append(r)

			return response


class GCMDevice(Device):
	device_id = HexIntegerField(
		verbose_name=_("Device ID"), blank=True, null=True, db_index=True,
		help_text=_("ANDROID_ID / TelephonyManager.getDeviceId() (always as hex)")
	)
~~	registration_id = models.TextField(verbose_name=_("Registration ID"), unique=SETTINGS["UNIQUE_REG_ID"])
~~	cloud_message_type = models.CharField(
		verbose_name=_("Cloud Message Type"), max_length=3,
		choices=CLOUD_MESSAGE_TYPES, default="GCM",
		help_text=_("You should choose FCM or GCM")
	)
	objects = GCMDeviceManager()

	class Meta:
		verbose_name = _("GCM device")

	def send_message(self, message, **kwargs):
		from .gcm import send_message as gcm_send_message

		data = kwargs.pop("extra", {})
		if message is not None:
			data["message"] = message

		return gcm_send_message(
			self.registration_id, data, self.cloud_message_type,
			application_id=self.application_id, **kwargs
		)


class APNSDeviceManager(models.Manager):
	def get_queryset(self):


## ... source file abbreviated to get to models examples ...



class APNSDeviceQuerySet(models.query.QuerySet):
	def send_message(self, message, creds=None, **kwargs):
		if self:
			from .apns import apns_send_bulk_message

			app_ids = self.filter(active=True).order_by("application_id")\
				.values_list("application_id", flat=True).distinct()
			res = []
			for app_id in app_ids:
				reg_ids = list(self.filter(active=True, application_id=app_id).values_list(
					"registration_id", flat=True)
				)
				r = apns_send_bulk_message(
					registration_ids=reg_ids, alert=message, application_id=app_id,
					creds=creds, **kwargs
				)
				if hasattr(r, "keys"):
					res += [r]
				elif hasattr(r, "__getitem__"):
					res += r
			return res


class APNSDevice(Device):
~~	device_id = models.UUIDField(
		verbose_name=_("Device ID"), blank=True, null=True, db_index=True,
		help_text="UDID / UIDevice.identifierForVendor()"
	)
~~	registration_id = models.CharField(
		verbose_name=_("Registration ID"), max_length=200, unique=SETTINGS["UNIQUE_REG_ID"]
	)

	objects = APNSDeviceManager()

	class Meta:
		verbose_name = _("APNS device")

	def send_message(self, message, creds=None, **kwargs):
		from .apns import apns_send_message

		return apns_send_message(
			registration_id=self.registration_id,
			alert=message,
			application_id=self.application_id, creds=creds,
			**kwargs
		)


class WNSDeviceManager(models.Manager):
	def get_queryset(self):
		return WNSDeviceQuerySet(self.model)


class WNSDeviceQuerySet(models.query.QuerySet):
	def send_message(self, message, **kwargs):
		from .wns import wns_send_bulk_message

		app_ids = self.filter(active=True).order_by("application_id").values_list(
			"application_id", flat=True
		).distinct()
		res = []
		for app_id in app_ids:
			reg_ids = self.filter(active=True, application_id=app_id).values_list(
				"registration_id", flat=True
			)
			r = wns_send_bulk_message(uri_list=list(reg_ids), message=message, **kwargs)
			if hasattr(r, "keys"):
				res += [r]
			elif hasattr(r, "__getitem__"):
				res += r

		return res


class WNSDevice(Device):
~~	device_id = models.UUIDField(
		verbose_name=_("Device ID"), blank=True, null=True, db_index=True,
		help_text=_("GUID()")
	)
~~	registration_id = models.TextField(verbose_name=_("Notification URI"), unique=SETTINGS["UNIQUE_REG_ID"])

	objects = WNSDeviceManager()

	class Meta:
		verbose_name = _("WNS device")

	def send_message(self, message, **kwargs):
		from .wns import wns_send_message

		return wns_send_message(
			uri=self.registration_id, message=message, application_id=self.application_id,
			**kwargs
		)


class WebPushDeviceManager(models.Manager):
	def get_queryset(self):
		return WebPushDeviceQuerySet(self.model)


class WebPushDeviceQuerySet(models.query.QuerySet):
	def send_message(self, message, **kwargs):
		devices = self.filter(active=True).order_by("application_id").distinct()
		res = []
		for device in devices:
			res.append(device.send_message(message))

		return res


class WebPushDevice(Device):
~~	registration_id = models.TextField(verbose_name=_("Registration ID"), unique=SETTINGS["UNIQUE_REG_ID"])
~~	p256dh = models.CharField(
		verbose_name=_("User public encryption key"),
		max_length=88)
~~	auth = models.CharField(
		verbose_name=_("User auth secret"),
		max_length=24)
~~	browser = models.CharField(
		verbose_name=_("Browser"), max_length=10,
		choices=BROWSER_TYPES, default=BROWSER_TYPES[0][0],
		help_text=_("Currently only support to Chrome, Firefox and Opera browsers")
	)
	objects = WebPushDeviceManager()

	class Meta:
		verbose_name = _("WebPush device")

	@property
	def device_id(self):
		return None

	def send_message(self, message, **kwargs):
		from .webpush import webpush_send_message

		return webpush_send_message(
			uri=self.registration_id, message=message, browser=self.browser,
			auth=self.auth, p256dh=self.p256dh, application_id=self.application_id, **kwargs)



## ... source file continues with no further models examples...

```


## Example 17 from django-rest-framework
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

from django.core.exceptions import FieldDoesNotExist, ImproperlyConfigured
from django.core.exceptions import ValidationError as DjangoValidationError
~~from django.db import models
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

from rest_framework.fields import (  # NOQA # isort:skip


## ... source file abbreviated to get to models examples ...



        if not self.allow_empty and len(data) == 0:
            message = self.error_messages['empty']
            raise ValidationError({
                api_settings.NON_FIELD_ERRORS_KEY: [message]
            }, code='empty')

        ret = []
        errors = []

        for item in data:
            try:
                validated = self.child.run_validation(item)
            except ValidationError as exc:
                errors.append(exc.detail)
            else:
                ret.append(validated)
                errors.append({})

        if any(errors):
            raise ValidationError(errors)

        return ret

    def to_representation(self, data):
~~        iterable = data.all() if isinstance(data, models.Manager) else data

        return [
            self.child.to_representation(item) for item in iterable
        ]

    def validate(self, attrs):
        return attrs

    def update(self, instance, validated_data):
        raise NotImplementedError(
            "Serializers with many=True do not support multiple update by "
            "default, only multiple create. For updates it is unclear how to "
            "deal with insertions and deletions. If you need to support "
            "multiple update, use a `ListSerializer` class and override "
            "`.update()` so you can specify the behavior exactly."
        )

    def create(self, validated_data):
        return [
            self.child.create(attrs) for attrs in validated_data
        ]

    def save(self, **kwargs):
        assert 'commit' not in kwargs, (


## ... source file abbreviated to get to models examples ...


            module=serializer.__class__.__module__,
            class_name=serializer.__class__.__name__
        )
    )

    assert not any(
        len(field.source_attrs) > 1 and
        (field.source_attrs[0] in validated_data) and
        (field.source_attrs[0] in model_field_info.relations) and
        isinstance(validated_data[field.source_attrs[0]], (list, dict))
        for field in serializer._writable_fields
    ), (
        'The `.{method_name}()` method does not support writable dotted-source '
        'fields by default.\nWrite an explicit `.{method_name}()` method for '
        'serializer `{module}.{class_name}`, or set `read_only=True` on '
        'dotted-source serializer fields.'.format(
            method_name=method_name,
            module=serializer.__class__.__module__,
            class_name=serializer.__class__.__name__
        )
    )


class ModelSerializer(Serializer):
    serializer_field_mapping = {
~~        models.AutoField: IntegerField,
~~        models.BigIntegerField: IntegerField,
~~        models.BooleanField: BooleanField,
~~        models.CharField: CharField,
~~        models.CommaSeparatedIntegerField: CharField,
~~        models.DateField: DateField,
~~        models.DateTimeField: DateTimeField,
~~        models.DecimalField: DecimalField,
~~        models.DurationField: DurationField,
~~        models.EmailField: EmailField,
~~        models.Field: ModelField,
~~        models.FileField: FileField,
~~        models.FloatField: FloatField,
~~        models.ImageField: ImageField,
~~        models.IntegerField: IntegerField,
~~        models.NullBooleanField: BooleanField,
~~        models.PositiveIntegerField: IntegerField,
~~        models.PositiveSmallIntegerField: IntegerField,
~~        models.SlugField: SlugField,
~~        models.SmallIntegerField: IntegerField,
~~        models.TextField: CharField,
~~        models.TimeField: TimeField,
~~        models.URLField: URLField,
~~        models.UUIDField: UUIDField,
~~        models.GenericIPAddressField: IPAddressField,
~~        models.FilePathField: FilePathField,
    }
    if postgres_fields:
        serializer_field_mapping[postgres_fields.HStoreField] = HStoreField
        serializer_field_mapping[postgres_fields.ArrayField] = ListField
        serializer_field_mapping[postgres_fields.JSONField] = JSONField
    serializer_related_field = PrimaryKeyRelatedField
    serializer_related_to_field = SlugRelatedField
    serializer_url_field = HyperlinkedIdentityField
    serializer_choice_field = ChoiceField

    url_field_name = None

    def create(self, validated_data):
        raise_errors_on_nested_writes('create', self, validated_data)

        ModelClass = self.Meta.model

        info = model_meta.get_field_info(ModelClass)
        many_to_many = {}
        for field_name, relation_info in info.relations.items():
            if relation_info.to_many and (field_name in validated_data):
                many_to_many[field_name] = validated_data.pop(field_name)

        try:


## ... source file continues with no further models examples...

```


## Example 18 from django-sitetree
[django-sitetree](https://github.com/idlesign/django-sitetree)
([project documentation](https://django-sitetree.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-sitetree/))
is a [Django](/django.html) extension that makes it easier for
developers to add site trees, menus and breadcrumb navigation elements
to their web applications.

The django-sitetree project is provided as open source under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/idlesign/django-sitetree/blob/master/LICENSE).

[**django-sitetree / sitetree / models.py**](https://github.com/idlesign/django-sitetree/blob/master/sitetree/./models.py)

```python
# models.py
from django.contrib.auth.models import Permission
~~from django.db import models
from django.utils.translation import gettext_lazy as _

from .settings import MODEL_TREE, TREE_ITEMS_ALIASES


class CharFieldNullable(models.CharField):
    def get_prep_value(self, value):
        if value is not None:
            if value.strip() == '':
                return None
        return self.to_python(value)


class TreeBase(models.Model):

~~    title = models.CharField(
        _('Title'), max_length=100, help_text=_('Site tree title for presentational purposes.'), blank=True)

~~    alias = models.CharField(
        _('Alias'), max_length=80,
        help_text=_('Short name to address site tree from templates.<br /><b>Note:</b> change with care.'),
        unique=True, db_index=True)

    class Meta:
        abstract = True
        verbose_name = _('Site Tree')
        verbose_name_plural = _('Site Trees')

    def get_title(self) -> str:
        return self.title or self.alias

    def __str__(self) -> str:
        return self.alias


class TreeItemBase(models.Model):

    PERM_TYPE_ANY = 1
    PERM_TYPE_ALL = 2

    PERM_TYPE_CHOICES = {
        PERM_TYPE_ANY: _('Any'),
        PERM_TYPE_ALL: _('All'),
    }

~~    title = models.CharField(
        _('Title'), max_length=100,
        help_text=_('Site tree item title. Can contain template variables E.g.: {{ mytitle }}.'))

~~    hint = models.CharField(
        _('Hint'), max_length=200,
        help_text=_('Some additional information about this item that is used as a hint.'), blank=True, default='')

~~    url = models.CharField(
        _('URL'), max_length=200,
        help_text=_('Exact URL or URL pattern (see "Additional settings") for this item.'), db_index=True)

~~    urlaspattern = models.BooleanField(
        _('URL as Pattern'),
        help_text=_('Whether the given URL should be treated as a pattern.<br />'
                    '<b>Note:</b> Refer to Django "URL dispatcher" documentation (e.g. "Naming URL patterns" part).'),
        db_index=True, default=False)

~~    tree = models.ForeignKey(
~~        MODEL_TREE, related_name='%(class)s_tree', on_delete=models.CASCADE, verbose_name=_('Site Tree'),
        help_text=_('Site tree this item belongs to.'), db_index=True)

~~    hidden = models.BooleanField(
        _('Hidden'), help_text=_('Whether to show this item in navigation.'), db_index=True, default=False)

    alias = CharFieldNullable(
        _('Alias'), max_length=80,
        help_text=_(
            'Short name to address site tree item from a template.<br />'
            '<b>Reserved aliases:</b> "%s".' % '", "'.join(TREE_ITEMS_ALIASES)
        ),
        db_index=True, blank=True, null=True)

~~    description = models.TextField(
        _('Description'),
        help_text=_('Additional comments on this item.'), blank=True, default='')

~~    inmenu = models.BooleanField(
        _('Show in menu'),
        help_text=_('Whether to show this item in a menu.'), db_index=True, default=True)

~~    inbreadcrumbs = models.BooleanField(
        _('Show in breadcrumb path'),
        help_text=_('Whether to show this item in a breadcrumb path.'), db_index=True, default=True)

~~    insitetree = models.BooleanField(
        _('Show in site tree'),
        help_text=_('Whether to show this item in a site tree.'), db_index=True, default=True)

~~    access_loggedin = models.BooleanField(
        _('Logged in only'),
        help_text=_('Check it to grant access to this item to authenticated users only.'),
        db_index=True, default=False)

~~    access_guest = models.BooleanField(
        _('Guests only'),
        help_text=_('Check it to grant access to this item to guests only.'), db_index=True, default=False)

~~    access_restricted = models.BooleanField(
        _('Restrict access to permissions'),
        help_text=_('Check it to restrict user access to this item, using Django permissions system.'),
        db_index=True, default=False)

~~    access_permissions = models.ManyToManyField(
        Permission, verbose_name=_('Permissions granting access'), blank=True)

~~    access_perm_type = models.IntegerField(
        _('Permissions interpretation'),
        help_text=_('<b>Any</b> &mdash; user should have any of chosen permissions. '
                    '<b>All</b> &mdash; user should have all chosen permissions.'),
        choices=PERM_TYPE_CHOICES.items(), default=PERM_TYPE_ANY)

~~    parent = models.ForeignKey(
~~        'self', related_name='%(class)s_parent', on_delete=models.CASCADE, verbose_name=_('Parent'),
        help_text=_('Parent site tree item.'), db_index=True, null=True, blank=True)

~~    sort_order = models.IntegerField(
        _('Sort order'),
        help_text=_('Item position among other site tree items under the same parent.'), db_index=True, default=0)

    def save(self, force_insert=False, force_update=False, **kwargs):
        if self.parent == self:
            self.parent = None
        
        id_ = self.id
        if id_ and self.sort_order == 0:
            self.sort_order = id_
        
        super().save(force_insert, force_update, **kwargs)

        if self.sort_order == 0:
            self.sort_order = self.id
            self.save()

    class Meta:
        abstract = True
        verbose_name = _('Site Tree Item')
        verbose_name_plural = _('Site Tree Items')
        unique_together = ('tree', 'alias')

    def __str__(self) -> str:


## ... source file continues with no further models examples...

```


## Example 19 from django-smithy
[django-smithy](https://github.com/jamiecounsell/django-smithy) is
a [Django](/django.html) code library that allows users to send
HTTP requests from the Django admin user interface. The code for
the project is open source under the
[MIT license](https://github.com/jamiecounsell/django-smithy/blob/master/LICENSE).

[**django-smithy / smithy / models.py**](https://github.com/jamiecounsell/django-smithy/blob/master/smithy/./models.py)

```python
# models.py

~~from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from requests import Request as HTTPRequest, Session
from requests.cookies import create_cookie, RequestsCookieJar
from urllib.parse import parse_qs, urlparse, urlencode
from requests_toolbelt.utils import dump

from model_utils.models import TimeStampedModel

from smithy.helpers import render_with_context, parse_dump_result


class NameValueModel(TimeStampedModel):
~~    name = models.CharField(max_length = 200)
~~    value = models.TextField(blank = True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Request(TimeStampedModel):
    METHODS = (
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('DELETE', 'DELETE'),
        ('OPTIONS', 'OPTIONS'),
        ('HEAD', 'HEAD'),
    )
    BODY_TYPES = (
        ('', 'Other'),
        ('application/x-www-form-urlencoded', 'x-www-form-urlencoded'),
        ('application/json', 'JSON'),
        ('text/plain', 'Text'),
        ('application/javascript', 'JavaScript'),
        ('application/xml', 'XML (application/xml)'),
        ('text/xml', 'XML (text/xml)'),
        ('text/html', 'HTML'),
    )
~~    method = models.CharField(
        max_length = 7, choices = METHODS,
        blank = False, null = False)
~~    name = models.CharField(max_length = 500, blank = False)
~~    url = models.CharField(max_length = 2083)
~~    body = models.TextField(blank = True)
~~    content_type = models.CharField(
        default = BODY_TYPES[0][0],
        blank = True, null = True,
        max_length = 100, choices = BODY_TYPES)

    def __str__(self):
        if self.name:
            return self.name
        return "{} {}".format(
            self.method,
            self.url,
        )


class RequestBlueprint(Request):
~~    follow_redirects = models.BooleanField(
        default = False, blank = False, null = False)

    @property
    def name_value_related(self):
        return [
            self.headers,
            self.query_parameters,
            self.cookies
        ]

    def send(self, context = None):

        context = context or {}
        for variable in self.variables.all():
            context[variable.name] = variable.value

        request = HTTPRequest(
            url = render_with_context(self.url, context),
            method = self.method)

        session = Session()
        record = RequestRecord.objects.create(blueprint = self)

        for qs in self.name_value_related:


## ... source file abbreviated to get to models examples ...


                obj.save()

        if self.content_type == self.BODY_TYPES[0][0]:
            data = render_with_context(self.body, context)
        else:
            data = {}
            for param in self.body_parameters.all():
                param.add_to(data, context)

        request.data = data
        prepared_request = request.prepare()

        response = session.send(prepared_request, stream = True)

        RequestRecord.objects.filter(pk = record.pk).update(
            raw_request = parse_dump_result(dump._dump_request_data, prepared_request),
            raw_response = parse_dump_result(dump._dump_response_data, response),
            status = response.status_code,
            **RequestRecord.get_clone_args(self, context)
        )

        return RequestRecord.objects.get(pk = record.pk)


class RequestRecord(Request):
~~    raw_request = models.TextField()
~~    raw_response = models.TextField()
~~    status = models.PositiveIntegerField(null = True)
~~    blueprint = models.ForeignKey(
        'smithy.RequestBlueprint',
~~        on_delete = models.SET_NULL,
        null = True)

    @property
    def is_success(self):
        return self.status and self.status < 400

    @staticmethod
    def of_blueprint(blueprint):
        return RequestRecord.objects.filter(
            blueprint = blueprint)

    @classmethod
    def get_clone_args(cls, obj, context : dict):
        return dict([
            (
                render_with_context(fld.name, context),
                render_with_context(getattr(obj, fld.name), context)
            )
            for fld \
            in cls._meta.fields \
            if fld.name != obj._meta.pk \
            and fld in obj._meta.fields \
            and fld.name not in [
                   'request', 'id', 'created', 'updated'
               ]])


class Variable(NameValueModel):
~~    request = models.ForeignKey(
        'smithy.RequestBlueprint',
~~        on_delete = models.CASCADE,
        related_name = 'variables')


class BodyParameter(NameValueModel):
~~    request = models.ForeignKey(
        'smithy.RequestBlueprint',
~~        on_delete = models.CASCADE,
        related_name = 'body_parameters')

    def add_to(self, payload : dict, context: dict):
        if self.name and self.value:
            payload[
                render_with_context(self.name, context)
            ] = render_with_context(self.value, context)
        else:
            pass # TODO: warn


class Header(NameValueModel):
~~    request = models.ForeignKey(
        'smithy.Request',
~~        on_delete = models.CASCADE,
        related_name = 'headers')

    def add_to(self, request : HTTPRequest):
        if self.name and self.value:
            request.headers[self.name] = self.value
        else:
            pass # TODO: warn


class QueryParameter(NameValueModel):
~~    request = models.ForeignKey(
        'smithy.Request',
~~        on_delete = models.CASCADE,
        related_name = 'query_parameters')

    def add_to(self, request : HTTPRequest):
        existing_param_str = urlparse(request.url).query
        param_dict = parse_qs(existing_param_str)

        param_dict[self.name] = self.value

        base_url = request.url.rstrip(existing_param_str)
        param_str = urlencode(param_dict, doseq=True)
        request.url = base_url.rstrip("?") + "?" + param_str


class Cookie(NameValueModel):
~~    request = models.ForeignKey(
        'smithy.Request',
~~        on_delete = models.CASCADE,
        related_name = 'cookies')

    def add_to(self, request : HTTPRequest):
        request.cookies = request.cookies or RequestsCookieJar()
        request.cookies.set_cookie(
            create_cookie(self.name, self.value)
        )


@receiver(post_save, sender = RequestBlueprint)
def add_content_type(sender, instance : RequestBlueprint, created, **kwargs):
    if created and not instance.headers.filter(name__iexact = 'content-type').exists():
        instance.content_type and Header.objects.create(
            name = 'Content-Type',
            value = instance.content_type,
            request = instance.request_ptr
        )



## ... source file continues with no further models examples...

```


## Example 20 from django-sql-explorer
[django-sql-explorer](https://github.com/groveco/django-sql-explorer)
([PyPI page](https://pypi.org/project/django-sql-explorer/0.2/)),
also referred to as "SQL Explorer",
is a code library for the [Django](/django.html) Admin that allows
approved, authenticated users to view and execute direct database SQL
queries. The tool keeps track of executed queries so users can share them
with each other, as well as export results to downloadable formats.
django-sql-explorer is provided as open source under the
[MIT license](https://github.com/groveco/django-sql-explorer/blob/master/LICENSE).

[**django-sql-explorer / explorer / models.py**](https://github.com/groveco/django-sql-explorer/blob/master/explorer/./models.py)

```python
# models.py
from __future__ import unicode_literals

import logging
from time import time
import six

~~from django.db import models, DatabaseError
try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

from django.conf import settings

from explorer import app_settings
from explorer.utils import (
    passes_blacklist,
    swap_params,
    extract_params,
    shared_dict_update,
    get_s3_bucket,
    get_params_for_url,
    get_valid_connection
)

MSG_FAILED_BLACKLIST = "Query failed the SQL blacklist: %s"


logger = logging.getLogger(__name__)

@six.python_2_unicode_compatible
class Query(models.Model):
~~    title = models.CharField(max_length=255)
~~    sql = models.TextField()
~~    description = models.TextField(null=True, blank=True)
~~    created_by_user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
~~    created_at = models.DateTimeField(auto_now_add=True)
~~    last_run_date = models.DateTimeField(auto_now=True)
~~    snapshot = models.BooleanField(default=False, help_text="Include in snapshot task (if enabled)")
~~    connection = models.CharField(blank=True, null=True, max_length=128,
                                  help_text="Name of DB connection (as specified in settings) to use for this query. Will use EXPLORER_DEFAULT_CONNECTION if left blank")

    def __init__(self, *args, **kwargs):
        self.params = kwargs.get('params')
        kwargs.pop('params', None)
        super(Query, self).__init__(*args, **kwargs)

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Queries'

    def __str__(self):
        return six.text_type(self.title)

    def get_run_count(self):
        return self.querylog_set.count()

    def avg_duration(self):
        return self.querylog_set.aggregate(models.Avg('duration'))['duration__avg']

    def passes_blacklist(self):
        return passes_blacklist(self.final_sql())

    def final_sql(self):


## ... source file abbreviated to get to models examples ...


        return ql

    @property
    def shared(self):
        return self.id in set(sum(app_settings.EXPLORER_GET_USER_QUERY_VIEWS().values(), []))

    @property
    def snapshots(self):
        if app_settings.ENABLE_TASKS:
            b = get_s3_bucket()
            keys = b.list(prefix='query-%s/snap-' % self.id)
            keys_s = sorted(keys, key=lambda k: k.last_modified)
            return [SnapShot(k.generate_url(expires_in=0, query_auth=False),
                             k.last_modified) for k in keys_s]


class SnapShot(object):

    def __init__(self, url, last_modified):
        self.url = url
        self.last_modified = last_modified


class QueryLog(models.Model):

~~    sql = models.TextField(null=True, blank=True)
~~    query = models.ForeignKey(Query, null=True, blank=True, on_delete=models.SET_NULL)
~~    run_by_user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
~~    run_at = models.DateTimeField(auto_now_add=True)
~~    duration = models.FloatField(blank=True, null=True)  # milliseconds
~~    connection = models.CharField(blank=True, null=True, max_length=128)

    @property
    def is_playground(self):
        return self.query_id is None

    class Meta:
        ordering = ['-run_at']


class QueryResult(object):

    def __init__(self, sql, connection):

        self.sql = sql
        self.connection = connection

        cursor, duration = self.execute_query()

        self._description = cursor.description or []
        self._data = [list(r) for r in cursor.fetchall()]
        self.duration = duration

        cursor.close()



## ... source file continues with no further models examples...

```


## Example 21 from django-tables2
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

from django.core.exceptions import FieldDoesNotExist
~~from django.db import models
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
        self[:] = chain(head, columns, tail)


## ... source file abbreviated to get to models examples ...



        return instance

    def resolve(self, context, safe=True, quiet=False):
        if isinstance(context, dict) and self in context:
            return context[self]

        try:
            current = context
            for bit in self.bits:
                try:  # dictionary lookup
                    current = current[bit]
                except (TypeError, AttributeError, KeyError):
                    try:  # attribute lookup
                        current = getattr(current, bit)
                    except (TypeError, AttributeError):
                        try:  # list-index lookup
                            current = current[int(bit)]
                        except (
                            IndexError,  # list index out of range
                            ValueError,  # invalid literal for int()
                            KeyError,  # dict without `int(bit)` key
                            TypeError,  # unsubscriptable object
                        ):
                            current_context = (
~~                                type(current) if isinstance(current, models.Model) else current
                            )

                            raise ValueError(
                                self.LOOKUP_ERROR_FMT.format(
                                    key=bit, context=current_context, accessor=self
                                )
                            )
                if callable(current):
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


## ... source file continues with no further models examples...

```


## Example 22 from django-taggit
[django-taggit](https://github.com/jazzband/django-taggit/)
([PyPI page](https://pypi.org/project/django-taggit/)) provides a way
to create, store, manage and use tags in a [Django](/django.html) project.
The code for django-taggit is
[open source](https://github.com/jazzband/django-taggit/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-taggit / taggit / models.py**](https://github.com/jazzband/django-taggit/blob/master/taggit/./models.py)

```python
# models.py
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
~~from django.db import IntegrityError, models, router, transaction
from django.utils.text import slugify
from django.utils.translation import gettext, gettext_lazy as _

try:
    from unidecode import unidecode
except ImportError:

    def unidecode(tag):
        return tag


class TagBase(models.Model):
~~    name = models.CharField(verbose_name=_("name"), unique=True, max_length=100)
~~    slug = models.SlugField(verbose_name=_("slug"), unique=True, max_length=100)

    def __str__(self):
        return self.name

    def __gt__(self, other):
        return self.name.lower() > other.name.lower()

    def __lt__(self, other):
        return self.name.lower() < other.name.lower()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self._state.adding and not self.slug:
            self.slug = self.slugify(self.name)
            using = kwargs.get("using") or router.db_for_write(
                type(self), instance=self
            )
            kwargs["using"] = using
            try:
                with transaction.atomic(using=using):
                    res = super().save(*args, **kwargs)
                return res


## ... source file abbreviated to get to models examples ...


    @classmethod
    def tag_model(cls):
        field = cls._meta.get_field("tag")
        return field.remote_field.model

    @classmethod
    def tag_relname(cls):
        field = cls._meta.get_field("tag")
        return field.remote_field.related_name

    @classmethod
    def lookup_kwargs(cls, instance):
        return {"content_object": instance}

    @classmethod
    def tags_for(cls, model, instance=None, **extra_filters):
        kwargs = extra_filters or {}
        if instance is not None:
            kwargs.update({"%s__content_object" % cls.tag_relname(): instance})
            return cls.tag_model().objects.filter(**kwargs)
        kwargs.update({"%s__content_object__isnull" % cls.tag_relname(): False})
        return cls.tag_model().objects.filter(**kwargs).distinct()


class TaggedItemBase(ItemBase):
~~    tag = models.ForeignKey(
~~        Tag, related_name="%(app_label)s_%(class)s_items", on_delete=models.CASCADE
    )

    class Meta:
        abstract = True


class CommonGenericTaggedItemBase(ItemBase):
~~    content_type = models.ForeignKey(
        ContentType,
~~        on_delete=models.CASCADE,
        verbose_name=_("content type"),
        related_name="%(app_label)s_%(class)s_tagged_items",
    )
    content_object = GenericForeignKey()

    class Meta:
        abstract = True

    @classmethod
    def lookup_kwargs(cls, instance):
        return {
            "object_id": instance.pk,
            "content_type": ContentType.objects.get_for_model(instance),
        }

    @classmethod
    def tags_for(cls, model, instance=None, **extra_filters):
        tag_relname = cls.tag_relname()
        model = model._meta.concrete_model
        kwargs = {
            "%s__content_type__app_label" % tag_relname: model._meta.app_label,
            "%s__content_type__model" % tag_relname: model._meta.model_name,
        }
        if instance is not None:
            kwargs["%s__object_id" % tag_relname] = instance.pk
        if extra_filters:
            kwargs.update(extra_filters)
        return cls.tag_model().objects.filter(**kwargs).distinct()


class GenericTaggedItemBase(CommonGenericTaggedItemBase):
~~    object_id = models.IntegerField(verbose_name=_("object ID"), db_index=True)

    class Meta:
        abstract = True


class GenericUUIDTaggedItemBase(CommonGenericTaggedItemBase):
~~    object_id = models.UUIDField(verbose_name=_("object ID"), db_index=True)

    class Meta:
        abstract = True


class TaggedItem(GenericTaggedItemBase, TaggedItemBase):
    class Meta:
        verbose_name = _("tagged item")
        verbose_name_plural = _("tagged items")
        app_label = "taggit"
        index_together = [["content_type", "object_id"]]
        unique_together = [["content_type", "object_id", "tag"]]



## ... source file continues with no further models examples...

```


## Example 23 from django-user-visit
[django-user-visit](https://github.com/yunojuno/django-user-visit)
([PyPI package information](https://pypi.org/project/django-user-visit/))
is a [Django](/django.html) app and
[middleware](https://docs.djangoproject.com/en/stable/topics/http/middleware/)
for tracking daily user visits to your web application. The goal
is to record per user per day instead of for every request a user
sends to the application. The project is provided as open source
under the
[MIT license](https://github.com/yunojuno/django-user-visit/blob/master/LICENSE).

[**django-user-visit / user_visit / models.py**](https://github.com/yunojuno/django-user-visit/blob/master/user_visit/./models.py)

```python
# models.py
from __future__ import annotations

import datetime
import hashlib
import uuid
from typing import Any

import user_agents
from django.conf import settings
~~from django.db import models
from django.http import HttpRequest
from django.utils import timezone


def parse_remote_addr(request: HttpRequest) -> str:
    x_forwarded_for = request.headers.get("X-Forwarded-For", "")
    if x_forwarded_for:
        return x_forwarded_for.split(",")[0]
    return request.META.get("REMOTE_ADDR", "")


def parse_ua_string(request: HttpRequest) -> str:
    return request.headers.get("User-Agent", "")


class UserVisitManager(models.Manager):

    def build(self, request: HttpRequest, timestamp: datetime.datetime) -> UserVisit:
        uv = UserVisit(
            user=request.user,
            timestamp=timestamp,
            session_key=request.session.session_key,
            remote_addr=parse_remote_addr(request),
            ua_string=parse_ua_string(request),
        )
        uv.hash = uv.md5().hexdigest()
        return uv


class UserVisit(models.Model):

~~    user = models.ForeignKey(
~~        settings.AUTH_USER_MODEL, related_name="user_visits", on_delete=models.CASCADE
    )
~~    timestamp = models.DateTimeField(
        help_text="The time at which the first visit of the day was recorded",
        default=timezone.now,
    )
~~    session_key = models.CharField(help_text="Django session identifier", max_length=40)
~~    remote_addr = models.CharField(
        help_text=(
            "Client IP address (from X-Forwarded-For HTTP header, "
            "or REMOTE_ADDR request property)"
        ),
        max_length=100,
        blank=True,
    )
~~    ua_string = models.TextField(
        "User agent (raw)", help_text="Client User-Agent HTTP header", blank=True,
    )
~~    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
~~    hash = models.CharField(
        max_length=32,
        help_text="MD5 hash generated from request properties",
        unique=True,
    )
~~    created_at = models.DateTimeField(
        help_text="The time at which the database record was created (!=timestamp)",
        auto_now_add=True,
    )

    objects = UserVisitManager()

    class Meta:
        get_latest_by = "timestamp"

    def __str__(self) -> str:
        return f"{self.user} visited the site on {self.timestamp}"

    def __repr__(self) -> str:
        return f"<UserVisit id={self.id} user_id={self.user_id} date='{self.date}'>"

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.hash = self.md5().hexdigest()
        super().save(*args, **kwargs)

    @property
    def user_agent(self) -> user_agents.parsers.UserAgent:
        return user_agents.parsers.parse(self.ua_string)

    @property


## ... source file continues with no further models examples...

```


## Example 24 from django-webshell
[django-webshell](https://github.com/onrik/django-webshell) is an extension
for executing arbitrary code in the
[Django admin](https://docs.djangoproject.com/en/stable/ref/contrib/admin/),
similar to how you can run code by using the `django manage.py shell`
command from the terminal.

The django-webshell project is provided as open source under the
[MIT license](https://github.com/onrik/django-webshell/blob/master/LICENSE).

[**django-webshell / webshell / models.py**](https://github.com/onrik/django-webshell/blob/master/webshell/./models.py)

```python
# models.py
~~from django.db import models
from django.utils.translation import ugettext_lazy as _


class Script(models.Model):
~~    name = models.CharField(_('Name'), max_length=100)
~~    source = models.TextField(_('Source'))

    class Meta:
        verbose_name = _('Script')
        verbose_name_plural = _('Scripts')

    def __unicode__(self):
        return self.name



## ... source file continues with no further models examples...

```


## Example 25 from django-wiki
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

[**django-wiki / src/wiki / migrations / 0003_mptt_upgrade.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/migrations/0003_mptt_upgrade.py)

```python
# 0003_mptt_upgrade.py
from django.db import migrations
~~from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("wiki", "0002_urlpath_moved_to"),
    ]

    operations = [
        migrations.AlterField(
            model_name="urlpath",
            name="level",
~~            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name="urlpath",
            name="lft",
~~            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name="urlpath",
            name="rght",
~~            field=models.PositiveIntegerField(editable=False),
        ),
    ]



## ... source file continues with no further models examples...

```


## Example 26 from dmd-interpreter
[dmd-interpreter](https://github.com/mitchalexbailey/dmd-interpreter)
([running web app](http://www.dmd.nl/DOVE))
is a Python tool to aggregate clinically relevant information related
to variants in the DMD gene and display that [data](/data.html) to a user
with a [Django](/django.html) web application.

[**dmd-interpreter / interpreter / models.py**](https://github.com/mitchalexbailey/dmd-interpreter/blob/master/interpreter/./models.py)

```python
# models.py
~~from django.db import models

class Question(models.Model):
~~	question_text = models.CharField(max_length=200)
~~	pub_date = models.DateTimeField("Date Published")
	def __unicode__(self):
		return self.question_text

class Choice(models.Model):
~~	question = models.ForeignKey(Question)
~~	choice_text = models.CharField(max_length=200)
~~	votes = models.IntegerField(default=0)
	def __unicode__(self):
		return self.choice_text



## ... source file continues with no further models examples...

```


## Example 27 from drf-action-serializer
[drf-action-serializer](https://github.com/gregschmit/drf-action-serializer)
([PyPI page](https://pypi.org/project/drf-action-serializer/))
that makes it easier to configure specific serializers to use based on the
client's request action. For example, a list view should have one serializer
whereas the detail view would have a different serializer.

The project is open source under the
[MIT license](https://github.com/gregschmit/drf-action-serializer/blob/master/LICENSE).

[**drf-action-serializer / action_serializer / tests.py**](https://github.com/gregschmit/drf-action-serializer/blob/master/action_serializer/./tests.py)

```python
# tests.py

import os

~~from django.db import models
from django.test import TestCase

from .serializers import ModelActionSerializer


def dedent(blocktext):
    return "\n".join([line[12:] for line in blocktext.splitlines()[1:-1]])


class RegularFieldsModel(models.Model):

~~    auto_field = models.AutoField(primary_key=True)
~~    boolean_field = models.BooleanField(default=False)
~~    char_field = models.CharField(max_length=100)
~~    date_field = models.DateField()
~~    decimal_field = models.DecimalField(max_digits=3, decimal_places=1)
~~    email_field = models.EmailField(max_length=100)
~~    float_field = models.FloatField()
~~    integer_field = models.IntegerField()


class ModelActionSerializerTestCase(TestCase):

    def test_action_fields(self):

        class TestSerializer(ModelActionSerializer):
            class Meta:
                model = RegularFieldsModel
                fields = "char_field"
                action_fields = {"list": {"fields": ("auto_field", "char_field")}}

        expected = dedent(
        )
        context = {"view": type("ActionView", (object,), {"action": "list"})}
        self.assertEqual(repr(TestSerializer(context=context)), expected)

    def test_action_fields_different_action(self):

        class TestSerializer(ModelActionSerializer):
            class Meta:
                model = RegularFieldsModel
                fields = ("char_field",)
                action_fields = {"list": {"fields": ("auto_field", "char_field")}}


## ... source file abbreviated to get to models examples ...


        )
        context = {"view": type("ActionView", (object,), {"action": "create"})}
        self.assertEqual(repr(TestSerializer(context=context)), expected)

    def test_action_extra_kwargs(self):

        class TestSerializer(ModelActionSerializer):
            class Meta:
                model = RegularFieldsModel
                fields = "char_field"
                action_fields = {
                    "list": {
                        "fields": ("auto_field", "char_field"),
                        "extra_kwargs": {
                            "auto_field": {"required": False, "read_only": False}
                        },
                    }
                }

        expected = dedent(
        )
        context = {"view": type("ActionView", (object,), {"action": "list"})}
        self.assertEqual(repr(TestSerializer(context=context)), expected)

    def test_action_exclude(self):
~~        auto_field = models.AutoField(primary_key=True)
~~        boolean_field = models.BooleanField(default=False)
~~        char_field = models.CharField(max_length=100)
~~        date_field = models.DateField()
~~        decimal_field = models.DecimalField(max_digits=3, decimal_places=1)
~~        email_field = models.EmailField(max_length=100)
~~        float_field = models.FloatField()
~~        integer_field = models.IntegerField()

        class TestSerializer(ModelActionSerializer):
            class Meta:
                model = RegularFieldsModel
                fields = "char_field"
                action_fields = {
                    "list": {
                        "exclude": (
                            "boolean_field",
                            "date_field",
                            "float_field",
                            "integer_field",
                        )
                    }
                }

        expected = dedent(
        )
        context = {"view": type("ActionView", (object,), {"action": "list"})}
        self.assertEqual(repr(TestSerializer(context=context)), expected)



## ... source file continues with no further models examples...

```


## Example 28 from elasticsearch-django
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
~~from django.db import models
from django.db.models.expressions import RawSQL
from django.db.models.fields import CharField
from django.db.models.query import QuerySet
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


## ... source file abbreviated to get to models examples ...


            return

        get_client().update(
            index=index,
            doc_type=self.search_doc_type,
            body={"doc": doc},
            id=self.pk,  # type: ignore
        )

    def delete_search_document(self, *, index: str) -> None:
        cache.delete(self.search_document_cache_key)
        get_client().delete(
            index=index, doc_type=self.search_doc_type, id=self.pk  # type: ignore
        )


class SearchQuery(models.Model):

    QUERY_TYPE_SEARCH = "SEARCH"
    QUERY_TYPE_COUNT = "COUNT"
    QUERY_TYPE_CHOICES = (
        (QUERY_TYPE_SEARCH, "Search results"),
        (QUERY_TYPE_COUNT, "Count only"),
    )

~~    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="search_queries",
        blank=True,
        null=True,
        help_text="The user who made the search query (nullable).",
~~        on_delete=models.SET_NULL,
    )
~~    index = models.CharField(
        max_length=100,
        default="_all",
        help_text="The name of the ElasticSearch index(es) being queried.",
    )
~~    search_terms = models.CharField(
        max_length=400,
        default="",
        blank=True,
        help_text=(
            "Free text search terms used in the query, stored for easy reference."
        ),
    )
    query = JSONField(
        help_text="The raw ElasticSearch DSL query.", encoder=DjangoJSONEncoder
    )
    query_type = CharField(
        help_text="Does this query return results, or just the hit count?",
        choices=QUERY_TYPE_CHOICES,
        default=QUERY_TYPE_SEARCH,
        max_length=10,
    )
    hits = JSONField(
        help_text="The list of meta info for each of the query matches returned.",
        encoder=DjangoJSONEncoder,
    )
~~    total_hits = models.IntegerField(
        default=0,
        help_text="Total number of matches found for the query (!= the hits returned).",
    )
~~    reference = models.CharField(
        max_length=100,
        default="",
        blank=True,
        help_text="Custom reference used to identify and group related searches.",
    )
~~    executed_at = models.DateTimeField(
        help_text="When the search was executed - set via execute() method."
    )
~~    duration = models.FloatField(
        help_text="Time taken to execute the search itself, in seconds."
    )

    class Meta:
        app_label = "elasticsearch_django"
        verbose_name = "Search query"
        verbose_name_plural = "Search queries"

    def __str__(self) -> str:
        return f"Query (id={self.pk}) run against index '{self.index}'"

    def __repr__(self) -> str:
        return (
            f"<SearchQuery id={self.pk} user={self.user} "
            f"index='{self.index}' total_hits={self.total_hits} >"
        )

    def save(self, *args: Any, **kwargs: Any) -> SearchQuery:
        if self.search_terms is None:
            self.search_terms = ""
        super().save(**kwargs)
        return self

    def _extract_set(self, _property: str) -> List[Union[str, int]]:


## ... source file continues with no further models examples...

```


## Example 29 from gadget-board
[gadget-board](https://github.com/mik4el/gadget-board) is a
[Django](/django.html),
[Django REST Framework (DRF)](/django-rest-framework-drf.html) and
[Angular](/angular.html) web application that is open source under the
[Apache2 license](https://github.com/mik4el/gadget-board/blob/master/LICENSE).

[**gadget-board / web / authentication / models.py**](https://github.com/mik4el/gadget-board/blob/master/web/authentication/models.py)

```python
# models.py
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
~~from django.db import models
from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):
    def create_account(self, username, password, **kwargs):
        if not username:
            raise ValueError('Users must have a valid username')

        if not password:
            raise ValueError('Users must have a valid password.')

        if not kwargs.get('email'):
            raise ValueError('Users must have a valid email.')

        account = self.model(
            username=username, email=self.normalize_email(kwargs.get('email'))
        )

        account.is_active = True

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, username, password, **kwargs):
        account = self.create_account(username, password, **kwargs)

        account.is_superuser = True

        account.save()

        return account


class Account(AbstractBaseUser, PermissionsMixin):
~~    username = models.CharField(max_length=40, unique=True)
~~    email = models.EmailField()  # users can share email

~~    is_gadget = models.BooleanField(default=False)
~~    is_active = models.BooleanField(default=True)

~~    created_at = models.DateTimeField(auto_now_add=True)
~~    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_superuser



## ... source file continues with no further models examples...

```


## Example 30 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / core / models.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/core/models.py)

```python
# models.py
import json
import logging
from collections import defaultdict
from io import StringIO
from urllib.parse import urlparse

from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core import checks
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.core.handlers.base import BaseHandler
from django.core.handlers.wsgi import WSGIRequest
~~from django.db import models, transaction
from django.db.models import Case, Q, Value, When
from django.db.models.functions import Concat, Lower, Substr
from django.http import Http404
from django.http.request import split_domain_port
from django.template.response import TemplateResponse
from django.urls import NoReverseMatch, reverse
from django.utils import timezone
from django.utils.cache import patch_cache_control
from django.utils.functional import cached_property
from django.utils.text import capfirst, slugify
from django.utils.translation import gettext_lazy as _
from modelcluster.models import (
    ClusterableModel, get_all_child_m2m_relations, get_all_child_relations)
from treebeard.mp_tree import MP_Node

from wagtail.core.query import PageQuerySet, TreeQuerySet
from wagtail.core.signals import page_published, page_unpublished, post_page_move, pre_page_move
from wagtail.core.sites import get_site_for_hostname
from wagtail.core.url_routing import RouteResult
from wagtail.core.utils import WAGTAIL_APPEND_SLASH, camelcase_to_underscore, resolve_model_string
from wagtail.search import index


logger = logging.getLogger('wagtail.core')

PAGE_TEMPLATE_VAR = 'page'


class SiteManager(models.Manager):
    def get_queryset(self):
        return super(SiteManager, self).get_queryset().order_by(Lower("hostname"))

    def get_by_natural_key(self, hostname, port):
        return self.get(hostname=hostname, port=port)


class Site(models.Model):
~~    hostname = models.CharField(verbose_name=_('hostname'), max_length=255, db_index=True)
~~    port = models.IntegerField(
        verbose_name=_('port'),
        default=80,
        help_text=_(
            "Set this to something other than 80 if you need a specific port number to appear in URLs"
            " (e.g. development on port 8000). Does not affect request handling (so port forwarding still works)."
        )
    )
~~    site_name = models.CharField(
        verbose_name=_('site name'),
        max_length=255,
        blank=True,
        help_text=_("Human-readable name for the site.")
    )
~~    root_page = models.ForeignKey('Page', verbose_name=_('root page'), related_name='sites_rooted_here', on_delete=models.CASCADE)
~~    is_default_site = models.BooleanField(
        verbose_name=_('is default site'),
        default=False,
        help_text=_(
            "If true, this site will handle requests for all other hostnames that do not have a site entry of their own"
        )
    )

    objects = SiteManager()

    class Meta:
        unique_together = ('hostname', 'port')
        verbose_name = _('site')
        verbose_name_plural = _('sites')

    def natural_key(self):
        return (self.hostname, self.port)

    def __str__(self):
        default_suffix = " [{}]".format(_("default"))
        if self.site_name:
            return(
                self.site_name
                + (default_suffix if self.is_default_site else "")
            )


## ... source file abbreviated to get to models examples ...



        if 'template' not in dct:
            cls.template = "%s/%s.html" % (cls._meta.app_label, camelcase_to_underscore(name))

        if 'ajax_template' not in dct:
            cls.ajax_template = None

        cls._clean_subpage_models = None  # to be filled in on first call to cls.clean_subpage_models
        cls._clean_parent_page_models = None  # to be filled in on first call to cls.clean_parent_page_models

        if 'is_creatable' not in dct:
            cls.is_creatable = not cls._meta.abstract

        if not cls._meta.abstract:
            PAGE_MODEL_CLASSES.append(cls)


class AbstractPage(MP_Node):
    objects = PageManager()

    class Meta:
        abstract = True


class Page(AbstractPage, index.Indexed, ClusterableModel, metaclass=PageBase):
~~    title = models.CharField(
        verbose_name=_('title'),
        max_length=255,
        help_text=_("The page title as you'd like it to be seen by the public")
    )
~~    draft_title = models.CharField(
        max_length=255,
        editable=False
    )
~~    slug = models.SlugField(
        verbose_name=_('slug'),
        allow_unicode=True,
        max_length=255,
        help_text=_("The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/")
    )
~~    content_type = models.ForeignKey(
        ContentType,
        verbose_name=_('content type'),
        related_name='pages',
~~        on_delete=models.SET(get_default_page_content_type)
    )
~~    live = models.BooleanField(verbose_name=_('live'), default=True, editable=False)
~~    has_unpublished_changes = models.BooleanField(
        verbose_name=_('has unpublished changes'),
        default=False,
        editable=False
    )
~~    url_path = models.TextField(verbose_name=_('URL path'), blank=True, editable=False)
~~    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('owner'),
        null=True,
        blank=True,
        editable=True,
~~        on_delete=models.SET_NULL,
        related_name='owned_pages'
    )

~~    seo_title = models.CharField(
        verbose_name=_("page title"),
        max_length=255,
        blank=True,
        help_text=_("Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.")
    )

    show_in_menus_default = False
~~    show_in_menus = models.BooleanField(
        verbose_name=_('show in menus'),
        default=False,
        help_text=_("Whether a link to this page will appear in automatically generated menus")
    )
~~    search_description = models.TextField(verbose_name=_('search description'), blank=True)

~~    go_live_at = models.DateTimeField(
        verbose_name=_("go live date/time"),
        blank=True,
        null=True
    )
~~    expire_at = models.DateTimeField(
        verbose_name=_("expiry date/time"),
        blank=True,
        null=True
    )
~~    expired = models.BooleanField(verbose_name=_('expired'), default=False, editable=False)

~~    locked = models.BooleanField(verbose_name=_('locked'), default=False, editable=False)
~~    locked_at = models.DateTimeField(verbose_name=_('locked at'), null=True, editable=False)
~~    locked_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('locked by'),
        null=True,
        blank=True,
        editable=False,
~~        on_delete=models.SET_NULL,
        related_name='locked_pages'
    )

~~    first_published_at = models.DateTimeField(
        verbose_name=_('first published at'),
        blank=True,
        null=True,
        db_index=True
    )
~~    last_published_at = models.DateTimeField(
        verbose_name=_('last published at'),
        null=True,
        editable=False
    )
~~    latest_revision_created_at = models.DateTimeField(
        verbose_name=_('latest revision created at'),
        null=True,
        editable=False
    )
~~    live_revision = models.ForeignKey(
        'PageRevision',
        related_name='+',
        verbose_name='live revision',
~~        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        editable=False
    )

    search_fields = [
        index.SearchField('title', partial_match=True, boost=2),
        index.AutocompleteField('title'),
        index.FilterField('title'),
        index.FilterField('id'),
        index.FilterField('live'),
        index.FilterField('owner'),
        index.FilterField('content_type'),
        index.FilterField('path'),
        index.FilterField('depth'),
        index.FilterField('locked'),
        index.FilterField('show_in_menus'),
        index.FilterField('first_published_at'),
        index.FilterField('last_published_at'),
        index.FilterField('latest_revision_created_at'),


## ... source file abbreviated to get to models examples ...


                self.title,
                self.id,
                cls._meta.app_label,
                cls.__name__,
                self.url_path
            )

        return result

    def delete(self, *args, **kwargs):
        if type(self) is Page:
            return super().delete(*args, **kwargs)
        else:
            return Page.objects.get(id=self.id).delete(*args, **kwargs)

    @classmethod
    def check(cls, **kwargs):
        errors = super(Page, cls).check(**kwargs)


        field_exceptions = [field.name
                            for model in [cls] + list(cls._meta.get_parent_list())
                            for field in model._meta.parents.values() if field]

        for field in cls._meta.fields:
~~            if isinstance(field, models.ForeignKey) and field.name not in field_exceptions:
~~                if field.remote_field.on_delete == models.CASCADE:
                    errors.append(
                        checks.Warning(
                            "Field hasn't specified on_delete action",
~~                            hint="Set on_delete=models.SET_NULL and make sure the field is nullable or set on_delete=models.PROTECT. Wagtail does not allow simple database CASCADE because it will corrupt its tree storage.",
                            obj=field,
                            id='wagtailcore.W001',
                        )
                    )

        if not isinstance(cls.objects, PageManager):
            errors.append(
                checks.Error(
                    "Manager does not inherit from PageManager",
                    hint="Ensure that custom Page managers inherit from wagtail.core.models.PageManager",
                    obj=cls,
                    id='wagtailcore.E002',
                )
            )

        try:
            cls.clean_subpage_models()
        except (ValueError, LookupError) as e:
            errors.append(
                checks.Error(


## ... source file abbreviated to get to models examples ...


            instance=new_self,
            parent_page_before=parent_before,
            parent_page_after=parent_after,
            url_path_before=old_url_path,
            url_path_after=new_url_path,
        )

        logger.info("Page moved: \"%s\" id=%d path=%s", self.title, self.id, new_url_path)

    def copy(self, recursive=False, to=None, update_attrs=None, copy_revisions=True, keep_live=True, user=None, process_child_object=None, exclude_fields=None):
        specific_self = self.specific
        default_exclude_fields = ['id', 'path', 'depth', 'numchild', 'url_path', 'path', 'index_entries']
        exclude_fields = default_exclude_fields + specific_self.exclude_fields_in_copy + (exclude_fields or [])
        specific_dict = {}

        for field in specific_self._meta.get_fields():
            if field.name in exclude_fields:
                continue

            if field.auto_created:
                continue

            if field.many_to_many:
                continue

~~            if isinstance(field, models.OneToOneField) and field.remote_field.parent_link:
                continue

            specific_dict[field.name] = getattr(specific_self, field.name)

        for related_field in get_all_child_m2m_relations(specific_self):
            if related_field.name in exclude_fields:
                continue

            field = getattr(specific_self, related_field.name)
            if field and hasattr(field, 'all'):
                values = field.all()
                if values:
                    specific_dict[related_field.name] = values

        page_copy = self.specific_class(**specific_dict)

        if not keep_live:
            page_copy.live = False
            page_copy.has_unpublished_changes = True
            page_copy.live_revision = None
            page_copy.first_published_at = None
            page_copy.last_published_at = None

        if user:


## ... source file abbreviated to get to models examples ...



        obj.path = self.path
        obj.depth = self.depth
        obj.numchild = self.numchild

        obj.set_url_path(self.get_parent())

        obj.draft_title = self.draft_title
        obj.live = self.live
        obj.has_unpublished_changes = self.has_unpublished_changes
        obj.owner = self.owner
        obj.locked = self.locked
        obj.locked_by = self.locked_by
        obj.locked_at = self.locked_at
        obj.latest_revision_created_at = self.latest_revision_created_at
        obj.first_published_at = self.first_published_at

        return obj

    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')


class Orderable(models.Model):
~~    sort_order = models.IntegerField(null=True, blank=True, editable=False)
    sort_order_field = 'sort_order'

    class Meta:
        abstract = True
        ordering = ['sort_order']


class SubmittedRevisionsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(submitted_for_moderation=True)


class PageRevision(models.Model):
~~    page = models.ForeignKey('Page', verbose_name=_('page'), related_name='revisions', on_delete=models.CASCADE)
~~    submitted_for_moderation = models.BooleanField(
        verbose_name=_('submitted for moderation'),
        default=False,
        db_index=True
    )
~~    created_at = models.DateTimeField(db_index=True, verbose_name=_('created at'))
~~    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_('user'), null=True, blank=True,
~~        on_delete=models.SET_NULL
    )
~~    content_json = models.TextField(verbose_name=_('content JSON'))
~~    approved_go_live_at = models.DateTimeField(
        verbose_name=_('approved go live at'),
        null=True,
        blank=True,
        db_index=True
    )

~~    objects = models.Manager()
    submitted_revisions = SubmittedRevisionsManager()

    def save(self, *args, **kwargs):
        if self.created_at is None:
            self.created_at = timezone.now()

        super().save(*args, **kwargs)
        if self.submitted_for_moderation:
            self.page.revisions.exclude(id=self.id).update(submitted_for_moderation=False)

    def as_page_object(self):
        return self.page.specific.with_content_json(self.content_json)

    def approve_moderation(self):
        if self.submitted_for_moderation:
            logger.info("Page moderation approved: \"%s\" id=%d revision_id=%d", self.page.title, self.page.id, self.id)
            self.publish()

    def reject_moderation(self):
        if self.submitted_for_moderation:
            logger.info("Page moderation rejected: \"%s\" id=%d revision_id=%d", self.page.title, self.page.id, self.id)
            self.submitted_for_moderation = False
            self.save(update_fields=['submitted_for_moderation'])



## ... source file abbreviated to get to models examples ...



    def __str__(self):
        return '"' + str(self.page) + '" at ' + str(self.created_at)

    class Meta:
        verbose_name = _('page revision')
        verbose_name_plural = _('page revisions')


PAGE_PERMISSION_TYPES = [
    ('add', _("Add"), _("Add/edit pages you own")),
    ('edit', _("Edit"), _("Edit any page")),
    ('publish', _("Publish"), _("Publish any page")),
    ('bulk_delete', _("Bulk delete"), _("Delete pages with children")),
    ('lock', _("Lock"), _("Lock/unlock pages you've locked")),
    ('unlock', _("Unlock"), _("Unlock any page")),
]

PAGE_PERMISSION_TYPE_CHOICES = [
    (identifier, long_label)
    for identifier, short_label, long_label in PAGE_PERMISSION_TYPES
]


class GroupPagePermission(models.Model):
~~    group = models.ForeignKey(Group, verbose_name=_('group'), related_name='page_permissions', on_delete=models.CASCADE)
~~    page = models.ForeignKey('Page', verbose_name=_('page'), related_name='group_permissions', on_delete=models.CASCADE)
~~    permission_type = models.CharField(
        verbose_name=_('permission type'),
        max_length=20,
        choices=PAGE_PERMISSION_TYPE_CHOICES
    )

    class Meta:
        unique_together = ('group', 'page', 'permission_type')
        verbose_name = _('group page permission')
        verbose_name_plural = _('group page permissions')

    def __str__(self):
        return "Group %d ('%s') has permission '%s' on page %d ('%s')" % (
            self.group.id, self.group,
            self.permission_type,
            self.page.id, self.page
        )


class UserPagePermissionsProxy:

    def __init__(self, user):
        self.user = user

        if user.is_active and not user.is_superuser:


## ... source file abbreviated to get to models examples ...


        if not destination.specific_class.creatable_subpage_models():
            return False

        if 'add' not in destination_perms.permissions:
            return False

        return True

    def can_view_revisions(self):
        return not self.page_is_root


class BaseViewRestriction(models.Model):
    NONE = 'none'
    PASSWORD = 'password'
    GROUPS = 'groups'
    LOGIN = 'login'

    RESTRICTION_CHOICES = (
        (NONE, _("Public")),
        (LOGIN, _("Private, accessible to logged-in users")),
        (PASSWORD, _("Private, accessible with the following password")),
        (GROUPS, _("Private, accessible to users in specific groups")),
    )

~~    restriction_type = models.CharField(
        max_length=20, choices=RESTRICTION_CHOICES)
~~    password = models.CharField(verbose_name=_('password'), max_length=255, blank=True)
~~    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True)

    def accept_request(self, request):
        if self.restriction_type == BaseViewRestriction.PASSWORD:
            passed_restrictions = request.session.get(self.passed_view_restrictions_session_key, [])
            if self.id not in passed_restrictions:
                return False

        elif self.restriction_type == BaseViewRestriction.LOGIN:
            if not request.user.is_authenticated:
                return False

        elif self.restriction_type == BaseViewRestriction.GROUPS:
            if not request.user.is_superuser:
                current_user_groups = request.user.groups.all()

                if not any(group in current_user_groups for group in self.groups.all()):
                    return False

        return True

    def mark_as_passed(self, request):
        has_existing_session = (settings.SESSION_COOKIE_NAME in request.COOKIES)
        passed_restrictions = request.session.setdefault(self.passed_view_restrictions_session_key, [])
        if self.id not in passed_restrictions:
            passed_restrictions.append(self.id)
            request.session[self.passed_view_restrictions_session_key] = passed_restrictions
        if not has_existing_session:
            request.session.set_expiry(0)

    class Meta:
        abstract = True
        verbose_name = _('view restriction')
        verbose_name_plural = _('view restrictions')


class PageViewRestriction(BaseViewRestriction):
~~    page = models.ForeignKey(
~~        'Page', verbose_name=_('page'), related_name='view_restrictions', on_delete=models.CASCADE
    )

    passed_view_restrictions_session_key = 'passed_page_view_restrictions'

    class Meta:
        verbose_name = _('page view restriction')
        verbose_name_plural = _('page view restrictions')


class BaseCollectionManager(models.Manager):
    def get_queryset(self):
        return TreeQuerySet(self.model).order_by('path')


CollectionManager = BaseCollectionManager.from_queryset(TreeQuerySet)


class CollectionViewRestriction(BaseViewRestriction):
~~    collection = models.ForeignKey(
        'Collection',
        verbose_name=_('collection'),
        related_name='view_restrictions',
~~        on_delete=models.CASCADE
    )

    passed_view_restrictions_session_key = 'passed_collection_view_restrictions'

    class Meta:
        verbose_name = _('collection view restriction')
        verbose_name_plural = _('collection view restrictions')


class Collection(MP_Node):
~~    name = models.CharField(max_length=255, verbose_name=_('name'))

    objects = CollectionManager()

    def __str__(self):
        return self.name

    def get_ancestors(self, inclusive=False):
        return Collection.objects.ancestor_of(self, inclusive)

    def get_descendants(self, inclusive=False):
        return Collection.objects.descendant_of(self, inclusive)

    def get_siblings(self, inclusive=True):
        return Collection.objects.sibling_of(self, inclusive)

    def get_next_siblings(self, inclusive=False):
        return self.get_siblings(inclusive).filter(path__gte=self.path).order_by('path')

    def get_prev_siblings(self, inclusive=False):
        return self.get_siblings(inclusive).filter(path__lte=self.path).order_by('-path')

    def get_view_restrictions(self):
        return CollectionViewRestriction.objects.filter(collection__in=self.get_ancestors(inclusive=True))

    @staticmethod
    def order_for_display(queryset):
        return queryset.annotate(
            display_order=Case(
                When(depth=1, then=Value('')),
                default='name')
        ).order_by('display_order')

    class Meta:
        verbose_name = _('collection')
        verbose_name_plural = _('collections')


def get_root_collection_id():
    return Collection.get_first_root_node().id


class CollectionMember(models.Model):
~~    collection = models.ForeignKey(
        Collection,
        default=get_root_collection_id,
        verbose_name=_('collection'),
        related_name='+',
~~        on_delete=models.CASCADE
    )

    search_fields = [
        index.FilterField('collection'),
    ]

    class Meta:
        abstract = True


class GroupCollectionPermission(models.Model):
~~    group = models.ForeignKey(
        Group,
        verbose_name=_('group'),
        related_name='collection_permissions',
~~        on_delete=models.CASCADE
    )
~~    collection = models.ForeignKey(
        Collection,
        verbose_name=_('collection'),
        related_name='group_permissions',
~~        on_delete=models.CASCADE
    )
~~    permission = models.ForeignKey(
        Permission,
        verbose_name=_('permission'),
~~        on_delete=models.CASCADE
    )

    def __str__(self):
        return "Group %d ('%s') has permission '%s' on collection %d ('%s')" % (
            self.group.id, self.group,
            self.permission,
            self.collection.id, self.collection
        )

    class Meta:
        unique_together = ('group', 'collection', 'permission')
        verbose_name = _('group collection permission')
        verbose_name_plural = _('group collection permissions')

    ]

    is_creatable = False



## ... source file abbreviated to get to models examples ...


                    "Invalid subpage_types setting for %s" % cls,
                    hint=str(e),
                    id='wagtailcore.E002'
                )


## ... source file continues with no further models examples...

```

