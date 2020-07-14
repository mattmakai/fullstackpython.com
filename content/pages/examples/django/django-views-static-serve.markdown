title: django.views.static serve Example Code
category: page
slug: django-views-static-serve-examples
sortorder: 500011542
toc: False
sidebartitle: django.views.static serve
meta: Python example code for the serve callable from the django.views.static module of the Django project.


serve is a callable within the django.views.static module of the Django project.


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

[**django-pipeline / pipeline / views.py**](https://github.com/jazzband/django-pipeline/blob/master/pipeline/./views.py)

```python
# views.py
from django.conf import settings as django_settings
from django.core.exceptions import ImproperlyConfigured
~~from django.views.static import serve

from .collector import default_collector
from .conf import settings


def serve_static(request, path, insecure=False, **kwargs):
    if not django_settings.DEBUG and not insecure:
        raise ImproperlyConfigured("The staticfiles view can only be used in "
                                   "debug mode or if the --insecure "
                                   "option of 'runserver' is used")

    if not settings.PIPELINE_ENABLED and settings.PIPELINE_COLLECTOR_ENABLED:
        default_collector.collect(request, files=[path])

~~    return serve(request, path, document_root=django_settings.STATIC_ROOT,
                 **kwargs)



## ... source file continues with no further serve examples...

```

