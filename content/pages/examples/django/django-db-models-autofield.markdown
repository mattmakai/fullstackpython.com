title: django.db.models AutoField Example Code
category: page
slug: django-db-models-autofield-examples
sortorder: 500012805
toc: False
sidebartitle: django.db.models AutoField
meta: Python code examples for the AutoField class used in the Django ORM, found within the django.db.models module of the Django project. 


[AutoField](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
is a [Django ORM](/django-orm.html) mapping from your Python code to an
integer-type column in your [relational database](/databases.html).

The [Django](/django.html) project has great documentation for
[AutoField](https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.AutoField)
as well as all of the other column fields.

Note that `AutoField` is defined within the 
[django.db.models.fields](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
module but is typically referenced from
[django.db.models](https://github.com/django/django/tree/master/django/db/models)
rather than including the `fields` module reference.


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

[**django-axes / axes / migrations / 0001_initial.py**](https://github.com/jazzband/django-axes/blob/master/axes/migrations/0001_initial.py)

```python
~~from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessAttempt',
            fields=[
                ('id', 
~~                 models.AutoField(verbose_name='ID', 
~~                                  serialize=False, 
~~                                  auto_created=True, 
~~                                  primary_key=True)),
                ('user_agent', models.CharField(max_length=255)),
                ('ip_address', 
                 models.GenericIPAddressField(null=True, 
                                              verbose_name='IP Address')),
                ('username', models.CharField(max_length=255, 
                                              null=True)),
                ('trusted', models.BooleanField(default=False)),
                ('http_accept', 
                 models.CharField(max_length=1025, 
                                  verbose_name='HTTP Accept')),
                ('path_info', 
                 models.CharField(max_length=255, 
                                  verbose_name='Path')),
                ('attempt_time', 
                 models.DateTimeField(auto_now_add=True)),
                ('get_data', 
                 models.TextField(verbose_name='GET Data')),
                ('post_data', models.TextField(verbose_name='POST Data')),
                ('failures_since_start', 
                  models.PositiveIntegerField(verbose_name='Failed Logins')),
            ],
            options={
                'ordering': ['-attempt_time'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccessLog',
            fields=[
~~                ('id', models.AutoField(verbose_name='ID', 
~~                                        serialize=False, 
~~                                        auto_created=True, 
~~                                        primary_key=True)),
                ('user_agent', models.CharField(max_length=255)),
                ('ip_address', 
                 models.GenericIPAddressField(null=True, 
                                              verbose_name='IP Address')),
                ('username', models.CharField(max_length=255, null=True)),
                ('trusted', models.BooleanField(default=False)),
                ('http_accept', 
                 models.CharField(max_length=1025, 
                                  verbose_name='HTTP Accept')),
                ('path_info', 
                 models.CharField(max_length=255, 
                                  verbose_name='Path')),
                ('attempt_time', 
                 models.DateTimeField(auto_now_add=True)),
                ('logout_time', models.DateTimeField(null=True, 
                                                     blank=True)),
            ],
            options={
                'ordering': ['-attempt_time'],
                'abstract': False,
            },
        ),
    ]
```


## Example 2 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / migrations / 0003_thumbnailoption.py**](https://github.com/divio/django-filer/blob/develop/filer/migrations/0003_thumbnailoption.py)

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
~~                ('id', models.AutoField(verbose_name='ID', 
~~                                          serialize=False, 
~~                                          auto_created=True, 
~~                                          primary_key=True)),
                ('name', models.CharField(max_length=100, 
                                          verbose_name='name')),
                ('width', 
                 models.IntegerField(help_text='width in pixel.', 
                                     verbose_name='width')),
                ('height', 
                 models.IntegerField(help_text='height in pixel.', 
                                     verbose_name='height')),
                ('crop', 
                 models.BooleanField(default=True, 
                                     verbose_name='crop')),
                ('upscale', 
                 models.BooleanField(default=True, 
                                     verbose_name='upscale')),
            ],
            options={
                'ordering': ('width', 'height'),
                'verbose_name': 'thumbnail option',
                'verbose_name_plural': 'thumbnail options',
            },
        ),
    ]
```
