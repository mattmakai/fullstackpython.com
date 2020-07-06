title: django.views.generic.edit DeletionMixin Example Code
category: page
slug: django-views-generic-edit-deletionmixin-examples
sortorder: 500011536
toc: False
sidebartitle: django.views.generic.edit DeletionMixin
meta: Python example code for the DeletionMixin class from the django.views.generic.edit module of the Django project.


DeletionMixin is a class within the django.views.generic.edit module of the Django project.


## Example 1 from django-mongonaut
[django-mongonaut](https://github.com/jazzband/django-mongonaut)
([project documentation](https://django-mongonaut.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-mongonaut/))
provides an introspective interface for working with
[MongoDB](/mongodb.html) via mongoengine. The project has its own new code
to map MongoDB to the [Django](/django.html) Admin interface.

django-mongonaut's highlighted features include automatic introspection of
mongoengine documents, the ability to constrain who sees what and what
they can do and full control for adding, editing and deleting documents.

The django-mongonaut project is open sourced under the
[MIT License](https://github.com/jazzband/django-mongonaut/blob/master/LICENSE.txt)
and it is maintained by the developer community group
[Jazzband](https://jazzband.co/).

[**django-mongonaut / mongonaut / views.py**](https://github.com/jazzband/django-mongonaut/blob/master/mongonaut/./views.py)

```python
# views.py
import math

from django.contrib import messages
from django.urls import reverse
from django.forms import Form
from django.http import HttpResponseForbidden
from django.http import Http404
from django.utils.functional import cached_property
~~from django.views.generic.edit import DeletionMixin
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from mongoengine.fields import EmbeddedDocumentField, ListField

from mongonaut.forms import MongoModelForm
from mongonaut.mixins import MongonautFormViewMixin
from mongonaut.mixins import MongonautViewMixin
from mongonaut.utils import is_valid_object_id


class IndexView(MongonautViewMixin, ListView):

    template_name = "mongonaut/index.html"
    queryset = []
    permission = 'has_view_permission'

    def get_queryset(self):
        return self.get_mongoadmins()


class DocumentListView(MongonautViewMixin, FormView):
    form_class = Form
    success_url = '/'


## ... source file abbreviated to get to DeletionMixin examples ...


    def get_context_data(self, **kwargs):
        context = super(DocumentAddFormView, self).get_context_data(**kwargs)
        self.set_mongoadmin()
        context = self.set_permissions_in_context(context)
        self.document_type = getattr(self.models, self.document_name)

        context['app_label'] = self.app_label
        context['document_name'] = self.document_name
        context['form_action'] = reverse('document_detail_add_form', args=[self.kwargs.get('app_label'),
                                                                           self.kwargs.get('document_name')])

        return context

    def get_form(self):
        self.set_mongonaut_base()
        self.document_type = getattr(self.models, self.document_name)
        self.form = Form()

        if self.request.method == 'POST':
            self.form = self.process_post_form('Your new document has been added and saved.')
        else:
            self.form = MongoModelForm(model=self.document_type).get_form()
        return self.form


~~class DocumentDeleteView(DeletionMixin, MongonautViewMixin, TemplateView):

    success_url = "/"
    template_name = "mongonaut/document_delete.html"

    def get_success_url(self):
        self.set_mongonaut_base()
        messages.add_message(self.request, messages.INFO, 'Your document has been deleted.')
        return reverse('document_list', kwargs={'app_label': self.app_label, 'document_name': self.document_name})

    def get_object(self):
        self.set_mongoadmin()
        self.document_type = getattr(self.models, self.document_name)
        self.ident = self.kwargs.get('id')
        self.document = self.document_type.objects.get(pk=self.ident)
        return self.document



## ... source file continues with no further DeletionMixin examples...

```

