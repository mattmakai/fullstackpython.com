title: django.core validators code examples
category: page
slug: django-core-validators-examples
sortorder: 500011086
toc: False
sidebartitle: django.core validators
meta: Python example code for the validators function from the django.core module of the Django project.


validators is a function within the django.core module of the Django project.


## Example 1 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / account / forms.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/account/forms.py)

```python
# forms.py
from __future__ import absolute_import

import warnings
from importlib import import_module

from django import forms
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
~~from django.core import exceptions, validators
from django.urls import reverse
from django.utils.translation import gettext, gettext_lazy as _, pgettext

from ..utils import (
    build_absolute_uri,
    get_username_max_length,
    set_form_field_order,
)
from . import app_settings
from .adapter import get_adapter
from .app_settings import AuthenticationMethod
from .models import EmailAddress
from .utils import (
    filter_users_by_email,
    get_user_model,
    perform_login,
    setup_user_email,
    sync_user_email_addresses,
    url_str_to_user_pk,
    user_email,
    user_pk_to_url_str,
    user_username,
)



## ... source file abbreviated to get to validators examples ...


        login = self.cleaned_data["login"]
        if app_settings.AUTHENTICATION_METHOD == AuthenticationMethod.EMAIL:
            credentials["email"] = login
        elif (
                app_settings.AUTHENTICATION_METHOD ==
                AuthenticationMethod.USERNAME):
            credentials["username"] = login
        else:
            if self._is_login_email(login):
                credentials["email"] = login
            credentials["username"] = login
        credentials["password"] = self.cleaned_data["password"]
        return credentials

    def clean_login(self):
        login = self.cleaned_data['login']
        return login.strip()

    def _is_login_email(self, login):
        try:
~~            validators.validate_email(login)
            ret = True
        except exceptions.ValidationError:
            ret = False
        return ret

    def clean(self):
        super(LoginForm, self).clean()
        if self._errors:
            return
        credentials = self.user_credentials()
        user = get_adapter(self.request).authenticate(
            self.request,
            **credentials)
        if user:
            self.user = user
        else:
            auth_method = app_settings.AUTHENTICATION_METHOD
            if auth_method == app_settings.AuthenticationMethod.USERNAME_EMAIL:
                login = self.cleaned_data['login']
                if self._is_login_email(login):
                    auth_method = app_settings.AuthenticationMethod.EMAIL
                else:
                    auth_method = app_settings.AuthenticationMethod.USERNAME
            raise forms.ValidationError(


## ... source file abbreviated to get to validators examples ...


class BaseSignupForm(_base_signup_form_class()):
    username = forms.CharField(label=_("Username"),
                               min_length=app_settings.USERNAME_MIN_LENGTH,
                               widget=forms.TextInput(
                                   attrs={'placeholder':
                                          _('Username'),
                                          'autofocus': 'autofocus'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'type': 'email',
               'placeholder': _('E-mail address')}))

    def __init__(self, *args, **kwargs):
        email_required = kwargs.pop('email_required',
                                    app_settings.EMAIL_REQUIRED)
        self.username_required = kwargs.pop('username_required',
                                            app_settings.USERNAME_REQUIRED)
        super(BaseSignupForm, self).__init__(*args, **kwargs)
        username_field = self.fields['username']
        username_field.max_length = get_username_max_length()
        username_field.validators.append(
~~            validators.MaxLengthValidator(username_field.max_length))
        username_field.widget.attrs['maxlength'] = str(
            username_field.max_length)

        default_field_order = [
            'email',
            'email2',  # ignored when not present
            'username',
            'password1',
            'password2'  # ignored when not present
        ]
        if app_settings.SIGNUP_EMAIL_ENTER_TWICE:
            self.fields["email2"] = forms.EmailField(
                label=_("E-mail (again)"),
                widget=forms.TextInput(
                    attrs={
                        'type': 'email',
                        'placeholder': _('E-mail address confirmation')
                    }
                )
            )
        if email_required:
            self.fields['email'].label = gettext("E-mail")
            self.fields['email'].required = True
        else:


## ... source file continues with no further validators examples...

```


## Example 2 from django-rest-framework
[Django REST Framework](https://github.com/encode/django-rest-framework)
([project homepage and documentation](https://www.django-rest-framework.org/),
[PyPI package information](https://pypi.org/project/djangorestframework/)
and [more resources on Full Stack Python](/django-rest-framework-drf.html)),
often abbreviated as "DRF", is a popular [Django](/django.html) extension
for building [web APIs](/application-programming-interfaces.html).
The project has fantastic documentation and a wonderful
[quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)
that serve as examples of how to make it easier for newcomers
to get started.

The project is open sourced under the
[Encode OSS Ltd. license](https://github.com/encode/django-rest-framework/blob/master/LICENSE.md).

[**django-rest-framework / rest_framework / utils / field_mapping.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/utils/field_mapping.py)

```python
# field_mapping.py
import inspect

~~from django.core import validators
from django.db import models
from django.utils.text import capfirst

from rest_framework.compat import postgres_fields
from rest_framework.validators import UniqueValidator

NUMERIC_FIELD_TYPES = (
    models.IntegerField, models.FloatField, models.DecimalField, models.DurationField,
)


class ClassLookupDict:
    def __init__(self, mapping):
        self.mapping = mapping

    def __getitem__(self, key):
        if hasattr(key, '_proxy_class'):
            base_class = key._proxy_class
        else:
            base_class = key.__class__

        for cls in inspect.getmro(base_class):
            if cls in self.mapping:
                return self.mapping[cls]


## ... source file abbreviated to get to validators examples ...


    if isinstance(model_field, models.FilePathField):
        kwargs['path'] = model_field.path

        if model_field.match is not None:
            kwargs['match'] = model_field.match

        if model_field.recursive is not False:
            kwargs['recursive'] = model_field.recursive

        if model_field.allow_files is not True:
            kwargs['allow_files'] = model_field.allow_files

        if model_field.allow_folders is not False:
            kwargs['allow_folders'] = model_field.allow_folders

    if model_field.choices:
        kwargs['choices'] = model_field.choices
    else:
        max_value = next((
            validator.limit_value for validator in validator_kwarg
~~            if isinstance(validator, validators.MaxValueValidator)
        ), None)
        if max_value is not None and isinstance(model_field, NUMERIC_FIELD_TYPES):
            kwargs['max_value'] = max_value
            validator_kwarg = [
                validator for validator in validator_kwarg
~~                if not isinstance(validator, validators.MaxValueValidator)
            ]

        min_value = next((
            validator.limit_value for validator in validator_kwarg
~~            if isinstance(validator, validators.MinValueValidator)
        ), None)
        if min_value is not None and isinstance(model_field, NUMERIC_FIELD_TYPES):
            kwargs['min_value'] = min_value
            validator_kwarg = [
                validator for validator in validator_kwarg
~~                if not isinstance(validator, validators.MinValueValidator)
            ]

        if isinstance(model_field, models.URLField):
            validator_kwarg = [
                validator for validator in validator_kwarg
~~                if not isinstance(validator, validators.URLValidator)
            ]

        if isinstance(model_field, models.EmailField):
            validator_kwarg = [
                validator for validator in validator_kwarg
~~                if validator is not validators.validate_email
            ]

        if isinstance(model_field, models.SlugField):
            validator_kwarg = [
                validator for validator in validator_kwarg
~~                if validator is not validators.validate_slug
            ]

        if isinstance(model_field, models.GenericIPAddressField):
            validator_kwarg = [
                validator for validator in validator_kwarg
~~                if validator is not validators.validate_ipv46_address
            ]
        if isinstance(model_field, models.DecimalField):
            validator_kwarg = [
                validator for validator in validator_kwarg
~~                if not isinstance(validator, validators.DecimalValidator)
            ]

    max_length = getattr(model_field, 'max_length', None)
    if max_length is not None and (isinstance(model_field, (models.CharField, models.TextField, models.FileField))):
        kwargs['max_length'] = max_length
        validator_kwarg = [
            validator for validator in validator_kwarg
~~            if not isinstance(validator, validators.MaxLengthValidator)
        ]

    min_length = next((
        validator.limit_value for validator in validator_kwarg
~~        if isinstance(validator, validators.MinLengthValidator)
    ), None)
    if min_length is not None and isinstance(model_field, models.CharField):
        kwargs['min_length'] = min_length
        validator_kwarg = [
            validator for validator in validator_kwarg
~~            if not isinstance(validator, validators.MinLengthValidator)
        ]

    if getattr(model_field, 'unique', False):
        unique_error_message = model_field.error_messages.get('unique', None)
        if unique_error_message:
            unique_error_message = unique_error_message % {
                'model_name': model_field.model._meta.verbose_name,
                'field_label': model_field.verbose_name
            }
        validator = UniqueValidator(
            queryset=model_field.model._default_manager,
            message=unique_error_message)
        validator_kwarg.append(validator)

    if validator_kwarg:
        kwargs['validators'] = validator_kwarg

    return kwargs


def get_relation_kwargs(field_name, relation_info):
    model_field, related_model, to_many, to_field, has_through_model, reverse = relation_info
    kwargs = {
        'queryset': related_model._default_manager,


## ... source file continues with no further validators examples...

```


## Example 3 from django-wiki
[django-wiki](https://github.com/django-wiki/django-wiki)
([project documentation](https://django-wiki.readthedocs.io/en/master/),
[demo](https://demo.django-wiki.org/),
and [PyPI page](https://pypi.org/project/django-wiki/))
is a wiki system code library for [Django](/django.html)
projects that makes it easier to create user-editable content.
The project aims to provide necessary core features and then
have an easy plugin format for additional features, rather than
having every exhaustive feature built into the core system.
django-wiki is a rewrite of an earlier now-defunct project
named [django-simplewiki](https://code.google.com/p/django-simple-wiki/).

The code for django-wiki is provided as open source under the
[GNU General Public License 3.0](https://github.com/django-wiki/django-wiki/blob/master/COPYING).

[**django-wiki / src/wiki / forms.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/./forms.py)

```python
# forms.py
    "UserUpdateForm",
    "WikiSlugField",
    "SpamProtectionMixin",
    "CreateRootForm",
    "MoveForm",
    "EditForm",
    "SelectWidgetBootstrap",
    "TextInputPrepend",
    "CreateForm",
    "DeleteForm",
    "PermissionsForm",
    "DirFilterForm",
    "SearchForm",
]

from datetime import timedelta

from django import forms
from django.apps import apps
from django.contrib.auth import get_user_model
~~from django.core import validators
from django.core.validators import RegexValidator
from django.forms.widgets import HiddenInput
from django.shortcuts import get_object_or_404
from django.urls import Resolver404, resolve
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.translation import gettext, gettext_lazy as _, pgettext_lazy
from wiki import models
from wiki.conf import settings
from wiki.core import permissions
from wiki.core.diff import simple_merge
from wiki.core.plugins.base import PluginSettingsFormMixin
from wiki.editors import getEditor

from .forms_account_handling import UserCreationForm, UserUpdateForm

validate_slug_numbers = RegexValidator(
    r"^[0-9]+$",
    _("A 'slug' cannot consist solely of numbers."),
    "invalid",
    inverse_match=True,
)


class WikiSlugField(forms.CharField):

    default_validators = [validators.validate_slug, validate_slug_numbers]

    def __init__(self, *args, **kwargs):
        self.allow_unicode = kwargs.pop("allow_unicode", False)
        if self.allow_unicode:
            self.default_validators = [
~~                validators.validate_unicode_slug,
                validate_slug_numbers,
            ]
        super().__init__(*args, **kwargs)


def _clean_slug(slug, urlpath):
    if slug.startswith("_"):
        raise forms.ValidationError(gettext("A slug may not begin with an underscore."))
    if slug == "admin":
        raise forms.ValidationError(gettext("'admin' is not a permitted slug name."))

    if settings.URL_CASE_SENSITIVE:
        already_existing_slug = models.URLPath.objects.filter(slug=slug, parent=urlpath)
    else:
        slug = slug.lower()
        already_existing_slug = models.URLPath.objects.filter(
            slug__iexact=slug, parent=urlpath
        )
    if already_existing_slug:
        already_urlpath = already_existing_slug[0]
        if already_urlpath.article and already_urlpath.article.current_revision.deleted:
            raise forms.ValidationError(
                gettext('A deleted article with slug "%s" already exists.')
                % already_urlpath.slug


## ... source file continues with no further validators examples...

```

