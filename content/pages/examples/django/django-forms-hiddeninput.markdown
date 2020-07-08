title: django.forms HiddenInput Example Code
category: page
slug: django-forms-hiddeninput-examples
sortorder: 500011268
toc: False
sidebartitle: django.forms HiddenInput
meta: Python example code for the HiddenInput class from the django.forms module of the Django project.


HiddenInput is a class within the django.forms module of the Django project.


## Example 1 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / review / forms.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/review/forms.py)

```python
# forms.py
from django import forms
~~from django.forms import Form, HiddenInput, CharField, ChoiceField, ModelForm

from conferences.models import ProceedingType, ProceedingVolume
from review.models import Review, check_review_details, ReviewDecision


class EditReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'technical_merit', 'relevance', 'originality', 'clarity',
            'details', 'submitted'
        ]

    submitted = forms.BooleanField(required=False)
    technical_merit = forms.ChoiceField(choices=Review.SCORE_CHOICES, required=False)
    relevance = forms.ChoiceField(choices=Review.SCORE_CHOICES, required=False)
    originality = forms.ChoiceField(choices=Review.SCORE_CHOICES, required=False)
    details = forms.CharField(widget=forms.Textarea(attrs={'rows': '5'}), required=False)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['submitted']:
            is_incomplete = False
            for score_field in self.instance.score_fields().keys():
                if not cleaned_data[score_field]:
                    self.add_error(score_field, 'Must select a score')
                    is_incomplete = True
            stype = self.instance.paper.stype
            if not check_review_details(cleaned_data['details'], stype):
                self.add_error(
                    'details',
                    f'Review details must have at least '
                    f'{stype.min_num_words_in_review} words'
                )
                is_incomplete = True
            if is_incomplete:
                self.cleaned_data['submitted'] = False
                raise forms.ValidationError('Review is incomplete')
        return cleaned_data


class UpdateReviewDecisionForm(ModelForm):
    class Meta:
        model = ReviewDecision
        fields = ['decision_type']


class UpdateVolumeForm(Form):
~~    volume = CharField(widget=HiddenInput(), required=False)

    def __init__(self, *args, instance=None, **kwargs):
        if not instance:
            raise ValueError('Decision instance is required')
        self.instance = instance
        kwargs.update({
            'initial': {
                'volume': str(instance.volume.pk) if instance.volume else '',
            }
        })
        super().__init__(*args, **kwargs)
        self.volume = None

    def clean_volume(self):
        try:
            pk = int(self.cleaned_data['volume'])
            volumes = ProceedingVolume.objects.filter(pk=pk)
            self.volume = volumes.first() if volumes.count() else None
        except ValueError:
            self.volume = None
        return self.cleaned_data['volume']

    def save(self, commit=True):
        self.instance.volume = self.volume


## ... source file continues with no further HiddenInput examples...

```


## Example 2 from django-flexible-subscriptions
[django-flexible-subscriptions](https://github.com/studybuffalo/django-flexible-subscriptions)
([project documentation](https://django-flexible-subscriptions.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-flexible-subscriptions/))
provides boilerplate code for adding subscription and recurrent billing
to [Django](/django.html) web applications. Various payment providers
can be added on the back end to run the transactions.

The django-flexible-subscriptions project is open sourced under the
[GNU General Public License v3.0](https://github.com/studybuffalo/django-flexible-subscriptions/blob/master/LICENSE).

[**django-flexible-subscriptions / subscriptions / views.py**](https://github.com/studybuffalo/django-flexible-subscriptions/blob/master/subscriptions/./views.py)

```python
# views.py
from copy import copy

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
from django.contrib.messages.views import SuccessMessageMixin
~~from django.forms import HiddenInput
from django.forms.models import inlineformset_factory
from django.http import HttpResponseRedirect
from django.http.response import HttpResponseNotAllowed, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.utils import timezone

from subscriptions import models, forms, abstract


class DashboardView(PermissionRequiredMixin, abstract.TemplateView):
    permission_required = 'subscriptions.subscriptions'
    raise_exception = True
    template_name = 'subscriptions/dashboard.html'


class TagListView(PermissionRequiredMixin, abstract.ListView):
    model = models.PlanTag
    permission_required = 'subscriptions.subscriptions'
    raise_exception = True
    context_object_name = 'tags'
    template_name = 'subscriptions/tag_list.html'



## ... source file abbreviated to get to HiddenInput examples ...


            payment_transaction = self.process_payment(
                payment_form=payment_form,
                plan_cost_form=plan_cost_form,
            )

            if payment_transaction:
                subscription = self.setup_subscription(
                    request.user, plan_cost_form.cleaned_data['plan_cost']
                )

                transaction = self.record_transaction(
                    subscription,
                    self.retrieve_transaction_date(payment_transaction)
                )

                return HttpResponseRedirect(
                    self.get_success_url(transaction_id=transaction.id)
                )

            messages.error(request, 'Error processing payment')

        return self.render_confirmation(request, **kwargs)

    def hide_form(self, form):
        for _, field in form.fields.items():
~~            field.widget = HiddenInput()

        return form

    def process_payment(self, *args, **kwargs):  # pylint: disable=unused-argument
        return True

    def setup_subscription(self, request_user, plan_cost):
        current_date = timezone.now()

        subscription = models.UserSubscription.objects.create(
            user=request_user,
            subscription=plan_cost,
            date_billing_start=current_date,
            date_billing_end=None,
            date_billing_last=current_date,
            date_billing_next=plan_cost.next_billing_datetime(current_date),
            active=True,
            cancelled=False,
        )

        try:
            group = self.subscription_plan.group
            group.user_set.add(request_user)
        except AttributeError:


## ... source file continues with no further HiddenInput examples...

```

