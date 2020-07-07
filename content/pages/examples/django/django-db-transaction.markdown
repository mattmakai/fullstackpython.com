title: django.db transaction Example Code
category: page
slug: django-db-transaction-examples
sortorder: 500011169
toc: False
sidebartitle: django.db transaction
meta: Python example code for the transaction callable from the django.db module of the Django project.


transaction is a callable within the django.db module of the Django project.


## Example 1 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / account / models.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/account/models.py)

```python
# models.py
from __future__ import unicode_literals

import datetime

from django.core import signing
~~from django.db import models, transaction
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _

from .. import app_settings as allauth_app_settings
from . import app_settings, signals
from .adapter import get_adapter
from .managers import EmailAddressManager, EmailConfirmationManager
from .utils import user_email


class EmailAddress(models.Model):

    user = models.ForeignKey(allauth_app_settings.USER_MODEL,
                             verbose_name=_('user'),
                             on_delete=models.CASCADE)
    email = models.EmailField(unique=app_settings.UNIQUE_EMAIL,
                              max_length=app_settings.EMAIL_MAX_LENGTH,
                              verbose_name=_('e-mail address'))
    verified = models.BooleanField(verbose_name=_('verified'), default=False)
    primary = models.BooleanField(verbose_name=_('primary'), default=False)

    objects = EmailAddressManager()



## ... source file abbreviated to get to transaction examples ...


    def __str__(self):
        return self.email

    def set_as_primary(self, conditional=False):
        old_primary = EmailAddress.objects.get_primary(self.user)
        if old_primary:
            if conditional:
                return False
            old_primary.primary = False
            old_primary.save()
        self.primary = True
        self.save()
        user_email(self.user, self.email)
        self.user.save()
        return True

    def send_confirmation(self, request=None, signup=False):
        if app_settings.EMAIL_CONFIRMATION_HMAC:
            confirmation = EmailConfirmationHMAC(self)
        else:
            confirmation = EmailConfirmation.create(self)
        confirmation.send(request, signup=signup)
        return confirmation

    def change(self, request, new_email, confirm=True):
~~        with transaction.atomic():
            user_email(self.user, new_email)
            self.user.save()
            self.email = new_email
            self.verified = False
            self.save()
            if confirm:
                self.send_confirmation(request)


class EmailConfirmation(models.Model):

    email_address = models.ForeignKey(EmailAddress,
                                      verbose_name=_('e-mail address'),
                                      on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name=_('created'),
                                   default=timezone.now)
    sent = models.DateTimeField(verbose_name=_('sent'), null=True)
    key = models.CharField(verbose_name=_('key'), max_length=64, unique=True)

    objects = EmailConfirmationManager()

    class Meta:
        verbose_name = _("email confirmation")
        verbose_name_plural = _("email confirmations")


## ... source file continues with no further transaction examples...

```


## Example 2 from django-import-export
[django-import-export](https://github.com/django-import-export/django-import-export)
([documentation](https://django-import-export.readthedocs.io/en/latest/)
and [PyPI page](https://pypi.org/project/django-import-export/))
is a [Django](/django.html) code library for importing and exporting data
from the Django Admin. The tool supports many export and import formats
such as CSV, JSON and YAML. django-import-export is open source under the
[BSD 2-Clause "Simplified" License](https://github.com/django-import-export/django-import-export/blob/master/LICENSE).

[**django-import-export / import_export / utils.py**](https://github.com/django-import-export/django-import-export/blob/master/import_export/./utils.py)

```python
# utils.py
~~from django.db import transaction


class atomic_if_using_transaction:
    def __init__(self, using_transactions):
        self.using_transactions = using_transactions
        if using_transactions:
~~            self.context_manager = transaction.atomic()

    def __enter__(self):
        if self.using_transactions:
            self.context_manager.__enter__()

    def __exit__(self, *args):
        if self.using_transactions:
            self.context_manager.__exit__(*args)



## ... source file continues with no further transaction examples...

```


## Example 3 from django-model-utils
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
~~from django.db import models, transaction, router
from django.db.models.signals import post_save, pre_save
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


## ... source file abbreviated to get to transaction examples ...


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
            pre_save.send(
                sender=origin, instance=self, raw=raw, using=using,
                update_fields=update_fields,
            )
~~        with transaction.atomic(using=using, savepoint=False):
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



## ... source file continues with no further transaction examples...

```


## Example 4 from django-oauth-toolkit
[django-oauth-toolkit](https://github.com/jazzband/django-oauth-toolkit)
([project website](http://dot.evonove.it/) and
[PyPI package information](https://pypi.org/project/django-oauth-toolkit/1.2.0/))
is a code library for adding and handling [OAuth2](https://oauth.net/)
flows within your [Django](/django.html) web application and
[API](/application-programming-interfaces.html).

The django-oauth-toolkit project is open sourced under the
[FreeBSD license](https://github.com/jazzband/django-oauth-toolkit/blob/master/LICENSE)
and it is maintained by the developer community group
[Jazzband](https://jazzband.co/).

[**django-oauth-toolkit / oauth2_provider / models.py**](https://github.com/jazzband/django-oauth-toolkit/blob/master/oauth2_provider/./models.py)

```python
# models.py
import logging
from datetime import timedelta
from urllib.parse import parse_qsl, urlparse

from django.apps import apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
~~from django.db import models, transaction
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .generators import generate_client_id, generate_client_secret
from .scopes import get_scopes_backend
from .settings import oauth2_settings
from .validators import RedirectURIValidator, WildcardSet


logger = logging.getLogger(__name__)


class AbstractApplication(models.Model):
    CLIENT_CONFIDENTIAL = "confidential"
    CLIENT_PUBLIC = "public"
    CLIENT_TYPES = (
        (CLIENT_CONFIDENTIAL, _("Confidential")),
        (CLIENT_PUBLIC, _("Public")),
    )

    GRANT_AUTHORIZATION_CODE = "authorization-code"
    GRANT_IMPLICIT = "implicit"
    GRANT_PASSWORD = "password"


## ... source file abbreviated to get to transaction examples ...


    class Meta(AbstractAccessToken.Meta):
        swappable = "OAUTH2_PROVIDER_ACCESS_TOKEN_MODEL"


class AbstractRefreshToken(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s"
    )
    token = models.CharField(max_length=255)
    application = models.ForeignKey(
        oauth2_settings.APPLICATION_MODEL, on_delete=models.CASCADE)
    access_token = models.OneToOneField(
        oauth2_settings.ACCESS_TOKEN_MODEL, on_delete=models.SET_NULL, blank=True, null=True,
        related_name="refresh_token"
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    revoked = models.DateTimeField(null=True)

    def revoke(self):
        access_token_model = get_access_token_model()
        refresh_token_model = get_refresh_token_model()
~~        with transaction.atomic():
            self = refresh_token_model.objects.filter(
                pk=self.pk, revoked__isnull=True
            ).select_for_update().first()
            if not self:
                return

            try:
                access_token_model.objects.get(id=self.access_token_id).revoke()
            except access_token_model.DoesNotExist:
                pass
            self.access_token = None
            self.revoked = timezone.now()
            self.save()

    def __str__(self):
        return self.token

    class Meta:
        abstract = True
        unique_together = ("token", "revoked",)


class RefreshToken(AbstractRefreshToken):
    class Meta(AbstractRefreshToken.Meta):


## ... source file abbreviated to get to transaction examples ...



def get_access_token_model():
    return apps.get_model(oauth2_settings.ACCESS_TOKEN_MODEL)


def get_refresh_token_model():
    return apps.get_model(oauth2_settings.REFRESH_TOKEN_MODEL)


def clear_expired():
    now = timezone.now()
    refresh_expire_at = None
    access_token_model = get_access_token_model()
    refresh_token_model = get_refresh_token_model()
    grant_model = get_grant_model()
    REFRESH_TOKEN_EXPIRE_SECONDS = oauth2_settings.REFRESH_TOKEN_EXPIRE_SECONDS
    if REFRESH_TOKEN_EXPIRE_SECONDS:
        if not isinstance(REFRESH_TOKEN_EXPIRE_SECONDS, timedelta):
            try:
                REFRESH_TOKEN_EXPIRE_SECONDS = timedelta(seconds=REFRESH_TOKEN_EXPIRE_SECONDS)
            except TypeError:
                e = "REFRESH_TOKEN_EXPIRE_SECONDS must be either a timedelta or seconds"
                raise ImproperlyConfigured(e)
        refresh_expire_at = now - REFRESH_TOKEN_EXPIRE_SECONDS

~~    with transaction.atomic():
        if refresh_expire_at:
            revoked = refresh_token_model.objects.filter(
                revoked__lt=refresh_expire_at,
            )
            expired = refresh_token_model.objects.filter(
                access_token__expires__lt=refresh_expire_at,
            )

            logger.info("%s Revoked refresh tokens to be deleted", revoked.count())
            logger.info("%s Expired refresh tokens to be deleted", expired.count())

            revoked.delete()
            expired.delete()
        else:
            logger.info("refresh_expire_at is %s. No refresh tokens deleted.",
                        refresh_expire_at)

        access_tokens = access_token_model.objects.filter(
            refresh_token__isnull=True,
            expires__lt=now
        )
        grants = grant_model.objects.filter(expires__lt=now)

        logger.info("%s Expired access tokens to be deleted", access_tokens.count())


## ... source file continues with no further transaction examples...

```


## Example 5 from django-rest-framework
[Django REST Framework](https://github.com/encode/django-rest-framework)
([project homepage and documentation](https://www.django-rest-framework.org/),
[PyPI package information](https://pypi.org/project/djangorestframework/)
and [more resources on Full Stack Python](/django-rest-framework-drf.html)),
often abbreviated as "DRF", is a popular [Django](/django.html) extension
for building [web APIs](/application-programming-interfaces.html).
The project has fantastic documentation and a wonderful
[quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)
that serve as examples of how to make it easier for newcomers
to get started.

The project is open sourced under the
[Encode OSS Ltd. license](https://github.com/encode/django-rest-framework/blob/master/LICENSE.md).

[**django-rest-framework / rest_framework / views.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./views.py)

```python
# views.py
from django.conf import settings
from django.core.exceptions import PermissionDenied
~~from django.db import connection, models, transaction
from django.http import Http404
from django.http.response import HttpResponseBase
from django.utils.cache import cc_delim_re, patch_vary_headers
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from rest_framework import exceptions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.schemas import DefaultSchema
from rest_framework.settings import api_settings
from rest_framework.utils import formatting


def get_view_name(view):
    name = getattr(view, 'name', None)
    if name is not None:
        return name

    name = view.__class__.__name__
    name = formatting.remove_trailing_string(name, 'View')
    name = formatting.remove_trailing_string(name, 'ViewSet')
    name = formatting.camelcase_to_spaces(name)

    suffix = getattr(view, 'suffix', None)
    if suffix:
        name += ' ' + suffix

    return name


def get_view_description(view, html=False):
    description = getattr(view, 'description', None)
    if description is None:
        description = view.__class__.__doc__ or ''

    description = formatting.dedent(smart_str(description))
    if html:
        return formatting.markup_description(description)
    return description


def set_rollback():
    atomic_requests = connection.settings_dict.get('ATOMIC_REQUESTS', False)
    if atomic_requests and connection.in_atomic_block:
~~        transaction.set_rollback(True)


def exception_handler(exc, context):
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, (list, dict)):
            data = exc.detail
        else:
            data = {'detail': exc.detail}

        set_rollback()
        return Response(data, status=exc.status_code, headers=headers)

    return None


## ... source file continues with no further transaction examples...

```


## Example 6 from django-taggit
[django-taggit](https://github.com/jazzband/django-taggit/)
([PyPI page](https://pypi.org/project/django-taggit/)) provides a way
to create, store, manage and use tags in a [Django](/django.html) project.
The code for django-taggit is
[open source](https://github.com/jazzband/django-taggit/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-taggit / taggit / models.py**](https://github.com/jazzband/django-taggit/blob/master/taggit/./models.py)

```python
# models.py
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
~~from django.db import IntegrityError, models, router, transaction
from django.utils.text import slugify
from django.utils.translation import gettext, gettext_lazy as _

try:
    from unidecode import unidecode
except ImportError:

    def unidecode(tag):
        return tag


class TagBase(models.Model):
    name = models.CharField(verbose_name=_("name"), unique=True, max_length=100)
    slug = models.SlugField(verbose_name=_("slug"), unique=True, max_length=100)

    def __str__(self):
        return self.name

    def __gt__(self, other):
        return self.name.lower() > other.name.lower()

    def __lt__(self, other):
        return self.name.lower() < other.name.lower()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self._state.adding and not self.slug:
            self.slug = self.slugify(self.name)
            using = kwargs.get("using") or router.db_for_write(
                type(self), instance=self
            )
            kwargs["using"] = using
            try:
~~                with transaction.atomic(using=using):
                    res = super().save(*args, **kwargs)
                return res
            except IntegrityError:
                pass
            slugs = set(
                type(self)
                ._default_manager.filter(slug__startswith=self.slug)
                .values_list("slug", flat=True)
            )
            i = 1
            while True:
                slug = self.slugify(self.name, i)
                if slug not in slugs:
                    self.slug = slug
                    return super().save(*args, **kwargs)
                i += 1
        else:
            return super().save(*args, **kwargs)

    def slugify(self, tag, i=None):
        slug = slugify(unidecode(tag))
        if i is not None:
            slug += "_%d" % i
        return slug


## ... source file continues with no further transaction examples...

```


## Example 7 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / core / models.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/core/models.py)

```python
# models.py
import json
import logging
from collections import defaultdict
from io import StringIO
from urllib.parse import urlparse

from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core import checks
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.core.handlers.base import BaseHandler
from django.core.handlers.wsgi import WSGIRequest
~~from django.db import models, transaction
from django.db.models import Case, Q, Value, When
from django.db.models.functions import Concat, Lower, Substr
from django.http import Http404
from django.http.request import split_domain_port
from django.template.response import TemplateResponse
from django.urls import NoReverseMatch, reverse
from django.utils import timezone
from django.utils.cache import patch_cache_control
from django.utils.functional import cached_property
from django.utils.text import capfirst, slugify
from django.utils.translation import gettext_lazy as _
from modelcluster.models import (
    ClusterableModel, get_all_child_m2m_relations, get_all_child_relations)
from treebeard.mp_tree import MP_Node

from wagtail.core.query import PageQuerySet, TreeQuerySet
from wagtail.core.signals import page_published, page_unpublished, post_page_move, pre_page_move
from wagtail.core.sites import get_site_for_hostname
from wagtail.core.url_routing import RouteResult
from wagtail.core.utils import WAGTAIL_APPEND_SLASH, camelcase_to_underscore, resolve_model_string
from wagtail.search import index


logger = logging.getLogger('wagtail.core')


## ... source file abbreviated to get to transaction examples ...


        return self.revisions.exclude(approved_go_live_at__isnull=True).exists()

    def has_unpublished_subtree(self):
        return (not self.live) and (not self.get_descendants().filter(live=True).exists())

    def move(self, target, pos=None):
        parent_before = self.get_parent()
        if pos in ('first-child', 'last-child', 'sorted-child'):
            parent_after = target
        else:
            parent_after = target.get_parent()

        old_self = Page.objects.get(id=self.id)
        old_url_path = old_self.url_path
        new_url_path = old_self.set_url_path(parent=parent_after)

        pre_page_move.send(
            sender=self.specific_class or self.__class__,
            instance=self,
            parent_page_before=parent_before,
            parent_page_after=parent_after,
            url_path_before=old_url_path,
            url_path_after=new_url_path,
        )

~~        with transaction.atomic():
            super().move(target, pos=pos)

            new_self = Page.objects.get(id=self.id)
            new_self.url_path = new_url_path
            new_self.save()

            if old_url_path != new_url_path:
                new_self._update_descendant_url_paths(old_url_path, new_url_path)

        post_page_move.send(
            sender=self.specific_class or self.__class__,
            instance=new_self,
            parent_page_before=parent_before,
            parent_page_after=parent_after,
            url_path_before=old_url_path,
            url_path_after=new_url_path,
        )

        logger.info("Page moved: \"%s\" id=%d path=%s", self.title, self.id, new_url_path)

    def copy(self, recursive=False, to=None, update_attrs=None, copy_revisions=True, keep_live=True, user=None, process_child_object=None, exclude_fields=None):
        specific_self = self.specific
        default_exclude_fields = ['id', 'path', 'depth', 'numchild', 'url_path', 'path', 'index_entries']
        exclude_fields = default_exclude_fields + specific_self.exclude_fields_in_copy + (exclude_fields or [])


## ... source file continues with no further transaction examples...

```

