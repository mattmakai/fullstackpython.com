title: django.utils.timezone now Example Code
category: page
slug: django-utils-timezone-now-examples
sortorder: 500011496
toc: False
sidebartitle: django.utils.timezone now
meta: Python example code for the now callable from the django.utils.timezone module of the Django project.


now is a callable within the django.utils.timezone module of the Django project.


## Example 1 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / account / utils.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/account/utils.py)

```python
# utils.py
import unicodedata
from collections import OrderedDict
from datetime import timedelta

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import FieldDoesNotExist, ValidationError
from django.db import models
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.utils.encoding import force_str
from django.utils.http import base36_to_int, int_to_base36, urlencode
~~from django.utils.timezone import now

from ..exceptions import ImmediateHttpResponse
from ..utils import (
    get_request_param,
    get_user_model,
    import_callable,
    valid_email_or_none,
)
from . import app_settings, signals
from .adapter import get_adapter
from .app_settings import EmailVerificationMethod


def _unicode_ci_compare(s1, s2):
    norm_s1 = unicodedata.normalize('NFKC', s1).casefold()
    norm_s2 = unicodedata.normalize('NFKC', s2).casefold()
    return norm_s1 == norm_s2


def get_next_redirect_url(request, redirect_field_name="next"):
    redirect_to = get_request_param(request, redirect_field_name)
    if not get_adapter(request).is_safe_url(redirect_to):
        redirect_to = None
    return redirect_to


## ... source file abbreviated to get to now examples ...


        a.user = user
        a.save()
    EmailAddress.objects.fill_cache_for_user(user, addresses)
    if (primary and email and email.lower() != primary.email.lower()):
        user_email(user, primary.email)
        user.save()
    return primary


def send_email_confirmation(request, user, signup=False):
    from .models import EmailAddress, EmailConfirmation

    cooldown_period = timedelta(
        seconds=app_settings.EMAIL_CONFIRMATION_COOLDOWN
    )

    email = user_email(user)
    if email:
        try:
            email_address = EmailAddress.objects.get_for_user(user, email)
            if not email_address.verified:
                if app_settings.EMAIL_CONFIRMATION_HMAC:
                    send_email = True
                else:
                    send_email = not EmailConfirmation.objects.filter(
~~                        sent__gt=now() - cooldown_period,
                        email_address=email_address).exists()
                if send_email:
                    email_address.send_confirmation(request,
                                                    signup=signup)
            else:
                send_email = False
        except EmailAddress.DoesNotExist:
            send_email = True
            email_address = EmailAddress.objects.add_email(request,
                                                           user,
                                                           email,
                                                           signup=signup,
                                                           confirm=True)
            assert email_address
        if send_email:
            get_adapter(request).add_message(
                request,
                messages.INFO,
                'account/messages/'
                'email_confirmation_sent.txt',
                {'email': email})
    if signup:
        get_adapter(request).stash_user(request, user_pk_to_url_str(user))



## ... source file continues with no further now examples...

```


## Example 2 from django-axes
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

[**django-axes / axes / attempts.py**](https://github.com/jazzband/django-axes/blob/master/axes/./attempts.py)

```python
# attempts.py
from logging import getLogger

from django.db.models import QuerySet
~~from django.utils.timezone import datetime, now

from axes.conf import settings
from axes.models import AccessAttempt
from axes.helpers import get_client_username, get_client_parameters, get_cool_off

log = getLogger(settings.AXES_LOGGER)


def get_cool_off_threshold(attempt_time: datetime = None) -> datetime:

    cool_off = get_cool_off()
    if cool_off is None:
        raise TypeError(
            "Cool off threshold can not be calculated with settings.AXES_COOLOFF_TIME set to None"
        )

    if attempt_time is None:
~~        return now() - cool_off
    return attempt_time - cool_off


def filter_user_attempts(request, credentials: dict = None) -> QuerySet:

    username = get_client_username(request, credentials)

    filter_kwargs = get_client_parameters(
        username, request.axes_ip_address, request.axes_user_agent
    )

    return AccessAttempt.objects.filter(**filter_kwargs)


def get_user_attempts(request, credentials: dict = None) -> QuerySet:

    attempts = filter_user_attempts(request, credentials)

    if settings.AXES_COOLOFF_TIME is None:
        log.debug(
            "AXES: Getting all access attempts from database because no AXES_COOLOFF_TIME is configured"
        )
        return attempts



## ... source file continues with no further now examples...

```


## Example 3 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / views.py**](https://github.com/divio/django-cms/blob/develop/cms/./views.py)

```python
# views.py

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login
from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils.cache import patch_cache_control
from django.utils.http import is_safe_url, urlquote
~~from django.utils.timezone import now
from django.utils.translation import get_language_from_request
from django.views.decorators.http import require_POST

from cms.cache.page import get_page_cache
from cms.exceptions import LanguageError
from cms.forms.login import CMSToolbarLoginForm
from cms.models.pagemodel import TreeNode
from cms.page_rendering import _handle_no_page, render_page, render_object_structure, _render_welcome_page
from cms.toolbar.utils import get_toolbar_from_request
from cms.utils import get_current_site
from cms.utils.conf import get_cms_setting
from cms.utils.i18n import (get_fallback_languages, get_public_languages,
                            get_redirect_on_fallback, get_language_list,
                            get_default_language_for_site,
                            is_language_prefix_patterns_used)
from cms.utils.page import get_page_from_request
from cms.utils.page_permissions import user_can_change_page


def _clean_redirect_url(redirect_url, language):
    if (redirect_url and is_language_prefix_patterns_used() and redirect_url[0] == "/"
            and not redirect_url.startswith('/%s/' % language)):
        redirect_url = "/%s/%s" % (language, redirect_url.lstrip("/"))
    return redirect_url


def details(request, slug):
~~    response_timestamp = now()
    if get_cms_setting("PAGE_CACHE") and (
        not hasattr(request, 'toolbar') or (
            not request.toolbar.edit_mode_active and
            not request.toolbar.show_toolbar and
            not request.user.is_authenticated
        )
    ):
        cache_content = get_page_cache(request)
        if cache_content is not None:
            content, headers, expires_datetime = cache_content
            response = HttpResponse(content)
            response.xframe_options_exempt = True
            response._headers = headers
            max_age = int(
                (expires_datetime - response_timestamp).total_seconds() + 0.5)
            patch_cache_control(response, max_age=max_age)
            return response

    site = get_current_site()
    page = get_page_from_request(request, use_path=slug)
    toolbar = get_toolbar_from_request(request)
    tree_nodes = TreeNode.objects.get_for_site(site)

    if not page and not slug and not tree_nodes.exists():


## ... source file continues with no further now examples...

```


## Example 4 from django-downloadview
[django-downloadview](https://github.com/benoitbryon/django-downloadview)
([project documentation](https://django-downloadview.readthedocs.io/en/1.9/)
and
[PyPI package information](https://pypi.org/project/django-downloadview/))
is a [Django](/django.html) extension for serving downloads through your
web application. While typically you would use a web server to handle
[static content](/static-content.html), sometimes you need to control
file access, such as requiring a user to register before downloading a
PDF. In that situations, django-downloadview is a handy library to avoid
boilerplate code for common scenarios.

[**django-downloadview / django_downloadview / nginx / response.py**](https://github.com/benoitbryon/django-downloadview/blob/master/django_downloadview/nginx/response.py)

```python
# response.py
from datetime import timedelta

~~from django.utils.timezone import now

from django_downloadview.response import ProxiedDownloadResponse, content_disposition
from django_downloadview.utils import content_type_to_charset, url_basename


class XAccelRedirectResponse(ProxiedDownloadResponse):
    "Http response that delegates serving file to Nginx via X-Accel headers."

    def __init__(
        self,
        redirect_url,
        content_type,
        basename=None,
        expires=None,
        with_buffering=None,
        limit_rate=None,
        attachment=True,
    ):
        super(XAccelRedirectResponse, self).__init__(content_type=content_type)
        if attachment:
            self.basename = basename or url_basename(redirect_url, content_type)
            self["Content-Disposition"] = content_disposition(self.basename)
        self["X-Accel-Redirect"] = redirect_url
        self["X-Accel-Charset"] = content_type_to_charset(content_type)
        if with_buffering is not None:
            self["X-Accel-Buffering"] = with_buffering and "yes" or "no"
        if expires:
~~            expire_seconds = timedelta(expires - now()).seconds
            self["X-Accel-Expires"] = expire_seconds
        elif expires is not None:  # We explicitely want it off.
            self["X-Accel-Expires"] = "off"
        if limit_rate is not None:
            self["X-Accel-Limit-Rate"] = limit_rate and "%d" % limit_rate or "off"



## ... source file continues with no further now examples...

```


## Example 5 from django-extensions
[django-extensions](https://github.com/django-extensions/django-extensions)
([project documentation](https://django-extensions.readthedocs.io/en/latest/)
and [PyPI page](https://pypi.org/project/django-extensions/))
is a [Django](/django.html) project that adds a bunch of additional
useful commands to the `manage.py` interface. This
[GoDjango video](https://www.youtube.com/watch?v=1F6G3ONhr4k) provides a
quick overview of what you get when you install it into your Python
environment.

The django-extensions project is open sourced under the
[MIT license](https://github.com/django-extensions/django-extensions/blob/master/LICENSE).

[**django-extensions / django_extensions / db / models.py**](https://github.com/django-extensions/django-extensions/blob/master/django_extensions/db/models.py)

```python
# models.py

from django.db import models
~~from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from django_extensions.db.fields import AutoSlugField, CreationDateTimeField, ModificationDateTimeField


class TimeStampedModel(models.Model):

    created = CreationDateTimeField(_('created'))
    modified = ModificationDateTimeField(_('modified'))

    def save(self, **kwargs):
        self.update_modified = kwargs.pop('update_modified', getattr(self, 'update_modified', True))
        super().save(**kwargs)

    class Meta:
        get_latest_by = 'modified'
        abstract = True


class TitleDescriptionModel(models.Model):

    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)



## ... source file abbreviated to get to now examples ...



    def inactive(self):
        return self.get_queryset().inactive()


class ActivatorModel(models.Model):

    INACTIVE_STATUS = 0
    ACTIVE_STATUS = 1

    STATUS_CHOICES = (
        (INACTIVE_STATUS, _('Inactive')),
        (ACTIVE_STATUS, _('Active')),
    )
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=ACTIVE_STATUS)
    activate_date = models.DateTimeField(blank=True, null=True, help_text=_('keep empty for an immediate activation'))
    deactivate_date = models.DateTimeField(blank=True, null=True, help_text=_('keep empty for indefinite activation'))
    objects = ActivatorModelManager()

    class Meta:
        ordering = ('status', '-activate_date',)
        abstract = True

    def save(self, *args, **kwargs):
        if not self.activate_date:
~~            self.activate_date = now()
        super().save(*args, **kwargs)



## ... source file continues with no further now examples...

```


## Example 6 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / models / imagemodels.py**](https://github.com/divio/django-filer/blob/develop/filer/models/imagemodels.py)

```python
# imagemodels.py
from __future__ import absolute_import

import logging
from datetime import datetime

from django.conf import settings
from django.db import models
~~from django.utils.timezone import get_current_timezone, make_aware, now
from django.utils.translation import ugettext_lazy as _

from .abstract import BaseImage


logger = logging.getLogger("filer")


class Image(BaseImage):
    date_taken = models.DateTimeField(_('date taken'), null=True, blank=True,
                                      editable=False)
    author = models.CharField(_('author'), max_length=255, null=True, blank=True)
    must_always_publish_author_credit = models.BooleanField(_('must always publish author credit'), default=False)
    must_always_publish_copyright = models.BooleanField(_('must always publish copyright'), default=False)

    class Meta(BaseImage.Meta):
        swappable = 'FILER_IMAGE_MODEL'
        default_manager_name = 'objects'

    def save(self, *args, **kwargs):
        if self.date_taken is None:
            try:
                exif_date = self.exif.get('DateTimeOriginal', None)
                if exif_date is not None:
                    d, t = exif_date.split(" ")
                    year, month, day = d.split(':')
                    hour, minute, second = t.split(':')
                    if getattr(settings, "USE_TZ", False):
                        tz = get_current_timezone()
                        self.date_taken = make_aware(datetime(
                            int(year), int(month), int(day),
                            int(hour), int(minute), int(second)), tz)
                    else:
                        self.date_taken = datetime(
                            int(year), int(month), int(day),
                            int(hour), int(minute), int(second))
            except Exception:
                pass
        if self.date_taken is None:
~~            self.date_taken = now()
        super(Image, self).save(*args, **kwargs)



## ... source file continues with no further now examples...

```


## Example 7 from django-filter
[django-filter](https://github.com/carltongibson/django-filter)
([project documentation](https://django-filter.readthedocs.io/en/master/)
and
[PyPI page](https://pypi.org/project/django-filter/2.2.0/))
makes it easier to filter down querysets from the
[Django ORM](/django-orm.html) by providing common bits of boilerplate
code. django-filter is provided as
[open source](https://github.com/carltongibson/django-filter/blob/master/LICENSE).

[**django-filter / django_filters / filters.py**](https://github.com/carltongibson/django-filter/blob/master/django_filters/./filters.py)

```python
# filters.py
from collections import OrderedDict
from datetime import timedelta

from django import forms
from django.db.models import Q
from django.db.models.constants import LOOKUP_SEP
from django.forms.utils import pretty_name
from django.utils.itercompat import is_iterable
~~from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from .conf import settings
from .constants import EMPTY_VALUES
from .fields import (
    BaseCSVField,
    BaseRangeField,
    ChoiceField,
    DateRangeField,
    DateTimeRangeField,
    IsoDateTimeField,
    IsoDateTimeRangeField,
    LookupChoiceField,
    ModelChoiceField,
    ModelMultipleChoiceField,
    MultipleChoiceField,
    RangeField,
    TimeRangeField
)
from .utils import get_model_field, label_for_filter

__all__ = [
    'AllValuesFilter',
    'AllValuesMultipleFilter',


## ... source file abbreviated to get to now examples ...


            elif value.start is not None:
                self.lookup_expr = 'gte'
                value = value.start
            elif value.stop is not None:
                self.lookup_expr = 'lte'
                value = value.stop

        return super().filter(qs, value)


def _truncate(dt):
    return dt.date()


class DateRangeFilter(ChoiceFilter):
    choices = [
        ('today', _('Today')),
        ('yesterday', _('Yesterday')),
        ('week', _('Past 7 days')),
        ('month', _('This month')),
        ('year', _('This year')),
    ]

    filters = {
        'today': lambda qs, name: qs.filter(**{
~~            '%s__year' % name: now().year,
~~            '%s__month' % name: now().month,
~~            '%s__day' % name: now().day
        }),
        'yesterday': lambda qs, name: qs.filter(**{
            '%s__year' % name: (now() - timedelta(days=1)).year,
            '%s__month' % name: (now() - timedelta(days=1)).month,
            '%s__day' % name: (now() - timedelta(days=1)).day,
        }),
        'week': lambda qs, name: qs.filter(**{
            '%s__gte' % name: _truncate(now() - timedelta(days=7)),
            '%s__lt' % name: _truncate(now() + timedelta(days=1)),
        }),
        'month': lambda qs, name: qs.filter(**{
~~            '%s__year' % name: now().year,
~~            '%s__month' % name: now().month
        }),
        'year': lambda qs, name: qs.filter(**{
~~            '%s__year' % name: now().year,
        }),
    }

    def __init__(self, choices=None, filters=None, *args, **kwargs):
        if choices is not None:
            self.choices = choices
        if filters is not None:
            self.filters = filters

        unique = set([x[0] for x in self.choices]) ^ set(self.filters)
        assert not unique, \
            "Keys must be present in both 'choices' and 'filters'. Missing keys: " \
            "'%s'" % ', '.join(sorted(unique))

        assert not hasattr(self, 'options'), \
            "The 'options' attribute has been replaced by 'choices' and 'filters'. " \
            "See: https://django-filter.readthedocs.io/en/master/guide/migration.html"

        kwargs.setdefault('null_label', None)
        super().__init__(choices=self.choices, *args, **kwargs)

    def filter(self, qs, value):
        if not value:
            return qs


## ... source file continues with no further now examples...

```


## Example 8 from django-import-export
[django-import-export](https://github.com/django-import-export/django-import-export)
([documentation](https://django-import-export.readthedocs.io/en/latest/)
and [PyPI page](https://pypi.org/project/django-import-export/))
is a [Django](/django.html) code library for importing and exporting data
from the Django Admin. The tool supports many export and import formats
such as CSV, JSON and YAML. django-import-export is open source under the
[BSD 2-Clause "Simplified" License](https://github.com/django-import-export/django-import-export/blob/master/LICENSE).

[**django-import-export / import_export / mixins.py**](https://github.com/django-import-export/django-import-export/blob/master/import_export/./mixins.py)

```python
# mixins.py
from django.http import HttpResponse
~~from django.utils.timezone import now
from django.views.generic.edit import FormView

from .formats import base_formats
from .forms import ExportForm
from .resources import modelresource_factory
from .signals import post_export


class ExportViewMixin:
    formats = base_formats.DEFAULT_FORMATS
    form_class = ExportForm
    resource_class = None

    def get_export_formats(self):
        return [f for f in self.formats if f().can_export()]

    def get_resource_class(self):
        if not self.resource_class:
            return modelresource_factory(self.model)
        return self.resource_class

    def get_export_resource_class(self):
        return self.get_resource_class()

    def get_resource_kwargs(self, request, *args, **kwargs):
        return {}

    def get_export_resource_kwargs(self, request, *args, **kwargs):
        return self.get_resource_kwargs(request, *args, **kwargs)

    def get_export_data(self, file_format, queryset, *args, **kwargs):
        resource_class = self.get_export_resource_class()
        data = resource_class(**self.get_export_resource_kwargs(self.request))\
            .export(queryset, *args, **kwargs)
        export_data = file_format.export_data(data)
        return export_data

    def get_export_filename(self, file_format):
~~        date_str = now().strftime('%Y-%m-%d')
        filename = "%s-%s.%s" % (self.model.__name__,
                                 date_str,
                                 file_format.get_extension())
        return filename

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['formats'] = self.get_export_formats()
        return kwargs


class ExportViewFormMixin(ExportViewMixin, FormView):
    def form_valid(self, form):
        formats = self.get_export_formats()
        file_format = formats[
            int(form.cleaned_data['file_format'])
        ]()
        if hasattr(self, 'get_filterset'):
            queryset = self.get_filterset(self.get_filterset_class()).qs
        else:


## ... source file continues with no further now examples...

```


## Example 9 from django-model-utils
[django-model-utils](https://github.com/jazzband/django-model-utils)
([project documentation](https://django-model-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-model-utils/))
provides useful mixins and utilities for working with
[Django ORM](/django-orm.html) models in your projects.

The django-model-utils project is open sourced under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/jazzband/django-model-utils/blob/master/LICENSE.txt).

[**django-model-utils / model_utils / fields.py**](https://github.com/jazzband/django-model-utils/blob/master/model_utils/./fields.py)

```python
# fields.py
import uuid
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
~~from django.utils.timezone import now

DEFAULT_CHOICES_NAME = 'STATUS'


class AutoCreatedField(models.DateTimeField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('editable', False)
        kwargs.setdefault('default', now)
        super().__init__(*args, **kwargs)


class AutoLastModifiedField(AutoCreatedField):
    def get_default(self):
        if not hasattr(self, "_default"):
            self._default = self._get_default()
        return self._default

    def pre_save(self, model_instance, add):
~~        value = now()
        if add:
            current_value = getattr(model_instance, self.attname, self.get_default())
            if current_value != self.get_default():
                value = getattr(model_instance, self.attname)
            else:
                for field in model_instance._meta.get_fields():
                    if isinstance(field, AutoCreatedField):
                        value = getattr(model_instance, field.name)
                        break
        setattr(model_instance, self.attname, value)
        return value


class StatusField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 100)
        self.check_for_status = not kwargs.pop('no_check_for_status', False)
        self.choices_name = kwargs.pop('choices_name', DEFAULT_CHOICES_NAME)
        super().__init__(*args, **kwargs)

    def prepare_class(self, sender, **kwargs):
        if not sender._meta.abstract and self.check_for_status:
            assert hasattr(sender, self.choices_name), \


## ... source file abbreviated to get to now examples ...


        monitor = kwargs.pop('monitor', None)
        if not monitor:
            raise TypeError(
                '%s requires a "monitor" argument' % self.__class__.__name__)
        self.monitor = monitor
        when = kwargs.pop('when', None)
        if when is not None:
            when = set(when)
        self.when = when
        super().__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name):
        self.monitor_attname = '_monitor_%s' % name
        models.signals.post_init.connect(self._save_initial, sender=cls)
        super().contribute_to_class(cls, name)

    def get_monitored_value(self, instance):
        return getattr(instance, self.monitor)

    def _save_initial(self, sender, instance, **kwargs):
        if self.monitor in instance.get_deferred_fields():
            return
        setattr(instance, self.monitor_attname, self.get_monitored_value(instance))

    def pre_save(self, model_instance, add):
~~        value = now()
        previous = getattr(model_instance, self.monitor_attname, None)
        current = self.get_monitored_value(model_instance)
        if previous != current:
            if self.when is None or current in self.when:
                setattr(model_instance, self.attname, value)
                self._save_initial(model_instance.__class__, model_instance)
        return super().pre_save(model_instance, add)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['monitor'] = self.monitor
        if self.when is not None:
            kwargs['when'] = self.when
        return name, path, args, kwargs


SPLIT_MARKER = getattr(settings, 'SPLIT_MARKER', '<!-- split -->')

SPLIT_DEFAULT_PARAGRAPHS = getattr(settings, 'SPLIT_DEFAULT_PARAGRAPHS', 2)


def _excerpt_field_name(name):
    return '_%s_excerpt' % name



## ... source file continues with no further now examples...

```

