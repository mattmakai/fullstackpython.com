title: Django Extensions, Plug-ins and Related Libraries
category: page
slug: django-extensions-plug-ins-related-libraries
sortorder: 500010000
toc: False
sidebartitle: Django Extensions
meta: Python code extensions and plug-in projects that show how to use the Django web application framework.


[Django](/django.html) is a Python [web framework](/web-frameworks.html).

<a href="http://www.djangoproject.com/" style="border: none;"><img src="/img/logos/django.png" width="100%" alt="Official Django logo. Trademark Django Software Foundation." class="shot" style="margin-top:20px"></a>

Part of Django's widespread adoption comes from a broad ecosystem of 
open source code libraries that augment the core framework.

It's good to familiarize yourself with the following projects to 
learn what is available to you beyond the extensive 
"[batteries-included](https://www.quora.com/Why-does-Django-tout-itself-as-a-batteries-included-web-framework-when-you-have-to-manually-write-regexes-to-do-URL-routing)" 
code base.

These projects, ordered alphabetically, can also be helpful as example 
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
The code for django-angular is provided as open source
[under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

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
[PyPI package information](https://pypi.org/project/django-axes/))
is a code library for [Django](/django.html) projects to track failed
login attempts against a web application. The goal of the project is
to make it easier for you to stop people and scripts from hacking your
Django-powered website.

The code for django-axes is
[open source under the MIT license](https://github.com/jazzband/django-axes/blob/master/LICENSE)
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


### Django DownloadView
[django-downloadview](https://github.com/benoitbryon/django-downloadview)
([project documentation](https://django-downloadview.readthedocs.io/en/1.9/)
and
[PyPI package information](https://pypi.org/project/django-downloadview/))
is a [Django](/django.html) extension for serving downloads through your
web application. While typically you would use a web server to handle
[static content](/static-content.html), sometimes you need to control
file access, such as requiring a user to register before downloading a
PDF. In that situations, django-downloadview is a handy library to avoid
boilerplate code for common scenarios.


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


### django-environ
[django-environ](https://github.com/joke2k/django-environ)
([project documentation](https://django-environ.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-environ/))
is a library that aims to make it easier to configure your Django
project's configuration through environment variables. The philosophy
is inspired by the [Twelve-Factor App](https://www.12factor.net/)
set of principles.

django-environ is open source under the 
[MIT license](https://github.com/joke2k/django-environ/blob/develop/LICENSE.txt).


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


### django-filter
[django-filter](https://github.com/carltongibson/django-filter)
([project documentation](https://django-filter.readthedocs.io/en/master/)
and
[PyPI page](https://pypi.org/project/django-filter/2.2.0/))
makes it easier to filter down querysets from the 
[Django ORM](/django-orm.html) by providing common bits of boilerplate
code. django-filter is provided as 
[open source](https://github.com/carltongibson/django-filter/blob/master/LICENSE).


### django-flexible-subscriptions
[django-flexible-subscriptions](https://github.com/studybuffalo/django-flexible-subscriptions)
([project documentation](https://django-flexible-subscriptions.readthedocs.io/en/latest/)
and 
[PyPI package information](https://pypi.org/project/django-flexible-subscriptions/))
provides boilerplate code for adding subscription and recurrent billing
to [Django](/django.html) web applications. Various payment providers 
can be added on the back end to run the transactions.

The django-flexible-subscriptions project is open sourced under the
[GNU General Public License v3.0](https://github.com/studybuffalo/django-flexible-subscriptions/blob/master/LICENSE).


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


### django-import-export
[django-import-export](https://github.com/django-import-export/django-import-export)
([documentation](https://django-import-export.readthedocs.io/en/latest/)
and [PyPI page](https://pypi.org/project/django-import-export/))
is a [Django](/django.html) code library for importing and exporting data
from the Django Admin. The tool supports many export and import formats 
such as CSV, JSON and YAML. django-import-export is open source under the
[BSD 2-Clause "Simplified" License](https://github.com/django-import-export/django-import-export/blob/master/LICENSE).


### django-inline-actions
[django-inline-actions](https://github.com/escaped/django-inline-actions)
([PyPI package information](https://pypi.org/project/django-inline-actions/))
is an extension that adds actions to the [Django](/django.html)
Admin InlineModelAdmin and ModelAdmin changelists. The project is open
sourced under the 
[BSD 3-Clause "New" or "Revised" License](https://github.com/escaped/django-inline-actions/blob/master/LICENSE).


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
([jsonfield on PyPI](https://pypi.org/project/jsonfield/)) is a
[Django](/django.html) code library that makes it easier to store validated
JSON in a [Django object-relational mapper (ORM)](/django-orm.html) database 
model.

The django-jsonfield project is open source under the 
[MIT license](https://github.com/dmkoch/django-jsonfield/blob/master/LICENSE).


### django-loginas
[django-loginas](https://github.com/skorokithakis/django-loginas)
([PyPI package information](https://pypi.org/project/django-loginas/))
is [Django](/django.html) code library for admins to log into an application
as another user, typically for debugging purposes.

django-loginas is open source under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/skorokithakis/django-loginas/blob/master/LICENSE).


### django-markdown-view
[django-markdown-view](https://github.com/rgs258/django-markdown-view)
([PyPI package information](https://pypi.org/project/django-markdown-view/))
is a Django extension for serving [Markdown](/markdown.html) files as
[Django templates](/django-templates.html). The project is open
sourced under the 
[BSD 3-Clause "New" or "Revised" license](https://github.com/rgs258/django-markdown-view/blob/master/LICENSE).


### django-migration-linter
[django-migration-linter](https://github.com/3YOURMIND/django-migration-linter)
([PyPI package information](https://pypi.org/project/django-migration-linter/))
checks for backwards-incompatible changes in [Django ORM](/django-orm.html)
schema migrations and warns you about them. The purpose of the project is
to save time in older and larger projects by detecting field migrations
that will be a problem so you do not run into issues later, and make it
easier to enable continuous [deployment](/deployment.html) configurations 
with database changes. There is a 
[blog post on keeping Django database migrations backward compatible](https://medium.com/3yourmind/keeping-django-database-migrations-backward-compatible-727820260dbb) 
that goes into further detail on the tool.

The django-migration-linter project is open sourced under the
[Apache 2.0 license](https://github.com/3YOURMIND/django-migration-linter/blob/master/LICENSE).


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

django-mongonaut's highlighted features include automatic introspection 
of mongoengine documents, the ability to constrain who sees what and what 
they can do, and full control for adding, editing and deleting documents.

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


### Django REST Framework
[Django REST Framework](https://github.com/encode/django-rest-framework)
([project homepage and documentation](https://www.django-rest-framework.org/),
[PyPI package information](https://pypi.org/project/djangorestframework/)
and [more resources on Full Stack Python](/django-rest-framework-drf.html)), 
often abbreviated as "DRF", is a popular [Django](/django.html) extension
for building [web APIs](/application-programming-interfaces.html).
The project has fantastic documentation and a wonderful
[quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)
that serve as examples of how to make it easier for newcomers
to get started.

The project is open sourced under the 
[Encode OSS Ltd. license](https://github.com/encode/django-rest-framework/blob/master/LICENSE.md).


### django-rq
[django-rq](https://github.com/rq/django-rq)
([PyPI package information](https://pypi.org/project/django-rq/))
is an [RQ](/redis-queue-rq.html)-based [task queue](/task-queues.html)
that integrates with [Django](/django.html) as an app. This project
is useful when you need a lightweight task queue and do not want
to go through configuring [Celery](/celery.html) in your project.
django-rq is open sourced under the
[MIT license](https://github.com/rq/django-rq/blob/master/LICENSE.txt).


### django-simple-task
[django-simple-task](https://github.com/ericls/django-simple-task) 
([project documentation](https://django-simple-task.readthedocs.io/)
and
[PyPI package information](https://pypi.org/project/django-simple-task/))
is a task runner similar but more brittle than other 
[task queues](/task-queues.html) such as [Celery](/celery.html) and 
[RQ](/redis-queue-rq.html). django-simple-task requires Django 3.0's new
ASGI event loop functionality to work properly. It is open sourced under the
[MIT license](https://github.com/ericls/django-simple-task/blob/master/LICENSE).


### django-sitetree
[django-sitetree](https://github.com/idlesign/django-sitetree)
([project documentation](https://django-sitetree.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-sitetree/))
is a [Django](/django.html) extension that makes it easier for
developers to add site trees, menus and breadcrumb navigation elements
to their web applications.

The django-sitetree project is provided as open source under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/idlesign/django-sitetree/blob/master/LICENSE).


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


### django-sql-explorer
[django-sql-explorer](https://github.com/groveco/django-sql-explorer)
([PyPI page](https://pypi.org/project/django-sql-explorer/0.2/)),
also referred to as "SQL Explorer",
is a code library for the [Django](/django.html) Admin that allows
approved, authenticated users to view and execute direct database SQL 
queries. The tool keeps track of executed queries so users can share them
with each other, as well as export results to downloadable formats.
django-sql-explorer is provided as open source under the
[MIT license](https://github.com/groveco/django-sql-explorer/blob/master/LICENSE).


### django-tables2
[django-tables2](https://github.com/jieter/django-tables2) 
([projection documentation](https://django-tables2.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-tables2/))
is a code library for [Django](/django.html) that simplifies creating and 
displaying tables in [Django templates](/django-templates.html),
especially with more advanced features such as pagination and sorting.
The project and its code are 
[available as open source](https://github.com/jieter/django-tables2/blob/master/LICENSE).


### django-taggit
[django-taggit](https://github.com/jazzband/django-taggit)
([project documentation](https://django-taggit.readthedocs.io/)
and
[PyPI page](https://pypi.org/project/django-taggit/)) provides a way
to create, store, manage and use tags in a [Django](/django.html) project. 
The code for django-taggit is 
[open source](https://github.com/jazzband/django-taggit/blob/master/LICENSE)
and maintained by the collaborative developer community group 
[Jazzband](https://jazzband.co/).


### django-user-visit
[django-user-visit](https://github.com/yunojuno/django-user-visit)
([PyPI package information](https://pypi.org/project/django-user-visit/))
is a [Django](/django.html) app and 
[middleware](https://docs.djangoproject.com/en/stable/topics/http/middleware/)
for tracking daily user visits to your web application. The goal
is to record per user per day instead of for every request a user
sends to the application. The project is provided as open source
under the 
[MIT license](https://github.com/yunojuno/django-user-visit/blob/master/LICENSE).


### django-webshell
[django-webshell](https://github.com/onrik/django-webshell) is an extension
for executing arbitrary code in the 
[Django admin](https://docs.djangoproject.com/en/stable/ref/contrib/admin/),
similar to how you can run code by using the `django manage.py shell` 
command from the terminal.

The django-webshell project is provided as open source under the
[MIT license](https://github.com/onrik/django-webshell/blob/master/LICENSE).


### django-webtest
[django-webtest](https://github.com/django-webtest/django-webtest)
([PyPI package information](https://pypi.org/project/django-webtest/))
is a [Django](/django.html) extension that makes it easier to use
[WebTest](http://docs.pylonsproject.org/projects/webtest/) with
your projects.

The project is open sourced under the
[MIT license](https://github.com/django-webtest/django-webtest/blob/master/LICENSE.txt).


### django-wiki
[django-wiki](https://github.com/django-wiki/django-wiki)
([project documentation](https://django-wiki.readthedocs.io/en/master/),
[demo](https://demo.django-wiki.org/),
and [PyPI page](https://pypi.org/project/django-wiki/))
is a wiki system code library for [Django](/django.html)
projects that makes it easier to create user-editable content.
The project aims to provide necessary core features and then
have an easy plugin format for additional features, rather than
having every exhaustive feature built into the core system.
django-wiki is a rewrite of an earlier now-defunct project
named [django-simplewiki](https://code.google.com/p/django-simple-wiki/).

The code for django-wiki is provided as open source under the
[GNU General Public License 3.0](https://github.com/django-wiki/django-wiki/blob/master/COPYING).


### elasticsearch-django
[elasticsearch-django](https://github.com/yunojuno/elasticsearch-django)
([PyPI package information](https://pypi.org/project/elasticsearch-django/))
is a [Django](/django.html) app for managing 
[ElasticSearch](https://github.com/elastic/elasticsearch) indexes
populated by [Django ORM](/django-orm.html) models. The project is
available as open source under the
[MIT license](https://github.com/yunojuno/elasticsearch-django/blob/master/LICENSE).


### pytest-django
[pytest-django](https://github.com/pytest-dev/pytest-django)
([project documentation](https://pytest-django.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/pytest-django/))
is a code library that makes it easier to use 
[pytest](https://docs.pytest.org/en/latest/) with [Django](/django.html)
applications. The project and its code are open sourced under the 
[BSD 3-clause license](https://github.com/pytest-dev/pytest-django/blob/master/LICENSE).


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

