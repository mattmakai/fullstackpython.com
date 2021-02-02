title: django.template.loader_tags ExtendsNode Example Code
category: page
slug: django-template-loader-tags-extendsnode-examples
sortorder: 500011396
toc: False
sidebartitle: django.template.loader_tags ExtendsNode
meta: Example code for understanding how to use the ExtendsNode class from the django.template.loader_tags module of the Django project.


`ExtendsNode` is a class within the `django.template.loader_tags` module of the Django project.

<a href="/django-template-loader-tags-blocknode-examples.html">BlockNode</a>
and
<a href="/django-template-loader-tags-includenode-examples.html">IncludeNode</a>
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


## ... source file abbreviated to get to ExtendsNode examples ...


            placeholders.append(placeholder)
            clean_placeholders.append(slot)
    return placeholders


def get_static_placeholders(template, context):
    compiled_template = get_template(template)
    nodes = _scan_static_placeholders(_get_nodelist(compiled_template))
    placeholders = [node.get_declaration(context) for node in nodes]
    placeholders_with_code = []

    for placeholder in placeholders:
        if placeholder.slot:
            placeholders_with_code.append(placeholder)
        else:
            warnings.warn('Unable to resolve static placeholder '
                          'name in template "{}"'.format(template),
                          Warning)
    return placeholders_with_code


def _get_block_nodes(extend_node):
    parent = extend_node.get_parent(get_context())
    parent_nodelist = _get_nodelist(parent)
    parent_nodes = parent_nodelist.get_nodes_by_type(BlockNode)
~~    parent_extend_nodes = parent_nodelist.get_nodes_by_type(ExtendsNode)

    if parent_extend_nodes:
        nodes = _get_block_nodes(parent_extend_nodes[0])
    else:
        nodes = OrderedDict()

    for node in parent_nodes:
        nodes[node.name] = node

    current_nodes = _get_nodelist(extend_node).get_nodes_by_type(BlockNode)

    for node in current_nodes:
        if node.name in nodes:
            node.super = nodes[node.name]
        nodes[node.name] = node
    return nodes


def _get_placeholder_nodes_from_extend(extend_node, node_class):
    block_nodes = _get_block_nodes(extend_node)
    block_names = list(block_nodes.keys())

    placeholders = []

    for block in block_nodes.values():
        placeholders.extend(_scan_placeholders(_get_nodelist(block), node_class, block, block_names))

    parent_template = _find_topmost_template(extend_node)
    placeholders += _scan_placeholders(_get_nodelist(parent_template), node_class, None, block_names)
    return placeholders


def _find_topmost_template(extend_node):
    parent_template = extend_node.get_parent(get_context())
~~    for node in _get_nodelist(parent_template).get_nodes_by_type(ExtendsNode):
        return _find_topmost_template(node)
    return extend_node.get_parent(get_context())


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
        elif isinstance(node, IncludeNode):
            if node.template:
                if not callable(getattr(node.template, 'render', None)):
                    if isinstance(node.template.var, Variable):
                        continue
                    else:
                        template = get_template(node.template.var)
                else:
                    template = node.template
                nodes += _scan_placeholders(_get_nodelist(template), node_class, current_block)
~~        elif isinstance(node, ExtendsNode):
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
                            current_block = node
                        nodes += _scan_placeholders(subnodelist, node_class, current_block, ignore_blocks)
        else:
            for attr in dir(node):
                obj = getattr(node, attr)
                if isinstance(obj, NodeList):
                    if isinstance(node, BlockNode):
                        current_block = node
                    nodes += _scan_placeholders(obj, node_class, current_block, ignore_blocks)
    return nodes


## ... source file continues with no further ExtendsNode examples...

```

