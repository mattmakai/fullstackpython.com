title: django.utils.http urlquote Example Code
category: page
slug: django-utils-http-urlquote-examples
sortorder: 500011476
toc: False
sidebartitle: django.utils.http urlquote
meta: Python example code for the urlquote callable from the django.utils.http module of the Django project.


urlquote is a callable within the django.utils.http module of the Django project.


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



## ... source file abbreviated to get to urlquote examples ...


        selection_note_all = ungettext('%(total_count)s selected',
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
~~            'q': urlquote(q),
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
        return render(request, self.directory_listing_template, context)

    def filter_folder(self, qs, terms=()):
        def construct_search(field_name):
            if field_name.startswith('^'):
                return "%s__istartswith" % field_name[1:]
            elif field_name.startswith('='):


## ... source file continues with no further urlquote examples...

```


## Example 2 from django-sitetree
[django-sitetree](https://github.com/idlesign/django-sitetree)
([project documentation](https://django-sitetree.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-sitetree/))
is a [Django](/django.html) extension that makes it easier for
developers to add site trees, menus and breadcrumb navigation elements
to their web applications.

The django-sitetree project is provided as open source under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/idlesign/django-sitetree/blob/master/LICENSE).

[**django-sitetree / sitetree / sitetreeapp.py**](https://github.com/idlesign/django-sitetree/blob/master/sitetree/./sitetreeapp.py)

```python
# sitetreeapp.py
import warnings
from collections import defaultdict
from copy import deepcopy
from inspect import getfullargspec
from sys import exc_info
from threading import local
from typing import Callable, List, Optional, Dict, Union, Sequence, Any, Tuple

from django.conf import settings
from django.core.cache import cache
from django.db.models import signals, QuerySet
from django.template.base import (
    FilterExpression, Lexer, Parser, Token, Variable, VariableDoesNotExist, VARIABLE_TAG_START, Context)
from django.template.defaulttags import url as url_tag
from django.template.loader import get_template
from django.utils import module_loading
~~from django.utils.http import urlquote
from django.utils.translation import get_language

from .compat import TOKEN_BLOCK, TOKEN_TEXT, TOKEN_VAR
from .exceptions import SiteTreeError
from .settings import (
    ALIAS_TRUNK, ALIAS_THIS_CHILDREN, ALIAS_THIS_SIBLINGS, ALIAS_THIS_PARENT_SIBLINGS, ALIAS_THIS_ANCESTOR_CHILDREN,
    UNRESOLVED_ITEM_MARKER, RAISE_ITEMS_ERRORS_ON_DEBUG, CACHE_TIMEOUT, DYNAMIC_ONLY, ADMIN_APP_NAME, SITETREE_CLS)
from .utils import get_tree_model, get_tree_item_model, import_app_sitetree_module, generate_id_for

if False:  # pragma: nocover
    from django.contrib.auth.models import User  # noqa
    from .models import TreeItemBase, TreeBase

TypeDynamicTrees = Dict[str, Union[Dict[str, List['TreeBase']], List['TreeBase']]]

MODEL_TREE_CLASS = get_tree_model()
MODEL_TREE_ITEM_CLASS = get_tree_item_model()


_ITEMS_PROCESSOR: Optional[Callable] = None

_ITEMS_PROCESSOR_ARGS_LEN: int = 0

_I18N_TREES: List[str] = []


## ... source file abbreviated to get to urlquote examples ...


        return depth

    def get_item_by_id(self, tree_alias: str, item_id: int) -> 'TreeItemBase':
        return self.cache.get_entry('items_by_ids', tree_alias)[item_id]

    def get_tree_current_item(self, tree_alias: str) -> Optional['TreeItemBase']:
        current_item = self._current_items.get(tree_alias, _UNSET)

        if current_item is not _UNSET:

            if current_item is not None:
                current_item.is_current = True  # Could be reset by .get_sitetree()

            return current_item  # noqa

        current_item = None

        if self.current_app_is_admin():
            self._current_items[tree_alias] = current_item
            return None

        current_url = self.current_request.path
        if isinstance(current_url, str):
            current_url = current_url.encode('UTF-8')
        if current_url:
~~            current_url = urlquote(current_url)

        for url_item, url in self._items_urls.items():
            if url != current_url:
                continue

            url_item.is_current = True
            if url_item.tree.alias == tree_alias:
                current_item = url_item

        if current_item is not None:
            self._current_items[tree_alias] = current_item

        return current_item

    def url(self, sitetree_item: Union['TreeItemBase', FilterExpression], context: Context = None) -> str:
        context = context or self.current_page_context
        resolve_var = self.resolve_var

        if not isinstance(sitetree_item, MODEL_TREE_ITEM_CLASS):
            sitetree_item = resolve_var(sitetree_item, context)

        resolved_url = self._items_urls.get(sitetree_item)
        if resolved_url is not None:
            return resolved_url


## ... source file continues with no further urlquote examples...

```


## Example 3 from django-wiki
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

[**django-wiki / src/wiki / decorators.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/./decorators.py)

```python
# decorators.py
from functools import wraps

from django.http import HttpResponseForbidden
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse
~~from django.utils.http import urlquote
from wiki.conf import settings
from wiki.core.exceptions import NoRootURL


def response_forbidden(request, article, urlpath, read_denied=False):
    if request.user.is_anonymous:
        qs = request.META.get("QUERY_STRING", "")
        if qs:
~~            qs = urlquote("?" + qs)
        else:
            qs = ""
        return redirect(settings.LOGIN_URL + "?next=" + request.path + qs)
    else:
        return HttpResponseForbidden(
            render_to_string(
                "wiki/permission_denied.html",
                context={
                    "article": article,
                    "urlpath": urlpath,
                    "read_denied": read_denied,
                },
                request=request,
            )
        )


def get_article(  # noqa: max-complexity=23
    func=None,
    can_read=True,
    can_write=False,
    deleted_contents=False,
    not_locked=False,
    can_delete=False,


## ... source file continues with no further urlquote examples...

```


## Example 4 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / utils / sendfile.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/utils/sendfile.py)

```python
# sendfile.py
import os.path
from mimetypes import guess_type

VERSION = (0, 3, 6)
__version__ = '.'.join(map(str, VERSION))


def _lazy_load(fn):
    _cached = []

    def _decorated():
        if not _cached:
            _cached.append(fn())
        return _cached[0]

    def clear():
        while _cached:
            _cached.pop()
    _decorated.clear = clear
    return _decorated


@_lazy_load
def _get_sendfile():
    from importlib import import_module
    from django.conf import settings
    from django.core.exceptions import ImproperlyConfigured

    backend = getattr(settings, 'SENDFILE_BACKEND', None)
    if not backend:
        raise ImproperlyConfigured('You must specify a value for SENDFILE_BACKEND')
    module = import_module(backend)
    return module.sendfile




## ... source file abbreviated to get to urlquote examples ...


    _sendfile = backend or _get_sendfile()

    if not os.path.exists(filename):
        from django.http import Http404
        raise Http404('"%s" does not exist' % filename)

    guessed_mimetype, guessed_encoding = guess_type(filename)
    if mimetype is None:
        if guessed_mimetype:
            mimetype = guessed_mimetype
        else:
            mimetype = 'application/octet-stream'

    response = _sendfile(request, filename, mimetype=mimetype)
    if attachment:
        if attachment_filename is None:
            attachment_filename = os.path.basename(filename)
        parts = ['attachment']
        if attachment_filename:
            from unidecode import unidecode
            from django.utils.encoding import force_str
            attachment_filename = force_str(attachment_filename)
            ascii_filename = unidecode(attachment_filename)
            parts.append('filename="%s"' % ascii_filename)
            if ascii_filename != attachment_filename:
~~                from django.utils.http import urlquote
~~                quoted_filename = urlquote(attachment_filename)
                parts.append('filename*=UTF-8\'\'%s' % quoted_filename)
        response['Content-Disposition'] = '; '.join(parts)

    response['Content-length'] = os.path.getsize(filename)
    response['Content-Type'] = mimetype
    response['Content-Encoding'] = encoding or guessed_encoding

    return response



## ... source file continues with no further urlquote examples...

```

