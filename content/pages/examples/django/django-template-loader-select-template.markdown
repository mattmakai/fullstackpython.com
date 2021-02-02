title: django.template.loader select_template Example Code
category: page
slug: django-template-loader-select-template-examples
sortorder: 500011394
toc: False
sidebartitle: django.template.loader select_template
meta: Python example code that shows how to use the select_template callable from the django.template.loader module of the Django project.


`select_template` is a callable within the `django.template.loader` module of the Django project.

<a href="/django-template-loader-get-template-examples.html">get_template</a>
and
<a href="/django-template-loader-render-to-string-examples.html">render_to_string</a>
are a couple of other callables within the `django.template.loader` package that also have code examples.

## Example 1 from django-tables2
[django-tables2](https://github.com/jieter/django-tables2)
([projection documentation](https://django-tables2.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-tables2/))
is a code library for [Django](/django.html) that simplifies creating and
displaying tables in [Django templates](/django-templates.html),
especially with more advanced features such as pagination and sorting.
The project and its code are
[available as open source](https://github.com/jieter/django-tables2/blob/master/LICENSE).

[**django-tables2 / django_tables2 / templatetags / django_tables2.py**](https://github.com/jieter/django-tables2/blob/master/django_tables2/templatetags/django_tables2.py)

```python
# django_tables2.py
import re
from collections import OrderedDict

from django import template
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.template import Node, TemplateSyntaxError
~~from django.template.loader import get_template, select_template
from django.templatetags.l10n import register as l10n_register
from django.utils.html import escape
from django.utils.http import urlencode

import django_tables2 as tables
from django_tables2.paginators import LazyPaginator
from django_tables2.utils import AttributeDict

register = template.Library()
kwarg_re = re.compile(r"(?:(.+)=)?(.+)")
context_processor_error_msg = (
    "Tag {%% %s %%} requires django.template.context_processors.request to be "
    "in the template configuration in "
    "settings.TEMPLATES[]OPTIONS.context_processors) in order for the included "
    "template tags to function correctly."
)


def token_kwargs(bits, parser):
    if not bits:
        return {}
    kwargs = OrderedDict()
    while bits:
        match = kwarg_re.match(bits[0])


## ... source file abbreviated to get to select_template examples ...


        self.template_name = template_name

    def render(self, context):
        table = self.table.resolve(context)

        request = context.get("request")

        if isinstance(table, tables.Table):
            pass
        elif hasattr(table, "model"):
            queryset = table

            table = tables.table_factory(model=queryset.model)(queryset, request=request)
        else:
            klass = type(table).__name__
            raise ValueError("Expected table or queryset, not {}".format(klass))

        if self.template_name:
            template_name = self.template_name.resolve(context)
        else:
            template_name = table.template_name

        if isinstance(template_name, str):
            template = get_template(template_name)
        else:
~~            template = select_template(template_name)

        try:
            table.context = context
            table.before_render(request)

            return template.render(context={"table": table}, request=request)
        finally:
            del table.context


@register.tag
def render_table(parser, token):
    bits = token.split_contents()
    bits.pop(0)

    table = parser.compile_filter(bits.pop(0))
    template = parser.compile_filter(bits.pop(0)) if bits else None

    return RenderTableNode(table, template)


register.filter("localize", l10n_register.filters["localize"])
register.filter("unlocalize", l10n_register.filters["unlocalize"])



## ... source file continues with no further select_template examples...

```

