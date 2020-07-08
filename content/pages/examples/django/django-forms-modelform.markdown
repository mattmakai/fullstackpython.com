title: django.forms ModelForm Example Code
category: page
slug: django-forms-modelform-examples
sortorder: 500011273
toc: False
sidebartitle: django.forms ModelForm
meta: Python example code for the ModelForm class from the django.forms module of the Django project.


ModelForm is a class within the django.forms module of the Django project.


## Example 1 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / proceedings / forms.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/proceedings/forms.py)

```python
# forms.py
~~from django.forms import ModelForm

from gears.widgets import DropdownSelectSubmit
from proceedings.models import CameraReady


EMPTY_VOLUME_LABEL = '(no volume)'


~~class UpdateVolumeForm(ModelForm):

    class Meta:
        model = CameraReady
        fields = ['volume']
        widgets = {
            'volume': DropdownSelectSubmit(
                empty_label=EMPTY_VOLUME_LABEL,
                label_class='font-weight-normal dccn-text-small',
                empty_label_class='text-warning-18',
                nonempty_label_class='text-success-18',
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['volume'].queryset = self.instance.proc_type.volumes.all()
        self.fields['volume'].empty_label = EMPTY_VOLUME_LABEL



## ... source file continues with no further ModelForm examples...

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

[**django-flexible-subscriptions / subscriptions / forms.py**](https://github.com/studybuffalo/django-flexible-subscriptions/blob/master/subscriptions/./forms.py)

```python
# forms.py
from django import forms
from django.core import validators
~~from django.forms import ModelForm
from django.utils import timezone

from subscriptions.conf import SETTINGS
from subscriptions.models import SubscriptionPlan, PlanCost


def assemble_cc_years():
    cc_years = []
    now = timezone.now()

    for year in range(now.year, now.year + 60):
        cc_years.append((year, year))

    return cc_years


~~class SubscriptionPlanForm(ModelForm):
    class Meta:
        model = SubscriptionPlan
        fields = [
            'plan_name', 'plan_description', 'group', 'tags', 'grace_period',
        ]


~~class PlanCostForm(ModelForm):
    class Meta:
        model = PlanCost
        fields = ['recurrence_period', 'recurrence_unit', 'cost']


class PaymentForm(forms.Form):
    CC_MONTHS = (
        ('1', '01 - January'),
        ('2', '02 - February'),
        ('3', '03 - March'),
        ('4', '04 - April'),
        ('5', '05 - May'),
        ('6', '06 - June'),
        ('7', '07 - July'),
        ('8', '08 - August'),
        ('9', '09 - September'),
        ('10', '10 - October'),
        ('11', '11 - November'),
        ('12', '12 - December'),
    )
    CC_YEARS = assemble_cc_years()

    cardholder_name = forms.CharField(
        label='Cardholder name',


## ... source file continues with no further ModelForm examples...

```


## Example 3 from django-sql-explorer
[django-sql-explorer](https://github.com/groveco/django-sql-explorer)
([PyPI page](https://pypi.org/project/django-sql-explorer/0.2/)),
also referred to as "SQL Explorer",
is a code library for the [Django](/django.html) Admin that allows
approved, authenticated users to view and execute direct database SQL
queries. The tool keeps track of executed queries so users can share them
with each other, as well as export results to downloadable formats.
django-sql-explorer is provided as open source under the
[MIT license](https://github.com/groveco/django-sql-explorer/blob/master/LICENSE).

[**django-sql-explorer / explorer / forms.py**](https://github.com/groveco/django-sql-explorer/blob/master/explorer/./forms.py)

```python
# forms.py
from django.db import DatabaseError
~~from django.forms import ModelForm, Field, ValidationError, BooleanField, CharField
from django.forms.widgets import CheckboxInput, Select

from explorer.app_settings import EXPLORER_DEFAULT_CONNECTION, EXPLORER_CONNECTIONS
from explorer.models import Query, MSG_FAILED_BLACKLIST


class SqlField(Field):

    def validate(self, value):

        query = Query(sql=value)

        passes_blacklist, failing_words = query.passes_blacklist()

        error = MSG_FAILED_BLACKLIST % ', '.join(failing_words) if not passes_blacklist else None

        if error:
            raise ValidationError(
                error,
                code="InvalidSql"
            )


~~class QueryForm(ModelForm):

    sql = SqlField()
    snapshot = BooleanField(widget=CheckboxInput, required=False)
    connection = CharField(widget=Select, required=False)

    def __init__(self, *args, **kwargs):
        super(QueryForm, self).__init__(*args, **kwargs)
        self.fields['connection'].widget.choices = self.connections
        if not self.instance.connection:
            self.initial['connection'] = EXPLORER_DEFAULT_CONNECTION
        self.fields['connection'].widget.attrs['class'] = 'form-control'

    def clean(self):
        if self.instance and self.data.get('created_by_user', None):
            self.cleaned_data['created_by_user'] = self.instance.created_by_user
        return super(QueryForm, self).clean()

    @property
    def created_by_user_email(self):
        return self.instance.created_by_user.email if self.instance.created_by_user else '--'

    @property
    def created_at_time(self):
        return self.instance.created_at.strftime('%Y-%m-%d')


## ... source file continues with no further ModelForm examples...

```

