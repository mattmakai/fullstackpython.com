title: django.utils.http http_date Example Code
category: page
slug: django-utils-http-http-date-examples
sortorder: 500011470
toc: False
sidebartitle: django.utils.http http_date
meta: Python example code for the http_date callable from the django.utils.http module of the Django project.


http_date is a callable within the django.utils.http module of the Django project.


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
from django.utils.encoding import filepath_to_uri
~~from django.utils.http import http_date
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
~~        response["Last-Modified"] = http_date(statobj.st_mtime)
    else:
        if isinstance(last_modified, datetime):
            last_modified = float(dateformat.format(last_modified, "U"))
~~        response["Last-Modified"] = http_date(epoch_seconds=last_modified)

    response["Content-Length"] = statobj.st_size

    if encoding:
        response["Content-Encoding"] = encoding

    if filename:
        filename_escaped = filepath_to_uri(filename)
        if "pdf" in mimetype.lower():
            response["Content-Disposition"] = "inline; filename=%s" % filename_escaped
        else:
            response["Content-Disposition"] = (
                "attachment; filename=%s" % filename_escaped
            )

    return response



## ... source file continues with no further http_date examples...

```


## Example 2 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / utils / sendfile_streaming_backend.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/utils/sendfile_streaming_backend.py)

```python
# sendfile_streaming_backend.py

import os
import re
import stat
from email.utils import mktime_tz, parsedate_tz
from wsgiref.util import FileWrapper

from django.http import HttpResponseNotModified, StreamingHttpResponse
~~from django.utils.http import http_date


def sendfile(request, filename, **kwargs):
    statobj = os.stat(filename)

    if not was_modified_since(request.META.get('HTTP_IF_MODIFIED_SINCE'),
                              statobj[stat.ST_MTIME], statobj[stat.ST_SIZE]):
        return HttpResponseNotModified()

    response = StreamingHttpResponse(FileWrapper(open(filename, 'rb')))

~~    response["Last-Modified"] = http_date(statobj[stat.ST_MTIME])
    return response


def was_modified_since(header=None, mtime=0, size=0):
    try:
        if header is None:
            raise ValueError
        matches = re.match(r"^([^;]+)(; length=([0-9]+))?$", header,
                           re.IGNORECASE)
        header_date = parsedate_tz(matches.group(1))
        if header_date is None:
            raise ValueError
        header_mtime = mktime_tz(header_date)
        header_len = matches.group(3)
        if header_len and int(header_len) != size:
            raise ValueError
        if mtime > header_mtime:
            raise ValueError
    except (AttributeError, ValueError, OverflowError):
        return True
    return False



## ... source file continues with no further http_date examples...

```

