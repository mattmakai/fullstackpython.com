title: django.db.models Model Example Code
category: page
slug: django-db-models-model-examples
sortorder: 500012875
toc: False
sidebartitle: django.db.models Model
meta: Python code examples for the Model class within the django.db.models module of the Django project. 


The 
[Model](https://github.com/django/django/blob/master/django/db/models/base.py)
class is the superclass for all data stored in [Django](/django.html) 
applications.


## Example 1 from django-audit-log
[django-audit-log](https://github.com/vvangelovski/django-audit-log) is a
[code library](https://pypi.org/project/django-audit-log/) that tracks 
changes to [Django](/django.html) models. The source code is available 
under the 
[BSD 3 "New" license](https://github.com/vvangelovski/django-audit-log/blob/master/LICENSE.txt).

[**django-audit-log / audit-log / models / __init__.py**](https://github.com/vvangelovski/django-audit-log/blob/master/audit_log/models/__init__.py)

```python
# __init__.py
~~from django.db.models import Model
from django.utils.translation import ugettext_lazy as _
from audit_log.models.fields import (CreatingUserField, CreatingSessionKeyField, 
                                     LastUserField, LastSessionKeyField)


~~class AuthStampedModel(Model):
~~    """An abstract base class model that provides auth and session information
~~    fields.
~~    """
~~    created_by = CreatingUserField(verbose_name = _("created by"), 
~~                                   related_name = "created_%(app_label)s_%(class)s_set")
~~    created_with_session_key = CreatingSessionKeyField(_("created with session key"))
~~    modified_by = LastUserField(verbose_name = _("modified by"), 
~~                                related_name = "modified_%(app_label)s_%(class)s_set")
~~    modified_with_session_key = LastSessionKeyField(_("modified with session key"))
~~
~~    class Meta:
~~        abstract = True
```


## Example 2 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) 
[code library](https://pypi.org/project/django-cms/) 
for use with Django web apps that is open sourced under the 
[BSD 3-Clause "New" License](https://github.com/divio/django-cms/blob/develop/LICENSE).

[**django-cms / cms / models / permisssionmodels.py**](https://github.com/divio/django-cms/blob/develop/cms/models/pagemodel.py)

```python
# -*- coding: utf-8 -*-
from django.apps import apps
~~from django.db import models
from django.conf import settings
~~from django.contrib.auth.models import Group, UserManager
~~from django.contrib.sites.models import Site
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.utils.encoding import force_text, python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

~~from cms.models import Page
~~from cms.models.managers import (PagePermissionManager,
~~                                 GlobalPagePermissionManager)
from cms.utils.compat import DJANGO_1_11


# Cannot use contrib.auth.get_user_model() at compile time.
user_app_name, user_model_name = settings.AUTH_USER_MODEL.rsplit('.', 1)
User = None
try:
    User = apps.get_registered_model(user_app_name, user_model_name)
except KeyError:
    pass
if User is None:
    raise ImproperlyConfigured(
        "You have defined a custom user model %s, but the app %s is not "
        "in settings.INSTALLED_APPS" % (settings.AUTH_USER_MODEL, user_app_name)
    )


# NOTE: those are not just numbers!! we will do binary AND on them,
# so pay attention when adding/changing them, or MASKs..
ACCESS_PAGE = 1
ACCESS_CHILDREN = 2  # just immediate children (1 level)
ACCESS_PAGE_AND_CHILDREN = 3  # just immediate children (1 level)
ACCESS_DESCENDANTS = 4
ACCESS_PAGE_AND_DESCENDANTS = 5

# binary masks for ACCESS permissions
MASK_PAGE = 1
MASK_CHILDREN = 2
MASK_DESCENDANTS = 4

ACCESS_CHOICES = (
    (ACCESS_PAGE, _('Current page')),
    (ACCESS_CHILDREN, _('Page children (immediate)')),
    (ACCESS_PAGE_AND_CHILDREN, _('Page and children (immediate)')),
    (ACCESS_DESCENDANTS, _('Page descendants')),
    (ACCESS_PAGE_AND_DESCENDANTS, _('Page and descendants')),
)


~~class AbstractPagePermission(models.Model):
    """Abstract page permissions
    """

    # who:
~~    user = models.ForeignKey(
~~        settings.AUTH_USER_MODEL,
~~        on_delete=models.CASCADE,
~~        verbose_name=_("user"),
~~        blank=True,
~~        null=True,
~~    )
~~    group = models.ForeignKey(
~~        Group,
~~        on_delete=models.CASCADE,
~~        verbose_name=_("group"),
~~        blank=True,
~~        null=True,
~~    )

    # what:
~~    can_change = models.BooleanField(_("can edit"), default=True)
~~    can_add = models.BooleanField(_("can add"), default=True)
~~    can_delete = models.BooleanField(_("can delete"), default=True)
~~    can_change_advanced_settings = models.BooleanField(_(\
~~          "can change advanced settings"), 
                                                         default=False)
~~    can_publish = models.BooleanField(_("can publish"), default=True)
~~    can_change_permissions = models.BooleanField(_("can change permissions"), 
                                                   default=False, 
                                                   help_text=_("on page level"))
~~    can_move_page = models.BooleanField(_("can move"), default=True)
~~    can_view = models.BooleanField(_("view restricted"), default=False, 
                                     help_text=_("frontend view restriction"))
~~
~~    class Meta:
~~        abstract = True
~~        app_label = 'cms'

    def clean(self):
        super(AbstractPagePermission, self).clean()

        if not self.user and not self.group:
            raise ValidationError(_('Please select user or group.'))

        if self.can_change:
            return

        if self.can_add:
            message = _("Users can't create a page without permissions "
                        "to change the created page. Edit permissions required.")
            raise ValidationError(message)

        if self.can_delete:
            message = _("Users can't delete a page without permissions "
                        "to change the page. Edit permissions required.")
            raise ValidationError(message)

        if self.can_publish:
            message = _("Users can't publish a page without permissions "
                        "to change the page. Edit permissions required.")
            raise ValidationError(message)

        if self.can_change_advanced_settings:
            message = _("Users can't change page advanced settings without permissions "
                        "to change the page. Edit permissions required.")
            raise ValidationError(message)

        if self.can_change_permissions:
            message = _("Users can't change page permissions without permissions "
                        "to change the page. Edit permissions required.")
            raise ValidationError(message)

        if self.can_move_page:
            message = _("Users can't move a page without permissions "
                        "to change the page. Edit permissions required.")
            raise ValidationError(message)

    @property
    def audience(self):
        """Return audience by priority, so: All or User, Group
        """
        targets = filter(lambda item: item, (self.user, self.group,))
        return ", ".join([force_text(t) for t in targets]) or 'No one'

    def save(self, *args, **kwargs):
        if not self.user and not self.group:
            # don't allow `empty` objects
            return
        return super(AbstractPagePermission, self).save(*args, **kwargs)

    def get_configured_actions(self):
        actions = [action for action in self.get_permissions_by_action()
                   if self.has_configured_action(action)]
        return actions

    def has_configured_action(self, action):
        permissions = self.get_permissions_by_action()[action]
        return all(getattr(self, perm) for perm in permissions)

    @classmethod
    def get_all_permissions(cls):
        perms = [
            'can_add',
            'can_change',
            'can_delete',
            'can_publish',
            'can_change_advanced_settings',
            'can_change_permissions',
            'can_move_page',
            'can_view',
        ]
        return perms

    @classmethod
    def get_permissions_by_action(cls):
        # Maps an action to the required flags on the
        # PagePermission model or GlobalPagePermission model
        permissions_by_action = {
            'add_page': ['can_add', 'can_change'],
            'change_page': ['can_change'],
            'change_page_advanced_settings': ['can_change', 
                                              'can_change_advanced_settings'],
            'change_page_permissions': ['can_change', 'can_change_permissions'],
            'delete_page': ['can_change', 'can_delete'],
            'delete_page_translation': ['can_change', 'can_delete'],
            'move_page': ['can_change', 'can_move_page'],
            'publish_page': ['can_change', 'can_publish'],
            'view_page': ['can_view'],
        }
        return permissions_by_action
```


## Example 3 from dccnconf
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration 
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnconf / wwwdccn / conferences / models.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/conferences/models.py)

```python
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
~~from django.db import models

# Create your models here.
from django_countries.fields import CountryField


~~User = get_user_model()


~~class Conference(models.Model):
~~    full_name = models.CharField(
~~        max_length=300, verbose_name=_('Full name of the conference')
~~    )
~~
~~    short_name = models.CharField(
~~        max_length=30, verbose_name=_('Short name of the conference')
~~    )
~~
~~    is_ieee = models.BooleanField(
~~        default=False, verbose_name=_('The conference is supported by IEEE')
~~    )
~~
~~    country = CountryField(null=True, verbose_name=_('Country'))
~~
~~    city = models.CharField(
~~        max_length=100, verbose_name=_('City')
~~    )
~~
~~    start_date = models.DateField(null=True, verbose_name=_('Opens at'))
~~    close_date = models.DateField(null=True, verbose_name=_('Closes at'))
~~
~~    chairs = models.ManyToManyField(User, related_name='chaired_conferences')
~~
~~    creator = models.ForeignKey(
~~        User, null=True, blank=True, on_delete=models.SET_NULL,
~~        related_name='created_conferences'
~~    )
~~
~~    logotype = models.ImageField(
~~        verbose_name=_("Conference logotype"),
~~        upload_to=f'{settings.MEDIA_PUBLIC_ROOT}/conferences/logo/',
~~        null=True, blank=True
~~    )
~~
~~    description = models.TextField(
~~        verbose_name=_('Medium length description of the conference'),
~~        default="",
~~        blank=True,
~~    )
~~
~~    site_url = models.URLField(
~~        verbose_name=_('Conference informational site'),
~~        default="",
~~        blank=True,
~~    )
~~
~~    def __str__(self):
~~        return f'{self.full_name} ({self.short_name})'


~~class SubmissionStage(models.Model):
~~    conference = models.OneToOneField(
~~        Conference, on_delete=models.CASCADE, related_name='submission_stage'
~~    )
~~
~~    end_date = models.DateTimeField(
~~        null=True, verbose_name=_('Deadline for submissions')
~~    )
~~
~~    end_date_description = models.CharField(blank=True, max_length=100)


~~class ReviewStage(models.Model):
~~    conference = models.OneToOneField(
~~        Conference, on_delete=models.CASCADE, related_name='review_stage'
~~    )
~~
~~    end_date = models.DateTimeField(
~~        null=True, verbose_name=_('End of review')
~~    )


~~class ProceedingType(models.Model):
~~    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
~~
~~    name = models.CharField(
~~        max_length=100, verbose_name=_('Short name')
~~    )
~~
~~    description = models.CharField(
~~        max_length=1000, verbose_name=_('Long description')
~~    )
~~
~~    final_manuscript_deadline = models.DateTimeField(
~~        null=True, verbose_name=_('Deadline for final manuscript submission')
~~    )
~~
~~    min_num_pages = models.IntegerField(
~~        default=4, verbose_name=_('Minimum number of pages in submission')
~~    )
~~
~~    max_num_pages = models.IntegerField(
~~        default=4, verbose_name=_('Maximum number of pages in submission')
~~    )
~~
~~    final_latex_template = models.FileField(
~~        null=True, blank=True,
~~        verbose_name=_('LaTeX template for final manuscript'),
~~        upload_to=f'{settings.MEDIA_PUBLIC_ROOT}/conferences/templates'
~~    )
~~
~~    _final_latex_template_version = models.IntegerField(default=1)
~~
~~    def __str__(self):
~~        return self.name


~~class SubmissionType(models.Model):
~~    LANGUAGES = (
~~        (None, _('Select submission language')),
~~        ('RU', _('Russian')),
~~        ('EN', _('English')),
~~    )
~~
~~    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
~~
~~    name = models.CharField(
~~        max_length=100, verbose_name=_('Short name')
~~    )
~~
~~    description = models.CharField(
~~        max_length=1000, verbose_name=_('Long description')
~~    )
~~
~~    language = models.TextField(max_length=2, choices=LANGUAGES)
~~
~~    latex_template = models.FileField(
~~        null=True, verbose_name=_('LaTeX template'),
~~        upload_to=f'{settings.MEDIA_PUBLIC_ROOT}/conferences/templates'
~~    )
~~
~~    _latex_template_version = models.IntegerField(default=1)
~~
~~    num_reviews = models.IntegerField(
~~        default=2, verbose_name=_('Number of reviews per submission')
~~    )
~~
~~    min_num_pages = models.IntegerField(
~~        default=4, verbose_name=_('Minimum number of pages in submission')
~~    )
~~
~~    max_num_pages = models.IntegerField(
~~        default=4, verbose_name=_('Maximum number of pages in submission')
~~    )
~~
~~    blind_review = models.BooleanField(
~~        default=False, verbose_name=_('Blind review')
~~    )
~~
~~    possible_proceedings = models.ManyToManyField(ProceedingType)
~~
~~    def __str__(self):
~~        return self.name


~~class Topic(models.Model):
~~    class Meta:
~~        ordering = ['order']
~~
~~    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
~~
~~    name = models.CharField(max_length=250, verbose_name=_('Topic name'))
~~    order = models.IntegerField(default=0)
~~
~~    def __str__(self):
~~        return f'{self.name}'


# source file continues from here without further Model examples
```


## Example 4 from mezzanine
[mezzanine](https://github.com/stephenmcd/mezzanine) is a 
[Django](/django.html)-based CMS with open source code under the
[BSD 2-Clause "Simplified" License](https://github.com/stephenmcd/mezzanine/blob/master/LICENSE).

[**mezzanine / mezzanine / core / models.py**](https://github.com/stephenmcd/mezzanine/blob/master/mezzanine/core/models.py)

```python
from __future__ import unicode_literals
from future.builtins import str
from future.utils import with_metaclass

from json import loads
try:
    from urllib.request import urlopen
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlopen, urlencode

from django.apps import apps
from django.contrib.contenttypes.fields import GenericForeignKey
~~from django.db import models
from django.db.models.base import ModelBase
from django.template.defaultfilters import truncatewords_html
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import format_html, strip_tags
from django.utils.timesince import timesince
from django.utils.timezone import now
from django.utils.translation import ugettext, ugettext_lazy as _

from mezzanine.conf import settings
from mezzanine.core.fields import RichTextField, OrderField
from mezzanine.core.managers import DisplayableManager, CurrentSiteManager
from mezzanine.generic.fields import KeywordsField
from mezzanine.utils.html import TagCloser
from mezzanine.utils.models import base_concrete_model, get_user_model_name
from mezzanine.utils.sites import current_site_id, current_request
from mezzanine.utils.urls import admin_url, slugify, unique_slug


user_model_name = get_user_model_name()


def wrapped_manager(klass):
    if settings.USE_MODELTRANSLATION:
        from modeltranslation.manager import MultilingualManager

        class Mgr(MultilingualManager, klass):
            pass
        return Mgr()
    else:
        return klass()


~~class SiteRelated(models.Model):
    """
    Abstract model for all things site-related. Adds a foreignkey to
    Django's ``Site`` model, and filters by site with all querysets.
    See ``mezzanine.utils.sites.current_site_id`` for implementation
    details.
    """

    objects = wrapped_manager(CurrentSiteManager)

    class Meta:
        abstract = True

~~    site = models.ForeignKey("sites.Site", on_delete=models.CASCADE,
~~        editable=False)

    def save(self, update_site=False, *args, **kwargs):
        """
        Set the site to the current site when the record is first
        created, or the ``update_site`` argument is explicitly set
        to ``True``.
        """
        if update_site or (self.id is None and self.site_id is None):
            self.site_id = current_site_id()
        super(SiteRelated, self).save(*args, **kwargs)
```


## Example 5 from sorl-thumbnail
[sorl-thumbnail](https://github.com/jazzband/sorl-thumbnail)
([project documentation](https://sorl-thumbnail.readthedocs.io/en/latest/))
is a code library to make it easier to work with thumbnails
in [Django](/django.html) applications. The code for the 
project is open source under the
[BSD 3-Clause "New" or "Revised" license](https://github.com/jazzband/sorl-thumbnail/blob/master/LICENSE).

[**sorl-thumbnail / sorl / thumbnail / models.py**](https://github.com/jazzband/sorl-thumbnail/blob/master/sorl/thumbnail/models.py)

```python
# models.py
~~from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from sorl.thumbnail.conf import settings


@python_2_unicode_compatible
~~class KVStore(models.Model):
~~    key = models.CharField(
~~        max_length=200, primary_key=True,
~~        db_column=settings.THUMBNAIL_KEY_DBCOLUMN
~~    )
~~    value = models.TextField()

    def __str__(self):
        return self.key
```


## Example 6 from django-push-notifications
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
~~class Device(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"),
                            blank=True, null=True)
    active = models.BooleanField(
        verbose_name=_("Is active"), default=True,
        help_text=_("Inactive devices will" 
                    " not be sent notifications")
    )
    user = models.ForeignKey(
        SETTINGS["USER_MODEL"], blank=True, null=True, 
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(
        verbose_name=_("Creation date"), auto_now_add=True, 
        null=True
    )
    application_id = models.CharField(
        max_length=64, verbose_name=_("Application ID"),
        help_text=_(
            "Opaque application identity, "
            "should be filled in for multiple"
            " key/certificate access"
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

# code continues on from here without further examples
```
