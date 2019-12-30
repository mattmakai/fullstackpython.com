title: django.db.models GenericIPAddressField Python Code Examples
category: page
slug: django-db-models-genericipaddressfield-examples
sortorder: 500012850
toc: False
sidebartitle: django.db.models GenericIPAddressField
meta: Python code examples for the GenericIPAddressField class used in the Django ORM, found within the django.db.models module of the Django project. 


[GenericIPAddressField](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
is a [Django ORM](/django-orm.html) for mapping from your Python code to an
database column that needs to store a valid IP address.

The [Django](/django.html) project has great documentation for
[GenericIPAddressField](https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.GenericIPAddressField)
as well as all of the other column fields.

Note that `GenericIPAddressField` is defined within the 
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

[**AuditLog / src / auditlog / models.py**](https://github.com/jjkester/django-auditlog/blob/master/src/auditlog/models.py)

```python
from __future__ import unicode_literals

import json
import ast

from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import FieldDoesNotExist
~~from django.db import models, DEFAULT_DB_ALIAS
from django.db.models import QuerySet, Q
from django.utils import formats, timezone
from django.utils.encoding import python_2_unicode_compatible, smart_text
from django.utils.six import iteritems, integer_types
from django.utils.translation import ugettext_lazy as _

from jsonfield.fields import JSONField
from dateutil import parser
from dateutil.tz import gettz


## ... source file abbreviated to get to GenericIPAddressExample ...


@python_2_unicode_compatible
class LogEntry(models.Model):
    """
    Represents an entry in the audit log. The content type is saved along with the textual and numeric (if available)
    primary key, as well as the textual representation of the object when it was saved. It holds the action performed
    and the fields that were changed in the transaction.

    If AuditlogMiddleware is used, the actor will be set automatically. Keep in mind that editing / re-saving LogEntry
    instances may set the actor to a wrong value - editing LogEntry instances is not recommended (and it should not be
    necessary).
    """

    class Action:
        """
        The actions that Auditlog distinguishes: creating, updating and deleting objects. Viewing objects is not logged.
        The values of the actions are numeric, a higher integer value means a more intrusive action. This may be useful
        in some cases when comparing actions because the ``__lt``, ``__lte``, ``__gt``, ``__gte`` lookup filters can be
        used in queries.

        The valid actions are :py:attr:`Action.CREATE`, :py:attr:`Action.UPDATE` and :py:attr:`Action.DELETE`.
        """
        CREATE = 0
        UPDATE = 1
        DELETE = 2

        choices = (
            (CREATE, _("create")),
            (UPDATE, _("update")),
            (DELETE, _("delete")),
        )

    content_type = models.ForeignKey(to='contenttypes.ContentType', on_delete=models.CASCADE, related_name='+', verbose_name=_("content type"))
    object_pk = models.CharField(db_index=True, max_length=255, verbose_name=_("object pk"))
    object_id = models.BigIntegerField(blank=True, db_index=True, null=True, verbose_name=_("object id"))
    object_repr = models.TextField(verbose_name=_("object representation"))
    action = models.PositiveSmallIntegerField(choices=Action.choices, verbose_name=_("action"))
    changes = models.TextField(blank=True, verbose_name=_("change message"))
    actor = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, related_name='+', verbose_name=_("actor"))
~~    remote_addr = models.GenericIPAddressField(blank=True, null=True, verbose_name=_("remote address"))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_("timestamp"))
    additional_data = JSONField(blank=True, null=True, verbose_name=_("additional data"))

    objects = LogEntryManager()

    class Meta:
        get_latest_by = 'timestamp'
        ordering = ['-timestamp']
        verbose_name = _("log entry")
        verbose_name_plural = _("log entries")

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

## ... source file continues with no further GenericIPAddress examples ...
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

[**django-axes / axes / migrations / 0002_auto_20151217_2044.py**](https://github.com/jazzband/django-axes/blob/master/axes/migrations/0002_auto_20151217_2044.py)

```python
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axes', '0001_initial'),
    ]

    operations = [
~~        migrations.AlterField(
~~            model_name='accessattempt',
~~            name='ip_address',
~~            field=models.GenericIPAddressField(db_index=True, null=True, verbose_name='IP Address'),
~~        ),
        migrations.AlterField(
            model_name='accessattempt',
            name='trusted',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='accessattempt',
            name='user_agent',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='accessattempt',
            name='username',
            field=models.CharField(db_index=True, max_length=255, null=True),
        ),
~~        migrations.AlterField(
~~            model_name='accesslog',
~~            name='ip_address',
~~            field=models.GenericIPAddressField(db_index=True, null=True, verbose_name='IP Address'),
~~        ),
        migrations.AlterField(
            model_name='accesslog',
            name='trusted',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='user_agent',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='username',
            field=models.CharField(db_index=True, max_length=255, null=True),
        ),
    ]

```


## Example 3 from django-wiki
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
~~from django.db.models.fields import GenericIPAddressField as IPAddressField
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
~~                ('ip_address', IPAddressField(null=True, verbose_name='IP address', blank=True, editable=False)),
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
~~                ('ip_address', IPAddressField(null=True, verbose_name='IP address', blank=True, editable=False)),
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

## ... source file continues with no further GenericIPAddressField examples ...

```

