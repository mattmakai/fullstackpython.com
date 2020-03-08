title: django.forms TypedChoiceField Python Code Examples
category: page
slug: django-forms-typedchoicefield-examples
sortorder: 500013129
toc: False
sidebartitle: django.forms TypedChoiceField
meta: View code examples that show how to use the TypedChoiceField class within the forms module of Django.


[TypedChoiceField](https://github.com/django/django/blob/master/django/forms/fields.py)
([documentation](https://docs.djangoproject.com/en/stable/ref/forms/fields/#typedchoicefield)),
from the [Django](/django.html) `forms` module, enables safe handling of 
pre-defined selections collected via an HTTP POST request from an
[HTML](/hypertext-markup-language-html.html) form submission.

TypedChoiceField can either be imported from `django.forms` or 
`django.forms.fields`. `django.forms` is more commonly used because it
is less characters for the equivalent effect.


## Example 1 from dmd-interpreter
[dmd-interpreter](https://github.com/mitchalexbailey/dmd-interpreter)
([running web app](http://www.dmd.nl/DOVE))
is a Python tool to aggregate clinically relevant information related
to variants in the DMD gene and display that [data](/data.html) to a user
with a [Django](/django.html) web application.

[**dmd-interpreter / interpreter / forms.py**](https://github.com/mitchalexbailey/dmd-interpreter/blob/master/interpreter/./forms.py)

```python
# forms.py
~~from django import forms

choices = [(True,'Yes'),(False,'No')]

class IndexForm(forms.Form):
    mutation = forms.CharField(label = 'Mutation', max_length = 100)

class ACMGForm(forms.Form):
~~    pvs1 = forms.TypedChoiceField(label = 'Does the variant cause a premature stop codon (nonsense)?', choices=choices, widget=forms.RadioSelect)
~~    pvs2 = forms.TypedChoiceField(label = 'Does the variant cause a frameshift?', choices=choices, widget=forms.RadioSelect)
~~    pvs3 = forms.TypedChoiceField(label = 'Does the variant cause a multiexon deletion involving key functional domains?', choices=choices, widget=forms.RadioSelect)
~~    pvs4 = forms.TypedChoiceField(label = 'Does the variant cause a change in splice site?', choices=choices, widget=forms.RadioSelect)
~~    pvs5 = forms.TypedChoiceField(label = 'Does the variant cause a change in initiation codon?', choices=choices, widget=forms.RadioSelect)
~~    ps1 = forms.TypedChoiceField(label = 'Is there a reported pathogenic variant causing the same amino acid change?', choices=choices, widget=forms.RadioSelect)
~~    ps2 = forms.TypedChoiceField(label = 'Is the variant <i>de novo</i> (confirmed to not be present in either parent)?', choices=choices, widget=forms.RadioSelect)
~~    ps3 = forms.TypedChoiceField(label = 'Are there well-established <i>in vitro</i> studies predicting a damaging effect of this variant on the gene or gene product?', choices=choices, widget=forms.RadioSelect)
~~    ps4 = forms.TypedChoiceField(label = 'Is this variant more prevalence in affected individuals versus controls? (OR > 5.0)', choices=choices, widget=forms.RadioSelect)
~~    pm1 = forms.TypedChoiceField(label = 'Is this variant located in a mutational hot spot and/or critical functional domain?', choices=choices, widget=forms.RadioSelect)
~~    pm2 = forms.TypedChoiceField(label = 'Is the variant absent from controls (autosomal dominant), or found at an extremely low frequency (autosomal recessive)? (Ex. in ExAC or 1000 genomes)', choices=choices, widget=forms.RadioSelect)
~~    pm3 = forms.TypedChoiceField(label = 'Is this variant in a gene linked to an autosomal recessive condition and in <i>trans</i> with a pathogenic variant?', choices=choices, widget=forms.RadioSelect)
~~    pm4 = forms.TypedChoiceField(label = 'Does the variant change the protein length (while preserving reading frame; deletion, insertion, stop-loss)?', choices=choices, widget=forms.RadioSelect)
~~    pm5 = forms.TypedChoiceField(label = 'Does the variant cause a missense change at a residue where a different change is known to be pathogenic?', choices=choices, widget=forms.RadioSelect)
~~    pm6 = forms.TypedChoiceField(label = 'Do you think the variant is <i>de novo</i> but there has not been confirmation (sequencing of parents)?', choices=choices, widget=forms.RadioSelect)
~~    pp1 = forms.TypedChoiceField(label = 'Is the variant in a known disease-causing gene and has it co-segregated with affected family members?', choices=choices, widget=forms.RadioSelect)
~~    pp2 = forms.TypedChoiceField(label = 'Is the variant in a gene where disease-causing variants are not commonly missense, and in which missense variants are a common mechanism of disease?', choices=choices, widget=forms.RadioSelect)
~~    pp3 = forms.TypedChoiceField(label = 'Do multiple <i>in silico</i> functional predication tools support a deleterious effect on the gene or gene product?', choices=choices, widget=forms.RadioSelect)
~~    pp4 = forms.TypedChoiceField(label = 'Does the patient\'s phenotype and/or family history strongly indicate a disease with a single genetic ontology?', choices=choices, widget=forms.RadioSelect)
~~    pp5 = forms.TypedChoiceField(label = 'Does a reputable source report the variant as pathogenic (but the evidence is not available)?', choices=choices, widget=forms.RadioSelect)
```


# Example 2 from django-angular
[django-angular](https://github.com/jrief/django-angular)
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / forms / fields.py**](https://github.com/jrief/django-angular/blob/master/djng/forms/fields.py)

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import mimetypes

from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core import signing
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from django.urls import reverse_lazy
~~from django.forms import fields, models as model_fields, widgets
from django.utils.html import format_html
from django.utils.module_loading import import_string
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _, ungettext_lazy

from djng import app_settings
from .widgets import DropFileWidget, DropImageWidget


## ... source file abbreviated to get to the TypedChoiceField examples ...

~~class TypedChoiceField(MultipleFieldMixin, fields.TypedChoiceField):
~~    def get_potential_errors(self):
~~        if isinstance(self.widget, widgets.RadioSelect):
~~            errors = self.get_multiple_choices_required()
~~        else:
~~            errors = self.get_input_required_errors()
~~        return errors



## ... source file continues with no further examples ...
```


## Example 3 from django-filter
[django-filter](https://github.com/carltongibson/django-filter)
([project documentation](https://django-filter.readthedocs.io/en/master/)
and
[PyPI page](https://pypi.org/project/django-filter/2.2.0/))
makes it easier to filter down querysets from the
[Django ORM](/django-orm.html) by providing common bits of boilerplate
code. django-filter is provided as
[open source](https://github.com/carltongibson/django-filter/blob/master/LICENSE).

[**django-filter / django_filters / filters.py**](https://github.com/carltongibson/django-filter/blob/master/django_filters/./filters.py)

```python
from collections import OrderedDict
from datetime import timedelta

~~from django import forms
from django.db.models import Q
from django.db.models.constants import LOOKUP_SEP
from django.forms.utils import pretty_name
from django.utils.itercompat import is_iterable
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from .conf import settings
from .constants import EMPTY_VALUES
from .fields import (
    BaseCSVField,
    BaseRangeField,
    ChoiceField,
    DateRangeField,
    DateTimeRangeField,
    IsoDateTimeField,
    IsoDateTimeRangeField,
    LookupChoiceField,
    ModelChoiceField,
    ModelMultipleChoiceField,
    MultipleChoiceField,
    RangeField,
    TimeRangeField
)
from .utils import get_model_field, label_for_filter


## ... source file abbreviated to get to code examples ...


~~class TypedChoiceFilter(Filter):
~~    field_class = forms.TypedChoiceField


class UUIDFilter(Filter):
    field_class = forms.UUIDField


## ... source file continues with no further TypedChoiceField examples ...

```

