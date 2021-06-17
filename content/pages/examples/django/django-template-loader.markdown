title: django.template loader Example Code
category: page
slug: django-template-loader-examples
sortorder: 500011368
toc: False
sidebartitle: django.template loader
meta: Python example code that shows how to use the loader callable from the django.template module of the Django project.


`loader` is a callable within the `django.template` module of the Django project.

<a href="/django-template-context-examples.html">Context</a>,
<a href="/django-template-engine-examples.html">Engine</a>,
<a href="/django-template-library-examples.html">Library</a>,
<a href="/django-template-node-examples.html">Node</a>,
<a href="/django-template-nodelist-examples.html">NodeList</a>,
<a href="/django-template-origin-examples.html">Origin</a>,
<a href="/django-template-requestcontext-examples.html">RequestContext</a>,
<a href="/django-template-template-examples.html">Template</a>,
<a href="/django-template-templatedoesnotexist-examples.html">TemplateDoesNotExist</a>,
<a href="/django-template-templatesyntaxerror-examples.html">TemplateSyntaxError</a>,
<a href="/django-template-variable-examples.html">Variable</a>,
<a href="/django-template-context-examples.html">context</a>,
<a href="/django-template-engine-examples.html">engine</a>,
and <a href="/django-template-library-examples.html">library</a>
are several other callables with code examples from the same `django.template` package.

## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / plugin_pool.py**](https://github.com/divio/django-cms/blob/develop/cms/./plugin_pool.py)

```python
# plugin_pool.py
from operator import attrgetter

from django.core.exceptions import ImproperlyConfigured
from django.urls import re_path, include
from django.template.defaultfilters import slugify
from django.utils.encoding import force_text
from django.utils.functional import cached_property
from django.utils.module_loading import autodiscover_modules
from django.utils.translation import get_language, deactivate_all, activate
from django.template import TemplateDoesNotExist, TemplateSyntaxError

from cms.exceptions import PluginAlreadyRegistered, PluginNotRegistered
from cms.plugin_base import CMSPluginBase
from cms.utils.conf import get_cms_setting
from cms.utils.helpers import normalize_name


class PluginPool:

    def __init__(self):
        self.plugins = {}
        self.discovered = False

    def _clear_cached(self):
        if 'registered_plugins' in self.__dict__:
            del self.__dict__['registered_plugins']

        if 'plugins_with_extra_menu' in self.__dict__:
            del self.__dict__['plugins_with_extra_menu']

        if 'plugins_with_extra_placeholder_menu' in self.__dict__:
            del self.__dict__['plugins_with_extra_placeholder_menu']

    def discover_plugins(self):
        if self.discovered:


## ... source file abbreviated to get to loader examples ...


        autodiscover_modules('cms_plugins')
        self.discovered = True

    def clear(self):
        self.discovered = False
        self.plugins = {}
        self._clear_cached()

    def validate_templates(self, plugin=None):
        if plugin:
            plugins = [plugin]
        else:
            plugins = self.plugins.values()
        for plugin in plugins:
            if (plugin.render_plugin and not type(plugin.render_plugin) == property
                    or hasattr(plugin.model, 'render_template')
                    or hasattr(plugin, 'get_render_template')):
                if (plugin.render_template is None and
                        not hasattr(plugin, 'get_render_template')):
                    raise ImproperlyConfigured(
                        "CMS Plugins must define a render template, "
                        "a get_render_template method or "
                        "set render_plugin=False: %s" % plugin
                    )
                elif not hasattr(plugin, 'get_render_template'):
~~                    from django.template import loader

                    template = plugin.render_template
                    if isinstance(template, str) and template:
                        try:
~~                            loader.get_template(template)
                        except TemplateDoesNotExist as e:
                            if str(e) == template:
                                raise ImproperlyConfigured(
                                    "CMS Plugins must define a render template (%s) that exists: %s"
                                    % (plugin, template)
                                )
                            else:
                                pass
                        except TemplateSyntaxError:
                            pass
            else:
                if plugin.allow_children:
                    raise ImproperlyConfigured(
                        "CMS Plugins can not define render_plugin=False and allow_children=True: %s"
                        % plugin
                    )

    def register_plugin(self, plugin):
        if not issubclass(plugin, CMSPluginBase):
            raise ImproperlyConfigured(
                "CMS Plugins must be subclasses of CMSPluginBase, %r is not."
                % plugin
            )
        plugin_name = plugin.__name__


## ... source file continues with no further loader examples...

```


## Example 2 from django-extensions
[django-extensions](https://github.com/django-extensions/django-extensions)
([project documentation](https://django-extensions.readthedocs.io/en/latest/)
and [PyPI page](https://pypi.org/project/django-extensions/))
is a [Django](/django.html) project that adds a bunch of additional
useful commands to the `manage.py` interface. This
[GoDjango video](https://www.youtube.com/watch?v=1F6G3ONhr4k) provides a
quick overview of what you get when you install it into your Python
environment.

The django-extensions project is open sourced under the
[MIT license](https://github.com/django-extensions/django-extensions/blob/master/LICENSE).

[**django-extensions / django_extensions / management / modelviz.py**](https://github.com/django-extensions/django-extensions/blob/master/django_extensions/management/modelviz.py)

```python
# modelviz.py

import datetime
import os
import re

from django.apps import apps
from django.db.models.fields.related import (
    ForeignKey, ManyToManyField, OneToOneField, RelatedField,
)
from django.contrib.contenttypes.fields import GenericRelation
~~from django.template import Context, Template, loader
from django.utils.encoding import force_str
from django.utils.safestring import mark_safe
from django.utils.translation import activate as activate_language


__version__ = "1.1"
__license__ = "Python"
__author__ = "Bas van Oostveen <v.oostveen@gmail.com>",
__contributors__ = [
    "Antonio Cavedoni <http://cavedoni.com/>"
    "Stefano J. Attardi <http://attardi.org/>",
    "Carlo C8E Miron",
    "Andre Campos <cahenan@gmail.com>",
    "Justin Findlay <jfindlay@gmail.com>",
    "Alexander Houben <alexander@houben.ch>",
    "Joern Hees <gitdev@joernhees.de>",
    "Kevin Cherepski <cherepski@gmail.com>",
    "Jose Tomas Tocino <theom3ga@gmail.com>",
    "Adam Dobrawy <naczelnik@jawnosc.tk>",
    "Mikkel Munch Mortensen <https://www.detfalskested.dk/>",
    "Andrzej Bistram <andrzej.bistram@gmail.com>",
    "Daniel Lipsitt <danlipsitt@gmail.com>",
]


## ... source file abbreviated to get to loader examples ...


    def use_model(self, model_name):
        if self.include_models:
            for model_pattern in self.include_models:
                model_pattern = '^%s$' % model_pattern.replace('*', '.*')
                if re.search(model_pattern, model_name):
                    return True
        if self.exclude_models:
            for model_pattern in self.exclude_models:
                model_pattern = '^%s$' % model_pattern.replace('*', '.*')
                if re.search(model_pattern, model_name):
                    return False
        return not self.include_models

    def skip_field(self, field):
        if self.exclude_columns:
            if self.verbose_names and field.verbose_name:
                if field.verbose_name in self.exclude_columns:
                    return True
            if field.name in self.exclude_columns:
                return True
        return False


def generate_dot(graph_data, template='django_extensions/graph_models/digraph.dot'):
    if isinstance(template, str):
~~        template = loader.get_template(template)

    if not isinstance(template, Template) and not (hasattr(template, 'template') and isinstance(template.template, Template)):
        raise Exception("Default Django template loader isn't used. "
                        "This can lead to the incorrect template rendering. "
                        "Please, check the settings.")

    c = Context(graph_data).flatten()
    dot = template.render(c)

    return dot


def generate_graph_data(*args, **kwargs):
    generator = ModelGraph(*args, **kwargs)
    generator.generate_graph_data()
    return generator.get_graph_data()


def use_model(model, include_models, exclude_models):
    generator = ModelGraph([], include_models=include_models, exclude_models=exclude_models)
    return generator.use_model(model)



## ... source file continues with no further loader examples...

```


## Example 3 from django-filter
[django-filter](https://github.com/carltongibson/django-filter)
([project documentation](https://django-filter.readthedocs.io/en/master/)
and
[PyPI page](https://pypi.org/project/django-filter/2.2.0/))
makes it easier to filter down querysets from the
[Django ORM](/django-orm.html) by providing common bits of boilerplate
code. django-filter is provided as
[open source](https://github.com/carltongibson/django-filter/blob/master/LICENSE).

[**django-filter / django_filters / rest_framework / backends.py**](https://github.com/carltongibson/django-filter/blob/master/django_filters/rest_framework/backends.py)

```python
# backends.py
import warnings

~~from django.template import loader
from django.utils.deprecation import RenameMethodsBase

from .. import compat, utils
from . import filters, filterset


class RenameAttributes(utils.RenameAttributesBase, RenameMethodsBase):
    renamed_attributes = (
        ('default_filter_set', 'filterset_base', utils.MigrationNotice),
    )
    renamed_methods = (
        ('get_filter_class', 'get_filterset_class', utils.MigrationNotice),
    )


class DjangoFilterBackend(metaclass=RenameAttributes):
    filterset_base = filterset.FilterSet
    raise_exception = True

    @property
    def template(self):
        if compat.is_crispy():
            return 'django_filters/rest_framework/crispy_form.html'
        return 'django_filters/rest_framework/form.html'


## ... source file abbreviated to get to loader examples ...


            return AutoFilterSet

        return None

    def get_filterset_kwargs(self, request, queryset, view):
        return {
            'data': request.query_params,
            'queryset': queryset,
            'request': request,
        }

    def filter_queryset(self, request, queryset, view):
        filterset = self.get_filterset(request, queryset, view)
        if filterset is None:
            return queryset

        if not filterset.is_valid() and self.raise_exception:
            raise utils.translate_validation(filterset.errors)
        return filterset.qs

    def to_html(self, request, queryset, view):
        filterset = self.get_filterset(request, queryset, view)
        if filterset is None:
            return None

~~        template = loader.get_template(self.template)
        context = {'filter': filterset}
        return template.render(context, request)

    def get_coreschema_field(self, field):
        if isinstance(field, filters.NumberFilter):
            field_cls = compat.coreschema.Number
        else:
            field_cls = compat.coreschema.String
        return field_cls(
            description=str(field.extra.get('help_text', ''))
        )

    def get_schema_fields(self, view):
        assert compat.coreapi is not None, 'coreapi must be installed to use `get_schema_fields()`'
        assert compat.coreschema is not None, 'coreschema must be installed to use `get_schema_fields()`'

        try:
            queryset = view.get_queryset()
        except Exception:
            queryset = None
            warnings.warn(
                "{} is not compatible with schema generation".format(view.__class__)
            )



## ... source file continues with no further loader examples...

```


## Example 4 from django-floppyforms
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

[**django-floppyforms / floppyforms / widgets.py**](https://github.com/jazzband/django-floppyforms/blob/master/floppyforms/./widgets.py)

```python
# widgets.py
import datetime
import re
from itertools import chain

import django
from django import forms
from django.conf import settings
from django.forms.widgets import FILE_INPUT_CONTRADICTION
~~from django.template import loader
from django.utils import datetime_safe, formats
from django.utils.dates import MONTHS
from django.utils.encoding import force_str
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .compat import MULTIVALUE_DICT_TYPES, flatten_contexts


from django.forms.utils import to_current_timezone


RE_DATE = re.compile(r'(\d{4})-(\d\d?)-(\d\d?)$')


__all__ = (
    'TextInput', 'PasswordInput', 'HiddenInput', 'ClearableFileInput',
    'FileInput', 'DateInput', 'DateTimeInput', 'TimeInput', 'Textarea',
    'CheckboxInput', 'Select', 'NullBooleanSelect', 'SelectMultiple',
    'RadioSelect', 'CheckboxSelectMultiple', 'SearchInput', 'RangeInput',
    'ColorInput', 'EmailInput', 'URLInput', 'PhoneNumberInput', 'NumberInput',
    'IPAddressInput', 'MultiWidget', 'Widget', 'SplitDateTimeWidget',
    'SplitHiddenDateTimeWidget', 'MultipleHiddenInput', 'SelectDateWidget',


## ... source file abbreviated to get to loader examples ...



        if value is None:
            value = ''

        if value != '':
            context['value'] = self.format_value(value)

        context.update(self.get_context_data())
        context['attrs'] = self.build_attrs(attrs)

        for key, attr in context['attrs'].items():
            if attr == 1:
                if not isinstance(attr, bool):
                    context['attrs'][key] = str(attr)

        if self.datalist is not None:
            context['datalist'] = self.datalist
        return context

    def render(self, name, value, attrs=None, **kwargs):
        template_name = kwargs.pop('template_name', None)
        if template_name is None:
            template_name = self.template_name
        context = self.get_context(name, value, attrs=attrs or {})
        context = flatten_contexts(self.context_instance, context)
~~        return loader.render_to_string(template_name, context)


class TextInput(Input):
    template_name = 'floppyforms/text.html'
    input_type = 'text'

    def __init__(self, *args, **kwargs):
        if kwargs.get('attrs', None) is not None:
            self.input_type = kwargs['attrs'].pop('type', self.input_type)
        super(TextInput, self).__init__(*args, **kwargs)


class PasswordInput(TextInput):
    template_name = 'floppyforms/password.html'
    input_type = 'password'

    def __init__(self, attrs=None, render_value=False):
        super(PasswordInput, self).__init__(attrs)
        self.render_value = render_value

    def render(self, name, value, attrs=None, renderer=None):
        if not self.render_value:
            value = None
        return super(PasswordInput, self).render(name, value, attrs, renderer=renderer)


## ... source file abbreviated to get to loader examples ...


                    except ValueError:
                        pass
                else:
                    match = RE_DATE.match(value)
                    if match:
                        year_val, month_val, day_val = map(int, match.groups())

        context = self.get_context(name, value, attrs=attrs,
                                   extra_context=extra_context)

        context['year_choices'] = [(i, i) for i in self.years]
        context['year_val'] = year_val

        context['month_choices'] = list(MONTHS.items())
        context['month_val'] = month_val

        context['day_choices'] = [(i, i) for i in range(1, 32)]
        context['day_val'] = day_val


        if self.required is False:
            context['year_choices'].insert(0, self.none_value)
            context['month_choices'].insert(0, self.none_value)
            context['day_choices'].insert(0, self.none_value)

~~        return loader.render_to_string(self.template_name, context)

    def value_from_datadict(self, data, files, name):
        y = data.get(self.year_field % name)
        m = data.get(self.month_field % name)
        d = data.get(self.day_field % name)
        if y == m == d == "0":
            return None
        if y and m and d:
            if settings.USE_L10N:
                input_format = formats.get_format('DATE_INPUT_FORMATS')[0]
                try:
                    date_value = datetime.date(int(y), int(m), int(d))
                except ValueError:
                    return '%s-%s-%s' % (y, m, d)
                else:
                    date_value = datetime_safe.new_date(date_value)
                    return date_value.strftime(input_format)
            else:
                return '%s-%s-%s' % (y, m, d)
        return data.get(name, None)



## ... source file continues with no further loader examples...

```


## Example 5 from django-haystack
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

[**django-haystack / haystack / fields.py**](https://github.com/django-haystack/django-haystack/blob/master/haystack/./fields.py)

```python
# fields.py
import re
from inspect import ismethod

~~from django.template import loader
from django.utils import datetime_safe

from haystack.exceptions import SearchFieldError
from haystack.utils import get_model_ct_tuple


class NOT_PROVIDED:
    pass


DATE_REGEX = re.compile(
    r"^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})(?:|T00:00:00Z?)$"
)
DATETIME_REGEX = re.compile(
    r"^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})(T|\s+)(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2}).*?$"
)




class SearchField(object):

    field_type = None



## ... source file abbreviated to get to loader examples ...


            return []

        elif not hasattr(current_objects, "__iter__"):
            current_objects = [current_objects]

        return current_objects

    def prepare_template(self, obj):
        if self.instance_name is None and self.template_name is None:
            raise SearchFieldError(
                "This field requires either its instance_name variable to be populated or an explicit template_name in order to load the correct template."
            )

        if self.template_name is not None:
            template_names = self.template_name

            if not isinstance(template_names, (list, tuple)):
                template_names = [template_names]
        else:
            app_label, model_name = get_model_ct_tuple(obj)
            template_names = [
                "search/indexes/%s/%s_%s.txt"
                % (app_label, model_name, self.instance_name)
            ]

~~        t = loader.select_template(template_names)
        return t.render({"object": obj})

    def convert(self, value):
        return value


class CharField(SearchField):
    field_type = "string"

    def __init__(self, **kwargs):
        if kwargs.get("facet_class") is None:
            kwargs["facet_class"] = FacetCharField

        super(CharField, self).__init__(**kwargs)

    def prepare(self, obj):
        return self.convert(super(CharField, self).prepare(obj))

    def convert(self, value):
        if value is None:
            return None

        return str(value)



## ... source file continues with no further loader examples...

```


## Example 6 from django-rest-framework
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

[**django-rest-framework / rest_framework / renderers.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./renderers.py)

```python
# renderers.py
import base64
from collections import OrderedDict
from urllib import parse

from django import forms
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.paginator import Page
from django.http.multipartparser import parse_header
~~from django.template import engines, loader
from django.urls import NoReverseMatch
from django.utils.html import mark_safe

from rest_framework import VERSION, exceptions, serializers, status
from rest_framework.compat import (
    INDENT_SEPARATORS, LONG_SEPARATORS, SHORT_SEPARATORS, coreapi, coreschema,
    pygments_css, yaml
)
from rest_framework.exceptions import ParseError
from rest_framework.request import is_form_media_type, override_method
from rest_framework.settings import api_settings
from rest_framework.utils import encoders, json
from rest_framework.utils.breadcrumbs import get_breadcrumbs
from rest_framework.utils.field_mapping import ClassLookupDict


def zero_as_none(value):
    return None if value == 0 else value


class BaseRenderer:
    media_type = None
    format = None
    charset = 'utf-8'


## ... source file abbreviated to get to loader examples ...


    exception_template_names = [
        '%(status_code)s.html',
        'api_exception.html'
    ]
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        renderer_context = renderer_context or {}
        view = renderer_context['view']
        request = renderer_context['request']
        response = renderer_context['response']

        if response.exception:
            template = self.get_exception_template(response)
        else:
            template_names = self.get_template_names(response, view)
            template = self.resolve_template(template_names)

        if hasattr(self, 'resolve_context'):
            context = self.resolve_context(data, request, response)
        else:
            context = self.get_template_context(data, renderer_context)
        return template.render(context, request=request)

    def resolve_template(self, template_names):
~~        return loader.select_template(template_names)

    def get_template_context(self, data, renderer_context):
        response = renderer_context['response']
        if response.exception:
            data['status_code'] = response.status_code
        return data

    def get_template_names(self, response, view):
        if response.template_name:
            return [response.template_name]
        elif self.template_name:
            return [self.template_name]
        elif hasattr(view, 'get_template_names'):
            return view.get_template_names()
        elif hasattr(view, 'template_name'):
            return [view.template_name]
        raise ImproperlyConfigured(
            'Returned a template response with no `template_name` attribute set on either the view or response'
        )

    def get_exception_template(self, response):
        template_names = [name % {'status_code': response.status_code}
                          for name in self.exception_template_names]



## ... source file abbreviated to get to loader examples ...


        serializers.JSONField: {
            'base_template': 'textarea.html',
        },
    })

    def render_field(self, field, parent_style):
        if isinstance(field._field, serializers.HiddenField):
            return ''

        style = self.default_style[field].copy()
        style.update(field.style)
        if 'template_pack' not in style:
            style['template_pack'] = parent_style.get('template_pack', self.template_pack)
        style['renderer'] = self

        field = field.as_form_field()

        if style.get('input_type') == 'datetime-local' and isinstance(field.value, str):
            field.value = field.value.rstrip('Z')

        if 'template' in style:
            template_name = style['template']
        else:
            template_name = style['template_pack'].strip('/') + '/' + style['base_template']

~~        template = loader.get_template(template_name)
        context = {'field': field, 'style': style}
        return template.render(context)

    def render(self, data, accepted_media_type=None, renderer_context=None):
        renderer_context = renderer_context or {}
        form = data.serializer

        style = renderer_context.get('style', {})
        if 'template_pack' not in style:
            style['template_pack'] = self.template_pack
        style['renderer'] = self

        template_pack = style['template_pack'].strip('/')
        template_name = template_pack + '/' + self.base_template
~~        template = loader.get_template(template_name)
        context = {
            'form': form,
            'style': style
        }
        return template.render(context)


class BrowsableAPIRenderer(BaseRenderer):
    media_type = 'text/html'
    format = 'api'
    template = 'rest_framework/api.html'
    filter_template = 'rest_framework/filters/base.html'
    code_style = 'emacs'
    charset = 'utf-8'
    form_renderer_class = HTMLFormRenderer

    def get_default_renderer(self, view):
        renderers = [renderer for renderer in view.renderer_classes
                     if not issubclass(renderer, BrowsableAPIRenderer)]
        non_template_renderers = [renderer for renderer in renderers
                                  if not hasattr(renderer, 'get_template_names')]

        if not renderers:
            return None


## ... source file abbreviated to get to loader examples ...


        if not hasattr(view, 'get_queryset') or not hasattr(view, 'filter_backends'):
            return

        paginator = getattr(view, 'paginator', None)
        if isinstance(data, list):
            pass
        elif paginator is not None and data is not None:
            try:
                paginator.get_results(data)
            except (TypeError, KeyError):
                return
        elif not isinstance(data, list):
            return

        queryset = view.get_queryset()
        elements = []
        for backend in view.filter_backends:
            if hasattr(backend, 'to_html'):
                html = backend().to_html(request, queryset, view)
                if html:
                    elements.append(html)

        if not elements:
            return

~~        template = loader.get_template(self.filter_template)
        context = {'elements': elements}
        return template.render(context)

    def get_context(self, data, accepted_media_type, renderer_context):
        view = renderer_context['view']
        request = renderer_context['request']
        response = renderer_context['response']

        renderer = self.get_default_renderer(view)

        raw_data_post_form = self.get_raw_data_form(data, view, 'POST', request)
        raw_data_put_form = self.get_raw_data_form(data, view, 'PUT', request)
        raw_data_patch_form = self.get_raw_data_form(data, view, 'PATCH', request)
        raw_data_put_or_patch_form = raw_data_put_form or raw_data_patch_form

        response_headers = OrderedDict(sorted(response.items()))
        renderer_content_type = ''
        if renderer:
            renderer_content_type = '%s' % renderer.media_type
            if renderer.charset:
                renderer_content_type += ' ;%s' % renderer.charset
        response_headers['Content-Type'] = renderer_content_type

        if getattr(view, 'paginator', None) and view.paginator.display_page_controls:


## ... source file abbreviated to get to loader examples ...


            'put_form': self.get_rendered_html_form(data, view, 'PUT', request),
            'post_form': self.get_rendered_html_form(data, view, 'POST', request),
            'delete_form': self.get_rendered_html_form(data, view, 'DELETE', request),
            'options_form': self.get_rendered_html_form(data, view, 'OPTIONS', request),

            'extra_actions': self.get_extra_actions(view, response.status_code),

            'filter_form': self.get_filter_form(data, view, request),

            'raw_data_put_form': raw_data_put_form,
            'raw_data_post_form': raw_data_post_form,
            'raw_data_patch_form': raw_data_patch_form,
            'raw_data_put_or_patch_form': raw_data_put_or_patch_form,

            'display_edit_forms': bool(response.status_code != 403),

            'api_settings': api_settings,
            'csrf_cookie_name': csrf_cookie_name,
            'csrf_header_name': csrf_header_name
        }

    def render(self, data, accepted_media_type=None, renderer_context=None):
        self.accepted_media_type = accepted_media_type or ''
        self.renderer_context = renderer_context or {}

~~        template = loader.get_template(self.template)
        context = self.get_context(data, accepted_media_type, renderer_context)
        ret = template.render(context, request=renderer_context['request'])

        response = renderer_context['response']
        if response.status_code == status.HTTP_204_NO_CONTENT:
            response.status_code = status.HTTP_200_OK

        return ret


class AdminRenderer(BrowsableAPIRenderer):
    template = 'rest_framework/admin.html'
    format = 'admin'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        self.accepted_media_type = accepted_media_type or ''
        self.renderer_context = renderer_context or {}

        response = renderer_context['response']
        request = renderer_context['request']
        view = self.renderer_context['view']

        if response.status_code == status.HTTP_400_BAD_REQUEST:
            self.error_form = self.get_rendered_html_form(data, view, request.method, request)
            self.error_title = {'POST': 'Create', 'PUT': 'Edit'}.get(request.method, 'Errors')

            with override_method(view, request, 'GET') as request:
                response = view.get(request, *view.args, **view.kwargs)
            data = response.data

~~        template = loader.get_template(self.template)
        context = self.get_context(data, accepted_media_type, renderer_context)
        ret = template.render(context, request=renderer_context['request'])

        if response.status_code == status.HTTP_201_CREATED and 'Location' in response:
            response.status_code = status.HTTP_303_SEE_OTHER
            response['Location'] = request.build_absolute_uri()
            ret = ''

        if response.status_code == status.HTTP_204_NO_CONTENT:
            response.status_code = status.HTTP_303_SEE_OTHER
            try:
                response['Location'] = self.get_breadcrumbs(request)[-2][1]
            except KeyError:
                response['Location'] = request.full_path
            ret = ''

        return ret

    def get_context(self, data, accepted_media_type, renderer_context):
        context = super().get_context(
            data, accepted_media_type, renderer_context
        )

        paginator = getattr(context['view'], 'paginator', None)


## ... source file abbreviated to get to loader examples ...


        except (KeyError, NoReverseMatch):
            return


class DocumentationRenderer(BaseRenderer):
    media_type = 'text/html'
    format = 'html'
    charset = 'utf-8'
    template = 'rest_framework/docs/index.html'
    error_template = 'rest_framework/docs/error.html'
    code_style = 'emacs'
    languages = ['shell', 'javascript', 'python']

    def get_context(self, data, request):
        return {
            'document': data,
            'langs': self.languages,
            'lang_htmls': ["rest_framework/docs/langs/%s.html" % language for language in self.languages],
            'lang_intro_htmls': ["rest_framework/docs/langs/%s-intro.html" % language for language in self.languages],
            'code_style': pygments_css(self.code_style),
            'request': request
        }

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if isinstance(data, coreapi.Document):
~~            template = loader.get_template(self.template)
            context = self.get_context(data, renderer_context['request'])
            return template.render(context, request=renderer_context['request'])
        else:
~~            template = loader.get_template(self.error_template)
            context = {
                "data": data,
                "request": renderer_context['request'],
                "response": renderer_context['response'],
                "debug": settings.DEBUG,
            }
            return template.render(context, request=renderer_context['request'])


class SchemaJSRenderer(BaseRenderer):
    media_type = 'application/javascript'
    format = 'javascript'
    charset = 'utf-8'
    template = 'rest_framework/schema.js'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        codec = coreapi.codecs.CoreJSONCodec()
        schema = base64.b64encode(codec.encode(data)).decode('ascii')

~~        template = loader.get_template(self.template)
        context = {'schema': mark_safe(schema)}
        request = renderer_context['request']
        return template.render(context, request=request)


class MultiPartRenderer(BaseRenderer):
    media_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'
    format = 'multipart'
    charset = 'utf-8'
    BOUNDARY = 'BoUnDaRyStRiNg'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        from django.test.client import encode_multipart

        if hasattr(data, 'items'):
            for key, value in data.items():
                assert not isinstance(value, dict), (
                    "Test data contained a dictionary value for key '%s', "
                    "but multipart uploads do not support nested data. "
                    "You may want to consider using format='json' in this "
                    "test case." % key
                )
        return encode_multipart(self.BOUNDARY, data)



## ... source file continues with no further loader examples...

```


## Example 7 from django-request-token
[Django Request Token](https://github.com/yunojuno/django-request-token)
([PyPI package information](https://pypi.org/project/django-request-token/0.13/))
encapsulates the logic for issuing expiring and one-time tokens
with a [Django](/django.html) web application to use with protected URLs.
Note that [PostgreSQL](/postgresql.html) as your backend
[database](/databases.html) is a dependency for using this project.

The Django Request Token project is open sourced under the
[MIT license](https://github.com/yunojuno/django-request-token/blob/master/LICENSE).

[**django-request-token / request_token / apps.py**](https://github.com/yunojuno/django-request-token/blob/master/request_token/./apps.py)

```python
# apps.py
from __future__ import annotations

from django.apps import AppConfig
from django.core.exceptions import ImproperlyConfigured
~~from django.template import TemplateDoesNotExist, loader

from .settings import FOUR03_TEMPLATE


class RequestTokenAppConfig(AppConfig):

    name = "request_token"
    verbose_name = "JWT Request Tokens"

    def ready(self) -> None:
        super(RequestTokenAppConfig, self).ready()
        if FOUR03_TEMPLATE:
            check_template(FOUR03_TEMPLATE)


def check_template(template: str) -> None:
    try:
~~        loader.get_template(template)
    except TemplateDoesNotExist:
        raise ImproperlyConfigured(
            f"Custom request token template does not exist: '{template}'"
        )



## ... source file continues with no further loader examples...

```


## Example 8 from graphite-web
[Graphite](https://github.com/graphite-project/graphite-web)
([project website](http://graphiteapp.org/),
[documentation](https://graphite.readthedocs.io/en/latest/) and
[PyPI package information](https://pypi.org/project/graphite-web/))
is a metrics collection and visualization tool, built with both
Python and JavaScript. Metrics are collected by a Node.js application
and displayed using a [Django](/django.html) web application,
called "Graphite-Web", which is one of three core projects under
the Graphite umbrella (the other two are
[Carbon](https://github.com/graphite-project/carbon) and
[Whisper](https://github.com/graphite-project/whisper)).

Graphite is provided as open sourced under the
[Apache License 2.0](https://github.com/graphite-project/whisper/blob/master/LICENSE).

[**graphite-web / webapp / graphite / views.py**](https://github.com/graphite-project/graphite-web/blob/master/webapp/graphite/views.py)

```python
# views.py
import traceback
from django.http import HttpResponseServerError
~~from django.template import loader


def server_error(request, template_name='500.html'):
~~    template = loader.get_template(template_name)
    context = {'stacktrace' : traceback.format_exc()}
    return HttpResponseServerError(template.render(context))



## ... source file continues with no further loader examples...

```

