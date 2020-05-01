title: django.conf.urls.url Example Code
category: page
slug: django-conf-urls-url-examples
sortorder: 500010055
toc: False
sidebartitle: django.conf.urls.url
meta: Python code examples for the url function within the django.conf.urls module of the Django project. 


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

[**gadget-board / web / gadget_board_backend / urls.py**](https://github.com/mik4el/gadget-board/blob/master/web/gadget_board_backend/urls.py)

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
~~    url(r'^backend/api-auth/', include('rest_framework.urls', 
~~        namespace='rest_framework')),
~~    url(r'^backend/api-token-auth/', obtain_jwt_token),
~~    url(r'^backend/api-token-refresh/', refresh_jwt_token),
~~    url(r'^backend/api/v1/', include(router.urls)),
~~    url(r'^backend/api/v1/', include(gadgets_router.urls)),
]
```


## Example 2 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the 
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail/wagtail/admin/urls/pages.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/admin/urls/pages.py)

```python
# pages.py
~~from django.conf.urls import url

from wagtail.admin.views import page_privacy, pages


app_name = 'wagtailadmin_pages'
urlpatterns = [
~~    url(r'^add/(\w+)/(\w+)/(\d+)/$', pages.create, name='add'),
~~    url(r'^add/(\w+)/(\w+)/(\d+)/preview/$',
~~        pages.PreviewOnCreate.as_view(), name='preview_on_add'),
~~    url(r'^usage/(\w+)/(\w+)/$', pages.content_type_use, 
~~        name='type_use'),

~~    url(r'^(\d+)/edit/$', pages.edit, name='edit'),
~~    url(r'^(\d+)/edit/preview/$', pages.PreviewOnEdit.as_view(), 
~~        name='preview_on_edit'),

~~    url(r'^(\d+)/view_draft/$', pages.view_draft, name='view_draft'),
~~    url(r'^(\d+)/add_subpage/$', pages.add_subpage, name='add_subpage'),
~~    url(r'^(\d+)/delete/$', pages.delete, name='delete'),
~~    url(r'^(\d+)/unpublish/$', pages.unpublish, name='unpublish'),

~~    url(r'^search/$', pages.search, name='search'),

~~    url(r'^(\d+)/move/$', pages.move_choose_destination, name='move'),
~~    url(r'^(\d+)/move/(\d+)/$', pages.move_choose_destination, 
~~        name='move_choose_destination'),
~~    url(r'^(\d+)/move/(\d+)/confirm/$', pages.move_confirm, 
~~        name='move_confirm'),
~~    url(r'^(\d+)/set_position/$', pages.set_page_position, 
~~        name='set_page_position'),

~~    url(r'^(\d+)/copy/$', pages.copy, name='copy'),

~~    url(r'^moderation/(\d+)/approve/$', pages.approve_moderation, 
~~        name='approve_moderation'),
~~    url(r'^moderation/(\d+)/reject/$', pages.reject_moderation, 
~~        name='reject_moderation'),
~~    url(r'^moderation/(\d+)/preview/$', pages.preview_for_moderation, 
~~        name='preview_for_moderation'),

~~    url(r'^(\d+)/privacy/$', page_privacy.set_privacy, 
~~        name='set_privacy'),

~~    url(r'^(\d+)/lock/$', pages.lock, name='lock'),
~~    url(r'^(\d+)/unlock/$', pages.unlock, name='unlock'),

~~    url(r'^(\d+)/revisions/$', pages.revisions_index, 
~~        name='revisions_index'),
~~    url(r'^(\d+)/revisions/(\d+)/view/$', pages.revisions_view, 
~~        name='revisions_view'),
~~    url(r'^(\d+)/revisions/(\d+)/revert/$', pages.revisions_revert, 
~~        name='revisions_revert'),
~~    url(r'^(\d+)/revisions/(\d+)/unschedule/$', pages.revisions_unschedule, 
~~        name='revisions_unschedule'),
~~    url(r'^(\d+)/revisions/compare/(live|earliest|\d+)\.\.\.(live|latest|\d+)/$', 
~~        pages.revisions_compare, name='revisions_compare'),
]
```


## Example 3 from register
[register](https://github.com/ORGAN-IZE/register) is a [Django](/django.html),
[Bootstrap](/bootstrap-css.html), [PostgreSQL](/postgresql.html) project that is
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
~~    django.conf.urls.url(r'^i18n/', 
~~      django.conf.urls.include('django.conf.urls.i18n')),
~~    django.conf.urls.url(r'^robots.txt$', 
~~                         django.views.generic.TemplateView.as_view(\
~~                           template_name='robots.txt')),
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


## Example 4 from django-allauth
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
~~    url(r"^password/set/$", views.password_set, 
~~        name="account_set_password"),

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
~~    url(r"^password/reset/key/done/$", 
~~        views.password_reset_from_key_done,
~~        name="account_reset_password_from_key_done"),
]
```


## Example 5 from django-cms
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


## Example 6 from apiserver
[apiserver](https://github.com/renjith-tring/apiserver) is a 
[RESTful web API](/application-programming-interfaces.html) server project
built with [Django](/django.html) for user management tasks such as 
registration (with email verification), login, logout and password changes.

[**apiserver / apps / accounts / urls.py**](https://github.com/renjith-tring/apiserver/blob/master/apps/accounts/urls.py)

```python
~~from django.conf.urls import url, include
from tastypie.api import Api
from apps.accounts.api import UserResource
from apps.accounts import signals

v1_api = Api(api_name='v1')
v1_api.register(UserResource())

urlpatterns = [
~~    url(r'^api/', include(v1_api.urls)),
~~    url(r'^reset/(?P<uidb36>[0-9A-Za-z_\-]+)/' + \
~~         '(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
~~        'reset_confirm', 
~~         name='password_reset_confirm'
~~        ),

~~    url(r'^accounts/password/reset/' + \
~~         '(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
~~        'django.contrib.auth.views.password_reset_confirm',
~~        {'post_reset_redirect': '/accounts/password/done/'},),
]
```


## Example 7 from django-angular
[django-angular](https://github.com/jrief/django-angular) 
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use 
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is 
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / urls.py**](https://github.com/jrief/django-angular/blob/master/djng/urls.py)

```python
import warnings
from django.urls import reverse
~~from django.conf.urls import url
from django.http.response import HttpResponsePermanentRedirect


warnings.warn("Reversing URL's using urlpatterns is deprecated. "
              "Please use the middleware instead", 
              DeprecationWarning)


def angular_reverse(request, *args, **kwargs):
    url_name = request.GET.get('djng_url_name')
    url_args = request.GET.getlist('djng_url_args', None)
    url_kwargs = {}

    prefix = 'djng_url_kwarg_'
    for param in request.GET:
        if param.startswith(prefix):
            url_kwargs[param[len(prefix):]] = request.GET[param]

    url = reverse(url_name, args=url_args, kwargs=url_kwargs)
    return HttpResponsePermanentRedirect(url)


urlpatterns = [
~~    url(r'^reverse/$', angular_reverse),
]
```
