title: django.conf.urls.url Examples
category: page
slug: django-conf-urls-url-examples
sortorder: 50001
toc: False
sidebartitle: django.conf.urls.url Examples
meta: Python code examples for the url function within the django.conf.urls module of the Django project. 


# django.conf.urls.url Examples
The [url](https://github.com/django/django/blob/master/django/conf/urls/__init__.py)
function is contained with the 
[django.conf.urls](https://github.com/django/django/tree/master/django/conf/urls) 
module within the [Django project](/django.html) code base. 

`url` relies on Django's 
[URL dispatcher](https://docs.djangoproject.com/en/dev/topics/http/urls/) 
functionality and is used for mapping URLs to matching view functions within 
a Django app.


## Example 1 from gadget-board
[gadget-board](https://github.com/mik4el/gadget-board) is a [Django](/django.html),
[Django REST Framework (DRF)](/django-rest-framework-drf.html) and
[Angular](/angular.html) web application that is open source under the 
[Apache2 license](https://github.com/mik4el/gadget-board/blob/master/LICENSE).

[**gadget-board/web/gadget_board_backend/urls.py**](https://github.com/mik4el/gadget-board/blob/master/web/gadget_board_backend/urls.py)

```python
from django.contrib import admin
~~from django.conf.urls import url, include
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


## Example 2 from register
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


## Example 3 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth) 
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the 
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).

[**django-allauth/allauth/account/urls.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/account/urls.py)

```python
from . import views

~~from django.conf.urls import url


urlpatterns = [
~~    url(r"^signup/$", views.signup, name="account_signup"),
~~    url(r"^login/$", views.login, name="account_login"),
~~    url(r"^logout/$", views.logout, name="account_logout"),

~~    url(r"^password/change/$", views.password_change,
~~        name="account_change_password"),
~~    url(r"^password/set/$", views.password_set, name="account_set_password"),

~~    url(r"^inactive/$", views.account_inactive, name="account_inactive"),

    # E-mail
~~    url(r"^email/$", views.email, name="account_email"),
~~    url(r"^confirm-email/$", views.email_verification_sent,
~~        name="account_email_verification_sent"),
~~    url(r"^confirm-email/(?P<key>[-:\w]+)/$", views.confirm_email,
~~        name="account_confirm_email"),

    # password reset
~~    url(r"^password/reset/$", views.password_reset,
~~        name="account_reset_password"),
~~    url(r"^password/reset/done/$", views.password_reset_done,
~~        name="account_reset_password_done"),
~~    url(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
~~        views.password_reset_from_key,
~~        name="account_reset_password_from_key"),
~~    url(r"^password/reset/key/done/$", views.password_reset_from_key_done,
~~        name="account_reset_password_from_key_done"),
]
```


## Example 4 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/) 
for use with Django web apps that is open sourced under the 
[BSD 3-Clause "New" License](https://github.com/divio/django-cms/blob/develop/LICENSE).

[**django-cms/cms/urls.py**](https://github.com/divio/django-cms/blob/develop/cms/urls.py)

```python
# -*- coding: utf-8 -*-
from django.conf import settings
~~from django.conf.urls import include, url

from cms import views
from cms.apphook_pool import apphook_pool
from cms.appresolver import get_app_patterns
from cms.constants import SLUG_REGEXP


if settings.APPEND_SLASH:
    regexp = r'^(?P<slug>%s)/$' % SLUG_REGEXP
else:
    regexp = r'^(?P<slug>%s)$' % SLUG_REGEXP

if apphook_pool.get_apphooks():
    # If there are some application urls, use special resolver,
    # so we will have standard reverse support.
    urlpatterns = get_app_patterns()
else:
    urlpatterns = []


urlpatterns.extend([
~~    url(r'^cms_login/$', views.login, name='cms_login'),
~~    url(r'^cms_wizard/', include('cms.wizards.urls')),
~~    url(regexp, views.details, name='pages-details-by-slug'),
~~    url(r'^$', views.details, {'slug': ''}, name='pages-root'),
])
```
