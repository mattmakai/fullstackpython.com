title: django.apps.config AppConfig Example Code
category: page
slug: django-apps-config-appconfig-examples
sortorder: 500010020
toc: False
sidebartitle: django.apps.config AppConfig
meta: Python code examples for the AppConfig class that is part of Django's django.apps.config package.


[AppConfig](https://github.com/django/django/blob/master/django/apps/config.py)
([documentation](https://docs.djangoproject.com/en/stable/ref/applications/#django.apps.AppConfig))
represents an app for a [Django](/django.html) project, including
metadata such as name, label and path.


## Example 1 from AuditLog
[Auditlog](https://github.com/jjkester/django-auditlog)
([project documentation](https://django-auditlog.readthedocs.io/en/latest/))
is a [Django](/django.html) app that logs changes to Python objects,
similar to the Django admin's logs but with more details and
output formats. Auditlog's source code is provided as open source under the
[MIT license](https://github.com/jjkester/django-auditlog/blob/master/LICENSE).

[**AuditLog / src/auditlog_tests / apps.py**](https://github.com/jjkester/django-auditlog/blob/master/src/auditlog_tests/apps.py)

```python
~~from django.apps import AppConfig


~~class AuditlogTestConfig(AppConfig):
~~    name = 'auditlog_tests'
```


## Example 2 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn/registration / apps.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/registration/apps.py)

```python
~~from django.apps import AppConfig


~~class RegistrationConfig(AppConfig):
~~    name = 'registration'
```


## Example 3 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth/socialaccount / apps.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/socialaccount/apps.py)

```python
~~from django.apps import AppConfig

from allauth.compat import ugettext_lazy as _


~~class SocialAccountConfig(AppConfig):
~~    name = 'allauth.socialaccount'
~~    verbose_name = _('Social Accounts')
```


## Example 4 from gadget-board
[gadget-board](https://github.com/mik4el/gadget-board) is a
[Django](/django.html),
[Django REST Framework (DRF)](/django-rest-framework-drf.html) and
[Angular](/angular.html) web application that is open source under the
[Apache2 license](https://github.com/mik4el/gadget-board/blob/master/LICENSE).

[**gadget-board / web/authentication / apps.py**](https://github.com/mik4el/gadget-board/blob/master/web/authentication/apps.py)

```python
~~from django.apps import AppConfig


~~class AuthenticationConfig(AppConfig):
~~    name = 'authentication'
```

