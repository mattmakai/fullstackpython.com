title: django.db.models PositiveIntegerField Example Code
category: page
slug: django-db-models-positiveintegerfield-examples
sortorder: 500012880
toc: False
sidebartitle: django.db.models PositiveIntegerField
meta: Python code examples for the PositiveIntegerField class used in the Django ORM, found within the django.db.models module of the Django project. 


[PositiveIntegerField](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
([documentation](https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.PositiveIntegerField))
is a [Django ORM](/django-orm.html) mapping from your Python code to an
integer-type column in your [relational database](/databases.html)
that is restricted to only positive values from 0 to 2147483647.

Note that `PositiveIntegerField` is defined within the 
[django.db.models.fields](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
module but is typically referenced from
[django.db.models](https://github.com/django/django/tree/master/django/db/models)
rather than including the `fields` module reference.


## Example 1 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based content management system with code 
that is open source under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / images / models.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/images/models.py)

```python
import hashlib
import os.path
from collections import OrderedDict
from contextlib import contextmanager
from io import BytesIO

from django.conf import settings
from django.core import checks
from django.core.files import File
~~from django.db import models
from django.forms.utils import flatatt
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from unidecode import unidecode
from willow.image import Image as WillowImage

from wagtail.admin.models import get_object_usage
from wagtail.core import hooks
from wagtail.core.models import CollectionMember
from wagtail.images.exceptions import InvalidFilterSpecError
from wagtail.images.rect import Rect
from wagtail.search import index
from wagtail.search.queryset import SearchableQuerySetMixin


class SourceImageIOError(IOError):
    """
    Custom exception to distinguish IOErrors that were thrown while opening the source image
    """
    pass


class ImageQuerySet(SearchableQuerySetMixin, models.QuerySet):
    pass


def get_upload_to(instance, filename):
    """
    Obtain a valid upload path for an image file.

    This needs to be a module-level function so that it can be referenced within migrations,
    but simply delegates to the `get_upload_to` method of the instance, so that AbstractImage
    subclasses can override it.
    """
    return instance.get_upload_to(filename)


def get_rendition_upload_to(instance, filename):
    """
    Obtain a valid upload path for an image rendition file.

    This needs to be a module-level function so that it can be referenced within migrations,
    but simply delegates to the `get_upload_to` method of the instance, so that AbstractRendition
    subclasses can override it.
    """
    return instance.get_upload_to(filename)


class AbstractImage(CollectionMember, index.Indexed, models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    file = models.ImageField(
        verbose_name=_('file'), upload_to=get_upload_to, width_field='width', height_field='height'
    )
    width = models.IntegerField(verbose_name=_('width'), editable=False)
    height = models.IntegerField(verbose_name=_('height'), editable=False)
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, db_index=True)
    uploaded_by_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_('uploaded by user'),
        null=True, blank=True, editable=False, on_delete=models.SET_NULL
    )

    tags = TaggableManager(help_text=None, blank=True, verbose_name=_('tags'))

~~    focal_point_x = models.PositiveIntegerField(null=True, blank=True)
~~    focal_point_y = models.PositiveIntegerField(null=True, blank=True)
~~    focal_point_width = models.PositiveIntegerField(null=True, blank=True)
~~    focal_point_height = models.PositiveIntegerField(null=True, blank=True)

~~    file_size = models.PositiveIntegerField(null=True, editable=False)
    # A SHA-1 hash of the file contents
    file_hash = models.CharField(max_length=40, blank=True, editable=False)

    objects = ImageQuerySet.as_manager()

    def is_stored_locally(self):
        """
        Returns True if the image is hosted on the local filesystem
        """
        try:
            self.file.path

            return True
        except NotImplementedError:
            return False

    def get_file_size(self):
        if self.file_size is None:
            try:
                self.file_size = self.file.size
            except Exception as e:
                # File not found
                #
                # Have to catch everything, because the exception
                # depends on the file subclass, and therefore the
                # storage being used.
                raise SourceImageIOError(str(e))

            self.save(update_fields=['file_size'])

        return self.file_size


## ... source file continues with no further PositiveIntegerField examples ...

```

## Example 2 from django-axes
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

[**django-axes / axes / migrations / 0001_initial.py**](https://github.com/jazzband/django-axes/blob/master/axes/migrations/0001_initial.py)

```python
# 0001_initial.py
~~from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessAttempt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_agent', models.CharField(max_length=255)),
                ('ip_address', models.GenericIPAddressField(null=True, verbose_name='IP Address')),
                ('username', models.CharField(max_length=255, null=True)),
                ('trusted', models.BooleanField(default=False)),
                ('http_accept', models.CharField(max_length=1025, verbose_name='HTTP Accept')),
                ('path_info', models.CharField(max_length=255, verbose_name='Path')),
                ('attempt_time', models.DateTimeField(auto_now_add=True)),
                ('get_data', models.TextField(verbose_name='GET Data')),
                ('post_data', models.TextField(verbose_name='POST Data')),
~~                ('failures_since_start', models.PositiveIntegerField(verbose_name='Failed Logins')),
            ],
            options={
                'ordering': ['-attempt_time'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccessLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_agent', models.CharField(max_length=255)),
                ('ip_address', models.GenericIPAddressField(null=True, verbose_name='IP Address')),
                ('username', models.CharField(max_length=255, null=True)),
                ('trusted', models.BooleanField(default=False)),
                ('http_accept', models.CharField(max_length=1025, verbose_name='HTTP Accept')),
                ('path_info', models.CharField(max_length=255, verbose_name='Path')),
                ('attempt_time', models.DateTimeField(auto_now_add=True)),
                ('logout_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'ordering': ['-attempt_time'],
                'abstract': False,
            },
        ),
    ]

```


## Example 3 from django-cms
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
~~                ('depth', models.PositiveIntegerField()),
~~                ('numchild', models.PositiveIntegerField(default=0)),
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
~~            field=models.PositiveIntegerField(null=True),
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


## Example 4 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / migrations / 0011_auto_20190418_0137.py**](https://github.com/divio/django-filer/blob/develop/filer/migrations/0011_auto_20190418_0137.py)

```python
# -*- coding: utf-8 -*-
# Generated by Django 2.2 on 2019-04-25 11:29
~~from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0010_auto_20180414_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='level',
~~            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='folder',
            name='lft',
~~            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='folder',
            name='rght',
~~            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterIndexTogether(
            name='folder',
            index_together={('tree_id', 'lft')},
        ),
    ]

```


## Example 5 from django-jet
[django-jet](https://github.com/geex-arts/django-jet)
([project documentation](https://jet.readthedocs.io/en/latest/),
[PyPI project page](https://pypi.org/project/django-jet/) and
[more information](http://jet.geex-arts.com/))
is a fancy [Django](/django.html) Admin panel replacement.

The django-jet project is open source under the
[GNU Affero General Public License v3.0](https://github.com/geex-arts/django-jet/blob/dev/LICENSE).

[**django-jet / jet / migrations / 0001_initial.py**](https://github.com/geex-arts/django-jet/blob/dev/jet/migrations/0001_initial.py)

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

~~from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(verbose_name='URL')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
~~                ('user', models.PositiveIntegerField(verbose_name='user')),
                ('date_add', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
            ],
            options={
                'ordering': ('date_add',),
                'verbose_name': 'bookmark',
                'verbose_name_plural': 'bookmarks',
            },
        ),
        migrations.CreateModel(
            name='PinnedApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_label', models.CharField(max_length=255, verbose_name='application name')),
~~                ('user', models.PositiveIntegerField(verbose_name='user')),
                ('date_add', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
            ],
            options={
                'ordering': ('date_add',),
                'verbose_name': 'pinned application',
                'verbose_name_plural': 'pinned applications',
            },
        ),
        migrations.CreateModel(
            name='UserDashboardModule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('module', models.CharField(max_length=255, verbose_name='module')),
                ('app_label', models.CharField(max_length=255, null=True, verbose_name='application name', blank=True)),
~~                ('user', models.PositiveIntegerField(verbose_name='user')),
~~                ('column', models.PositiveIntegerField(verbose_name='column')),
                ('order', models.IntegerField(verbose_name='order')),
                ('settings', models.TextField(default=b'', verbose_name='settings', blank=True)),
                ('children', models.TextField(default=b'', verbose_name='children', blank=True)),
                ('collapsed', models.BooleanField(default=False, verbose_name='collapsed')),
            ],
            options={
                'ordering': ('column', 'order'),
                'verbose_name': 'user dashboard module',
                'verbose_name_plural': 'user dashboard modules',
            },
        ),
    ]

```


## Example 6 from django-wiki
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
~~from django.db import migrations, models
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
~~                ('object_id', models.PositiveIntegerField(verbose_name='object ID')),
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
~~                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
~~                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
~~                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
~~                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
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

## ... source file continues with no further PositiveIntegerField examples ...

```

