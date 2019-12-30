title: django.utils.html format_html Example Code
category: page
slug: django-utils-html-format-html-examples
sortorder: 500013705
toc: False
sidebartitle: django.utils.html format_html
meta: Python code examples for using the format_html function contained within Django's django.utils.html module.


[format_html](https://github.com/django/django/blob/master/django/utils/html.py)
is a function within the [Django](/django.html) project that is like
`str.format` but for [HTML](/hypertext-markup-language-html.html) content.
The function allows a program to safely create small HTML fragments to
render, most likely in an output webpaage.

Understanding these concepts are useful when coding with projects 
that use Django's `format_html` function:

* [Django](/django.html) and [Django templates](/django-templates.html) 
* [Web development](/web-development.html), 
  [web frameworks](/web-frameworks.html) and
  [HTML](/hypertext-markup-language-html.html)
* [Angular](/angular.html) and [JavaScript](/javascript.html)

You can also view the [complete all topics page](/table-of-contents.html)
for even more resources.


## Example 1 from django-angular
[django-angular](https://github.com/jrief/django-angular) 
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use 
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is 
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / templatetags / djng_tags.py**](https://github.com/jrief/django-angular/blob/master/djng/templatetags/djng_tags.py)

```python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json

from django.template import Library
from django.template.base import Node, NodeList, TextNode, VariableNode
~~from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import get_language_from_request

from djng.core.urlresolvers import (get_all_remote_methods, 
                                    get_current_remote_methods)


register = Library()


@register.simple_tag(name='djng_all_rmi')
def djng_all_rmi():
    """
    Returns a dictionary of all methods for all Views available for 
    this project, marked with the ``@allow_remote_invocation`` 
    decorator. The return string can be used directly to initialize
    the AngularJS provider, such as 
    ``djangoRMIProvider.configure({­% djng_rmi_configs %­});``
    """
    return mark_safe(json.dumps(get_all_remote_methods()))


@register.simple_tag(name='djng_current_rmi', takes_context=True)
def djng_current_rmi(context):
    """
    Returns a dictionary of all methods for the current View of 
    this request, marked with the @allow_remote_invocation decorator. 
    The return string can be used directly to initialize the 
    AngularJS provider, such as 
    ``djangoRMIProvider.configure({­% djng_current_rmi %­});``
    """
    return mark_safe(json.dumps(get_current_remote_methods(context.get('view'))))


@register.simple_tag(name='load_djng_urls', takes_context=True)
def djng_urls(context, *namespaces):
    raise DeprecationWarning(
        "load_djng_urls templatetag is deprecated and has " + \
        "been removed from this version of django-angular."
        "Please refer to documentation for updated way to " + \
        "manage django urls in angular.")


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
    """
    Conditionally switch between AngularJS and Django variable 
    expansion for ``{{`` and ``}}`` keeping Django's expansion 
    for ``{%`` and ``%}``
    Usage::
        {% angularjs 1 %} or simply {% angularjs %}
            {% process variables through the AngularJS template engine %}
        {% endangularjs %}
        {% angularjs 0 %}
            {% process variables through the Django template engine %}
        {% endangularjs %}
        Instead of 0 and 1, it is possible to use a context variable.
    """
    bits = token.contents.split()
    if len(bits) < 2:
        bits.append('1')
    values = [parser.compile_filter(bit) for bit in bits[1:]]
    django_nodelist = parser.parse(('endangularjs',))
    angular_nodelist = NodeList()
    for node in django_nodelist:
        # convert all occurrences of VariableNode into a TextNode using the
        # AngularJS double curly bracket notation
        if isinstance(node, VariableNode):
            # convert Django's array notation into JS array notation
            tokens = node.filter_expression.token.split('.')
            token = tokens[0]
            for part in tokens[1:]:
                if part.isdigit():
                    token += '[%s]' % part
                else:
                    token += '.%s' % part
            node = TextNode('{{ %s }}' % token)
        angular_nodelist.append(node)
    parser.delete_first_token()
    return AngularJsNode(django_nodelist, angular_nodelist, values[0])


@register.simple_tag(name='djng_locale_script', takes_context=True)
def djng_locale_script(context, default_language='en'):
    """
    Returns a script tag for including the proper locale 
    script in any HTML page. This tag determines the current 
    language with its locale.
    Usage:
        <script src="{% static 'node_modules/angular-i18n/' %}
        {% djng_locale_script %}"></script>
    or, if used with a default language:
        <script src="{% static 'node_modules/angular-i18n/' %}
        {% djng_locale_script 'de' %}"></script>
    """
    language = get_language_from_request(context['request'])
    if not language:
        language = default_language
~~    return format_html('angular-locale_{}.js', language.lower())
```


## Example 2 from AuditLog
[Auditlog](https://github.com/jjkester/django-auditlog) 
([project documentation](https://django-auditlog.readthedocs.io/en/latest/))
is a [Django](/django.html) app that logs changes to Python objects,
similar to the Django admin's logs but with more details and
output formats. Auditlog's source code is provided as open source under the
[MIT license](https://github.com/jjkester/django-auditlog/blob/master/LICENSE).

[**django-auditlog / src / auditlog / mixins.py**](https://github.com/jjkester/django-auditlog/blob/master/src/auditlog/mixins.py)

```python
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
~~from django.utils.html import format_html
from django.utils.safestring import mark_safe

MAX = 75


class LogEntryAdminMixin(object):

    def created(self, obj):
        return obj.timestamp.strftime('%Y-%m-%d %H:%M:%S')
    created.short_description = 'Created'

    def user_url(self, obj):
        if obj.actor:
            app_label, model = settings.AUTH_USER_MODEL.split('.')
            viewname = 'admin:%s_%s_change' % (app_label, 
                                               model.lower())
            try:
                link = urlresolvers.reverse(viewname, 
                                            args=[obj.actor.id])
            except NoReverseMatch:
                return u'%s' % (obj.actor)
~~            return format_html(u'<a href="{}">{}</a>', 
~~                               link, obj.actor)

        return 'system'
    user_url.short_description = 'User'

    def resource_url(self, obj):
        app_label, model = obj.content_type.app_label, 
                           obj.content_type.model
        viewname = 'admin:%s_%s_change' % (app_label, model)
        try:
            args = [obj.object_pk] if obj.object_id is \
                   None else [obj.object_id]
            link = urlresolvers.reverse(viewname, args=args)
        except NoReverseMatch:
            return obj.object_repr
        else:
~~            return format_html(u'<a href="{}">{}</a>', 
~~                               link, obj.object_repr)
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
        msg = '<table><tr><th>#</th><th>Field</th>' + \
              '<th>From</th><th>To</th></tr>'
        for i, field in enumerate(sorted(changes), 1):
            value = [i, field] + (['***', '***'] if field == \
                    'password' else changes[field])
~~            msg += format_html('<tr><td>{}</td><td>{}</td><td>' + \
~~                               '{}</td><td>{}</td></tr>', *value)

        msg += '</table>'
        return mark_safe(msg)
    msg.short_description = 'Changes'
```
