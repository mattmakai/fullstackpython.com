title: django.core serializers code examples
category: page
slug: django-core-serializers-examples
sortorder: 500011083
toc: False
sidebartitle: django.core serializers
meta: Python example code for the serializers function from the django.core module of the Django project.


serializers is a function within the django.core module of the Django project.


## Example 1 from django-angular
[django-angular](https://github.com/jrief/django-angular)
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / views / crud.py**](https://github.com/jrief/django-angular/blob/master/djng/views/crud.py)

```python
# crud.py
import json

from django.core.exceptions import ValidationError
~~from django.core import serializers
from django.forms.models import modelform_factory
from django.views.generic import FormView

from djng.views.mixins import JSONBaseMixin, JSONResponseException


class NgMissingParameterError(ValueError):
    pass


class NgCRUDView(JSONBaseMixin, FormView):
    model = None
    fields = None
    form_class = None
    slug_field = 'slug'
    serializer_name = 'python'
    serialize_natural_keys = False

    allowed_methods = ['GET', 'POST', 'DELETE']
    exclude_methods = []

    def get_allowed_methods(self):
        return [method for method in self.allowed_methods if method not in self.exclude_methods]



## ... source file abbreviated to get to serializers examples ...


    def get_form_class(self):
        return self.form_class or modelform_factory(self.model, exclude=[])

    def build_json_response(self, data, **kwargs):
        return self.json_response(self.serialize_queryset(data), separators=(',', ':'), **kwargs)

    def error_json_response(self, message, status_code=400, detail=None):
        response_data = {
            "message": message,
            "detail": detail,
        }
        return self.json_response(response_data, status=status_code, separators=(',', ':'))

    def serialize_queryset(self, queryset):
        object_data = []
        is_queryset = False
        query_fields = self.get_fields()
        try:
            iter(queryset)
            is_queryset = True
~~            raw_data = serializers.serialize(self.serializer_name, queryset, fields=query_fields,
                                             use_natural_keys=self.serialize_natural_keys)
        except TypeError:  # Not iterable
~~            raw_data = serializers.serialize(self.serializer_name, [queryset, ], fields=query_fields,
                                             use_natural_keys=self.serialize_natural_keys)

        for obj in raw_data:  # Add pk to fields
            obj['fields']['pk'] = obj['pk']
            object_data.append(obj['fields'])

        if is_queryset:
            return object_data
        return object_data[0]  # If there's only one object

    def get_form_kwargs(self):
        kwargs = super(NgCRUDView, self).get_form_kwargs()
        kwargs['data'] = json.loads(self.request.body.decode('utf-8'))

        if 'pk' in self.request.GET or self.slug_field in self.request.GET:
            kwargs['instance'] = self.get_object()
        return kwargs

    def get_object(self):
        if 'pk' in self.request.GET:
            return self.model.objects.get(pk=self.request.GET['pk'])
        elif self.slug_field in self.request.GET:
            return self.model.objects.get(**{self.slug_field: self.request.GET[self.slug_field]})
        raise NgMissingParameterError(


## ... source file continues with no further serializers examples...

```

