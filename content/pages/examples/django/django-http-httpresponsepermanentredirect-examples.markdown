title: django.http HttpResponsePermanentRedirect Python Code Examples
category: page
slug: django-http-httpresponsepermanentredirect-examples
sortorder: 500013460
toc: False
sidebartitle: django.http HttpResponsePermanentRedirect
meta: Example code that shows you how to use the HttpResponsePermanentRedirect class from the django.http module.


[HttpResponsePermanentRedirect](https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpResponsePermanentRedirect)
([source code](https://github.com/django/django/blob/master/django/http/response.py))
is a class in the [Django](/django.html) code base for returning an
[HTTP 301 status code](https://blog.hubspot.com/blog/tabid/6307/bid/7430/what-is-a-301-redirect-and-why-should-you-care.aspx)
or a permanent URL redirect from your web application.

Note that you can import `HttpResponsePermanentRedirect` from either
`django.http.responses` or `django.http`, because the latter one 
imports the responses from the `responses.py` file.

`HttpResponsePermanentRedirect` is often used in combination with
[django.conf.urls url](/django-conf-urls-url-examples.html).


## Example 1 from django-angular
[django-angular](https://github.com/jrief/django-angular) 
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use 
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is open source under
[the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / urls.py**](https://github.com/jrief/django-angular/blob/master/djng/urls.py)

```python
import warnings
from django.urls import reverse
from django.conf.urls import url
~~from django.http.response import HttpResponsePermanentRedirect


warnings.warn("Reversing URL's using urlpatterns is deprecated. "
              "Please use the middleware instead",
              DeprecationWarning)


def angular_reverse(request, *args, **kwargs):
    url_name = request.GET.get('djng_url_name')
    url_args = request.GET.getlist('djng_url_args', None)
    url_kwargs = {}

    prefix = 'djng_url_kwarg_'
    for param in request.GET:
        if param.startswith(prefix):
            url_kwargs[param[len(prefix):]] = request.GET[param]

~~    url = reverse(url_name, args=url_args, kwargs=url_kwargs)
~~    return HttpResponsePermanentRedirect(url)


urlpatterns = [
    url(r'^reverse/$', angular_reverse),
]
```
