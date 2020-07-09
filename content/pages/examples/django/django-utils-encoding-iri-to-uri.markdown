title: django.utils.encoding iri_to_uri Example Code
category: page
slug: django-utils-encoding-iri-to-uri-examples
sortorder: 500011445
toc: False
sidebartitle: django.utils.encoding iri_to_uri
meta: Python example code for the iri_to_uri callable from the django.utils.encoding module of the Django project.


iri_to_uri is a callable within the django.utils.encoding module of the Django project.


## Example 1 from django-oauth-toolkit
[django-oauth-toolkit](https://github.com/jazzband/django-oauth-toolkit)
([project website](http://dot.evonove.it/) and
[PyPI package information](https://pypi.org/project/django-oauth-toolkit/1.2.0/))
is a code library for adding and handling [OAuth2](https://oauth.net/)
flows within your [Django](/django.html) web application and
[API](/application-programming-interfaces.html).

The django-oauth-toolkit project is open sourced under the
[FreeBSD license](https://github.com/jazzband/django-oauth-toolkit/blob/master/LICENSE)
and it is maintained by the developer community group
[Jazzband](https://jazzband.co/).

[**django-oauth-toolkit / oauth2_provider / http.py**](https://github.com/jazzband/django-oauth-toolkit/blob/master/oauth2_provider/./http.py)

```python
# http.py
from urllib.parse import urlparse

from django.core.exceptions import DisallowedRedirect
from django.http import HttpResponse
~~from django.utils.encoding import iri_to_uri


class OAuth2ResponseRedirect(HttpResponse):
    status_code = 302

    def __init__(self, redirect_to, allowed_schemes, *args, **kwargs):
        super().__init__(*args, **kwargs)
~~        self["Location"] = iri_to_uri(redirect_to)
        self.allowed_schemes = allowed_schemes
        self.validate_redirect(redirect_to)

    @property
    def url(self):
        return self["Location"]

    def validate_redirect(self, redirect_to):
        parsed = urlparse(str(redirect_to))
        if not parsed.scheme:
            raise DisallowedRedirect("OAuth2 redirects require a URI scheme.")
        if parsed.scheme not in self.allowed_schemes:
            raise DisallowedRedirect(
                "Redirect to scheme {!r} is not permitted".format(parsed.scheme)
            )



## ... source file continues with no further iri_to_uri examples...

```


## Example 2 from django-rest-framework
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
~~from django.utils.encoding import force_str, iri_to_uri
from django.utils.html import escape, format_html, smart_urlquote
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


## ... source file abbreviated to get to iri_to_uri examples ...


@register.simple_tag
def optional_logout(request, user):
    try:
        logout_url = reverse('rest_framework:logout')
    except NoReverseMatch:
        snippet = format_html('<li class="navbar-text">{user}</li>', user=escape(user))
        return mark_safe(snippet)

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

    return mark_safe(snippet)


@register.simple_tag
def add_query_param(request, key, val):
    iri = request.get_full_path()
~~    uri = iri_to_uri(iri)
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


## ... source file continues with no further iri_to_uri examples...

```

