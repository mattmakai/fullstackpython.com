title: django.core.exceptions DisallowedRedirect Example Code
category: page
slug: django-core-exceptions-disallowedredirect-examples
sortorder: 500011098
toc: False
sidebartitle: django.core.exceptions DisallowedRedirect
meta: Python example code for the DisallowedRedirect class from the django.core.exceptions module of the Django project.


DisallowedRedirect is a class within the django.core.exceptions module of the Django project.


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

~~from django.core.exceptions import DisallowedRedirect
from django.http import HttpResponse
from django.utils.encoding import iri_to_uri


class OAuth2ResponseRedirect(HttpResponse):
    status_code = 302

    def __init__(self, redirect_to, allowed_schemes, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self["Location"] = iri_to_uri(redirect_to)
        self.allowed_schemes = allowed_schemes
        self.validate_redirect(redirect_to)

    @property
    def url(self):
        return self["Location"]

    def validate_redirect(self, redirect_to):
        parsed = urlparse(str(redirect_to))
        if not parsed.scheme:
~~            raise DisallowedRedirect("OAuth2 redirects require a URI scheme.")
        if parsed.scheme not in self.allowed_schemes:
~~            raise DisallowedRedirect(
                "Redirect to scheme {!r} is not permitted".format(parsed.scheme)
            )



## ... source file continues with no further DisallowedRedirect examples...

```

