title: django.utils.functional wraps Example Code
category: page
slug: django-utils-functional-wraps-examples
sortorder: 500011460
toc: False
sidebartitle: django.utils.functional wraps
meta: Python example code for the wraps callable from the django.utils.functional module of the Django project.


wraps is a callable within the django.utils.functional module of the Django project.


## Example 1 from django-guardian
[django-guardian](https://github.com/django-guardian/django-guardian)
([project documentation](https://django-guardian.readthedocs.io/en/stable/)
and
[PyPI page](https://pypi.org/project/django-guardian/))
provides per-object permissions in [Django](/django.html) projects
by enhancing the existing authentication backend. The project's code
is open source under the
[MIT license](https://github.com/django-guardian/django-guardian/blob/devel/LICENSE).

[**django-guardian / guardian / decorators.py**](https://github.com/django-guardian/django-guardian/blob/devel/guardian/./decorators.py)

```python
# decorators.py
from django.apps import apps
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.db.models import Model
from django.db.models.base import ModelBase
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
~~from django.utils.functional import wraps
from guardian.exceptions import GuardianError
from guardian.utils import get_40x_or_None


def permission_required(perm, lookup_variables=None, **kwargs):
    login_url = kwargs.pop('login_url', settings.LOGIN_URL)
    redirect_field_name = kwargs.pop(
        'redirect_field_name', REDIRECT_FIELD_NAME)
    return_403 = kwargs.pop('return_403', False)
    return_404 = kwargs.pop('return_404', False)
    accept_global_perms = kwargs.pop('accept_global_perms', False)

    if not isinstance(perm, str):
        raise GuardianError("First argument must be in format: "
                            "'app_label.codename or a callable which return similar string'")

    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            obj = None
            if lookup_variables:
                model, lookups = lookup_variables[0], lookup_variables[1:]
                if isinstance(model, str):
                    splitted = model.split('.')
                    if len(splitted) != 2:


## ... source file abbreviated to get to wraps examples ...


                                            "string it needs format: 'app_label.ModelClass'")
                    model = apps.get_model(*splitted)
                elif issubclass(model.__class__, (Model, ModelBase, QuerySet)):
                    pass
                else:
                    raise GuardianError("First lookup argument must always be "
                                        "a model, string pointing at app/model or queryset. "
                                        "Given: %s (type: %s)" % (model, type(model)))
                if len(lookups) % 2 != 0:
                    raise GuardianError("Lookup variables must be provided "
                                        "as pairs of lookup_string and view_arg")
                lookup_dict = {}
                for lookup, view_arg in zip(lookups[::2], lookups[1::2]):
                    if view_arg not in kwargs:
                        raise GuardianError("Argument %s was not passed "
                                            "into view function" % view_arg)
                    lookup_dict[lookup] = kwargs[view_arg]
                obj = get_object_or_404(model, **lookup_dict)

            response = get_40x_or_None(request, perms=[perm], obj=obj,
                                       login_url=login_url, redirect_field_name=redirect_field_name,
                                       return_403=return_403, return_404=return_404, accept_global_perms=accept_global_perms)
            if response:
                return response
            return view_func(request, *args, **kwargs)
~~        return wraps(view_func)(_wrapped_view)
    return decorator


def permission_required_or_403(perm, *args, **kwargs):
    kwargs['return_403'] = True
    return permission_required(perm, *args, **kwargs)


def permission_required_or_404(perm, *args, **kwargs):
    kwargs['return_404'] = True
    return permission_required(perm, *args, **kwargs)



## ... source file continues with no further wraps examples...

```


## Example 2 from django-taggit
[django-taggit](https://github.com/jazzband/django-taggit/)
([PyPI page](https://pypi.org/project/django-taggit/)) provides a way
to create, store, manage and use tags in a [Django](/django.html) project.
The code for django-taggit is
[open source](https://github.com/jazzband/django-taggit/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-taggit / taggit / utils.py**](https://github.com/jazzband/django-taggit/blob/master/taggit/./utils.py)

```python
# utils.py
from django.conf import settings
~~from django.utils.functional import wraps
from django.utils.module_loading import import_string


def _parse_tags(tagstring):
    if not tagstring:
        return []

    if "," not in tagstring and '"' not in tagstring:
        words = list(set(split_strip(tagstring, " ")))
        words.sort()
        return words

    words = []
    buffer = []
    to_be_split = []
    saw_loose_comma = False
    open_quote = False
    i = iter(tagstring)
    try:
        while True:
            c = next(i)
            if c == '"':
                if buffer:
                    to_be_split.append("".join(buffer))


## ... source file abbreviated to get to wraps examples ...


    words = list(set(words))
    words.sort()
    return words


def split_strip(string, delimiter=","):
    if not string:
        return []

    words = [w.strip() for w in string.split(delimiter)]
    return [w for w in words if w]


def _edit_string_for_tags(tags):
    names = []
    for tag in tags:
        name = tag.name
        if "," in name or " " in name:
            names.append('"%s"' % name)
        else:
            names.append(name)
    return ", ".join(sorted(names))


def require_instance_manager(func):
~~    @wraps(func)
    def inner(self, *args, **kwargs):
        if self.instance is None:
            raise TypeError("Can't call %s with a non-instance manager" % func.__name__)
        return func(self, *args, **kwargs)

    return inner


def get_func(key, default):
    func_path = getattr(settings, key, None)
    return default if func_path is None else import_string(func_path)


def parse_tags(tagstring):
    func = get_func("TAGGIT_TAGS_FROM_STRING", _parse_tags)
    return func(tagstring)


def edit_string_for_tags(tags):
    func = get_func("TAGGIT_STRING_FROM_TAGS", _edit_string_for_tags)
    return func(tags)



## ... source file continues with no further wraps examples...

```

