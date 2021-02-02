title: django.template.loader_tags IncludeNode Example Code
category: page
slug: django-template-loader-tags-includenode-examples
sortorder: 500011397
toc: False
sidebartitle: django.template.loader_tags IncludeNode
meta: Example code for understanding how to use the IncludeNode class from the django.template.loader_tags module of the Django project.


`IncludeNode` is a class within the `django.template.loader_tags` module of the Django project.

<a href="/django-template-loader-tags-blocknode-examples.html">BlockNode</a>
and
<a href="/django-template-loader-tags-extendsnode-examples.html">ExtendsNode</a>
are a couple of other callables within the `django.template.loader_tags` package that also have code examples.

## Example 1 from django-cms
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
from django.template.base import VariableNode
from django.template.loader import get_template
~~from django.template.loader_tags import BlockNode, ExtendsNode, IncludeNode

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
        return {}


def get_placeholder_conf(setting, placeholder, template=None, default=None):


## ... source file abbreviated to get to IncludeNode examples ...




def restore_sekizai_context(context, changes):
    varname = get_varname()
    sekizai_container = context.get(varname)
    for key, values in changes.items():
        sekizai_namespace = sekizai_container[key]
        for value in values:
            sekizai_namespace.append(value)


def _scan_placeholders(nodelist, node_class=None, current_block=None, ignore_blocks=None):
    from cms.templatetags.cms_tags import Placeholder

    if not node_class:
        node_class = Placeholder

    nodes = []

    if ignore_blocks is None:
        ignore_blocks = []

    for node in nodelist:
        if isinstance(node, node_class):
            nodes.append(node)
~~        elif isinstance(node, IncludeNode):
            if node.template:
                if not callable(getattr(node.template, 'render', None)):
                    if isinstance(node.template.var, Variable):
                        continue
                    else:
                        template = get_template(node.template.var)
                else:
                    template = node.template
                nodes += _scan_placeholders(_get_nodelist(template), node_class, current_block)
        elif isinstance(node, ExtendsNode):
            nodes += _get_placeholder_nodes_from_extend(node, node_class)
        elif isinstance(node, VariableNode) and current_block:
            if node.filter_expression.token == 'block.super':
                if not hasattr(current_block.super, 'nodelist'):
                    raise TemplateSyntaxError("Cannot render block.super for blocks without a parent.")
                nodes += _scan_placeholders(_get_nodelist(current_block.super), node_class, current_block.super)
        elif isinstance(node, BlockNode) and node.name in ignore_blocks:
            continue
        elif hasattr(node, 'child_nodelists'):
            for nodelist_name in node.child_nodelists:
                if hasattr(node, nodelist_name):
                    subnodelist = getattr(node, nodelist_name)
                    if isinstance(subnodelist, NodeList):
                        if isinstance(node, BlockNode):


## ... source file continues with no further IncludeNode examples...

```

