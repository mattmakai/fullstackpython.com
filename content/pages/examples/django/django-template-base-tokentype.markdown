title: django.template.base TokenType Example Code
category: page
slug: django-template-base-tokentype-examples
sortorder: 500011372
toc: False
sidebartitle: django.template.base TokenType
meta: Python example code for the TokenType class from the django.template.base module of the Django project.


TokenType is a class within the django.template.base module of the Django project.


## Example 1 from django-sitetree
[django-sitetree](https://github.com/idlesign/django-sitetree)
([project documentation](https://django-sitetree.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-sitetree/))
is a [Django](/django.html) extension that makes it easier for
developers to add site trees, menus and breadcrumb navigation elements
to their web applications.

The django-sitetree project is provided as open source under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/idlesign/django-sitetree/blob/master/LICENSE).

[**django-sitetree / sitetree / compat.py**](https://github.com/idlesign/django-sitetree/blob/master/sitetree/./compat.py)

```python
# compat.py
from typing import Callable

try:
~~    from django.template.base import TokenType
~~    TOKEN_BLOCK = TokenType.BLOCK
~~    TOKEN_TEXT = TokenType.TEXT
~~    TOKEN_VAR = TokenType.VAR
except ImportError:
    from django.template.base import TOKEN_BLOCK, TOKEN_TEXT, TOKEN_VAR


class CommandOption:

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


def options_getter(command_options):
    def get_options(option_func: Callable = None):
        from optparse import make_option

        func = option_func or make_option
        options = tuple([func(*option.args, **option.kwargs) for option in command_options])

        return [] if option_func is None else options

    return get_options



## ... source file continues with no further TokenType examples...

```

