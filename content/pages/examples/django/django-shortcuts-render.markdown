title: django.shortcuts render Example Code
category: page
slug: django-shortcuts-render-examples
sortorder: 500011348
toc: False
sidebartitle: django.shortcuts render
meta: Python example code for the render callable from the django.shortcuts module of the Django project.


render is a callable within the django.shortcuts module of the Django project.


## Example 1 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / registration / views.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/registration/views.py)

```python
# views.py
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
~~from django.shortcuts import render, redirect

from users.models import generate_avatar
from users.forms import PersonalForm, ProfessionalForm, SubscriptionsForm

User = get_user_model()


@login_required
def personal(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = PersonalForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            profile.avatar = generate_avatar(profile)
            profile.save()
            return redirect('register-professional')
    else:
        form = PersonalForm(instance=profile)
~~    return render(request, 'registration/personal.html', {
        'form': form
    })

@login_required
def professional(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfessionalForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('register-subscriptions')
    else:
        form = ProfessionalForm(instance=profile)
~~    return render(request, 'registration/professional.html', {
        'form': form
    })


@login_required
def subscriptions(request):
    subscriptions = request.user.subscriptions
    if request.method == 'POST':
        form = SubscriptionsForm(request.POST, instance=subscriptions)
        if form.is_valid():
            form.save()
            request.user.has_finished_registration = True
            request.user.save()
            return redirect('home')
    else:
        form = SubscriptionsForm(instance=subscriptions)
~~    return render(request, 'registration/subscriptions.html', {
        'form': form
    })



## ... source file continues with no further render examples...

```


## Example 2 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / socialaccount / helpers.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/socialaccount/helpers.py)

```python
# helpers.py
from django.contrib import messages
from django.forms import ValidationError
from django.http import HttpResponseRedirect
~~from django.shortcuts import render
from django.urls import reverse

from allauth.account import app_settings as account_settings
from allauth.account.adapter import get_adapter as get_account_adapter
from allauth.account.utils import complete_signup, perform_login, user_username
from allauth.exceptions import ImmediateHttpResponse

from . import app_settings, signals
from .adapter import get_adapter
from .models import SocialLogin
from .providers.base import AuthError, AuthProcess


def _process_signup(request, sociallogin):
    auto_signup = get_adapter(request).is_auto_signup_allowed(
        request,
        sociallogin)
    if not auto_signup:
        request.session['socialaccount_sociallogin'] = sociallogin.serialize()
        url = reverse('socialaccount_signup')
        ret = HttpResponseRedirect(url)
    else:
        if account_settings.USER_MODEL_USERNAME_FIELD:
            username = user_username(sociallogin.user)
            try:
                get_account_adapter(request).clean_username(username)
            except ValidationError:
                user_username(sociallogin.user, '')
        if not get_adapter(request).is_open_for_signup(
                request,
                sociallogin):
~~            return render(
                request,
                "account/signup_closed." +
                account_settings.TEMPLATE_EXTENSION)
        get_adapter(request).save_user(request, sociallogin, form=None)
        ret = complete_social_signup(request, sociallogin)
    return ret


def _login_social_account(request, sociallogin):
    return perform_login(request, sociallogin.user,
                         email_verification=app_settings.EMAIL_VERIFICATION,
                         redirect_url=sociallogin.get_redirect_url(request),
                         signal_kwargs={"sociallogin": sociallogin})


def render_authentication_error(request,
                                provider_id,
                                error=AuthError.UNKNOWN,
                                exception=None,
                                extra_context=None):
    try:
        if extra_context is None:
            extra_context = {}
        get_adapter(request).authentication_error(
            request,
            provider_id,
            error=error,
            exception=exception,
            extra_context=extra_context)
    except ImmediateHttpResponse as e:
        return e.response
    if error == AuthError.CANCELLED:
        return HttpResponseRedirect(reverse('socialaccount_login_cancelled'))
    context = {
        'auth_error': {
            'provider': provider_id,
            'code': error,
            'exception': exception
        }
    }
    context.update(extra_context)
~~    return render(
        request,
        "socialaccount/authentication_error." +
        account_settings.TEMPLATE_EXTENSION,
        context
    )


def _add_social_account(request, sociallogin):
    if request.user.is_anonymous:
        return HttpResponseRedirect(reverse('socialaccount_connections'))
    level = messages.INFO
    message = 'socialaccount/messages/account_connected.txt'
    action = None
    if sociallogin.is_existing:
        if sociallogin.user != request.user:
            level = messages.ERROR
            message = 'socialaccount/messages/account_connected_other.txt'
        else:
            action = 'updated'
            message = 'socialaccount/messages/account_connected_updated.txt'
            signals.social_account_updated.send(
                sender=SocialLogin,
                request=request,
                sociallogin=sociallogin)


## ... source file continues with no further render examples...

```


## Example 3 from django-axes
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

[**django-axes / axes / helpers.py**](https://github.com/jazzband/django-axes/blob/master/axes/./helpers.py)

```python
# helpers.py
from datetime import timedelta
from hashlib import md5
from logging import getLogger
from string import Template
from typing import Callable, Optional, Type, Union
from urllib.parse import urlencode

from django.core.cache import caches, BaseCache
from django.http import HttpRequest, HttpResponse, JsonResponse, QueryDict
~~from django.shortcuts import render, redirect
from django.utils.module_loading import import_string

import ipware.ip

from axes.conf import settings
from axes.models import AccessBase

log = getLogger(__name__)


def get_cache() -> BaseCache:

    return caches[getattr(settings, "AXES_CACHE", "default")]


def get_cache_timeout() -> Optional[int]:

    cool_off = get_cool_off()
    if cool_off is None:
        return None
    return int(cool_off.total_seconds())


def get_cool_off() -> Optional[timedelta]:


## ... source file abbreviated to get to render examples ...


        raise TypeError(
            "settings.AXES_LOCKOUT_CALLABLE needs to be a string, callable, or None."
        )

    status = 403
    context = {
        "failure_limit": get_failure_limit(request, credentials),
        "username": get_client_username(request, credentials) or "",
    }

    cool_off = get_cool_off()
    if cool_off:
        context.update(
            {
                "cooloff_time": get_cool_off_iso8601(
                    cool_off
                ),  # differing old name is kept for backwards compatibility
                "cooloff_timedelta": cool_off,
            }
        )

    if request.is_ajax():
        return JsonResponse(context, status=status)

    if settings.AXES_LOCKOUT_TEMPLATE:
~~        return render(request, settings.AXES_LOCKOUT_TEMPLATE, context, status=status)

    if settings.AXES_LOCKOUT_URL:
        lockout_url = settings.AXES_LOCKOUT_URL
        query_string = urlencode({"username": context["username"]})
        url = "{}?{}".format(lockout_url, query_string)
        return redirect(url)

    return HttpResponse(get_lockout_message(), status=status)


def is_ip_address_in_whitelist(ip_address: str) -> bool:
    if not settings.AXES_IP_WHITELIST:
        return False

    return ip_address in settings.AXES_IP_WHITELIST


def is_ip_address_in_blacklist(ip_address: str) -> bool:
    if not settings.AXES_IP_BLACKLIST:
        return False

    return ip_address in settings.AXES_IP_BLACKLIST




## ... source file continues with no further render examples...

```


## Example 4 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / page_rendering.py**](https://github.com/divio/django-cms/blob/develop/cms/./page_rendering.py)

```python
# page_rendering.py
from django.conf import settings
from django.http import Http404
~~from django.shortcuts import render
from django.template.response import TemplateResponse
from django.urls import Resolver404, resolve, reverse

from cms import __version__
from cms.cache.page import set_page_cache
from cms.models import Page
from cms.utils.conf import get_cms_setting
from cms.utils.page import get_page_template_from_request
from cms.utils.page_permissions import user_can_change_page, user_can_view_page


def render_page(request, page, current_language, slug):
    context = {}
    context['lang'] = current_language
    context['current_page'] = page
    context['has_change_permissions'] = user_can_change_page(request.user, page)
    context['has_view_permissions'] = user_can_view_page(request.user, page)

    if not context['has_view_permissions']:
        return _handle_no_page(request)

    template = get_page_template_from_request(request)
    response = TemplateResponse(request, template, context)
    response.add_post_render_callback(set_page_cache)

    xframe_options = page.get_xframe_options()
    if xframe_options == Page.X_FRAME_OPTIONS_INHERIT or xframe_options is None:
        return response

    response.xframe_options_exempt = True

    if xframe_options == Page.X_FRAME_OPTIONS_ALLOW:
        return response
    elif xframe_options == Page.X_FRAME_OPTIONS_SAMEORIGIN:
        response['X-Frame-Options'] = 'SAMEORIGIN'
    elif xframe_options == Page.X_FRAME_OPTIONS_DENY:
        response['X-Frame-Options'] = 'DENY'
    return response


def render_object_structure(request, obj):
    context = {
        'object': obj,
        'cms_toolbar': request.toolbar,
    }
~~    return render(request, 'cms/toolbar/structure.html', context)


def _handle_no_page(request):
    try:
        resolve('%s$' % request.path)
    except Resolver404 as e:
        exc = Http404(dict(path=request.path, tried=e.args[0]['tried']))
        raise exc
    raise Http404('CMS Page not found: %s' % request.path)


def _render_welcome_page(request):
    context = {
        'cms_version': __version__,
        'cms_edit_on': get_cms_setting('CMS_TOOLBAR_URL__EDIT_ON'),
        'django_debug': settings.DEBUG,
        'next_url': reverse('pages-root'),
    }
    return TemplateResponse(request, "cms/welcome.html", context)



## ... source file continues with no further render examples...

```


## Example 5 from django-filer
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
from django.db import models, router
from django.http import HttpResponse, HttpResponseRedirect
~~from django.shortcuts import get_object_or_404, render
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
from .tools import (
    AdminContext, admin_url_params_encoded, check_files_edit_permissions,


## ... source file abbreviated to get to render examples ...


            'virtual_items': virtual_items,
            'uploader_connections': settings.FILER_UPLOADER_CONNECTIONS,
            'permissions': permissions,
            'permstest': userperms_for_request(folder, request),
            'current_url': request.path,
            'title': _('Directory listing for %(folder_name)s') % {'folder_name': folder.name},
            'search_string': ' '.join(search_terms),
            'q': urlquote(q),
            'show_result_count': show_result_count,
            'folder_children': folder_children,
            'folder_files': folder_files,
            'limit_search_to_folder': limit_search_to_folder,
            'is_popup': popup_status(request),
            'filer_admin_context': AdminContext(request),
            'root_path': reverse('admin:index'),
            'action_form': action_form,
            'actions_on_top': self.actions_on_top,
            'actions_on_bottom': self.actions_on_bottom,
            'actions_selection_counter': self.actions_selection_counter,
            'selection_note': _('0 of %(cnt)s selected') % {'cnt': len(paginated_items.object_list)},
            'selection_note_all': selection_note_all % {'total_count': paginator.count},
            'media': self.media,
            'enable_permissions': settings.FILER_ENABLE_PERMISSIONS,
            'can_make_folder': request.user.is_superuser or (folder.is_root and settings.FILER_ALLOW_REGULAR_USERS_TO_ADD_ROOT_FOLDERS) or permissions.get("has_add_children_permission"),
        })
~~        return render(request, self.directory_listing_template, context)

    def filter_folder(self, qs, terms=()):
        def construct_search(field_name):
            if field_name.startswith('^'):
                return "%s__istartswith" % field_name[1:]
            elif field_name.startswith('='):
                return "%s__iexact" % field_name[1:]
            elif field_name.startswith('@'):
                return "%s__search" % field_name[1:]
            else:
                return "%s__icontains" % field_name

        for term in terms:
            filters = models.Q()
            for filter_ in self.search_fields:
                filters |= models.Q(**{construct_search(filter_): term})
            for filter_ in self.get_owner_filter_lookups():
                filters |= models.Q(**{filter_: term})
            qs = qs.filter(filters)
        return qs

    def filter_file(self, qs, terms=()):
        for term in terms:
            filters = (models.Q(name__icontains=term)


## ... source file abbreviated to get to render examples ...


            return None

        if all_perms_needed or all_protected:
            title = _("Cannot delete files and/or folders")
        else:
            title = _("Are you sure?")

        context = self.admin_site.each_context(request)
        context.update({
            "title": title,
            "instance": current_folder,
            "breadcrumbs_action": _("Delete files and/or folders"),
            "deletable_objects": all_deletable_objects,
            "files_queryset": files_queryset,
            "folders_queryset": folders_queryset,
            "perms_lacking": all_perms_needed,
            "protected": all_protected,
            "opts": opts,
            'is_popup': popup_status(request),
            'filer_admin_context': AdminContext(request),
            "root_path": reverse('admin:index'),
            "app_label": app_label,
            "action_checkbox_name": helpers.ACTION_CHECKBOX_NAME,
        })

~~        return render(
            request,
            "admin/filer/delete_selected_files_confirmation.html",
            context
        )

    delete_files_or_folders.short_description = ugettext_lazy(
        "Delete selected files and/or folders")

    def _format_callback(self, obj, user, admin_site, perms_needed):
        has_admin = obj.__class__ in admin_site._registry
        opts = obj._meta
        if has_admin:
            admin_url = reverse('%s:%s_%s_change'
                                % (admin_site.name,
                                   opts.app_label,
                                   opts.object_name.lower()),
                                None, (quote(obj._get_pk_val()),))
            p = get_delete_permission(opts)
            if not user.has_perm(p):
                perms_needed.add(opts.verbose_name)
            return mark_safe('%s: <a href="%s">%s</a>' %
                             (escape(capfirst(opts.verbose_name)),
                              admin_url,
                              escape(obj)))


## ... source file abbreviated to get to render examples ...


                                          "destination") % ", ".join(conflicting_names))
            elif n:
                self._move_files_and_folders_impl(files_queryset, folders_queryset, destination)
                self.message_user(request, _("Successfully moved %(count)d files and/or folders to folder '%(destination)s'.") % {
                    "count": n,
                    "destination": destination,
                })
            return None

        context = self.admin_site.each_context(request)
        context.update({
            "title": _("Move files and/or folders"),
            "instance": current_folder,
            "breadcrumbs_action": _("Move files and/or folders"),
            "to_move": to_move,
            "destination_folders": folders,
            "files_queryset": files_queryset,
            "folders_queryset": folders_queryset,
            "perms_lacking": perms_needed,
            "opts": opts,
            "root_path": reverse('admin:index'),
            "app_label": app_label,
            "action_checkbox_name": helpers.ACTION_CHECKBOX_NAME,
        })

~~        return render(request, "admin/filer/folder/choose_move_destination.html", context)

    move_files_and_folders.short_description = ugettext_lazy("Move selected files and/or folders")

    def _rename_file(self, file_obj, form_data, counter, global_counter):
        original_basename, original_extension = os.path.splitext(file_obj.original_filename)
        if file_obj.name:
            current_basename, current_extension = os.path.splitext(file_obj.name)
        else:
            current_basename = ""
            current_extension = ""
        file_obj.name = form_data['rename_format'] % {
            'original_filename': file_obj.original_filename,
            'original_basename': original_basename,
            'original_extension': original_extension,
            'current_filename': file_obj.name or "",
            'current_basename': current_basename,
            'current_extension': current_extension,
            'current_folder': getattr(file_obj.folder, 'name', ''),
            'counter': counter + 1,  # 1-based
            'global_counter': global_counter + 1,  # 1-based
        }
        file_obj.save()

    def _rename_files(self, files, form_data, global_counter):


## ... source file abbreviated to get to render examples ...


                if files_queryset.count() + folders_queryset.count():
                    n = self._rename_files_impl(files_queryset, folders_queryset, form.cleaned_data, 0)
                    self.message_user(request, _("Successfully renamed %(count)d files.") % {
                        "count": n,
                    })
                return None
        else:
            form = RenameFilesForm()

        context = self.admin_site.each_context(request)
        context.update({
            "title": _("Rename files"),
            "instance": current_folder,
            "breadcrumbs_action": _("Rename files"),
            "to_rename": to_rename,
            "rename_form": form,
            "files_queryset": files_queryset,
            "folders_queryset": folders_queryset,
            "perms_lacking": perms_needed,
            "opts": opts,
            "root_path": reverse('admin:index'),
            "app_label": app_label,
            "action_checkbox_name": helpers.ACTION_CHECKBOX_NAME,
        })

~~        return render(request, "admin/filer/folder/choose_rename_format.html", context)

    rename_files.short_description = ugettext_lazy("Rename files")

    def _generate_new_filename(self, filename, suffix):
        basename, extension = os.path.splitext(filename)
        return basename + suffix + extension

    def _copy_file(self, file_obj, destination, suffix, overwrite):
        if overwrite:
            raise NotImplementedError


        filename = self._generate_new_filename(file_obj.file.name, suffix)

        file_obj.pk = None
        file_obj.id = None
        file_obj.save()
        file_obj.folder = destination
        file_obj._file_data_changed_hint = False  # no need to update size, sha1, etc.
        file_obj.file = file_obj._copy_file(filename)
        file_obj.original_filename = self._generate_new_filename(file_obj.original_filename, suffix)
        file_obj.save()

    def _copy_files(self, files, destination, suffix, overwrite):


## ... source file abbreviated to get to render examples ...


            selected_destination_folder = int(request.POST.get('destination', 0))
        except ValueError:
            if current_folder:
                selected_destination_folder = current_folder.pk
            else:
                selected_destination_folder = 0

        context = self.admin_site.each_context(request)
        context.update({
            "title": _("Copy files and/or folders"),
            "instance": current_folder,
            "breadcrumbs_action": _("Copy files and/or folders"),
            "to_copy": to_copy,
            "destination_folders": folders,
            "selected_destination_folder": selected_destination_folder,
            "copy_form": form,
            "files_queryset": files_queryset,
            "folders_queryset": folders_queryset,
            "perms_lacking": perms_needed,
            "opts": opts,
            "root_path": reverse('admin:index'),
            "app_label": app_label,
            "action_checkbox_name": helpers.ACTION_CHECKBOX_NAME,
        })

~~        return render(request, "admin/filer/folder/choose_copy_destination.html", context)

    copy_files_and_folders.short_description = ugettext_lazy("Copy selected files and/or folders")

    def _check_resize_perms(self, request, files_queryset, folders_queryset):
        try:
            check_files_read_permissions(request, files_queryset)
            check_folder_read_permissions(request, folders_queryset)
            check_files_edit_permissions(request, files_queryset)
        except PermissionDenied:
            return True
        return False

    def _list_folders_to_resize(self, request, folders):
        for fo in folders:
            children = list(self._list_folders_to_resize(request, fo.children.all()))
            children.extend([self._format_callback(f, request.user, self.admin_site, set()) for f in sorted(fo.files) if isinstance(f, Image)])
            if children:
                yield self._format_callback(fo, request.user, self.admin_site, set())
                yield children

    def _list_all_to_resize(self, request, files_queryset, folders_queryset):
        to_resize = list(self._list_folders_to_resize(request, folders_queryset))
        to_resize.extend([self._format_callback(f, request.user, self.admin_site, set()) for f in sorted(files_queryset) if isinstance(f, Image)])
        return to_resize


## ... source file abbreviated to get to render examples ...


                    form.cleaned_data['upscale'] = form.cleaned_data['thumbnail_option'].upscale
                if files_queryset.count() + folders_queryset.count():
                    n = self._resize_images_impl(files_queryset, folders_queryset, form.cleaned_data)
                    self.message_user(request, _("Successfully resized %(count)d images.") % {"count": n, })
                return None
        else:
            form = ResizeImagesForm()

        context = self.admin_site.each_context(request)
        context.update({
            "title": _("Resize images"),
            "instance": current_folder,
            "breadcrumbs_action": _("Resize images"),
            "to_resize": to_resize,
            "resize_form": form,
            "cmsplugin_enabled": 'cmsplugin_filer_image' in django_settings.INSTALLED_APPS,
            "files_queryset": files_queryset,
            "folders_queryset": folders_queryset,
            "perms_lacking": perms_needed,
            "opts": opts,
            "root_path": reverse('admin:index'),
            "app_label": app_label,
            "action_checkbox_name": helpers.ACTION_CHECKBOX_NAME,
        })

~~        return render(request, "admin/filer/folder/choose_images_resize_options.html", context)

    resize_images.short_description = ugettext_lazy("Resize selected images")



## ... source file continues with no further render examples...

```


## Example 6 from django-guardian
[django-guardian](https://github.com/django-guardian/django-guardian)
([project documentation](https://django-guardian.readthedocs.io/en/stable/)
and
[PyPI page](https://pypi.org/project/django-guardian/))
provides per-object permissions in [Django](/django.html) projects
by enhancing the existing authentication backend. The project's code
is open source under the
[MIT license](https://github.com/django-guardian/django-guardian/blob/devel/LICENSE).

[**django-guardian / guardian / admin.py**](https://github.com/django-guardian/django-guardian/blob/devel/guardian/./admin.py)

```python
# admin.py
from collections import OrderedDict

from django import forms
from django.conf import settings
from django.contrib import admin, messages
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth import get_user_model
~~from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, path
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext
from guardian.forms import GroupObjectPermissionsForm, UserObjectPermissionsForm
from django.contrib.auth.models import Group
from guardian.shortcuts import (get_group_perms, get_groups_with_perms, get_perms_for_model, get_user_perms,
                                get_users_with_perms)


class AdminUserObjectPermissionsForm(UserObjectPermissionsForm):

    def get_obj_perms_field_widget(self):
        return FilteredSelectMultiple(_("Permissions"), False)


class AdminGroupObjectPermissionsForm(GroupObjectPermissionsForm):

    def get_obj_perms_field_widget(self):
        return FilteredSelectMultiple(_("Permissions"), False)


class GuardedModelAdminMixin:
    change_form_template = \
        'admin/guardian/model/change_form.html'


## ... source file abbreviated to get to render examples ...


                request)(request.POST)
            info = (
                self.admin_site.name,
                self.model._meta.app_label,
                self.model._meta.model_name,
            )
            if group_form.is_valid():
                group_id = group_form.cleaned_data['group'].id
                url = reverse(
                    '%s:%s_%s_permissions_manage_group' % info,
                    args=[obj.pk, group_id]
                )
                return redirect(url)
        else:
            user_form = self.get_obj_perms_user_select_form(request)()
            group_form = self.get_obj_perms_group_select_form(request)()

        context = self.get_obj_perms_base_context(request, obj)
        context['users_perms'] = users_perms
        context['groups_perms'] = groups_perms
        context['user_form'] = user_form
        context['group_form'] = group_form

        request.current_app = self.admin_site.name

~~        return render(request, self.get_obj_perms_manage_template(), context)

    def get_obj_perms_manage_template(self):
        if 'grappelli' in settings.INSTALLED_APPS:
            return 'admin/guardian/contrib/grappelli/obj_perms_manage.html'
        return self.obj_perms_manage_template

    def obj_perms_manage_user_view(self, request, object_pk, user_id):
        if not self.has_change_permission(request, None):
            post_url = reverse('admin:index', current_app=self.admin_site.name)
            return redirect(post_url)

        user = get_object_or_404(get_user_model(), pk=user_id)
        obj = get_object_or_404(self.get_queryset(request), pk=object_pk)
        form_class = self.get_obj_perms_manage_user_form(request)
        form = form_class(user, obj, request.POST or None)

        if request.method == 'POST' and form.is_valid():
            form.save_obj_perms()
            msg = gettext("Permissions saved.")
            messages.success(request, msg)
            info = (
                self.admin_site.name,
                self.model._meta.app_label,
                self.model._meta.model_name,
            )
            url = reverse(
                '%s:%s_%s_permissions_manage_user' % info,
                args=[obj.pk, user.pk]
            )
            return redirect(url)

        context = self.get_obj_perms_base_context(request, obj)
        context['user_obj'] = user
        context['user_perms'] = get_user_perms(user, obj)
        context['form'] = form

        request.current_app = self.admin_site.name

~~        return render(request, self.get_obj_perms_manage_user_template(), context)

    def get_obj_perms_manage_user_template(self):
        if 'grappelli' in settings.INSTALLED_APPS:
            return 'admin/guardian/contrib/grappelli/obj_perms_manage_user.html'
        return self.obj_perms_manage_user_template

    def get_obj_perms_user_select_form(self, request):
        return UserManage

    def get_obj_perms_group_select_form(self, request):
        return GroupManage

    def get_obj_perms_manage_user_form(self, request):
        return AdminUserObjectPermissionsForm

    def obj_perms_manage_group_view(self, request, object_pk, group_id):
        if not self.has_change_permission(request, None):
            post_url = reverse('admin:index', current_app=self.admin_site.name)
            return redirect(post_url)

        group = get_object_or_404(Group, id=group_id)
        obj = get_object_or_404(self.get_queryset(request), pk=object_pk)
        form_class = self.get_obj_perms_manage_group_form(request)
        form = form_class(group, obj, request.POST or None)

        if request.method == 'POST' and form.is_valid():
            form.save_obj_perms()
            msg = gettext("Permissions saved.")
            messages.success(request, msg)
            info = (
                self.admin_site.name,
                self.model._meta.app_label,
                self.model._meta.model_name,
            )
            url = reverse(
                '%s:%s_%s_permissions_manage_group' % info,
                args=[obj.pk, group.id]
            )
            return redirect(url)

        context = self.get_obj_perms_base_context(request, obj)
        context['group_obj'] = group
        context['group_perms'] = get_group_perms(group, obj)
        context['form'] = form

        request.current_app = self.admin_site.name

~~        return render(request, self.get_obj_perms_manage_group_template(), context)

    def get_obj_perms_manage_group_template(self):
        if 'grappelli' in settings.INSTALLED_APPS:
            return 'admin/guardian/contrib/grappelli/obj_perms_manage_group.html'
        return self.obj_perms_manage_group_template

    def get_obj_perms_manage_group_form(self, request):
        return AdminGroupObjectPermissionsForm


class GuardedModelAdmin(GuardedModelAdminMixin, admin.ModelAdmin):


class UserManage(forms.Form):
    user = forms.CharField(label=_("User identification"),
                           max_length=200,
                           error_messages={'does_not_exist': _(
                               "This user does not exist")},
                           help_text=_(
                               'Enter a value compatible with User.USERNAME_FIELD')
                           )

    def clean_user(self):
        identification = self.cleaned_data['user']


## ... source file continues with no further render examples...

```


## Example 7 from django-haystack
[django-haystack](https://github.com/django-haystack/django-haystack)
([project website](http://haystacksearch.org/) and
[PyPI page](https://pypi.org/project/django-haystack/))
is a search abstraction layer that separates the Python search code
in a [Django](/django.html) web application from the search engine
implementation that it runs on, such as
[Apache Solr](http://lucene.apache.org/solr/),
[Elasticsearch](https://www.elastic.co/)
or [Whoosh](https://whoosh.readthedocs.io/en/latest/intro.html).

The django-haystack project is open source under the
[BSD license](https://github.com/django-haystack/django-haystack/blob/master/LICENSE).

[**django-haystack / haystack / admin.py**](https://github.com/django-haystack/django-haystack/blob/master/haystack/./admin.py)

```python
# admin.py
from django.contrib.admin.options import ModelAdmin, csrf_protect_m
from django.contrib.admin.views.main import SEARCH_VAR, ChangeList
from django.core.exceptions import PermissionDenied
from django.core.paginator import InvalidPage, Paginator
~~from django.shortcuts import render
from django.utils.encoding import force_str
from django.utils.translation import ungettext

from haystack import connections
from haystack.constants import DEFAULT_ALIAS
from haystack.query import SearchQuerySet
from haystack.utils import get_model_ct_tuple


class SearchChangeList(ChangeList):
    def __init__(self, **kwargs):
        self.haystack_connection = kwargs.pop("haystack_connection", DEFAULT_ALIAS)
        super(SearchChangeList, self).__init__(**kwargs)

    def get_results(self, request):
        if SEARCH_VAR not in request.GET:
            return super(SearchChangeList, self).get_results(request)

        sqs = (
            SearchQuerySet(self.haystack_connection)
            .models(self.model)
            .auto_query(request.GET[SEARCH_VAR])
            .load_all()
        )


## ... source file abbreviated to get to render examples ...


            "%(total_count)s selected",
            "All %(total_count)s selected",
            changelist.result_count,
        )

        context = {
            "module_name": force_str(self.model._meta.verbose_name_plural),
            "selection_note": selection_note % {"count": len(changelist.result_list)},
            "selection_note_all": selection_note_all
            % {"total_count": changelist.result_count},
            "title": changelist.title,
            "is_popup": changelist.is_popup,
            "cl": changelist,
            "media": media,
            "has_add_permission": self.has_add_permission(request),
            "opts": changelist.opts,
            "app_label": self.model._meta.app_label,
            "action_form": action_form,
            "actions_on_top": self.actions_on_top,
            "actions_on_bottom": self.actions_on_bottom,
            "actions_selection_counter": getattr(self, "actions_selection_counter", 0),
        }
        context.update(extra_context or {})
        request.current_app = self.admin_site.name
        app_name, model_name = get_model_ct_tuple(self.model)
~~        return render(
            request,
            self.change_list_template
            or [
                "admin/%s/%s/change_list.html" % (app_name, model_name),
                "admin/%s/change_list.html" % app_name,
                "admin/change_list.html",
            ],
            context,
        )


class SearchModelAdmin(SearchModelAdminMixin, ModelAdmin):
    pass



## ... source file continues with no further render examples...

```


## Example 8 from django-oauth-toolkit
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

[**django-oauth-toolkit / oauth2_provider / views / base.py**](https://github.com/jazzband/django-oauth-toolkit/blob/master/oauth2_provider/views/base.py)

```python
# base.py
import json
import logging
import urllib.parse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
~~from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, View

from ..exceptions import OAuthToolkitError
from ..forms import AllowForm
from ..http import OAuth2ResponseRedirect
from ..models import get_access_token_model, get_application_model
from ..scopes import get_scopes_backend
from ..settings import oauth2_settings
from ..signals import app_authorized
from .mixins import OAuthLibMixin


log = logging.getLogger("oauth2_provider")


class BaseAuthorizationView(LoginRequiredMixin, OAuthLibMixin, View):

    def dispatch(self, request, *args, **kwargs):
        self.oauth2_data = {}


## ... source file abbreviated to get to render examples ...


            return self.error_response(error, application)

        return self.render_to_response(self.get_context_data(**kwargs))

    def redirect(self, redirect_to, application, token=None):

        if not redirect_to.startswith("urn:ietf:wg:oauth:2.0:oob"):
            return super().redirect(redirect_to, application)

        parsed_redirect = urllib.parse.urlparse(redirect_to)
        code = urllib.parse.parse_qs(parsed_redirect.query)["code"][0]

        if redirect_to.startswith("urn:ietf:wg:oauth:2.0:oob:auto"):

            response = {
                    "access_token": code,
                    "token_uri": redirect_to,
                    "client_id": application.client_id,
                    "client_secret": application.client_secret,
                    "revoke_uri": reverse("oauth2_provider:revoke-token"),
                    }

            return JsonResponse(response)

        else:
~~            return render(
                    request=self.request,
                    template_name="oauth2_provider/authorized-oob.html",
                    context={
                        "code": code,
                        },
                    )


@method_decorator(csrf_exempt, name="dispatch")
class TokenView(OAuthLibMixin, View):
    server_class = oauth2_settings.OAUTH2_SERVER_CLASS
    validator_class = oauth2_settings.OAUTH2_VALIDATOR_CLASS
    oauthlib_backend_class = oauth2_settings.OAUTH2_BACKEND_CLASS

    @method_decorator(sensitive_post_parameters("password"))
    def post(self, request, *args, **kwargs):
        url, headers, body, status = self.create_token_response(request)
        if status == 200:
            access_token = json.loads(body).get("access_token")
            if access_token is not None:
                token = get_access_token_model().objects.get(
                    token=access_token)
                app_authorized.send(
                    sender=self, request=request,


## ... source file continues with no further render examples...

```


## Example 9 from django-sql-explorer
[django-sql-explorer](https://github.com/groveco/django-sql-explorer)
([PyPI page](https://pypi.org/project/django-sql-explorer/0.2/)),
also referred to as "SQL Explorer",
is a code library for the [Django](/django.html) Admin that allows
approved, authenticated users to view and execute direct database SQL
queries. The tool keeps track of executed queries so users can share them
with each other, as well as export results to downloadable formats.
django-sql-explorer is provided as open source under the
[MIT license](https://github.com/groveco/django-sql-explorer/blob/master/LICENSE).

[**django-sql-explorer / explorer / views.py**](https://github.com/groveco/django-sql-explorer/blob/master/explorer/./views.py)

```python
# views.py
import re
import six
from collections import Counter

try:
    from django.urls import reverse_lazy
except ImportError:
    from django.core.urlresolvers import reverse_lazy

import django
from django.db import DatabaseError
from django.db.models import Count
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
~~from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, DeleteView
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import LoginView

from explorer import app_settings
from explorer.connections import connections
from explorer.exporters import get_exporter_class
from explorer.forms import QueryForm
from explorer.models import Query, QueryLog, MSG_FAILED_BLACKLIST
from explorer.tasks import execute_query
from explorer.utils import (
    url_get_rows,
    url_get_query_id,
    url_get_log_id,
    url_get_params,
    safe_login_prompt,
    fmt_sql,
    allowed_query_pks,
    url_get_show,
    url_get_fullscreen
)

from explorer.schema import schema_info
from explorer import permissions


class ExplorerContextMixin(object):

    def gen_ctx(self):
        return {'can_view': app_settings.EXPLORER_PERMISSION_VIEW(self.request.user),
                'can_change': app_settings.EXPLORER_PERMISSION_CHANGE(self.request.user)}

    def get_context_data(self, **kwargs):
        ctx = super(ExplorerContextMixin, self).get_context_data(**kwargs)
        ctx.update(self.gen_ctx())
        return ctx

    def render_template(self, template, ctx):
        ctx.update(self.gen_ctx())
~~        return render(self.request, template, ctx)


class PermissionRequiredMixin(object):

    permission_required = None

    def get_permission_required(self):
        if self.permission_required is None:
            raise ImproperlyConfigured(
                '{0} is missing the permission_required attribute. Define {0}.permission_required, or override '
                '{0}.get_permission_required().'.format(self.__class__.__name__)
            )
        return self.permission_required

    def has_permission(self, request, *args, **kwargs):
        perms = self.get_permission_required()
        handler = getattr(permissions, perms)  # TODO: fix the case when the perms is
        return handler(request, *args, **kwargs)

    def handle_no_permission(self, request):
        return SafeLoginView.as_view(
            extra_context={'title': 'Log in', REDIRECT_FIELD_NAME: request.get_full_path()})(request)

    def dispatch(self, request, *args, **kwargs):


## ... source file abbreviated to get to render examples ...



    permission_required = 'view_permission'

    def post(self, request, query_id, *args, **kwargs):
        if request.is_ajax():
            email = request.POST.get('email', None)
            if email:
                execute_query.delay(query_id, email)
                return JsonResponse({'message': 'message was sent successfully'})
        return JsonResponse({}, status=403)


class SchemaView(PermissionRequiredMixin, View):
    permission_required = 'change_permission'

    @method_decorator(xframe_options_sameorigin)
    def dispatch(self, *args, **kwargs):
        return super(SchemaView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        connection = kwargs.get('connection')
        if connection not in connections:
            raise Http404
        schema = schema_info(connection)
        if schema:
~~            return render(None, 'explorer/schema.html',
                                      {'schema': schema_info(connection)})
        else:
~~            return render(None, 'explorer/schema_building.html')


@require_POST
def format_sql(request):
    sql = request.POST.get('sql', '')
    formatted = fmt_sql(sql)
    return JsonResponse({"formatted": formatted})


class ListQueryView(PermissionRequiredMixin, ExplorerContextMixin, ListView):

    permission_required = 'view_permission_list'

    def recently_viewed(self):
        qll = QueryLog.objects.filter(run_by_user=self.request.user, query_id__isnull=False).order_by(
            '-run_at').select_related('query')
        ret = []
        tracker = []
        for ql in qll:
            if len(ret) == app_settings.EXPLORER_RECENT_QUERY_COUNT:
                break

            if ql.query_id not in tracker:
                ret.append(ql)


## ... source file abbreviated to get to render examples ...


class PlayQueryView(PermissionRequiredMixin, ExplorerContextMixin, View):

    permission_required = 'change_permission'

    def get(self, request):
        if url_get_query_id(request):
            query = get_object_or_404(Query, pk=url_get_query_id(request))
            return self.render_with_sql(request, query, run_query=False)

        if url_get_log_id(request):
            log = get_object_or_404(QueryLog, pk=url_get_log_id(request))
            query = Query(sql=log.sql, title="Playground", connection=log.connection)
            return self.render_with_sql(request, query)

        return self.render()

    def post(self, request):
        sql = request.POST.get('sql')
        show = url_get_show(request)
        query = Query(sql=sql, title="Playground", connection=request.POST.get('connection'))
        passes_blacklist, failing_words = query.passes_blacklist()
        error = MSG_FAILED_BLACKLIST % ', '.join(failing_words) if not passes_blacklist else None
        run_query = not bool(error) if show else False
        return self.render_with_sql(request, query, run_query=run_query, error=error)

~~    def render(self):
        return self.render_template('explorer/play.html', {'title': 'Playground', 'form': QueryForm()})

    def render_with_sql(self, request, query, run_query=True, error=None):
        rows = url_get_rows(request)
        fullscreen = url_get_fullscreen(request)
        template = 'fullscreen' if fullscreen else 'play'
        form = QueryForm(request.POST if len(request.POST) else None, instance=query)
        return self.render_template('explorer/%s.html' % template, query_viewmodel(request.user,
                                                                                   query,
                                                                                   title="Playground",
                                                                                   run_query=run_query,
                                                                                   error=error,
                                                                                   rows=rows,
                                                                                   form=form))


class QueryView(PermissionRequiredMixin, ExplorerContextMixin, View):

    permission_required = 'view_permission'

    def get(self, request, query_id):
        query, form = QueryView.get_instance_and_form(request, query_id)
        query.save()  # updates the modified date
        show = url_get_show(request)


## ... source file continues with no further render examples...

```


## Example 10 from django-wiki
[django-wiki](https://github.com/django-wiki/django-wiki)
([project documentation](https://django-wiki.readthedocs.io/en/master/),
[demo](https://demo.django-wiki.org/),
and [PyPI page](https://pypi.org/project/django-wiki/))
is a wiki system code library for [Django](/django.html)
projects that makes it easier to create user-editable content.
The project aims to provide necessary core features and then
have an easy plugin format for additional features, rather than
having every exhaustive feature built into the core system.
django-wiki is a rewrite of an earlier now-defunct project
named [django-simplewiki](https://code.google.com/p/django-simple-wiki/).

The code for django-wiki is provided as open source under the
[GNU General Public License 3.0](https://github.com/django-wiki/django-wiki/blob/master/COPYING).

[**django-wiki / src/wiki / views / accounts.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/views/accounts.py)

```python
# accounts.py
from django.conf import settings as django_settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
~~from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.generic import CreateView
from django.views.generic import FormView
from django.views.generic import UpdateView
from django.views.generic import View
from wiki import forms
from wiki.conf import settings

User = get_user_model()


class Signup(CreateView):
    model = User
    form_class = forms.UserCreationForm
    template_name = "wiki/accounts/signup.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_anonymous and not request.user.is_superuser:
            return redirect("wiki:root")
        if not settings.ACCOUNT_HANDLING:
            return redirect(settings.SIGNUP_URL)
        if not request.user.is_superuser and not settings.ACCOUNT_SIGNUP_ALLOWED:
            c = {"error_msg": _("Account signup is only allowed for administrators.")}
~~            return render(request, "wiki/error.html", context=c)

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["honeypot_class"] = context["form"].honeypot_class
        context["honeypot_jsfunction"] = context["form"].honeypot_jsfunction
        return context

    def get_success_url(self, *args):
        messages.success(
            self.request, _("You are now signed up... and now you can sign in!")
        )
        return reverse("wiki:login")


class Logout(View):
    def dispatch(self, request, *args, **kwargs):
        if not settings.ACCOUNT_HANDLING:
            return redirect(settings.LOGOUT_URL)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        auth_logout(request)


## ... source file continues with no further render examples...

```


## Example 11 from dmd-interpreter
[dmd-interpreter](https://github.com/mitchalexbailey/dmd-interpreter)
([running web app](http://www.dmd.nl/DOVE))
is a Python tool to aggregate clinically relevant information related
to variants in the DMD gene and display that [data](/data.html) to a user
with a [Django](/django.html) web application.

[**dmd-interpreter / interpreter / views.py**](https://github.com/mitchalexbailey/dmd-interpreter/blob/master/interpreter/./views.py)

```python
# views.py
~~from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from .forms import IndexForm, ACMGForm

from interpreter_functions import *
import os,sys
import subprocess
import csv
import re
import pprint

interpreter_dir = os.path.dirname(__file__)

def index(request):
	if request.method == "POST":
		user = request.POST.get('user', None)
~~	return render(request, 'index.html')


def results(request):
	if request.method == 'POST':
		mut = request.POST.get('mutation', None)

	ucsc_info = [12, 'NM_004006', 'chrX', '-', 31137344, 33229673, 31140035, 33229429, 79, '31137344,31144758,31152218,31164407,31165391,31187559,31190464,31191655,31196048,31196785,31198486,31200854,31222077,31224698,31227614,31241163,31279071,31341714,31366672,31462597,31496222,31497099,31514904,31525397,31645789,31676106,31697491,31747747,31792076,31838091,31854834,31893307,31947712,31950196,31986455,32235032,32305645,32328198,32360216,32361250,32364059,32366522,32380904,32382698,32383136,32398626,32404426,32407617,32408187,32429868,32456357,32459296,32466572,32472778,32481555,32482702,32486614,32490280,32503035,32509393,32519871,32536124,32563275,32583818,32591646,32591861,32613873,32632419,32662248,32663080,32715986,32717228,32827609,32834584,32841411,32862899,32867844,33038255,33229398,', '31140047,31144790,31152311,31164531,31165635,31187718,31190530,31191721,31196087,31196922,31198598,31201021,31222235,31224784,31227816,31241238,31279133,31341775,31366751,31462744,31496491,31497220,31515061,31525570,31645979,31676261,31697703,31747865,31792309,31838200,31854939,31893490,31947862,31950344,31986631,32235180,32305818,32328393,32360399,32361403,32364197,32366645,32381075,32382827,32383316,32398797,32404582,32407791,32408298,32430030,32456507,32459431,32466755,32472949,32481711,32482816,32486827,32490426,32503216,32509635,32519959,32536248,32563451,32583998,32591754,32591963,32613993,32632570,32662430,32663269,32716115,32717410,32827728,32834757,32841504,32862977,32867937,33038317,33229673,', 0, 'DMD', 'cmpl', 'cmpl', '0,1,1,0,2,2,2,2,2,0,2,0,1,2,1,1,2,1,0,0,1,0,2,0,2,0,1,0,1,0,0,0,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,2,0,0,0,0,0,2,0,0,0,1,2,0,0,0,0,1,0,']
	


	f = open(os.path.join(interpreter_dir, "rescue_esesites.txt"))
	ese_sites = []
	for line in f:
	    temp = ''
	    for char in line:
	        if char != "\n":
	            temp += char
	        temp = ''.join(temp)
	    ese_sites += [temp]
	f.close()

	f = open(os.path.join(interpreter_dir, "esssites.txt"))
	ess_sites = []
	for line in f:


## ... source file abbreviated to get to render examples ...


	provean = 'Not missense'
	metasvm = 'Not missense'
	nsfp_score = ''
	nsfp_message = ''
	cv = ''
	consequence = ''
	consequence_statement = ''
	ese_message = ''
	esefinder = ''
	rescueese = ''
	ess_message = ''
	splice_message = ''
	splice_message2 = ''
	motif_message = ''
	ds = ''
	splice_result = []
	long_aa_change = []
	readthrough_elig = "<c style='color:red'><b>Not eligible</b></c>"

	ex_input = exoninput(mut)
	mutype, search = type_inp(mut, ex_input)
	num_list, intron_list = parse(mut, mutype, exon_positions, ex_input)


	if mutype == "Invalid mutation" and len(num_list) == 0:
~~		return render(request, 'index.html',{'success':False})
	else:
		pass
	
	
	for num in num_list:
		if int(num) > 3685*3 and not ex_input: #AA length *3
			past_max = True
		elif int(num) > len_ref:
			past_max = True
		else:
			pass
	

	intron_only = intron_count(intron_list, num_list)
	

	if (mutype == "Deletion" or mutype == "Duplication") and "c." not in mut and len(num_list) > 0 and not ex_input and "Nucleotide" not in mut:
		if max(num_list) < 80 and not ex_input:
			with open(os.path.join(interpreter_dir, 'templates/triage.html'), 'w') as g:
				num_list = re.findall("\d+", mut)
				g.write("""<div class='container' style='text-align:center'><h1>You entered: '<c style='color:red'>""")
				g.write(mut)
				g.write("""</c>'</h1><br><h2>Did you mean...<br><br>'<i>""")		
				temp = ''
				temp += mutype
				if len(num_list) == 1:
					temp += " of exon "
					temp += str(num_list[0])
				if len(num_list) > 1:
					temp += " of exons "
					temp += str(min(num_list))
					temp += "-"
					temp += str(max(num_list))
				g.write(temp)
				g.write("""</i>'?</h2><br><div class='row'><form action="{% url 'interpreter:results' %}" method="post"> {% csrf_token %}{% csrf_token %}	<button name='mutation' id='mutation' value=' """)
				g.write(temp)
				g.write("""' class='btn-success btn-lg'>Yes, I meant exon.<br></button><button name='mutation' id='mutation' value='(Nucleotide) """)
				g.write(mut)
				g.write("""'class='btn-danger btn-lg'>No, I meant nucleotide.<br></button></form></div></div></body>""")
			g.closed
~~			return render(request, 'index.html', {'triage':True})



	if past_max or mutype == "Invalid mutation":
		with open(os.path.join(interpreter_dir, 'templates/triage.html'), 'w') as g:
			g.write("""<div class='container' style='text-align:center'><h1>You entered: '<c style='color:red'>""")
			g.write(mut)
			g.write("""</c>'<br><br>Did you mean...<br>""")	

			if past_max:
				g.write(("""</h1><h2>A smaller number?</h2><br>You entered: <c style='color:red'>%s""" % str(max(num_list))) + """</c><br>Which is larger than the length of the <i>DMD, Dp427m</i> coding sequence (11055 nt)<br><br>Please enter your revised mutation below, or <a href="{% url 'interpreter:index' %}">return to the previous page</a> to try the "Exon deletion selector" feature.<br><br><form action="{% url 'interpreter:results' %}" method="post"> {% csrf_token %}<input type = "text" id='userAnswer' name = "mutation" id='mutation' style='height:70px;width:100%;font-size:24pt;'/><br><br><button type = "submit" style = 'height:70px;width:150px;font-size:24px;align:center' class = 'btn btn-lg btn-primary'>Interpret</button></form></div></body>""")

			if mutype == "Invalid mutation" and not past_max and len(num_list)>0:# and not ex_input:   
				tridel = "Deletion of Nucleotide(s) "
				tridelex = "Deletion of Exon(s) "
				tridup = "Duplication of Nucleotide(s) "
				tridupex = "Duplication of Exon(s) "
				triins = "Insertion at Nucleotide position(s) "
				tridelins = "Deletion/Insertion at Nucleotide position(s) "
				tripoint = "Point mutation at Nucleotide position(s) "
				if len(num_list) == 1:
					tridel += str(num_list[0])
					tridup += str(num_list[0])
					tridelex += str(num_list[0])


## ... source file abbreviated to get to render examples ...


				
				g.write("</div><div class='row'>")

				g.write("</button><button name='mutation' id='mutation' value='")
				g.write(tripoint)
				g.write("' class='btn-primary btn-lg'>")
				g.write(tripoint)	

				g.write("</div><div class='row'>")

				g.write("</button><button name='mutation' id='mutation' value='")
				g.write(triins)
				g.write("' class='btn-primary btn-lg'>")
				g.write(triins)	

				g.write("</div><div class='row'>")

				g.write("</button><button name='mutation' id='mutation' value='")
				g.write(tridelins)
				g.write("' class='btn-primary btn-lg'>")
				g.write(tridelins)	

				g.write("""</div></form></div>""")		

		g.closed
~~		return render(request, 'index.html', {'triage':True})

	if mutype != "Invalid mutation" and len(num_list) == 0 and not intron_only:
		with open(os.path.join(interpreter_dir, 'templates/triage.html'), 'w') as g:
			g.write("""<div class='container' style='text-align:center'><h1>You entered: '<c style='color:red'>""")
			g.write(mut)
			g.write("</c>'</h1><br><br><h2>This mutation type (")
			g.write(mutype)
			g.write(""") requires a position to be interpreted.</h2><br><br>Please complete the mutation in the box below, or <a href="{% url 'interpreter:index' %}">return to the previous page</a> to try the "Exon deletion selector" feature.<br><br><form action="{% url 'interpreter:results' %}" method="post"> {% csrf_token %}<input type = "text" id='userAnswer' name = "mutation" id='mutation' value='""")
			try:
				g.write(pm_pre)
			except:
				pass
			g.write(search)
			try:
				g.write(pm_change)
			except:
				pass
			g.write(""" of ' style='height:70px;width:100%;font-size:24pt;'/> <br> *Note that the symbol '>' denotes point mutation*<br><br><button type = "submit" style = 'height:70px;width:150px;font-size:24px;align:center' class = 'btn btn-lg btn-primary'>Interpret</button></form></div>""")
		g.closed
~~		return render(request, 'index.html', {'triage':True})

	if not past_max and mutype != "Invalid mutation": # and len(num_list) != 0:       
		if intron_only:
			missense = False
			nonsense = False
			silent = True
			frame_shift = False
			length_mutation, pm_change, pm_pre = get_length(mut, mutype, num_list, mut, ex_input, reference_cdna)
			positions_in_genomic1, positions_in_genomic2, positions_in_genomic3 = cdna2gen(num_list, exon_positions, genomic_positions1, genomic_positions2, genomic_positions3, intron_list)				
			ghgvs, ghgvs19 = HGVS(positions_in_genomic2, positions_in_genomic3, mutype, search, length_mutation, ex_input, [[],[]], pm_change, pm_pre, True)

			
			if mutype == "Point mutation" and len(pm_pre) == 0:
				if mutype == "Point mutation" or mutype == "Deletion/Insertion":
					if len(num_list) == 1:
						pm_pre = genomic_dna[min(positions_in_genomic1)]
					if len(num_list)>1:
						pm_pre = genomic_dna[min(positions_in_genomic1):max(positions_in_genomic1)]
				else:
					if len(num_list) == 1:
						pm_change = genomic_dna[min(positions_in_genomic1)]
					if len(num_list)>1 and length_mutation < 4:
						pm_change = genomic_dna[min(positions_in_genomic1):max(positions_in_genomic1)]
			cDNA, mut_genomic_dna =  alter_cDNA(reference_cdna, num_list, positions_in_genomic1, length_mutation, mutype, pm_change, genomic_dna, intron_only)


## ... source file abbreviated to get to render examples ...


					if mutype == "Deletion" or mutype == "Duplication":
						if len(num_list) == 1:
							pm_change = genomic_dna[min(positions_in_genomic1)]
						if len(num_list)>1 and length_mutation < 4:
							pm_change = genomic_dna[min(positions_in_genomic1)-1:max(positions_in_genomic1)]
				cDNA, mut_genomic_dna = alter_cDNA(reference_cdna, num_list, positions_in_genomic1, length_mutation, mutype, pm_change, genomic_dna, intron_only)
				if ("Insertion" in mutype or mutype == "Point mutation") and len(pm_change) == 0:
					with open(os.path.join(interpreter_dir, 'templates/triage.html'), 'w') as g:
						g.write("""<div class='container' style='text-align:center'><h1>You entered: '<c style='color:red'>""")
						g.write(mut)
						g.write("""</c>'<h1><h2>This mutation type requires that you input the inserted nucleotides (i.e. an A, T, G, C or combination thereof).</h2><br><br>Please add the inserted bases in the box below, or <a href="{% url 'interpreter:index' %}">return to the previous page</a> to try the "Exon deletion selector" feature.<br><br><form action="{% url 'interpreter:results' %}" method="post"> {% csrf_token %}<input type = "text" id='userAnswer' name = "mutation" id='mutation' value='c.""")
						if len(num_list) == 1:
							g.write(str(num_list[0]))
						if len(num_list) > 1:
							g.write(str(min(num_list)))
							g.write("_")
							g.write(str(max(num_list)))
						if mutype == "Point mutation":
							try:
								g.write(pm_pre)
							except:
								g.write(" ")
						g.write(search)
						g.write("""' style='height:70px;width:100%;font-size:24pt;'/><br><br><button type = "submit" style = 'height:70px;width:150px;font-size:24px;align:center' class = 'btn btn-lg btn-primary'>Interpret</button></form></div>""")
					g.closed
~~					return render(request, 'index.html', {'triage':True})
				frame_shift = frame(length_mutation, mutype, num_list)
				exon_numbers = []
				exon_ints = []
				if (mutype == "Deletion" or mutype == "Duplication"):
					exon_numbers, part = exons(num_list, exon_positions, ex_input, mut, part)
					if len(exon_numbers) != 0:
						for item in exon_numbers:
							exon_ints += [int(item)]
							temp = str(exon_numbers[0]), "-", str(exon_numbers[len(exon_numbers)-1])
							temp = ''.join(temp)
				standard_hgvs, catcher = HGVS(num_list, num_list, mutype, search, length_mutation, ex_input, intron_list, pm_change, pm_pre)
				mv_results = myVariantSearch(standard_hgvs)
				CV = ClinVar(mv_results, standard_hgvs)
				aa_ref = translate(reference_cdna[244:])	
				nsfp_results, path_pred = gen_point(positions_in_genomic1, complement(pm_change), intron_only, length_mutation, NSFP)

				if mutype == "Deletion" and len(num_list) != 0:
					cDNA, mut_genomic_dna = alter_cDNA(reference_cdna, num_list, positions_in_genomic1, length_mutation, mutype, pm_change, genomic_dna, intron_only)
					aa_seq = translate(cDNA[244:])
					if frame_shift == False:
						aa_length = (length_mutation)/3
						i = 0
						filler = ''
						while i < aa_length:


## ... source file abbreviated to get to render examples ...




			if len(posskip)>0 and frame_shift:
				if part == True:
					posskip = []
			if part and ex_input:
				print part
				posskip = []
				posskip += ["This variant includes a partial exon deletion."]
			elif not frame_shift:
				posskip = []
				posskip += ["<c style='color:gray'><b>There is no frameshift predicted.</b></c>"]
			elif length_mutation < 32:
				posskip = []
				posskip += ["This variant type (missense; nonsense; small insertion, deletion, indel; or splice-affecting) has not been clinically tested in <i>DMD</i> with exon skip therapy."]
			elif len(posskip) == 0 and length_mutation >= 32:
				posskip += ["There are no theoretical exon skips predicted to apply to this mutation."]
			
			if nonsense and not frame_shift:
				readthrough_elig = "<c style='color:green'><b>Eligible</b></c>"
			else:
				pass
			
		
		else:
~~			return render(request, 'index.html',{'success':False})


		if mutype != "Deletion" and mutype != "Deletion/Insertion" and mutype != "Duplication" and not intron_only:
			temp_cdna = "<em class='gray'>",cDNA[0:min(num_list)+243],"</em><em class='red'>",cDNA[min(num_list)+243:min(num_list)+243+length_mutation],"</em><em class='gray'>",cDNA[max(num_list)+243+length_mutation:len(cDNA)],"</em>"
		if mutype == "Point mutation (insertion)":
			temp_cdna = "<em class='gray'>",cDNA[0:max(num_list)+244],"</em><em class='red'>",cDNA[max(num_list)+244:max(num_list)+244+length_mutation],"</em><em class='gray'>",cDNA[max(num_list)+244+length_mutation:len(cDNA)],"</em>"
		if mutype == "Duplication" and not intron_only:
			temp_cdna = "<em class='gray'>",cDNA[0:min(num_list)+244],"</em><em class='green'>",cDNA[min(num_list)+244:min(num_list)+244+(length_mutation)],"</em><em class='red'>",cDNA[min(num_list)+244+(length_mutation):min(num_list)+244+(length_mutation*2)],"</em><em class='gray'>",cDNA[min(num_list)+244+(length_mutation*2):len(cDNA)],"</em>"
		if mutype == "Insertion" and not intron_only:
			temp_cdna = "<em class='gray'>",cDNA[0:min(num_list)+243],"</em><em class='red'>",cDNA[min(num_list)+244:min(num_list)+244+length_mutation],"</em><em class='gray'>",cDNA[max(num_list)+244+length_mutation:len(cDNA)],"</em>"
		if mutype == "Deletion" and not intron_only:
			fill = ''
			i = 0
			while i<length_mutation:
				fill += 'x'
				i+=1
			temp_cdna = "<em class='gray'>",cDNA[0:min(num_list)+244],"</em><em class='red'>",fill,"</em><em class='gray'>",cDNA[min(num_list)+244:len(cDNA)],"</em>"
		if intron_only:
			temp_refcdna = "<em class='color:gray'>",reference_cdna,"</em>"
			temp_cdna = temp_refcdna
			refcdna_for_print = ''.join(temp_refcdna)
		if mutype == "Deletion/Insertion" and not intron_only:
			i = 0
			fill = ''


## ... source file abbreviated to get to render examples ...


			standard_hgvs_search = ''.join(standard_hgvs_search)
			leiden_link ="https://databases.lovd.nl/shared/variants/DMD/unique?search_var_status=%3D%22Marked%22%7C%3D%22Public%22#object_id=VariantOnTranscriptUnique%2CVariantOnGenome&id=DMD&order=VariantOnTranscript%2FDNA%2CASC&skip[chromosome]=chromosome&skip[allele_]=allele_&skip[transcriptid]=transcriptid&search_transcriptid=00000024&skip[owner_countryid]=owner_countryid&FRMatchType_CustomVL_VOTunique_VOG_DMD=1&FRMatchType_CustomVL_VOTunique_VOG_DMD=2&FRMatchType_CustomVL_VOTunique_VOG_DMD=3&FRReplaceAll_CustomVL_VOTunique_VOG_DMD=1&=Preview&=Cancel&=Submit&search_VariantOnTranscript/DNA="+standard_hgvs_search
			iframe = "<iframe src='"+ leiden_link+"'&search_Variant%2FRNA=&search_Variant%2FProtein=&search_Patient%2FPhenotype%2FDisease=' align = 'center' width = '100%' height = '800' style='background-color: white'></iframe>"
		elif length_mutation > 30 and mutype != "Deletion/Insertion":
			leiden_link = "https://databases.lovd.nl/shared/variants/DMD/unique?search_var_status=%3D%22Marked%22%7C%3D%22Public%22#object_id=VariantOnTranscriptUnique%2CVariantOnGenome&id=DMD&order=VariantOnTranscript%2FDNA%2CASC&skip[chromosome]=chromosome&skip[allele_]=allele_&skip[transcriptid]=transcriptid&search_transcriptid=00000024&skip[owner_countryid]=owner_countryid&FRMatchType_CustomVL_VOTunique_VOG_DMD=1&FRMatchType_CustomVL_VOTunique_VOG_DMD=2&FRMatchType_CustomVL_VOTunique_VOG_DMD=3&FRReplaceAll_CustomVL_VOTunique_VOG_DMD=1&=Preview&=Cancel&=Submit&search_VariantOnTranscript/DNA="+search_nums+"%20"+search
			iframe = "<iframe src='"+leiden_link+ "'align = 'center' width = '100%' height = '800' style = 'background-color: white'></iframe>"
		elif length_mutation < 30 and mutype != "Point mutation":
			leiden_link = "https://databases.lovd.nl/shared/variants/DMD/unique?search_var_status=%3D%22Marked%22%7C%3D%22Public%22#object_id=VariantOnTranscriptUnique%2CVariantOnGenome&id=DMD&order=VariantOnTranscript%2FDNA%2CASC&skip[chromosome]=chromosome&skip[allele_]=allele_&skip[transcriptid]=transcriptid&search_transcriptid=00000024&skip[owner_countryid]=owner_countryid&FRMatchType_CustomVL_VOTunique_VOG_DMD=1&FRMatchType_CustomVL_VOTunique_VOG_DMD=2&FRMatchType_CustomVL_VOTunique_VOG_DMD=3&FRReplaceAll_CustomVL_VOTunique_VOG_DMD=1&=Preview&=Cancel&=Submit&search_VariantOnTranscript/DNA="+standard_hgvs_search
			iframe = "<iframe src='"+leiden_link+ "'align = 'center' width = '100%' height = '800' style = 'background-color: white'></iframe>"
		else:
			leiden_link = "https://databases.lovd.nl/shared/variants/DMD/unique?search_var_status=%3D%22Marked%22%7C%3D%22Public"
			iframe = "<iframe src='"+leiden_link+ "'align = 'center' width = '100%' height = '800' style = 'background-color: white'></iframe>"

		if nsfp_score == '':
			nsfp_score = 'N/A'
		else:
			pass

		try:
			mv_results = mv_results[0]
			mv_results_formatted = pprint.pformat(mv_results, indent=4)
			mv_disable = False
		except:
			mv_results_formatted = "No myVariantInfo results available"
			mv_disable = True
~~	return render(request, 'main.html',
		{'user_inp':mut,
		'mutype':mutype,
		'hgvs':standard_hgvs,
		'ghgvs':ghgvs,
		'ghgvs19':ghgvs19,
		'length_mutation':length_mutation,
		'exons': exon_numbers,
		'domains':ds,
		'therapy':therapy,
		'insilico_message':insilico_message,
		'splice_message':splice_message,
		'ese_message':ese_message,
		'consequence':consequence,
		'consequence_message':consequence_statement,
		'cv':cv,
		'leiden_link':leiden_link,
		'leiden_frame':iframe,
		'cdna_for_print':cdna_for_print, #full mutated sequence
		'cdna_print_preview':cdna_print_preview, #partial mutated
		'refcdna_for_print':refcdna_for_print, #full wt cdna
		'refcdna_print_preview':refcdna_print_preview, #wt preview
		'readthrough_elig':readthrough_elig,
		'posskip':posskip, #list of skips (empty if there are none)
		'sift':sift,


## ... source file continues with no further render examples...

```

