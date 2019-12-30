title: django.urls.exceptions NoReverseMatch Python Code Examples
category: page
slug: django-urls-exceptions-noreversematch-examples
sortorder: 500013610
toc: False
sidebartitle: django.urls.exceptions NoReverseMatch
meta: Python example code for the NoReverseMatch exception class from the django.urls.exceptions module.


[NoReverseMatch](https://docs.djangoproject.com/en/dev/ref/exceptions/#noreversematch)
([source code](https://github.com/django/django/blob/b9cf764be62e77b4777b3a75ec256f6209a57671/django/urls/exceptions.py))
is a [Django](/django.html) exception that is raised when a URL
cannot be matched against any string or regular express in your URL 
configuration. 

A URL matching problem is often caused by missing arguments or 
supplying too many arguments. For example, let's say you have a blog
project with URLs like "myblog.com/2019/10/title-slug", where `2019`
is the year, `10` is the month and `title-slug` is the article's title
as a [slug](https://stackoverflow.com/questions/427102/what-is-a-slug-in-django). 
A miss could happen if you have a URL configuration that is trying to 
find a blog post with the year and the month in the path, but your 
application only specifies the year without the month.


## Example 1 from django-angular
[django-angular](https://github.com/jrief/django-angular) 
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use 
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is 
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / core / urlresolvers.py**](https://github.com/jrief/django-angular/blob/master/djng/core/urlresolvers.py)

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from inspect import isclass

from django.utils import six
~~from django.urls import (get_resolver, get_urlconf, resolve, 
~~                         reverse, NoReverseMatch)
from django.core.exceptions import ImproperlyConfigured

try:
    from django.utils.module_loading import import_string
except ImportError:
    from django.utils.module_loading \
        import import_by_path as import_string

from djng.views.mixins import JSONResponseMixin


def _get_remote_methods_for(view_object, url):
    # view_object can be a view class or instance
    result = {}
    for field in dir(view_object):
        member = getattr(view_object, field, None)
        if callable(member) and hasattr(member, 'allow_rmi'):
            config = {
                'url': url,
                'method': getattr(member, 'allow_rmi'),
                'headers': {'DjNg-Remote-Method': field},
            }
            result.update({field: config})
    return result


def get_all_remote_methods(resolver=None, ns_prefix=''):
    """
    Returns a dictionary to be used for calling 
    ``djangoCall.configure()``, which itself extends the
    Angular API to the client, offering him to call remote methods.
    """
    if not resolver:
        resolver = get_resolver(get_urlconf())
    result = {}
    for name in resolver.reverse_dict.keys():
        if not isinstance(name, six.string_types):
            continue
~~        try:
~~            url = reverse(ns_prefix + name)
~~            resmgr = resolve(url)
~~            ViewClass = import_string('{0}.{1}'.format(\
~~                resmgr.func.__module__, resmgr.func.__name__))
~~            if isclass(ViewClass) and issubclass(ViewClass, 
~~                                                 JSONResponseMixin):
~~                result[name] = _get_remote_methods_for(ViewClass, 
~~                                                       url)
~~        except (NoReverseMatch, ImproperlyConfigured):
~~            pass
    for namespace, ns_pattern in resolver.namespace_dict.items():
        sub_res = get_all_remote_methods(ns_pattern[1], 
                                         ns_prefix + namespace + ':')
        if sub_res:
            result[namespace] = sub_res
    return result


def get_current_remote_methods(view):
    if isinstance(view, JSONResponseMixin):
        return _get_remote_methods_for(view, 
                                       view.request.path_info)
```
