title: django.utils.html smart_urlquote Example Code
category: page
slug: django-utils-html-smart-urlquote-examples
sortorder: 500011467
toc: False
sidebartitle: django.utils.html smart_urlquote
meta: Python example code for the smart_urlquote callable from the django.utils.html module of the Django project.


smart_urlquote is a callable within the django.utils.html module of the Django project.


## Example 1 from django-rest-framework
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
~~from django.utils.html import escape, format_html, smart_urlquote
from django.utils.safestring import SafeData, mark_safe

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


## ... source file abbreviated to get to smart_urlquote examples ...


        return new_links

    return links


@register.filter
def add_nested_class(value):
    if isinstance(value, dict):
        return 'class=nested'
    if isinstance(value, list) and any([isinstance(item, (list, dict)) for item in value]):
        return 'class=nested'
    return ''


TRAILING_PUNCTUATION = ['.', ',', ':', ';', '.)', '"', "']", "'}", "'"]
WRAPPING_PUNCTUATION = [('(', ')'), ('<', '>'), ('[', ']'), ('&lt;', '&gt;'),
                        ('"', '"'), ("'", "'")]
word_split_re = re.compile(r'(\s+)')
simple_url_re = re.compile(r'^https?://\[?\w', re.IGNORECASE)
simple_url_2_re = re.compile(r'^www\.|^(?!http)\w[^@]+\.(com|edu|gov|int|mil|net|org)$', re.IGNORECASE)
simple_email_re = re.compile(r'^\S+@\S+\.\S+$')


def smart_urlquote_wrapper(matched_url):
    try:
~~        return smart_urlquote(matched_url)
    except ValueError:
        return None


@register.filter(needs_autoescape=True)
def urlize_quoted_links(text, trim_url_limit=None, nofollow=True, autoescape=True):
    def trim_url(x, limit=trim_url_limit):
        return limit is not None and (len(x) > limit and ('%s...' % x[:max(0, limit - 3)])) or x

    safe_input = isinstance(text, SafeData)

    def conditional_escape(text):
        return escape(text) if autoescape and not safe_input else text

    words = word_split_re.split(force_str(text))
    for i, word in enumerate(words):
        if '.' in word or '@' in word or ':' in word:
            lead, middle, trail = '', word, ''
            for punctuation in TRAILING_PUNCTUATION:
                if middle.endswith(punctuation):
                    middle = middle[:-len(punctuation)]
                    trail = punctuation + trail
            for opening, closing in WRAPPING_PUNCTUATION:
                if middle.startswith(opening):


## ... source file continues with no further smart_urlquote examples...

```

