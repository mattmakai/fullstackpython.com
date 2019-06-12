title: django.urls.path Examples
category: page
slug: django-urls-path-examples
sortorder: 5000
toc: False
sidebartitle: django.urls.path Examples
meta: Python code examples for the path function within the django.urls module of the Django project. 


# django.urls.path Examples
The [path](https://github.com/django/django/blob/master/django/urls/conf.py) 
function is contained with the 
[django.urls](https://github.com/django/django/tree/master/django/urls) 
module within the [Django project](/django.html) code base. 

`path` is used for routing URLs to the appropriate view functions within 
a Django application using the
[URL dispatcher](https://docs.djangoproject.com/en/dev/topics/http/urls/).


## Example 1 from gadget-board
[gadget-board](https://github.com/mik4el/gadget-board) is a [Django](/django.html),
[Django REST Framework (DRF)](/django-rest-framework-drf.html) and
[Angular](/angular.html) web application that is open source under the 
[Apache2 license](https://github.com/mik4el/gadget-board/blob/master/LICENSE).

[**gadget-board/web/gadget_board_backend/urls.py**](https://github.com/mik4el/gadget-board/blob/master/web/gadget_board_backend/urls.py)

```python
~~from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_nested import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token

from authentication.views import AccountViewSet
from gadgets.views import GadgetViewSet, GadgetDataViewSet

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'gadgets', GadgetViewSet)
gadgets_router = routers.NestedSimpleRouter(router, r'gadgets', lookup='gadget')
gadgets_router.register(r'data', GadgetDataViewSet, base_name='gadgets-data')

urlpatterns = [
~~    url(r'^backend/admin/', admin.site.urls),
~~    url(r'^backend/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
~~    url(r'^backend/api-token-auth/', obtain_jwt_token),
~~    url(r'^backend/api-token-refresh/', refresh_jwt_token),
~~    url(r'^backend/api/v1/', include(router.urls)),
~~    url(r'^backend/api/v1/', include(gadgets_router.urls)),
]
```


## Example 2 from ORGAN-IZE/register
[register](https://github.com/ORGAN-IZE/register) is a [Django](/django.html),
[Bootstrap](/bootstrap.html), [PostgreSQL](/postgresql.html) project that is
open source under the 
[GNU General Public License v3.0](https://github.com/ORGAN-IZE/register/blob/master/LICENSE).
This web application makes it easier for people to register as organ donors. 
You can see the application live at 
[https://register.organize.org/](https://register.organize.org/).

[**ORGAN-IZE/register/urls.py**](https://github.com/ORGAN-IZE/register/blob/master/urls.py)

```python
from __future__ import unicode_literals

~~import django.conf
~~import django.conf.urls
import django.views.generic
import django.contrib.auth.urls
import django.conf
import django.conf.urls.static
import django.conf.urls.i18n
import django.contrib.admin
from django.contrib.auth import views


urlpatterns = [
~~    django.conf.urls.url(r'^i18n/', django.conf.urls.include('django.conf.urls.i18n')),
~~    django.conf.urls.url(r'^robots.txt$', 
~~                         django.views.generic.TemplateView.as_view(template_name='robots.txt')),
~~    django.conf.urls.url(r'^', django.conf.urls.include('registration.urls')),
~~    django.conf.urls.url(r'^brand/', django.conf.urls.include('cobrand.urls')),
~~    django.conf.urls.url(r'^admin/', django.conf.urls.include(django.contrib.admin.site.urls)),

    # override the admin password reset flow to use the normal site password
    # reset flow
~~    django.conf.urls.url(r'^password_reset/$', views.password_reset, 
~~                         name='admin_password_reset'),
~~    django.conf.urls.url(r'^login/$', 
~~                         django.views.generic.RedirectView.as_view(url='/admin/login')),
~~    django.conf.urls.url(r'^', django.conf.urls.include('accountsplus.urls')),
~~    django.conf.urls.url(r'^widget/', django.conf.urls.include('widget.urls')),
]

## ... the source file continues here without any further examples
```

