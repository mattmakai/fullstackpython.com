title: django.contrib.admin helpers Example Code
category: page
slug: django-contrib-admin-helpers-examples
sortorder: 500011017
toc: False
sidebartitle: django.contrib.admin helpers
meta: Python example code for the helpers callable from the django.contrib.admin module of the Django project.


[helpers](https://github.com/django/django/blob/master/django/contrib/admin/helpers.py)
is a module within the [Django](/django.html) project code base. It
contains classes related to extending the functionality of the
[Django Admin](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/actions/),
such as [ActionForm](/django-contrib-admin-helpers-actionform-examples.html)
and [AdminForm](/django-contrib-admin-helpers-adminform-examples.html).


## Example 1 from django-filer
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
~~from django.contrib.admin import helpers
from django.contrib.admin.utils import capfirst, quote, unquote
from django.core.exceptions import PermissionDenied, ValidationError
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models, router
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


## ... source file abbreviated to get to helpers examples ...


                if "move-to-clipboard-%d" % (f.id,) in request.POST:
                    clipboard = tools.get_user_clipboard(request.user)
                    if f.has_edit_permission(request):
                        tools.move_file_to_clipboard([f], clipboard)
                        return HttpResponseRedirect(request.get_full_path())
                    else:
                        raise PermissionDenied

        selected = request.POST.getlist(helpers.ACTION_CHECKBOX_NAME)
        if (
            actions and request.method == 'POST'
            and 'index' in request.POST
            and '_save' not in request.POST
        ):
            if selected:
                response = self.response_action(request, files_queryset=file_qs, folders_queryset=folder_qs)
                if response:
                    return response
            else:
                msg = _("Items must be selected in order to perform "
                        "actions on them. No items have been changed.")
                self.message_user(request, msg)

        if (
            actions and request.method == 'POST'
~~            and helpers.ACTION_CHECKBOX_NAME in request.POST
            and 'index' not in request.POST
            and '_save' not in request.POST
        ):
            if selected:
                response = self.response_action(request, files_queryset=file_qs, folders_queryset=folder_qs)
                if response:
                    return response

        if actions:
            action_form = self.action_form(auto_id=None)
            action_form.fields['action'].choices = self.get_action_choices(request)
        else:
            action_form = None

        selection_note_all = ungettext('%(total_count)s selected',
            'All %(total_count)s selected', paginator.count)

        try:
            paginated_items = paginator.page(request.GET.get('page', 1))
        except PageNotAnInteger:
            paginated_items = paginator.page(1)
        except EmptyPage:
            paginated_items = paginator.page(paginator.num_pages)



## ... source file abbreviated to get to helpers examples ...


                    self.log_deletion(request, f, force_text(f))
                    f.delete()
                self.message_user(request, _("Successfully deleted %(count)d files and/or folders.") % {"count": n, })
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
~~            "action_checkbox_name": helpers.ACTION_CHECKBOX_NAME,
        })

        return render(
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


## ... source file abbreviated to get to helpers examples ...


            conflicting_names = [folder.name for folder in self.get_queryset(request).filter(parent=destination, name__in=folders_queryset.values('name'))]
            if conflicting_names:
                messages.error(request, _("Folders with names %s already exist at the selected "
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
~~            "action_checkbox_name": helpers.ACTION_CHECKBOX_NAME,
        })

        return render(request, "admin/filer/folder/choose_move_destination.html", context)

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


## ... source file abbreviated to get to helpers examples ...


                raise PermissionDenied
            form = RenameFilesForm(request.POST)
            if form.is_valid():
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
~~            "action_checkbox_name": helpers.ACTION_CHECKBOX_NAME,
        })

        return render(request, "admin/filer/folder/choose_rename_format.html", context)

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


## ... source file abbreviated to get to helpers examples ...


            form = CopyFilesAndFoldersForm()

        try:
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
~~            "action_checkbox_name": helpers.ACTION_CHECKBOX_NAME,
        })

        return render(request, "admin/filer/folder/choose_copy_destination.html", context)

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


## ... source file abbreviated to get to helpers examples ...


                    form.cleaned_data['width'] = form.cleaned_data['thumbnail_option'].width
                    form.cleaned_data['height'] = form.cleaned_data['thumbnail_option'].height
                    form.cleaned_data['crop'] = form.cleaned_data['thumbnail_option'].crop
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
~~            "action_checkbox_name": helpers.ACTION_CHECKBOX_NAME,
        })

        return render(request, "admin/filer/folder/choose_images_resize_options.html", context)

    resize_images.short_description = ugettext_lazy("Resize selected images")



## ... source file continues with no further helpers examples...

```

