title: django.dispatch.dispatcher.Signal Examples
category: page
slug: django-dispatch-dispatcher-signal-examples
sortorder: 50004
toc: False
sidebartitle: django.dispatch.dispatcher Signal
meta: Python code examples for the Signal class within the django.dispatch module of the Django project. 


# django.dispatch.dispatcher Signal Examples
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


[**django-simple-history/simple_history/signals.py**](https://github.com/treyhunner/django-simple-history/blob/master/simple_history/signals.py)

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

[**aldryn-accounts/aldryn_accounts/signal.py**](https://github.com/divio/aldryn-accounts/blob/develop/aldryn_accounts/signals.py)

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
