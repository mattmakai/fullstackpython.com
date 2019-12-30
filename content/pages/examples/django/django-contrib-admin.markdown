title: django.contrib.admin Example Code
category: page
slug: django-contrib-admin-examples
sortorder: 500010155
toc: False
sidebartitle: django.contrib.admin
meta: Python code examples for the admin module within django.contrib of the Django project. 


The [Django admin](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)
is an automatically-generated user interface for [Django models](/django-orm.html).
The admin interface can be heavily customized and the code examples below can
help you understand how to implement some of the trickier parts of customization.


## Example 1 from django-oscar
[django-oscar](https://github.com/django-oscar/django-oscar/) 
([project website](http://oscarcommerce.com/))
is a framework for building e-commerce sites on top of 
[Django](/django.html). The code for the project is available open 
source under a 
[custom license written by Tangent Communications PLC](https://github.com/django-oscar/django-oscar/blob/master/LICENSE).

[**django-oscar / src / oscar / apps / address / admin.py**](https://github.com/django-oscar/django-oscar/blob/master/src/oscar/apps/address/admin.py)

```python
# admin.py
~~from django.contrib import admin

from oscar.core.loading import get_model


~~class UserAddressAdmin(admin.ModelAdmin):
~~    readonly_fields = ('num_orders_as_billing_address', 'num_orders_as_shipping_address')


~~class CountryAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'display_order'
    ]
    list_filter = [
        'is_shipping_country'
    ]
    search_fields = [
        'name',
        'printable_name',
        'iso_3166_1_a2',
        'iso_3166_1_a3'
    ]


~~admin.site.register(get_model('address', 'useraddress'), UserAddressAdmin)
~~admin.site.register(get_model('address', 'country'), CountryAdmin)
```


## Example 2 from heritagesites
[heritagesites](https://github.com/Michael-Cantley/heritagesites) is a
[Django](/django.html)-based web app with a [MySQL](/mysql.html)
backend that displays 
[UNESCO heritage sites](https://whc.unesco.org/en/list/). The project
code is open source under the 
[MIT license](https://github.com/Michael-Cantley/heritagesites/blob/master/LICENSE).

[**heritagesites / heritagesites / admin.py**](https://github.com/Michael-Cantley/heritagesites/blob/master/heritagesites/admin.py)

```python
# admin.py
~~from django.contrib import admin

import heritagesites.models as models


~~@admin.register(models.CountryArea)
~~class CountryAreaAdmin(admin.ModelAdmin):
    fields = [
        'country_area_name',
        'iso_alpha3_code',
        'm49_code',
        'location',
        'dev_status'
    ]

    list_display = [
        'country_area_name',
        'location',
        'iso_alpha3_code',
        'm49_code',
        'dev_status'
    ]

    list_filter = ['location', 'dev_status']


~~@admin.register(models.DevStatus)
~~class DevStatusAdmin(admin.ModelAdmin):
    fields = ['dev_status_name']
    list_display = ['dev_status_name']
    ordering = ['dev_status_name']


~~@admin.register(models.HeritageSite)
~~class HeritageSiteAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'site_name',
                'heritage_site_category',
                'description',
                'justification',
                'date_inscribed'
            )
        }),
        ('Location and Area', {
            'fields': [
                (
                    'longitude',
                    'latitude'
                ),
                'area_hectares',
                'transboundary'
            ]
        })
    )

    list_display = (
        'site_name',
        'date_inscribed',
        'area_hectares',
        'heritage_site_category',
        'country_area_display'
    )

    list_filter = (
        'heritage_site_category',
        'date_inscribed'
    )


~~@admin.register(models.HeritageSiteCategory)
~~class HeritageSiteCategoryAdmin(admin.ModelAdmin):
    fields = ['category_name']
    list_display = ['category_name']
    ordering = ['category_name']


~~@admin.register(models.IntermediateRegion)
~~class IntermediateRegionAdmin(admin.ModelAdmin):
    fields = ['intermediate_region_name', 'sub_region']
    list_display = ['intermediate_region_name', 'sub_region']
    ordering = ['intermediate_region_name']


~~@admin.register(models.Region)
~~class RegionAdmin(admin.ModelAdmin):
    fields = ['region_name', 'planet']
    list_display = ['region_name', 'planet']
    ordering = ['region_name', 'planet']


~~@admin.register(models.SubRegion)
~~class SubRegionAdmin(admin.ModelAdmin):
    fields = ['sub_region_name', 'region']
    list_display = ['sub_region_name', 'region']
    ordering = ['sub_region_name']


~~@admin.register(models.Planet)
~~class Planet(admin.ModelAdmin):
    """New class added as a result of Mtg 5 database refactoring.
    """
    fields = ['planet_name', 'unsd_name']
    list_display = ['planet_name', 'unsd_name']
    ordering = ['planet_name', 'unsd_name']


~~@admin.register(models.Location)
~~class Location(admin.ModelAdmin):
    """New class added as a result of Mtg 5 database refactoring.
    """
    fields = ['planet', 'region', 'sub_region', 'intermediate_region']
    list_display = ['planet', 'region', 'sub_region', 'intermediate_region']
    ordering = ['planet', 'region', 'sub_region', 'intermediate_region']
```


## Example 3 from viewflow
[viewflow](https://github.com/viewflow/viewflow) 
([project website](http://viewflow.io/)) is a reusable workflow
code library for organizing business logic in complex web applications.
The code for the project is available under the 
[GNU Alfredo license](https://github.com/viewflow/viewflow/blob/master/LICENSE).

[**viewflow / viewflow / admin.py**](https://github.com/viewflow/viewflow/blob/master/viewflow/admin.py)

```python
# admin.py
~~from django.contrib import admin, auth
from viewflow.models import Process, Task


~~class TaskInline(admin.TabularInline):
    """Task inline."""

    model = Task
    fields = ['flow_task', 'flow_task_type', 'status',
              'token', 'owner']
    readonly_fields = ['flow_task', 'flow_task_type', 'status', 
                       'token']

    def has_add_permission(self, request):
        """Disable manually task creation."""
        return False

    def has_delete_permission(self, request, obj=None):
        """Disable task deletion in the process inline."""
        return False


~~class ProcessAdmin(admin.ModelAdmin):
    """List all of viewflow process."""

    icon = '<i class="material-icons">assignment</i>'

    actions = None
    date_hierarchy = 'created'
    list_display = ['pk', 'created', 'flow_class', 'status', 
                    'participants']
    list_display_links = ['pk', 'created', 'flow_class']
    list_filter = ['status']
    readonly_fields = ['flow_class', 'status', 'finished']
    inlines = [TaskInline]

    def has_add_permission(self, request):
        """Disable manually process creation."""
        return False

    def participants(self, obj):
        """List of users performed tasks on the process."""
        user_ids = obj.task_set.exclude(owner__isnull=True).\
                   values('owner')
        USER_MODEL = auth.get_user_model()
        username_field = USER_MODEL.USERNAME_FIELD
        users = USER_MODEL._default_manager.filter(pk__in=user_ids).\
                values_list(username_field)
        return ', '.join(user[0] for user in users)


~~class TaskAdmin(admin.ModelAdmin):
    """List all of viewflow tasks."""

    icon = '<i class="material-icons">assignment_turned_in</i>'

    actions = None
    date_hierarchy = 'created'
    list_display = ['pk', 'created', 'process', 'status',
                    'owner', 'owner_permission', 'token',
                    'started', 'finished']
    list_display_links = ['pk', 'created', 'process']
    list_filter = ['status']
    readonly_fields = ['process', 'status', 'flow_task', 'started', 
                       'finished', 'previous', 'token']

    def has_add_permission(self, request):
        """Disable manually task creation."""
        return False


~~admin.site.register(Process, ProcessAdmin)
~~admin.site.register(Task, TaskAdmin)
```


## Example 4 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and 
images in Django's admin interface. 

The project's code is available under the 
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / admin / fileadmin.py**](https://github.com/divio/django-filer/blob/develop/filer/admin/fileadmin.py)

```python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django import forms
from django.contrib.admin.utils import unquote
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

from .. import settings
from ..models import File
~~from .permissions import PrimitivePermissionAwareModelAdmin
~~from .tools import AdminContext, admin_url_params_encoded, popup_status


~~class FileAdminChangeFrom(forms.ModelForm):
    class Meta(object):
        model = File
        exclude = ()


~~class FileAdmin(PrimitivePermissionAwareModelAdmin):
    list_display = ('label',)
    list_per_page = 10
    search_fields = ['name', 'original_filename', 'sha1', 'description']
    raw_id_fields = ('owner',)
    readonly_fields = ('sha1', 'display_canonical')

    form = FileAdminChangeFrom

    @classmethod
    def build_fieldsets(cls, extra_main_fields=(), extra_advanced_fields=(),
                        extra_fieldsets=()):
        fieldsets = (
            (None, {
                'fields': (
                    'name',
                    'owner',
                    'description',
                ) + extra_main_fields,
            }),
            (_('Advanced'), {
                'fields': (
                    'file',
                    'sha1',
                    'display_canonical',
                ) + extra_advanced_fields,
                'classes': ('collapse',),
            }),
        ) + extra_fieldsets
        if settings.FILER_ENABLE_PERMISSIONS:
            fieldsets = fieldsets + (
                (None, {
                    'fields': ('is_public',)
                }),
            )
        return fieldsets

    def response_change(self, request, obj):
        """
        Overrides the default to be able to forward to the directory listing
        instead of the default change_list_view
        """
        if (
            request.POST
            and '_continue' not in request.POST
            and '_saveasnew' not in request.POST
            and '_addanother' not in request.POST
        ):
            # Popup in pick mode or normal mode. In both cases we want to go
            # back to the folder list view after save. And not the useless file
            # list view.
            if obj.folder:
                url = reverse('admin:filer-directory_listing',
                              kwargs={'folder_id': obj.folder.id})
            else:
                url = reverse(
                    'admin:filer-directory_listing-unfiled_images')
            url = "{0}{1}".format(
                url,
                admin_url_params_encoded(request),
            )
            return HttpResponseRedirect(url)
        return super(FileAdmin, self).response_change(request, obj)

    def render_change_form(self, request, context, add=False, change=False,
                           form_url='', obj=None):
        info = self.model._meta.app_label, self.model._meta.model_name
        extra_context = {'show_delete': True,
                         'history_url': 'admin:%s_%s_history' % info,
                         'is_popup': popup_status(request),
                         'filer_admin_context': AdminContext(request)}
        context.update(extra_context)
        return super(FileAdmin, self).render_change_form(
            request=request, context=context, add=add, change=change,
            form_url=form_url, obj=obj)

    def delete_view(self, request, object_id, extra_context=None):
        """
        Overrides the default to enable redirecting to the directory view after
        deletion of a image.
        we need to fetch the object and find out who the parent is
        before super, because super will delete the object and make it
        impossible to find out the parent folder to redirect to.
        """
        try:
            obj = self.get_queryset(request).get(pk=unquote(object_id))
            parent_folder = obj.folder
        except self.model.DoesNotExist:
            parent_folder = None

        if request.POST:
            # Return to folder listing, since there is no usable file listing.
            super(FileAdmin, self).delete_view(
                request=request, object_id=object_id,
                extra_context=extra_context)
            if parent_folder:
                url = reverse('admin:filer-directory_listing',
                              kwargs={'folder_id': parent_folder.id})
            else:
                url = reverse('admin:filer-directory_listing-unfiled_images')
            url = "{0}{1}".format(
                url,
                admin_url_params_encoded(request)
            )
            return HttpResponseRedirect(url)

        return super(FileAdmin, self).delete_view(
            request=request, object_id=object_id,
            extra_context=extra_context)

    def get_model_perms(self, request):
        """
        It seems this is only used for the list view. NICE :-)
        """
        return {
            'add': False,
            'change': False,
            'delete': False,
        }

    def display_canonical(self, instance):
        canonical = instance.canonical_url
        if canonical:
            return mark_safe('<a href="%s">%s</a>' % (canonical, canonical))
        else:
            return '-'
    display_canonical.allow_tags = True
    display_canonical.short_description = _('canonical URL')


~~FileAdmin.fieldsets = FileAdmin.build_fieldsets()
```


## Example 5 from gadget-board
[gadget-board](https://github.com/mik4el/gadget-board) is a 
[Django](/django.html),
[Django REST Framework (DRF)](/django-rest-framework-drf.html) and
[Angular](/angular.html) web application that is open source under the 
[Apache2 license](https://github.com/mik4el/gadget-board/blob/master/LICENSE).

[**gadget-board / web / authentication / admin.py**](https://github.com/mik4el/gadget-board/blob/master/web/authentication/admin.py)

```python
~~from django.contrib import admin
from .models import Account


~~@admin.register(Account)
~~class AccountAdmin(admin.ModelAdmin):
	readonly_fields = ('created_at','updated_at',)
```
