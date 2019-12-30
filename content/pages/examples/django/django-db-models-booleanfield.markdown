title: django.db.models BooleanField Example Code
category: page
slug: django-db-models-booleanfield-examples
sortorder: 500012810
toc: False
sidebartitle: django.db.models BooleanField
meta: Python code examples for the BooleanField class used with the Django ORM to create a Boolean column in a database.


[BooleanField](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
is a Python class within [Django](/django.html) that maps Python code to
a [relational database](/databases.html) Boolean column through the 
[Django object-relational-mapper (ORM)](/django-orm.html).

[Django](/django.html)'s documentation explains more about 
[BooleanField](https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.TextField)
and all of the other ORM column fields.

Note that `BooleanField` is defined within the 
[django.db.models.fields](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
module but is typically referenced from
[django.db.models](https://github.com/django/django/tree/master/django/db/models)
rather than including the `fields` module reference.


## Example 1 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn/review / models.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/review/models.py)

```python
from django.conf import settings
from django.core.mail import send_mail
~~from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from conferences.models import Conference
from submissions.models import Submission
from users.models import User


# Create your models here.
class Reviewer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)


SCORE = (
    ('1', _('1 - Very Poor')),
    ('2', _('2 - Below Average')),
    ('3', _('3 - Average')),
    ('4', _('4 - Good')),
    ('5', _('5 - Excellent')),
)


class Review(models.Model):
    NUM_SCORES = 4

    # Score choices codes:
    POOR = 1
    BELOW_AVERAGE = 2
    AVERAGE = 3
    GOOD = 4
    EXCELLENT = 5

    SCORE_CHOICES = (
        ('', _('Choose your score')),
        (str(POOR), _('1 - Very Poor')),
        (str(BELOW_AVERAGE), _('2 - Below Average')),
        (str(AVERAGE), _('3 - Average')),
        (str(GOOD), _('4 - Good')),
        (str(EXCELLENT), _('5 - Excellent'))
    )

    reviewer = models.ForeignKey(
        Reviewer,
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    paper = models.ForeignKey(
        Submission,
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    technical_merit = models.CharField(
        choices=SCORE_CHOICES,
        max_length=1,
        blank=True,
    )

    clarity = models.CharField(
        choices=SCORE_CHOICES,
        max_length=1,
        blank=True,
    )

    relevance = models.CharField(
        choices=SCORE_CHOICES,
        max_length=1,
        blank=True,
    )

    originality = models.CharField(
        choices=SCORE_CHOICES,
        max_length=1,
        blank=True,
    )

    details = models.TextField()

~~    submitted = models.BooleanField(default=False)

    def __str__(self):
        name = self.reviewer.user.profile.get_full_name()
        return f'Review for submission #{self.paper.pk} by {name}'

    def check_details(self):
        return check_review_details(self.details, self.paper.stype)

    def score_fields(self):
        return {
            'technical_merit': self.technical_merit,
            'clarity': self.clarity,
            'originality': self.originality,
            'relevance': self.relevance,
        }


## ... source file continues here with no further BooleanField examples ...
```


## Example 2 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth/account / models.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/account/models.py)

```python
from __future__ import unicode_literals

import datetime

from django.core import signing
from django.db import models, transaction
from django.utils import timezone
from django.utils.crypto import get_random_string

from allauth.compat import python_2_unicode_compatible, ugettext_lazy as _

from .. import app_settings as allauth_app_settings
from . import app_settings, signals
from .adapter import get_adapter
from .managers import EmailAddressManager, EmailConfirmationManager
from .utils import user_email


@python_2_unicode_compatible
class EmailAddress(models.Model):

    user = models.ForeignKey(allauth_app_settings.USER_MODEL,
                             verbose_name=_('user'),
                             on_delete=models.CASCADE)
    email = models.EmailField(unique=app_settings.UNIQUE_EMAIL,
                              max_length=app_settings.EMAIL_MAX_LENGTH,
                              verbose_name=_('e-mail address'))
~~    verified = models.BooleanField(verbose_name=_('verified'), default=False)
~~    primary = models.BooleanField(verbose_name=_('primary'), default=False)

    objects = EmailAddressManager()

    class Meta:
        verbose_name = _("email address")
        verbose_name_plural = _("email addresses")
        if not app_settings.UNIQUE_EMAIL:
            unique_together = [("user", "email")]

    def __str__(self):
        return "%s (%s)" % (self.email, self.user)

## ... source file continues here with no further BooleanField examples ...
```


## Example 3 from django-axes
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

[**django-axes / axes/migrations / 0002_auto_20151217_2044.py**](https://github.com/jazzband/django-axes/blob/master/axes/migrations/0002_auto_20151217_2044.py)

```python
~~from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessattempt',
            name='ip_address',
            field=models.GenericIPAddressField(db_index=True, null=True, 
                                               verbose_name='IP Address'),
        ),
~~        migrations.AlterField(
~~            model_name='accessattempt',
~~            name='trusted',
~~            field=models.BooleanField(db_index=True, default=False),
~~        ),
        migrations.AlterField(
            model_name='accessattempt',
            name='user_agent',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='accessattempt',
            name='username',
            field=models.CharField(db_index=True, max_length=255, 
                                   null=True),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='ip_address',
            field=models.GenericIPAddressField(db_index=True, null=True, 
                                               verbose_name='IP Address'),
        ),
~~        migrations.AlterField(
~~            model_name='accesslog',
~~            name='trusted',
~~            field=models.BooleanField(db_index=True, default=False),
~~        ),
        migrations.AlterField(
            model_name='accesslog',
            name='user_agent',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='username',
            field=models.CharField(db_index=True, max_length=255, 
                                   null=True),
        ),
    ]
```


## Example 4 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer/migrations / 0003_thumbnailoption.py**](https://github.com/divio/django-filer/blob/develop/filer/migrations/0003_thumbnailoption.py)

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

~~from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThumbnailOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', 
                                        serialize=False, 
                                        auto_created=True, 
                                        primary_key=True)),
                ('name', models.CharField(max_length=100, 
                                          verbose_name='name')),
                ('width', models.IntegerField( \
                            help_text='width in pixel.', 
                            verbose_name='width')),
                ('height', models.IntegerField( \
                            help_text='height in pixel.', 
                            verbose_name='height')),
~~                ('crop', models.BooleanField( \
~~                            default=True, verbose_name='crop')),
~~                ('upscale', models.BooleanField( \
~~                            default=True, 
~~                            verbose_name='upscale')),
            ],
            options={
                'ordering': ('width', 'height'),
                'verbose_name': 'thumbnail option',
                'verbose_name_plural': 'thumbnail options',
            },
        ),
    ]
```


## Example 5 from django-push-notifications
[django-push-notifications](https://github.com/jazzband/django-push-notifications)
is a [Django](/django.html) app for storing and interacting with
push notification services such as 
[Google's Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/)
and 
[Apple Notifications](https://developer.apple.com/notifications/).
The django-push-notification project's source code is available
open source under the 
[MIT license](https://github.com/jazzband/django-push-notifications/blob/master/LICENSE).

[**django-push-notifications / push_notifications / models.py**](https://github.com/jazzband/django-push-notifications/blob/master/push_notifications/models.py)

```python
from __future__ import unicode_literals

~~from django.db import models
from django.utils.encoding import python_2_unicode_compatible
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


@python_2_unicode_compatible
class Device(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"), 
                            blank=True, null=True)
~~    active = models.BooleanField(
~~        verbose_name=_("Is active"), default=True,
~~        help_text=_("Inactive devices will not be sent notifications")
~~    )
    user = models.ForeignKey(
        SETTINGS["USER_MODEL"], blank=True, null=True, 
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(
        verbose_name=_("Creation date"), auto_now_add=True, null=True
    )
    application_id = models.CharField(
        max_length=64, verbose_name=_("Application ID"),
        help_text=_(
            "Opaque application identity, should be filled in for"
            " multiple key/certificate access"
        ),
        blank=True, null=True
    )

## ... source file continues here without further BooleanField examples ...
```


## Example 6 from AuditLog
[Auditlog](https://github.com/jjkester/django-auditlog)
([project documentation](https://django-auditlog.readthedocs.io/en/latest/))
is a [Django](/django.html) app that logs changes to Python objects,
similar to the Django admin's logs but with more details and
output formats. Auditlog's source code is provided as open source under the
[MIT license](https://github.com/jjkester/django-auditlog/blob/master/LICENSE).

[**AuditLog / src/auditlog_tests / models.py**](https://github.com/jjkester/django-auditlog/blob/master/src/auditlog_tests/models.py)

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
~~    boolean = models.BooleanField(default=False)
    integer = models.IntegerField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now=True)

    history = AuditlogHistoryField()


class AltPrimaryKeyModel(models.Model):
    """
    A model with a non-standard primary key.
    """

    key = models.CharField(max_length=100, primary_key=True)

    text = models.TextField(blank=True)
~~    boolean = models.BooleanField(default=False)
    integer = models.IntegerField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now=True)

    history = AuditlogHistoryField(pk_indexable=False)


class UUIDPrimaryKeyModel(models.Model):
    """
    A model with a UUID primary key.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    text = models.TextField(blank=True)
~~    boolean = models.BooleanField(default=False)
    integer = models.IntegerField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now=True)

    history = AuditlogHistoryField(pk_indexable=False)

## ... source file continues here without different BooleanField examples ...
```


## Example 7 from gadget-board
[gadget-board](https://github.com/mik4el/gadget-board) is a
[Django](/django.html),
[Django REST Framework (DRF)](/django-rest-framework-drf.html) and
[Angular](/angular.html) web application that is open source under the
[Apache2 license](https://github.com/mik4el/gadget-board/blob/master/LICENSE).

[**gadget-board / web/authentication / models.py**](https://github.com/mik4el/gadget-board/blob/master/web/authentication/models.py)

```python
from django.contrib.auth.models import (AbstractBaseUser, 
                                        PermissionsMixin)
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
            username=username, 
            email=self.normalize_email(kwargs.get('email'))
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
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField()  # users can share email

~~    is_gadget = models.BooleanField(default=False)
~~    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
```


## Example 8 from wagtail
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


class Site(models.Model):
    hostname = models.CharField(verbose_name=_('hostname'), 
                                max_length=255, db_index=True)
    port = models.IntegerField(
        verbose_name=_('port'),
        default=80,
        help_text=_(
            "Set this to something other than 80 if you need a "
            "specific port number to appear in URLs"
            " (e.g. development on port 8000). Does not affect "
            "request handling (so port forwarding still works)."
        )
    )
    site_name = models.CharField(
        verbose_name=_('site name'),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Human-readable name for the site.")
    )
    root_page = models.ForeignKey('Page', 
                                  verbose_name=_('root page'), 
                                  related_name='sites_rooted_here', 
                                  on_delete=models.CASCADE)
~~    is_default_site = models.BooleanField(
~~        verbose_name=_('is default site'),
~~        default=False,
~~        help_text=_(
~~            "If true, this site will handle requests for all "
~~            "other hostnames that do not have a site entry "
~~            "of their own"
~~        )
~~    )

    objects = SiteManager()

    class Meta:
        unique_together = ('hostname', 'port')
        verbose_name = _('site')
        verbose_name_plural = _('sites')


## ... source file continues with a few similar BooleanField examples ...
```

