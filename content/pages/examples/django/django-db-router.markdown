title: django.db router Example Code
category: page
slug: django-db-router-examples
sortorder: 500011168
toc: False
sidebartitle: django.db router
meta: Python example code for the router callable from the django.db module of the Django project.


router is a callable within the django.db module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / admin / placeholderadmin.py**](https://github.com/divio/django-cms/blob/develop/cms/admin/placeholderadmin.py)

```python
# placeholderadmin.py
import uuid
import warnings

from django.conf.urls import url
from django.contrib.admin.helpers import AdminForm
from django.contrib.admin.utils import get_deleted_objects
from django.core.exceptions import PermissionDenied
~~from django.db import router, transaction
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_text
from django.utils import translation
from django.utils.translation import ugettext as _
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.http import require_POST

from six.moves.urllib.parse import parse_qsl, urlparse

from six import get_unbound_function, get_method_function

from cms import operations
from cms.admin.forms import PluginAddValidationForm
from cms.constants import SLUG_REGEXP
from cms.exceptions import PluginLimitReached


## ... source file abbreviated to get to router examples ...


        source_placeholder.mark_as_dirty(target_language, clear_cache=False)

        self._send_post_placeholder_operation(
            request,
            operation=operations.CUT_PLUGIN,
            token=action_token,
            plugin=updated_plugin.get_bound_plugin(),
            clipboard=target_placeholder,
            clipboard_language=target_language,
            source_language=source_language,
            source_placeholder=source_placeholder,
            source_parent_id=plugin.parent_id,
            source_order=new_source_order,
        )
        return updated_plugin

    @xframe_options_sameorigin
    def delete_plugin(self, request, plugin_id):
        plugin = self._get_plugin_from_id(plugin_id)

        if not self.has_delete_plugin_permission(request, plugin):
            return HttpResponseForbidden(force_text(
                _("You do not have permission to delete this plugin")))

        opts = plugin._meta
~~        using = router.db_for_write(opts.model)
        if DJANGO_2_0:
            get_deleted_objects_additional_kwargs = {
                'opts': opts,
                'using': using,
                'user': request.user,
            }
        else:
            get_deleted_objects_additional_kwargs = {'request': request}
        deleted_objects, __, perms_needed, protected = get_deleted_objects(
            [plugin], admin_site=self.admin_site,
            **get_deleted_objects_additional_kwargs
        )

        if request.POST:  # The user has already confirmed the deletion.
            if perms_needed:
                raise PermissionDenied(_("You do not have permission to delete this plugin"))
            obj_display = force_text(plugin)
            placeholder = plugin.placeholder
            plugin_tree_order = placeholder.get_plugin_tree_order(
                language=plugin.language,
                parent_id=plugin.parent_id,
            )

            operation_token = self._send_pre_placeholder_operation(


## ... source file abbreviated to get to router examples ...


            "object": plugin,
            "deleted_objects": deleted_objects,
            "perms_lacking": perms_needed,
            "protected": protected,
            "opts": opts,
            "app_label": opts.app_label,
        }
        request.current_app = self.admin_site.name
        return TemplateResponse(
            request, "admin/cms/page/plugin/delete_confirmation.html", context
        )

    @xframe_options_sameorigin
    def clear_placeholder(self, request, placeholder_id):
        placeholder = get_object_or_404(Placeholder, pk=placeholder_id)
        language = request.GET.get('language')

        if placeholder.pk == request.toolbar.clipboard.pk:
            placeholder.clear(language)
            return HttpResponseRedirect(admin_reverse('index', current_app=self.admin_site.name))

        if not self.has_clear_placeholder_permission(request, placeholder, language):
            return HttpResponseForbidden(force_text(_("You do not have permission to clear this placeholder")))

        opts = Placeholder._meta
~~        using = router.db_for_write(Placeholder)
        plugins = placeholder.get_plugins_list(language)

        if DJANGO_2_0:
            get_deleted_objects_additional_kwargs = {
                'opts': opts,
                'using': using,
                'user': request.user,
            }
        else:
            get_deleted_objects_additional_kwargs = {'request': request}
        deleted_objects, __, perms_needed, protected = get_deleted_objects(
            plugins, admin_site=self.admin_site,
            **get_deleted_objects_additional_kwargs
        )

        obj_display = force_text(placeholder)

        if request.POST:
            if perms_needed:
                return HttpResponseForbidden(force_text(_("You do not have permission to clear this placeholder")))

            operation_token = self._send_pre_placeholder_operation(
                request,
                operation=operations.CLEAR_PLACEHOLDER,


## ... source file continues with no further router examples...

```


## Example 2 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / admin / folderadmin.py**](https://github.com/divio/django-filer/blob/develop/filer/admin/folderadmin.py)

```python
# folderadmin.py
from __future__ import absolute_import, division, unicode_literals

import itertools
import os
import re
from collections import OrderedDict

from django import forms
from django.conf import settings as django_settings
from django.conf.urls import url
from django.contrib import messages
from django.contrib.admin import helpers
from django.contrib.admin.utils import capfirst, quote, unquote
from django.core.exceptions import PermissionDenied, ValidationError
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
~~from django.db import models, router
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.encoding import force_text
from django.utils.html import escape
from django.utils.http import urlquote, urlunquote
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy, ungettext

from .. import settings
from ..models import (
    File, Folder, FolderPermission, FolderRoot, ImagesWithMissingData,
    UnsortedImages, tools,
)
from ..settings import FILER_IMAGE_MODEL, FILER_PAGINATE_BY
from ..thumbnail_processors import normalize_subject_location
from ..utils.compatibility import get_delete_permission
from ..utils.filer_easy_thumbnails import FilerActionThumbnailer
from ..utils.loader import load_model
from . import views
from .forms import CopyFilesAndFoldersForm, RenameFilesForm, ResizeImagesForm
from .patched.admin_utils import get_deleted_objects
from .permissions import PrimitivePermissionAwareModelAdmin


## ... source file abbreviated to get to router examples ...


        return self.files_set_public_or_private(request, False, files_queryset,
                                                folders_queryset)

    files_set_private.short_description = ugettext_lazy(
        "Enable permissions for selected files")

    def files_set_public(self, request, files_queryset, folders_queryset):
        return self.files_set_public_or_private(request, True, files_queryset,
                                                folders_queryset)

    files_set_public.short_description = ugettext_lazy(
        "Disable permissions for selected files")

    def delete_files_or_folders(self, request, files_queryset, folders_queryset):
        opts = self.model._meta
        app_label = opts.app_label

        if not self.has_delete_permission(request):
            raise PermissionDenied

        current_folder = self._get_current_action_folder(
            request, files_queryset, folders_queryset)

        all_protected = []

~~        using = router.db_for_write(self.model)
        deletable_files, model_count_files, perms_needed_files, protected_files = get_deleted_objects(files_queryset, files_queryset.model._meta, request.user, self.admin_site, using)
        deletable_folders, model_count_folder, perms_needed_folders, protected_folders = get_deleted_objects(folders_queryset, folders_queryset.model._meta, request.user, self.admin_site, using)
        all_protected.extend(protected_files)
        all_protected.extend(protected_folders)

        all_deletable_objects = [deletable_files, deletable_folders]
        all_perms_needed = perms_needed_files.union(perms_needed_folders)

        if request.POST.get('post'):
            if all_perms_needed:
                raise PermissionDenied
            n = files_queryset.count() + folders_queryset.count()
            if n:
                for f in files_queryset:
                    self.log_deletion(request, f, force_text(f))
                    f.delete()
                folder_ids = set()
                for folder in folders_queryset:
                    folder_ids.add(folder.id)
                    folder_ids.update(
                        folder.get_descendants().values_list('id', flat=True))
                for f in File.objects.filter(folder__in=folder_ids):
                    self.log_deletion(request, f, force_text(f))
                    f.delete()


## ... source file continues with no further router examples...

```


## Example 3 from django-guardian
[django-guardian](https://github.com/django-guardian/django-guardian)
([project documentation](https://django-guardian.readthedocs.io/en/stable/)
and
[PyPI page](https://pypi.org/project/django-guardian/))
provides per-object permissions in [Django](/django.html) projects
by enhancing the existing authentication backend. The project's code
is open source under the
[MIT license](https://github.com/django-guardian/django-guardian/blob/devel/LICENSE).

[**django-guardian / guardian / management / __init__.py**](https://github.com/django-guardian/django-guardian/blob/devel/guardian/management/__init__.py)

```python
# __init__.py
from django.contrib.auth import get_user_model
from django.db.models import signals
from django.utils.module_loading import import_string
~~from django.db import router
from guardian.conf import settings as guardian_settings


def get_init_anonymous_user(User):
    kwargs = {
        User.USERNAME_FIELD: guardian_settings.ANONYMOUS_USER_NAME
    }
    user = User(**kwargs)
    user.set_unusable_password()
    return user


def create_anonymous_user(sender, **kwargs):
    User = get_user_model()
~~    if not router.allow_migrate_model(kwargs['using'], User):
        return
    try:
        lookup = {User.USERNAME_FIELD: guardian_settings.ANONYMOUS_USER_NAME}
        User.objects.using(kwargs['using']).get(**lookup)
    except User.DoesNotExist:
        retrieve_anonymous_function = import_string(
            guardian_settings.GET_INIT_ANONYMOUS_USER)
        user = retrieve_anonymous_function(User)
        user.save(using=kwargs['using'])

if guardian_settings.ANONYMOUS_USER_NAME is not None:
    from django.apps import apps
    guardian_app = apps.get_app_config('guardian')
    signals.post_migrate.connect(create_anonymous_user, sender=guardian_app,
                                 dispatch_uid="guardian.management.create_anonymous_user")



## ... source file continues with no further router examples...

```


## Example 4 from django-model-utils
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


## ... source file abbreviated to get to router examples ...




class UUIDModel(models.Model):
    id = UUIDField(
        primary_key=True,
        version=4,
        editable=False,
    )

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
~~        using = using or router.db_for_write(self.__class__, instance=self)
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
            post_save.send(
                sender=origin, instance=self, created=(not updated),
                update_fields=update_fields, raw=raw, using=using,


## ... source file continues with no further router examples...

```


## Example 5 from django-taggit
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
~~            using = kwargs.get("using") or router.db_for_write(
                type(self), instance=self
            )
            kwargs["using"] = using
            try:
                with transaction.atomic(using=using):
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



## ... source file continues with no further router examples...

```

