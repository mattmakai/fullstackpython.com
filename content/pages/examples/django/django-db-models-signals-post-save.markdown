title: django.db.models.signals post_save Example Code
category: page
slug: django-db-models-signals-post-save-examples
sortorder: 500011249
toc: False
sidebartitle: django.db.models.signals post_save
meta: Python example code for the post_save callable from the django.db.models.signals module of the Django project.


post_save is a callable within the django.db.models.signals module of the Django project.


## Example 1 from django-model-utils
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


## ... source file abbreviated to get to post_save examples ...



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
            pre_save.send(
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
~~            post_save.send(
                sender=origin, instance=self, created=(not updated),
                update_fields=update_fields, raw=raw, using=using,
            )

        self.signals_to_disable = []



## ... source file continues with no further post_save examples...

```


## Example 2 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / core / signal_handlers.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/core/signal_handlers.py)

```python
# signal_handlers.py
import logging

from django.core.cache import cache
~~from django.db.models.signals import post_delete, post_save, pre_delete

from wagtail.core.models import Page, Site

logger = logging.getLogger('wagtail.core')


def post_save_site_signal_handler(instance, update_fields=None, **kwargs):
    cache.delete('wagtail_site_root_paths')


def post_delete_site_signal_handler(instance, **kwargs):
    cache.delete('wagtail_site_root_paths')


def pre_delete_page_unpublish(sender, instance, **kwargs):
    if instance.live:
        instance.unpublish(commit=False)


def post_delete_page_log_deletion(sender, instance, **kwargs):
    logger.info("Page deleted: \"%s\" id=%d", instance.title, instance.id)


def register_signal_handlers():
~~    post_save.connect(post_save_site_signal_handler, sender=Site)
    post_delete.connect(post_delete_site_signal_handler, sender=Site)

    pre_delete.connect(pre_delete_page_unpublish, sender=Page)
    post_delete.connect(post_delete_page_log_deletion, sender=Page)



## ... source file continues with no further post_save examples...

```

