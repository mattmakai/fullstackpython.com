title: django.utils.http urlunquote Example Code
category: page
slug: django-utils-http-urlunquote-examples
sortorder: 500011477
toc: False
sidebartitle: django.utils.http urlunquote
meta: Python example code for the urlunquote callable from the django.utils.http module of the Django project.


urlunquote is a callable within the django.utils.http module of the Django project.


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
~~from django.utils.http import urlquote, urlunquote
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
)



## ... source file abbreviated to get to urlunquote examples ...


                self.get_queryset(request).get(id=last_folder_id)
            except self.model.DoesNotExist:
                url = reverse('admin:filer-directory_listing-root')
                url = "%s%s" % (url, admin_url_params_encoded(request))
            else:
                url = reverse('admin:filer-directory_listing', kwargs={'folder_id': last_folder_id})
                url = "%s%s" % (url, admin_url_params_encoded(request))
            return HttpResponseRedirect(url)
        elif folder_id is None:
            folder = FolderRoot()
        else:
            folder = get_object_or_404(self.get_queryset(request), id=folder_id)
        request.session['filer_last_folder_id'] = folder_id

        actions = self.get_actions(request)

        list_display = list(self.list_display)
        if not actions:
            try:
                list_display.remove('action_checkbox')
            except ValueError:
                pass

        q = request.GET.get('q', None)
        if q:
~~            search_terms = urlunquote(q).split(" ")
            search_mode = True
        else:
            search_terms = []
            q = ''
            search_mode = False
        limit_search_to_folder = request.GET.get('limit_search_to_folder',
                                                 False) in (True, 'on')

        if len(search_terms) > 0:
            if folder and limit_search_to_folder and not folder.is_root:
                folder_qs = folder.get_descendants(include_self=False)
                file_qs = File.objects.filter(
                    folder__in=folder.get_descendants(include_self=True))
            else:
                folder_qs = self.get_queryset(request)
                file_qs = File.objects.all()
            folder_qs = self.filter_folder(folder_qs, search_terms)
            file_qs = self.filter_file(file_qs, search_terms)

            show_result_count = True
        else:
            folder_qs = folder.children.all()
            file_qs = folder.files.all()
            show_result_count = False


## ... source file continues with no further urlunquote examples...

```

