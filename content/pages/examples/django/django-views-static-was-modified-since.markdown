title: django.views.static was_modified_since Example Code
category: page
slug: django-views-static-was-modified-since-examples
sortorder: 500011543
toc: False
sidebartitle: django.views.static was_modified_since
meta: Python example code for the was_modified_since callable from the django.views.static module of the Django project.


was_modified_since is a callable within the django.views.static module of the Django project.


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

[**django-downloadview / django_downloadview / views / base.py**](https://github.com/benoitbryon/django-downloadview/blob/master/django_downloadview/views/base.py)

```python
# base.py
import calendar

from django.http import Http404, HttpResponseNotModified
from django.views.generic.base import View
~~from django.views.static import was_modified_since

from django_downloadview import exceptions
from django_downloadview.response import DownloadResponse


class DownloadMixin(object):

    response_class = DownloadResponse

    attachment = True

    basename = None

    mimetype = None

    encoding = None

    def get_file(self):
        raise NotImplementedError()

    def get_basename(self):
        return self.basename

    def get_mimetype(self):
        return self.mimetype

    def get_encoding(self):
        return self.encoding

~~    def was_modified_since(self, file_instance, since):
        try:
            return file_instance.was_modified_since(since)
        except (AttributeError, NotImplementedError):
            try:
                modification_time = calendar.timegm(
                    file_instance.modified_time.utctimetuple()
                )
                size = file_instance.size
            except (AttributeError, NotImplementedError) as e:
                print("!=======!", e)
                return True
            else:
~~                return was_modified_since(since, modification_time, size)

    def not_modified_response(self, *response_args, **response_kwargs):
        return HttpResponseNotModified(*response_args, **response_kwargs)

    def download_response(self, *response_args, **response_kwargs):
        response_kwargs.setdefault("file_instance", self.file_instance)
        response_kwargs.setdefault("attachment", self.attachment)
        response_kwargs.setdefault("basename", self.get_basename())
        response_kwargs.setdefault("file_mimetype", self.get_mimetype())
        response_kwargs.setdefault("file_encoding", self.get_encoding())
        response = self.response_class(*response_args, **response_kwargs)
        return response

    def file_not_found_response(self):
        raise Http404()

    def render_to_response(self, *response_args, **response_kwargs):
        try:
            self.file_instance = self.get_file()
        except exceptions.FileNotFound:
            return self.file_not_found_response()
        since = self.request.META.get("HTTP_IF_MODIFIED_SINCE", None)
        if since is not None:
            if not self.was_modified_since(self.file_instance, since):


## ... source file continues with no further was_modified_since examples...

```

