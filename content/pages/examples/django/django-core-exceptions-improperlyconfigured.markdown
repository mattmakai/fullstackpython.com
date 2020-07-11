title: django.core.exceptions ImproperlyConfigured Example Code
category: page
slug: django-core-exceptions-improperlyconfigured-examples
sortorder: 500012505
toc: False
sidebartitle: django.core.exceptions ImproperlyConfigured
meta: Python code examples for the ImproperlyConfigured exception class provided by the Django codebase. 


[ImproperlyConfigured](https://github.com/django/django/blob/master/django/core/exceptions.py)
is a class within the [Django](/django.html) project that is thrown
when there is a mistake in an application's settings. The exception
can also be thrown by a developer when building a library for project
that will be used with Django.


## Example 1 from django-object-tools
[django-object-tools](https://github.com/praekelt/django-object-tools)
is a code library to make it easier to create new 
[Django admin](https://docs.djangoproject.com/en/dev/ref/contrib/admin/) 
object tools. The project's code provided as open source under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/praekelt/django-object-tools/blob/develop/LICENSE).

[**django-object-tools / object_tools / validation.py**](https://github.com/praekelt/django-object-tools/blob/develop/object_tools/validation.py)

```python
from __future__ import unicode_literals

~~from django.core.exceptions import ImproperlyConfigured

__all__ = ['validate']


def validate(tool_class, model_class):
    """
    Does basic ObjectTool option validation.
    """
    if not hasattr(tool_class, 'name'):
~~        raise ImproperlyConfigured("No 'name' attribute found for tool %s." % (
~~            tool_class.__name__
        ))

    if not hasattr(tool_class, 'label'):
~~        raise ImproperlyConfigured("No 'label' attribute found for tool %s." % (
~~            tool_class.__name__
        ))

    if not hasattr(tool_class, 'view'):
~~        raise NotImplementedError("No 'view' method found for tool %s." % (
~~            tool_class.__name__
        ))
```
