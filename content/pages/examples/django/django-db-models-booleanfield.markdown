title: django.db.models BooleanField Example Code
category: page
slug: django-db-models-booleanfield-examples
sortorder: 50103
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

## source file continues here without further BooleanField examples
```
