title: django.utils.text capfirst Example Code
category: page
slug: django-utils-text-capfirst-examples
sortorder: 500011489
toc: False
sidebartitle: django.utils.text capfirst
meta: Python example code for the capfirst callable from the django.utils.text module of the Django project.


capfirst is a callable within the django.utils.text module of the Django project.


## Example 1 from django-filter
[django-filter](https://github.com/carltongibson/django-filter)
([project documentation](https://django-filter.readthedocs.io/en/master/)
and
[PyPI page](https://pypi.org/project/django-filter/2.2.0/))
makes it easier to filter down querysets from the
[Django ORM](/django-orm.html) by providing common bits of boilerplate
code. django-filter is provided as
[open source](https://github.com/carltongibson/django-filter/blob/master/LICENSE).

[**django-filter / django_filters / utils.py**](https://github.com/carltongibson/django-filter/blob/master/django_filters/./utils.py)

```python
# utils.py
import warnings
from collections import OrderedDict

from django.conf import settings
from django.core.exceptions import FieldDoesNotExist, FieldError
from django.db import models
from django.db.models.constants import LOOKUP_SEP
from django.db.models.expressions import Expression
from django.db.models.fields.related import ForeignObjectRel, RelatedField
from django.utils import timezone
from django.utils.encoding import force_str
~~from django.utils.text import capfirst
from django.utils.translation import gettext as _

from .exceptions import FieldLookupError


def deprecate(msg, level_modifier=0):
    warnings.warn(msg, MigrationNotice, stacklevel=3 + level_modifier)


class MigrationNotice(DeprecationWarning):
    url = 'https://django-filter.readthedocs.io/en/master/guide/migration.html'

    def __init__(self, message):
        super().__init__('%s See: %s' % (message, self.url))


class RenameAttributesBase(type):
    renamed_attributes = ()

    def __new__(metacls, name, bases, attrs):
        old_names = [r[0] for r in metacls.renamed_attributes]
        old_names = [name for name in old_names if name in attrs]
        old_attrs = {name: attrs.pop(name) for name in old_names}



## ... source file abbreviated to get to capfirst examples ...


            names.append(force_str(part.verbose_name))

    return ' '.join(names)


def verbose_lookup_expr(lookup_expr):
    from .conf import settings as app_settings

    VERBOSE_LOOKUPS = app_settings.VERBOSE_LOOKUPS or {}
    lookups = [
        force_str(VERBOSE_LOOKUPS.get(lookup, _(lookup)))
        for lookup in lookup_expr.split(LOOKUP_SEP)
    ]

    return ' '.join(lookups)


def label_for_filter(model, field_name, lookup_expr, exclude=False):
    name = verbose_field_name(model, field_name)
    verbose_expression = [_('exclude'), name] if exclude else [name]

    if isinstance(lookup_expr, str):
        verbose_expression += [verbose_lookup_expr(lookup_expr)]

    verbose_expression = [force_str(part) for part in verbose_expression if part]
~~    verbose_expression = capfirst(' '.join(verbose_expression))

    return verbose_expression


def translate_validation(error_dict):
    from rest_framework.exceptions import ValidationError, ErrorDetail

    exc = OrderedDict(
        (key, [ErrorDetail(e.message % (e.params or ()), code=e.code)
               for e in error_list])
        for key, error_list in error_dict.as_data().items()
    )

    return ValidationError(exc)



## ... source file continues with no further capfirst examples...

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

[**django-haystack / haystack / forms.py**](https://github.com/django-haystack/django-haystack/blob/master/haystack/./forms.py)

```python
# forms.py
from django import forms
from django.utils.encoding import smart_text
~~from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _

from haystack import connections
from haystack.constants import DEFAULT_ALIAS
from haystack.query import EmptySearchQuerySet, SearchQuerySet
from haystack.utils import get_model_ct
from haystack.utils.app_loading import haystack_get_model


def model_choices(using=DEFAULT_ALIAS):
    choices = [
~~        (get_model_ct(m), capfirst(smart_text(m._meta.verbose_name_plural)))
        for m in connections[using].get_unified_index().get_indexed_models()
    ]
    return sorted(choices, key=lambda x: x[1])


class SearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        label=_("Search"),
        widget=forms.TextInput(attrs={"type": "search"}),
    )

    def __init__(self, *args, **kwargs):
        self.searchqueryset = kwargs.pop("searchqueryset", None)
        self.load_all = kwargs.pop("load_all", False)

        if self.searchqueryset is None:
            self.searchqueryset = SearchQuerySet()

        super(SearchForm, self).__init__(*args, **kwargs)

    def no_query_found(self):
        return EmptySearchQuerySet()



## ... source file continues with no further capfirst examples...

```


## Example 3 from django-inline-actions
[django-inline-actions](https://github.com/escaped/django-inline-actions)
([PyPI package information](https://pypi.org/project/django-inline-actions/))
is an extension that adds actions to the [Django](/django.html)
Admin InlineModelAdmin and ModelAdmin changelists. The project is open
sourced under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/escaped/django-inline-actions/blob/master/LICENSE).

[**django-inline-actions / inline_actions / admin.py**](https://github.com/escaped/django-inline-actions/blob/master/inline_actions/./admin.py)

```python
# admin.py
from django.apps import apps
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.safestring import mark_safe
~~from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _


class InlineActionException(Exception):
    pass


class ActionNotCallable(InlineActionException):
    def __init__(self, model_admin, action, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_admin = model_admin
        self.action = action


class BaseInlineActionsMixin:
    INLINE_MODEL_ADMIN = 'inline'
    MODEL_ADMIN = 'admin'

    inline_actions = []

    def get_inline_actions(self, request, obj=None):
        if self.inline_actions is None:
            return []



## ... source file abbreviated to get to capfirst examples ...



        if isinstance(model_admin, admin.options.InlineModelAdmin):
            return self.INLINE_MODEL_ADMIN
        return self.MODEL_ADMIN

    def render_inline_actions(self, obj=None):  # NOQA: C901
        if not (obj and obj.pk):
            return ''

        buttons = []
        for action_name in self.get_inline_actions(self._request, obj):
            action_func = getattr(self, action_name, None)
            if not action_func:
                raise RuntimeError(
                    "Could not find action `{}`".format(action_name))

            action_name = action_func.__name__
            label_handler = getattr(
                self, 'get_{}_label'.format(action_name), None)
            if callable(label_handler):
                description = label_handler(obj=obj)
            else:
                try:
                    description = action_func.short_description
                except AttributeError:
~~                    description = capfirst(action_name.replace('_', ' '))

            css_handler = getattr(
                self, 'get_{}_css'.format(action_name), None)
            if callable(css_handler):
                css_classes = css_handler(obj=obj)
            else:
                try:
                    css_classes = action_func.css_classes
                except AttributeError:
                    css_classes = ''

            action_data = [
                self.__class__.__name__.lower(),
                self._get_admin_type(),
                action_name,
                obj._meta.app_label,
                obj._meta.model_name,
                str(obj.pk),
            ]
            buttons.append(
                '<input type="submit" name="{}" value="{}" class="{}">'.format(
                    '_action__{}'.format('__'.join(action_data)),
                    description,
                    css_classes,


## ... source file continues with no further capfirst examples...

```


## Example 4 from django-jet
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
~~from django.utils.text import capfirst
from django.contrib import messages
from django.utils.encoding import force_text
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
    admin_site = get_admin_site(context)
    request = context['request']

    app_dict = {}
    for model, model_admin in admin_site._registry.items():
        app_label = model._meta.app_label
        try:
            has_module_perms = model_admin.has_module_permission(request)
        except AttributeError:
            has_module_perms = request.user.has_module_perms(app_label) # Fix Django < 1.8 issue

        if has_module_perms:
            perms = model_admin.get_model_perms(request)

            if True in perms.values():
                info = (app_label, model._meta.model_name)
                model_dict = {
~~                    'name': capfirst(model._meta.verbose_name_plural),
                    'object_name': model._meta.object_name,
                    'perms': perms,
                    'model_name': model._meta.model_name
                }
                if perms.get('change', False):
                    try:
                        model_dict['admin_url'] = reverse('admin:%s_%s_changelist' % info, current_app=admin_site.name)
                    except NoReverseMatch:
                        pass
                if perms.get('add', False):
                    try:
                        model_dict['add_url'] = reverse('admin:%s_%s_add' % info, current_app=admin_site.name)
                    except NoReverseMatch:
                        pass
                if app_label in app_dict:
                    app_dict[app_label]['models'].append(model_dict)
                else:
                    try:
                        name = apps.get_app_config(app_label).verbose_name
                    except NameError:
                        name = app_label.title()
                    app_dict[app_label] = {
                        'name': name,
                        'app_label': app_label,


## ... source file abbreviated to get to capfirst examples ...



    split = language_code.split('-', 2)
    if len(split) == 2:
        language_code = '%s-%s' % (split[0].lower(), split[1].upper()) if split[0] != split[1] else split[0]

    language_codes.append(language_code)

    if len(split) == 2:
        language_codes.append(split[0].lower())

    return language_codes


def get_original_menu_items(context):
    if context.get('user') and user_is_authenticated(context['user']):
        pinned_apps = PinnedApplication.objects.filter(user=context['user'].pk).values_list('app_label', flat=True)
    else:
        pinned_apps = []

    original_app_list = get_app_list(context)

    return map(lambda app: {
        'app_label': app['app_label'],
        'url': app['app_url'],
        'url_blank': False,
~~        'label': app.get('name', capfirst(_(app['app_label']))),
        'has_perms': app.get('has_module_perms', False),
        'models': list(map(lambda model: {
            'url': model.get('admin_url'),
            'url_blank': False,
            'name': model['model_name'],
            'object_name': model['object_name'],
            'label': model.get('name', model['object_name']),
            'has_perms': any(model.get('perms', {}).values()),
        }, app['models'])),
        'pinned': app['app_label'] in pinned_apps,
        'custom': False
    }, original_app_list)


def get_menu_item_url(url, original_app_list):
    if isinstance(url, dict):
        url_type = url.get('type')

        if url_type == 'app':
            return original_app_list[url['app_label']]['url']
        elif url_type == 'model':
            models = dict(map(
                lambda x: (x['name'], x['url']),
                original_app_list[url['app_label']]['models']


## ... source file continues with no further capfirst examples...

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

[**django-rest-framework / rest_framework / utils / field_mapping.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/utils/field_mapping.py)

```python
# field_mapping.py
import inspect

from django.core import validators
from django.db import models
~~from django.utils.text import capfirst

from rest_framework.compat import postgres_fields
from rest_framework.validators import UniqueValidator

NUMERIC_FIELD_TYPES = (
    models.IntegerField, models.FloatField, models.DecimalField, models.DurationField,
)


class ClassLookupDict:
    def __init__(self, mapping):
        self.mapping = mapping

    def __getitem__(self, key):
        if hasattr(key, '_proxy_class'):
            base_class = key._proxy_class
        else:
            base_class = key.__class__

        for cls in inspect.getmro(base_class):
            if cls in self.mapping:
                return self.mapping[cls]
        raise KeyError('Class %s not found in lookup.' % base_class.__name__)

    def __setitem__(self, key, value):
        self.mapping[key] = value


def needs_label(model_field, field_name):
    default_label = field_name.replace('_', ' ').capitalize()
~~    return capfirst(model_field.verbose_name) != default_label


def get_detail_view_name(model):
    return '%(model_name)s-detail' % {
        'app_label': model._meta.app_label,
        'model_name': model._meta.object_name.lower()
    }


def get_field_kwargs(field_name, model_field):
    kwargs = {}
    validator_kwarg = list(model_field.validators)

    kwargs['model_field'] = model_field

    if model_field.verbose_name and needs_label(model_field, field_name):
~~        kwargs['label'] = capfirst(model_field.verbose_name)

    if model_field.help_text:
        kwargs['help_text'] = model_field.help_text

    max_digits = getattr(model_field, 'max_digits', None)
    if max_digits is not None:
        kwargs['max_digits'] = max_digits

    decimal_places = getattr(model_field, 'decimal_places', None)
    if decimal_places is not None:
        kwargs['decimal_places'] = decimal_places

    if isinstance(model_field, models.SlugField):
        kwargs['allow_unicode'] = model_field.allow_unicode

    if isinstance(model_field, models.TextField) and not model_field.choices or \
            (postgres_fields and isinstance(model_field, postgres_fields.JSONField)):
        kwargs['style'] = {'base_template': 'textarea.html'}

    if isinstance(model_field, models.AutoField) or not model_field.editable:
        kwargs['read_only'] = True
        return kwargs

    if model_field.has_default() or model_field.blank or model_field.null:


## ... source file abbreviated to get to capfirst examples ...


def get_relation_kwargs(field_name, relation_info):
    model_field, related_model, to_many, to_field, has_through_model, reverse = relation_info
    kwargs = {
        'queryset': related_model._default_manager,
        'view_name': get_detail_view_name(related_model)
    }

    if to_many:
        kwargs['many'] = True

    if to_field:
        kwargs['to_field'] = to_field

    limit_choices_to = model_field and model_field.get_limit_choices_to()
    if limit_choices_to:
        if not isinstance(limit_choices_to, models.Q):
            limit_choices_to = models.Q(**limit_choices_to)
        kwargs['queryset'] = kwargs['queryset'].filter(limit_choices_to)

    if has_through_model:
        kwargs['read_only'] = True
        kwargs.pop('queryset', None)

    if model_field:
        if model_field.verbose_name and needs_label(model_field, field_name):
~~            kwargs['label'] = capfirst(model_field.verbose_name)
        help_text = model_field.help_text
        if help_text:
            kwargs['help_text'] = help_text
        if not model_field.editable:
            kwargs['read_only'] = True
            kwargs.pop('queryset', None)
        if kwargs.get('read_only', False):
            return kwargs

        if model_field.has_default() or model_field.blank or model_field.null:
            kwargs['required'] = False
        if model_field.null:
            kwargs['allow_null'] = True
        if model_field.validators:
            kwargs['validators'] = model_field.validators
        if getattr(model_field, 'unique', False):
            validator = UniqueValidator(queryset=model_field.model._default_manager)
            kwargs['validators'] = kwargs.get('validators', []) + [validator]
        if to_many and not model_field.blank:
            kwargs['allow_empty'] = False

    return kwargs




## ... source file continues with no further capfirst examples...

```


## Example 6 from django-tables2
[django-tables2](https://github.com/jieter/django-tables2)
([projection documentation](https://django-tables2.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-tables2/))
is a code library for [Django](/django.html) that simplifies creating and
displaying tables in [Django templates](/django-templates.html),
especially with more advanced features such as pagination and sorting.
The project and its code are
[available as open source](https://github.com/jieter/django-tables2/blob/master/LICENSE).

[**django-tables2 / django_tables2 / columns / base.py**](https://github.com/jieter/django-tables2/blob/master/django_tables2/columns/base.py)

```python
# base.py
from collections import OrderedDict
from itertools import islice

from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import SafeData
~~from django.utils.text import capfirst

from ..utils import (
    Accessor,
    AttributeDict,
    OrderBy,
    OrderByTuple,
    call_with_appropriate,
    computed_values,
)


class Library:

    def __init__(self):
        self.columns = []

    def register(self, column):
        if not hasattr(column, "from_field"):
            raise ImproperlyConfigured(
                "{} is not a subclass of Column".format(column.__class__.__name__)
            )
        self.columns.append(column)
        return column

    def column_for_field(self, field, **kwargs):
        if field is None:
            return self.columns[0](**kwargs)

        for candidate in reversed(self.columns):
            if hasattr(field, "get_related_field"):
                verbose_name = field.get_related_field().verbose_name
            else:
                verbose_name = getattr(field, "verbose_name", field.name)
~~            kwargs["verbose_name"] = capfirst(verbose_name)
            column = candidate.from_field(field, **kwargs)
            if column is None:
                continue
            return column


library = Library()


class LinkTransform:

    viewname = None
    accessor = None
    attrs = None

    def __init__(self, url=None, accessor=None, attrs=None, reverse_args=None):
        self.url = url
        self.attrs = attrs
        self.accessor = accessor

        if isinstance(reverse_args, (list, tuple)):
            viewname, args = reverse_args
            reverse_args = {"viewname": viewname}
            reverse_args["kwargs" if isinstance(args, dict) else "args"] = args


## ... source file abbreviated to get to capfirst examples ...


    @property
    def orderable(self):
        if self.column.orderable is not None:
            return self.column.orderable
        return self._table.orderable

    @property
    def verbose_name(self):
        if self.column.verbose_name is not None:
            return self.column.verbose_name

        name = self.name.replace("_", " ")

        model = self._table.data.model
        if model:
            field = Accessor(self.accessor).get_field(model)
            if field:
                if hasattr(field, "field"):
                    name = field.field.verbose_name
                else:
                    name = getattr(field, "verbose_name", field.name)

            if isinstance(name, SafeData):
                return name

~~        return capfirst(name)

    @property
    def visible(self):
        return self.column.visible

    @property
    def localize(self):
        return self.column.localize


class BoundColumns:

    def __init__(self, table, base_columns):
        self._table = table
        self.columns = OrderedDict()
        for name, column in base_columns.items():
            self.columns[name] = bound_column = BoundColumn(table, column, name)
            bound_column.render = getattr(table, "render_" + name, column.render)
            bound_column.value = getattr(
                table, "value_" + name, getattr(table, "render_" + name, column.value)
            )
            bound_column.order = getattr(table, "order_" + name, column.order)

    def iternames(self):


## ... source file continues with no further capfirst examples...

```


## Example 7 from django-taggit
[django-taggit](https://github.com/jazzband/django-taggit/)
([PyPI page](https://pypi.org/project/django-taggit/)) provides a way
to create, store, manage and use tags in a [Django](/django.html) project.
The code for django-taggit is
[open source](https://github.com/jazzband/django-taggit/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-taggit / taggit / managers.py**](https://github.com/jazzband/django-taggit/blob/master/taggit/./managers.py)

```python
# managers.py
import uuid
from operator import attrgetter

from django import VERSION
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import connections, models, router
from django.db.models import signals
from django.db.models.fields.related import (
    ManyToManyRel,
    OneToOneRel,
    RelatedField,
    lazy_related_operation,
)
from django.db.models.query_utils import PathInfo
~~from django.utils.text import capfirst
from django.utils.translation import gettext_lazy as _

from taggit.forms import TagField
from taggit.models import (
    CommonGenericTaggedItemBase,
    GenericUUIDTaggedItemBase,
    TaggedItem,
)
from taggit.utils import require_instance_manager


class ExtraJoinRestriction:

    contains_aggregate = False

    def __init__(self, alias, col, content_types):
        self.alias = alias
        self.col = col
        self.content_types = content_types

    def as_sql(self, compiler, connection):
        qn = compiler.quote_name_unless_alias
        if len(self.content_types) == 1:
            extra_where = "{}.{} = %s".format(qn(self.alias), qn(self.col))


## ... source file abbreviated to get to capfirst examples ...


        )

        if not self.remote_field.model:
            self.remote_field.model = self.through._meta.get_field(
                "tag"
            ).remote_field.model

        if self.use_gfk:
            tagged_items = GenericRelation(self.through)
            tagged_items.contribute_to_class(cls, "tagged_items")

        for rel in cls._meta.local_many_to_many:
            if rel == self or not isinstance(rel, TaggableManager):
                continue
            if rel.through == self.through:
                raise ValueError(
                    "You can't have two TaggableManagers with the"
                    " same through model."
                )

    def save_form_data(self, instance, value):
        getattr(instance, self.name).set(*value)

    def formfield(self, form_class=TagField, **kwargs):
        defaults = {
~~            "label": capfirst(self.verbose_name),
            "help_text": self.help_text,
            "required": not self.blank,
        }
        defaults.update(kwargs)
        return form_class(**defaults)

    def value_from_object(self, obj):
        if obj.pk is None:
            return []
        qs = self.through.objects.select_related("tag").filter(
            **self.through.lookup_kwargs(obj)
        )
        return [ti.tag for ti in qs]

    def m2m_reverse_name(self):
        return self.through._meta.get_field("tag").column

    def m2m_reverse_field_name(self):
        return self.through._meta.get_field("tag").name

    def m2m_target_field_name(self):
        return self.model._meta.pk.name

    def m2m_reverse_target_field_name(self):


## ... source file continues with no further capfirst examples...

```


## Example 8 from wagtail
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
from django.db import models, transaction
from django.db.models import Case, Q, Value, When
from django.db.models.functions import Concat, Lower, Substr
from django.http import Http404
from django.http.request import split_domain_port
from django.template.response import TemplateResponse
from django.urls import NoReverseMatch, reverse
from django.utils import timezone
from django.utils.cache import patch_cache_control
from django.utils.functional import cached_property
~~from django.utils.text import capfirst, slugify
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

PAGE_TEMPLATE_VAR = 'page'


class SiteManager(models.Manager):
    def get_queryset(self):
        return super(SiteManager, self).get_queryset().order_by(Lower("hostname"))

    def get_by_natural_key(self, hostname, port):
        return self.get(hostname=hostname, port=port)


## ... source file abbreviated to get to capfirst examples ...


            page_model for page_model in cls.allowed_subpage_models()
            if page_model.is_creatable
        ]

    @classmethod
    def can_exist_under(cls, parent):
        return cls in parent.specific_class.allowed_subpage_models()

    @classmethod
    def can_create_at(cls, parent):
        can_create = cls.is_creatable and cls.can_exist_under(parent)

        if cls.max_count is not None:
            can_create = can_create and cls.objects.count() < cls.max_count

        if cls.max_count_per_parent is not None:
            can_create = can_create and parent.get_children().type(cls).count() < cls.max_count_per_parent

        return can_create

    def can_move_to(self, parent):
        return self.can_exist_under(parent)

    @classmethod
    def get_verbose_name(cls):
~~        return capfirst(cls._meta.verbose_name)

    @property
    def status_string(self):
        if not self.live:
            if self.expired:
                return _("expired")
            elif self.approved_schedule:
                return _("scheduled")
            else:
                return _("draft")
        else:
            if self.approved_schedule:
                return _("live + scheduled")
            elif self.has_unpublished_changes:
                return _("live + draft")
            else:
                return _("live")

    @property
    def approved_schedule(self):
        return self.revisions.exclude(approved_go_live_at__isnull=True).exists()

    def has_unpublished_subtree(self):
        return (not self.live) and (not self.get_descendants().filter(live=True).exists())


## ... source file continues with no further capfirst examples...

```

