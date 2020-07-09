title: django.utils termcolors Example Code
category: page
slug: django-utils-termcolors-examples
sortorder: 500011420
toc: False
sidebartitle: django.utils termcolors
meta: Python example code for the termcolors callable from the django.utils module of the Django project.


termcolors is a callable within the django.utils module of the Django project.


## Example 1 from django-extensions
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

[**django-extensions / django_extensions / management / color.py**](https://github.com/django-extensions/django-extensions/blob/master/django_extensions/management/color.py)

```python
# color.py

from django.core.management import color
~~from django.utils import termcolors


def _dummy_style_func(msg):
    return msg


def no_style():
    style = color.no_style()
    for role in ('INFO', 'WARN', 'BOLD', 'URL', 'MODULE', 'MODULE_NAME', 'URL_NAME'):
        setattr(style, role, _dummy_style_func)
    return style


def color_style():
    if color.supports_color():
        style = color.color_style()
~~        style.INFO = termcolors.make_style(fg='green')
~~        style.WARN = termcolors.make_style(fg='yellow')
~~        style.BOLD = termcolors.make_style(opts=('bold',))
~~        style.URL = termcolors.make_style(fg='green', opts=('bold',))
~~        style.MODULE = termcolors.make_style(fg='yellow')
~~        style.MODULE_NAME = termcolors.make_style(opts=('bold',))
~~        style.URL_NAME = termcolors.make_style(fg='red')
    else:
        style = no_style()
    return style



## ... source file continues with no further termcolors examples...

```

