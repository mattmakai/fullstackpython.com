title: django.urls.path Example Code
category: page
slug: django-urls-path-examples
sortorder: 500013610
toc: False
sidebartitle: django.urls.path
meta: Python code examples for the path function within the django.urls module of the Django project. 


The [path](https://github.com/django/django/blob/master/django/urls/conf.py) 
function is contained with the 
[django.urls](https://github.com/django/django/tree/master/django/urls) 
module within the [Django project](/django.html) code base. 

`path` is used for routing URLs to the appropriate view functions within 
a Django application using the
[URL dispatcher](https://docs.djangoproject.com/en/dev/topics/http/urls/).


## Example 1 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration 
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys/wwwdccn/wwwdccn/urls.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/wwwdccn/urls.py)

```python
from django.conf import settings
from django.conf.urls.static import static
~~from django.urls import path, include

urlpatterns = [
~~    path('', include('public_site.urls')),
~~    path('user/', include('user_site.urls')),
~~    path('auth/', include('auth_app.urls')),
~~    path('users/', include('users.urls')),
~~    path('registration/', include('registration.urls')),
~~    path('conferences/', include('conferences.urls')),
~~    path('submissions/', include('submissions.urls')),
~~    path('chair/', include('chair.urls')),
]

if settings.USE_LOCAL_MEDIA:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.USE_DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
```


## Example 2 from heritagesites
[heritagesites](https://github.com/Michael-Cantley/heritagesites) is a
[Django](/django.html) web application with a [MySQL](/mysql.html)
backend that displays 
[UNESCO heritage sites](https://whc.unesco.org/en/list/). The project
code is open source under the 
[MIT license](https://github.com/Michael-Cantley/heritagesites/blob/master/LICENSE).

[**heritagesites / heritagesites / urls.py**](https://github.com/Michael-Cantley/heritagesites/blob/master/heritagesites/urls.py)

```python
# urls.py
~~from django.urls import path, re_path
from . import views


urlpatterns = [
~~    path('', views.HomePageView.as_view(), name='home'),
~~    path('about/', views.AboutPageView.as_view(), name='about'),
~~    path('countries/', views.CountryAreaListView.as_view(), name='country_area'),
~~    path('countries/<int:pk>/', views.CountryAreaDetailView.as_view(), 
           name='country_area_detail'),
~~    path('sites/', views.SiteListView.as_view(), name='sites'),
~~    path('sites/<int:pk>/', views.SiteDetailView.as_view(), name='site_detail'),

~~    path('sites/new/', views.SiteCreateView.as_view(), name='site_new'),
~~    path('sites/<int:pk>/delete/', views.SiteDeleteView.as_view(), name='site_delete'),
~~    path('sites/<int:pk>/update/', views.SiteUpdateView.as_view(), name='site_update'),

~~    path('sites/search', views.SiteFilterView.as_view(), name="search")
]
```

## Example 3 from drf-action-serializer
[drf-action-serializer](https://github.com/gregschmit/drf-action-serializer)
is an extension for [Django REST Framework](/django-rest-framework-drf.html)
that makes it easier to configure specific serializers to use based on the
client's request action. For example, a list view should have one serializer
whereas the detail view would have a different serializer.

The project is open source under the 
[MIT license](https://github.com/gregschmit/drf-action-serializer/blob/master/LICENSE).

[**drf-action-serializer / action_serializer / urls.py**](https://github.com/gregschmit/drf-action-serializer/blob/master/action_serializer/urls.py)

```python
from django.contrib import admin
~~from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .sample_group_viewset import GroupViewSet


router = DefaultRouter()
router.register('auth/group', GroupViewSet)
router.register('auth/groups', GroupViewSet)

urlpatterns = [
~~    path('api/', include(router.urls)),
~~    path('admin/doc/', include('django.contrib.admindocs.urls')),
~~    path('admin/', admin.site.urls),
]
```
