title: django.db.models TextField Example Code
category: page
slug: django-db-models-textfield-examples
sortorder: 50102
toc: False
sidebartitle: django.db.models TextField
meta: Python code examples for the Django ORM's TextField class, found within the django.db.models module of the Django project. 


[TextField](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
is a field used to create an arbitrary amount of text characters in a 
[database](/databases.html) column defined by the 
[Django ORM](/django-orm.html).

The [Django](/django.html) project has wonderful documentation for
[TextField](https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.TextField)
and all of the other column fields.

Note that `TextField` is defined within the 
[django.db.models.fields](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
module but is typically referenced from
[django.db.models](https://github.com/django/django/tree/master/django/db/models)
rather than including the `fields` module reference.


## Example 1 from django-smithy
[django-smithy](https://github.com/jamiecounsell/django-smithy) is
a code library for [Django](/django.html) that makes it easy for users 
to send HTTP requests from the Django admin user interface. The code for
the project is open source under the 
[MIT license](https://github.com/jamiecounsell/django-smithy/blob/master/LICENSE).

[**django-smithy / smithy / models.py**](https://github.com/jamiecounsell/django-smithy/blob/master/smithy/models.py)

```python
# -*- coding: utf-8 -*-

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
    name = models.CharField(max_length = 200)
~~    value = models.TextField(blank = True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Request(TimeStampedModel):
    """
    A base model shared by RequestBlueprint and
    RequestRecord. Used solely to reduce
    """
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
    method = models.CharField(
        max_length = 7, choices = METHODS,
        blank = False, null = False)
    name = models.CharField(max_length = 500, blank = False)
    url = models.CharField(max_length = 2083)
~~    body = models.TextField(blank = True)
    content_type = models.CharField(
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
    """
    A blueprint for HTTP requests. This model will be
    used to generate and send HTTP requests. Once sent,
    a RequestRecord will be created for that request.
    """
    follow_redirects = models.BooleanField(
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

        # Copy RequestBlueprint values to RequestRecord
        for qs in self.name_value_related:
            for obj in qs.all():
                obj.pk = 0
                obj.name = render_with_context(obj.name, context)
                obj.value = render_with_context(obj.value, context)
                obj.add_to(request)
                obj.request = record
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
        # TODO: follow redirects

        RequestRecord.objects.filter(pk = record.pk).update(
            raw_request = parse_dump_result(dump._dump_request_data, prepared_request),
            raw_response = parse_dump_result(dump._dump_response_data, response),
            status = response.status_code,
            **RequestRecord.get_clone_args(self, context)
        )

        # Return fresh copy after update
        return RequestRecord.objects.get(pk = record.pk)


class RequestRecord(Request):
    """
    A record of a Request that has been sent.
    Contains response and diagnostic information
    about the request.
    """
~~    raw_request = models.TextField()
~~    raw_response = models.TextField()
    status = models.PositiveIntegerField(null = True)
    blueprint = models.ForeignKey(
        'smithy.RequestBlueprint',
        on_delete = models.SET_NULL,
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


## source file continues from here without further TextField examples
```


## Example 2 from django-push-notifications
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
~~from django.db import migrations, models

import push_notifications.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='APNSDevice',
            fields=[
                ('id', 
                 models.AutoField(verbose_name='ID', 
                                  serialize=False, 
                                  auto_created=True, 
                                  primary_key=True)),
                ('name', 
                 models.CharField(max_length=255, 
                                  null=True, 
                                  verbose_name='Name', 
                                  blank=True)),
                ('active', 
                 models.BooleanField(default=True, 
                                     help_text='Inactive devices '
                                               'will not be sent '
                                               'notifications', 
                                     verbose_name='Is active')),
                ('date_created', 
                 models.DateTimeField(auto_now_add=True, 
                                      verbose_name='Creation date', 
                                      null=True)),
                ('device_id', 
                 models.UUIDField(help_text='UDID / '
                                            'UIDevice.'
                                            'identifierForVendor()', 
                                  max_length=32, 
                                  null=True, 
                                  verbose_name='Device ID', 
                                  blank=True, 
                                  db_index=True)),
                ('registration_id', 
                 models.CharField(unique=True, max_length=64, 
                                  verbose_name='Registration ID')),
                ('user', 
                 models.ForeignKey(blank=True, 
                                   to=settings.AUTH_USER_MODEL, 
                                   null=True, 
                                   on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'APNS device',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GCMDevice',
            fields=[
                ('id', 
                 models.AutoField(verbose_name='ID', 
                                  serialize=False, 
                                  auto_created=True, 
                                  primary_key=True)),
                ('name', 
                 models.CharField(max_length=255, 
                                  null=True, 
                                  verbose_name='Name', 
                                  blank=True)),
                ('active', 
                 models.BooleanField(default=True, 
                                     help_text='Inactive devices '
                                               'will not be sent '
                                               'notifications', 
                                     verbose_name='Is active')),
                ('date_created', 
                 models.DateTimeField(auto_now_add=True, 
                                      verbose_name='Creation date', 
                                      null=True)),
                ('device_id', 
                 push_notifications.fields.HexIntegerField(\
                   help_text='ANDROID_ID / TelephonyManager.'
                             'getDeviceId() (always as hex)', 
                   null=True, verbose_name='Device ID', 
                   blank=True, db_index=True)),
~~                ('registration_id', 
~~                 models.TextField(verbose_name='Registration ID')),
                ('user', 
                 models.ForeignKey(blank=True, 
                                   to=settings.AUTH_USER_MODEL, 
                                   null=True, 
                                   on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'GCM device',
            },
            bases=(models.Model,),
        ),
    ]
```
