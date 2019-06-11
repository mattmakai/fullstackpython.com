title: django.urls.path Examples
category: page
slug: django-urls-path-examples
sortorder: 5000
toc: False
sidebartitle: django.urls.path Examples
meta: Python code examples for the path function within the django.urls module of the Django project. 


# django.urls.path Examples
The [path](https://github.com/django/django/blob/master/django/urls/conf.py) function 
is contained with the 
[django.urls](https://github.com/django/django/tree/master/django/urls) module within
the [Django project](/django.html) code base.


## Example 1 from gadget-board
[gadget-board](https://github.com/mik4el/gadget-board) is a [Django](/django.html),
[Django REST Framework (DRF)](/django-rest-framework-drf.html) and
[Angular](/angular.html) web application that is open source under the 
[Apache2 license](https://github.com/mik4el/gadget-board/blob/master/LICENSE).

[**gadget-board/web/gadget_board_backend/urls.py**](https://github.com/mik4el/gadget-board/blob/master/web/gadget_board_backend/urls.py)

```python
from django.conf.urls import url, include
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
    url(r'^backend/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^backend/api-token-auth/', obtain_jwt_token),
    url(r'^backend/api-token-refresh/', refresh_jwt_token),
    url(r'^backend/api/v1/', include(router.urls)),
    url(r'^backend/api/v1/', include(gadgets_router.urls)),
]
```


## Example 2 from gadget-board
