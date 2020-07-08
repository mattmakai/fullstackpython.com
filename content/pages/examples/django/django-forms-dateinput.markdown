title: django.forms DateInput Example Code
category: page
slug: django-forms-dateinput-examples
sortorder: 500011262
toc: False
sidebartitle: django.forms DateInput
meta: Python example code for the DateInput class from the django.forms module of the Django project.


DateInput is a class within the django.forms module of the Django project.


## Example 1 from register
[register](https://github.com/ORGAN-IZE/register) is a [Django](/django.html),
[Bootstrap](/bootstrap-css.html), [PostgreSQL](/postgresql.html) project that is
open source under the
[GNU General Public License v3.0](https://github.com/ORGAN-IZE/register/blob/master/LICENSE).
This web application makes it easier for people to register as organ donors.
You can see the application live at
[https://register.organize.org/](https://register.organize.org/).

[**register / registration / forms.py**](https://github.com/ORGAN-IZE/register/blob/master/registration/./forms.py)

```python
# forms.py
from __future__ import unicode_literals

import logging
import re
import collections
import datetime

~~import django.forms
~~import django.forms.utils
~~import django.forms.widgets
import django.core.validators
import django.core.exceptions
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

import form_utils.forms
import requests
import dateutil.parser
import validate_email

logger = logging.getLogger(__name__)


REGISTRATION_CONFIGURATION_NAME = 'registration_configuration'

RE_NON_DECIMAL = re.compile(r'[^\d]+')
RE_NON_ALPHA = re.compile('[\W]+')
RE_POSTAL_CODE = re.compile(r'^[0-9]{5}$')
validate_postal_code = django.core.validators.RegexValidator(
    RE_POSTAL_CODE, _("Enter a valid postal code consisting 5 numbers."), 'invalid')


CHOICES_GENDER = (


## ... source file abbreviated to get to DateInput examples ...


            'clean_ssn': register_form_clean_ssn,
            'clean_license_id': register_form_clean_license_id,
            'api_errors': {},
            'skip_api_error_validation': False,
            'validate_organ_tissue_selection': conf.get('validate_organ_tissue_selection', None),
        })
    return cls


class RevokeForm(django.forms.Form):
    email = django.forms.EmailField(label=_('Email'))
    first_name = django.forms.CharField(
        label=_('First Name'), max_length=150, min_length=1)
    middle_name = django.forms.CharField(
        label=_('Middle Name'), max_length=150, min_length=0, required=False)
    last_name = django.forms.CharField(
        label=_('Last Name'), max_length=150, min_length=1)
    postal_code = django.forms.CharField(
        label=_('Postal Code'),
        max_length=5, min_length=5, validators=[validate_postal_code])
    gender = django.forms.ChoiceField(
        label=_('Gender'), choices=CHOICES_GENDER,
        widget=django.forms.RadioSelect)
    birthdate = django.forms.DateField(
        label=_('Birthdate'),
~~        widget=django.forms.DateInput(
            attrs={'placeholder': '__/__/____', 'class': 'date',}))
    agree_to_tos = django.forms.BooleanField(label='', widget=django.forms.widgets.CheckboxInput(attrs={'required': 'required', }))

    def clean_email(self):
        email = self.cleaned_data['email']
        if settings.DISABLE_EMAIL_VALIDATION:
            logger.warning(
                'Email validation disabled: DISABLE_EMAIL_VALIDATION is set')
            return email
        if not hasattr(settings, 'MAILGUN_PUBLIC_API_KEY'):
            logger.warning(
                'Cannot validate email: MAILGUN_PUBLIC_API_KEY not set')
            return email
        r = requests.get(
            'https://api.mailgun.net/v2/address/validate',
            data={'address': email, },
            auth=('api', settings.MAILGUN_PUBLIC_API_KEY))
        if r.status_code == 200:
            if r.json()['is_valid']:
                return email
        logger.warning('Cannot validate email: {}'.format(r.text))
        raise django.forms.ValidationError(_('Enter a valid email.'))




## ... source file continues with no further DateInput examples...

```

