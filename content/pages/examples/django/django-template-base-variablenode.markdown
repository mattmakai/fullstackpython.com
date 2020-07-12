title: django.template.base VariableNode Example Code
category: page
slug: django-template-base-variablenode-examples
sortorder: 500011374
toc: False
sidebartitle: django.template.base VariableNode
meta: Python example code for the VariableNode class from the django.template.base module of the Django project.


VariableNode is a class within the django.template.base module of the Django project.


## Example 1 from django-angular
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
~~from django.template.base import Node, NodeList, TextNode, VariableNode
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import get_language_from_request

from djng.core.urlresolvers import get_all_remote_methods, get_current_remote_methods


register = Library()


@register.simple_tag(name='djng_all_rmi')
def djng_all_rmi():
    return mark_safe(json.dumps(get_all_remote_methods()))


@register.simple_tag(name='djng_current_rmi', takes_context=True)
def djng_current_rmi(context):
    return mark_safe(json.dumps(get_current_remote_methods(context.get('view'))))


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
    if len(bits) < 2:
        bits.append('1')
    values = [parser.compile_filter(bit) for bit in bits[1:]]
    django_nodelist = parser.parse(('endangularjs',))
    angular_nodelist = NodeList()
    for node in django_nodelist:
~~        if isinstance(node, VariableNode):
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
    language = get_language_from_request(context['request'])
    if not language:
        language = default_language
    return format_html('angular-locale_{}.js', language.lower())



## ... source file continues with no further VariableNode examples...

```


## Example 2 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / utils / placeholder.py**](https://github.com/divio/django-cms/blob/develop/cms/utils/placeholder.py)

```python
# placeholder.py
import operator
import warnings
from collections import OrderedDict

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db.models.query_utils import Q
from django.template import TemplateSyntaxError, NodeList, Variable, Context, Template, engines
~~from django.template.base import VariableNode
from django.template.loader import get_template
from django.template.loader_tags import BlockNode, ExtendsNode, IncludeNode

from six import string_types

from sekizai.helpers import get_varname

from cms.exceptions import DuplicatePlaceholderWarning
from cms.utils.conf import get_cms_setting


def _get_nodelist(tpl):
    if hasattr(tpl, 'template'):
        return tpl.template.nodelist
    else:
        return tpl.nodelist


def get_context():
    if engines is not None:
        context = Context()
        context.template = Template('')
        return context
    else:


## ... source file continues with no further VariableNode examples...

```

