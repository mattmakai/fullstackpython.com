title: django.contrib.admin.filters SimpleListFilter Example Code
category: page
slug: django-contrib-admin-filters-simplelistfilter-examples
sortorder: 500010185
toc: False
sidebartitle: django.contrib.admin.filters SimpleListFilter
meta: Python code examples for using the SimpleListFilter class contained within django.contrib.admin.filters.


[SimpleListFilter](https://github.com/django/django/blob/master/django/contrib/admin/filters.py)
is a class within the [Django](/django.html) project which can
be subclasses to customize the Django admin's lookups and querying
interface.

Understanding the following concepts are useful when coding projects
that use Django's `SimpleListFilter` class:

* [Django](/django.html) and [Django templates](/django-templates.html) 
* [Web development](/web-development.html), 
  [web frameworks](/web-frameworks.html) and
  [HTML](/hypertext-markup-language-html.html)
* [Angular](/angular.html) and [JavaScript](/javascript.html)

You can also view the [complete all topics page](/table-of-contents.html)
for even more resources.


## Example 1 from AuditLog
[Auditlog](https://github.com/jjkester/django-auditlog) 
([project documentation](https://django-auditlog.readthedocs.io/en/latest/))
is a [Django](/django.html) app that logs changes to Python objects,
similar to the Django admin's logs but with more details and
output formats. Auditlog's source code is provided as open source under the
[MIT license](https://github.com/jjkester/django-auditlog/blob/master/LICENSE).

[**django-auditlog / src / auditlog / filters.py**](https://github.com/jjkester/django-auditlog/blob/master/src/auditlog/filters.py)

```python
# filters.py
~~from django.contrib.admin import SimpleListFilter


~~class ResourceTypeFilter(SimpleListFilter):
    title = 'Resource Type'
    parameter_name = 'resource_type'

    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request)
        types = qs.values_list('content_type_id', 'content_type__model')
        return list(types.order_by('content_type__model').distinct())

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        return queryset.filter(content_type_id=self.value())
```
