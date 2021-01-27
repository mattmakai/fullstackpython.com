title: django.template.base Node Example Code
category: page
slug: django-template-base-node-examples
sortorder: 500011371
toc: False
sidebartitle: django.template.base Node
meta: Example code for understanding how to use the Node class from the django.template.base module of the Django project.


`Node` is a class within the `django.template.base` module of the Django project.

<a href="/django-template-base-context-examples.html">Context</a>,
<a href="/django-template-base-filterexpression-examples.html">FilterExpression</a>,
<a href="/django-template-base-nodelist-examples.html">NodeList</a>,
<a href="/django-template-base-parser-examples.html">Parser</a>,
<a href="/django-template-base-template-examples.html">Template</a>,
<a href="/django-template-base-templatesyntaxerror-examples.html">TemplateSyntaxError</a>,
<a href="/django-template-base-textnode-examples.html">TextNode</a>,
<a href="/django-template-base-token-examples.html">Token</a>,
<a href="/django-template-base-tokentype-examples.html">TokenType</a>,
<a href="/django-template-base-variabledoesnotexist-examples.html">VariableDoesNotExist</a>,
<a href="/django-template-base-variablenode-examples.html">VariableNode</a>,
and <a href="/django-template-base-token-kwargs-examples.html">token_kwargs</a>
are several other callables with code examples from the same `django.template.base` package.

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


~~class AngularJsNode(Node):
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
        if isinstance(node, VariableNode):
            tokens = node.filter_expression.token.split('.')
            token = tokens[0]
            for part in tokens[1:]:


## ... source file continues with no further Node examples...

```

