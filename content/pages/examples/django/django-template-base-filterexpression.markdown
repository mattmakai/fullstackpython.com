title: django.template.base FilterExpression Example Code
category: page
slug: django-template-base-filterexpression-examples
sortorder: 500011364
toc: False
sidebartitle: django.template.base FilterExpression
meta: Python example code for the FilterExpression class from the django.template.base module of the Django project.


FilterExpression is a class within the django.template.base module of the Django project.


## Example 1 from django-sitetree
[django-sitetree](https://github.com/idlesign/django-sitetree)
([project documentation](https://django-sitetree.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-sitetree/))
is a [Django](/django.html) extension that makes it easier for
developers to add site trees, menus and breadcrumb navigation elements
to their web applications.

The django-sitetree project is provided as open source under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/idlesign/django-sitetree/blob/master/LICENSE).

[**django-sitetree / sitetree / templatetags / sitetree.py**](https://github.com/idlesign/django-sitetree/blob/master/sitetree/templatetags/sitetree.py)

```python
# sitetree.py
from django import template
~~from django.template.base import FilterExpression
from django.template.loader import get_template

from ..sitetreeapp import get_sitetree

register = template.Library()


@register.tag
def sitetree_tree(parser, token):
    tokens = token.split_contents()
    use_template = detect_clause(parser, 'template', tokens)
    tokens_num = len(tokens)

    if tokens_num in (3, 5):
        tree_alias = parser.compile_filter(tokens[2])
        return sitetree_treeNode(tree_alias, use_template)
    else:
        raise template.TemplateSyntaxError(
            '%r tag requires two arguments. E.g. {%% sitetree_tree from "mytree" %%}.' % tokens[0])


@register.tag
def sitetree_children(parser, token):
    tokens = token.split_contents()


## ... source file abbreviated to get to FilterExpression examples ...



    def get_value(self, context):
        return get_sitetree().get_current_page_attr('description', self.item, context)


class sitetree_page_hintNode(SimpleNode):

    def get_value(self, context):
        return get_sitetree().get_current_page_attr('hint', self.item, context)
    

def detect_clause(parser, clause_name, tokens):
    if clause_name in tokens:
        t_index = tokens.index(clause_name)
        clause_value = parser.compile_filter(tokens[t_index + 1])
        del tokens[t_index:t_index + 2]
    else:
        clause_value = None
    return clause_value


def render(context, tree_items, use_template):
    context.push()
    context['sitetree_items'] = tree_items

~~    if isinstance(use_template, FilterExpression):
        use_template = use_template.resolve(context)

    content = get_template(use_template).render(context.flatten())
    context.pop()

    return content



## ... source file continues with no further FilterExpression examples...

```

