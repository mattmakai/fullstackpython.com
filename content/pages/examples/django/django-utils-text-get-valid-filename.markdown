title: django.utils.text get_valid_filename Example Code
category: page
slug: django-utils-text-get-valid-filename-examples
sortorder: 500011492
toc: False
sidebartitle: django.utils.text get_valid_filename
meta: Python example code for the get_valid_filename callable from the django.utils.text module of the Django project.


get_valid_filename is a callable within the django.utils.text module of the Django project.


## Example 1 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / utils / files.py**](https://github.com/divio/django-filer/blob/develop/filer/utils/files.py)

```python
# files.py
from __future__ import absolute_import, unicode_literals

import os

from django.http.multipartparser import (
    ChunkIter, SkipFile, StopFutureHandlers, StopUpload, exhaust,
)
from django.template.defaultfilters import slugify as slugify_django
from django.utils.encoding import force_text
~~from django.utils.text import get_valid_filename as get_valid_filename_django

from unidecode import unidecode


class UploadException(Exception):
    pass


def handle_upload(request):
    if not request.method == "POST":
        raise UploadException("AJAX request not valid: must be POST")
    if request.is_ajax():
        is_raw = True
        filename = request.GET.get('qqfile', False) or request.GET.get('filename', False) or ''

        try:
            content_length = int(request.META['CONTENT_LENGTH'])
        except (IndexError, TypeError, ValueError):
            content_length = None

        if content_length < 0:
            raise UploadException("Invalid content length: %r" % content_length)

        upload_handlers = request.upload_handlers


## ... source file abbreviated to get to get_valid_filename examples ...



        for i, handler in enumerate(upload_handlers):
            file_obj = handler.file_complete(counters[i])
            if file_obj:
                upload = file_obj
                break
    else:
        if len(request.FILES) == 1:
            upload, filename, is_raw = handle_request_files_upload(request)
        else:
            raise UploadException("AJAX request not valid: Bad Upload")
    return upload, filename, is_raw


def handle_request_files_upload(request):
    is_raw = False
    upload = list(request.FILES.values())[0]
    filename = upload.name
    return upload, filename, is_raw


def slugify(string):
    return slugify_django(unidecode(force_text(string)))


~~def get_valid_filename(s):
    s = get_valid_filename_django(s)
    filename, ext = os.path.splitext(s)
    filename = slugify(filename)
    ext = slugify(ext)
    if ext:
        return "%s.%s" % (filename, ext)
    else:
        return "%s" % (filename,)



## ... source file continues with no further get_valid_filename examples...

```

