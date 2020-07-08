title: django.forms MultipleChoiceField Example Code
category: page
slug: django-forms-multiplechoicefield-examples
sortorder: 500011275
toc: False
sidebartitle: django.forms MultipleChoiceField
meta: Python example code for the MultipleChoiceField class from the django.forms module of the Django project.


MultipleChoiceField is a class within the django.forms module of the Django project.


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



## ... source file abbreviated to get to MultipleChoiceField examples ...


    )

    Q1 = 'Q1'
    Q2 = 'Q2'
    Q3 = 'Q3'
    Q4 = 'Q4'
    QUARTILE_CHOICES = ((Q1, 'Q1'), (Q2, 'Q2'), (Q3, 'Q3'), (Q4, 'Q4'))

    ORDER_BY_PK = 'PK'
    ORDER_BY_TITLE = 'TITLE'
    ORDER_BY_SCORE = 'SCORE'
    ORDER_CHOICES = (
        (ORDER_BY_PK, 'Order by ID'),
        (ORDER_BY_SCORE, 'Order by score'),
        (ORDER_BY_TITLE, 'Order by title'),
    )

    DIRECTION_CHOICES = (('ASC', 'Ascending'), ('DESC', 'Descending'))

    class Meta:
        model = Conference
        fields = []

    term = forms.CharField(required=False)

~~    completion = MultipleChoiceField(
        widget=CustomCheckboxSelectMultiple(attrs={
            'btn_class': 'btn btn-link dccn-link dccn-text-small',
            'label_class': 'dccn-text-0',
        }), required=False, choices=COMPLETION_CHOICES)

~~    types = MultipleChoiceField(
        widget=CustomCheckboxSelectMultiple, required=False)

~~    topics = MultipleChoiceField(
        widget=CustomCheckboxSelectMultiple, required=False)

~~    status = MultipleChoiceField(
        widget=CustomCheckboxSelectMultiple, required=False,
        choices=Submission.STATUS_CHOICE)

~~    countries = MultipleChoiceField(
        widget=CustomCheckboxSelectMultiple, required=False)

~~    affiliations = MultipleChoiceField(
        widget=CustomCheckboxSelectMultiple, required=False)

~~    proc_types = MultipleChoiceField(
        widget=CustomCheckboxSelectMultiple(
            attrs={'label': 'Proceedings'}), required=False)

~~    volumes = MultipleChoiceField(
        widget=CustomCheckboxSelectMultiple, required=False)

~~    quartiles = MultipleChoiceField(
        widget=CustomCheckboxSelectMultiple, required=False,
        choices=QUARTILE_CHOICES)

~~    artifacts = MultipleChoiceField(
        widget=CustomCheckboxSelectMultiple, required=False)

    order = ChoiceField(required=False, choices=ORDER_CHOICES)
    direction = ChoiceField(required=False, choices=DIRECTION_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert isinstance(self.instance, Conference)
        self.fields['types'].choices = [
            (x.pk, x.name) for x in self.instance.submissiontype_set.all()]
        self.fields['topics'].choices = [
            (x.pk, x.name) for x in self.instance.topic_set.all()]
        self.fields['proc_types'].choices = [('', 'Not defined')] + [
            (x.pk, x.name) for x in self.instance.proceedingtype_set.all()]
        self.fields['volumes'].choices = [('', 'Not defined')] + [
            (vol_pk, vol_name) for (vol_pk, vol_name) in
            self.instance.proceedingtype_set.values_list(
                'volumes__pk', 'volumes__name').distinct()]
        self.fields['artifacts'].choices = [
            (x.pk, f'{x.name} ({x.proc_type.name}') for x in
            ArtifactDescriptor.objects.filter(
                 proc_type__conference=self.instance)]

        profiles_data = Profile.objects.filter(


## ... source file abbreviated to get to MultipleChoiceField examples ...


    term = forms.CharField(required=False)

    authorship = forms.MultipleChoiceField(
        widget=CustomCheckboxSelectMultiple, required=False,
        choices=AUTHORSHIP_CHOICES,
    )

    countries = forms.MultipleChoiceField(
        widget=CustomCheckboxSelectMultiple, required=False,
    )

    affiliations = forms.MultipleChoiceField(
        widget=CustomCheckboxSelectMultiple, required=False,
    )

    graduation = forms.MultipleChoiceField(
        widget=CustomCheckboxSelectMultiple, required=False,
        choices=GRADUATION_CHOICES,
    )

    membership = forms.MultipleChoiceField(
        widget=CustomCheckboxSelectMultiple, required=False,
        choices=MEMBERSHIP_CHOICES,
    )

~~    reviewer = MultipleChoiceField(
        widget=CustomCheckboxSelectMultiple, required=False,
        choices=REVIEWER_CHOICES)

    order = ChoiceField(required=False, choices=ORDER_CHOICES)
    direction = ChoiceField(required=False, choices=DIRECTION_CHOICES)

    columns = forms.MultipleChoiceField(
        required=False, choices=COLUMNS,
        widget=CustomCheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert isinstance(self.instance, Conference)
        countries_dict = dict(countries)

        self.fields['countries'].choices = [
            (code, countries_dict[code]) for code in
            Profile.objects.filter(country__isnull=False).values_list(
                'country', flat=True).order_by('country').distinct()]

        self.fields['affiliations'].choices = [
            (aff, aff) for aff in
            Profile.objects.values_list('affiliation', flat=True).order_by(


## ... source file abbreviated to get to MultipleChoiceField examples ...


class ExportSubmissionsForm(Form):
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

~~    columns = MultipleChoiceField(
        widget=CustomCheckboxSelectMultiple(hide_apply_btn=True),
        required=False, choices=COLUMNS)

~~    status = MultipleChoiceField(
        widget=CustomCheckboxSelectMultiple(hide_apply_btn=True),
        required=False, choices=Submission.STATUS_CHOICE)

~~    countries = MultipleChoiceField(
        widget=CustomCheckboxSelectMultiple(hide_apply_btn=True),
        required=False)

~~    topics = MultipleChoiceField(
        widget=CustomCheckboxSelectMultiple(hide_apply_btn=True),
        required=False)

    def __init__(self, *args, conference=None, **kwargs):
        super().__init__(*args, **kwargs)
        if conference is None:
            raise ValueError('conference must be provided')
        self.conference = conference
        self.fields['columns'].initial = [
            self.ORDER_COLUMN, self.ID_COLUMN, self.TITLE_COLUMN,
            self.AUTHORS_COLUMN, self.STATUS_COLUMN]
        countries_list = list(
            set(p.country for p in Profile.objects.all() if p.country))
        countries_list.sort(key=lambda cnt: cnt.name)
        self.fields['countries'].choices = [
            (cnt.code, cnt.name) for cnt in countries_list]
        self.fields['topics'].choices = [
            (t.pk, t.name) for t in self.conference.topic_set.all()]

    def apply(self, request):
        submissions = Submission.objects.filter(conference=self.conference)
        if self.cleaned_data['status']:
            submissions = submissions.filter(
                status__in=self.cleaned_data['status'])


## ... source file continues with no further MultipleChoiceField examples...

```

