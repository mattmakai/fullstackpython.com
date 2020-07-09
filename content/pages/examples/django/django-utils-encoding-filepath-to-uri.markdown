title: django.utils.encoding filepath_to_uri Example Code
category: page
slug: django-utils-encoding-filepath-to-uri-examples
sortorder: 500011441
toc: False
sidebartitle: django.utils.encoding filepath_to_uri
meta: Python example code for the filepath_to_uri callable from the django.utils.encoding module of the Django project.


filepath_to_uri is a callable within the django.utils.encoding module of the Django project.


## Example 1 from django-wiki
[django-wiki](https://github.com/django-wiki/django-wiki)
([project documentation](https://django-wiki.readthedocs.io/en/master/),
[demo](https://demo.django-wiki.org/),
and [PyPI page](https://pypi.org/project/django-wiki/))
is a wiki system code library for [Django](/django.html)
projects that makes it easier to create user-editable content.
The project aims to provide necessary core features and then
have an easy plugin format for additional features, rather than
having every exhaustive feature built into the core system.
django-wiki is a rewrite of an earlier now-defunct project
named [django-simplewiki](https://code.google.com/p/django-simple-wiki/).

The code for django-wiki is provided as open source under the
[GNU General Public License 3.0](https://github.com/django-wiki/django-wiki/blob/master/COPYING).

[**django-wiki / src/wiki / core / http.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/core/http.py)

```python
# http.py
import mimetypes
import os
from datetime import datetime

from django.http import HttpResponse
from django.utils import dateformat
~~from django.utils.encoding import filepath_to_uri
from django.utils.http import http_date
from wiki.conf import settings


def django_sendfile_response(request, filepath):
    from sendfile import sendfile

    return sendfile(request, filepath)


def send_file(request, filepath, last_modified=None, filename=None):
    fullpath = filepath
    statobj = os.stat(fullpath)
    if filename:
        mimetype, encoding = mimetypes.guess_type(filename)
    else:
        mimetype, encoding = mimetypes.guess_type(fullpath)

    mimetype = mimetype or "application/octet-stream"

    if settings.USE_SENDFILE:
        response = django_sendfile_response(request, filepath)
    else:
        response = HttpResponse(open(fullpath, "rb").read(), content_type=mimetype)

    if not last_modified:
        response["Last-Modified"] = http_date(statobj.st_mtime)
    else:
        if isinstance(last_modified, datetime):
            last_modified = float(dateformat.format(last_modified, "U"))
        response["Last-Modified"] = http_date(epoch_seconds=last_modified)

    response["Content-Length"] = statobj.st_size

    if encoding:
        response["Content-Encoding"] = encoding

    if filename:
~~        filename_escaped = filepath_to_uri(filename)
        if "pdf" in mimetype.lower():
            response["Content-Disposition"] = "inline; filename=%s" % filename_escaped
        else:
            response["Content-Disposition"] = (
                "attachment; filename=%s" % filename_escaped
            )

    return response



## ... source file continues with no further filepath_to_uri examples...

```

