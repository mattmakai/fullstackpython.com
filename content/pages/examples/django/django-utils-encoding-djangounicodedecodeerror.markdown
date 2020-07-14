title: django.utils.encoding DjangoUnicodeDecodeError Example Code
category: page
slug: django-utils-encoding-djangounicodedecodeerror-examples
sortorder: 500011440
toc: False
sidebartitle: django.utils.encoding DjangoUnicodeDecodeError
meta: Python example code for the DjangoUnicodeDecodeError class from the django.utils.encoding module of the Django project.


DjangoUnicodeDecodeError is a class within the django.utils.encoding module of the Django project.


## Example 1 from django-pipeline
[django-pipeline](https://github.com/jazzband/django-pipeline)
([project documentation](https://django-pipeline.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-pipeline/))
is a code library for handling and compressing
[static content assets](/static-content.html) when handling requests in
[Django](/django.html) web applications.

The django-pipeline project is open sourced under the
[MIT License](https://github.com/jazzband/django-pipeline/blob/master/LICENSE)
and it is maintained by the developer community group
[Jazzband](https://jazzband.co/).

[**django-pipeline / pipeline / middleware.py**](https://github.com/jazzband/django-pipeline/blob/master/pipeline/./middleware.py)

```python
# middleware.py
from django.core.exceptions import MiddlewareNotUsed
~~from django.utils.encoding import DjangoUnicodeDecodeError
from django.utils.html import strip_spaces_between_tags as minify_html

from pipeline.conf import settings

from django.utils.deprecation import MiddlewareMixin


class MinifyHTMLMiddleware(MiddlewareMixin):
    def __init__(self, *args, **kwargs):
        super(MinifyHTMLMiddleware, self).__init__(*args, **kwargs)
        if not settings.PIPELINE_ENABLED:
            raise MiddlewareNotUsed

    def process_response(self, request, response):
        if response.has_header('Content-Type') and 'text/html' in response['Content-Type']:
            try:
                response.content = minify_html(response.content.decode('utf-8').strip())
                response['Content-Length'] = str(len(response.content))
~~            except DjangoUnicodeDecodeError:
                pass
        return response



## ... source file continues with no further DjangoUnicodeDecodeError examples...

```

