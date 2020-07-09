title: django.urls get_callable Example Code
category: page
slug: django-urls-get-callable-examples
sortorder: 500011403
toc: False
sidebartitle: django.urls get_callable
meta: Python example code for the get_callable callable from the django.urls module of the Django project.


get_callable is a callable within the django.urls module of the Django project.


## Example 1 from django-wiki
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

[**django-wiki / src/wiki / editors / __init__.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/editors/__init__.py)

```python
# __init__.py
~~from django.urls import get_callable
from wiki.conf import settings

_EditorClass = None
_editor = None


def getEditorClass():
    global _EditorClass
    if not _EditorClass:
~~        _EditorClass = get_callable(settings.EDITOR)
    return _EditorClass


def getEditor():
    global _editor
    if not _editor:
        _editor = getEditorClass()()
    return _editor



## ... source file continues with no further get_callable examples...

```

