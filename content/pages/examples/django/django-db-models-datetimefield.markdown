title: django.db.models DateTimeField Example Code
category: page
slug: django-db-models-datetimefield-examples
sortorder: 500012825
toc: False
sidebartitle: django.db.models DateTimeField
meta: Python code examples for the DateTimeField class provided by the Django ORM. DateTimeField is found within the django.db.models module.


[DateTimeField](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
is a frequently-used attribute on 
[Model](/django-db-models-model-examples.html) classes when defining
date- and time-based [database columns](/databases.html) with
the [Django ORM](/django-orm.html).

The [Django](/django.html) project has great documentation for
[DateTimeField](https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.DateTimeField)
and all of the other column fields.

Note that `DateTimeField` is defined within the 
[django.db.models.fields](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
module but is typically referenced from
[django.db.models](https://github.com/django/django/tree/master/django/db/models)
rather than including the `fields` module reference.


## Example 1 from django-push-notifications
[django-push-notifications](https://github.com/jazzband/django-push-notifications)
is a [Django](/django.html) app for storing and interacting with
push notification services such as 
[Google's Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/)
and 
[Apple Notifications](https://developer.apple.com/notifications/).
The django-push-notification project's source code is available
open source under the 
[MIT license](https://github.com/jazzband/django-push-notifications/blob/master/LICENSE).

[**django-push-notifications / push_notifications / models.py**](


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
    active = models.BooleanField(
        verbose_name=_("Is active"), default=True,
        help_text=_("Inactive devices will not be sent notifications")
    )
    user = models.ForeignKey(
        SETTINGS["USER_MODEL"], blank=True, null=True, 
        on_delete=models.CASCADE
    )
~~    date_created = models.DateTimeField(
~~        verbose_name=_("Creation date"), auto_now_add=True, null=True
~~    )
    application_id = models.CharField(
        max_length=64, verbose_name=_("Application ID"),
        help_text=_(
            "Opaque application identity, should be filled in for"
            " multiple key/certificate access"
        ),
        blank=True, null=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return (
            self.name or
            str(self.device_id or "") or
            "%s for %s" % (self.__class__.__name__, 
                           self.user or "unknown user")
        )

## source code continues here without further DateTimeField examples
```


## Example 2 from AuditLog
[Auditlog](https://github.com/jjkester/django-auditlog) 
([project documentation](https://django-auditlog.readthedocs.io/en/latest/))
is a [Django](/django.html) app that logs changes to Python objects,
similar to the Django admin's logs but with more details and
output formats. Auditlog's source code is provided as open source under the
[MIT license](https://github.com/jjkester/django-auditlog/blob/master/LICENSE).

[**django-auditlog / src / auditlog / diff.py**](https://github.com/jjkester/django-auditlog/blob/master/src/auditlog/diff.py)

```python
from __future__ import unicode_literals

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
~~from django.db.models import Model, NOT_PROVIDED, DateTimeField
from django.utils import timezone
from django.utils.encoding import smart_text


def track_field(field):
    """
    Returns whether the given field should be tracked by Auditlog.
    Untracked fields are many-to-many relations and relations to 
    the Auditlog LogEntry model.
    :param field: The field to check.
    :type field: Field
    :return: Whether the given field should be tracked.
    :rtype: bool
    """
    from auditlog.models import LogEntry
    # Do not track many to many relations
    if field.many_to_many:
        return False

    # Do not track relations to LogEntry
    if getattr(field, 'remote_field', None) is not None and \
        field.remote_field.model == LogEntry:
        return False

    # 1.8 check
    elif getattr(field, 'rel', None) is not None and \
        field.rel.to == LogEntry:
        return False

    return True


def get_fields_in_model(instance):
    """
    Returns the list of fields in the given model instance. 
    Checks whether to use the official _meta API or use the raw
    data. This method excludes many to many fields.
    :param instance: The model instance to get the fields for
    :type instance: Model
    :return: The list of fields for the given model (instance)
    :rtype: list
    """
    assert isinstance(instance, Model)

    # Check if the Django 1.8 _meta API is available
    use_api = hasattr(instance._meta, 'get_fields') and \
              callable(instance._meta.get_fields)

    if use_api:
        return [f for f in instance._meta.get_fields() if track_field(f)]
    return instance._meta.fields


def get_field_value(obj, field):
    """
    Gets the value of a given model instance field.
    :param obj: The model instance.
    :type obj: Model
    :param field: The field you want to find the value of.
    :type field: Any
    :return: The value of the field as a string.
    :rtype: str
    """
~~    if isinstance(field, DateTimeField):
~~        # DateTimeFields are timezone-aware, so we need 
~~        # to convert the field to its naive form before we 
~~        # can accuratly compare them for changes.
~~        try:
~~            value = field.to_python(getattr(obj, field.name, 
~~                                    None))
~~            if value is not None and settings.USE_TZ and \
~~                not timezone.is_naive(value):
~~                value = timezone.make_naive(value, 
~~                                            timezone=timezone.utc)
~~        except ObjectDoesNotExist:
~~            value = field.default if field.default \
~~                is not NOT_PROVIDED else None
    else:
        try:
            value = smart_text(getattr(obj, field.name, None))
        except ObjectDoesNotExist:
            value = field.default if field.default \
                is not NOT_PROVIDED else None

    return value

## ... source file continues here without further DateTime examples ...
```
