title: django.core.exceptions SuspiciousMultipartForm Example Code
category: page
slug: django-core-exceptions-suspiciousmultipartform-examples
sortorder: 500011107
toc: False
sidebartitle: django.core.exceptions SuspiciousMultipartForm
meta: Python example code for the SuspiciousMultipartForm class from the django.core.exceptions module of the Django project.


SuspiciousMultipartForm is a class within the django.core.exceptions module of the Django project.


## Example 1 from django-angular
[django-angular](https://github.com/jrief/django-angular)
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / views / upload.py**](https://github.com/jrief/django-angular/blob/master/djng/views/upload.py)

```python
# upload.py
~~from django.core.exceptions import SuspiciousMultipartForm
from django.core import signing
from django.views.generic import View
from django.http import JsonResponse

from djng import app_settings
from djng.forms.fields import FileField, ImageField


class FileUploadView(View):
    storage = app_settings.upload_storage
    thumbnail_size = app_settings.THUMBNAIL_OPTIONS
    signer = signing.Signer()

    def post(self, request, *args, **kwargs):
        if request.POST.get('filetype') == 'file':
            field = FileField
        elif request.POST.get('filetype') == 'image':
            field = ImageField
        else:
~~            raise SuspiciousMultipartForm("Missing attribute 'filetype' in form data.")
        data = {}
        for name, file_obj in request.FILES.items():
            data[name] = field.preview(file_obj)
        return JsonResponse(data)



## ... source file continues with no further SuspiciousMultipartForm examples...

```

