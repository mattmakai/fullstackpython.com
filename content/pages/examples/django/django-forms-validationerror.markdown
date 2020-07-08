title: django.forms ValidationError Example Code
category: page
slug: django-forms-validationerror-examples
sortorder: 500011278
toc: False
sidebartitle: django.forms ValidationError
meta: Python example code for the ValidationError class from the django.forms module of the Django project.


ValidationError is a class within the django.forms module of the Django project.


## Example 1 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / socialaccount / helpers.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/socialaccount/helpers.py)

```python
# helpers.py
from django.contrib import messages
~~from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from allauth.account import app_settings as account_settings
from allauth.account.adapter import get_adapter as get_account_adapter
from allauth.account.utils import complete_signup, perform_login, user_username
from allauth.exceptions import ImmediateHttpResponse

from . import app_settings, signals
from .adapter import get_adapter
from .models import SocialLogin
from .providers.base import AuthError, AuthProcess


def _process_signup(request, sociallogin):
    auto_signup = get_adapter(request).is_auto_signup_allowed(
        request,
        sociallogin)
    if not auto_signup:
        request.session['socialaccount_sociallogin'] = sociallogin.serialize()
        url = reverse('socialaccount_signup')
        ret = HttpResponseRedirect(url)
    else:
        if account_settings.USER_MODEL_USERNAME_FIELD:
            username = user_username(sociallogin.user)
            try:
                get_account_adapter(request).clean_username(username)
~~            except ValidationError:
                user_username(sociallogin.user, '')
        if not get_adapter(request).is_open_for_signup(
                request,
                sociallogin):
            return render(
                request,
                "account/signup_closed." +
                account_settings.TEMPLATE_EXTENSION)
        get_adapter(request).save_user(request, sociallogin, form=None)
        ret = complete_social_signup(request, sociallogin)
    return ret


def _login_social_account(request, sociallogin):
    return perform_login(request, sociallogin.user,
                         email_verification=app_settings.EMAIL_VERIFICATION,
                         redirect_url=sociallogin.get_redirect_url(request),
                         signal_kwargs={"sociallogin": sociallogin})


def render_authentication_error(request,
                                provider_id,
                                error=AuthError.UNKNOWN,
                                exception=None,


## ... source file continues with no further ValidationError examples...

```


## Example 2 from django-jsonfield
[django-jsonfield](https://github.com/dmkoch/django-jsonfield)
([jsonfield on PyPi](https://pypi.org/project/jsonfield/)) is a
[Django](/django.html) code library that makes it easier to store validated
JSON in a [Django object-relational mapper (ORM)](/django-orm.html) database
model.

The django-jsonfield project is open source under the
[MIT license](https://github.com/dmkoch/django-jsonfield/blob/master/LICENSE).

[**django-jsonfield / src/jsonfield / fields.py**](https://github.com/dmkoch/django-jsonfield/blob/master/src/jsonfield/./fields.py)

```python
# fields.py
import copy
import json
import warnings

from django.db import models
~~from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _

from . import forms
from .encoder import JSONEncoder
from .json import JSONString, checked_loads

DEFAULT_DUMP_KWARGS = {
    'cls': JSONEncoder,
}

DEFAULT_LOAD_KWARGS = {}

INVALID_JSON_WARNING = (
    '{0!s} failed to load invalid json ({1}) from the database. The value has '
    'been returned as a string instead.'
)


class JSONFieldMixin(models.Field):
    form_class = forms.JSONField

    def __init__(self, *args, dump_kwargs=None, load_kwargs=None, **kwargs):
        self.dump_kwargs = DEFAULT_DUMP_KWARGS if dump_kwargs is None else dump_kwargs
        self.load_kwargs = DEFAULT_LOAD_KWARGS if load_kwargs is None else load_kwargs

        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()

        if self.dump_kwargs != DEFAULT_DUMP_KWARGS:
            kwargs['dump_kwargs'] = self.dump_kwargs
        if self.load_kwargs != DEFAULT_LOAD_KWARGS:
            kwargs['load_kwargs'] = self.load_kwargs

        return name, path, args, kwargs

    def to_python(self, value):
        try:
            return checked_loads(value, **self.load_kwargs)
        except ValueError:
~~            raise ValidationError(_("Enter valid JSON."))

    def from_db_value(self, value, expression, connection):
        if value is None:
            return None

        try:
            return checked_loads(value, **self.load_kwargs)
        except json.JSONDecodeError:
            warnings.warn(INVALID_JSON_WARNING.format(self, value), RuntimeWarning)
            return JSONString(value)

    def get_prep_value(self, value):
        if self.null and value is None:
            return None
        return json.dumps(value, **self.dump_kwargs)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return json.dumps(value, **self.dump_kwargs)

    def formfield(self, **kwargs):
        kwargs.setdefault('form_class', self.form_class)
        if issubclass(kwargs['form_class'], forms.JSONField):
            kwargs.setdefault('dump_kwargs', self.dump_kwargs)


## ... source file continues with no further ValidationError examples...

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
~~            raise ValidationError(
                error,
                code="InvalidSql"
            )


class QueryForm(ModelForm):

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


## ... source file continues with no further ValidationError examples...

```


## Example 4 from register
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


## ... source file abbreviated to get to ValidationError examples ...


class StateLookupForm(django.forms.Form):
    email = django.forms.EmailField(label=_('Email'), help_text=_('so we can send you confirmation of your registration'))
    postal_code = django.forms.CharField(
        label=_('Postal Code'),
        max_length=5, min_length=5, validators=[validate_postal_code],
        help_text=_('to determine which series of state-based questions we will ask next'))

    def clean_email(self):
        email = self.cleaned_data['email']
        if settings.DISABLE_EMAIL_VALIDATION:
            logger.warning('Email validation disabled: DISABLE_EMAIL_VALIDATION '
                           'is set')
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
~~        raise django.forms.ValidationError(_('Enter a valid email.'))


class UPENNStateLookupForm(StateLookupForm):
    error_css_class = 'invalid-data-error'
    email = django.forms.EmailField(label='')
    postal_code = django.forms.CharField(label='', max_length=5, min_length=5, validators=[validate_postal_code])

    email.widget.attrs['placeholder'] = 'EMAIL'
    email.widget.attrs['class'] = 'upenn-text-field'

    postal_code.widget.attrs['placeholder'] = 'POSTAL CODE'
    postal_code.widget.attrs['class'] = 'upenn-text-field'


def register_form_clean(self):
    cleaned_data = super(self.__class__, self).clean()

    if self.validate_organ_tissue_selection:
        organ_choices = [value for key, value in cleaned_data.items() if key.startswith('include')]
        if organ_choices:
            if not any(organ_choices):
~~                raise django.forms.ValidationError(_('At least one organ/tissue needs to be selected'))

    if self.api_errors and not self.skip_api_error_validation:
        for k, v in self.api_errors.items():
            if k in self.fields:
                self.add_error(k, v)

    return cleaned_data


def register_form_clean_license_id(self):
    license_id = self.cleaned_data['license_id']
    if self.fields['license_id'].required and is_license_id_not_applicable(license_id):
~~        raise django.forms.ValidationError(_('License ID is required.'))
    return license_id


def is_license_id_not_applicable(license_id):
    not_applicable_list = ['na', 'n/a', ]
    if license_id.lower() in not_applicable_list:
        return True
    return False


def register_form_clean_birthdate(self):
    date = self.cleaned_data['birthdate']
    if not date:
        return date
    if date >= datetime.date.today():
~~        raise django.forms.ValidationError(_('Enter an accurate birthdate.'))
    return date


def register_form_clean_phone_number(self):
    phone_number = self.cleaned_data['phone_number']
    if not phone_number:
        return phone_number
    phone_number = RE_NON_DECIMAL.sub('', phone_number)
    if phone_number.startswith('1'):
        phone_number = phone_number[1:]
    if len(phone_number) != 10:
~~        raise django.forms.ValidationError(
            _('Enter an accurate phone number including area code.'))
    return phone_number


def register_form_clean_ssn(self):
    ssn = self.cleaned_data['ssn']
    if not ssn:
        return ssn
    if len(ssn) != 4:
~~        raise django.forms.ValidationError(
            _('Enter the last 4 digits of your social security number.'))
    try:
        int(ssn)
    except ValueError:
~~        raise django.forms.ValidationError(_('Enter only digits.'))
    return ssn


def validate_date_generator(min_value):
    min_value = dateutil.parser.parse(min_value).date()

    def validate_date(date):
        if date < min_value:
~~            raise django.forms.ValidationError(
                _('Date must be later than %(date)s.') %
                {'date': min_value.strftime('%m/%d/%Y'), },
                code='minimum')

    return validate_date


def register_form_generator(conf):
    fieldsets = []
    fields = collections.OrderedDict()
    for index, fieldset_def in enumerate(conf['fieldsets']):
        fieldset_title = _(fieldset_def['title'])
        fieldset_fields = fieldset_def['fields']

        if not fieldset_fields:
            continue
        fieldset = (unicode(index), {'legend': fieldset_title, 'fields': []}, )

        has_booleans = False

        for field_def in fieldset_def['fields']:
            field_name = field_def['field_name']
            field_type = field_def.get('type')
            label = _(field_def['human_name']) or ''


## ... source file abbreviated to get to ValidationError examples ...


        widget=django.forms.RadioSelect)
    birthdate = django.forms.DateField(
        label=_('Birthdate'),
        widget=django.forms.DateInput(
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
~~        raise django.forms.ValidationError(_('Enter a valid email.'))


class EmailNextOfKinForm(django.forms.Form):
    to = MultiEmailField(label=_('To'), max_length=300, help_text=_('Enter one or more emails separated by commas.'))
    subject = django.forms.CharField(label=_('Subject'), max_length=250)
    body = django.forms.CharField(label=_('Body'), widget=django.forms.widgets.Textarea())

    def clean_to(self):
        emails = self.cleaned_data['to']
        if settings.DISABLE_EMAIL_VALIDATION:
            logger.warning('Email validation disabled: DISABLE_EMAIL_VALIDATION is set')
            return emails
        if not hasattr(settings, 'MAILGUN_PUBLIC_API_KEY'):
            logger.warning('Cannot validate email: MAILGUN_PUBLIC_API_KEY not set')
            return emails
        valid_emails = []
        invalid_emails = []
        for email in emails:
            r = requests.get('https://api.mailgun.net/v2/address/validate',
                             data={'address': email, },
                             auth=('api', settings.MAILGUN_PUBLIC_API_KEY))
            if r.status_code == 200 and r.json()['is_valid']:
                valid_emails.append(email)
            else:
                logger.warning('Cannot validate email: {}'.format(r.text))
                invalid_emails.append(email)
        if invalid_emails:
~~            raise django.forms.ValidationError(_('Enter valid email addresses.'))
        else:
            return valid_emails



## ... source file continues with no further ValidationError examples...

```

