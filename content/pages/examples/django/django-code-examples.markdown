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

* [django.apps.config AppConfig](/django-apps-config-appconfig-examples.html)
* [django.contrib.admin.filters SimpleListFilter](/django-contrib-admin-filters-simplelistfilter-examples.html)
* [django.contrib.admin.sites.register](/django-contrib-admin-sites-register-examples.html)
* [django.db.models DateField](/django-db-models-datefield-examples.html)
* [django.db.models DateTimeField](/django-db-models-datetimefield-examples.html)
* [django.db.models IntegerField](/django-db-models-integerfield-examples.html)
* [django.utils.html format_html](/django-utils-html-format-html-examples.html)


### dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration 
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

dccnsys is shown on the following code example pages:

* [django.apps.config AppConfig](/django-apps-config-appconfig-examples.html)
* [django.contrib.auth get_user_model](/django-contrib-auth-get-user-model-examples.html)
* [django.contrib.auth.decorators login_required](/django-contrib-auth-decorators-login-required-examples.html)
* [django.db.models DateField](/django-db-models-datefield-examples.html)
* [django.db.models IntegerField](/django-db-models-integerfield-examples.html)
* [django.http HttpResponseForbidden](/django-http-httpresponseforbidden-examples.html)
* [django.urls.path](/django-urls-path-examples.html)


### django-allauth
[django-allauth](https://github.com/pennersr/django-allauth) 
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the 
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).

Code used for examples from the django-allauth project:

* [django.apps.config AppConfig](/django-apps-config-appconfig-examples.html)
* [django.conf.urls.url](/django-conf-urls-url-examples.html)
* [django.contrib.admin.sites.register](/django-contrib-admin-sites-register-examples.html)
* [django.forms](/django-forms-examples.html)


### django-angular
[django-angular](https://github.com/jrief/django-angular) 
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use 
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is 
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

Code from django-angular is shown on:

* [django.conf.urls url](/django-conf-urls-url-examples.html)
* [django.conf settings](/django-conf-settings-examples.html)
* [django.http HttpResponseBadRequest](/django-http-httpresponsebadrequest-examples.html)
* [django.http HttpResponseForbidden](/django-http-httpresponseforbidden-examples.html)
* [django.http HttpResponsePermanentRedirect](/django-http-responses-httpresponsepermanentredirect-examples.html)
* [django.utils.html format_html](/django-utils-html-format-html-examples.html)
* [django.urls.exceptions NoReverseMatch](/django-urls-exceptions-noreversematch-examples.html)


### django-axes
[django-axes](https://github.com/jazzband/django-axes/)
([project documentation](https://django-axes.readthedocs.io/en/latest/)
and 
[PyPI package information](https://pypi.org/project/django-axes/)
is a code library for [Django](/django.html) projects to track failed
login attempts against a web application. The goal of the project is
to make it easier for you to stop people and scripts from hacking your
Django-powered website.

The code for django-axes is
[open source under the MIT liense](https://github.com/jazzband/django-axes/blob/master/LICENSE)
and maintained by the group of developers known as
[Jazzband](https://jazzband.co/).


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
* [django.contrib.admin.sites.register](/django-contrib-admin-sites-register-examples.html)
* [django.db OperationalError](/django-db-operationalerror-examples.html)
* [django.db.models Model](/django-db-models-model-examples.html)
* [django.http HttpResponseBadRequest](/django-http-httpresponsebadrequest-examples.html)
* [django.http HttpResponseForbidden](/django-http-httpresponseforbidden-examples.html)
* [django.template.response TemplateResponse](/django-template-response-templateresponse-examples.html)
* [django.utils timezone](/django-utils-timezone-examples.html)


### django-debug-toolbar
[django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)
([project documentation](https://github.com/jazzband/django-debug-toolbar)
and [PyPI page](https://pypi.org/project/django-debug-toolbar/))
grants a developer detailed request-response cycle information while
developing a [Django](/django.html) web application.
The code for django-debug-toolbar is
[open source](https://github.com/jazzband/django-debug-toolbar/blob/master/LICENSE)
and maintained by the developer community group known as
[Jazzband](https://jazzband.co/).


### django-easy-timezones
[django-easy-timezones](https://github.com/Miserlou/django-easy-timezones)
([project website](https://www.gun.io/blog/django-easy-timezones))
is a Django
[middleware](https://docs.djangoproject.com/en/stable/topics/http/middleware/)
[code library](https://pypi.org/project/django-easy-timezones/)
to simplify handling time data in your applications using
users' geolocation data.

Useful example code found within django-easy-timezones:

* [django.conf settings](/django-conf-settings-examples.html)
* [django.dispatch Signal](/django-dispatch-dispatcher-signal-examples.html)
* [django.utils.timezone](/django-utils-timezone-examples.html)


### django-extensions
[django-extensions](https://github.com/django-extensions/django-extensions)
([project documentation](https://django-extensions.readthedocs.io/en/latest/)
and [PyPI page](https://pypi.org/project/django-extensions/))
is a [Django](/django.html) project that adds a bunch of additional
useful commands to the `manage.py` interface. This 
[GoDjango video](https://www.youtube.com/watch?v=1F6G3ONhr4k) provides a 
quick overview of what you get when you install it into your Python
environment.

The django-extensions project is open sourced under the
[MIT license](https://github.com/django-extensions/django-extensions/blob/master/LICENSE).


### django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images 
in Django's admin interface. The project's code is available under the 
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

Code from django-filer can be found on these pages:

* [django.conf settings](/django-conf-settings-examples.html)
* [django.contrib.admin](/django-contrib-admin-examples.html)
* [django.contrib.admin.sites.register](/django-contrib-admin-sites-register-examples.html)
* [django.core.management.base BaseCommand](/django-core-management-base-basecommand-examples.html)
* [django.http HttpResponseBadRequest](/django-http-httpresponsebadrequest-examples.html)


### django-floppyforms
[django-floppyforms](https://github.com/jazzband/django-floppyforms)
([project documentation](https://django-floppyforms.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-floppyforms/))
is a [Django](/django.html) code library for better control
over rendering HTML forms in your [templates](/template-engines.html).

The django-floppyforms code is provided as
[open source](https://github.com/jazzband/django-floppyforms/blob/master/LICENSE)
and maintained by the collaborative developer community group 
[Jazzband](https://jazzband.co/).

Code from django-floppyforms is used as examples for the following parts of
Django:

* [django.db.models DateField](/django-db-models-datefield-examples.html)


### django-guardian
[django-guardian](https://github.com/django-guardian/django-guardian)
([project documentation](https://django-guardian.readthedocs.io/en/stable/)
and
[PyPI page](https://pypi.org/project/django-guardian/))
provides per-object permissions in [Django](/django.html) projects 
by enhancing the existing authentication backend. The project's code
is open source under the 
[MIT license](https://github.com/django-guardian/django-guardian/blob/devel/LICENSE).


### django-haystack
[django-haystack](https://github.com/django-haystack/django-haystack)
([project website](http://haystacksearch.org/) and 
[PyPI page](https://pypi.org/project/django-haystack/))
is a search abstraction layer that separates the Python search code
in a [Django](/django.html) web application from the search engine 
implementation that it runs on, such as 
[Apache Solr](http://lucene.apache.org/solr/), 
[Elasticsearch](https://www.elastic.co/)
or [Whoosh](https://whoosh.readthedocs.io/en/latest/intro.html).

The django-haystack project is open source under the
[BSD license](https://github.com/django-haystack/django-haystack/blob/master/LICENSE).


### django-jet
[django-jet](https://github.com/geex-arts/django-jet) 
([project documentation](https://jet.readthedocs.io/en/latest/),
[PyPI project page](https://pypi.org/project/django-jet/) and
[more information](http://jet.geex-arts.com/))
is a fancy [Django](/django.html) Admin panel replacement.

The django-jet project is open source under the
[GNU Affero General Public License v3.0](https://github.com/geex-arts/django-jet/blob/dev/LICENSE).


### django-jsonfield
[django-jsonfield](https://github.com/dmkoch/django-jsonfield) 
([jsonfield on PyPi](https://pypi.org/project/jsonfield/)) is a
[Django](/django.html) code library that makes it easier to store validated
JSON in a [Django object-relational mapper (ORM)](/django-orm.html) database 
model.

The django-jsonfield project is open source under the 
[MIT license](https://github.com/dmkoch/django-jsonfield/blob/master/LICENSE).


### django-model-utils
[django-model-utils](https://github.com/jazzband/django-model-utils)
([project documentation](https://django-model-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-model-utils/))
provides useful mixins and utilities for working with 
[Django ORM](/django-orm.html) models in your projects.

The django-model-utils project is open sourced under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/jazzband/django-model-utils/blob/master/LICENSE.txt)
and it is maintained by the developer community group 
[Jazzband](https://jazzband.co/).


### django-mongonaut
[django-mongonaut](https://github.com/jazzband/django-mongonaut)
([project documentation](https://django-mongonaut.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-mongonaut/))
provides an introspective interface for working with 
[MongoDB](/mongodb.html) via mongoengine. The project has its own new code 
to map MongoDB to the [Django](/django.html) Admin interface.

django-mongonaut's highlighted features include:

    * Automatic introspection of mongoengine documents
    * The ability to constrain who sees what and what they can do
    * Full control for adding, editing and deleting documents

The django-mongonaut project is open sourced under the
[MIT License](https://github.com/jazzband/django-mongonaut/blob/master/LICENSE.txt)
and it is maintained by the developer community group 
[Jazzband](https://jazzband.co/).


### django-oauth-toolkit
[django-oauth-toolkit](https://github.com/jazzband/django-oauth-toolkit)
([project website](http://dot.evonove.it/)
and
[PyPI package information](https://pypi.org/project/django-oauth-toolkit/1.2.0/))
is a code library for adding and handling [OAuth2](https://oauth.net/)
flows within your [Django](/django.html) web application and 
[API](/application-programming-interfaces.html).

The django-oauth-toolkit project is open sourced under the
[FreeBSD license](https://github.com/jazzband/django-oauth-toolkit/blob/master/LICENSE)
and it is maintained by the developer community group 
[Jazzband](https://jazzband.co/).

Code examples provided by django-oauth-toolkit:

* [django.http HttpResponseForbidden](/django-http-httpresponseforbidden-examples.html)


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


### django-pipeline
[django-pipeline](https://github.com/jazzband/django-pipeline)
([project documentation](https://django-pipeline.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-pipeline/))
is a code library for handling and compressing 
[static content assets](/static-content.html) when handling requests in
[Django](/django.html) web applications.

The django-pipeline project is open sourced under the
[MIT License](https://github.com/jazzband/django-pipeline/blob/master/LICENSE)
and it is maintained by the developer community group 
[Jazzband](https://jazzband.co/).


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


### django-taggit
[django-taggit](https://github.com/jazzband/django-taggit)
([project documentation](https://django-taggit.readthedocs.io/))
[PyPI page](https://pypi.org/project/django-taggit/)) provides a way
to create, store, manage and use tags in a [Django](/django.html) project. 
The code for django-taggit is 
[open source](https://github.com/jazzband/django-taggit/blob/master/LICENSE)
and maintained by the collaborative developer community group 
[Jazzband](https://jazzband.co/).


### drf-action-serializer
[drf-action-serializer](https://github.com/gregschmit/drf-action-serializer)
([PyPI page](https://pypi.org/project/drf-action-serializer/))
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

* [django.apps.config AppConfig](/django-apps-config-appconfig-examples.html)
* [django.conf.urls url](/django-conf-urls-url-examples.html)
* [django.contrib admin](/django-contrib-admin-examples.html)
* [django.contrib.auth.hashers make_password](/django-contrib-auth-hashers-make-password-examples.html)


### jazzband
[jazzband](https://github.com/jazzband/website) is a 
[Django](/django.html)-based web application that runs a website with
information on many Django projects such as 
[django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)
and [django-taggit](https://github.com/jazzband/django-taggit).

The project's code is provided as open source under the
[MIT license](https://github.com/jazzband/website/blob/master/LICENSE).


### pytest-django
[pytest-django](https://github.com/pytest-dev/pytest-django)
([project documentation](https://pytest-django.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/pytest-django/))
is a code library that makes it easier to use 
[pytest](https://docs.pytest.org/en/latest/) with [Django](/django.html)
applications. The project and its code are open sourced under the 
[BSD 3-clause license](https://github.com/pytest-dev/pytest-django/blob/master/LICENSE).


### register
[register](https://github.com/ORGAN-IZE/register) is a [Django](/django.html),
[Bootstrap](/bootstrap-css.html), [PostgreSQL](/postgresql.html) project that is
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
* [django.contrib.admin.sites.register](/django-contrib-admin-sites-register-examples.html)
* [django.db.models DateField](/django-db-models-datefield-examples.html)
* [django.db.models IntegerField](/django-db-models-integerfield-examples.html)
* [django.http HttpResponseNotModified](/django-http-httpresponsenotmodified-examples.html)
* [django.http Http404](/django-http-http404-examples.html)
* [django.template.response TemplateResponse](/django-template-response-templateresponse-examples.html)

