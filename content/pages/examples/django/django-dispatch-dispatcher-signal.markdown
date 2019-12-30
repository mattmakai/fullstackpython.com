title: django.dispatch Signal Example Code
category: page
slug: django-dispatch-dispatcher-signal-examples
sortorder: 500012930
toc: False
sidebartitle: django.dispatch Signal
meta: Python code examples for the Signal class within the django.dispatch module of the Django project. 


The 
[Signal](https://github.com/django/django/blob/master/django/dispatch/dispatcher.py)
class allows certain senders to notify a set of receivers that some action 
has taken place across [Django](/django.html) apps within the same project.


## Example 1 from django-simple-history
[django-simple-history](https://github.com/treyhunner/django-simple-history) 
is a [code library](https://pypi.org/project/django-simple-history/) that 
stores Django model state to track history, view and revert changes via the 
[Django admin site](https://docs.djangoproject.com/en/dev/ref/contrib/admin/).
It is open source under the 
[BSD 3-Clause "New" or "Revise" License](https://github.com/treyhunner/django-simple-history/blob/master/LICENSE.txt).

[**django-simple-history / simple_history / signals.py**](https://github.com/treyhunner/django-simple-history/blob/master/simple_history/signals.py)

```python
# signals.py
~~import django.dispatch


~~pre_create_historical_record = django.dispatch.Signal(
    providing_args=[
        "instance",
        "history_instance",
        "history_date",
        "history_user",
        "history_change_reason",
        "using",
    ]
)
~~post_create_historical_record = django.dispatch.Signal(
    providing_args=[
        "instance",
        "history_instance",
        "history_date",
        "history_user",
        "history_change_reason",
        "using",
    ]
)
```


## Example 2 from aldryn-accounts
[aldryn-accounts](https://github.com/divio/aldryn-accounts) is a code library
for user registration and authentication in [Django](/django.html) projects.
The code for this project is open source under the 
[MIT license](https://github.com/divio/aldryn-accounts/blob/develop/LICENSE).

[**aldryn-accounts / aldryn_accounts / signal.py**](https://github.com/divio/aldryn-accounts/blob/develop/aldryn_accounts/signals.py)

```python
# -*- coding: utf-8 -*-
~~import django.dispatch
from django.contrib.auth import user_logged_in
from django.db.models import signals, ObjectDoesNotExist
from django.utils.encoding import force_text
from django.utils import timezone
from django.contrib.auth.models import User

from .utils import generate_username


~~user_signed_up = django.dispatch.Signal(providing_args=["user", "form"])
~~user_sign_up_attempt = django.dispatch.Signal(providing_args=["username",  "email", "result"])
~~signup_code_sent = django.dispatch.Signal(providing_args=["signup_code"])
~~signup_code_used = django.dispatch.Signal(providing_args=["signup_code_result"])
~~email_confirmed = django.dispatch.Signal(providing_args=["email_address"])
~~email_confirmation_sent = django.dispatch.Signal(providing_args=["confirmation"])
~~password_changed = django.dispatch.Signal(providing_args=["user"])


# code continues from here without any further django.dispatch.Signal references
```


## Example 3 from django-easy-timezones
[django-easy-timezones](https://github.com/Miserlou/django-easy-timezones)
([project website](https://www.gun.io/blog/django-easy-timezones))
is a [Django](/django.html) 
[middleware](https://docs.djangoproject.com/en/stable/topics/http/middleware/)
[code library](https://pypi.org/project/django-easy-timezones/)
to simplify handling time data in your applications using
users' geolocation data.

[**django-easy-timezones / easy_timezones / signals.py**](https://github.com/Miserlou/django-easy-timezones/blob/master/easy_timezones/middleware.py)

```python
# Django
~~import django.dispatch

~~detected_timezone = django.dispatch.Signal(providing_args=["instance", "timezone"])
```


## Example 4 from viewflow
[viewflow](https://github.com/viewflow/viewflow) 
([project website](http://viewflow.io/)) is a reusable workflow
code library for organizing business logic in a complex web application.
The code for the project is available under the 
[GNU Alfredo license](https://github.com/viewflow/viewflow/blob/master/LICENSE).

[**viewflow / viewflow / signals.py**](https://github.com/viewflow/viewflow/blob/master/viewflow/signals.py)

```python
# signals.py
~~from django.dispatch import Signal

~~flow_started = Signal(providing_args=["process", "task"])
~~flow_finished = Signal(providing_args=["process", "task"])

~~task_started = Signal(providing_args=["process", "task"])
~~task_failed = Signal(providing_args=["process", "task", "exception", 
~~                                     "traceback"])
~~task_finished = Signal(providing_args=["process", "task"])
```


## Example 5 from django-registration (redux)
[django-registration (redux)](https://github.com/macropin/django-registration)
([project documentation](https://django-registration-redux.readthedocs.io/en/latest/))
is a [Django](/django.html) code library for one-phase, two-phase and 
three-phase registration flows. The code is available 
[open source](https://github.com/macropin/django-registration/blob/master/LICENSE). 

[**django-registration / registrations / signals.py**](https://github.com/macropin/django-registration/blob/master/registration/signals.py)

```python
from django.conf import settings
from django.contrib.auth import get_backends
from django.contrib.auth import login
~~from django.dispatch import Signal

# An admin has approved a user's account
~~user_approved = Signal(providing_args=["user", "request"])

# A new user has registered.
~~user_registered = Signal(providing_args=["user", "request"])

# A user has activated his or her account.
~~user_activated = Signal(providing_args=["user", "request"])


def login_user(sender, user, request, **kwargs):
    """ Automatically authenticate the user when activated  """
    backend = get_backends()[0]  # Hack to bypass `authenticate()`.
    user.backend = "%s.%s" % (backend.__module__, backend.__class__.__name__)
    login(request, user)
    request.session['REGISTRATION_AUTO_LOGIN'] = True
    request.session.modified = True


if getattr(settings, 'REGISTRATION_AUTO_LOGIN', False):
    user_activated.connect(login_user)
```


## Example 6 from django-cors-headers
[django-cors-headers](https://github.com/ottoyiu/django-cors-headers) is
an 
[open source](https://github.com/ottoyiu/django-cors-headers/blob/master/LICENSE)
library for enabling 
[Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) 
handling in your [Django](/django.html) web applications and appropriately
dealing with HTTP headers for CORS requests.

[**django-cors-headers / src / corsheaders / signals.py**](https://github.com/adamchainz/django-cors-headers/blob/master/src/corsheaders/signals.py)

```python
~~from django.dispatch import Signal

# If any attached handler returns Truthy, CORS will be allowed for the request.
# This can be used to build custom logic into the request handling when the
# configuration doesn't work.
~~check_request_enabled = Signal(providing_args=["request"])
```
