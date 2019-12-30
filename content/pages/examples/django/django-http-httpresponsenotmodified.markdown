title: django.http HttpResponseNotModified Python Code Examples
category: page
slug: django-http-httpresponsenotmodified-examples
sortorder: 500013450
toc: False
sidebartitle: django.http HttpResponseNotModified
meta: Example Python code for using the HttpResponseNotModified object provided by Django in the django.http module.


[HttpResponseNotModified](https://docs.djangoproject.com/en/stable/ref/request-response/#django.http.HttpResponseNotModified)
([source code](https://github.com/django/django/blob/master/django/http/response.py))
returns the 
[HTTP 304 status code](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) 
from a [Django](/django.html) web application view. The HTTP 304 status code
indicates that the resource has not been modified since the client last requested
it.

[HttpResponseRedirect](/django-http-httpresponseredirect-examples.html) 
and
[HttpResponsePermanentRedirect](/django-http-httpresponsepermanentredirect-examples.html)
are other types of 300-level HTTP status codes that can be
sent as a response by your Django application.


## Example 1 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / utils / sendfile_streaming_backend.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/utils/sendfile_streaming_backend.py)

```python
# Sendfile "streaming" backend
# This is based on sendfiles builtin "simple" backend but uses a StreamingHttpResponse

import os
import re
import stat
from email.utils import mktime_tz, parsedate_tz
from wsgiref.util import FileWrapper

~~from django.http import HttpResponseNotModified, StreamingHttpResponse
from django.utils.http import http_date


def sendfile(request, filename, **kwargs):
    # Respect the If-Modified-Since header.
    statobj = os.stat(filename)

    if not was_modified_since(request.META.get('HTTP_IF_MODIFIED_SINCE'),
                              statobj[stat.ST_MTIME], statobj[stat.ST_SIZE]):
~~        return HttpResponseNotModified()

    response = StreamingHttpResponse(FileWrapper(open(filename, 'rb')))

    response["Last-Modified"] = http_date(statobj[stat.ST_MTIME])
    return response


def was_modified_since(header=None, mtime=0, size=0):
    """
    Was something modified since the user last downloaded it?

    header
      This is the value of the If-Modified-Since header.  If this is None,
      I'll just return True.

    mtime
      This is the modification time of the item we're talking about.

    size
      This is the size of the item we're talking about.
    """
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

```

