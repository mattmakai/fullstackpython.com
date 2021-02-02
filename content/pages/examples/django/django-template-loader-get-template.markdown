title: django.template.loader get_template Example Code
category: page
slug: django-template-loader-get-template-examples
sortorder: 500011392
toc: False
sidebartitle: django.template.loader get_template
meta: Python example code that shows how to use the get_template callable from the django.template.loader module of the Django project.


`get_template` is a callable within the `django.template.loader` module of the Django project.

<a href="/django-template-loader-render-to-string-examples.html">render_to_string</a>
and
<a href="/django-template-loader-select-template-examples.html">select_template</a>
are a couple of other callables within the `django.template.loader` package that also have code examples.

## Example 1 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / chair_mail / views.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/chair_mail/views.py)

```python
# views.py
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
~~from django.template.loader import get_template
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_GET, require_POST

from conferences.utilities import validate_chair_access
from chair_mail.context import USER_VARS, CONFERENCE_VARS, SUBMISSION_VARS, \
    FRAME_VARS
from chair_mail.forms import EmailFrameUpdateForm, EmailFrameTestForm, \
    MessageForm, get_preview_form_class, EditNotificationForm, \
    UpdateNotificationStateForm
from chair_mail.mailing_lists import ALL_LISTS
from chair_mail.models import EmailSettings, EmailFrame, EmailMessage, \
    GroupMessage, MSG_TYPE_USER, MSG_TYPE_SUBMISSION, get_group_message_model, \
    get_message_leaf_model, SystemNotification, DEFAULT_NOTIFICATIONS_DATA
from chair_mail.utility import get_email_frame, get_email_frame_or_404, \
    reverse_preview_url, reverse_list_objects_url, get_object_name, \
    get_object_url
from conferences.models import Conference


def _get_grouped_vars(msg_type):
    if msg_type == MSG_TYPE_USER:
        return (
            ('Conference variables', CONFERENCE_VARS),


## ... source file abbreviated to get to get_template examples ...


            ('Submission variables', SUBMISSION_VARS),
        )
    raise ValueError(f'unrecognized message type "{msg_type}"')


@require_GET
def overview(request, conf_pk):
    conference = get_object_or_404(Conference, pk=conf_pk)
    validate_chair_access(request.user, conference)
    frame = get_email_frame(conference)
    return render(request, 'chair_mail/tab_pages/overview.html', context={
        'conference': conference,
        'frame': frame,
        'active_tab': 'overview',
    })


@require_POST
def create_frame(request, conf_pk):
    conference = get_object_or_404(Conference, pk=conf_pk)
    validate_chair_access(request.user, conference)
    if not hasattr(conference, 'email_settings'):
        EmailSettings.objects.create(conference=conference)
    email_settings = conference.email_settings
    frame = email_settings.frame
~~    template_html = get_template(
        'chair_mail/email/default_frame_html.html').template
~~    template_plain = get_template(
        'chair_mail/email/default_frame_plain.txt').template
    if frame:
        frame.text_html = template_html.source
        frame.text_plain = template_plain.source
        frame.created_at = timezone.now()
        frame.updated_at = timezone.now()
        frame.created_by = request.user
        frame.save()
        messages.success(request, 'Reset existing frame')
    else:
        frame = EmailFrame.objects.create(
            conference=conference,
            created_by=request.user,
            text_plain=template_plain.source,
            text_html=template_html.source,
        )
        email_settings.frame = frame
        email_settings.save()
        messages.success(request, 'Created new template')

    default_next = reverse('chair_mail:overview', kwargs={'conf_pk': conf_pk})
    next_url = request.GET.get('next', default_next)
    return redirect(next_url)



## ... source file continues with no further get_template examples...

```


## Example 2 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / templates.py**](https://github.com/divio/django-cms/blob/develop/cms/./templates.py)

```python
# templates.py
~~from django.template.loader import get_template
from django.utils.functional import cached_property


class TemplatesCache:

    def __init__(self):
        self._cached_templates = {}

    def get_cached_template(self, template):
        if hasattr(template, 'render'):
            return template

        if not template in self._cached_templates:
~~            self._cached_templates[template] = get_template(template)
        return self._cached_templates[template]

    @cached_property
    def drag_item_template(self):
~~        return get_template('cms/toolbar/dragitem.html')

    @cached_property
    def placeholder_plugin_menu_template(self):
~~        return get_template('cms/toolbar/dragitem_menu.html')

    @cached_property
    def dragbar_template(self):
~~        return get_template('cms/toolbar/dragbar.html')



## ... source file continues with no further get_template examples...

```


## Example 3 from django-floppyforms
[django-floppyforms](https://github.com/jazzband/django-floppyforms)
([project documentation](https://django-floppyforms.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-floppyforms/))
is a [Django](/django.html) code library for better control
over rendering HTML forms in your [templates](/template-engines.html).

The django-floppyforms code is provided as
[open source](https://github.com/jazzband/django-floppyforms/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-floppyforms / floppyforms / compat.py**](https://github.com/jazzband/django-floppyforms/blob/master/floppyforms/./compat.py)

```python
# compat.py
from contextlib import contextmanager

import django
from django.template import Context
from django.utils.datastructures import MultiValueDict

MULTIVALUE_DICT_TYPES = (MultiValueDict,)


REQUIRED_CONTEXT_ATTRIBTUES = (
    '_form_config',
    '_form_render',
)


class DictContext(dict):
    pass


if django.VERSION < (1, 8):
~~    def get_template(context, template_name):
~~        from django.template.loader import get_template
~~        return get_template(template_name)

    def get_context(context):
        if not isinstance(context, Context):
            context = Context(context)
        return context

else:
~~    def get_template(context, template_name):
        return context.template.engine.get_template(template_name)

    def get_context(context):
        return context


def flatten_context(context):
    if isinstance(context, Context):
        flat = {}
        for d in context.dicts:
            flat.update(d)
        return flat
    else:
        return context


def flatten_contexts(*contexts):
    new_context = DictContext()
    for context in contexts:
        if context is not None:
            new_context.update(flatten_context(context))
            for attr in REQUIRED_CONTEXT_ATTRIBTUES:
                if hasattr(context, attr):
                    setattr(new_context, attr, getattr(context, attr))


## ... source file continues with no further get_template examples...

```


## Example 4 from django-sitetree
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
from django.core.cache import caches
from django.db.models import signals, QuerySet
from django.template.base import (
    FilterExpression, Lexer, Parser, Variable, VariableDoesNotExist, VARIABLE_TAG_START)
from django.template.context import Context
~~from django.template.loader import get_template
from django.urls import reverse, NoReverseMatch
from django.utils import module_loading
from django.utils.encoding import iri_to_uri
from django.utils.translation import get_language

from .compat import TOKEN_TEXT, TOKEN_VAR
from .exceptions import SiteTreeError
from .settings import (
    ALIAS_TRUNK, ALIAS_THIS_CHILDREN, ALIAS_THIS_SIBLINGS, ALIAS_THIS_PARENT_SIBLINGS, ALIAS_THIS_ANCESTOR_CHILDREN,
    UNRESOLVED_ITEM_MARKER, RAISE_ITEMS_ERRORS_ON_DEBUG, CACHE_TIMEOUT, CACHE_NAME, DYNAMIC_ONLY, ADMIN_APP_NAME,
    SITETREE_CLS)
from .utils import get_tree_model, get_tree_item_model, import_app_sitetree_module, generate_id_for

if False:  # pragma: nocover
    from django.contrib.auth.models import User  # noqa
    from .models import TreeItemBase, TreeBase

TypeDynamicTrees = Dict[str, Union[Dict[str, List['TreeBase']], List['TreeBase']]]

MODEL_TREE_CLASS = get_tree_model()
MODEL_TREE_ITEM_CLASS = get_tree_item_model()


_ITEMS_PROCESSOR: Optional[Callable] = None


## ... source file abbreviated to get to get_template examples ...


            return []

        tree_items = self.filter_items(self.get_children(tree_alias, None), 'sitetree')
        tree_items = self.apply_hook(tree_items, 'sitetree')
        self.update_has_children(tree_alias, tree_items, 'sitetree')

        return tree_items

    def children(
            self,
            parent_item: 'TreeItemBase',
            navigation_type: str,
            use_template: str,
            context: Context
    ) -> str:
        parent_item = self.resolve_var(parent_item, context)
        tree_alias, tree_items = self.get_sitetree(parent_item.tree.alias)

        self.tree_climber(tree_alias, self.get_tree_current_item(tree_alias))

        tree_items = self.get_children(tree_alias, parent_item)
        tree_items = self.filter_items(tree_items, navigation_type)
        tree_items = self.apply_hook(tree_items, f'{navigation_type}.children')
        self.update_has_children(tree_alias, tree_items, navigation_type)

~~        my_template = get_template(use_template)

        context.push()
        context['sitetree_items'] = tree_items
        rendered = my_template.render(context.flatten())
        context.pop()

        return rendered

    def get_children(self, tree_alias: str, item: Optional['TreeItemBase']) -> List['TreeItemBase']:
        if not self._current_app_is_admin:
            tree_alias = self.resolve_tree_i18n_alias(tree_alias)

        return self.cache.get_entry('parents', tree_alias)[item]

    def update_has_children(self, tree_alias: str, tree_items: List['TreeItemBase'], navigation_type: str):
        get_children = self.get_children
        filter_items = self.filter_items
        apply_hook = self.apply_hook

        for tree_item in tree_items:
            children = get_children(tree_alias, tree_item)
            children = filter_items(children, navigation_type)
            children = apply_hook(children, f'{navigation_type}.has_children')
            tree_item.has_children = len(children) > 0


## ... source file continues with no further get_template examples...

```


## Example 5 from django-tables2
[django-tables2](https://github.com/jieter/django-tables2)
([projection documentation](https://django-tables2.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-tables2/))
is a code library for [Django](/django.html) that simplifies creating and
displaying tables in [Django templates](/django-templates.html),
especially with more advanced features such as pagination and sorting.
The project and its code are
[available as open source](https://github.com/jieter/django-tables2/blob/master/LICENSE).

[**django-tables2 / django_tables2 / tables.py**](https://github.com/jieter/django-tables2/blob/master/django_tables2/./tables.py)

```python
# tables.py
import copy
from collections import OrderedDict
from itertools import count

from django.conf import settings
from django.core.paginator import Paginator
from django.db import models
~~from django.template.loader import get_template
from django.utils.encoding import force_str

from . import columns
from .config import RequestConfig
from .data import TableData
from .rows import BoundRows
from .utils import Accessor, AttributeDict, OrderBy, OrderByTuple, Sequence


class DeclarativeColumnsMetaclass(type):

    def __new__(mcs, name, bases, attrs):
        attrs["_meta"] = opts = TableOptions(attrs.get("Meta", None), name)

        cols, remainder = [], {}
        for attr_name, attr in attrs.items():
            if isinstance(attr, columns.Column):
                attr._explicit = True
                cols.append((attr_name, attr))
            else:
                remainder[attr_name] = attr
        attrs = remainder

        cols.sort(key=lambda x: x[1].creation_counter)


## ... source file abbreviated to get to get_template examples ...


            order_by = self._meta.order_by
        if order_by is None:
            self._order_by = None
            order_by = self.data.ordering
            if order_by is not None:
                self.order_by = order_by
        else:
            self.order_by = order_by
        self.template_name = template_name
        if request:
            RequestConfig(request).configure(self)

        self._counter = count()

    def get_top_pinned_data(self):
        return None

    def get_bottom_pinned_data(self):
        return None

    def before_render(self, request):
        return

    def as_html(self, request):
        self._counter = count()
~~        template = get_template(self.template_name)

        context = {"table": self, "request": request}

        self.before_render(request)
        return template.render(context)

    def as_values(self, exclude_columns=None):
        if exclude_columns is None:
            exclude_columns = ()

        columns = [
            column
            for column in self.columns.iterall()
            if not (column.column.exclude_from_export or column.name in exclude_columns)
        ]

        yield [force_str(column.header, strings_only=True) for column in columns]

        for row in self.rows:
            yield [
                force_str(row.get_cell_value(column.name), strings_only=True) for column in columns
            ]

    def has_footer(self):


## ... source file continues with no further get_template examples...

```

