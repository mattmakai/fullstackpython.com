title: django.views.generic.detail SingleObjectMixin Example Code
category: page
slug: django-views-generic-detail-singleobjectmixin-examples
sortorder: 500011533
toc: False
sidebartitle: django.views.generic.detail SingleObjectMixin
meta: Python example code for the SingleObjectMixin class from the django.views.generic.detail module of the Django project.


SingleObjectMixin is a class within the django.views.generic.detail module of the Django project.


## Example 1 from django-downloadview
[django-downloadview](https://github.com/benoitbryon/django-downloadview)
([project documentation](https://django-downloadview.readthedocs.io/en/1.9/)
and
[PyPI package information](https://pypi.org/project/django-downloadview/))
is a [Django](/django.html) extension for serving downloads through your
web application. While typically you would use a web server to handle
[static content](/static-content.html), sometimes you need to control
file access, such as requiring a user to register before downloading a
PDF. In that situations, django-downloadview is a handy library to avoid
boilerplate code for common scenarios.

[**django-downloadview / django_downloadview / views / object.py**](https://github.com/benoitbryon/django-downloadview/blob/master/django_downloadview/views/object.py)

```python
# object.py
~~from django.views.generic.detail import SingleObjectMixin

from django_downloadview.exceptions import FileNotFound
from django_downloadview.views.base import BaseDownloadView


~~class ObjectDownloadView(SingleObjectMixin, BaseDownloadView):

    file_field = "file"

    basename_field = None

    encoding_field = None

    mime_type_field = None

    charset_field = None

    modification_time_field = None

    size_field = None

    def get_file(self):
        file_instance = getattr(self.object, self.file_field)
        if not file_instance:
            raise FileNotFound(
                f'Field="{self.file_field}" on object="{self.object}" is empty'
            )
        for field in ("encoding", "mime_type", "charset", "modification_time", "size"):
            model_field = getattr(self, "%s_field" % field, False)
            if model_field:


## ... source file continues with no further SingleObjectMixin examples...

```

