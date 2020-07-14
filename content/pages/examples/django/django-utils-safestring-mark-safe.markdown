title: django.utils.safestring mark_safe Example Code
category: page
slug: django-utils-safestring-mark-safe-examples
sortorder: 500011486
toc: False
sidebartitle: django.utils.safestring mark_safe
meta: Python example code for the mark_safe callable from the django.utils.safestring module of the Django project.


mark_safe is a callable within the django.utils.safestring module of the Django project.


## Example 1 from AuditLog
[Auditlog](https://github.com/jjkester/django-auditlog)
([project documentation](https://django-auditlog.readthedocs.io/en/latest/))
is a [Django](/django.html) app that logs changes to Python objects,
similar to the Django admin's logs but with more details and
output formats. Auditlog's source code is provided as open source under the
[MIT license](https://github.com/jjkester/django-auditlog/blob/master/LICENSE).

[**AuditLog / src / auditlog / mixins.py**](https://github.com/jjkester/django-auditlog/blob/master/src/auditlog/mixins.py)

```python
# mixins.py
import json

from django.conf import settings
try:
    from django.core import urlresolvers
except ImportError:
    from django import urls as urlresolvers
try:
    from django.urls.exceptions import NoReverseMatch
except ImportError:
    from django.core.urlresolvers import NoReverseMatch
from django.utils.html import format_html
~~from django.utils.safestring import mark_safe

MAX = 75


class LogEntryAdminMixin(object):

    def created(self, obj):
        return obj.timestamp.strftime('%Y-%m-%d %H:%M:%S')
    created.short_description = 'Created'

    def user_url(self, obj):
        if obj.actor:
            app_label, model = settings.AUTH_USER_MODEL.split('.')
            viewname = 'admin:%s_%s_change' % (app_label, model.lower())
            try:
                link = urlresolvers.reverse(viewname, args=[obj.actor.id])
            except NoReverseMatch:
                return u'%s' % (obj.actor)
            return format_html(u'<a href="{}">{}</a>', link, obj.actor)

        return 'system'
    user_url.short_description = 'User'

    def resource_url(self, obj):


## ... source file abbreviated to get to mark_safe examples ...


            return format_html(u'<a href="{}">{}</a>', link, obj.object_repr)
    resource_url.short_description = 'Resource'

    def msg_short(self, obj):
        if obj.action == 2:
            return ''  # delete
        changes = json.loads(obj.changes)
        s = '' if len(changes) == 1 else 's'
        fields = ', '.join(changes.keys())
        if len(fields) > MAX:
            i = fields.rfind(' ', 0, MAX)
            fields = fields[:i] + ' ..'
        return '%d change%s: %s' % (len(changes), s, fields)
    msg_short.short_description = 'Changes'

    def msg(self, obj):
        if obj.action == 2:
            return ''  # delete
        changes = json.loads(obj.changes)
        msg = '<table><tr><th>#</th><th>Field</th><th>From</th><th>To</th></tr>'
        for i, field in enumerate(sorted(changes), 1):
            value = [i, field] + (['***', '***'] if field == 'password' else changes[field])
            msg += format_html('<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>', *value)

        msg += '</table>'
~~        return mark_safe(msg)
    msg.short_description = 'Changes'



## ... source file continues with no further mark_safe examples...

```


## Example 2 from django-angular
[django-angular](https://github.com/jrief/django-angular)
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / templatetags / djng_tags.py**](https://github.com/jrief/django-angular/blob/master/djng/templatetags/djng_tags.py)

```python
# djng_tags.py
import json

from django.template import Library
from django.template.base import Node, NodeList, TextNode, VariableNode
from django.utils.html import format_html
~~from django.utils.safestring import mark_safe
from django.utils.translation import get_language_from_request

from djng.core.urlresolvers import get_all_remote_methods, get_current_remote_methods


register = Library()


@register.simple_tag(name='djng_all_rmi')
def djng_all_rmi():
~~    return mark_safe(json.dumps(get_all_remote_methods()))


@register.simple_tag(name='djng_current_rmi', takes_context=True)
def djng_current_rmi(context):
~~    return mark_safe(json.dumps(get_current_remote_methods(context.get('view'))))


@register.simple_tag(name='load_djng_urls', takes_context=True)
def djng_urls(context, *namespaces):
    raise DeprecationWarning(
        "load_djng_urls templatetag is deprecated and has been removed from this version of django-angular."
        "Please refer to documentation for updated way to manage django urls in angular.")


class AngularJsNode(Node):
    def __init__(self, django_nodelist, angular_nodelist, variable):
        self.django_nodelist = django_nodelist
        self.angular_nodelist = angular_nodelist
        self.variable = variable

    def render(self, context):
        if self.variable.resolve(context):
            return self.angular_nodelist.render(context)
        return self.django_nodelist.render(context)


@register.tag
def angularjs(parser, token):
    bits = token.contents.split()


## ... source file continues with no further mark_safe examples...

```


## Example 3 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / plugin_rendering.py**](https://github.com/divio/django-cms/blob/develop/cms/./plugin_rendering.py)

```python
# plugin_rendering.py
from __future__ import unicode_literals
from collections import OrderedDict

from functools import partial

from classytags.utils import flatten_context

from django.contrib.sites.models import Site
from django.template import Context
from django.utils.functional import cached_property
from django.utils.module_loading import import_string
~~from django.utils.safestring import mark_safe

from cms.cache.placeholder import get_placeholder_cache, set_placeholder_cache
from cms.toolbar.utils import (
    get_placeholder_toolbar_js,
    get_plugin_toolbar_js,
    get_toolbar_from_request,
)
from cms.utils import get_language_from_request
from cms.utils.conf import get_cms_setting
from cms.utils.permissions import has_plugin_permission
from cms.utils.placeholder import get_toolbar_plugin_struct, restore_sekizai_context
from cms.utils.plugins import get_plugin_restrictions


def _unpack_plugins(parent_plugin):
    found_plugins = []

    for plugin in parent_plugin.child_plugin_instances or []:
        found_plugins.append(plugin)

        if plugin.child_plugin_instances:
            found_plugins.extend(_unpack_plugins(plugin))
    return found_plugins



## ... source file abbreviated to get to mark_safe examples ...


            return False
        return not self._placeholders_are_editable

    def render_placeholder(self, placeholder, context, language=None, page=None,
                           editable=False, use_cache=False, nodelist=None, width=None):
        from sekizai.helpers import Watcher

        language = language or self.request_language
        editable = editable and self._placeholders_are_editable

        if use_cache and not editable and placeholder.cache_placeholder:
            use_cache = self.placeholder_cache_is_enabled()
        else:
            use_cache = False

        if use_cache:
            cached_value = self._get_cached_placeholder_content(
                placeholder=placeholder,
                language=language,
            )
        else:
            cached_value = None

        if cached_value is not None:
            restore_sekizai_context(context, cached_value['sekizai'])
~~            return mark_safe(cached_value['content'])

        context.push()

        width = width or placeholder.default_width
        template = page.get_template() if page else None

        if width:
            context['width'] = width

        for key, value in placeholder.get_extra_context(template).items():
            if key not in context:
                context[key] = value

        if use_cache:
            watcher = Watcher(context)

        plugin_content = self.render_plugins(
            placeholder,
            language=language,
            context=context,
            editable=editable,
            template=template,
        )
        placeholder_content = ''.join(plugin_content)


## ... source file abbreviated to get to mark_safe examples ...


                site_id=self.current_site.pk,
                content=content,
                request=self.request,
            )

        rendered_placeholder = RenderedPlaceholder(
            placeholder=placeholder,
            language=language,
            site_id=self.current_site.pk,
            cached=use_cache,
            editable=editable,
            has_content=bool(placeholder_content),
        )

        if placeholder.pk not in self._rendered_placeholders:
            if not self.toolbar._cache_disabled:
                self.toolbar._cache_disabled = not use_cache
            self._rendered_placeholders[placeholder.pk] = rendered_placeholder

        if editable:
            data = self.get_editable_placeholder_context(placeholder, page=page)
            data['content'] = placeholder_content
            placeholder_content = self.placeholder_edit_template.format(**data)

        context.pop()
~~        return mark_safe(placeholder_content)

    def get_editable_placeholder_context(self, placeholder, page=None):
        placeholder_cache = self.get_rendered_plugins_cache(placeholder)
        placeholder_toolbar_js = self.get_placeholder_toolbar_js(placeholder, page)
        plugin_toolbar_js_bits = (self.get_plugin_toolbar_js(plugin, page=page)
                                  for plugin in placeholder_cache['plugins'])
        context = {
            'plugin_js': ''.join(plugin_toolbar_js_bits),
            'placeholder_js': placeholder_toolbar_js,
            'placeholder_id': placeholder.pk,
        }
        return context

    def render_page_placeholder(self, slot, context, inherit,
                                page=None, nodelist=None, editable=True):
        if not self.current_page:
            return ''

        current_page = page or self.current_page
        placeholder_cache = self._placeholders_by_page_cache

        if current_page.pk not in placeholder_cache:
            self._preload_placeholders_for_page(current_page)



## ... source file abbreviated to get to mark_safe examples ...


        if not placeholder:
            placeholder = instance.placeholder

        instance, plugin = instance.get_plugin_instance()

        if not instance or not plugin.render_plugin:
            return ''

        context = PluginContext(context, instance, placeholder)
        context = plugin.render(context, instance, placeholder.slot)
        context = flatten_context(context)

        template = plugin._get_render_template(context, instance, placeholder)
        template = self.templates.get_cached_template(template)

        content = template.render(context)

        for path in get_cms_setting('PLUGIN_PROCESSORS'):
            processor = import_string(path)
            content = processor(instance, placeholder, content, context)

        if editable:
            content = self.plugin_edit_template.format(pk=instance.pk, content=content)
            placeholder_cache = self._rendered_plugins_by_placeholder.setdefault(placeholder.pk, {})
            placeholder_cache.setdefault('plugins', []).append(instance)
~~        return mark_safe(content)

    def render_plugins(self, placeholder, language, context, editable=False, template=None):
        plugins = self.get_plugins_to_render(
            placeholder=placeholder,
            template=template,
            language=language,
        )

        for plugin in plugins:
            plugin._placeholder_cache = placeholder
            yield self.render_plugin(plugin, context, placeholder, editable)

    def _get_cached_placeholder_content(self, placeholder, language):
        site_id = self.current_site.pk
        site_cache = self._placeholders_content_cache.setdefault(site_id, {})
        language_cache = site_cache.setdefault(language, {})

        if placeholder.pk not in language_cache:
            cached_value = get_placeholder_cache(
                placeholder,
                lang=language,
                site_id=site_id,
                request=self.request,
            )


## ... source file abbreviated to get to mark_safe examples ...


            for plugin in _unpack_plugins(plugin):
                yield plugin

    def render_placeholder(self, placeholder, language, page=None):
        rendered_plugins = self.render_plugins(placeholder, language=language, page=page)
        plugin_js_output = ''.join(rendered_plugins)

        placeholder_toolbar_js = self.get_placeholder_toolbar_js(placeholder, page)
        rendered_placeholder = RenderedPlaceholder(
            placeholder=placeholder,
            language=language,
            site_id=self.current_site.pk,
            cached=False,
            editable=True,
        )

        if placeholder.pk not in self._rendered_placeholders:
            self._rendered_placeholders[placeholder.pk] = rendered_placeholder

        placeholder_structure_is = self.placeholder_edit_template.format(
            placeholder_id=placeholder.pk,
            plugin_js=plugin_js_output,
            plugin_menu_js=self.get_placeholder_plugin_menu(placeholder, page=page),
            placeholder_js=placeholder_toolbar_js,
        )
~~        return mark_safe(placeholder_structure_is)

    def render_page_placeholder(self, page, placeholder, language=None):
        return self.render_placeholder(placeholder, language=language, page=page)

    def render_static_placeholder(self, static_placeholder, language=None):
        user = self.request.user

        if not user.has_perm('cms.edit_static_placeholder'):
            return ''

        language = language or self.request_language

        placeholder = static_placeholder.draft
        placeholder.is_static = True

        content = self.render_placeholder(placeholder, language=language)

        if static_placeholder.pk not in self._rendered_static_placeholders:
            self._rendered_static_placeholders[static_placeholder.pk] = static_placeholder
        return content

    def render_plugin(self, instance, page=None):
        placeholder_cache = self._rendered_plugins_by_placeholder.setdefault(instance.placeholder_id, {})
        placeholder_cache.setdefault('plugins', []).append(instance)


## ... source file continues with no further mark_safe examples...

```


## Example 4 from django-debug-toolbar
[django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)
([project documentation](https://github.com/jazzband/django-debug-toolbar)
and [PyPI page](https://pypi.org/project/django-debug-toolbar/))
grants a developer detailed request-response cycle information while
developing a [Django](/django.html) web application.
The code for django-debug-toolbar is
[open source](https://github.com/jazzband/django-debug-toolbar/blob/master/LICENSE)
and maintained by the developer community group known as
[Jazzband](https://jazzband.co/).

[**django-debug-toolbar / debug_toolbar / utils.py**](https://github.com/jazzband/django-debug-toolbar/blob/master/debug_toolbar/./utils.py)

```python
# utils.py
import inspect
import os.path
import re
import sys
from importlib import import_module
from itertools import chain

import django
from django.core.exceptions import ImproperlyConfigured
from django.template import Node
from django.template.loader import render_to_string
~~from django.utils.safestring import mark_safe

from debug_toolbar import settings as dt_settings

try:
    import threading
except ImportError:
    threading = None


django_path = os.path.realpath(os.path.dirname(django.__file__))


def get_module_path(module_name):
    try:
        module = import_module(module_name)
    except ImportError as e:
        raise ImproperlyConfigured("Error importing HIDE_IN_STACKTRACES: {}".format(e))
    else:
        source_path = inspect.getsourcefile(module)
        if source_path.endswith("__init__.py"):
            source_path = os.path.dirname(source_path)
        return os.path.realpath(source_path)




## ... source file abbreviated to get to mark_safe examples ...


def tidy_stacktrace(stack):
    trace = []
    for frame, path, line_no, func_name, text in (f[:5] for f in stack):
        if omit_path(os.path.realpath(path)):
            continue
        text = "".join(text).strip() if text else ""
        frame_locals = (
            frame.f_locals
            if dt_settings.get_config()["ENABLE_STACKTRACES_LOCALS"]
            else None
        )
        trace.append((path, line_no, func_name, text, frame_locals))
    return trace


def render_stacktrace(trace):
    stacktrace = []
    for frame in trace:
        params = (v for v in chain(frame[0].rsplit(os.path.sep, 1), frame[1:]))
        params_dict = {str(idx): v for idx, v in enumerate(params)}
        try:
            stacktrace.append(params_dict)
        except KeyError:
            continue

~~    return mark_safe(
        render_to_string(
            "debug_toolbar/panels/sql_stacktrace.html",
            {
                "stacktrace": stacktrace,
                "show_locals": dt_settings.get_config()["ENABLE_STACKTRACES_LOCALS"],
            },
        )
    )


def get_template_info():
    template_info = None
    cur_frame = sys._getframe().f_back
    try:
        while cur_frame is not None:
            in_utils_module = cur_frame.f_code.co_filename.endswith(
                "/debug_toolbar/utils.py"
            )
            is_get_template_context = (
                cur_frame.f_code.co_name == get_template_context.__name__
            )
            if in_utils_module and is_get_template_context:
                break
            elif cur_frame.f_code.co_name == "render":


## ... source file continues with no further mark_safe examples...

```


## Example 5 from django-extensions
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

[**django-extensions / django_extensions / templatetags / highlighting.py**](https://github.com/django-extensions/django-extensions/blob/master/django_extensions/templatetags/highlighting.py)

```python
# highlighting.py

from django import template
from django.template import (
    Context, Node, Template, TemplateSyntaxError, Variable,
)
from django.template.defaultfilters import stringfilter
~~from django.utils.safestring import mark_safe

try:
    from pygments import highlight as pyghighlight
    from pygments.lexers import get_lexer_by_name
    from pygments.formatters import HtmlFormatter
    HAS_PYGMENTS = True
except ImportError:  # pragma: no cover
    HAS_PYGMENTS = False

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def parse_template(value):
~~    return mark_safe(Template(value).render(Context()))


class CodeNode(Node):
    def __init__(self, language, nodelist, name=''):
        self.language = Variable(language)
        self.nodelist = nodelist
        if name:
            self.name = Variable(name)
        else:
            self.name = None

    def render(self, context):
        code = self.nodelist.render(context).strip()
        lexer = get_lexer_by_name(self.language.resolve(context))
        formatter = HtmlFormatter(linenos=False)
        html = ""
        if self.name:
            name = self.name.resolve(context)
            html = '<div class="predesc"><span>%s</span></div>' % name
        return html + pyghighlight(code, lexer, formatter)


@register.tag
def highlight(parser, token):


## ... source file continues with no further mark_safe examples...

```


## Example 6 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / admin / fileadmin.py**](https://github.com/divio/django-filer/blob/develop/filer/admin/fileadmin.py)

```python
# fileadmin.py
from __future__ import absolute_import

from django import forms
from django.contrib.admin.utils import unquote
from django.http import HttpResponseRedirect
from django.urls import reverse
~~from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

from .. import settings
from ..models import File
from .permissions import PrimitivePermissionAwareModelAdmin
from .tools import AdminContext, admin_url_params_encoded, popup_status


class FileAdminChangeFrom(forms.ModelForm):
    class Meta(object):
        model = File
        exclude = ()


class FileAdmin(PrimitivePermissionAwareModelAdmin):
    list_display = ('label',)
    list_per_page = 10
    search_fields = ['name', 'original_filename', 'sha1', 'description']
    raw_id_fields = ('owner',)
    readonly_fields = ('sha1', 'display_canonical')

    form = FileAdminChangeFrom

    @classmethod


## ... source file abbreviated to get to mark_safe examples ...


            if parent_folder:
                url = reverse('admin:filer-directory_listing',
                              kwargs={'folder_id': parent_folder.id})
            else:
                url = reverse('admin:filer-directory_listing-unfiled_images')
            url = "{0}{1}".format(
                url,
                admin_url_params_encoded(request)
            )
            return HttpResponseRedirect(url)

        return super(FileAdmin, self).delete_view(
            request=request, object_id=object_id,
            extra_context=extra_context)

    def get_model_perms(self, request):
        return {
            'add': False,
            'change': False,
            'delete': False,
        }

    def display_canonical(self, instance):
        canonical = instance.canonical_url
        if canonical:
~~            return mark_safe('<a href="%s">%s</a>' % (canonical, canonical))
        else:
            return '-'
    display_canonical.allow_tags = True
    display_canonical.short_description = _('canonical URL')


FileAdmin.fieldsets = FileAdmin.build_fieldsets()



## ... source file continues with no further mark_safe examples...

```


## Example 7 from django-filter
[django-filter](https://github.com/carltongibson/django-filter)
([project documentation](https://django-filter.readthedocs.io/en/master/)
and
[PyPI page](https://pypi.org/project/django-filter/2.2.0/))
makes it easier to filter down querysets from the
[Django ORM](/django-orm.html) by providing common bits of boilerplate
code. django-filter is provided as
[open source](https://github.com/carltongibson/django-filter/blob/master/LICENSE).

[**django-filter / django_filters / widgets.py**](https://github.com/carltongibson/django-filter/blob/master/django_filters/./widgets.py)

```python
# widgets.py
from collections.abc import Iterable
from copy import deepcopy
from itertools import chain
from re import search, sub

from django import forms
from django.db.models.fields import BLANK_CHOICE_DASH
from django.forms.utils import flatatt
from django.utils.datastructures import MultiValueDict
from django.utils.encoding import force_str
from django.utils.http import urlencode
~~from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _


class LinkWidget(forms.Widget):
    def __init__(self, attrs=None, choices=()):
        super().__init__(attrs)

        self.choices = choices

    def value_from_datadict(self, data, files, name):
        value = super().value_from_datadict(data, files, name)
        self.data = data
        return value

    def render(self, name, value, attrs=None, choices=(), renderer=None):
        if not hasattr(self, 'data'):
            self.data = {}
        if value is None:
            value = ''
        final_attrs = self.build_attrs(self.attrs, extra_attrs=attrs)
        output = ['<ul%s>' % flatatt(final_attrs)]
        options = self.render_options(choices, [value], name)
        if options:
            output.append(options)
        output.append('</ul>')
~~        return mark_safe('\n'.join(output))

    def render_options(self, choices, selected_choices, name):
        selected_choices = set(force_str(v) for v in selected_choices)
        output = []
        for option_value, option_label in chain(self.choices, choices):
            if isinstance(option_label, (list, tuple)):
                for option in option_label:
                    output.append(
                        self.render_option(name, selected_choices, *option))
            else:
                output.append(
                    self.render_option(name, selected_choices,
                                       option_value, option_label))
        return '\n'.join(output)

    def render_option(self, name, selected_choices,
                      option_value, option_label):
        option_value = force_str(option_value)
        if option_label == BLANK_CHOICE_DASH[0][1]:
            option_label = _("All")
        data = self.data.copy()
        data[name] = option_value
        selected = data == self.data or option_value in selected_choices
        try:


## ... source file continues with no further mark_safe examples...

```


## Example 8 from django-floppyforms
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
from django.template import loader
from django.utils import datetime_safe, formats
from django.utils.dates import MONTHS
from django.utils.encoding import force_str
from django.utils.html import conditional_escape
~~from django.utils.safestring import mark_safe
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
    'SlugInput',
)


class Widget(forms.Widget):


## ... source file abbreviated to get to mark_safe examples ...



class HiddenInput(Input):
    template_name = 'floppyforms/hidden.html'
    input_type = 'hidden'


class MultipleHiddenInput(HiddenInput):
    def __init__(self, attrs=None, choices=()):
        super(MultipleHiddenInput, self).__init__(attrs)
        self.choices = choices

    def render(self, name, value, attrs=None, choices=(), renderer=None):
        if value is None:
            value = []

        final_attrs = self.build_attrs(attrs)
        id_ = final_attrs.get('id', None)
        inputs = []
        for i, v in enumerate(value):
            input_attrs = final_attrs.copy()
            if id_:
                input_attrs['id'] = '%s_%s' % (id_, i)
            input_ = HiddenInput()
            input_.is_required = self.is_required
            inputs.append(input_.render(name, force_str(v), input_attrs, renderer=renderer))
~~        return mark_safe("\n".join(inputs))

    def value_from_datadict(self, data, files, name):
        if isinstance(data, MULTIVALUE_DICT_TYPES):
            return data.getlist(name)
        return data.get(name, None)


class SlugInput(TextInput):
    template_name = 'floppyforms/slug.html'

    def get_context(self, name, value, attrs):
        context = super(SlugInput, self).get_context(name, value, attrs)
        context['attrs']['pattern'] = r"[-\w]+"
        return context


class IPAddressInput(TextInput):
    template_name = 'floppyforms/ipaddress.html'

    ip_pattern = (r"(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25"
                  r"[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}")

    def get_context(self, name, value, attrs):
        context = super(IPAddressInput, self).get_context(name, value, attrs)


## ... source file continues with no further mark_safe examples...

```


## Example 9 from django-import-export
[django-import-export](https://github.com/django-import-export/django-import-export)
([documentation](https://django-import-export.readthedocs.io/en/latest/)
and [PyPI page](https://pypi.org/project/django-import-export/))
is a [Django](/django.html) code library for importing and exporting data
from the Django Admin. The tool supports many export and import formats
such as CSV, JSON and YAML. django-import-export is open source under the
[BSD 2-Clause "Simplified" License](https://github.com/django-import-export/django-import-export/blob/master/LICENSE).

[**django-import-export / import_export / resources.py**](https://github.com/django-import-export/django-import-export/blob/master/import_export/./resources.py)

```python
# resources.py
import functools
import logging
import tablib
import traceback
from collections import OrderedDict
from copy import deepcopy

from diff_match_patch import diff_match_patch

import django
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.core.management.color import no_style
from django.core.paginator import Paginator
from django.db import DEFAULT_DB_ALIAS, connections
from django.db.models.fields.related import ForeignObjectRel
from django.db.models.query import QuerySet
from django.db.transaction import (
    TransactionManagementError,
    atomic,
    savepoint,
    savepoint_commit,
    savepoint_rollback
)
from django.utils.encoding import force_str
~~from django.utils.safestring import mark_safe

from . import widgets
from .fields import Field
from .instance_loaders import ModelInstanceLoader
from .results import Error, Result, RowResult
from .utils import atomic_if_using_transaction

if django.VERSION[0] >= 3:
    from django.core.exceptions import FieldDoesNotExist
else:
    from django.db.models.fields import FieldDoesNotExist


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

USE_TRANSACTIONS = getattr(settings, 'IMPORT_EXPORT_USE_TRANSACTIONS', True)
CHUNK_SIZE = getattr(settings, 'IMPORT_EXPORT_CHUNK_SIZE', 1)


def get_related_model(field):
    if hasattr(field, 'related_model'):
        return field.related_model
    if field.rel:


## ... source file abbreviated to get to mark_safe examples ...


                       if not option.startswith('_')]:
            setattr(meta, option, getattr(options, option))
        new_class._meta = meta

        return new_class


class Diff:
    def __init__(self, resource, instance, new):
        self.left = self._export_resource_fields(resource, instance)
        self.right = []
        self.new = new

    def compare_with(self, resource, instance, dry_run=False):
        self.right = self._export_resource_fields(resource, instance)

    def as_html(self):
        data = []
        dmp = diff_match_patch()
        for v1, v2 in zip(self.left, self.right):
            if v1 != v2 and self.new:
                v1 = ""
            diff = dmp.diff_main(force_str(v1), force_str(v2))
            dmp.diff_cleanupSemantic(diff)
            html = dmp.diff_prettyHtml(diff)
~~            html = mark_safe(html)
            data.append(html)
        return data

    def _export_resource_fields(self, resource, instance):
        return [resource.export_field(f, instance) if instance else "" for f in resource.get_user_visible_fields()]


class Resource(metaclass=DeclarativeMetaclass):

    def __init__(self):
        self.fields = deepcopy(self.fields)

        self.create_instances = list()
        self.update_instances = list()
        self.delete_instances = list()

    @classmethod
    def get_result_class(self):
        return Result

    @classmethod
    def get_row_result_class(self):
        return RowResult



## ... source file continues with no further mark_safe examples...

```


## Example 10 from django-inline-actions
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
~~from django.utils.safestring import mark_safe
from django.utils.text import capfirst
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


## ... source file abbreviated to get to mark_safe examples ...


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
                )
            )
~~        return mark_safe('<div class="submit_row inline_actions">{}</div>'.format(
            ''.join(buttons)
        ))
    render_inline_actions.short_description = _("Actions")
    render_inline_actions.allow_tags = True


class InlineActionsMixin(BaseInlineActionsMixin):
    def render_inline_actions(self, obj=None):
        html = super().render_inline_actions(obj=obj)
~~        return mark_safe('</p>{}<p>'.format(html))

    render_inline_actions.short_description = _("Actions")
    render_inline_actions.allow_tags = True

    def get_fields(self, request, obj=None):
        self._request = request

        fields = super().get_fields(request, obj)
        if self.inline_actions is not None:  # is it explicitly disabled?
            fields = list(fields)
            if 'render_inline_actions' not in fields:
                fields.append('render_inline_actions')
        return fields


class InlineActionsModelAdminMixin(BaseInlineActionsMixin):
    class Media:
        css = {
            "all": (
                "inline_actions/css/inline_actions.css",
            )
        }

    def get_list_display(self, request):


## ... source file continues with no further mark_safe examples...

```


## Example 11 from django-jet
[django-jet](https://github.com/geex-arts/django-jet)
([project documentation](https://jet.readthedocs.io/en/latest/),
[PyPI project page](https://pypi.org/project/django-jet/) and
[more information](http://jet.geex-arts.com/))
is a fancy [Django](/django.html) Admin panel replacement.

The django-jet project is open source under the
[GNU Affero General Public License v3.0](https://github.com/geex-arts/django-jet/blob/dev/LICENSE).

[**django-jet / jet / templatetags / jet_tags.py**](https://github.com/geex-arts/django-jet/blob/dev/jet/templatetags/jet_tags.py)

```python
# jet_tags.py
from __future__ import unicode_literals
import json
import os
from django import template
try:
    from django.core.urlresolvers import reverse
except ImportError: # Django 1.11
    from django.urls import reverse

from django.forms import CheckboxInput, ModelChoiceField, Select, ModelMultipleChoiceField, SelectMultiple
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.utils.formats import get_format
~~from django.utils.safestring import mark_safe
from django.utils.encoding import smart_text
from jet import settings, VERSION
from jet.models import Bookmark
from jet.utils import get_model_instance_label, get_model_queryset, get_possible_language_codes, \
    get_admin_site, get_menu_items

try:
    from urllib.parse import parse_qsl
except ImportError:
    from urlparse import parse_qsl


register = template.Library()
assignment_tag = register.assignment_tag if hasattr(register, 'assignment_tag') else register.simple_tag


@assignment_tag
def jet_get_date_format():
    return get_format('DATE_INPUT_FORMATS')[0]


@assignment_tag
def jet_get_time_format():
    return get_format('TIME_INPUT_FORMATS')[0]


## ... source file abbreviated to get to mark_safe examples ...


    return jet_sibling_object(context, False)


@assignment_tag(takes_context=True)
def jet_next_object(context):
    return jet_sibling_object(context, True)


@assignment_tag(takes_context=True)
def jet_popup_response_data(context):
    if context.get('popup_response_data'):
        return context['popup_response_data']

    return json.dumps({
        'action': context.get('action'),
        'value': context.get('value') or context.get('pk_value'),
        'obj': smart_text(context.get('obj')),
        'new_value': context.get('new_value')
    })


@assignment_tag(takes_context=True)
def jet_delete_confirmation_context(context):
    if context.get('deletable_objects') is None and context.get('deleted_objects') is None:
        return ''
~~    return mark_safe('<div class="delete-confirmation-marker"></div>')


@assignment_tag
def jet_static_translation_urls():
    language_codes = get_possible_language_codes()

    urls = []
    url_templates = [
        'jet/js/i18n/jquery-ui/datepicker-__LANGUAGE_CODE__.js',
        'jet/js/i18n/jquery-ui-timepicker/jquery.ui.timepicker-__LANGUAGE_CODE__.js',
        'jet/js/i18n/select2/__LANGUAGE_CODE__.js'
    ]

    static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')

    for tpl in url_templates:
        for language_code in language_codes:
            url = tpl.replace('__LANGUAGE_CODE__', language_code)
            path = os.path.join(static_dir, url)

            if os.path.exists(path):
                urls.append(url)
                break



## ... source file continues with no further mark_safe examples...

```


## Example 12 from django-markdown-view
[django-markdown-view](https://github.com/rgs258/django-markdown-view)
([PyPI package information](https://pypi.org/project/django-markdown-view/))
is a Django extension for serving [Markdown](/markdown.html) files as
[Django templates](/django-templates.html). The project is open
sourced under the
[BSD 3-Clause "New" or "Revised" license](https://github.com/rgs258/django-markdown-view/blob/master/LICENSE).

[**django-markdown-view / markdown_view / views.py**](https://github.com/rgs258/django-markdown-view/blob/master/markdown_view/./views.py)

```python
# views.py
import logging

import markdown
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.template import Engine, Template, Context
from django.template.loader import render_to_string
~~from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
from markdown_view.constants import (
    DEFAULT_MARKDOWN_VIEW_LOADERS,
    DEFAULT_MARKDOWN_VIEW_EXTENSIONS, DEFAULT_MARKDOWN_VIEW_TEMPLATE,
    DEFAULT_MARKDOWN_VIEW_USE_REQUEST_CONTEXT, DEFAULT_MARKDOWN_VIEW_EXTRA_CONTEXT,
)

logger = logging.getLogger(__name__)


class MarkdownView(TemplateView):
    file_name = None

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.file_name:
            engine = Engine(loaders=getattr(
                settings, "MARKDOWN_VIEW_LOADERS", DEFAULT_MARKDOWN_VIEW_LOADERS)
            )
            template = engine.get_template(self.file_name)
            md = markdown.Markdown(extensions=getattr(
                settings,
                "MARKDOWN_VIEW_EXTENSIONS",
                DEFAULT_MARKDOWN_VIEW_EXTENSIONS
            ))
            template = Template(
                "{{% load static %}}{}".format(md.convert(template.source))
            )
            render_context_base = {}
            if getattr(
                settings,
                "MARKDOWN_VIEW_USE_REQUEST_CONTEXT",
                DEFAULT_MARKDOWN_VIEW_USE_REQUEST_CONTEXT
            ):
                render_context_base = context
            render_context = Context({
                **render_context_base,
                **(getattr(
                    settings,
                    "MARKDOWN_VIEW_EXTRA_CONTEXT",
                    DEFAULT_MARKDOWN_VIEW_EXTRA_CONTEXT
                ))
            })
            context.update({
~~                "markdown_content": mark_safe(template.render(render_context)),
~~                "markdown_toc": mark_safe(md.toc),
~~                "page_title": mark_safe(md.toc_tokens[0]['name']),
            })
        return context

    template_name = getattr(
        settings,
        "MARKDOWN_VIEW_TEMPLATE",
        DEFAULT_MARKDOWN_VIEW_TEMPLATE
    )


class LoggedInMarkdownView(LoginRequiredMixin, MarkdownView):
    pass


class StaffMarkdownView(UserPassesTestMixin, MarkdownView):
    def test_func(self):
        return self.request.user.is_active and self.request.user.is_staff



## ... source file continues with no further mark_safe examples...

```


## Example 13 from django-mongonaut
[django-mongonaut](https://github.com/jazzband/django-mongonaut)
([project documentation](https://django-mongonaut.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-mongonaut/))
provides an introspective interface for working with
[MongoDB](/mongodb.html) via mongoengine. The project has its own new code
to map MongoDB to the [Django](/django.html) Admin interface.

django-mongonaut's highlighted features include automatic introspection of
mongoengine documents, the ability to constrain who sees what and what
they can do and full control for adding, editing and deleting documents.

The django-mongonaut project is open sourced under the
[MIT License](https://github.com/jazzband/django-mongonaut/blob/master/LICENSE.txt)
and it is maintained by the developer community group
[Jazzband](https://jazzband.co/).

[**django-mongonaut / mongonaut / templatetags / mongonaut_tags.py**](https://github.com/jazzband/django-mongonaut/blob/master/mongonaut/templatetags/mongonaut_tags.py)

```python
# mongonaut_tags.py

from django import template
from django.urls import reverse
~~from django.utils.safestring import mark_safe

from bson.objectid import ObjectId
from mongoengine import Document
from mongoengine.fields import URLField

register = template.Library()


@register.simple_tag()
def get_document_value(document, key):
    value = getattr(document, key)
    if isinstance(value, ObjectId):
        return value

    if isinstance(document._fields.get(key), URLField):
~~        return mark_safe("""<a href="{0}">{1}</a>""".format(value, value))

    if isinstance(value, Document):
        app_label = value.__module__.replace(".models", "")
        document_name = value._class_name
        url = reverse(
            "document_detail",
            kwargs={'app_label': app_label, 'document_name': document_name,
                    'id': value.id})
~~        return mark_safe("""<a href="{0}">{1}</a>""".format(url, value))

    return value



## ... source file continues with no further mark_safe examples...

```


## Example 14 from django-pipeline
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

[**django-pipeline / pipeline / templatetags / pipeline.py**](https://github.com/jazzband/django-pipeline/blob/master/pipeline/templatetags/pipeline.py)

```python
# pipeline.py
import logging
import subprocess

from django.contrib.staticfiles.storage import staticfiles_storage

from django import template
from django.template.base import Context, VariableDoesNotExist
from django.template.loader import render_to_string
~~from django.utils.safestring import mark_safe

from ..collector import default_collector
from ..conf import settings
from ..exceptions import CompilerError
from ..packager import Packager, PackageNotFound
from ..utils import guess_type

logger = logging.getLogger(__name__)

register = template.Library()


class PipelineMixin(object):
    request = None
    _request_var = None

    @property
    def request_var(self):
        if not self._request_var:
            self._request_var = template.Variable('request')
        return self._request_var

    def package_for(self, package_name, package_type):
        package = {


## ... source file abbreviated to get to mark_safe examples ...


            'command': subprocess.list2cmdline(e.command),
            'errors': e.error_output,
        })


class StylesheetNode(PipelineMixin, template.Node):
    def __init__(self, name):
        self.name = name

    def render(self, context):
        super(StylesheetNode, self).render(context)
        package_name = template.Variable(self.name).resolve(context)

        try:
            package = self.package_for(package_name, 'css')
        except PackageNotFound:
            logger.warn("Package %r is unknown. Check PIPELINE['STYLESHEETS'] in your settings.", package_name)
            return ''  # fail silently, do not return anything if an invalid group is specified
        return self.render_compressed(package, package_name, 'css')

    def render_css(self, package, path):
        template_name = package.template_name or "pipeline/css.html"
        context = package.extra_context
        context.update({
            'type': guess_type(path, 'text/css'),
~~            'url': mark_safe(staticfiles_storage.url(path))
        })
        return render_to_string(template_name, context)

    def render_individual_css(self, package, paths, **kwargs):
        tags = [self.render_css(package, path) for path in paths]
        return '\n'.join(tags)

    def render_error_css(self, package_name, e):
        return super(StylesheetNode, self).render_error(
            'CSS', package_name, e)


class JavascriptNode(PipelineMixin, template.Node):
    def __init__(self, name):
        self.name = name

    def render(self, context):
        super(JavascriptNode, self).render(context)
        package_name = template.Variable(self.name).resolve(context)

        try:
            package = self.package_for(package_name, 'js')
        except PackageNotFound:
            logger.warn("Package %r is unknown. Check PIPELINE['JAVASCRIPT'] in your settings.", package_name)
            return ''  # fail silently, do not return anything if an invalid group is specified
        return self.render_compressed(package, package_name, 'js')

    def render_js(self, package, path):
        template_name = package.template_name or "pipeline/js.html"
        context = package.extra_context
        context.update({
            'type': guess_type(path, 'text/javascript'),
~~            'url': mark_safe(staticfiles_storage.url(path))
        })
        return render_to_string(template_name, context)

    def render_inline(self, package, js):
        context = package.extra_context
        context.update({
            'source': js
        })
        return render_to_string("pipeline/inline_js.html", context)

    def render_individual_js(self, package, paths, templates=None):
        tags = [self.render_js(package, js) for js in paths]
        if templates:
            tags.append(self.render_inline(package, templates))
        return '\n'.join(tags)

    def render_error_js(self, package_name, e):
        return super(JavascriptNode, self).render_error(
            'JavaScript', package_name, e)


@register.tag
def stylesheet(parser, token):
    try:


## ... source file continues with no further mark_safe examples...

```


## Example 15 from django-rest-framework
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

[**django-rest-framework / rest_framework / templatetags / rest_framework.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/templatetags/rest_framework.py)

```python
# rest_framework.py
import re
from collections import OrderedDict

from django import template
from django.template import loader
from django.urls import NoReverseMatch, reverse
from django.utils.encoding import force_str, iri_to_uri
from django.utils.html import escape, format_html, smart_urlquote
~~from django.utils.safestring import SafeData, mark_safe

from rest_framework.compat import apply_markdown, pygments_highlight
from rest_framework.renderers import HTMLFormRenderer
from rest_framework.utils.urls import replace_query_param

register = template.Library()

class_re = re.compile(r'(?<=class=["\'])(.*)(?=["\'])')


@register.tag(name='code')
def highlight_code(parser, token):
    code = token.split_contents()[-1]
    nodelist = parser.parse(('endcode',))
    parser.delete_first_token()
    return CodeNode(code, nodelist)


class CodeNode(template.Node):
    style = 'emacs'

    def __init__(self, lang, code):
        self.lang = lang
        self.nodelist = code


## ... source file abbreviated to get to mark_safe examples ...


        text = self.nodelist.render(context)
        return pygments_highlight(text, self.lang, self.style)


@register.filter()
def with_location(fields, location):
    return [
        field for field in fields
        if field.location == location
    ]


@register.simple_tag
def form_for_link(link):
    import coreschema
    properties = OrderedDict([
        (field.name, field.schema or coreschema.String())
        for field in link.fields
    ])
    required = [
        field.name
        for field in link.fields
        if field.required
    ]
    schema = coreschema.Object(properties=properties, required=required)
~~    return mark_safe(coreschema.render_to_form(schema))


@register.simple_tag
def render_markdown(markdown_text):
    if apply_markdown is None:
        return markdown_text
~~    return mark_safe(apply_markdown(markdown_text))


@register.simple_tag
def get_pagination_html(pager):
    return pager.to_html()


@register.simple_tag
def render_form(serializer, template_pack=None):
    style = {'template_pack': template_pack} if template_pack else {}
    renderer = HTMLFormRenderer()
    return renderer.render(serializer.data, None, {'style': style})


@register.simple_tag
def render_field(field, style):
    renderer = style.get('renderer', HTMLFormRenderer())
    return renderer.render_field(field, style)


@register.simple_tag
def optional_login(request):
    try:
        login_url = reverse('rest_framework:login')
    except NoReverseMatch:
        return ''

    snippet = "<li><a href='{href}?next={next}'>Log in</a></li>"
    snippet = format_html(snippet, href=login_url, next=escape(request.path))

~~    return mark_safe(snippet)


@register.simple_tag
def optional_docs_login(request):
    try:
        login_url = reverse('rest_framework:login')
    except NoReverseMatch:
        return 'log in'

    snippet = "<a href='{href}?next={next}'>log in</a>"
    snippet = format_html(snippet, href=login_url, next=escape(request.path))

~~    return mark_safe(snippet)


@register.simple_tag
def optional_logout(request, user):
    try:
        logout_url = reverse('rest_framework:logout')
    except NoReverseMatch:
        snippet = format_html('<li class="navbar-text">{user}</li>', user=escape(user))
~~        return mark_safe(snippet)

    snippet = """<li class="dropdown">
        <a href="#" class="dropdown-toggle" data-toggle="dropdown">
            {user}
            <b class="caret"></b>
        </a>
        <ul class="dropdown-menu">
            <li><a href='{href}?next={next}'>Log out</a></li>
        </ul>
    </li>"""
    snippet = format_html(snippet, user=escape(user), href=logout_url, next=escape(request.path))

~~    return mark_safe(snippet)


@register.simple_tag
def add_query_param(request, key, val):
    iri = request.get_full_path()
    uri = iri_to_uri(iri)
    return escape(replace_query_param(uri, key, val))


@register.filter
def as_string(value):
    if value is None:
        return ''
    return '%s' % value


@register.filter
def as_list_of_strings(value):
    return [
        '' if (item is None) else ('%s' % item)
        for item in value
    ]


@register.filter
def add_class(value, css_class):
    html = str(value)
    match = class_re.search(html)
    if match:
        m = re.search(r'^%s$|^%s\s|\s%s\s|\s%s$' % (css_class, css_class,
                                                    css_class, css_class),
                      match.group(1))
        if not m:
~~            return mark_safe(class_re.sub(match.group(1) + " " + css_class,
                                          html))
    else:
~~        return mark_safe(html.replace('>', ' class="%s">' % css_class, 1))
    return value


@register.filter
def format_value(value):
    if getattr(value, 'is_hyperlink', False):
        name = str(value.obj)
~~        return mark_safe('<a href=%s>%s</a>' % (value, escape(name)))
    if value is None or isinstance(value, bool):
~~        return mark_safe('<code>%s</code>' % {True: 'true', False: 'false', None: 'null'}[value])
    elif isinstance(value, list):
        if any([isinstance(item, (list, dict)) for item in value]):
            template = loader.get_template('rest_framework/admin/list_value.html')
        else:
            template = loader.get_template('rest_framework/admin/simple_list_value.html')
        context = {'value': value}
        return template.render(context)
    elif isinstance(value, dict):
        template = loader.get_template('rest_framework/admin/dict_value.html')
        context = {'value': value}
        return template.render(context)
    elif isinstance(value, str):
        if (
            (value.startswith('http:') or value.startswith('https:')) and not
            re.search(r'\s', value)
        ):
~~            return mark_safe('<a href="{value}">{value}</a>'.format(value=escape(value)))
        elif '@' in value and not re.search(r'\s', value):
~~            return mark_safe('<a href="mailto:{value}">{value}</a>'.format(value=escape(value)))
        elif '\n' in value:
~~            return mark_safe('<pre>%s</pre>' % escape(value))
    return str(value)


@register.filter
def items(value):
    if value is None:
        return []
    return value.items()


@register.filter
def data(value):
    return value.data


@register.filter
def schema_links(section, sec_key=None):
    NESTED_FORMAT = '%s > %s'  # this format is used in docs/js/api.js:normalizeKeys
    links = section.links
    if section.data:
        data = section.data.items()
        for sub_section_key, sub_section in data:
            new_links = schema_links(sub_section, sec_key=sub_section_key)
            links.update(new_links)


## ... source file abbreviated to get to mark_safe examples ...


            url = None
            nofollow_attr = ' rel="nofollow"' if nofollow else ''
            if simple_url_re.match(middle):
                url = smart_urlquote_wrapper(middle)
            elif simple_url_2_re.match(middle):
                url = smart_urlquote_wrapper('http://%s' % middle)
            elif ':' not in middle and simple_email_re.match(middle):
                local, domain = middle.rsplit('@', 1)
                try:
                    domain = domain.encode('idna').decode('ascii')
                except UnicodeError:
                    continue
                url = 'mailto:%s@%s' % (local, domain)
                nofollow_attr = ''

            if url:
                trimmed = trim_url(middle)
                lead, trail = conditional_escape(lead), conditional_escape(trail)
                url, trimmed = conditional_escape(url), conditional_escape(trimmed)
                middle = '<a href="%s"%s>%s</a>' % (url, nofollow_attr, trimmed)
                words[i] = '%s%s%s' % (lead, middle, trail)
            else:
                words[i] = conditional_escape(word)
        else:
            words[i] = conditional_escape(word)
~~    return mark_safe(''.join(words))


@register.filter
def break_long_headers(header):
    if len(header) > 160 and ',' in header:
~~        header = mark_safe('<br> ' + ', <br>'.join(header.split(',')))
    return header



## ... source file continues with no further mark_safe examples...

```


## Example 16 from django-sitetree
[django-sitetree](https://github.com/idlesign/django-sitetree)
([project documentation](https://django-sitetree.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-sitetree/))
is a [Django](/django.html) extension that makes it easier for
developers to add site trees, menus and breadcrumb navigation elements
to their web applications.

The django-sitetree project is provided as open source under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/idlesign/django-sitetree/blob/master/LICENSE).

[**django-sitetree / sitetree / fields.py**](https://github.com/idlesign/django-sitetree/blob/master/sitetree/./fields.py)

```python
# fields.py
from typing import Optional

from django import template
from django.template.base import Parser, Token
from django.forms import ChoiceField
~~from django.utils.safestring import mark_safe

from .compat import TOKEN_BLOCK
from .templatetags.sitetree import sitetree_tree
from .utils import get_tree_model, get_tree_item_model
from .settings import ITEMS_FIELD_ROOT_ID

if False:  # pragma: nocover
    from .models import TreeItemBase, TreeBase  # noqa


MODEL_TREE_CLASS = get_tree_model()
MODEL_TREE_ITEM_CLASS = get_tree_item_model()


class TreeItemChoiceField(ChoiceField):
    template: str = 'admin/sitetree/tree/tree_combo.html'
    root_title: str = '---------'

    def __init__(
            self,
            tree: 'TreeBase' = None,
            required: bool = True,
            widget=None,
            label=None,


## ... source file abbreviated to get to mark_safe examples ...


        if not tree:
            return

        if isinstance(tree, MODEL_TREE_CLASS):
            tree = tree.alias

        self.tree = tree
        self.choices = self._build_choices()

    def _build_choices(self):
        tree_token = f'sitetree_tree from "{self.tree}" template "{self.template}"'

        context_kwargs = {'current_app': 'admin'}
        context = template.Context(context_kwargs)
        context.update({'request': object()})

        choices_str = sitetree_tree(
            Parser(None), Token(token_type=TOKEN_BLOCK, contents=tree_token)
        ).render(context)

        tree_choices = [(ITEMS_FIELD_ROOT_ID, self.root_title)]

        for line in choices_str.splitlines():
            if line.strip():
                splitted = line.split(':::')
~~                tree_choices.append((splitted[0], mark_safe(splitted[1])))

        return tree_choices

    def clean(self, value):
        if not value:
            return None

        try:
            return MODEL_TREE_ITEM_CLASS.objects.get(pk=value)

        except MODEL_TREE_ITEM_CLASS.DoesNotExist:
            return None



## ... source file continues with no further mark_safe examples...

```


## Example 17 from django-tables2
[django-tables2](https://github.com/jieter/django-tables2)
([projection documentation](https://django-tables2.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-tables2/))
is a code library for [Django](/django.html) that simplifies creating and
displaying tables in [Django templates](/django-templates.html),
especially with more advanced features such as pagination and sorting.
The project and its code are
[available as open source](https://github.com/jieter/django-tables2/blob/master/LICENSE).

[**django-tables2 / django_tables2 / columns / checkboxcolumn.py**](https://github.com/jieter/django-tables2/blob/master/django_tables2/columns/checkboxcolumn.py)

```python
# checkboxcolumn.py
~~from django.utils.safestring import mark_safe

from django_tables2.utils import Accessor, AttributeDict

from .base import Column, library


@library.register
class CheckBoxColumn(Column):

    def __init__(self, attrs=None, checked=None, **extra):
        self.checked = checked
        kwargs = {"orderable": False, "attrs": attrs}
        kwargs.update(extra)
        super().__init__(**kwargs)

    @property
    def header(self):
        default = {"type": "checkbox"}
        general = self.attrs.get("input")
        specific = self.attrs.get("th__input")
        attrs = AttributeDict(default, **(specific or general or {}))
~~        return mark_safe("<input %s/>" % attrs.as_html())

    def render(self, value, bound_column, record):
        default = {"type": "checkbox", "name": bound_column.name, "value": value}
        if self.is_checked(value, record):
            default.update({"checked": "checked"})

        general = self.attrs.get("input")
        specific = self.attrs.get("td__input")
        attrs = AttributeDict(default, **(specific or general or {}))
~~        return mark_safe("<input %s/>" % attrs.as_html())

    def is_checked(self, value, record):
        if self.checked is None:
            return False
        if self.checked is True:
            return True

        if callable(self.checked):
            return bool(self.checked(value, record))

        checked = Accessor(self.checked)
        if checked in record:
            return bool(record[checked])
        return False



## ... source file continues with no further mark_safe examples...

```


## Example 18 from django-wiki
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

[**django-wiki / src/wiki / forms.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/./forms.py)

```python
# forms.py
    "WikiSlugField",
    "SpamProtectionMixin",
    "CreateRootForm",
    "MoveForm",
    "EditForm",
    "SelectWidgetBootstrap",
    "TextInputPrepend",
    "CreateForm",
    "DeleteForm",
    "PermissionsForm",
    "DirFilterForm",
    "SearchForm",
]

from datetime import timedelta

from django import forms
from django.apps import apps
from django.contrib.auth import get_user_model
from django.core import validators
from django.core.validators import RegexValidator
from django.forms.widgets import HiddenInput
from django.shortcuts import get_object_or_404
from django.urls import Resolver404, resolve
from django.utils import timezone
~~from django.utils.safestring import mark_safe
from django.utils.translation import gettext, gettext_lazy as _, pgettext_lazy
from wiki import models
from wiki.conf import settings
from wiki.core import permissions
from wiki.core.diff import simple_merge
from wiki.core.plugins.base import PluginSettingsFormMixin
from wiki.editors import getEditor

from .forms_account_handling import UserCreationForm, UserUpdateForm

validate_slug_numbers = RegexValidator(
    r"^[0-9]+$",
    _("A 'slug' cannot consist solely of numbers."),
    "invalid",
    inverse_match=True,
)


class WikiSlugField(forms.CharField):

    default_validators = [validators.validate_slug, validate_slug_numbers]

    def __init__(self, *args, **kwargs):
        self.allow_unicode = kwargs.pop("allow_unicode", False)


## ... source file abbreviated to get to mark_safe examples ...


        self.check_spam()
        return self.cleaned_data


class SelectWidgetBootstrap(forms.Select):

    def __init__(self, attrs=None, choices=()):
        if attrs is None:
            attrs = {"class": ""}
        elif "class" not in attrs:
            attrs["class"] = ""
        attrs["class"] += " form-control"

        super().__init__(attrs, choices)


class TextInputPrepend(forms.TextInput):
    template_name = "wiki/forms/text.html"

    def __init__(self, *args, **kwargs):
        self.prepend = kwargs.pop("prepend", "")
        super().__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
~~        context["prepend"] = mark_safe(self.prepend)
        return context


class CreateForm(forms.Form, SpamProtectionMixin):
    def __init__(self, request, urlpath_parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.urlpath_parent = urlpath_parent

    title = forms.CharField(label=_("Title"),)
    slug = WikiSlugField(
        label=_("Slug"),
        help_text=_(
            "This will be the address where your article can be found. Use only alphanumeric characters and - or _.<br>Note: If you change the slug later on, links pointing to this article are <b>not</b> updated."
        ),
        max_length=models.URLPath.SLUG_MAX_LENGTH,
    )
    content = forms.CharField(
        label=_("Contents"), required=False, widget=getEditor().get_widget()
    )  # @UndefinedVariable

    summary = forms.CharField(
        label=pgettext_lazy("Revision comment", "Summary"),
        help_text=_("Write a brief message for the article's history log."),


## ... source file continues with no further mark_safe examples...

```


## Example 19 from elasticsearch-django
[elasticsearch-django](https://github.com/yunojuno/elasticsearch-django)
([PyPI package information](https://pypi.org/project/elasticsearch-django/))
is a [Django](/django.html) app for managing
[ElasticSearch](https://github.com/elastic/elasticsearch) indexes
populated by [Django ORM](/django-orm.html) models. The project is
available as open source under the
[MIT license](https://github.com/yunojuno/elasticsearch-django/blob/master/LICENSE).

[**elasticsearch-django / elasticsearch_django / admin.py**](https://github.com/yunojuno/elasticsearch-django/blob/master/elasticsearch_django/./admin.py)

```python
# admin.py
import logging

import simplejson as json  # simplejson supports Decimal serialization
from django.contrib import admin
from django.template.defaultfilters import truncatechars, truncatewords
~~from django.utils.safestring import mark_safe

from .models import SearchQuery

logger = logging.getLogger(__name__)


def pprint(data: dict) -> str:
    pretty = json.dumps(data, sort_keys=True, indent=4, separators=(",", ": "))
    html = pretty.replace(" ", "&nbsp;").replace("\n", "<br>")
~~    return mark_safe("<code>%s</code>" % html)


class SearchQueryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "search_terms_",
        "total_hits",
        "returned_",
        "min_",
        "max_",
        "reference",
        "executed_at",
    )
    list_filter = ("index", "query_type")
    search_fields = ("search_terms", "user__first_name", "user__last_name", "reference")
    exclude = ("hits", "query", "page")
    readonly_fields = (
        "user",
        "index",
        "search_terms",
        "query_type",
        "total_hits",


## ... source file continues with no further mark_safe examples...

```


## Example 20 from register
[register](https://github.com/ORGAN-IZE/register) is a [Django](/django.html),
[Bootstrap](/bootstrap-css.html), [PostgreSQL](/postgresql.html) project that is
open source under the
[GNU General Public License v3.0](https://github.com/ORGAN-IZE/register/blob/master/LICENSE).
This web application makes it easier for people to register as organ donors.
You can see the application live at
[https://register.organize.org/](https://register.organize.org/).

[**register / registration / forms.py**](https://github.com/ORGAN-IZE/register/blob/master/registration/./forms.py)

```python
# forms.py
from __future__ import unicode_literals

import logging
import re
import collections
import datetime

import django.forms
import django.forms.utils
import django.forms.widgets
import django.core.validators
import django.core.exceptions
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
~~from django.utils.safestring import mark_safe

import form_utils.forms
import requests
import dateutil.parser
import validate_email

logger = logging.getLogger(__name__)


REGISTRATION_CONFIGURATION_NAME = 'registration_configuration'

RE_NON_DECIMAL = re.compile(r'[^\d]+')
RE_NON_ALPHA = re.compile('[\W]+')
RE_POSTAL_CODE = re.compile(r'^[0-9]{5}$')
validate_postal_code = django.core.validators.RegexValidator(
    RE_POSTAL_CODE, _("Enter a valid postal code consisting 5 numbers."), 'invalid')


CHOICES_GENDER = (
    ('M', _('Male')),
    ('F', _('Female')),
)




## ... source file abbreviated to get to mark_safe examples ...



            d = {
                'label': label,
            }

            if field_type == 'string':
                d['required'] = is_required
                d['initial'] = initial
                if choices and is_editable:
                    d['help_text'] = help_text
                    d['choices'] = choices
                    d['widget'] = django.forms.RadioSelect
                    field_class = django.forms.ChoiceField
                elif field_name == 'email':
                    d['max_length'] = max_length
                    d['help_text'] = help_text
                    field_class = django.forms.EmailField
                elif field_name == 'license_id' \
                        and 'license_id_formats' in conf:
                    d['max_length'] = max_length
                    license_id_formats = '{}{}{}'.format(
                            _('<p class=\'hint-license-id-format\'>Valid state License IDs should look like: '),
                            ', '.join(map(unicode, conf['license_id_formats'])), '</p>')
                    help_text = '{}{}{}'.format('<p> ', unicode(help_text), '</p>')
                    license_id_formats = '{}{}'.format(license_id_formats, help_text)
~~                    d['help_text'] = mark_safe(license_id_formats)
                    field_class = django.forms.CharField
                else:
                    d['max_length'] = max_length
                    d['help_text'] = help_text
                    field_class = django.forms.CharField
            elif field_type == 'date':
                d['required'] = is_required
                d['initial'] = initial
                d['help_text'] = help_text
                if min_value:
                    d['validators'] = [validate_date_generator(min_value), ]
                field_class = django.forms.DateField
            elif field_type == 'boolean':
                has_booleans = True
                d['initial'] = initial
                if field_name == 'agree_to_tos':
~~                    d['help_text'] = mark_safe(help_text)
~~                    d['label'] = mark_safe(label)
                else:
                    d['required'] = False
                    d['help_text'] = help_text
                field_class = django.forms.BooleanField
            else:
                raise Exception('Unknown field type: {}'.format(field_type))

            fields[field_name] = field_class(**d)
            fieldset[1]['fields'].append(field_name)

            widget = fields[field_name].widget
            if not is_editable:
                if isinstance(widget, django.forms.Select):
                    widget.attrs['disabled'] = 'disabled'
                else:
                    widget.attrs['readonly'] = 'readonly'
            if field_type == 'date':
                widget.attrs['placeholder'] = '__/__/____'
                widget.attrs['class'] = 'date'
            if field_name == 'phone_number':
                widget.attrs['placeholder'] = '(___) ___-____'
                widget.attrs['class'] = 'phonenumber'
            if field_name == 'ssn':
                widget.attrs['placeholder'] = '____'


## ... source file continues with no further mark_safe examples...

```


## Example 21 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / snippets / edit_handlers.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/snippets/edit_handlers.py)

```python
# edit_handlers.py
from django.template.loader import render_to_string
~~from django.utils.safestring import mark_safe

from wagtail.admin.edit_handlers import BaseChooserPanel

from .widgets import AdminSnippetChooser


class SnippetChooserPanel(BaseChooserPanel):
    object_type_name = 'item'

    def widget_overrides(self):
        return {self.field_name: AdminSnippetChooser(model=self.target_model)}

    def render_as_field(self):
        instance_obj = self.get_chosen_item()
~~        return mark_safe(render_to_string(self.field_template, {
            'field': self.bound_field,
            self.object_type_name: instance_obj,
        }))

    def on_model_bound(self):
        super().on_model_bound()
        self.target_model = self.db_field.remote_field.model



## ... source file continues with no further mark_safe examples...

```

