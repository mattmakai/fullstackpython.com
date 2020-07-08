title: django.forms Form Example Code
category: page
slug: django-forms-form-examples
sortorder: 500011267
toc: False
sidebartitle: django.forms Form
meta: Python example code for the Form class from the django.forms module of the Django project.


Form is a class within the django.forms module of the Django project.


## Example 1 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / chair / forms.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/chair/forms.py)

```python
# forms.py
from functools import reduce

from django import forms
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q, F, Count, Max, Subquery, OuterRef, Value
from django.db.models.functions import Concat
~~from django.forms import MultipleChoiceField, ChoiceField, Form
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from django_countries import countries

from conferences.models import Conference, ArtifactDescriptor
from gears.widgets import CustomCheckboxSelectMultiple, CustomFileInput
from review.models import Reviewer, Review, ReviewStats
from review.utilities import get_average_score
from submissions.models import Submission, Attachment
from users.models import Profile

User = get_user_model()


def clean_data_to_int(iterable, empty=None):
    return [int(x) if x != '' else None for x in iterable]


def q_or(disjuncts, default=True):
    if disjuncts:
        return reduce(lambda acc, d: acc | d, disjuncts)
    return Q(pk__isnull=(not default))  # otherwise, check whether PK is null



## ... source file abbreviated to get to Form examples ...


        available_reviewers = Reviewer.objects.exclude(
            Q(pk__in=assigned_reviewers) | Q(user__in=authors_users)
        )
        profiles = {
            rev: rev.user.profile for rev in available_reviewers
        }
        reviewers = list(available_reviewers)
        reviewers.sort(key=lambda r: r.reviews.count())
        self.fields['reviewer'].choices = (
            (rev.pk,
             f'{profiles[rev].get_full_name()} ({rev.reviews.count()}) - '
             f'{profiles[rev].affiliation}, '
             f'{profiles[rev].get_country_display()}')
            for rev in reviewers
        )

    def save(self):
        reviewer = Reviewer.objects.get(pk=self.cleaned_data['reviewer'])
        review = Review.objects.create(
            reviewer=reviewer, stage=self.review_stage)
        return review




~~class ExportSubmissionsForm(Form):
    ORDER_COLUMN = '#'
    ID_COLUMN = 'ID'
    AUTHORS_COLUMN = 'AUTHORS'
    TITLE_COLUMN = 'TITLE'
    COUNTRY_COLUMN = 'COUNTRY'
    STYPE_COLUMN = 'TYPE'
    REVIEW_PAPER_COLUMN = 'REVIEW_MANUSCRIPT'
    REVIEW_SCORE_COLUMN = 'REVIEW_SCORE'
    STATUS_COLUMN = 'STATUS'
    TOPICS_COLUMN = 'TOPICS'

    COLUMNS = (
        (ORDER_COLUMN, ORDER_COLUMN),
        (ID_COLUMN, ID_COLUMN),
        (TITLE_COLUMN, TITLE_COLUMN),
        (AUTHORS_COLUMN, AUTHORS_COLUMN),
        (COUNTRY_COLUMN, COUNTRY_COLUMN),
        (STYPE_COLUMN, STYPE_COLUMN),
        (REVIEW_PAPER_COLUMN, REVIEW_PAPER_COLUMN),
        (REVIEW_SCORE_COLUMN, REVIEW_SCORE_COLUMN),
        (STATUS_COLUMN, STATUS_COLUMN),
        (TOPICS_COLUMN, TOPICS_COLUMN),
    )



## ... source file continues with no further Form examples...

```


## Example 2 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / wizards / views.py**](https://github.com/divio/django-cms/blob/develop/cms/wizards/views.py)

```python
# views.py

import os

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.core.files.storage import FileSystemStorage
~~from django.forms import Form
from django.template.response import SimpleTemplateResponse
from django.urls import NoReverseMatch

from formtools.wizard.views import SessionWizardView

from cms.models import Page
from cms.utils import get_current_site
from cms.utils.i18n import get_site_language_from_request

from .wizard_pool import wizard_pool
from .forms import (
    WizardStep1Form,
    WizardStep2BaseForm,
    step2_form_factory,
)


class WizardCreateView(SessionWizardView):
    template_name = 'cms/wizards/start.html'
    file_storage = FileSystemStorage(
        location=os.path.join(settings.MEDIA_ROOT, 'wizard_tmp_files'))

    form_list = [
        ('0', WizardStep1Form),


## ... source file continues with no further Form examples...

```


## Example 3 from django-mongonaut
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
~~from django.forms import Form
from django.http import HttpResponseForbidden
from django.http import Http404
from django.utils.functional import cached_property
from django.views.generic.edit import DeletionMixin
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



## ... source file abbreviated to get to Form examples ...


        self.ident = self.kwargs.get('id')
        self.document = self.document_type.objects.get(pk=self.ident)

        context['document'] = self.document
        context['app_label'] = self.app_label
        context['document_name'] = self.document_name
        context['form_action'] = reverse('document_detail_edit_form', args=[self.kwargs.get('app_label'),
                                                                            self.kwargs.get('document_name'),
                                                                            self.kwargs.get('id')])

        return context

    def get_form(self): #get_form(self, Form) leads to "get_form() missing 1 required positional argument: 'Form'" error."
        self.set_mongoadmin()
        context = self.set_permissions_in_context({})

        if not context['has_edit_permission']:
            return HttpResponseForbidden("You do not have permissions to edit this content.")

        self.document_type = getattr(self.models, self.document_name)
        self.ident = self.kwargs.get('id')
        try:
            self.document = self.document_type.objects.get(pk=self.ident)
        except self.document_type.DoesNotExist:
            raise Http404
~~        self.form = Form()

        if self.request.method == 'POST':
            self.form = self.process_post_form('Your changes have been saved.')
        else:
            self.form = MongoModelForm(model=self.document_type, instance=self.document).get_form()
        return self.form


class DocumentAddFormView(MongonautViewMixin, FormView, MongonautFormViewMixin):

    template_name = "mongonaut/document_add_form.html"
    form_class = Form
    success_url = '/'
    permission = 'has_add_permission'

    def get_success_url(self):
        self.set_mongonaut_base()
        return reverse('document_detail', kwargs={'app_label': self.app_label, 'document_name': self.document_name, 'id': str(self.new_document.id)})

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
~~        self.form = Form()

        if self.request.method == 'POST':
            self.form = self.process_post_form('Your new document has been added and saved.')
        else:
            self.form = MongoModelForm(model=self.document_type).get_form()
        return self.form


class DocumentDeleteView(DeletionMixin, MongonautViewMixin, TemplateView):

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


## ... source file continues with no further Form examples...

```

