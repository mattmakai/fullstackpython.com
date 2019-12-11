title: django.db.models ForeignKey Python Code Examples
category: page
slug: django-db-models-foreignkey-examples
sortorder: 50132
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
from django.db import migrations, models
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
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='cms.TreeNode')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='djangocms_nodes', to='sites.Site', verbose_name='site')),
            ],
            options={
                'ordering': ('path',),
                'default_permissions': [],
            },
        ),
        migrations.RunPython(create_page_nodes),
        migrations.AddField(
            model_name='page',
            name='node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cms_pages',
                                    to='cms.TreeNode'),
        ),
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


## Example 5 from django-extensions
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
# -*- coding: utf-8 -*-
#
# Autocomplete feature for admin panel
#
import six
import operator
from functools import update_wrapper
from six.moves import reduce
from typing import Tuple, Dict, Callable  # NOQA

from django.apps import apps
from django.http import HttpResponse, HttpResponseNotFound
from django.conf import settings
from django.db import models
from django.db.models.query import QuerySet
from django.utils.encoding import smart_str
from django.utils.translation import ugettext as _
from django.utils.text import get_text_list
from django.contrib import admin

from django_extensions.admin.widgets import ForeignKeySearchInput


class ForeignKeyAutocompleteAdminMixin(object):
    """
    Admin class for models using the autocomplete feature.

    There are two additional fields:
       - related_search_fields: defines fields of managed model that
         have to be represented by autocomplete input, together with
         a list of target model fields that are searched for
         input string, e.g.:

         related_search_fields = {
            'author': ('first_name', 'email'),
         }

       - related_string_functions: contains optional functions which
         take target model instance as only argument and return string
         representation. By default __unicode__() method of target
         object is used.

    And also an optional additional field to set the limit on the
    results returned by the autocomplete query. You can set this integer
    value in your settings file using FOREIGNKEY_AUTOCOMPLETE_LIMIT or
    you can set this per ForeignKeyAutocompleteAdmin basis. If any value
    is set the results will not be limited.
    """

    related_search_fields = {}  # type: Dict[str, Tuple[str]]
    related_string_functions = {}  # type: Dict[str, Callable]
    autocomplete_limit = getattr(settings, 'FOREIGNKEY_AUTOCOMPLETE_LIMIT', None)

    def get_urls(self):
        from django.conf.urls import url

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        return [
            url(r'foreignkey_autocomplete/$', wrap(self.foreignkey_autocomplete),
                name='%s_%s_autocomplete' % (self.model._meta.app_label, self.model._meta.model_name))
        ] + super(ForeignKeyAutocompleteAdminMixin, self).get_urls()

    def foreignkey_autocomplete(self, request):
        """
        Search in the fields of the given related model and returns the
        result as a simple string to be used by the jQuery Autocomplete plugin
        """
        query = request.GET.get('q', None)
        app_label = request.GET.get('app_label', None)
        model_name = request.GET.get('model_name', None)
        search_fields = request.GET.get('search_fields', None)
        object_pk = request.GET.get('object_pk', None)

        try:
            to_string_function = self.related_string_functions[model_name]
        except KeyError:
            if six.PY3:
                to_string_function = lambda x: x.__str__()
            else:
                to_string_function = lambda x: x.__unicode__()

        if search_fields and app_label and model_name and (query or object_pk):
            def construct_search(field_name):
                # use different lookup methods depending on the notation
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
                    other_qs = QuerySet(model)
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
        """
        Given a model class and current request return an optional Q object
        that should be applied as an additional filter for autocomplete query.
        If no additional filtering is needed, this method should return
        None.
        """
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
        """
        Override the default widget for Foreignkey fields if they are
        specified in the related_search_fields class attribute.
        """
        if isinstance(db_field, models.ForeignKey) and db_field.name in self.related_search_fields:
            help_text = self.get_help_text(db_field.name, db_field.remote_field.model._meta.object_name)
            if kwargs.get('help_text'):
                help_text = six.u('%s %s' % (kwargs['help_text'], help_text))
            kwargs['widget'] = ForeignKeySearchInput(db_field.remote_field, self.related_search_fields[db_field.name])
            kwargs['help_text'] = help_text
        return super(ForeignKeyAutocompleteAdminMixin, self).formfield_for_dbfield(db_field, **kwargs)


class ForeignKeyAutocompleteAdmin(ForeignKeyAutocompleteAdminMixin, admin.ModelAdmin):
    pass


class ForeignKeyAutocompleteTabularInline(ForeignKeyAutocompleteAdminMixin, admin.TabularInline):
    pass


class ForeignKeyAutocompleteStackedInline(ForeignKeyAutocompleteAdminMixin, admin.StackedInline):
    pass

```


## Example 6 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / migrations / 0002_auto_20150606_2003.py**](https://github.com/divio/django-filer/blob/develop/filer/migrations/0002_auto_20150606_2003.py)

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_filer.file_set+', editable=False, to='contenttypes.ContentType', null=True, on_delete=django.db.models.deletion.CASCADE),
            preserve_default=True,
        ),
    ]

```


## Example 7 from django-floppyforms
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

[**django-floppyforms / floppyforms / __future__ / models.py**](https://github.com/jazzband/django-floppyforms/blob/master/floppyforms/__future__/models.py)

```python
# flake8: noqa
import django
from django.db import models as db_models
from django.forms.models import (ModelForm as _ModelForm,
                                 ModelFormMetaclass as _ModelFormMetaclass,
                                 modelform_factory as _modelform_factory,
                                 modelformset_factory as _modelformset_factory,
                                 inlineformset_factory as _inlineformset_factory,
                                 model_to_dict, fields_for_model, BaseModelForm,
                                 BaseModelFormSet,
                                 BaseInlineFormSet)
if django.VERSION < (1, 9):
    from django.forms.models import save_instance
from django.utils import six

from floppyforms import fields
from floppyforms.forms import LayoutRenderer
from floppyforms.models import (ModelChoiceField, ModelMultipleChoiceField)
from floppyforms.widgets import Textarea


__all__ = (
    'ModelForm', 'BaseModelForm', 'model_to_dict', 'fields_for_model',
    'ModelChoiceField', 'ModelMultipleChoiceField',
    'BaseModelFormSet', 'modelformset_factory', 'BaseInlineFormSet',
    'inlineformset_factory',
)
if django.VERSION < (1, 9):
    __all__ += ('save_instance',)


if django.VERSION > (1, 7):
    from django.forms.models import ALL_FIELDS

    __all__ = __all__ + ('ALL_FIELDS',)


FORMFIELD_OVERRIDES = {
    db_models.BooleanField: {'form_class': fields.BooleanField},
    db_models.CharField: {'form_class': fields.CharField},
    db_models.CommaSeparatedIntegerField: {'form_class': fields.CharField},
    db_models.DateField: {'form_class': fields.DateField},
    db_models.DateTimeField: {'form_class': fields.DateTimeField},
    db_models.DecimalField: {'form_class': fields.DecimalField},
    db_models.EmailField: {'form_class': fields.EmailField},
    db_models.FilePathField: {'form_class': fields.FilePathField},
    db_models.FloatField: {'form_class': fields.FloatField},
    db_models.IntegerField: {'form_class': fields.IntegerField},
    db_models.BigIntegerField: {'form_class': fields.IntegerField},
    db_models.GenericIPAddressField: {'form_class': fields.GenericIPAddressField},
    db_models.NullBooleanField: {'form_class': fields.NullBooleanField},
    db_models.PositiveIntegerField: {'form_class': fields.IntegerField},
    db_models.PositiveSmallIntegerField: {'form_class': fields.IntegerField},
    db_models.SlugField: {'form_class': fields.SlugField},
    db_models.SmallIntegerField: {'form_class': fields.IntegerField},
    db_models.TextField: {'form_class': fields.CharField, 'widget': Textarea},
    db_models.TimeField: {'form_class': fields.TimeField},
    db_models.URLField: {'form_class': fields.URLField},
    # Binary field is never editable, so we don't need to convert it.

    db_models.FileField: {'form_class': fields.FileField},
    db_models.ImageField: {'form_class': fields.ImageField},

    db_models.ForeignKey: {'form_class': ModelChoiceField},
    db_models.ManyToManyField: {'form_class': ModelMultipleChoiceField},
    db_models.OneToOneField: {'form_class': ModelChoiceField},
}
if django.VERSION < (1, 9):
    FORMFIELD_OVERRIDES[db_models.IPAddressField] = {'form_class': fields.IPAddressField}

for value in FORMFIELD_OVERRIDES.values():
    value['choices_form_class'] = fields.TypedChoiceField


def formfield_callback(db_field, **kwargs):
    defaults = FORMFIELD_OVERRIDES.get(db_field.__class__, {}).copy()
    defaults.update(kwargs)
    return db_field.formfield(**defaults)


class ModelFormMetaclass(_ModelFormMetaclass):
    def __new__(mcs, name, bases, attrs):
        if not attrs.get('formfield_callback'):
            attrs['formfield_callback'] = formfield_callback
        return super(ModelFormMetaclass, mcs).__new__(mcs, name, bases, attrs)


class ModelForm(six.with_metaclass(ModelFormMetaclass, LayoutRenderer, _ModelForm)):
    pass


def modelform_factory(model, form=ModelForm, fields=None, exclude=None,
                      formfield_callback=formfield_callback, *args, **kwargs):
    return _modelform_factory(model, form, fields, exclude, formfield_callback,
                              *args, **kwargs)


def modelformset_factory(model, form=ModelForm,
                         formfield_callback=formfield_callback,
                         *args, **kwargs):
    return _modelformset_factory(model, form, formfield_callback,
                                 *args, **kwargs)


def inlineformset_factory(parent_model, model, form=ModelForm,
                          formset=BaseInlineFormSet, fk_name=None,
                          fields=None, exclude=None, extra=3, can_order=False,
                          can_delete=True, max_num=None,
                          formfield_callback=formfield_callback,
                          *args, **kwargs):
    return _inlineformset_factory(parent_model, model, form, formset, fk_name,
                                  fields, exclude, extra, can_order,
                                  can_delete, max_num, formfield_callback,
                                  *args, **kwargs)

```


## Example 8 from django-guardian
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
from django.db import models, migrations
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
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', on_delete=models.CASCADE)),
                ('group', models.ForeignKey(to='auth.Group', on_delete=models.CASCADE)),
                ('permission', models.ForeignKey(to='auth.Permission', on_delete=models.CASCADE)),
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
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', on_delete=models.CASCADE)),
                ('permission', models.ForeignKey(to='auth.Permission', on_delete=models.CASCADE)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
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


## Example 9 from django-jet
[django-jet](https://github.com/geex-arts/django-jet)
([project documentation](https://jet.readthedocs.io/en/latest/),
[PyPI project page](https://pypi.org/project/django-jet/) and
[more information](http://jet.geex-arts.com/))
is a fancy [Django](/django.html) Admin panel replacement.

The django-jet project is open source under the
[GNU Affero General Public License v3.0](https://github.com/geex-arts/django-jet/blob/dev/LICENSE).

[**django-jet / jet / tests / models.py**](https://github.com/geex-arts/django-jet/blob/dev/jet/tests/models.py)

```python
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class TestModel(models.Model):
    field1 = models.CharField(max_length=255)
    field2 = models.IntegerField()

    def __str__(self):
        return '%s%d' % (self.field1, self.field2)


@python_2_unicode_compatible
class RelatedToTestModel(models.Model):
    field = models.ForeignKey(TestModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.field


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


## Example 10 from django-oauth-toolkit
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

[**django-oauth-toolkit / oauth2_provider / migrations / 0001_initial.py**](https://github.com/jazzband/django-oauth-toolkit/blob/master/oauth2_provider/migrations/0001_initial.py)

```python
from django.conf import settings
import django.db.models.deletion
from django.db import migrations, models

import oauth2_provider.generators
import oauth2_provider.validators
from oauth2_provider.settings import oauth2_settings


class Migration(migrations.Migration):
    """
    The following migrations are squashed here:
    - 0001_initial.py
    - 0002_08_updates.py
    - 0003_auto_20160316_1503.py
    - 0004_auto_20160525_1623.py
    - 0005_auto_20170514_1141.py
    - 0006_auto_20171214_2232.py
    """
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL)
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(serialize=False, primary_key=True)),
                ('client_id', models.CharField(default=oauth2_provider.generators.generate_client_id, unique=True, max_length=100, db_index=True)),
                ('redirect_uris', models.TextField(help_text='Allowed URIs list, space separated', blank=True)),
                ('client_type', models.CharField(max_length=32, choices=[('confidential', 'Confidential'), ('public', 'Public')])),
                ('authorization_grant_type', models.CharField(max_length=32, choices=[('authorization-code', 'Authorization code'), ('implicit', 'Implicit'), ('password', 'Resource owner password-based'), ('client-credentials', 'Client credentials')])),
                ('client_secret', models.CharField(default=oauth2_provider.generators.generate_client_secret, max_length=255, db_index=True, blank=True)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('user', models.ForeignKey(related_name="oauth2_provider_application", blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)),
                ('skip_authorization', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
                'swappable': 'OAUTH2_PROVIDER_APPLICATION_MODEL',
            },
        ),
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.BigAutoField(serialize=False, primary_key=True)),
                ('token', models.CharField(unique=True, max_length=255)),
                ('expires', models.DateTimeField()),
                ('scope', models.TextField(blank=True)),
                ('application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=oauth2_settings.APPLICATION_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='oauth2_provider_accesstoken', to=settings.AUTH_USER_MODEL)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                # Circular reference. Can't add it here.
                #('source_refresh_token', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=oauth2_settings.REFRESH_TOKEN_MODEL, related_name="refreshed_access_token")),
            ],
            options={
                'abstract': False,
                'swappable': 'OAUTH2_PROVIDER_ACCESS_TOKEN_MODEL',
            },
        ),
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.BigAutoField(serialize=False, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=255)),
                ('expires', models.DateTimeField()),
                ('redirect_uri', models.CharField(max_length=255)),
                ('scope', models.TextField(blank=True)),
                ('application', models.ForeignKey(to=oauth2_settings.APPLICATION_MODEL, on_delete=models.CASCADE)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oauth2_provider_grant', to=settings.AUTH_USER_MODEL)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
                'swappable': 'OAUTH2_PROVIDER_GRANT_MODEL',
            },
        ),
        migrations.CreateModel(
            name='RefreshToken',
            fields=[
                ('id', models.BigAutoField(serialize=False, primary_key=True)),
                ('token', models.CharField(max_length=255)),
                ('access_token', models.OneToOneField(blank=True, null=True, related_name="refresh_token", to=oauth2_settings.ACCESS_TOKEN_MODEL, on_delete=models.SET_NULL)),
                ('application', models.ForeignKey(to=oauth2_settings.APPLICATION_MODEL, on_delete=models.CASCADE)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oauth2_provider_refreshtoken', to=settings.AUTH_USER_MODEL)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('revoked', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
                'swappable': 'OAUTH2_PROVIDER_REFRESH_TOKEN_MODEL',
                'unique_together': set([("token", "revoked")]),
            },
        ),
        migrations.AddField(
            model_name='AccessToken',
            name='source_refresh_token',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=oauth2_settings.REFRESH_TOKEN_MODEL, related_name="refreshed_access_token"),
        ),
    ]

```


## Example 11 from django-push-notifications
[django-push-notifications](https://github.com/jazzband/django-push-notifications)
is a [Django](/django.html) app for storing and interacting with
push notification services such as
[Google's Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/)
and
[Apple Notifications](https://developer.apple.com/notifications/).
The django-push-notification project's source code is available
open source under the
[MIT license](https://github.com/jazzband/django-push-notifications/blob/master/LICENSE).

[**django-push-notifications / push_notifications / migrations / 0001_initial.py**](https://github.com/jazzband/django-push-notifications/blob/master/push_notifications/migrations/0001_initial.py)

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models

import push_notifications.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='APNSDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name', blank=True)),
                ('active', models.BooleanField(default=True, help_text='Inactive devices will not be sent notifications', verbose_name='Is active')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date', null=True)),
                ('device_id', models.UUIDField(help_text='UDID / UIDevice.identifierForVendor()', max_length=32, null=True, verbose_name='Device ID', blank=True, db_index=True)),
                ('registration_id', models.CharField(unique=True, max_length=64, verbose_name='Registration ID')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'APNS device',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GCMDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name', blank=True)),
                ('active', models.BooleanField(default=True, help_text='Inactive devices will not be sent notifications', verbose_name='Is active')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date', null=True)),
                ('device_id', push_notifications.fields.HexIntegerField(help_text='ANDROID_ID / TelephonyManager.getDeviceId() (always as hex)', null=True, verbose_name='Device ID', blank=True, db_index=True)),
                ('registration_id', models.TextField(verbose_name='Registration ID')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'GCM device',
            },
            bases=(models.Model,),
        ),
    ]

```


## Example 12 from django-smithy
[django-smithy](https://github.com/jamiecounsell/django-smithy) is
a [Django](/django.html) code library that allows users to send
HTTP requests from the Django admin user interface. The code for
the project is open source under the
[MIT license](https://github.com/jamiecounsell/django-smithy/blob/master/LICENSE).

[**django-smithy / smithy / migrations / 0002_auto_20190317_1052_squashed_0008_auto_20190317_1213.py**](https://github.com/jamiecounsell/django-smithy/blob/master/smithy/migrations/0002_auto_20190317_1052_squashed_0008_auto_20190317_1213.py)

```python
# Generated by Django 2.1.5 on 2019-03-17 17:14

from django.db import migrations, models
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
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='body_parameters', to='smithy.RequestBlueprint')),
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


## Example 13 from django-sql-explorer
[django-sql-explorer](https://github.com/groveco/django-sql-explorer)
([PyPI page](https://pypi.org/project/django-sql-explorer/0.2/)),
also referred to as "SQL Explorer",
is a code library for the [Django](/django.html) Admin that allows
approved, authenticated users to view and execute direct database SQL
queries. The tool keeps track of executed queries so users can share them
with each other, as well as export results to downloadable formats.
django-sql-explorer is provided as open source under the
[MIT license](https://github.com/groveco/django-sql-explorer/blob/master/LICENSE).

[**django-sql-explorer / explorer / migrations / 0001_initial.py**](https://github.com/groveco/django-sql-explorer/blob/master/explorer/migrations/0001_initial.py)

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('sql', models.TextField()),
                ('description', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_run_date', models.DateTimeField(auto_now=True)),
                ('created_by_user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name_plural': 'Queries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QueryLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sql', models.TextField()),
                ('is_playground', models.BooleanField(default=False)),
                ('run_at', models.DateTimeField(auto_now_add=True)),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='explorer.Query', null=True)),
                ('run_by_user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ['-run_at'],
            },
            bases=(models.Model,),
        ),
    ]

```


## Example 14 from django-taggit
[django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)
([source code](https://github.com/jazzband/django-debug-toolbar) and
[PyPI page](https://pypi.org/project/django-taggit/)) provides a way
to create, store, manage and use tags in a [Django](/django.html) project.
The code for django-taggit is
[open source](https://github.com/jazzband/django-taggit/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-taggit / taggit / migrations / 0001_initial.py**](https://github.com/jazzband/django-taggit/blob/master/taggit/migrations/0001_initial.py)

```python
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("contenttypes", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        help_text="",
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="", unique=True, max_length=100, verbose_name="Name"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="", unique=True, max_length=100, verbose_name="Slug"
                    ),
                ),
            ],
            options={"verbose_name": "Tag", "verbose_name_plural": "Tags"},
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="TaggedItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        help_text="",
                        verbose_name="ID",
                    ),
                ),
                (
                    "object_id",
                    models.IntegerField(
                        help_text="", verbose_name="Object id", db_index=True
                    ),
                ),
                (
                    "content_type",
                    models.ForeignKey(
                        related_name="taggit_taggeditem_tagged_items",
                        verbose_name="Content type",
                        to="contenttypes.ContentType",
                        help_text="",
                        on_delete=models.CASCADE,
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        related_name="taggit_taggeditem_items",
                        to="taggit.Tag",
                        help_text="",
                        on_delete=models.CASCADE,
                    ),
                ),
            ],
            options={
                "verbose_name": "Tagged Item",
                "verbose_name_plural": "Tagged Items",
            },
            bases=(models.Model,),
        ),
    ]

```


## Example 15 from django-wiki
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

[**django-wiki / src/wiki / migrations / 0001_initial.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/migrations/0001_initial.py)

```python
import django.db.models.deletion
import mptt.fields
from django.conf import settings
from django.db import migrations, models
from django.db.models.fields import GenericIPAddressField as IPAddressField
from wiki.conf.settings import GROUP_MODEL


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='modified', auto_now=True, help_text='Article properties last modified')),
                ('group_read', models.BooleanField(default=True, verbose_name='group read access')),
                ('group_write', models.BooleanField(default=True, verbose_name='group write access')),
                ('other_read', models.BooleanField(default=True, verbose_name='others read access')),
                ('other_write', models.BooleanField(default=True, verbose_name='others write access')),
            ],
            options={
                'permissions': (('moderate', 'Can edit all articles and lock/unlock/restore'), ('assign', 'Can change ownership of any article'), ('grant', 'Can assign permissions to other users')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticleForObject',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(verbose_name='object ID')),
                ('is_mptt', models.BooleanField(default=False, editable=False)),
                ('article', models.ForeignKey(to='wiki.Article', on_delete=models.CASCADE)),
                ('content_type', models.ForeignKey(related_name='content_type_set_for_articleforobject', verbose_name='content type', to='contenttypes.ContentType', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name_plural': 'Articles for object',
                'verbose_name': 'Article for object',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticlePlugin',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticleRevision',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('revision_number', models.IntegerField(verbose_name='revision number', editable=False)),
                ('user_message', models.TextField(blank=True)),
                ('automatic_log', models.TextField(blank=True, editable=False)),
                ('ip_address', IPAddressField(null=True, verbose_name='IP address', blank=True, editable=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False, verbose_name='deleted')),
                ('locked', models.BooleanField(default=False, verbose_name='locked')),
                ('content', models.TextField(blank=True, verbose_name='article contents')),
                ('title', models.CharField(max_length=512, verbose_name='article title', help_text='Each revision contains a title field that must be filled out, even if the title has not changed')),
                ('article', models.ForeignKey(to='wiki.Article', verbose_name='article', on_delete=models.CASCADE)),
                ('previous_revision', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wiki.ArticleRevision')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'get_latest_by': 'revision_number',
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReusablePlugin',
            fields=[
                ('articleplugin_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='wiki.ArticlePlugin', serialize=False, auto_created=True, on_delete=models.CASCADE)),
                ('articles', models.ManyToManyField(related_name='shared_plugins_set', to='wiki.Article')),
            ],
            options={
            },
            bases=('wiki.articleplugin',),
        ),
        migrations.CreateModel(
            name='RevisionPlugin',
            fields=[
                ('articleplugin_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='wiki.ArticlePlugin', serialize=False, auto_created=True, on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=('wiki.articleplugin',),
        ),
        migrations.CreateModel(
            name='RevisionPluginRevision',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('revision_number', models.IntegerField(verbose_name='revision number', editable=False)),
                ('user_message', models.TextField(blank=True)),
                ('automatic_log', models.TextField(blank=True, editable=False)),
                ('ip_address', IPAddressField(null=True, verbose_name='IP address', blank=True, editable=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False, verbose_name='deleted')),
                ('locked', models.BooleanField(default=False, verbose_name='locked')),
                ('plugin', models.ForeignKey(related_name='revision_set', to='wiki.RevisionPlugin', on_delete=models.CASCADE)),
                ('previous_revision', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wiki.RevisionPluginRevision')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'get_latest_by': 'revision_number',
                'ordering': ('-created',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SimplePlugin',
            fields=[
                ('articleplugin_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='wiki.ArticlePlugin', serialize=False, auto_created=True, on_delete=models.CASCADE)),
                ('article_revision', models.ForeignKey(to='wiki.ArticleRevision', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=('wiki.articleplugin',),
        ),
        migrations.CreateModel(
            name='URLPath',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('slug', models.SlugField(null=True, blank=True, verbose_name='slug')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('article', models.ForeignKey(help_text='This field is automatically updated, but you need to populate it when creating a new URL path.', on_delete=django.db.models.deletion.CASCADE, to='wiki.Article', verbose_name='article')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, help_text='Position of URL path in the tree.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='wiki.URLPath')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'verbose_name_plural': 'URL paths',
                'verbose_name': 'URL path',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='urlpath',
            unique_together=set([('site', 'parent', 'slug')]),
        ),
        migrations.AddField(
            model_name='revisionplugin',
            name='current_revision',
            field=models.OneToOneField(related_name='plugin_set', null=True, help_text='The revision being displayed for this plugin. If you need to do a roll-back, simply change the value of this field.', blank=True, to='wiki.RevisionPluginRevision', verbose_name='current revision', on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='articlerevision',
            unique_together=set([('article', 'revision_number')]),
        ),
        migrations.AddField(
            model_name='articleplugin',
            name='article',
            field=models.ForeignKey(to='wiki.Article', verbose_name='article', on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='articleforobject',
            unique_together=set([('content_type', 'object_id')]),
        ),
        migrations.AddField(
            model_name='article',
            name='current_revision',
            field=models.OneToOneField(related_name='current_set', null=True, help_text='The revision being displayed for this article. If you need to do a roll-back, simply change the value of this field.', blank=True, to='wiki.ArticleRevision', verbose_name='current revision', on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, help_text='Like in a UNIX file system, permissions can be given to a user according to group membership. Groups are handled through the Django auth system.', blank=True, to=GROUP_MODEL, verbose_name='group'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='owner',
            field=models.ForeignKey(related_name='owned_articles', null=True, on_delete=django.db.models.deletion.SET_NULL, help_text='The owner of the article, usually the creator. The owner always has both read and write access.', blank=True, to=settings.AUTH_USER_MODEL, verbose_name='owner'),
            preserve_default=True,
        ),
    ]

```


## Example 16 from dmd-interpreter
[dmd-interpreter](https://github.com/mitchalexbailey/dmd-interpreter)
([running web app](http://www.dmd.nl/DOVE))
is a Python tool to aggregate clinically relevant information related
to variants in the DMD gene and display that [data](/data.html) to a user
with a [Django](/django.html) web application.

[**dmd-interpreter / interpreter / migrations / 0001_initial.py**](https://github.com/mitchalexbailey/dmd-interpreter/blob/master/interpreter/migrations/0001_initial.py)

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'Date Published')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='interpreter.Question'),
        ),
    ]

```


## Example 17 from gadget-board
[gadget-board](https://github.com/mik4el/gadget-board) is a
[Django](/django.html),
[Django REST Framework (DRF)](/django-rest-framework-drf.html) and
[Angular](/angular.html) web application that is open source under the
[Apache2 license](https://github.com/mik4el/gadget-board/blob/master/LICENSE).

[**gadget-board / web / gadgets / models.py**](https://github.com/mik4el/gadget-board/blob/master/web/gadgets/models.py)

```python
from django.db import models
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
    gadget = models.ForeignKey(Gadget, db_index=True, on_delete=models.DO_NOTHING)  # Add index on filtered fields
    data = JSONField()
    added_by = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(null=True, blank=True, db_index=True)  # Add index on filtered fields
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {} {}'.format(self.gadget, self.timestamp, self.added_by)

```

