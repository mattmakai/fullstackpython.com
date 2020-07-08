title: django.db.models.signals pre_save Example Code
category: page
slug: django-db-models-signals-pre-save-examples
sortorder: 500011251
toc: False
sidebartitle: django.db.models.signals pre_save
meta: Python example code for the pre_save callable from the django.db.models.signals module of the Django project.


pre_save is a callable within the django.db.models.signals module of the Django project.


## Example 1 from AuditLog
[Auditlog](https://github.com/jjkester/django-auditlog)
([project documentation](https://django-auditlog.readthedocs.io/en/latest/))
is a [Django](/django.html) app that logs changes to Python objects,
similar to the Django admin's logs but with more details and
output formats. Auditlog's source code is provided as open source under the
[MIT license](https://github.com/jjkester/django-auditlog/blob/master/LICENSE).

[**AuditLog / src / auditlog / middleware.py**](https://github.com/jjkester/django-auditlog/blob/master/src/auditlog/middleware.py)

```python
# middleware.py
from __future__ import unicode_literals

import threading
import time

from django.conf import settings
~~from django.db.models.signals import pre_save
from django.utils.functional import curry
from django.apps import apps
from auditlog.models import LogEntry
from auditlog.compat import is_authenticated

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


threadlocal = threading.local()


class AuditlogMiddleware(MiddlewareMixin):

    def process_request(self, request):
        threadlocal.auditlog = {
            'signal_duid': (self.__class__, time.time()),
            'remote_addr': request.META.get('REMOTE_ADDR'),
        }

        if request.META.get('HTTP_X_FORWARDED_FOR'):
            threadlocal.auditlog['remote_addr'] = request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0]

        if hasattr(request, 'user') and is_authenticated(request.user):
            set_actor = curry(self.set_actor, user=request.user, signal_duid=threadlocal.auditlog['signal_duid'])
~~            pre_save.connect(set_actor, sender=LogEntry, dispatch_uid=threadlocal.auditlog['signal_duid'], weak=False)

    def process_response(self, request, response):
        if hasattr(threadlocal, 'auditlog'):
~~            pre_save.disconnect(sender=LogEntry, dispatch_uid=threadlocal.auditlog['signal_duid'])

        return response

    def process_exception(self, request, exception):
        if hasattr(threadlocal, 'auditlog'):
~~            pre_save.disconnect(sender=LogEntry, dispatch_uid=threadlocal.auditlog['signal_duid'])

        return None

    @staticmethod
    def set_actor(user, sender, instance, signal_duid, **kwargs):
        if hasattr(threadlocal, 'auditlog'):
            if signal_duid != threadlocal.auditlog['signal_duid']:
                return
            try:
                app_label, model_name = settings.AUTH_USER_MODEL.split('.')
                auth_user_model = apps.get_model(app_label, model_name)
            except ValueError:
                auth_user_model = apps.get_model('auth', 'user')
            if sender == LogEntry and isinstance(user, auth_user_model) and instance.actor is None:
                instance.actor = user

            instance.remote_addr = threadlocal.auditlog['remote_addr']



## ... source file continues with no further pre_save examples...

```


## Example 2 from django-model-utils
[django-model-utils](https://github.com/jazzband/django-model-utils)
([project documentation](https://django-model-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-model-utils/))
provides useful mixins and utilities for working with
[Django ORM](/django-orm.html) models in your projects.

The django-model-utils project is open sourced under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/jazzband/django-model-utils/blob/master/LICENSE.txt).

[**django-model-utils / model_utils / models.py**](https://github.com/jazzband/django-model-utils/blob/master/model_utils/./models.py)

```python
# models.py
from django.core.exceptions import ImproperlyConfigured
from django.db import models, transaction, router
~~from django.db.models.signals import post_save, pre_save
from django.utils.translation import gettext_lazy as _

from model_utils.fields import (
    AutoCreatedField,
    AutoLastModifiedField,
    StatusField,
    MonitorField,
    UUIDField,
)
from model_utils.managers import (
    QueryManager,
    SoftDeletableManager,
)

from django.db.models.functions import Now
now = Now()


class TimeStampedModel(models.Model):
    created = AutoCreatedField(_('created'))
    modified = AutoLastModifiedField(_('modified'))

    def save(self, *args, **kwargs):
        if 'update_fields' in kwargs and 'modified' not in kwargs['update_fields']:


## ... source file abbreviated to get to pre_save examples ...


    class Meta:
        abstract = True


class SaveSignalHandlingModel(models.Model):
    class Meta:
        abstract = True

    def save(self, signals_to_disable=None, *args, **kwargs):

        self.signals_to_disable = signals_to_disable or []

        super().save(*args, **kwargs)

    def save_base(self, raw=False, force_insert=False,
                  force_update=False, using=None, update_fields=None):
        using = using or router.db_for_write(self.__class__, instance=self)
        assert not (force_insert and (force_update or update_fields))
        assert update_fields is None or len(update_fields) > 0
        cls = origin = self.__class__

        if cls._meta.proxy:
            cls = cls._meta.concrete_model
        meta = cls._meta
        if not meta.auto_created and 'pre_save' not in self.signals_to_disable:
~~            pre_save.send(
                sender=origin, instance=self, raw=raw, using=using,
                update_fields=update_fields,
            )
        with transaction.atomic(using=using, savepoint=False):
            if not raw:
                self._save_parents(cls, using, update_fields)
            updated = self._save_table(raw, cls, force_insert, force_update, using, update_fields)

        self._state.db = using
        self._state.adding = False

        if not meta.auto_created and 'post_save' not in self.signals_to_disable:
            post_save.send(
                sender=origin, instance=self, created=(not updated),
                update_fields=update_fields, raw=raw, using=using,
            )

        self.signals_to_disable = []



## ... source file continues with no further pre_save examples...

```


## Example 3 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / images / signal_handlers.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/images/signal_handlers.py)

```python
# signal_handlers.py
from django.conf import settings
from django.db import transaction
~~from django.db.models.signals import post_delete, pre_save

from wagtail.images import get_image_model


def post_delete_file_cleanup(instance, **kwargs):
    transaction.on_commit(lambda: instance.file.delete(False))


def post_delete_purge_rendition_cache(instance, **kwargs):
    instance.purge_from_cache()


def pre_save_image_feature_detection(instance, **kwargs):
    if getattr(settings, 'WAGTAILIMAGES_FEATURE_DETECTION_ENABLED', False):
        if not instance.has_focal_point():
            instance.set_focal_point(instance.get_suggested_focal_point())


def register_signal_handlers():
    Image = get_image_model()
    Rendition = Image.get_rendition_model()

~~    pre_save.connect(pre_save_image_feature_detection, sender=Image)
    post_delete.connect(post_delete_file_cleanup, sender=Image)
    post_delete.connect(post_delete_file_cleanup, sender=Rendition)
    post_delete.connect(post_delete_purge_rendition_cache, sender=Rendition)



## ... source file continues with no further pre_save examples...

```

