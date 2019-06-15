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

