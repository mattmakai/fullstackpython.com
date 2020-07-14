title: django.utils.encoding force_text Example Code
category: page
slug: django-utils-encoding-force-text-examples
sortorder: 500011444
toc: False
sidebartitle: django.utils.encoding force_text
meta: Python example code for the force_text callable from the django.utils.encoding module of the Django project.


force_text is a callable within the django.utils.encoding module of the Django project.


## Example 1 from django-angular
[django-angular](https://github.com/jrief/django-angular)
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / forms / angular_base.py**](https://github.com/jrief/django-angular/blob/master/djng/forms/angular_base.py)

```python
# angular_base.py
from base64 import b64encode
from collections import UserList
import json
import warnings

from django.forms import forms
from django.http import QueryDict
from django.utils.html import format_html, format_html_join, escape, conditional_escape
~~from django.utils.encoding import force_text
from django.utils.module_loading import import_string
from django.utils.safestring import mark_safe, SafeText, SafeData
from django.core.exceptions import ValidationError, ImproperlyConfigured

from .fields import DefaultFieldMixin


class SafeTuple(SafeData, tuple):


class TupleErrorList(UserList, list):
    def __init__(self, initlist=None, error_class=None):
        super(TupleErrorList, self).__init__(initlist)

        if error_class is None:
            self.error_class = 'errorlist'
        else:
            self.error_class = 'errorlist {}'.format(error_class)

    def as_data(self):
        return ValidationError(self.data).error_list

    def get_json_data(self, escape_html=False):
        errors = []


## ... source file abbreviated to get to force_text examples ...


                'message': escape(message) if escape_html else message,
                'code': error.code or '',
            })
        return errors

    def as_json(self, escape_html=False):
        return json.dumps(self.get_json_data(escape_html))

    def extend(self, iterable):
        for item in iterable:
            if not isinstance(item, str):
                self.append(item)
        return None

    def as_ul(self):
        if not self:
            return SafeText()
        first = self[0]
        if isinstance(first, tuple):
            error_lists = {'$pristine': [], '$dirty': []}
            for e in self:
                if e[5] == '$message':
                    li_format = '<li ng-show="{0}.{1} && {0}.{3}" class="{2}" ng-bind="{0}.{3}"></li>'
                else:
                    li_format = '<li ng-show="{0}.{1}" class="{2}">{3}</li>'
~~                err_tuple = (e[0], e[3], e[4], force_text(e[5]))
                error_lists[e[2]].append(format_html(li_format, *err_tuple))
            dirty_errors, pristine_errors = '', ''
            if len(error_lists['$dirty']) > 0:
                dirty_errors = format_html(
                    '<ul ng-show="{0}.$dirty && !{0}.$untouched" class="{1}" ng-cloak>{2}</ul>',  # duck typing: !...$untouched
                    first[0], first[1], mark_safe(''.join(error_lists['$dirty']))
                )
            if len(error_lists['$pristine']) > 0:
                pristine_errors = format_html(
                    '<ul ng-show="{0}.$pristine" class="{1}" ng-cloak>{2}</ul>',
                    first[0], first[1], mark_safe(''.join(error_lists['$pristine']))
                )
            return format_html('{}{}', dirty_errors, pristine_errors)
        return format_html('<ul class="errorlist">{0}</ul>',
            format_html_join('', '<li>{0}</li>', ((force_text(e),) for e in self)))

    def as_text(self):
        if not self:
            return ''
        if isinstance(self[0], tuple):
~~            return '\n'.join(['* %s' % force_text(e[5]) for e in self if bool(e[5])])
~~        return '\n'.join(['* %s' % force_text(e) for e in self])

    def __str__(self):
        return self.as_ul()

    def __repr__(self):
        if self and isinstance(self[0], tuple):
            return repr([force_text(e[5]) for e in self])
        return repr([force_text(e) for e in self])

    def __contains__(self, item):
        return item in list(self)

    def __eq__(self, other):
        return list(self) == other

    def __ne__(self, other):
        return list(self) != other

    def __getitem__(self, i):
        error = self.data[i]
        if isinstance(error, tuple):
            if isinstance(error[5], ValidationError):
                error[5] = list(error[5])[0]
            return error
        if isinstance(error, ValidationError):
            return list(error)[0]
~~        return force_text(error)


class NgWidgetMixin(object):
    def get_context(self, name, value, attrs):
        context = super(NgWidgetMixin, self).get_context(name, value, attrs)
        if callable(getattr(self._field, 'update_widget_rendering_context', None)):
            self._field.update_widget_rendering_context(context)
        return context


class NgBoundField(forms.BoundField):
    @property
    def errors(self):
        if not hasattr(self, '_errors_cache'):
            self._errors_cache = self.form.get_field_errors(self)
        return self._errors_cache

    def css_classes(self, extra_classes=None):
        if hasattr(extra_classes, 'split'):
            extra_classes = extra_classes.split()
        extra_classes = set(extra_classes or [])
        field_css_classes = getattr(self.form, 'field_css_classes', None)
        if hasattr(field_css_classes, 'split'):
            extra_classes.update(field_css_classes.split())


## ... source file continues with no further force_text examples...

```


## Example 2 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / plugin_base.py**](https://github.com/divio/django-cms/blob/develop/cms/./plugin_base.py)

```python
# plugin_base.py
import json
import re

from django.shortcuts import render as render_to_response

from django import forms
from django.contrib import admin
from django.contrib import messages
from django.core.exceptions import (
    ImproperlyConfigured,
    ObjectDoesNotExist,
    ValidationError,
)
~~from django.utils.encoding import force_text, smart_str
from django.utils.html import escapejs
from django.utils.translation import ugettext, ugettext_lazy as _

from six import with_metaclass, python_2_unicode_compatible

from cms import operations
from cms.exceptions import SubClassNeededError
from cms.models import CMSPlugin
from cms.toolbar.utils import get_plugin_tree_as_json, get_plugin_toolbar_info
from cms.utils.conf import get_cms_setting


class CMSPluginBaseMetaclass(forms.MediaDefiningClass):
    def __new__(cls, name, bases, attrs):
        super_new = super(CMSPluginBaseMetaclass, cls).__new__
        parents = [base for base in bases if isinstance(base, CMSPluginBaseMetaclass)]
        if not parents:
            return super_new(cls, name, bases, attrs)
        new_plugin = super_new(cls, name, bases, attrs)
        if not issubclass(new_plugin.model, CMSPlugin):
            raise SubClassNeededError(
                "The 'model' attribute on CMSPluginBase subclasses must be "
                "either CMSPlugin or a subclass of CMSPlugin. %r on %r is not."
                % (new_plugin.model, new_plugin)


## ... source file abbreviated to get to force_text examples ...


            else:
                parent_id = obj.parent.pk if obj.parent else None
                tree_order = obj.placeholder.get_plugin_tree_order(parent_id)
                operation_kwargs['plugin'] = obj
                operation_kwargs['operation'] = operations.ADD_PLUGIN
                operation_kwargs['tree_order'] = tree_order
            self._operation_token = pl_admin._send_pre_placeholder_operation(**operation_kwargs)

        self.saved_object = obj
        return super(CMSPluginBase, self).save_model(request, obj, form, change)

    def save_form(self, request, form, change):
        obj = super(CMSPluginBase, self).save_form(request, form, change)

        for field, value in self._cms_initial_attributes.items():
            setattr(obj, field, value)
        return obj

    def response_add(self, request, obj, **kwargs):
        self.object_successfully_changed = True
        return self.render_close_frame(request, obj)

    def response_change(self, request, obj):
        self.object_successfully_changed = True
        opts = self.model._meta
~~        msg_dict = {'name': force_text(opts.verbose_name), 'obj': force_text(obj)}
        msg = _('The %(name)s "%(obj)s" was changed successfully.') % msg_dict
        self.message_user(request, msg, messages.SUCCESS)
        return self.render_close_frame(request, obj)

    def log_addition(self, request, obj, bypass=None):
        pass

    def log_change(self, request, obj, message, bypass=None):
        pass

    def log_deletion(self, request, obj, object_repr, bypass=None):
        pass

    def icon_src(self, instance):
        return ""

    def icon_alt(self, instance):
~~        return "%s - %s" % (force_text(self.name), force_text(instance))

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(CMSPluginBase, self).get_fieldsets(request, obj)

        for name, data in fieldsets:
            if data.get('fields'):  # if fieldset with non-empty fields is found, return fieldsets
                return fieldsets

        if self.inlines:
            return []  # if plugin has inlines but no own fields return empty fieldsets to remove empty white fieldset

        try:  # if all fieldsets are empty (assuming there is only one fieldset then) add description
            fieldsets[0][1]['description'] = self.get_empty_change_form_text(obj=obj)
        except KeyError:
            pass
        return fieldsets

    @classmethod
    def get_empty_change_form_text(cls, obj=None):
        return ugettext('There are no further settings for this plugin. Please press save.')

    @classmethod
    def get_child_class_overrides(cls, slot, page):
        from cms.utils.placeholder import get_placeholder_conf


## ... source file continues with no further force_text examples...

```


## Example 3 from django-downloadview
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

[**django-downloadview / django_downloadview / io.py**](https://github.com/benoitbryon/django-downloadview/blob/master/django_downloadview/./io.py)

```python
# io.py
import io

~~from django.utils.encoding import force_bytes, force_text


class TextIteratorIO(io.TextIOBase):

    def __init__(self, iterator):
        self._iter = iterator

        self._left = ""

    def readable(self):
        return True

    def _read1(self, n=None):
        while not self._left:
            try:
                self._left = next(self._iter)
            except StopIteration:
                break
            else:
~~                self._left = force_text(self._left)
        ret = self._left[:n]
        self._left = self._left[len(ret) :]
        return ret

    def read(self, n=None):
        chunks = []
        if n is None or n < 0:
            while True:
                m = self._read1()
                if not m:
                    break
                chunks.append(m)
        else:
            while n > 0:
                m = self._read1(n)
                if not m:
                    break
                n -= len(m)
                chunks.append(m)
        return "".join(chunks)

    def readline(self):
        chunks = []
        while True:


## ... source file continues with no further force_text examples...

```


## Example 4 from django-filer
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
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
~~from django.utils.encoding import force_text
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
    check_files_read_permissions, check_folder_edit_permissions,
    check_folder_read_permissions, popup_status, userperms_for_request,


## ... source file abbreviated to get to force_text examples ...


        app_label = opts.app_label

        if not self.has_delete_permission(request):
            raise PermissionDenied

        current_folder = self._get_current_action_folder(
            request, files_queryset, folders_queryset)

        all_protected = []

        using = router.db_for_write(self.model)
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
~~                    self.log_deletion(request, f, force_text(f))
                    f.delete()
                folder_ids = set()
                for folder in folders_queryset:
                    folder_ids.add(folder.id)
                    folder_ids.update(
                        folder.get_descendants().values_list('id', flat=True))
                for f in File.objects.filter(folder__in=folder_ids):
~~                    self.log_deletion(request, f, force_text(f))
                    f.delete()
                for f in folders_queryset:
~~                    self.log_deletion(request, f, force_text(f))
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


## ... source file abbreviated to get to force_text examples ...


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
        else:
~~            return '%s: %s' % (capfirst(opts.verbose_name), force_text(obj))

    def _check_copy_perms(self, request, files_queryset, folders_queryset):
        try:
            check_files_read_permissions(request, files_queryset)
            check_folder_read_permissions(request, folders_queryset)
        except PermissionDenied:
            return True
        return False

    def _check_move_perms(self, request, files_queryset, folders_queryset):
        try:
            check_files_read_permissions(request, files_queryset)
            check_folder_read_permissions(request, folders_queryset)
            check_files_edit_permissions(request, files_queryset)
            check_folder_edit_permissions(request, folders_queryset)
        except PermissionDenied:
            return True
        return False

    def _get_current_action_folder(self, request, files_queryset,
                                   folders_queryset):
        if files_queryset:
            return files_queryset[0].folder
        elif folders_queryset:


## ... source file abbreviated to get to force_text examples ...


        else:
            return None

    def _list_folders_to_copy_or_move(self, request, folders):
        for fo in folders:
            yield self._format_callback(fo, request.user, self.admin_site, set())
            children = list(self._list_folders_to_copy_or_move(request, fo.children.all()))
            children.extend([self._format_callback(f, request.user, self.admin_site, set()) for f in sorted(fo.files)])
            if children:
                yield children

    def _list_all_to_copy_or_move(self, request, files_queryset, folders_queryset):
        to_copy_or_move = list(self._list_folders_to_copy_or_move(request, folders_queryset))
        to_copy_or_move.extend([self._format_callback(f, request.user, self.admin_site, set()) for f in sorted(files_queryset)])
        return to_copy_or_move

    def _list_all_destination_folders_recursive(self, request, folders_queryset, current_folder, folders, allow_self, level):
        for fo in folders:
            if not allow_self and fo in folders_queryset:
                continue

            if not fo.has_read_permission(request):
                continue

            enabled = (allow_self or fo != current_folder) and fo.has_add_children_permission(request)
~~            yield (fo, (mark_safe(("&nbsp;&nbsp;" * level) + force_text(fo)), enabled))
            for c in self._list_all_destination_folders_recursive(request, folders_queryset, current_folder, fo.children.all(), allow_self, level + 1):
                yield c

    def _list_all_destination_folders(self, request, folders_queryset, current_folder, allow_self):
        root_folders = self.get_queryset(request).filter(parent__isnull=True).order_by('name')
        return list(self._list_all_destination_folders_recursive(request, folders_queryset, current_folder, root_folders, allow_self, 0))

    def _move_files_and_folders_impl(self, files_queryset, folders_queryset, destination):
        for f in files_queryset:
            f.folder = destination
            f.save()
        for f in folders_queryset:
            f.move_to(destination, 'last-child')
            f.save()

    def move_files_and_folders(self, request, files_queryset, folders_queryset):
        opts = self.model._meta
        app_label = opts.app_label

        current_folder = self._get_current_action_folder(request, files_queryset, folders_queryset)
        perms_needed = self._check_move_perms(request, files_queryset, folders_queryset)
        to_move = self._list_all_to_copy_or_move(request, files_queryset, folders_queryset)
        folders = self._list_all_destination_folders(request, folders_queryset, current_folder, False)



## ... source file continues with no further force_text examples...

```


## Example 5 from django-jet
[django-jet](https://github.com/geex-arts/django-jet)
([project documentation](https://jet.readthedocs.io/en/latest/),
[PyPI project page](https://pypi.org/project/django-jet/) and
[more information](http://jet.geex-arts.com/))
is a fancy [Django](/django.html) Admin panel replacement.

The django-jet project is open source under the
[GNU Affero General Public License v3.0](https://github.com/geex-arts/django-jet/blob/dev/LICENSE).

[**django-jet / jet / utils.py**](https://github.com/geex-arts/django-jet/blob/dev/jet/./utils.py)

```python
# utils.py
import datetime
import json
from django.template import Context
from django.utils import translation
from jet import settings
from jet.models import PinnedApplication

try:
    from django.apps.registry import apps
except ImportError:
    try:
        from django.apps import apps # Fix Django 1.7 import issue
    except ImportError:
        pass
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
try:
    from django.core.urlresolvers import reverse, resolve, NoReverseMatch
except ImportError: # Django 1.11
    from django.urls import reverse, resolve, NoReverseMatch

from django.contrib.admin import AdminSite
from django.utils.encoding import smart_text
from django.utils.text import capfirst
from django.contrib import messages
~~from django.utils.encoding import force_text
from django.utils.functional import Promise
from django.contrib.admin.options import IncorrectLookupParameters
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict  # Python 2.6


class JsonResponse(HttpResponse):

    def __init__(self, data, encoder=DjangoJSONEncoder, safe=True, **kwargs):
        if safe and not isinstance(data, dict):
            raise TypeError('In order to allow non-dict objects to be '
                'serialized set the safe parameter to False')
        kwargs.setdefault('content_type', 'application/json')
        data = json.dumps(data, cls=encoder)
        super(JsonResponse, self).__init__(content=data, **kwargs)


def get_app_list(context, order=True):


## ... source file abbreviated to get to force_text examples ...


    try:
        current_resolver = resolve(context.get('request').path)
        index_resolver = resolve(reverse('%s:index' % current_resolver.namespaces[0]))

        if hasattr(index_resolver.func, 'admin_site'):
            return index_resolver.func.admin_site

        for func_closure in index_resolver.func.__closure__:
            if isinstance(func_closure.cell_contents, AdminSite):
                return func_closure.cell_contents
    except:
        pass

    return admin.site


def get_admin_site_name(context):
    return get_admin_site(context).name


class LazyDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, Promise):
~~            return force_text(obj)
        return self.encode(obj)


def get_model_instance_label(instance):
    if getattr(instance, "related_label", None):
        return instance.related_label()
    return smart_text(instance)


class SuccessMessageMixin(object):
    success_message = ''

    def form_valid(self, form):
        response = super(SuccessMessageMixin, self).form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data


def get_model_queryset(admin_site, model, request, preserved_filters=None):


## ... source file continues with no further force_text examples...

```


## Example 6 from django-pipeline
[django-pipeline](https://github.com/jazzband/django-pipeline)
([project documentation](https://django-pipeline.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-pipeline/))
is a code library for handling and compressing
[static content assets](/static-content.html) when handling requests in
[Django](/django.html) web applications.

The django-pipeline project is open sourced under the
[MIT License](https://github.com/jazzband/django-pipeline/blob/master/LICENSE)
and it is maintained by the developer community group
[Jazzband](https://jazzband.co/).

[**django-pipeline / pipeline / compressors / __init__.py**](https://github.com/jazzband/django-pipeline/blob/master/pipeline/compressors/__init__.py)

```python
# __init__.py
import base64
import os
import posixpath
import re
import subprocess

from itertools import takewhile

from django.contrib.staticfiles.storage import staticfiles_storage
~~from django.utils.encoding import smart_bytes, force_text

from pipeline.conf import settings
from pipeline.exceptions import CompressorError
from pipeline.utils import to_class, relpath, set_std_streams_blocking

URL_DETECTOR = r"""url\((['"]?)\s*(.*?)\1\)"""
URL_REPLACER = r"""url\(__EMBED__(.+?)(\?\d+)?\)"""
NON_REWRITABLE_URL = re.compile(r'^(#|http:|https:|data:|//)')

DEFAULT_TEMPLATE_FUNC = "template"
TEMPLATE_FUNC = r"""var template = function(str){var fn = new Function('obj', 'var __p=[],print=function(){__p.push.apply(__p,arguments);};with(obj||{}){__p.push(\''+str.replace(/\\/g, '\\\\').replace(/'/g, "\\'").replace(/<%=([\s\S]+?)%>/g,function(match,code){return "',"+code.replace(/\\'/g, "'")+",'";}).replace(/<%([\s\S]+?)%>/g,function(match,code){return "');"+code.replace(/\\'/g, "'").replace(/[\r\n\t]/g,' ')+"__p.push('";}).replace(/\r/g,'\\r').replace(/\n/g,'\\n').replace(/\t/g,'\\t')+"');}return __p.join('');");return fn;};"""

MIME_TYPES = {
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.gif': 'image/gif',
    '.tif': 'image/tiff',
    '.tiff': 'image/tiff',
    '.ttf': 'font/truetype',
    '.otf': 'font/opentype',
    '.woff': 'font/woff'
}
EMBED_EXTS = MIME_TYPES.keys()


## ... source file abbreviated to get to force_text examples ...


    def embeddable(self, path, variant):
        name, ext = os.path.splitext(path)
        font = ext in FONT_EXTS
        if not variant:
            return False
        if not (re.search(settings.EMBED_PATH, path.replace('\\', '/')) and self.storage.exists(path)):
            return False
        if ext not in EMBED_EXTS:
            return False
        if not (font or len(self.encoded_content(path)) < settings.EMBED_MAX_IMAGE_SIZE):
            return False
        return True

    def with_data_uri(self, css):
        def datauri(match):
            path = match.group(1)
            mime_type = self.mime_type(path)
            data = self.encoded_content(path)
            return f"url(\"data:{mime_type};charset=utf-8;base64,{data}\")"
        return re.sub(URL_REPLACER, datauri, css)

    def encoded_content(self, path):
        if path in self.__class__.asset_contents:
            return self.__class__.asset_contents[path]
        data = self.read_bytes(path)
~~        self.__class__.asset_contents[path] = force_text(base64.b64encode(data))
        return self.__class__.asset_contents[path]

    def mime_type(self, path):
        name, ext = os.path.splitext(path)
        return MIME_TYPES[ext]

    def absolute_path(self, path, start):
        if posixpath.isabs(path):
            path = posixpath.join(staticfiles_storage.location, path)
        else:
            path = posixpath.join(start, path)
        return posixpath.normpath(path)

    def relative_path(self, absolute_path, output_filename):
        absolute_path = posixpath.join(settings.PIPELINE_ROOT, absolute_path)
        output_path = posixpath.join(settings.PIPELINE_ROOT, posixpath.dirname(output_filename))
        return relpath(absolute_path, output_path)

    def read_bytes(self, path):
        file = staticfiles_storage.open(path)
        content = file.read()
        file.close()
        return content

    def read_text(self, path):
        content = self.read_bytes(path)
~~        return force_text(content)


class CompressorBase(object):
    def __init__(self, verbose):
        self.verbose = verbose

    def filter_css(self, css):
        raise NotImplementedError

    def filter_js(self, js):
        raise NotImplementedError


class SubProcessCompressor(CompressorBase):
    def execute_command(self, command, content):
        argument_list = []
        for flattening_arg in command:
            if isinstance(flattening_arg, (str,)):
                argument_list.append(flattening_arg)
            else:
                argument_list.extend(flattening_arg)

        pipe = subprocess.Popen(argument_list, stdout=subprocess.PIPE,
                                stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        if content:
            content = smart_bytes(content)
        stdout, stderr = pipe.communicate(content)
        set_std_streams_blocking()
        if stderr.strip() and pipe.returncode != 0:
            raise CompressorError(stderr)
        elif self.verbose:
            print(stderr)
~~        return force_text(stdout)


class NoopCompressor(CompressorBase):
    def compress_js(self, js):
        return js

    def compress_css(self, css):
        return css



## ... source file continues with no further force_text examples...

```

