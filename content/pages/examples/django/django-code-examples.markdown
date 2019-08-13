title: Django Code Examples
category: page
slug: django-code-examples
sortorder: 50000
toc: False
sidebartitle: Django Code Examples
meta: Python code examples that show how to use the Django web application framework for many different situations.


[Django](/django.html) is a Python [web framework](/web-frameworks.html).

<a href="http://www.djangoproject.com/" style="border: none;"><img src="/img/logos/django.png" width="100%" alt="Official Django logo. Trademark Django Software Foundation." class="shot" style="margin-top:20px"></a>


## Django Example Projects
Part of Django's widespread adoption comes from its broad ecosystem of 
open source code libraries and example projects.

It's good to familiarize yourself with the following projects to 
learn what is available to you beyond the extensive 
"[batteries-included](https://www.quora.com/Why-does-Django-tout-itself-as-a-batteries-included-web-framework-when-you-have-to-manually-write-regexes-to-do-URL-routing)" 
code base. 

These projects, ordered alphabetically, are also helpful as example 
code for how to build your own applications.


### AuditLog
[Auditlog](https://github.com/jjkester/django-auditlog) 
([project documentation](https://django-auditlog.readthedocs.io/en/latest/))
is a [Django](/django.html) app that logs changes to Python objects,
similar to the Django admin's logs but with more details and
output formats. Auditlog's source code is provided as open source under the
[MIT license](https://github.com/jjkester/django-auditlog/blob/master/LICENSE).

Example code found in the AuditLog project:

* [django.contrib.admin.filters SimpleListFilter](/django-contrib-admin-filters-simplelistfilter-examples.html)
* [django.db.models DateTimeField](/django-db-models-datetimefield-examples.html)
* [django.utils.html format_html](/django-utils-html-format-html-examples.html)


### dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration 
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

dccnsys is shown on the following code example pages:

* [django.contrib.auth get_user_model](/django-contrib-auth-get-user-model-examples.html)
* [django.contrib.auth.decorators login_required](/django-contrib-auth-decorators-login-required-examples.html)
* [django.urls.path](/django-urls-path-examples.html)

### django-allauth
[django-allauth](https://github.com/pennersr/django-allauth) 
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the 
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).

Code used for examples from the django-allauth project:

* [django.conf.urls.url](/django-conf-urls-url-examples.html)
* [django.forms](/django-forms-examples.html)


### django-angular
[django-angular](https://github.com/jrief/django-angular) 
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use 
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is 
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

Code from django-angular is shown on:

* [django-conf-urls url](/django-conf-urls-url-examples.html)
* [django.conf settings](/django-conf-settings-examples.html)
* [django.utils.html format_html](/django-utils-html-format-html-examples.html)
* [django.urls.exceptions NoReverseMatch](/django-urls-exceptions-noreversematch-examples.html)


### django-cors-headers
[django-cors-headers](https://github.com/ottoyiu/django-cors-headers) is
an 
[open source](https://github.com/ottoyiu/django-cors-headers/blob/master/LICENSE)
library for enabling 
[Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) 
handling in your [Django](/django.html) web applications and appropriately
dealing with HTTP headers for CORS requests.

Code examples from the django-cors-headers project:

* [django.conf settings](/django-conf-settings-examples.html)
* [django.dispatch Signal](/django-dispatch-dispatcher-signal-examples.html)


### django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/) 
for use with Django web apps that is open sourced under the 
[BSD 3-Clause "New" License](https://github.com/divio/django-cms/blob/develop/LICENSE).

Example code from django-cms:

* [django.conf.urls url](/django-conf-urls-url-examples.html)
* [django.db.models Model](/django-db-models-model-examples.html)
* [django.utils timezone](/django-utils-timezone-examples.html)


### django-easy-timezones
[django-easy-timezones](https://github.com/Miserlou/django-easy-timezones)
([project website](https://www.gun.io/blog/django-easy-timezones))
is a Django
[middleware](https://docs.djangoproject.com/en/2.2/topics/http/middleware/)
[code library](https://pypi.org/project/django-easy-timezones/)
to simplify handling time data in your applications using
users' geolocation data.

Useful example code found within django-easy-timezones:

* [django.conf settings](/django-conf-settings-examples.html)
* [django.dispatch Signal](/django-dispatch-dispatcher-signal-examples.html)
* [django.utils.timezone](/django-utils-timezone-examples.html)


### django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images 
in Django's admin interface. The project's code is available under the 
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

Code from django-filer can be found on these pages:

* [django.conf settings](/django-conf-settings-examples.html)
* [django.contrib.admin](/django-contrib-admin-examples.html)
* [django.core.management.base BaseCommand](/django-core-management-base-basecommand-examples.html)


### django-push-notifications
[django-push-notifications](https://github.com/jazzband/django-push-notifications)
is a [Django](/django.html) app for storing and interacting with
push notification services such as 
[Google's Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/)
and 
[Apple Notifications](https://developer.apple.com/notifications/).
The django-push-notification project's source code is available
open source under the 
[MIT license](https://github.com/jazzband/django-push-notifications/blob/master/LICENSE).

* [django.db.models Model](/django-db-models-model-examples.html)
* [django.db.models BooleanField](/django-db-models-booleanfield-examples.html)
* [django.db.models CharField](/django-db-models-charfield-examples.html)
* [django.db.models DateTimeField](/django-db-models-datetimefield-examples.html)


### django-oscar
[django-oscar](https://github.com/django-oscar/django-oscar/) 
([project website](http://oscarcommerce.com/))
is a framework for building e-commerce sites on top of 
[Django](/django.html). The code for the project is available open 
source under a 
[custom license written by Tangent Communications PLC](https://github.com/django-oscar/django-oscar/blob/master/LICENSE).

Further code examples from django-oscar:

* [django.contrib.admin](/django-contrib-admin-examples.html)
* [django.contrib.auth.decorators login_required](/django-contrib-auth-decorators-login-required-examples.html)


### django-smithy
[django-smithy](https://github.com/jamiecounsell/django-smithy) is
a [Django](/django.html) code library that allows users to send 
HTTP requests from the Django admin user interface. The code for
the project is open source under the 
[MIT license](https://github.com/jamiecounsell/django-smithy/blob/master/LICENSE).

Code examples from django-smithy are shown on the following pages:

* [django.utils timezone](/django-utils-timezone-examples.html)
* [django.db.models CharField](/django-db-models-charfield-examples.html)
* [django.db.models TextField](/django-db-models-textfield-examples.html)


### drf-action-serializer
[drf-action-serializer](https://github.com/gregschmit/drf-action-serializer)
is an extension for [Django REST Framework](/django-rest-framework-drf.html)
that makes it easier to configure specific serializers to use based on the
client's request action. For example, a list view should have one serializer
whereas the detail view would have a different serializer.

The project is open source under the 
[MIT license](https://github.com/gregschmit/drf-action-serializer/blob/master/LICENSE).

There are code examples from the drf-action-serializer project on the
following pages:

* [django.urls.path](/django-urls-path-examples.html)


### gadget-board
[gadget-board](https://github.com/mik4el/gadget-board) is a 
[Django](/django.html),
[Django REST Framework (DRF)](/django-rest-framework-drf.html) and
[Angular](/angular.html) web application that is open source under the 
[Apache2 license](https://github.com/mik4el/gadget-board/blob/master/LICENSE).

Additional example code found within gadget-board:

* [django.conf.urls url](/django-conf-urls-url-examples.html)
* [django.contrib admin](/django-contrib-admin-examples.html)
* [django.contrib.auth.hashers make_password](/django-contrib-auth-hashers-make-password-examples.html)


### register
[register](https://github.com/ORGAN-IZE/register) is a [Django](/django.html),
[Bootstrap](/bootstrap.html), [PostgreSQL](/postgresql.html) project that is
open source under the 
[GNU General Public License v3.0](https://github.com/ORGAN-IZE/register/blob/master/LICENSE).
This web application makes it easier for people to register as organ donors. 
You can see the application live at 
[https://register.organize.org/](https://register.organize.org/).

Useful example code from register can be found on:

* [django.conf.urls url](/django-conf-urls-url-examples.html)


### wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the 
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

Example code from wagtail shown on these pages:

* [django.conf.urls url](/django-conf-urls-url-examples.html)
* [django.http Http404](/django-http-http404-examples.html)

