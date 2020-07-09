title: django.utils.translation ungettext Example Code
category: page
slug: django-utils-translation-ungettext-examples
sortorder: 500011511
toc: False
sidebartitle: django.utils.translation ungettext
meta: Python example code for the ungettext callable from the django.utils.translation module of the Django project.


ungettext is a callable within the django.utils.translation module of the Django project.


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
from django.contrib.admin import helpers
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
~~from django.utils.translation import ugettext_lazy, ungettext

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
)


Image = load_model(FILER_IMAGE_MODEL)



## ... source file abbreviated to get to ungettext examples ...


                response = self.response_action(request, files_queryset=file_qs, folders_queryset=folder_qs)
                if response:
                    return response
            else:
                msg = _("Items must be selected in order to perform "
                        "actions on them. No items have been changed.")
                self.message_user(request, msg)

        if (
            actions and request.method == 'POST'
            and helpers.ACTION_CHECKBOX_NAME in request.POST
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

~~        selection_note_all = ungettext('%(total_count)s selected',
            'All %(total_count)s selected', paginator.count)

        try:
            paginated_items = paginator.page(request.GET.get('page', 1))
        except PageNotAnInteger:
            paginated_items = paginator.page(1)
        except EmptyPage:
            paginated_items = paginator.page(paginator.num_pages)

        context = self.admin_site.each_context(request)
        context.update({
            'folder': folder,
            'clipboard_files': File.objects.filter(
                in_clipboards__clipboarditem__clipboard__user=request.user
            ).distinct(),
            'paginator': paginator,
            'paginated_items': paginated_items,
            'virtual_items': virtual_items,
            'uploader_connections': settings.FILER_UPLOADER_CONNECTIONS,
            'permissions': permissions,
            'permstest': userperms_for_request(folder, request),
            'current_url': request.path,
            'title': _('Directory listing for %(folder_name)s') % {'folder_name': folder.name},
            'search_string': ' '.join(search_terms),


## ... source file continues with no further ungettext examples...

```


## Example 2 from django-haystack
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
from django.shortcuts import render
from django.utils.encoding import force_str
~~from django.utils.translation import ungettext

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

        paginator = Paginator(sqs, self.list_per_page)


## ... source file abbreviated to get to ungettext examples ...


            "model": self.model,
            "list_display": list_display,
            "list_display_links": self.list_display_links,
            "list_filter": self.list_filter,
            "date_hierarchy": self.date_hierarchy,
            "search_fields": self.search_fields,
            "list_select_related": self.list_select_related,
            "list_per_page": self.list_per_page,
            "list_editable": self.list_editable,
            "list_max_show_all": self.list_max_show_all,
            "model_admin": self,
        }
        if hasattr(self, 'get_sortable_by'):  # Django 2.1+
            kwargs["sortable_by"] = self.get_sortable_by(request)
        changelist = SearchChangeList(**kwargs)
        changelist.formset = None
        media = self.media

        actions = self.get_actions(request)
        if actions:
            action_form = self.action_form(auto_id=None)
            action_form.fields["action"].choices = self.get_action_choices(request)
        else:
            action_form = None

~~        selection_note = ungettext(
            "0 of %(count)d selected",
            "of %(count)d selected",
            len(changelist.result_list),
        )
~~        selection_note_all = ungettext(
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


## ... source file continues with no further ungettext examples...

```

