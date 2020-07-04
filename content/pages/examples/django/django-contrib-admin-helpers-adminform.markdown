title: django.contrib.admin.helpers AdminForm Example Code
category: page
slug: django-contrib-admin-helpers-adminform-examples
sortorder: 500011021
toc: False
sidebartitle: django.contrib.admin.helpers AdminForm
meta: Python example code for the AdminForm class from the django.contrib.admin.helpers module of the Django project.


[AdminForm](https://github.com/django/django/blob/master/django/contrib/admin/helpers.py)
is a class within the django.contrib.admin.helpers module of the
[Django](/django.html) project. AdminForm is not usually used directly by
developers but can be used by libraries that want to extend the
[forms](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/admindocs/)
within the
[Django Admin](https://docs.djangoproject.com/en/stable/ref/contrib/admin/).


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / admin / placeholderadmin.py**](https://github.com/divio/django-cms/blob/develop/cms/admin/placeholderadmin.py)

```python
# placeholderadmin.py
import uuid
import warnings

from django.conf.urls import url
~~from django.contrib.admin.helpers import AdminForm
from django.contrib.admin.utils import get_deleted_objects
from django.core.exceptions import PermissionDenied
from django.db import router, transaction
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_text
from django.utils import translation
from django.utils.translation import ugettext as _
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.http import require_POST

from six.moves.urllib.parse import parse_qsl, urlparse

from six import get_unbound_function, get_method_function

from cms import operations


## ... source file abbreviated to get to AdminForm examples ...


        saved_successfully = False
        cancel_clicked = request.POST.get("_cancel", False)
        raw_fields = request.GET.get("edit_fields")
        fields = [field for field in raw_fields.split(",") if field in self.frontend_editable_fields]
        if not fields:
            context = {
                'opts': opts,
                'message': force_text(_("Field %s not found")) % raw_fields
            }
            return render(request, 'admin/cms/page/plugin/error_form.html', context)
        if not request.user.has_perm("{0}.change_{1}".format(self.model._meta.app_label,
                                                             self.model._meta.model_name)):
            context = {
                'opts': opts,
                'message': force_text(_("You do not have permission to edit this item"))
            }
            return render(request, 'admin/cms/page/plugin/error_form.html', context)
        form_class = self.get_form(request, obj, fields=fields)
        if not cancel_clicked and request.method == 'POST':
            form = form_class(instance=obj, data=request.POST)
            if form.is_valid():
                form.save()
                saved_successfully = True
        else:
            form = form_class(instance=obj)
~~        admin_form = AdminForm(form, fieldsets=[(None, {'fields': fields})], prepopulated_fields={},
                               model_admin=self)
        media = self.media + admin_form.media
        context = {
            'CMS_MEDIA_URL': get_cms_setting('MEDIA_URL'),
            'title': opts.verbose_name,
            'plugin': None,
            'plugin_id': None,
            'adminform': admin_form,
            'add': False,
            'is_popup': True,
            'media': media,
            'opts': opts,
            'change': True,
            'save_as': False,
            'has_add_permission': False,
            'window_close_timeout': 10,
        }
        if cancel_clicked:
            context.update({
                'cancel': True,
            })
            return render(request, 'admin/cms/page/plugin/confirm_form.html', context)
        if not cancel_clicked and request.method == 'POST' and saved_successfully:
            return render(request, 'admin/cms/page/plugin/confirm_form.html', context)


## ... source file continues with no further AdminForm examples...

```

