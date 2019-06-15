title: django.db.models.Model Examples
category: page
slug: django-db-models-model-examples
sortorder: 50002
toc: False
sidebartitle: django.db.models.Model
meta: Python code examples for the Model class within the django.db.models module of the Django project. 


# django.db.models.Model Examples
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

[**django-audit-log/audit-log/models/__init__.py**](https://github.com/vvangelovski/django-audit-log/blob/master/audit_log/models/__init__.py)

```python
~~from django.db.models import Model
from django.utils.translation import ugettext_lazy as _
from audit_log.models.fields import CreatingUserField, CreatingSessionKeyField, LastUserField, LastSessionKeyField

~~class AuthStampedModel(Model):
    """
    An abstract base class model that provides auth and session information
    fields.
    """
    created_by = CreatingUserField(verbose_name = _("created by"), related_name = "created_%(app_label)s_%(class)s_set")
    created_with_session_key = CreatingSessionKeyField(_("created with session key"))
    modified_by =  LastUserField(verbose_name = _("modified by"), related_name = "modified_%(app_label)s_%(class)s_set")
    modified_with_session_key = LastSessionKeyField(_("modified with session key"))

    class Meta:
        abstract = True
```


## Example 2 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) 
[code library](https://pypi.org/project/django-cms/) 
for use with Django web apps that is open sourced under the 
[BSD 3-Clause "New" License](https://github.com/divio/django-cms/blob/develop/LICENSE).

```python
@python_2_unicode_compatible
class Page(models.Model):
    """
    A simple hierarchical page model
    """
    LIMIT_VISIBILITY_IN_MENU_CHOICES = (
        (constants.VISIBILITY_USERS, _('for logged in users only')),
        (constants.VISIBILITY_ANONYMOUS, _('for anonymous users only')),
    )
    TEMPLATE_DEFAULT = TEMPLATE_INHERITANCE_MAGIC if get_cms_setting('TEMPLATE_INHERITANCE') else get_cms_setting('TEMPLATES')[0][0]

    X_FRAME_OPTIONS_INHERIT = constants.X_FRAME_OPTIONS_INHERIT
    X_FRAME_OPTIONS_DENY = constants.X_FRAME_OPTIONS_DENY
    X_FRAME_OPTIONS_SAMEORIGIN = constants.X_FRAME_OPTIONS_SAMEORIGIN
    X_FRAME_OPTIONS_ALLOW = constants.X_FRAME_OPTIONS_ALLOW
    X_FRAME_OPTIONS_CHOICES = (
        (constants.X_FRAME_OPTIONS_INHERIT, _('Inherit from parent page')),
        (constants.X_FRAME_OPTIONS_DENY, _('Deny')),
        (constants.X_FRAME_OPTIONS_SAMEORIGIN, _('Only this website')),
        (constants.X_FRAME_OPTIONS_ALLOW, _('Allow'))
    )

    template_choices = [(x, _(y)) for x, y in get_cms_setting('TEMPLATES')]

    created_by = models.CharField(
        _("created by"), max_length=constants.PAGE_USERNAME_MAX_LENGTH,
        editable=False)
    changed_by = models.CharField(
        _("changed by"), max_length=constants.PAGE_USERNAME_MAX_LENGTH,
        editable=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    changed_date = models.DateTimeField(auto_now=True)

    publication_date = models.DateTimeField(_("publication date"), null=True, blank=True, help_text=_(
        'When the page should go live. Status must be "Published" for page to go live.'), db_index=True)
    publication_end_date = models.DateTimeField(_("publication end date"), null=True, blank=True,
                                                help_text=_('When to expire the page. Leave empty to never expire.'),
                                                db_index=True)
    #
    # Please use toggle_in_navigation() instead of affecting this property
    # directly so that the cms page cache can be invalidated as appropriate.
    #
    in_navigation = models.BooleanField(_("in navigation"), default=True, db_index=True)
    soft_root = models.BooleanField(_("soft root"), db_index=True, default=False,
                                    help_text=_("All ancestors will not be displayed in the navigation"))
    reverse_id = models.CharField(_("id"), max_length=40, db_index=True, blank=True, null=True, help_text=_(
        "A unique identifier that is used with the page_url templatetag for linking to this page"))
    navigation_extenders = models.CharField(_("attached menu"), max_length=80, db_index=True, blank=True, null=True)
    template = models.CharField(_("template"), max_length=100, choices=template_choices,
                                help_text=_('The template used to render the content.'),
                                default=TEMPLATE_DEFAULT)

    login_required = models.BooleanField(_("login required"), default=False)
    limit_visibility_in_menu = models.SmallIntegerField(_("menu visibility"), default=None, null=True, blank=True,
                                                        choices=LIMIT_VISIBILITY_IN_MENU_CHOICES, db_index=True,
                                                        help_text=_("limit when this page is visible in the menu"))
    is_home = models.BooleanField(editable=False, db_index=True, default=False)
    application_urls = models.CharField(_('application'), max_length=200, blank=True, null=True, db_index=True)
    application_namespace = models.CharField(_('application instance name'), max_length=200, blank=True, null=True)

    # Placeholders (plugins)
    placeholders = models.ManyToManyField('cms.Placeholder', editable=False)

    # Publisher fields
    publisher_is_draft = models.BooleanField(default=True, editable=False, db_index=True)
    # This is misnamed - the one-to-one relation is populated on both ends
    publisher_public = models.OneToOneField(
        'self',
        on_delete=models.CASCADE,
        related_name='publisher_draft',
        null=True,
        editable=False,
    )
    languages = models.CharField(max_length=255, editable=False, blank=True, null=True)

    # X Frame Options for clickjacking protection
    xframe_options = models.IntegerField(
        choices=X_FRAME_OPTIONS_CHOICES,
        default=get_cms_setting('DEFAULT_X_FRAME_OPTIONS'),
    )

    # Flag that marks a page as page-type
    is_page_type = models.BooleanField(default=False)

    node = models.ForeignKey(
        TreeNode,
        related_name='cms_pages',
        on_delete=models.CASCADE,
    )
```


## Example 3 from

## Example 4 from mezzanine


[**mezzanine/mezzanine/core/models.py**](https://github.com/stephenmcd/mezzanine/blob/master/mezzanine/core/models.py)

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

