title: django.db.models ForeignKey Python Code Examples
category: page
slug: django-db-models-foreignkey-examples
sortorder: 500012840
toc: False
sidebartitle: django.db.models ForeignKey
meta: Python code examples for the ForeignKey class used in the Django ORM, found within the django.db.models module of the Django project. 


[ForeignKey](https://github.com/django/django/blob/master/django/db/models/fields/related.py)
is a [Django ORM](/django-orm.html) field-to-column mapping for
creating and working with relationships between tables in 
[relational databases](/databases.html).

`ForeignKey` is defined within the 
[django.db.models.related](https://github.com/django/django/blob/master/django/db/models/fields/related.py)
module but is typically referenced from
[django.db.models](https://github.com/django/django/tree/master/django/db/models)
rather than using the `related` module reference.


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


## ... source file abbreviated to get to the ForeignKey examples ...


class RelatedModel(models.Model):
    """
    A model with a foreign key.
    """

~~    related = models.ForeignKey(to='self', on_delete=models.CASCADE)

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
~~    related = models.ForeignKey(to=SimpleModel, on_delete=models.CASCADE)

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


# ... source file continues with no further ForeignKey examples ...

```

## Example 2 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / review / models.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/review/models.py)

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
~~    user = models.ForeignKey(User, on_delete=models.CASCADE)
~~    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)


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

~~    reviewer = models.ForeignKey(
~~        Reviewer,
~~        on_delete=models.CASCADE,
~~        related_name='reviews',
~~    )

~~    paper = models.ForeignKey(
~~        Submission,
~~        on_delete=models.CASCADE,
~~        related_name='reviews',
~~    )

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

    submitted = models.BooleanField(default=False)

~~    def __str__(self):
~~        name = self.reviewer.user.profile.get_full_name()
~~        return f'Review for submission #{self.paper.pk} by {name}'

    def check_details(self):
        return check_review_details(self.details, self.paper.stype)

    def score_fields(self):
        return {
            'technical_merit': self.technical_merit,
            'clarity': self.clarity,
            'originality': self.originality,
            'relevance': self.relevance,
        }

    def missing_score_fields(self):
        return tuple(k for k, v in self.score_fields().items() if v == '')

    def all_scores_filled(self):
        return self.num_scores_missing() == 0

    def num_scores_missing(self):
        return len(self.missing_score_fields())

    def warnings(self):
        num_missing = self.num_scores_missing()
        warnings = []
        if num_missing == Review.NUM_SCORES and not self.details:
            warnings.append('Please, start the review')
        else:
            filled_details = self.check_details()
            filled_scores = num_missing == 0

            if not filled_scores:
                warnings.append(
                    f'{num_missing} of {Review.NUM_SCORES} scores not filled'
                )
            if not filled_details:
                warnings.append('Review details are incomplete')
            if filled_scores and filled_details and not self.submitted:
                warnings.append('Review is not submitted yet')
        return warnings

    def average_score(self):
        if self.all_scores_filled():
            fields = self.score_fields()
            return sum(int(x) for x in fields.values()) / len(fields)
        return 0

## ... source file continues with no further ForeignKey examples ...

```


## Example 3 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / socialaccount / models.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/socialaccount/models.py)

```python
from __future__ import absolute_import

from django.contrib.auth import authenticate
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import PermissionDenied
~~from django.db import models
from django.utils.crypto import get_random_string

import allauth.app_settings
from allauth.account.models import EmailAddress
from allauth.account.utils import get_next_redirect_url, setup_user_email
from allauth.compat import (
    force_str,
    python_2_unicode_compatible,
    ugettext_lazy as _,
)
from allauth.utils import get_user_model

from ..utils import get_request_param
from . import app_settings, providers
from .adapter import get_adapter
from .fields import JSONField


## ... source file abbreviated to get to ForeignKey examples ...


@python_2_unicode_compatible
class SocialAccount(models.Model):
~~    user = models.ForeignKey(allauth.app_settings.USER_MODEL,
~~                             on_delete=models.CASCADE)
    provider = models.CharField(verbose_name=_('provider'),
                                max_length=30,
                                choices=providers.registry.as_choices())
    # Just in case you're wondering if an OpenID identity URL is going
    # to fit in a 'uid':
    #
    # Ideally, URLField(max_length=1024, unique=True) would be used
    # for identity.  However, MySQL has a max_length limitation of 191
    # for URLField (in case of utf8mb4). How about
    # models.TextField(unique=True) then?  Well, that won't work
    # either for MySQL due to another bug[1]. So the only way out
    # would be to drop the unique constraint, or switch to shorter
    # identity URLs. Opted for the latter, as [2] suggests that
    # identity URLs are supposed to be short anyway, at least for the
    # old spec.
    #
    # [1] http://code.djangoproject.com/ticket/2495.
    # [2] http://openid.net/specs/openid-authentication-1_1.html#limits

    uid = models.CharField(verbose_name=_('uid'),
                           max_length=app_settings.UID_MAX_LENGTH)
    last_login = models.DateTimeField(verbose_name=_('last login'),
                                      auto_now=True)
    date_joined = models.DateTimeField(verbose_name=_('date joined'),
                                       auto_now_add=True)
    extra_data = JSONField(verbose_name=_('extra data'), default=dict)

    class Meta:
        unique_together = ('provider', 'uid')
        verbose_name = _('social account')
        verbose_name_plural = _('social accounts')

    def authenticate(self):
        return authenticate(account=self)

~~    def __str__(self):
~~        return force_str(self.user)

    def get_profile_url(self):
        return self.get_provider_account().get_profile_url()

    def get_avatar_url(self):
        return self.get_provider_account().get_avatar_url()

    def get_provider(self):
        return providers.registry.by_id(self.provider)

    def get_provider_account(self):
        return self.get_provider().wrap_account(self)


@python_2_unicode_compatible
class SocialToken(models.Model):
~~    app = models.ForeignKey(SocialApp, on_delete=models.CASCADE)
~~    account = models.ForeignKey(SocialAccount, on_delete=models.CASCADE)
    token = models.TextField(
        verbose_name=_('token'),
        help_text=_(
            '"oauth_token" (OAuth1) or access token (OAuth2)'))
    token_secret = models.TextField(
        blank=True,
        verbose_name=_('token secret'),
        help_text=_(
            '"oauth_token_secret" (OAuth1) or refresh token (OAuth2)'))
    expires_at = models.DateTimeField(blank=True, null=True,
                                      verbose_name=_('expires at'))

    class Meta:
        unique_together = ('app', 'account')
        verbose_name = _('social application token')
        verbose_name_plural = _('social application tokens')

    def __str__(self):
        return self.token


## ... source file continues with no further ForeignKey examples ...

```


## Example 4 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / migrations / 0018_create_pagenode.py**](https://github.com/divio/django-cms/blob/develop/cms/migrations/0018_create_pagenode.py)

```python
# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-03 19:50
from __future__ import unicode_literals

import django
import django.contrib.auth.models
~~from django.db import migrations, models
import django.db.models.deletion

from . import IrreversibleMigration


def get_descendants(root):
    """
    Returns the a generator of primary keys which represent
    descendants of the given page ID (root_id)
    """
    # Note this is done because get_descendants() can't be trusted
    # as the tree can be corrupt.

    for child in root.children.order_by('path').iterator():
        yield child

        for child in get_descendants(child):
            yield child


def create_page_nodes(apps, schema_editor):
    Page = apps.get_model('cms', 'Page')
    TreeNode = apps.get_model('cms', 'TreeNode')
    db_alias = schema_editor.connection.alias
    root_draft_pages = Page.objects.using(db_alias).filter(
        publisher_is_draft=True,
        parent__isnull=True,
    )

    create_node = TreeNode.objects.using(db_alias).create

    nodes_by_page = {}

    for root in root_draft_pages:
        node = create_node(
            site_id=root.site_id,
            path=root.path,
            depth=root.depth,
            numchild=root.numchild,
            parent=None,
        )

        nodes_by_page[root.pk] = node

        for descendant in get_descendants(root):
            node = create_node(
                site_id=descendant.site_id,
                path=descendant.path,
                depth=descendant.depth,
                numchild=descendant.numchild,
                parent=nodes_by_page[descendant.parent_id],
            )
            nodes_by_page[descendant.pk] = node


class Migration(IrreversibleMigration):

    dependencies = [
        ('sites', '0001_initial'),
        ('cms', '0017_pagetype'),
    ]
    replaces = [('cms', '0018_pagenode')]

    operations = [
        migrations.CreateModel(
            name='TreeNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
~~                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='cms.TreeNode')),
~~                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='djangocms_nodes', to='sites.Site', verbose_name='site')),
            ],
            options={
                'ordering': ('path',),
                'default_permissions': [],
            },
        ),
        migrations.RunPython(create_page_nodes),
~~        migrations.AddField(
~~            model_name='page',
~~            name='node',
~~            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cms_pages',
~~                                    to='cms.TreeNode'),
~~        ),
        migrations.AddField(
            model_name='page',
            name='migration_0018_control',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('node', 'publisher_is_draft')]),
        ),
        migrations.AlterModelManagers(
            name='pageusergroup',
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
    ]

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

[**django-guardian / guardian / migrations / 0001_initial.py**](https://github.com/django-guardian/django-guardian/blob/devel/guardian/migrations/0001_initial.py)

```python
# 0001_initial.py
~~from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupObjectPermission',
            fields=[
                ('id', models.AutoField(primary_key=True,
                                        serialize=False, auto_created=True, verbose_name='ID')),
                ('object_pk', models.CharField(
                    max_length=255, verbose_name='object ID')),
~~                ('content_type', models.ForeignKey(to='contenttypes.ContentType', on_delete=models.CASCADE)),
~~                ('group', models.ForeignKey(to='auth.Group', on_delete=models.CASCADE)),
~~                ('permission', models.ForeignKey(to='auth.Permission', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserObjectPermission',
            fields=[
                ('id', models.AutoField(primary_key=True,
                                        serialize=False, auto_created=True, verbose_name='ID')),
                ('object_pk', models.CharField(
                    max_length=255, verbose_name='object ID')),
~~                ('content_type', models.ForeignKey(to='contenttypes.ContentType', on_delete=models.CASCADE)),
~~                ('permission', models.ForeignKey(to='auth.Permission', on_delete=models.CASCADE)),
~~                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='userobjectpermission',
            unique_together=set([('user', 'permission', 'object_pk')]),
        ),
        migrations.AlterUniqueTogether(
            name='groupobjectpermission',
            unique_together=set([('group', 'permission', 'object_pk')]),
        ),
    ]

```


## Example 6 from django-jet
[django-jet](https://github.com/geex-arts/django-jet)
([project documentation](https://jet.readthedocs.io/en/latest/),
[PyPI project page](https://pypi.org/project/django-jet/) and
[more information](http://jet.geex-arts.com/))
is a fancy [Django](/django.html) Admin panel replacement.

The django-jet project is open source under the
[GNU Affero General Public License v3.0](https://github.com/geex-arts/django-jet/blob/dev/LICENSE).

[**django-jet / jet / tests / models.py**](https://github.com/geex-arts/django-jet/blob/dev/jet/tests/models.py)

```python
# models.py
~~from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class TestModel(models.Model):
    field1 = models.CharField(max_length=255)
    field2 = models.IntegerField()

    def __str__(self):
        return '%s%d' % (self.field1, self.field2)


@python_2_unicode_compatible
class RelatedToTestModel(models.Model):
~~    field = models.ForeignKey(TestModel, on_delete=models.CASCADE)

~~    def __str__(self):
~~        return self.field


@python_2_unicode_compatible
class SearchableTestModel(models.Model):
    field1 = models.CharField(max_length=255)
    field2 = models.IntegerField()

    def __str__(self):
        return '%s%d' % (self.field1, self.field2)

    @staticmethod
    def autocomplete_search_fields():
        return 'field1'

```


## Example 7 from django-smithy
[django-smithy](https://github.com/jamiecounsell/django-smithy) is
a [Django](/django.html) code library that allows users to send
HTTP requests from the Django admin user interface. The code for
the project is open source under the
[MIT license](https://github.com/jamiecounsell/django-smithy/blob/master/LICENSE).

[**django-smithy / smithy / migrations / 0002_auto_20190317_1052_squashed_0008_auto_20190317_1213.py**](https://github.com/jamiecounsell/django-smithy/blob/master/smithy/migrations/0002_auto_20190317_1052_squashed_0008_auto_20190317_1213.py)

```python
# Generated by Django 2.1.5 on 2019-03-17 17:14

~~from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    replaces = [('smithy', '0002_auto_20190317_1052'), ('smithy', '0003_auto_20190317_1103'), ('smithy', '0004_auto_20190317_1104'), ('smithy', '0005_auto_20190317_1107'), ('smithy', '0006_request_body_type'), ('smithy', '0007_auto_20190317_1159'), ('smithy', '0008_auto_20190317_1213')]

    dependencies = [
        ('smithy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=200)),
                ('value', models.TextField()),
~~                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='body_parameters', to='smithy.RequestBlueprint')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='requestrecord',
            name='raw_request',
            field=models.TextField(default=''),
        ),
        migrations.RemoveField(
            model_name='requestrecord',
            name='response',
        ),
        migrations.AddField(
            model_name='requestrecord',
            name='status',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='requestrecord',
            name='raw_response',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='content_type',
            field=models.CharField(blank=True, choices=[('', 'Other'), ('application/x-www-form-urlencoded', 'x-www-form-urlencoded'), ('application/json', 'JSON'), ('text/plain', 'Text'), ('application/javascript', 'JavaScript'), ('application/xml', 'XML (application/xml)'), ('text/xml', 'XML (text/xml)'), ('text/html', 'HTML')], default='', max_length=100, null=True),
        ),
    ]

```


## Example 8 from gadget-board
[gadget-board](https://github.com/mik4el/gadget-board) is a
[Django](/django.html),
[Django REST Framework (DRF)](/django-rest-framework-drf.html) and
[Angular](/angular.html) web application that is open source under the
[Apache2 license](https://github.com/mik4el/gadget-board/blob/master/LICENSE).

[**gadget-board / web / gadgets / models.py**](https://github.com/mik4el/gadget-board/blob/master/web/gadgets/models.py)

```python
# models.py
~~from django.db import models
from django.contrib.postgres.fields import JSONField
from django.template.defaultfilters import slugify
from authentication.models import Account


class Gadget(models.Model):
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField()
    users_can_upload = models.ManyToManyField(Account)
    image_name = models.CharField(max_length=140, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def image_url(self):
        if self.image_name != "":
            return "backend/static/media/{}".format(self.image_name)
        else:
            return "backend/static/dashboard_icon_big.png"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(Gadget, self).save(*args, **kwargs)


class GadgetData(models.Model):
~~    gadget = models.ForeignKey(Gadget, db_index=True, on_delete=models.DO_NOTHING)  # Add index on filtered fields
    data = JSONField()
~~    added_by = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(null=True, blank=True, db_index=True)  # Add index on filtered fields
    created_at = models.DateTimeField(auto_now_add=True)

~~    def __str__(self):
~~        return '{} {} {}'.format(self.gadget, self.timestamp, self.added_by)

```

