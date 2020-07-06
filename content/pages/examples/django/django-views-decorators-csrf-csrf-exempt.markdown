title: django.views.decorators.csrf csrf_exempt Example Code
category: page
slug: django-views-decorators-csrf-csrf-exempt-examples
sortorder: 500011516
toc: False
sidebartitle: django.views.decorators.csrf csrf_exempt
meta: Python example code for the csrf_exempt callable from the django.views.decorators.csrf module of the Django project.


csrf_exempt is a callable within the django.views.decorators.csrf module of the Django project.


## Example 1 from django-rest-framework
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

[**django-rest-framework / rest_framework / viewsets.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./viewsets.py)

```python
# viewsets.py
from collections import OrderedDict
from functools import update_wrapper
from inspect import getmembers

from django.urls import NoReverseMatch
from django.utils.decorators import classonlymethod
~~from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, mixins, views
from rest_framework.decorators import MethodMapper
from rest_framework.reverse import reverse


def _is_extra_action(attr):
    return hasattr(attr, 'mapping') and isinstance(attr.mapping, MethodMapper)


class ViewSetMixin:

    @classonlymethod
    def as_view(cls, actions=None, **initkwargs):
        cls.name = None
        cls.description = None

        cls.suffix = None

        cls.detail = None

        cls.basename = None

        if not actions:


## ... source file abbreviated to get to csrf_exempt examples ...


        def view(request, *args, **kwargs):
            self = cls(**initkwargs)

            if 'get' in actions and 'head' not in actions:
                actions['head'] = actions['get']

            self.action_map = actions

            for method, action in actions.items():
                handler = getattr(self, action)
                setattr(self, method, handler)

            self.request = request
            self.args = args
            self.kwargs = kwargs

            return self.dispatch(request, *args, **kwargs)

        update_wrapper(view, cls, updated=())

        update_wrapper(view, cls.dispatch, assigned=())

        view.cls = cls
        view.initkwargs = initkwargs
        view.actions = actions
~~        return csrf_exempt(view)

    def initialize_request(self, request, *args, **kwargs):
        request = super().initialize_request(request, *args, **kwargs)
        method = request.method.lower()
        if method == 'options':
            self.action = 'metadata'
        else:
            self.action = self.action_map.get(method)
        return request

    def reverse_action(self, url_name, *args, **kwargs):
        url_name = '%s-%s' % (self.basename, url_name)
        namespace = None
        if self.request and self.request.resolver_match:
            namespace = self.request.resolver_match.namespace
        if namespace:
            url_name = namespace + ':' + url_name
        kwargs.setdefault('request', self.request)

        return reverse(url_name, *args, **kwargs)

    @classmethod
    def get_extra_actions(cls):
        return [method for _, method in getmembers(cls, _is_extra_action)]


## ... source file continues with no further csrf_exempt examples...

```

