title: django.utils.version get_complete_version Example Code
category: page
slug: django-utils-version-get-complete-version-examples
sortorder: 500011513
toc: False
sidebartitle: django.utils.version get_complete_version
meta: Python example code for the get_complete_version callable from the django.utils.version module of the Django project.


get_complete_version is a callable within the django.utils.version module of the Django project.


## Example 1 from django-webtest
[django-webtest](https://github.com/django-webtest/django-webtest)
([PyPI package information](https://pypi.org/project/django-webtest/))
is a [Django](/django.html) extension that makes it easier to use
[WebTest](http://docs.pylonsproject.org/projects/webtest/) with
your projects.

The project is open sourced under the
[MIT license](https://github.com/django-webtest/django-webtest/blob/master/LICENSE.txt).

[**django-webtest / django_webtest / backends.py**](https://github.com/django-webtest/django-webtest/blob/master/django_webtest/./backends.py)

```python
# backends.py
from __future__ import absolute_import
~~from django.utils.version import get_complete_version
from django.contrib.auth.backends import RemoteUserBackend
from django_webtest.compat import from_wsgi_safe_string

class WebtestUserBackend(RemoteUserBackend):

~~    if get_complete_version() >= (1, 11):
        def authenticate(self, request, django_webtest_user):
            return super(WebtestUserBackend, self).authenticate(
                request, django_webtest_user)
    else:
        def authenticate(self, django_webtest_user):
            return super(WebtestUserBackend, self).authenticate(
                django_webtest_user)

    def clean_username(self, username):
        return from_wsgi_safe_string(username)



## ... source file continues with no further get_complete_version examples...

```

