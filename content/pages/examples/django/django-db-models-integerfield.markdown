title: django.db.models IntegerField Example Code
category: page
slug: django-db-models-integerfield-examples
sortorder: 500012870
toc: False
sidebartitle: django.db.models IntegerField
meta: Python code examples for the IntegerField class used in the Django ORM, found within the django.db.models module of the Django project. 


[IntegerField](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
is a [Django ORM](/django-orm.html) mapping from your Python code to an
integer-type column in your [relational database](/databases.html).

The [Django](/django.html) project has wonderful documentation for
[IntegerField](https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.IntegerField)
as well as all of the other column fields.

Note that `IntegerField` is defined within the 
[django.db.models.fields](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
module but is typically referenced from
[django.db.models](https://github.com/django/django/tree/master/django/db/models)
rather than including the `fields` module reference.


## Example 1 from AuditLog
[Auditlog](https://github.com/jjkester/django-auditlog)
([project documentation](https://django-auditlog.readthedocs.io/en/latest/))
is a [Django](/django.html) app that logs changes to Python objects,
similar to the Django admin's logs but with more details and
output formats. Auditlog's source code is provided as open source under the
[MIT license](https://github.com/jjkester/django-auditlog/blob/master/LICENSE).

[**AuditLog / src / auditlog_tests / models.py**](https://github.com/jjkester/django-auditlog/blob/master/src/auditlog_tests/models.py)

```python
import uuid

from django.contrib.postgres.fields import ArrayField
~~from django.db import models
from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog

from multiselectfield import MultiSelectField


@auditlog.register()
class SimpleModel(models.Model):
    """
    A simple model with no special things going on.
    """

    text = models.TextField(blank=True)
    boolean = models.BooleanField(default=False)
~~    integer = models.IntegerField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now=True)

    history = AuditlogHistoryField()


class AltPrimaryKeyModel(models.Model):
    """
    A model with a non-standard primary key.
    """

    key = models.CharField(max_length=100, primary_key=True)

    text = models.TextField(blank=True)
    boolean = models.BooleanField(default=False)
~~    integer = models.IntegerField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now=True)

    history = AuditlogHistoryField(pk_indexable=False)


class UUIDPrimaryKeyModel(models.Model):
    """
    A model with a UUID primary key.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    text = models.TextField(blank=True)
    boolean = models.BooleanField(default=False)
~~    integer = models.IntegerField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now=True)

    history = AuditlogHistoryField(pk_indexable=False)


class ProxyModel(SimpleModel):
    """
    A model that is a proxy for another model.
    """

    class Meta:
        proxy = True


class RelatedModel(models.Model):
    """
    A model with a foreign key.
    """

    related = models.ForeignKey(to='self', on_delete=models.CASCADE)

    history = AuditlogHistoryField()


class ManyRelatedModel(models.Model):
    """
    A model with a many to many relation.
    """

    related = models.ManyToManyField('self')

    history = AuditlogHistoryField()


@auditlog.register(include_fields=['label'])
class SimpleIncludeModel(models.Model):
    """
    A simple model used for register's include_fields kwarg
    """

    label = models.CharField(max_length=100)
    text = models.TextField(blank=True)

    history = AuditlogHistoryField()


class SimpleExcludeModel(models.Model):
    """
    A simple model used for register's exclude_fields kwarg
    """

    label = models.CharField(max_length=100)
    text = models.TextField(blank=True)

    history = AuditlogHistoryField()


class SimpleMappingModel(models.Model):
    """
    A simple model used for register's mapping_fields kwarg
    """

    sku = models.CharField(max_length=100)
    vtxt = models.CharField(verbose_name='Version', max_length=100)
    not_mapped = models.CharField(max_length=100)

    history = AuditlogHistoryField()


class AdditionalDataIncludedModel(models.Model):
    """
    A model where get_additional_data is defined which allows for logging extra
    information about the model in JSON
    """

    label = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    related = models.ForeignKey(to=SimpleModel, on_delete=models.CASCADE)

    history = AuditlogHistoryField()

    def get_additional_data(self):
        """
        Returns JSON that captures a snapshot of additional details of the
        model instance. This method, if defined, is accessed by auditlog
        manager and added to each logentry instance on creation.
        """
        object_details = {
            'related_model_id': self.related.id,
            'related_model_text': self.related.text
        }
        return object_details


class DateTimeFieldModel(models.Model):
    """
    A model with a DateTimeField, used to test DateTimeField
    changes are detected properly.
    """
    label = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    date = models.DateField()
    time = models.TimeField()
    naive_dt = models.DateTimeField(null=True, blank=True)

    history = AuditlogHistoryField()


class ChoicesFieldModel(models.Model):
    """
    A model with a CharField restricted to a set of choices.
    This model is used to test the changes_display_dict method.
    """
    RED = 'r'
    YELLOW = 'y'
    GREEN = 'g'

    STATUS_CHOICES = (
        (RED, 'Red'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
    )

    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    multiselect = MultiSelectField(max_length=3, choices=STATUS_CHOICES, max_choices=3)
    multiplechoice = models.CharField(max_length=3, choices=STATUS_CHOICES)

    history = AuditlogHistoryField()


class CharfieldTextfieldModel(models.Model):
    """
    A model with a max length CharField and a Textfield.
    This model is used to test the changes_display_dict
    method's ability to truncate long text.
    """

    longchar = models.CharField(max_length=255)
    longtextfield = models.TextField()

    history = AuditlogHistoryField()


class PostgresArrayFieldModel(models.Model):
    """
    Test auditlog with Postgres's ArrayField
    """
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
```


## Example 2 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / users / models.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/users/models.py)

```python
import io
from datetime import date

import pyavagen
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.files.base import ContentFile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
~~from django.db import models
from django_countries.fields import CountryField

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name=_('Email address'), 
                              unique=True)

    date_joined = models.DateTimeField(
        verbose_name=_('Date joined'),
        auto_now_add=True
    )

    is_active = models.BooleanField(
        verbose_name=_('Active'),
        default=True
    )

    has_finished_registration = models.BooleanField(
        default=False
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    # TODO: uncomment this later:
    # def get_absolute_url(self):
    #     return reverse('user-detail', kwargs={'pk': self.id})

    def __str__(self):
        return f'{self.pk}: {self.email}'


def get_avatar_full_path(instance, filename):
    ext = filename.split('.')[-1]
    path = f'{settings.MEDIA_PUBLIC_ROOT}/avatars'
    name = f'{instance.pk}_{instance.avatar_version:04d}'
    return f'{path}/{name}.{ext}'


class Profile(models.Model):
    ROLES = (
        (None, _('Select your role')),
        ('Student', _('Student')),
        ('PhD Student', _('PhD Student')),
        ('Assistant', _('Assistant')),
        ('Researcher', _('Researcher')),
        ('Assistant Professor', _('Assistant Professor')),
        ('Associate Professor', _('Associate Professor')),
        ('Professor', _('Professor')),
        ('Head of Department', _('Head of Department')),
        ('Head of Faculty', _('Head of Faculty')),
        ('Head of Laboratory', _('Head of Laboratory')),
        ('Vice Rector', _('Vice Rector')),
        ('Rector', _('Rector')),
        ('Software Developer', _('Software Developer')),
        ('Engineer', _('Engineer')),
        ('Technician', _('Technician')),
        ('Economist', _('Economist')),
        ('Lawyer', _('Lawyer')),
        ('Instructor', _('Instructor')),
        ('Consultant', _('Consultant')),
        ('Manager', _('Manager')),
        ('Administrator', _('Administrator')),
        ('Analyst', _('Analyst')),
        ('Journalist', _('Journalist')),
        ('Writer', _('Writer')),
        ('Editor', _('Editor')),
        ('Librarian', _('Librarian')),
        ('Vice Director', _('Vice Director')),
        ('Chief Executive Officer', _('Chief Executive Officer')),
        ('Retired', _('Retired')),
        ('Other', _('Other')),
    )

    DEGREE = (
        (None, _('Select your degree')),
        ('Undergraduate', _('Undergraduate')),
        ('Bachelor', _('Bachelor')),
        ('Master', _('Master')),
        ('PhD', _('PhD')),
        ('Candidate of Sciences', _('Candidate of Sciences')),
        ('Doctor of Sciences', _('Doctor of Sciences')),
    )

    LANGUAGES = (
        ('ENG', _('English')),
        ('RUS', _('Russian')),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(
        max_length=100, verbose_name=_("First Name in English")
    )
    last_name = models.CharField(
        max_length=100, verbose_name=_("Last Name in English")
    )
    first_name_rus = models.CharField(
        max_length=100, default="", verbose_name=_("First Name in Russian",),
        blank=True,
    )
    middle_name_rus = models.CharField(
        max_length=100, default="", verbose_name=_("Middle Name in Russian"),
        blank = True,
    )
    last_name_rus = models.CharField(
        max_length=100, default="", verbose_name=_("Last Name in Russian"),
        blank=True,
    )
    country = CountryField(null=True, verbose_name=_("Country"))
    city = models.CharField(max_length=100, verbose_name=_("City in English"))
    birthday = models.DateField(verbose_name=_("Birthday"), null=True)
    affiliation = models.CharField(
        max_length=100, verbose_name=_("Name of your organization in English"),
    )
    role = models.CharField(
        choices=ROLES, max_length=30, null=True,
        verbose_name=_('Primary role in organization')
    )
    degree = models.CharField(
        choices=DEGREE, max_length=30, null=True,
        verbose_name=_('Degree')
    )
    ieee_member = models.BooleanField(
        verbose_name=_('I am an IEEE Member'), default=False
    )

    preferred_language = models.CharField(
        choices=LANGUAGES, max_length=3, default='ENG'
    )

    avatar = models.ImageField(upload_to=get_avatar_full_path, blank=True)
~~    avatar_version = models.IntegerField(default=0, blank=True, editable=False)

# ... source file continues here without further IntegerField examples ...
```


## Example 3 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail/core / models.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/core/models.py)

```python
import json
import logging
from collections import defaultdict
from io import StringIO
from urllib.parse import urlparse
from warnings import warn

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
from django.db.models.functions import Concat, Substr
from django.http import Http404
from django.template.response import TemplateResponse
from django.urls import reverse
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.text import capfirst, slugify
from django.utils.translation import ugettext_lazy as _
from modelcluster.models import (
    ClusterableModel, get_all_child_m2m_relations, 
    get_all_child_relations)
from treebeard.mp_tree import MP_Node

from wagtail.core.query import PageQuerySet, TreeQuerySet
from wagtail.core.signals import page_published, page_unpublished
from wagtail.core.sites import get_site_for_hostname
from wagtail.core.url_routing import RouteResult
from wagtail.core.utils import (WAGTAIL_APPEND_SLASH, 
                                camelcase_to_underscore, 
                                resolve_model_string)
from wagtail.search import index
from wagtail.utils.deprecation import RemovedInWagtail29Warning


logger = logging.getLogger('wagtail.core')

PAGE_TEMPLATE_VAR = 'page'


class SiteManager(models.Manager):
    def get_by_natural_key(self, hostname, port):
        return self.get(hostname=hostname, port=port)

# ... some of source file skipped here for brevity ...

~~    url_path = models.TextField(verbose_name=_('URL path'), blank=True, editable=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('owner'),
        null=True,
        blank=True,
        editable=True,
        on_delete=models.SET_NULL,
        related_name='owned_pages'
    )

## ... source file continues without further TextField examples ...
```
