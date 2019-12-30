title: django.db.models FileField Example Code
category: page
slug: django-db-models-filefield-examples
sortorder: 500012830
toc: False
sidebartitle: django.db.models FileField
meta: Python code examples for the FileField class used in the Django ORM, found within the django.db.models module of the Django project. 


[FileField](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
is a [Django ORM](/django-orm.html) field-to-column mapping for
uploading files from the client to the [Django](/django.html)
application.

`FileField` is defined within the 
[django.db.models.fields](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
module but is typically referenced from
[django.db.models](https://github.com/django/django/tree/master/django/db/models)
rather than including the `fields` module reference.


## Example 1 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / submissions / models.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/submissions/models.py)

```python
import os

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
~~from django.db import models

from conferences.models import Topic, SubmissionType, Conference

User = get_user_model()


TITLE_MAX_LENGTH = 250
ABSTRACT_MAX_LENGTH = 2500  # 250 words


def get_review_manuscript_full_path(instance, filename):
    ext = filename.split('.')[-1]
    root = settings.MEDIA_PRIVATE_ROOT
    cpk = instance.conference.pk if instance.conference else 'unknown_conf'
    path = f'{root}/{cpk}/submissions'
    name = f'SID{instance.pk:05d}'
    return f'{path}/{name}.{ext}'


class Submission(models.Model):
    SUBMITTED = 'SUBMIT'
    UNDER_REVIEW = 'REVIEW'
    REJECTED = 'REJECT'
    ACCEPTED = 'ACCEPT'
    IN_PRINT = 'PRINT'
    PUBLISHED = 'PUBLISH'

    STATUS_CHOICE = (
        (SUBMITTED, _('Submitted')),
        (UNDER_REVIEW, _('Review')),
        (REJECTED, _('Rejected')),
        (ACCEPTED, _('Accepted')),
        (IN_PRINT, _('In-print')),
        (PUBLISHED, _('Published')),
    )

    conference = models.ForeignKey(
        Conference,
        on_delete=models.SET_NULL,
        null=True,
    )

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        default="",
        verbose_name=_('Title'),
    )

    abstract = models.CharField(
        max_length=ABSTRACT_MAX_LENGTH,
        default="",
        verbose_name=_('Abstract'),
    )

    topics = models.ManyToManyField(
        Topic,
        verbose_name=_('Topics'),
    )

    stype = models.ForeignKey(
        SubmissionType,
        related_name='submissions',
        verbose_name=_('Submission type'),
        on_delete=models.SET_NULL,
        null=True,
    )

    status = models.CharField(
        choices=STATUS_CHOICE,
        default='SUBMIT',
        max_length=10,
    )

~~    review_manuscript = models.FileField(
~~        upload_to=get_review_manuscript_full_path,
~~        blank=True,
~~    )


## ... source file continues with no further examples ...
```


## Example 2 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / images / signal_handlers.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/images/signal_handlers.py)

```python
from django.conf import settings
~~from django.db import transaction
from django.db.models.signals import post_delete, pre_save

from wagtail.images import get_image_model


~~def post_delete_file_cleanup(instance, **kwargs):
~~    # Pass false so FileField doesn't save the model.
~~    transaction.on_commit(lambda: instance.file.delete(False))


def pre_save_image_feature_detection(instance, **kwargs):
    if getattr(settings, 'WAGTAILIMAGES_FEATURE_DETECTION_ENABLED', False):
        # Make sure the image doesn't already have a focal point
        if not instance.has_focal_point():
            # Set the focal point
            instance.set_focal_point(instance.get_suggested_focal_point())


def register_signal_handlers():
    Image = get_image_model()
    Rendition = Image.get_rendition_model()

    pre_save.connect(pre_save_image_feature_detection, sender=Image)
    post_delete.connect(post_delete_file_cleanup, sender=Image)
    post_delete.connect(post_delete_file_cleanup, sender=Rendition)

```

