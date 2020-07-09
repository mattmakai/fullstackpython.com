title: django.utils.http unquote Example Code
category: page
slug: django-utils-http-unquote-examples
sortorder: 500011473
toc: False
sidebartitle: django.utils.http unquote
meta: Python example code for the unquote callable from the django.utils.http module of the Django project.


unquote is a callable within the django.utils.http module of the Django project.


## Example 1 from django-angular
[django-angular](https://github.com/jrief/django-angular)
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / middleware.py**](https://github.com/jrief/django-angular/blob/master/djng/./middleware.py)

```python
# middleware.py
from django import http
from django.urls import reverse
~~from django.utils.http import unquote
try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class AngularUrlMiddleware(MiddlewareMixin):
    ANGULAR_REVERSE = '/angular/reverse/'

    def process_request(self, request):
        if request.path == self.ANGULAR_REVERSE:
            url_name = request.GET.get('djng_url_name')
            url_args = request.GET.getlist('djng_url_args', [])
            url_kwargs = {}

            url_args = filter(lambda x: x, url_args)

            for param in request.GET:
                if param.startswith('djng_url_kwarg_'):
                    if request.GET[param]:
                        url_kwargs[param[15:]] = request.GET[param]  # [15:] to remove 'djng_url_kwarg' prefix

~~            url = unquote(reverse(url_name, args=url_args, kwargs=url_kwargs))
            assert not url.startswith(self.ANGULAR_REVERSE), "Prevent recursive requests"

            request.path = request.path_info = url
            request.environ['PATH_INFO'] = url
            query = request.GET.copy()
            for key in request.GET:
                if key.startswith('djng_url'):
                    query.pop(key, None)
            request.environ['QUERY_STRING'] = query.urlencode()

            request.GET = http.QueryDict(request.environ['QUERY_STRING'])



## ... source file continues with no further unquote examples...

```

