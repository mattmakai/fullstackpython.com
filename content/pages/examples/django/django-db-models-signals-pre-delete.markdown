title: django.db.models.signals pre_delete Example Code
category: page
slug: django-db-models-signals-pre-delete-examples
sortorder: 500011250
toc: False
sidebartitle: django.db.models.signals pre_delete
meta: Python example code for the pre_delete callable from the django.db.models.signals module of the Django project.


pre_delete is a callable within the django.db.models.signals module of the Django project.


## Example 1 from wagtail
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
    post_save.connect(post_save_site_signal_handler, sender=Site)
    post_delete.connect(post_delete_site_signal_handler, sender=Site)

~~    pre_delete.connect(pre_delete_page_unpublish, sender=Page)
    post_delete.connect(post_delete_page_log_deletion, sender=Page)



## ... source file continues with no further pre_delete examples...

```

