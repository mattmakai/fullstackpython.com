title: django.db migrations Example Code
category: page
slug: django-db-migrations-examples
sortorder: 500011166
toc: False
sidebartitle: django.db migrations
meta: Python example code for the migrations callable from the django.db module of the Django project.


migrations is a callable within the django.db module of the Django project.


## Example 1 from django-axes
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

[**django-axes / axes / migrations / 0004_auto_20181024_1538.py**](https://github.com/jazzband/django-axes/blob/master/axes/migrations/0004_auto_20181024_1538.py)

```python
# 0004_auto_20181024_1538.py
~~from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("axes", "0003_auto_20160322_0929")]

    operations = [
~~        migrations.AlterModelOptions(
            name="accessattempt",
            options={
                "verbose_name": "access attempt",
                "verbose_name_plural": "access attempts",
            },
        ),
~~        migrations.AlterModelOptions(
            name="accesslog",
            options={
                "verbose_name": "access log",
                "verbose_name_plural": "access logs",
            },
        ),
~~        migrations.AlterField(
            model_name="accessattempt",
            name="attempt_time",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Attempt Time"),
        ),
~~        migrations.AlterField(
            model_name="accessattempt",
            name="user_agent",
            field=models.CharField(
                db_index=True, max_length=255, verbose_name="User Agent"
            ),
        ),
~~        migrations.AlterField(
            model_name="accessattempt",
            name="username",
            field=models.CharField(
                db_index=True, max_length=255, null=True, verbose_name="Username"
            ),
        ),
~~        migrations.AlterField(
            model_name="accesslog",
            name="attempt_time",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Attempt Time"),
        ),
~~        migrations.AlterField(
            model_name="accesslog",
            name="logout_time",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Logout Time"
            ),
        ),
~~        migrations.AlterField(
            model_name="accesslog",
            name="user_agent",
            field=models.CharField(
                db_index=True, max_length=255, verbose_name="User Agent"
            ),
        ),
~~        migrations.AlterField(
            model_name="accesslog",
            name="username",
            field=models.CharField(
                db_index=True, max_length=255, null=True, verbose_name="Username"
            ),
        ),
    ]



## ... source file continues with no further migrations examples...

```


## Example 2 from django-cms
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
~~        migrations.AlterField(
            model_name='title',
            name='redirect',
            field=models.CharField(max_length=2048, null=True, verbose_name='redirect', blank=True),
            preserve_default=True,
        ),
    ]



## ... source file continues with no further migrations examples...

```


## Example 3 from django-filer
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
~~        migrations.AlterField(
            model_name='image',
            name='file_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='%(app_label)s_%(class)s_file', serialize=False, to='filer.File'),
        ),
    ]



## ... source file continues with no further migrations examples...

```


## Example 4 from django-flexible-subscriptions
[django-flexible-subscriptions](https://github.com/studybuffalo/django-flexible-subscriptions)
([project documentation](https://django-flexible-subscriptions.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-flexible-subscriptions/))
provides boilerplate code for adding subscription and recurrent billing
to [Django](/django.html) web applications. Various payment providers
can be added on the back end to run the transactions.

The django-flexible-subscriptions project is open sourced under the
[GNU General Public License v3.0](https://github.com/studybuffalo/django-flexible-subscriptions/blob/master/LICENSE).

[**django-flexible-subscriptions / subscriptions / migrations / 0006_add_slugs.py**](https://github.com/studybuffalo/django-flexible-subscriptions/blob/master/subscriptions/migrations/0006_add_slugs.py)

```python
# 0006_add_slugs.py

~~from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0005_update_recurrence_unit_default'),
    ]

    operations = [
~~        migrations.AddField(
            model_name='plancost',
            name='slug',
            field=models.SlugField(
                blank=True,
                help_text='slug to reference these cost details',
                max_length=128,
                null=True,
                unique=True,
            ),
        ),
~~        migrations.AddField(
            model_name='subscriptionplan',
            name='slug',
            field=models.SlugField(
                blank=True,
                help_text='slug to reference the subscription plan',
                max_length=128,
                null=True,
                unique=True,
            ),
        ),
~~        migrations.AddField(
            model_name='planlist',
            name='slug',
            field=models.SlugField(
                blank=True,
                help_text='slug to reference the subscription plan list',
                max_length=128,
                null=True,
                unique=True,
            ),
        ),
    ]



## ... source file continues with no further migrations examples...

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
~~        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
~~        migrations.CreateModel(
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
~~        migrations.CreateModel(
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
~~        migrations.AlterUniqueTogether(
            name='userobjectpermission',
            unique_together={('user', 'permission', 'object_pk')},
        ),
~~        migrations.AlterUniqueTogether(
            name='groupobjectpermission',
            unique_together={('group', 'permission', 'object_pk')},
        ),
    ]



## ... source file continues with no further migrations examples...

```


## Example 6 from django-jet
[django-jet](https://github.com/geex-arts/django-jet)
([project documentation](https://jet.readthedocs.io/en/latest/),
[PyPI project page](https://pypi.org/project/django-jet/) and
[more information](http://jet.geex-arts.com/))
is a fancy [Django](/django.html) Admin panel replacement.

The django-jet project is open source under the
[GNU Affero General Public License v3.0](https://github.com/geex-arts/django-jet/blob/dev/LICENSE).

[**django-jet / jet / migrations / 0002_delete_userdashboardmodule.py**](https://github.com/geex-arts/django-jet/blob/dev/jet/migrations/0002_delete_userdashboardmodule.py)

```python
# 0002_delete_userdashboardmodule.py
from __future__ import unicode_literals

~~from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jet', '0001_initial'),
    ]

    operations = [
~~        migrations.DeleteModel(
            name='UserDashboardModule',
        ),
    ]



## ... source file continues with no further migrations examples...

```


## Example 7 from django-oauth-toolkit
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
# 0001_initial.py
from django.conf import settings
import django.db.models.deletion
~~from django.db import migrations, models

import oauth2_provider.generators
import oauth2_provider.validators
from oauth2_provider.settings import oauth2_settings


class Migration(migrations.Migration):
    dependencies = [
~~        migrations.swappable_dependency(settings.AUTH_USER_MODEL)
    ]

    operations = [
~~        migrations.CreateModel(
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
~~        migrations.CreateModel(
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
            ],
            options={
                'abstract': False,
                'swappable': 'OAUTH2_PROVIDER_ACCESS_TOKEN_MODEL',
            },
        ),
~~        migrations.CreateModel(
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
~~        migrations.CreateModel(
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
~~        migrations.AddField(
            model_name='AccessToken',
            name='source_refresh_token',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=oauth2_settings.REFRESH_TOKEN_MODEL, related_name="refreshed_access_token"),
        ),
    ]



## ... source file continues with no further migrations examples...

```


## Example 8 from django-push-notifications
[django-push-notifications](https://github.com/jazzband/django-push-notifications)
is a [Django](/django.html) app for storing and interacting with
push notification services such as
[Google's Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/)
and
[Apple Notifications](https://developer.apple.com/notifications/).
The django-push-notification project's source code is available
open source under the
[MIT license](https://github.com/jazzband/django-push-notifications/blob/master/LICENSE).

[**django-push-notifications / push_notifications / migrations / 0002_auto_20160106_0850.py**](https://github.com/jazzband/django-push-notifications/blob/master/push_notifications/migrations/0002_auto_20160106_0850.py)

```python
# 0002_auto_20160106_0850.py
~~from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('push_notifications', '0001_initial'),
    ]

    operations = [
~~        migrations.AlterField(
            model_name='apnsdevice',
            name='registration_id',
            field=models.CharField(max_length=200, unique=True, verbose_name='Registration ID'),
        ),
    ]



## ... source file continues with no further migrations examples...

```


## Example 9 from django-sitetree
[django-sitetree](https://github.com/idlesign/django-sitetree)
([project documentation](https://django-sitetree.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-sitetree/))
is a [Django](/django.html) extension that makes it easier for
developers to add site trees, menus and breadcrumb navigation elements
to their web applications.

The django-sitetree project is provided as open source under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/idlesign/django-sitetree/blob/master/LICENSE).

[**django-sitetree / sitetree / migrations / 0001_initial.py**](https://github.com/idlesign/django-sitetree/blob/master/sitetree/migrations/0001_initial.py)

```python
# 0001_initial.py
from __future__ import unicode_literals

~~from django.db import models, migrations
import sitetree.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
~~        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Site tree title for presentational purposes.', max_length=100, verbose_name='Title', blank=True)),
                ('alias', models.CharField(help_text='Short name to address site tree from templates.<br /><b>Note:</b> change with care.', unique=True, max_length=80, verbose_name='Alias', db_index=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Site Tree',
                'verbose_name_plural': 'Site Trees',
            },
            bases=(models.Model,),
        ),
~~        migrations.CreateModel(
            name='TreeItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Site tree item title. Can contain template variables E.g.: {{ mytitle }}.', max_length=100, verbose_name='Title')),
                ('hint', models.CharField(default='', help_text='Some additional information about this item that is used as a hint.', max_length=200, verbose_name='Hint', blank=True)),
                ('url', models.CharField(help_text='Exact URL or URL pattern (see "Additional settings") for this item.', max_length=200, verbose_name='URL', db_index=True)),
                ('urlaspattern', models.BooleanField(default=False, help_text='Whether the given URL should be treated as a pattern.<br /><b>Note:</b> Refer to Django "URL dispatcher" documentation (e.g. "Naming URL patterns" part).', db_index=True, verbose_name='URL as Pattern')),
                ('hidden', models.BooleanField(default=False, help_text='Whether to show this item in navigation.', db_index=True, verbose_name='Hidden')),
                ('alias', sitetree.models.CharFieldNullable(max_length=80, blank=True, help_text='Short name to address site tree item from a template.<br /><b>Reserved aliases:</b> "trunk", "this-children", "this-siblings", "this-ancestor-children", "this-parent-siblings".', null=True, verbose_name='Alias', db_index=True)),
                ('description', models.TextField(default='', help_text='Additional comments on this item.', verbose_name='Description', blank=True)),
                ('inmenu', models.BooleanField(default=True, help_text='Whether to show this item in a menu.', db_index=True, verbose_name='Show in menu')),
                ('inbreadcrumbs', models.BooleanField(default=True, help_text='Whether to show this item in a breadcrumb path.', db_index=True, verbose_name='Show in breadcrumb path')),
                ('insitetree', models.BooleanField(default=True, help_text='Whether to show this item in a site tree.', db_index=True, verbose_name='Show in site tree')),
                ('access_loggedin', models.BooleanField(default=False, help_text='Check it to grant access to this item to authenticated users only.', db_index=True, verbose_name='Logged in only')),
                ('access_guest', models.BooleanField(default=False, help_text='Check it to grant access to this item to guests only.', db_index=True, verbose_name='Guests only')),
                ('access_restricted', models.BooleanField(default=False, help_text='Check it to restrict user access to this item, using Django permissions system.', db_index=True, verbose_name='Restrict access to permissions')),
                ('access_perm_type', models.IntegerField(default=1, help_text='<b>Any</b> &mdash; user should have any of chosen permissions. <b>All</b> &mdash; user should have all chosen permissions.', verbose_name='Permissions interpretation', choices=[(1, 'Any'), (2, 'All')])),
                ('sort_order', models.IntegerField(default=0, help_text='Item position among other site tree items under the same parent.', verbose_name='Sort order', db_index=True)),
                ('access_permissions', models.ManyToManyField(to='auth.Permission', verbose_name='Permissions granting access', blank=True)),
                ('parent', models.ForeignKey(related_name='treeitem_parent', on_delete=models.CASCADE, blank=True, to='sitetree.TreeItem', help_text='Parent site tree item.', null=True, verbose_name='Parent')),
                ('tree', models.ForeignKey(related_name='treeitem_tree', on_delete=models.CASCADE, verbose_name='Site Tree', to='sitetree.Tree', help_text='Site tree this item belongs to.')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Site Tree Item',
                'verbose_name_plural': 'Site Tree Items',
            },
            bases=(models.Model,),
        ),
~~        migrations.AlterUniqueTogether(
            name='treeitem',
            unique_together=set([('tree', 'alias')]),
        ),
    ]



## ... source file continues with no further migrations examples...

```


## Example 10 from django-smithy
[django-smithy](https://github.com/jamiecounsell/django-smithy) is
a [Django](/django.html) code library that allows users to send
HTTP requests from the Django admin user interface. The code for
the project is open source under the
[MIT license](https://github.com/jamiecounsell/django-smithy/blob/master/LICENSE).

[**django-smithy / smithy / migrations / 0004_auto_20190721_2012.py**](https://github.com/jamiecounsell/django-smithy/blob/master/smithy/migrations/0004_auto_20190721_2012.py)

```python
# 0004_auto_20190721_2012.py

~~from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smithy', '0003_auto_20190721_2004'),
    ]

    operations = [
~~        migrations.AlterField(
            model_name='bodyparameter',
            name='value',
            field=models.TextField(blank=True),
        ),
~~        migrations.AlterField(
            model_name='cookie',
            name='value',
            field=models.TextField(blank=True),
        ),
~~        migrations.AlterField(
            model_name='header',
            name='value',
            field=models.TextField(blank=True),
        ),
~~        migrations.AlterField(
            model_name='queryparameter',
            name='value',
            field=models.TextField(blank=True),
        ),
~~        migrations.AlterField(
            model_name='variable',
            name='value',
            field=models.TextField(blank=True),
        ),
    ]



## ... source file continues with no further migrations examples...

```


## Example 11 from django-sql-explorer
[django-sql-explorer](https://github.com/groveco/django-sql-explorer)
([PyPI page](https://pypi.org/project/django-sql-explorer/0.2/)),
also referred to as "SQL Explorer",
is a code library for the [Django](/django.html) Admin that allows
approved, authenticated users to view and execute direct database SQL
queries. The tool keeps track of executed queries so users can share them
with each other, as well as export results to downloadable formats.
django-sql-explorer is provided as open source under the
[MIT license](https://github.com/groveco/django-sql-explorer/blob/master/LICENSE).

[**django-sql-explorer / explorer / migrations / 0002_auto_20150501_1515.py**](https://github.com/groveco/django-sql-explorer/blob/master/explorer/migrations/0002_auto_20150501_1515.py)

```python
# 0002_auto_20150501_1515.py
from __future__ import unicode_literals

~~from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0001_initial'),
    ]

    operations = [
~~        migrations.RemoveField(
            model_name='querylog',
            name='is_playground',
        ),
~~        migrations.AlterField(
            model_name='querylog',
            name='sql',
            field=models.TextField(null=True, blank=True),
        ),
    ]



## ... source file continues with no further migrations examples...

```


## Example 12 from django-taggit
[django-taggit](https://github.com/jazzband/django-taggit/)
([PyPI page](https://pypi.org/project/django-taggit/)) provides a way
to create, store, manage and use tags in a [Django](/django.html) project.
The code for django-taggit is
[open source](https://github.com/jazzband/django-taggit/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-taggit / taggit / migrations / 0002_auto_20150616_2121.py**](https://github.com/jazzband/django-taggit/blob/master/taggit/migrations/0002_auto_20150616_2121.py)

```python
# 0002_auto_20150616_2121.py
~~from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("taggit", "0001_initial")]

    operations = [
~~        migrations.AlterIndexTogether(
            name="taggeditem", index_together={("content_type", "object_id")}
        )
    ]



## ... source file continues with no further migrations examples...

```


## Example 13 from django-user-visit
[django-user-visit](https://github.com/yunojuno/django-user-visit)
([PyPI package information](https://pypi.org/project/django-user-visit/))
is a [Django](/django.html) app and
[middleware](https://docs.djangoproject.com/en/stable/topics/http/middleware/)
for tracking daily user visits to your web application. The goal
is to record per user per day instead of for every request a user
sends to the application. The project is provided as open source
under the
[MIT license](https://github.com/yunojuno/django-user-visit/blob/master/LICENSE).

[**django-user-visit / user_visit / migrations / 0002_add_created_at.py**](https://github.com/yunojuno/django-user-visit/blob/master/user_visit/migrations/0002_add_created_at.py)

```python
# 0002_add_created_at.py
import django.utils.timezone
~~from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_visit", "0001_initial"),
    ]

    operations = [
~~        migrations.AlterModelOptions(
            name="uservisit", options={"get_latest_by": "timestamp"},
        ),
~~        migrations.AddField(
            model_name="uservisit",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                help_text=(
                    "The time at which the database record was created (!=timestamp)"
                ),
            ),
            preserve_default=False,
        ),
    ]



## ... source file continues with no further migrations examples...

```


## Example 14 from django-webshell
[django-webshell](https://github.com/onrik/django-webshell) is an extension
for executing arbitrary code in the
[Django admin](https://docs.djangoproject.com/en/stable/ref/contrib/admin/),
similar to how you can run code by using the `django manage.py shell`
command from the terminal.

The django-webshell project is provided as open source under the
[MIT license](https://github.com/onrik/django-webshell/blob/master/LICENSE).

[**django-webshell / webshell / migrations / 0001_initial.py**](https://github.com/onrik/django-webshell/blob/master/webshell/migrations/0001_initial.py)

```python
# 0001_initial.py
from __future__ import unicode_literals

~~from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
~~        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('source', models.TextField(verbose_name='Source')),
            ],
            options={
                'verbose_name': 'Script',
                'verbose_name_plural': 'Scripts',
            },
        ),
    ]



## ... source file continues with no further migrations examples...

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

[**django-wiki / src/wiki / migrations / 0002_urlpath_moved_to.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/migrations/0002_urlpath_moved_to.py)

```python
# 0002_urlpath_moved_to.py
import django.db.models.deletion
import mptt.fields
~~from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("wiki", "0001_initial"),
    ]

    operations = [
~~        migrations.AddField(
            model_name="urlpath",
            name="moved_to",
            field=mptt.fields.TreeForeignKey(
                blank=True,
                help_text="Article path was moved to this location",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="moved_from",
                to="wiki.URLPath",
                verbose_name="Moved to",
            ),
        ),
    ]



## ... source file continues with no further migrations examples...

```


## Example 16 from dmd-interpreter
[dmd-interpreter](https://github.com/mitchalexbailey/dmd-interpreter)
([running web app](http://www.dmd.nl/DOVE))
is a Python tool to aggregate clinically relevant information related
to variants in the DMD gene and display that [data](/data.html) to a user
with a [Django](/django.html) web application.

[**dmd-interpreter / interpreter / migrations / 0001_initial.py**](https://github.com/mitchalexbailey/dmd-interpreter/blob/master/interpreter/migrations/0001_initial.py)

```python
# 0001_initial.py
from __future__ import unicode_literals

~~from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
~~        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
~~        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'Date Published')),
            ],
        ),
~~        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='interpreter.Question'),
        ),
    ]



## ... source file continues with no further migrations examples...

```


## Example 17 from elasticsearch-django
[elasticsearch-django](https://github.com/yunojuno/elasticsearch-django)
([PyPI package information](https://pypi.org/project/elasticsearch-django/))
is a [Django](/django.html) app for managing
[ElasticSearch](https://github.com/elastic/elasticsearch) indexes
populated by [Django ORM](/django-orm.html) models. The project is
available as open source under the
[MIT license](https://github.com/yunojuno/elasticsearch-django/blob/master/LICENSE).

[**elasticsearch-django / elasticsearch_django / migrations / 0009_searchquery_query_type.py**](https://github.com/yunojuno/elasticsearch-django/blob/master/elasticsearch_django/migrations/0009_searchquery_query_type.py)

```python
# 0009_searchquery_query_type.py

~~from django.db import migrations, models

from ..models import SearchQuery


class Migration(migrations.Migration):

    dependencies = [("elasticsearch_django", "0008_searchquery_search_terms")]

    operations = [
~~        migrations.AddField(
            model_name="searchquery",
            name="query_type",
            field=models.CharField(
                choices=(lambda: SearchQuery.QUERY_TYPE_CHOICES)(),
                default="SEARCH",
                help_text="Does this query return results, or just the hit count?",
                max_length=10,
            ),
        )
    ]



## ... source file continues with no further migrations examples...

```

