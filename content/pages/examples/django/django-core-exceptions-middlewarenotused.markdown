title: django.core.exceptions MiddlewareNotUsed Example Code
category: page
slug: django-core-exceptions-middlewarenotused-examples
sortorder: 500011102
toc: False
sidebartitle: django.core.exceptions MiddlewareNotUsed
meta: Python example code for the MiddlewareNotUsed class from the django.core.exceptions module of the Django project.


MiddlewareNotUsed is a class within the django.core.exceptions module of the Django project.


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
~~from django.core.exceptions import MiddlewareNotUsed
from django.utils.encoding import DjangoUnicodeDecodeError
from django.utils.html import strip_spaces_between_tags as minify_html

from pipeline.conf import settings

from django.utils.deprecation import MiddlewareMixin


class MinifyHTMLMiddleware(MiddlewareMixin):
    def __init__(self, *args, **kwargs):
        super(MinifyHTMLMiddleware, self).__init__(*args, **kwargs)
        if not settings.PIPELINE_ENABLED:
~~            raise MiddlewareNotUsed

    def process_response(self, request, response):
        if response.has_header('Content-Type') and 'text/html' in response['Content-Type']:
            try:
                response.content = minify_html(response.content.decode('utf-8').strip())
                response['Content-Length'] = str(len(response.content))
            except DjangoUnicodeDecodeError:
                pass
        return response



## ... source file continues with no further MiddlewareNotUsed examples...

```


## Example 2 from django-user-visit
[django-user-visit](https://github.com/yunojuno/django-user-visit)
([PyPI package information](https://pypi.org/project/django-user-visit/))
is a [Django](/django.html) app and
[middleware](https://docs.djangoproject.com/en/stable/topics/http/middleware/)
for tracking daily user visits to your web application. The goal
is to record per user per day instead of for every request a user
sends to the application. The project is provided as open source
under the
[MIT license](https://github.com/yunojuno/django-user-visit/blob/master/LICENSE).

[**django-user-visit / user_visit / middleware.py**](https://github.com/yunojuno/django-user-visit/blob/master/user_visit/./middleware.py)

```python
# middleware.py
import logging
import typing

import django.db
~~from django.core.exceptions import MiddlewareNotUsed
from django.http import HttpRequest, HttpResponse
from django.utils import timezone

from user_visit.models import UserVisit

from .settings import RECORDING_DISABLED

logger = logging.getLogger(__name__)

SESSION_KEY = "user_visit.hash"


class UserVisitMiddleware:

    def __init__(self, get_response: typing.Callable) -> None:
        if RECORDING_DISABLED:
~~            raise MiddlewareNotUsed("UserVisit recording has been disabled")
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> typing.Optional[HttpResponse]:
        if request.user.is_anonymous:
            return self.get_response(request)

        uv = UserVisit.objects.build(request, timezone.now())
        if request.session.get(SESSION_KEY, "") == uv.hash:
            return self.get_response(request)

        try:
            uv.save()
        except django.db.IntegrityError:
            logger.warning("Unable to record user visit - duplicate request hash")
        else:
            request.session[SESSION_KEY] = uv.hash
        return self.get_response(request)



## ... source file continues with no further MiddlewareNotUsed examples...

```

