title: django.utils.html strip_tags Example Code
category: page
slug: django-utils-html-strip-tags-examples
sortorder: 500011468
toc: False
sidebartitle: django.utils.html strip_tags
meta: Python example code for the strip_tags callable from the django.utils.html module of the Django project.


strip_tags is a callable within the django.utils.html module of the Django project.


## Example 1 from django-haystack
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

[**django-haystack / haystack / utils / highlighting.py**](https://github.com/django-haystack/django-haystack/blob/master/haystack/utils/highlighting.py)

```python
# highlighting.py
~~from django.utils.html import strip_tags


class Highlighter(object):
    css_class = "highlighted"
    html_tag = "span"
    max_length = 200
    text_block = ""

    def __init__(self, query, **kwargs):
        self.query = query

        if "max_length" in kwargs:
            self.max_length = int(kwargs["max_length"])

        if "html_tag" in kwargs:
            self.html_tag = kwargs["html_tag"]

        if "css_class" in kwargs:
            self.css_class = kwargs["css_class"]

        self.query_words = set(
            [word.lower() for word in self.query.split() if not word.startswith("-")]
        )

    def highlight(self, text_block):
~~        self.text_block = strip_tags(text_block)
        highlight_locations = self.find_highlightable_words()
        start_offset, end_offset = self.find_window(highlight_locations)
        return self.render_html(highlight_locations, start_offset, end_offset)

    def find_highlightable_words(self):
        word_positions = {}

        end_offset = len(self.text_block)
        lower_text_block = self.text_block.lower()

        for word in self.query_words:
            if word not in word_positions:
                word_positions[word] = []

            start_offset = 0

            while start_offset < end_offset:
                next_offset = lower_text_block.find(word, start_offset, end_offset)

                if next_offset == -1:
                    break

                word_positions[word].append(next_offset)
                start_offset = next_offset + len(word)


## ... source file continues with no further strip_tags examples...

```


## Example 2 from django-tables2
[django-tables2](https://github.com/jieter/django-tables2)
([projection documentation](https://django-tables2.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-tables2/))
is a code library for [Django](/django.html) that simplifies creating and
displaying tables in [Django templates](/django-templates.html),
especially with more advanced features such as pagination and sorting.
The project and its code are
[available as open source](https://github.com/jieter/django-tables2/blob/master/LICENSE).

[**django-tables2 / django_tables2 / columns / templatecolumn.py**](https://github.com/jieter/django-tables2/blob/master/django_tables2/columns/templatecolumn.py)

```python
# templatecolumn.py
from django.template import Context, Template
from django.template.loader import get_template
~~from django.utils.html import strip_tags

from .base import Column, library


@library.register
class TemplateColumn(Column):

    empty_values = ()

    def __init__(self, template_code=None, template_name=None, extra_context=None, **extra):
        super().__init__(**extra)
        self.template_code = template_code
        self.template_name = template_name
        self.extra_context = extra_context or {}

        if not self.template_code and not self.template_name:
            raise ValueError("A template must be provided")

    def render(self, record, table, value, bound_column, **kwargs):
        context = getattr(table, "context", Context())
        context.update(self.extra_context)
        context.update(
            {
                "default": bound_column.default,
                "column": bound_column,
                "record": record,
                "value": value,
                "row_counter": kwargs["bound_row"].row_counter,
            }
        )

        try:
            if self.template_code:
                return Template(self.template_code).render(context)
            else:
                return get_template(self.template_name).render(context.flatten())
        finally:
            context.pop()

    def value(self, **kwargs):
        html = super().value(**kwargs)
~~        return strip_tags(html) if isinstance(html, str) else html



## ... source file continues with no further strip_tags examples...

```


## Example 3 from register
[register](https://github.com/ORGAN-IZE/register) is a [Django](/django.html),
[Bootstrap](/bootstrap-css.html), [PostgreSQL](/postgresql.html) project that is
open source under the
[GNU General Public License v3.0](https://github.com/ORGAN-IZE/register/blob/master/LICENSE).
This web application makes it easier for people to register as organ donors.
You can see the application live at
[https://register.organize.org/](https://register.organize.org/).

[**register / registration / bootstrap3_renderers.py**](https://github.com/ORGAN-IZE/register/blob/master/registration/./bootstrap3_renderers.py)

```python
# bootstrap3_renderers.py
import re

from django.forms import (
    CheckboxInput, ClearableFileInput, RadioSelect, CheckboxSelectMultiple
)
from django.forms.widgets import SelectDateWidget
~~from django.utils.html import strip_tags

import bootstrap3.renderers
from bootstrap3.forms import render_label


RE_INPUT_TAG = re.compile(r'(<label.*>)(<input.*/>)')


class FiftyThreeFieldRenderer(bootstrap3.renderers.FieldRenderer):
    def post_widget_render(self, html):
        if isinstance(self.widget, RadioSelect):
            html = self.list_to_class(html, 'radio')
            html = self.invert_radio_input(html)
        elif isinstance(self.widget, CheckboxSelectMultiple):
            html = self.list_to_class(html, 'checkbox')
        elif isinstance(self.widget, SelectDateWidget):
            html = self.fix_date_select_input(html)
        elif isinstance(self.widget, ClearableFileInput):
            html = self.fix_clearable_file_input(html)
        elif isinstance(self.widget, CheckboxInput):
            html = self.put_inside_label(html)
        return html

    def put_inside_label(self, html):
        return html + render_label(
            content=self.field.label, label_for=self.field.id_for_label,
~~            label_title=strip_tags(self.field_help))

    def invert_radio_input(self, html):
        return re.sub(RE_INPUT_TAG, r'\2\1', html)



## ... source file continues with no further strip_tags examples...

```

