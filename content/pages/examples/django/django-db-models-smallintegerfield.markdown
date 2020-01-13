title: django.db.models SmallIntegerField Code Examples
category: page
slug: django-db-models-smallintegerfield-examples
sortorder: 500012903
toc: False
sidebartitle: django.db.models SmallIntegerField
meta: Python code examples for the SmallIntegerField class used in the Django ORM, found within django.db.models.


[SmallIntegerField](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
([documentation](https://docs.djangoproject.com/en/stable/ref/models/fields/#django.db.models.SmallIntegerField))
is a [Django ORM](/django-orm.html) mapping from your Python code to an
integer-type column in your [relational database](/databases.html)
that is restricted to integer values only between -32768 and 32767.

Note that `SmallIntegerField` is defined within the 
[django.db.models.fields](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
module but is typically referenced from
[django.db.models](https://github.com/django/django/tree/master/django/db/models)
rather than including the `fields` module reference.


## Example 1 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / embeds / models.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/embeds/models.py)

```python
# models.py
~~from django.db import models
from django.utils.translation import ugettext_lazy as _

EMBED_TYPES = (
    ('video', 'Video'),
    ('photo', 'Photo'),
    ('link', 'Link'),
    ('rich', 'Rich'),
)


class Embed(models.Model):
    """
    When embed code is fetched from a provider (eg, youtube) we cache that code
    in the database so we don't need to ask for it again.

    This model is used for caching the embed html code. It also stores some
    metadata which gets displayed in the editor.

    If an instance of this model is deleted, it will be automatically refetched
    next time the embed code is needed.
    """
    url = models.URLField()
~~    max_width = models.SmallIntegerField(null=True, blank=True)
    type = models.CharField(max_length=10, choices=EMBED_TYPES)
    html = models.TextField(blank=True)
    title = models.TextField(blank=True)
    author_name = models.TextField(blank=True)
    provider_name = models.TextField(blank=True)
    thumbnail_url = models.URLField(max_length=255, null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('url', 'max_width')
        verbose_name = _('embed')
        verbose_name_plural = _('embeds')

    @property
    def ratio(self):
        if self.width and self.height:
            return self.height / self.width

    @property
    def ratio_css(self):
        ratio = self.ratio
        if ratio:
            return str(ratio * 100) + "%"

    @property
    def is_responsive(self):
        return self.ratio is not None

    def __str__(self):
        return self.url

```


## Example 2 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / migrations / 0001_initial.py**](https://github.com/divio/django-filer/blob/develop/filer/migrations/0001_initial.py)

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
~~from django.db import migrations, models

import filer.fields.multistorage_file
import filer.models.mixins
from filer.settings import FILER_IMAGE_MODEL


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clipboard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'clipboard',
                'verbose_name_plural': 'clipboards',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClipboardItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clipboard', models.ForeignKey(verbose_name='clipboard', to='filer.Clipboard', on_delete=django.db.models.deletion.CASCADE)),
            ],
            options={
                'verbose_name': 'clipboard item',
                'verbose_name_plural': 'clipboard items',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', filer.fields.multistorage_file.MultiStorageFileField(max_length=255, upload_to=filer.fields.multistorage_file.generate_filename_multistorage, null=True, verbose_name='file', blank=True)),
                ('_file_size', models.IntegerField(null=True, verbose_name='file size', blank=True)),
                ('sha1', models.CharField(default='', max_length=40, verbose_name='sha1', blank=True)),
                ('has_all_mandatory_data', models.BooleanField(default=False, verbose_name='has all mandatory data', editable=False)),
                ('original_filename', models.CharField(max_length=255, null=True, verbose_name='original filename', blank=True)),
                ('name', models.CharField(default='', max_length=255, verbose_name='name', blank=True)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='uploaded at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('is_public', models.BooleanField(default=True, help_text='Disable any permission checking for this file. File will be publicly accessible to anyone.', verbose_name='Permissions disabled')),
            ],
            options={
                'verbose_name': 'file',
                'verbose_name_plural': 'files',
            },
            bases=(models.Model, filer.models.mixins.IconsMixin),
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='uploaded at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('owner', models.ForeignKey(related_name='filer_owned_folders', verbose_name='owner', blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.CASCADE)),
                ('parent', models.ForeignKey(related_name='children', verbose_name='parent', blank=True, to='filer.Folder', null=True, on_delete=django.db.models.deletion.CASCADE)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Folder',
                'verbose_name_plural': 'Folders',
                'permissions': (('can_use_directory_listing', 'Can use directory listing'),),
            },
            bases=(models.Model, filer.models.mixins.IconsMixin),
        ),
        migrations.CreateModel(
            name='FolderPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
~~                ('type', models.SmallIntegerField(default=0, verbose_name='type', choices=[(0, 'all items'), (1, 'this item only'), (2, 'this item and all children')])),
                ('everybody', models.BooleanField(default=False, verbose_name='everybody')),
~~                ('can_edit', models.SmallIntegerField(default=None, null=True, verbose_name='can edit', blank=True, choices=[(1, 'allow'), (0, 'deny')])),
~~                ('can_read', models.SmallIntegerField(default=None, null=True, verbose_name='can read', blank=True, choices=[(1, 'allow'), (0, 'deny')])),
~~                ('can_add_children', models.SmallIntegerField(default=None, null=True, verbose_name='can add children', blank=True, choices=[(1, 'allow'), (0, 'deny')])),
                ('folder', models.ForeignKey(verbose_name='folder', blank=True, to='filer.Folder', null=True, on_delete=django.db.models.deletion.CASCADE)),
                ('group', models.ForeignKey(related_name='filer_folder_permissions', verbose_name='group', blank=True, to='auth.Group', null=True, on_delete=django.db.models.deletion.CASCADE)),
                ('user', models.ForeignKey(related_name='filer_folder_permissions', verbose_name='user', blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.CASCADE)),
            ],
            options={
                'verbose_name': 'folder permission',
                'verbose_name_plural': 'folder permissions',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='folder',
            unique_together=set([('parent', 'name')]),
        ),
        migrations.AddField(
            model_name='file',
            name='folder',
            field=models.ForeignKey(related_name='all_files', verbose_name='folder', blank=True, to='filer.Folder', null=True, on_delete=django.db.models.deletion.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='file',
            name='owner',
            field=models.ForeignKey(related_name='owned_files', verbose_name='owner', blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='file',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_filer.file_set', editable=False, to='contenttypes.ContentType', null=True, on_delete=django.db.models.deletion.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clipboarditem',
            name='file',
            field=models.ForeignKey(verbose_name='file', to='filer.File', on_delete=django.db.models.deletion.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clipboard',
            name='files',
            field=models.ManyToManyField(related_name='in_clipboards', verbose_name='files', through='filer.ClipboardItem', to='filer.File'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clipboard',
            name='user',
            field=models.ForeignKey(related_name='filer_clipboards', verbose_name='user', to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.CASCADE),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('file_ptr', models.OneToOneField(serialize=False, auto_created=True, to='filer.File', primary_key=True, parent_link=True, on_delete=django.db.models.deletion.CASCADE)),
                ('_height', models.IntegerField(null=True, blank=True)),
                ('_width', models.IntegerField(null=True, blank=True)),
                ('date_taken', models.DateTimeField(verbose_name='date taken', null=True, editable=False, blank=True)),
                ('default_alt_text', models.CharField(max_length=255, null=True, verbose_name='default alt text', blank=True)),
                ('default_caption', models.CharField(max_length=255, null=True, verbose_name='default caption', blank=True)),
                ('author', models.CharField(max_length=255, null=True, verbose_name='author', blank=True)),
                ('must_always_publish_author_credit', models.BooleanField(default=False, verbose_name='must always publish author credit')),
                ('must_always_publish_copyright', models.BooleanField(default=False, verbose_name='must always publish copyright')),
                ('subject_location', models.CharField(default=None, max_length=64, null=True, verbose_name='subject location', blank=True)),
            ],
            options={
                'swappable': 'FILER_IMAGE_MODEL',
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
            },
            bases=('filer.file',),
        )
    ]

```


## Example 3 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / migrations / 0002_auto_20140816_1918.py**](https://github.com/divio/django-cms/blob/develop/cms/migrations/0002_auto_20140816_1918.py)

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import cms.models.static_placeholder
import cms.models.fields
from django.conf import settings
from django.contrib.auth import get_user_model
~~from django.db import models, migrations
import django.utils.timezone

User = get_user_model()

user_model_label = '%s.%s' % (User._meta.app_label, User._meta.model_name)
user_ptr_name = '%s_ptr' % User._meta.object_name.lower()


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageUser',
            fields=[
                (user_ptr_name, models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, auto_created=True, parent_link=True, serialize=False, on_delete=models.CASCADE)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='created_users', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'User (page)',
                'verbose_name_plural': 'Users (page)',
            },
            bases=(user_model_label,),
        ),
        migrations.CreateModel(
            name='PageUserGroup',
            fields=[
                ('group_ptr', models.OneToOneField(primary_key=True, to='auth.Group', auto_created=True, parent_link=True, serialize=False, on_delete=models.CASCADE)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='created_usergroups', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'User group (page)',
                'verbose_name_plural': 'User groups (page)',
            },
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='Placeholder',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('slot', models.CharField(db_index=True, max_length=50, verbose_name='slot', editable=False)),
                ('default_width', models.PositiveSmallIntegerField(null=True, verbose_name='width', editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='page',
            name='placeholders',
            field=models.ManyToManyField(to='cms.Placeholder', editable=False),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('publisher_is_draft', 'application_namespace'), ('reverse_id', 'site', 'publisher_is_draft')]),
        ),
        migrations.AddField(
            model_name='cmsplugin',
            name='placeholder',
            field=models.ForeignKey(null=True, to='cms.Placeholder', editable=False, on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aliaspluginmodel',
            name='alias_placeholder',
            field=models.ForeignKey(null=True, to='cms.Placeholder', related_name='alias_placeholder', editable=False, on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='PlaceholderReference',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, to='cms.CMSPlugin', auto_created=True, parent_link=True, serialize=False, on_delete=models.CASCADE)),
                ('name', models.CharField(max_length=255)),
                ('placeholder_ref', cms.models.fields.PlaceholderField(null=True, to='cms.Placeholder', slotname='clipboard', editable=False)),
            ],
            options={
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='StaticPlaceholder',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255, default='', help_text='Descriptive name to identify this static placeholder. Not displayed to users.', blank=True, verbose_name='static placeholder name')),
                ('code', models.CharField(max_length=255, verbose_name='placeholder code', help_text='To render the static placeholder in templates.', blank=True)),
                ('dirty', models.BooleanField(default=False, editable=False)),
                ('creation_method', models.CharField(max_length=20, default='code', blank=True, verbose_name='creation_method', choices=cms.models.static_placeholder.StaticPlaceholder.CREATION_METHODS)),
                ('draft', cms.models.fields.PlaceholderField(null=True, to='cms.Placeholder', verbose_name='placeholder content', related_name='static_draft', slotname=cms.models.static_placeholder.static_slotname, editable=False)),
                ('public', cms.models.fields.PlaceholderField(null=True, to='cms.Placeholder', slotname=cms.models.static_placeholder.static_slotname, related_name='static_public', editable=False)),
                ('site', models.ForeignKey(null=True, to='sites.Site', blank=True, on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'static placeholder',
                'verbose_name_plural': 'static placeholders',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='staticplaceholder',
            unique_together=set([('code', 'site')]),
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('language', models.CharField(db_index=True, max_length=15, verbose_name='language')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('page_title', models.CharField(max_length=255, null=True, help_text='overwrite the title (html title tag)', blank=True, verbose_name='title')),
                ('menu_title', models.CharField(max_length=255, null=True, help_text='overwrite the title in the menu', blank=True, verbose_name='title')),
                ('meta_description', models.TextField(max_length=155, null=True, help_text='The text displayed in search engines.', blank=True, verbose_name='description')),
                ('slug', models.SlugField(max_length=255, verbose_name='slug')),
                ('path', models.CharField(db_index=True, max_length=255, verbose_name='Path')),
                ('has_url_overwrite', models.BooleanField(db_index=True, default=False, editable=False, verbose_name='has url overwrite')),
                ('redirect', models.CharField(max_length=255, null=True, blank=True, verbose_name='redirect')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='creation date', editable=False)),
                ('published', models.BooleanField(default=False, verbose_name='is published')),
                ('publisher_is_draft', models.BooleanField(db_index=True, default=True, editable=False)),
~~                ('publisher_state', models.SmallIntegerField(db_index=True, default=0, editable=False)),
                ('page', models.ForeignKey(to='cms.Page', verbose_name='page', related_name='title_set', on_delete=models.CASCADE)),
                ('publisher_public', models.OneToOneField(null=True, to='cms.Title', related_name='publisher_draft', editable=False, on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='title',
            unique_together=set([('language', 'page')]),
        ),
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('language', models.CharField(max_length=10, choices=settings.LANGUAGES, help_text='The language for the admin interface and toolbar', verbose_name='Language')),
                ('clipboard', models.ForeignKey(null=True, to='cms.Placeholder', blank=True, editable=False, on_delete=models.CASCADE)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True, related_name='djangocms_usersettings', editable=False, on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'user setting',
                'verbose_name_plural': 'user settings',
            },
            bases=(models.Model,),
        ),
    ]

```


## Example 4 from django-filter
[django-filter](https://github.com/carltongibson/django-filter)
([project documentation](https://django-filter.readthedocs.io/en/master/)
and
[PyPI page](https://pypi.org/project/django-filter/2.2.0/))
makes it easier to filter down querysets from the
[Django ORM](/django-orm.html) by providing common bits of boilerplate
code. django-filter is provided as
[open source](https://github.com/carltongibson/django-filter/blob/master/LICENSE).

[**django-filter / django_filters / . / filterset.py**](https://github.com/carltongibson/django-filter/blob/master/django_filters/./filterset.py)

```python
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
)
from .utils import (
    get_all_model_fields,
    get_model_field,
    resolve_field,
    try_dbfield
)


def remote_queryset(field):
    """
    Get the queryset for the other side of a relationship. This works
    for both `RelatedField`s and `ForignObjectRel`s.
    """
    model = field.related_model

    # Reverse relationships do not have choice limits
    if not hasattr(field, 'get_limit_choices_to'):
        return model._default_manager.all()

    limit_choices_to = field.get_limit_choices_to()
    return model._default_manager.complex_filter(limit_choices_to)


class FilterSetOptions(object):
    def __init__(self, options=None):
        self.model = getattr(options, 'model', None)
        self.fields = getattr(options, 'fields', None)
        self.exclude = getattr(options, 'exclude', None)

        self.filter_overrides = getattr(options, 'filter_overrides', {})


class FilterSetMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['declared_filters'] = cls.get_declared_filters(bases, attrs)

        new_class = super().__new__(cls, name, bases, attrs)
        new_class._meta = FilterSetOptions(getattr(new_class, 'Meta', None))
        new_class.base_filters = new_class.get_filters()

        # TODO: remove assertion in 2.1
        assert not hasattr(new_class, 'filter_for_reverse_field'), (
            "`%(cls)s.filter_for_reverse_field` has been removed. "
            "`%(cls)s.filter_for_field` now generates filters for reverse fields. "
            "See: https://django-filter.readthedocs.io/en/master/guide/migration.html"
            % {'cls': new_class.__name__}
        )

        return new_class

    @classmethod
    def get_declared_filters(cls, bases, attrs):
        filters = [
            (filter_name, attrs.pop(filter_name))
            for filter_name, obj in list(attrs.items())
            if isinstance(obj, Filter)
        ]

        # Default the `filter.field_name` to the attribute name on the filterset
        for filter_name, f in filters:
            if getattr(f, 'field_name', None) is None:
                f.field_name = filter_name

        filters.sort(key=lambda x: x[1].creation_counter)

        # merge declared filters from base classes
        for base in reversed(bases):
            if hasattr(base, 'declared_filters'):
                filters = [
                    (name, f) for name, f
                    in base.declared_filters.items()
                    if name not in attrs
                ] + filters

        return OrderedDict(filters)


FILTER_FOR_DBFIELD_DEFAULTS = {
    models.AutoField:                   {'filter_class': NumberFilter},
    models.CharField:                   {'filter_class': CharFilter},
    models.TextField:                   {'filter_class': CharFilter},
    models.BooleanField:                {'filter_class': BooleanFilter},
    models.DateField:                   {'filter_class': DateFilter},
    models.DateTimeField:               {'filter_class': DateTimeFilter},
    models.TimeField:                   {'filter_class': TimeFilter},
    models.DurationField:               {'filter_class': DurationFilter},
    models.DecimalField:                {'filter_class': NumberFilter},
~~    models.SmallIntegerField:           {'filter_class': NumberFilter},
    models.IntegerField:                {'filter_class': NumberFilter},
    models.PositiveIntegerField:        {'filter_class': NumberFilter},
    models.PositiveSmallIntegerField:   {'filter_class': NumberFilter},
    models.FloatField:                  {'filter_class': NumberFilter},
    models.NullBooleanField:            {'filter_class': BooleanFilter},
    models.SlugField:                   {'filter_class': CharFilter},
    models.EmailField:                  {'filter_class': CharFilter},
    models.FilePathField:               {'filter_class': CharFilter},
    models.URLField:                    {'filter_class': CharFilter},
    models.GenericIPAddressField:       {'filter_class': CharFilter},
    models.CommaSeparatedIntegerField:  {'filter_class': CharFilter},
    models.UUIDField:                   {'filter_class': UUIDFilter},


## ... source file continues with no further relevant examples ...
```
