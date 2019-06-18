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

[**django-oscar/src/oscar/apps/address/admin.py**](https://github.com/django-oscar/django-oscar/blob/master/src/oscar/apps/address/admin.py)

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

[**heritagesites/heritagesites/admin.py**](https://github.com/Michael-Cantley/heritagesites/blob/master/heritagesites/admin.py)

```python
# admin.py
~~from django.contrib import admin

import heritagesites.models as models


@admin.register(models.CountryArea)
class CountryAreaAdmin(admin.ModelAdmin):
    fields = [
        'country_area_name',
        # (
        #     'region',
        #     'sub_region',
        #     'intermediate_region'
        # ),
        'iso_alpha3_code',
        'm49_code',
        'location',
        'dev_status'
    ]

    list_display = [
        'country_area_name',
        # 'region',
        # 'sub_region',
        # 'intermediate_region',
        'location',
        'iso_alpha3_code',
        'm49_code',
        'dev_status'
    ]

    list_filter = ['location', 'dev_status']

    # list_filter = ['location', 'dev_status'] list_filter = ['region', 'sub_region', 'intermediate_region', 'dev_status']

# admin.site.register(models.CountryArea)


@admin.register(models.DevStatus)
class DevStatusAdmin(admin.ModelAdmin):
    fields = ['dev_status_name']
    list_display = ['dev_status_name']
    ordering = ['dev_status_name']

# admin.site.register(models.DevStatus)


@admin.register(models.HeritageSite)
class HeritageSiteAdmin(admin.ModelAdmin):
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

# admin.site.register(models.HeritageSite)


@admin.register(models.HeritageSiteCategory)
class HeritageSiteCategoryAdmin(admin.ModelAdmin):
    fields = ['category_name']
    list_display = ['category_name']
    ordering = ['category_name']

# admin.site.register(models.HeritageSiteCategory)


@admin.register(models.IntermediateRegion)
class IntermediateRegionAdmin(admin.ModelAdmin):
    fields = ['intermediate_region_name', 'sub_region']
    list_display = ['intermediate_region_name', 'sub_region']
    ordering = ['intermediate_region_name']

# admin.site.register(models.IntermediateRegion)


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    fields = ['region_name', 'planet']
    list_display = ['region_name', 'planet']
    ordering = ['region_name', 'planet']

# admin.site.register(models.Region)


@admin.register(models.SubRegion)
class SubRegionAdmin(admin.ModelAdmin):
    fields = ['sub_region_name', 'region']
    list_display = ['sub_region_name', 'region']
    ordering = ['sub_region_name']

# admin.site.register(models.SubRegion)

@admin.register(models.Planet)
class Planet(admin.ModelAdmin):
    """
    New class added as a result of Mtg 5 database refactoring.
    """
    fields = ['planet_name', 'unsd_name']
    list_display = ['planet_name', 'unsd_name']
    ordering = ['planet_name', 'unsd_name']


@admin.register(models.Location)
class Location(admin.ModelAdmin):
    """
    New class added as a result of Mtg 5 database refactoring.
    """
    fields = ['planet', 'region', 'sub_region', 'intermediate_region']
    list_display = ['planet', 'region', 'sub_region', 'intermediate_region']
    ordering = ['planet', 'region', 'sub_region', 'intermediate_region']
```
