title: django.contrib.admin Examples
category: page
slug: django-contrib-admin-examples
sortorder: 50001
toc: False
sidebartitle: django.contrib.admin
meta: Python code examples for the admin module within django.contrib of the Django project. 


# django.contrib.admin Examples
The [Django admin](https://docs.djangoproject.com/en/2.2/ref/contrib/admin/)
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
