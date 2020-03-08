title: django.forms EmailField Python Code Examples
category: page
slug: django-forms-emailfield-examples
sortorder: 500013124
toc: False
sidebartitle: django.forms EmailField
meta: View Python code examples that show how to use the EmailField class within the forms module of the Django open source project. 


[EmailField](https://github.com/django/django/blob/master/django/forms/fields.py)
([documentation](https://docs.djangoproject.com/en/stable/ref/forms/fields/#emailfield)),
from the [Django](/django.html) `forms` module, enables safe handling of 
text intended to be stored and used as valid email addresses. The email address
data is collected via an HTTP POST request from an
[HTML](/hypertext-markup-language-html.html) form submission.

Note that EmailField can either be imported from `django.forms` or 
`django.forms.fields`. `django.forms` is more commonly used because it
is less characters to type for the equivalent effect.


## Example 1 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / users / forms.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/users/forms.py)

```python
import re

~~from django import forms
from django.core.exceptions import ValidationError
from django.forms import Form
from django.utils.translation import ugettext_lazy as _

from users.models import Profile, User, Subscriptions, generate_avatar


def has_cyrillic(text):
    return bool(re.search('[\u0400-\u04FF]', text))


def only_cyrillic(text):
    return bool(re.fullmatch('[\u0400-\u04FF\-]*', text))


class PersonalForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'first_name', 'last_name', 'first_name_rus', 'middle_name_rus',
            'last_name_rus', 'country', 'city', 'birthday', 'preferred_language'
        )
        widgets = {
            'birthday': forms.TextInput(attrs={'class': 'datepicker'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'e.g.: Ivan',
            'last_name': 'e.g.: Petrov',
            'first_name_rus': 'пр.: Иван',
            'middle_name_rus': 'пр.: Дмитриевич',
            'last_name_rus': 'пр.: Петров',
            'city': 'e.g.: Moscow',
            'birthday': 'e.g.: 1980-02-20',
        }
        for key, value in placeholders.items():
            self.fields[key].widget.attrs['placeholder'] = value

    def clean_first_name(self):
        if has_cyrillic(self.cleaned_data['first_name']):
            raise ValidationError(
                _('This field should be written in English'),
                code='invalid_language'
            )
        return self.cleaned_data['first_name']

    def clean_last_name(self):
        if has_cyrillic(self.cleaned_data['last_name']):
            raise ValidationError(
                _('This field should be written in English'),
                code='invalid_language'
            )
        return self.cleaned_data['last_name']

    def clean_city(self):
        if has_cyrillic(self.cleaned_data['city']):
            raise ValidationError(
                _('This field should be written in English'),
                code='invalid_language'
            )
        return self.cleaned_data['city']

    def clean_first_name_rus(self):
        if not only_cyrillic(self.cleaned_data['first_name_rus']):
            raise ValidationError(
                _('Field should contain only cyrillic characters'),
                code='invalid_language'
            )
        return self.cleaned_data['first_name_rus']

    def clean_middle_name_rus(self):
        if not only_cyrillic(self.cleaned_data['middle_name_rus']):
            raise ValidationError(
                _('Field should contain only cyrillic characters'),
                code='invalid_language'
            )
        return self.cleaned_data['middle_name_rus']

    def clean_last_name_rus(self):
        if not only_cyrillic(self.cleaned_data['last_name_rus']):
            raise ValidationError(
                _('Field should contain only cyrillic characters'),
                code='invalid_language'
            )
        return self.cleaned_data['last_name_rus']


class ProfessionalForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('affiliation', 'degree', 'role', 'ieee_member')

    def clean_affiliation(self):
        if has_cyrillic(self.cleaned_data['affiliation']):
            raise ValidationError(
                _('This field should be written in English'),
                code='invalid_language'
            )
        return self.cleaned_data['affiliation']


class SubscriptionsForm(forms.ModelForm):
    class Meta:
        model = Subscriptions
        fields = ('trans_email', 'info_email')


class PasswordProtectedForm(Form):
    password = forms.CharField(
        strip=False,
        label=_('Enter your password'),
        widget=forms.PasswordInput(attrs={'placeholder': _('Password')})
    )

    def clean_password(self):
        """Validate that the entered password is correct.
        """
        password = self.cleaned_data['password']
        if not self.user.check_password(password):
            raise forms.ValidationError(
                _("The password is incorrect"),
                code='password_incorrect'
            )
        return password


class DeleteUserForm(PasswordProtectedForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self):
        self.user.delete()


~~class UpdateEmailForm(PasswordProtectedForm):
~~    email = forms.EmailField(label=_('Enter your new email'))

~~    def __init__(self, user, *args, **kwargs):
~~        super().__init__(*args, **kwargs)
~~        self.user = user

~~    def save(self):
~~        self.user.email = self.cleaned_data['email']
~~        self.user.save()


class DeleteAvatarForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        if self.instance.avatar:
            self.instance.avatar.delete()
            self.instance.avatar_version += 1
            self.instance.avatar = generate_avatar(self.instance)
        return super().save(commit)

```


## Example 2 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / account / forms.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/account/forms.py)

```python
from __future__ import absolute_import

import warnings
from importlib import import_module

~~from django import forms
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core import exceptions, validators
from django.urls import reverse
from django.utils.translation import pgettext

from allauth.compat import ugettext, ugettext_lazy as _

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


class EmailAwarePasswordResetTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        ret = super(
            EmailAwarePasswordResetTokenGenerator, self)._make_hash_value(
                user, timestamp)
        sync_user_email_addresses(user)
        emails = set([user.email] if user.email else [])
        emails.update(
            EmailAddress.objects
            .filter(user=user)
            .values_list('email', flat=True))
        ret += '|'.join(sorted(emails))
        return ret


default_token_generator = EmailAwarePasswordResetTokenGenerator()


class PasswordVerificationMixin(object):
    def clean(self):
        cleaned_data = super(PasswordVerificationMixin, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if (password1 and password2) and password1 != password2:
            self.add_error(
                'password2', _("You must type the same password each time.")
            )
        return cleaned_data


class PasswordField(forms.CharField):

    def __init__(self, *args, **kwargs):
        render_value = kwargs.pop('render_value',
                                  app_settings.PASSWORD_INPUT_RENDER_VALUE)
        kwargs['widget'] = forms.PasswordInput(render_value=render_value,
                                               attrs={'placeholder':
                                                      kwargs.get("label")})
        super(PasswordField, self).__init__(*args, **kwargs)


class SetPasswordField(PasswordField):

    def __init__(self, *args, **kwargs):
        super(SetPasswordField, self).__init__(*args, **kwargs)
        self.user = None

    def clean(self, value):
        value = super(SetPasswordField, self).clean(value)
        value = get_adapter().clean_password(value, user=self.user)
        return value


class LoginForm(forms.Form):

    password = PasswordField(label=_("Password"))
    remember = forms.BooleanField(label=_("Remember Me"),
                                  required=False)

    user = None
    error_messages = {
        'account_inactive':
        _("This account is currently inactive."),

        'email_password_mismatch':
        _("The e-mail address and/or password you specified are not correct."),

        'username_password_mismatch':
        _("The username and/or password you specified are not correct."),
    }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)
        if app_settings.AUTHENTICATION_METHOD == AuthenticationMethod.EMAIL:
            login_widget = forms.TextInput(attrs={'type': 'email',
                                                  'placeholder':
                                                  _('E-mail address'),
                                                  'autofocus': 'autofocus'})
~~            login_field = forms.EmailField(label=_("E-mail"),
~~                                           widget=login_widget)
        elif app_settings.AUTHENTICATION_METHOD \
                == AuthenticationMethod.USERNAME:
            login_widget = forms.TextInput(attrs={'placeholder':
                                                  _('Username'),
                                                  'autofocus': 'autofocus'})
            login_field = forms.CharField(
                label=_("Username"),
                widget=login_widget,
                max_length=get_username_max_length())
        else:
            assert app_settings.AUTHENTICATION_METHOD \
                == AuthenticationMethod.USERNAME_EMAIL
            login_widget = forms.TextInput(attrs={'placeholder':
                                                  _('Username or e-mail'),
                                                  'autofocus': 'autofocus'})
            login_field = forms.CharField(label=pgettext("field label",
                                                         "Login"),
                                          widget=login_widget)
~~        self.fields["login"] = login_field
        set_form_field_order(self, ["login", "password", "remember"])
        if app_settings.SESSION_REMEMBER is not None:
            del self.fields['remember']

    def user_credentials(self):
        """
        Provides the credentials required to authenticate the user for
        login.
        """
        credentials = {}
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
            validators.validate_email(login)
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
                self.error_messages['%s_password_mismatch' % auth_method])
        return self.cleaned_data

    def login(self, request, redirect_url=None):
        ret = perform_login(request, self.user,
                            email_verification=app_settings.EMAIL_VERIFICATION,
                            redirect_url=redirect_url)
        remember = app_settings.SESSION_REMEMBER
        if remember is None:
            remember = self.cleaned_data['remember']
        if remember:
            request.session.set_expiry(app_settings.SESSION_COOKIE_AGE)
        else:
            request.session.set_expiry(0)
        return ret


class _DummyCustomSignupForm(forms.Form):

    def signup(self, request, user):
        """
        Invoked at signup time to complete the signup of the user.
        """
        pass


def _base_signup_form_class():
    """
    Currently, we inherit from the custom form, if any. This is all
    not very elegant, though it serves a purpose:

    - There are two signup forms: one for local accounts, and one for
      social accounts
    - Both share a common base (BaseSignupForm)

    - Given the above, how to put in a custom signup form? Which form
      would your custom form derive from, the local or the social one?
    """
    if not app_settings.SIGNUP_FORM_CLASS:
        return _DummyCustomSignupForm
    try:
        fc_module, fc_classname = app_settings.SIGNUP_FORM_CLASS.rsplit('.', 1)
    except ValueError:
        raise exceptions.ImproperlyConfigured('%s does not point to a form'
                                              ' class'
                                              % app_settings.SIGNUP_FORM_CLASS)
    try:
        mod = import_module(fc_module)
    except ImportError as e:
        raise exceptions.ImproperlyConfigured('Error importing form class %s:'
                                              ' "%s"' % (fc_module, e))
    try:
        fc_class = getattr(mod, fc_classname)
    except AttributeError:
        raise exceptions.ImproperlyConfigured('Module "%s" does not define a'
                                              ' "%s" class' % (fc_module,
                                                               fc_classname))
    if not hasattr(fc_class, 'signup'):
        if hasattr(fc_class, 'save'):
            warnings.warn("The custom signup form must offer"
                          " a `def signup(self, request, user)` method",
                          DeprecationWarning)
        else:
            raise exceptions.ImproperlyConfigured(
                'The custom signup form must implement a "signup" method')
    return fc_class


class BaseSignupForm(_base_signup_form_class()):
    username = forms.CharField(label=_("Username"),
                               min_length=app_settings.USERNAME_MIN_LENGTH,
                               widget=forms.TextInput(
                                   attrs={'placeholder':
                                          _('Username'),
                                          'autofocus': 'autofocus'}))
~~    email = forms.EmailField(widget=forms.TextInput(
~~        attrs={'type': 'email',
~~               'placeholder': _('E-mail address')}))

    def __init__(self, *args, **kwargs):
        email_required = kwargs.pop('email_required',
                                    app_settings.EMAIL_REQUIRED)
        self.username_required = kwargs.pop('username_required',
                                            app_settings.USERNAME_REQUIRED)
        super(BaseSignupForm, self).__init__(*args, **kwargs)
        username_field = self.fields['username']
        username_field.max_length = get_username_max_length()
        username_field.validators.append(
            validators.MaxLengthValidator(username_field.max_length))
        username_field.widget.attrs['maxlength'] = str(
            username_field.max_length)

        default_field_order = [
            'email',
            'email2',  # ignored when not present
            'username',
            'password1',
            'password2'  # ignored when not present
        ]
~~        if app_settings.SIGNUP_EMAIL_ENTER_TWICE:
~~            self.fields["email2"] = forms.EmailField(
~~                label=_("E-mail (again)"),
~~                widget=forms.TextInput(
~~                    attrs={
~~                        'type': 'email',
~~                        'placeholder': _('E-mail address confirmation')
~~                    }
~~                )
~~            )
~~        if email_required:
~~            self.fields['email'].label = ugettext("E-mail")
~~            self.fields['email'].required = True
~~        else:
~~            self.fields['email'].label = ugettext("E-mail (optional)")
~~            self.fields['email'].required = False
~~            self.fields['email'].widget.is_required = False
~~            if self.username_required:
~~                default_field_order = [
~~                    'username',
~~                    'email',
~~                    'email2',  # ignored when not present
~~                    'password1',
~~                    'password2'  # ignored when not present
~~                ]

        if not self.username_required:
            del self.fields["username"]

        set_form_field_order(
            self,
            getattr(self, 'field_order', None) or default_field_order)

    def clean_username(self):
        value = self.cleaned_data["username"]
        value = get_adapter().clean_username(value)
        return value

~~    def clean_email(self):
~~        value = self.cleaned_data['email']
~~        value = get_adapter().clean_email(value)
~~        if value and app_settings.UNIQUE_EMAIL:
~~            value = self.validate_unique_email(value)
~~        return value

~~    def validate_unique_email(self, value):
~~        return get_adapter().validate_unique_email(value)

~~    def clean(self):
~~        cleaned_data = super(BaseSignupForm, self).clean()
~~        if app_settings.SIGNUP_EMAIL_ENTER_TWICE:
~~            email = cleaned_data.get('email')
~~            email2 = cleaned_data.get('email2')
~~            if (email and email2) and email != email2:
~~                self.add_error(
~~                    'email2', _("You must type the same email each time.")
~~                )
~~        return cleaned_data

    def custom_signup(self, request, user):
        custom_form = super(BaseSignupForm, self)
        if hasattr(custom_form, 'signup') and callable(custom_form.signup):
            custom_form.signup(request, user)
        else:
            warnings.warn("The custom signup form must offer"
                          " a `def signup(self, request, user)` method",
                          DeprecationWarning)
            # Historically, it was called .save, but this is confusing
            # in case of ModelForm
            custom_form.save(user)


class SignupForm(BaseSignupForm):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['password1'] = PasswordField(label=_("Password"))
        if app_settings.SIGNUP_PASSWORD_ENTER_TWICE:
            self.fields['password2'] = PasswordField(
                label=_("Password (again)"))

        if hasattr(self, 'field_order'):
            set_form_field_order(self, self.field_order)

    def clean(self):
        super(SignupForm, self).clean()

        # `password` cannot be of type `SetPasswordField`, as we don't
        # have a `User` yet. So, let's populate a dummy user to be used
        # for password validaton.
        dummy_user = get_user_model()
        user_username(dummy_user, self.cleaned_data.get("username"))
        user_email(dummy_user, self.cleaned_data.get("email"))
        password = self.cleaned_data.get('password1')
        if password:
            try:
                get_adapter().clean_password(
                    password,
                    user=dummy_user)
            except forms.ValidationError as e:
                self.add_error('password1', e)

        if app_settings.SIGNUP_PASSWORD_ENTER_TWICE \
                and "password1" in self.cleaned_data \
                and "password2" in self.cleaned_data:
            if self.cleaned_data["password1"] \
                    != self.cleaned_data["password2"]:
                self.add_error(
                    'password2',
                    _("You must type the same password each time."))
        return self.cleaned_data

    def save(self, request):
        adapter = get_adapter(request)
        user = adapter.new_user(request)
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        # TODO: Move into adapter `save_user` ?
        setup_user_email(request, user, [])
        return user


class UserForm(forms.Form):

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super(UserForm, self).__init__(*args, **kwargs)


class AddEmailForm(UserForm):

~~    email = forms.EmailField(
~~        label=_("E-mail"),
~~        required=True,
~~        widget=forms.TextInput(
~~            attrs={"type": "email",
~~                   "size": "30",
~~                   "placeholder": _('E-mail address')}))

~~    def clean_email(self):
~~        value = self.cleaned_data["email"]
~~        value = get_adapter().clean_email(value)
~~        errors = {
~~            "this_account": _("This e-mail address is already associated"
~~                              " with this account."),
~~            "different_account": _("This e-mail address is already associated"
~~                                   " with another account."),
~~        }
~~        users = filter_users_by_email(value)
~~        on_this_account = [u for u in users if u.pk == self.user.pk]
~~        on_diff_account = [u for u in users if u.pk != self.user.pk]

 ~~       if on_this_account:
 ~~           raise forms.ValidationError(errors["this_account"])
 ~~       if on_diff_account and app_settings.UNIQUE_EMAIL:
 ~~           raise forms.ValidationError(errors["different_account"])
 ~~       return value

~~    def save(self, request):
~~        return EmailAddress.objects.add_email(request,
~~                                              self.user,
~~                                              self.cleaned_data["email"],
~~                                              confirm=True)


class ChangePasswordForm(PasswordVerificationMixin, UserForm):

    oldpassword = PasswordField(label=_("Current Password"))
    password1 = SetPasswordField(label=_("New Password"))
    password2 = PasswordField(label=_("New Password (again)"))

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['password1'].user = self.user

    def clean_oldpassword(self):
        if not self.user.check_password(self.cleaned_data.get("oldpassword")):
            raise forms.ValidationError(_("Please type your current"
                                          " password."))
        return self.cleaned_data["oldpassword"]

    def save(self):
        get_adapter().set_password(self.user, self.cleaned_data["password1"])


class SetPasswordForm(PasswordVerificationMixin, UserForm):

    password1 = SetPasswordField(label=_("Password"))
    password2 = PasswordField(label=_("Password (again)"))

    def __init__(self, *args, **kwargs):
        super(SetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['password1'].user = self.user

    def save(self):
        get_adapter().set_password(self.user, self.cleaned_data["password1"])


~~class ResetPasswordForm(forms.Form):

~~    email = forms.EmailField(
~~        label=_("E-mail"),
~~        required=True,
~~        widget=forms.TextInput(attrs={
~~            "type": "email",
~~            "size": "30",
~~            "placeholder": _("E-mail address"),
~~        })
~~    )

~~    def clean_email(self):
~~        email = self.cleaned_data["email"]
~~        email = get_adapter().clean_email(email)
~~        self.users = filter_users_by_email(email)
~~        if not self.users:
~~            raise forms.ValidationError(_("The e-mail address is not assigned"
~~                                          " to any user account"))
~~        return self.cleaned_data["email"]

    def save(self, request, **kwargs):
        current_site = get_current_site(request)
        email = self.cleaned_data["email"]
        token_generator = kwargs.get("token_generator",
                                     default_token_generator)

        for user in self.users:

            temp_key = token_generator.make_token(user)

            # save it to the password reset model
            # password_reset = PasswordReset(user=user, temp_key=temp_key)
            # password_reset.save()

            # send the password reset email
            path = reverse("account_reset_password_from_key",
                           kwargs=dict(uidb36=user_pk_to_url_str(user),
                                       key=temp_key))
            url = build_absolute_uri(
                request, path)

            context = {"current_site": current_site,
                       "user": user,
                       "password_reset_url": url,
                       "request": request}

            if app_settings.AUTHENTICATION_METHOD \
                    != AuthenticationMethod.EMAIL:
                context['username'] = user_username(user)
            get_adapter(request).send_mail(
                'account/email/password_reset_key',
                email,
                context)
        return self.cleaned_data["email"]


## ... source file continues with no further EmailField examples ...

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

[**django-mongonaut / mongonaut / forms / widgets.py**](https://github.com/jazzband/django-mongonaut/blob/master/mongonaut/forms/widgets.py)

```python
# -*- coding: utf-8 -*-

""" Widgets for mongonaut forms"""

~~from django import forms

from mongoengine.base import ObjectIdField
from mongoengine.fields import BooleanField
from mongoengine.fields import DateTimeField
from mongoengine.fields import EmbeddedDocumentField
from mongoengine.fields import ListField
from mongoengine.fields import ReferenceField
from mongoengine.fields import FloatField
from mongoengine.fields import EmailField
from mongoengine.fields import DecimalField
from mongoengine.fields import URLField
from mongoengine.fields import IntField
from mongoengine.fields import StringField
from mongoengine.fields import GeoPointField


def get_widget(model_field, disabled=False):
    """Choose which widget to display for a field."""

    attrs = get_attrs(model_field, disabled)

    if hasattr(model_field, "max_length") and not model_field.max_length:
        return forms.Textarea(attrs=attrs)

    elif isinstance(model_field, DateTimeField):
        return forms.DateTimeInput(attrs=attrs)

    elif isinstance(model_field, BooleanField):
        return forms.CheckboxInput(attrs=attrs)

    elif isinstance(model_field, ReferenceField) or model_field.choices:
        return forms.Select(attrs=attrs)

    elif (isinstance(model_field, ListField) or
          isinstance(model_field, EmbeddedDocumentField) or
          isinstance(model_field, GeoPointField)):
        return None

    else:
        return forms.TextInput(attrs=attrs)


def get_attrs(model_field, disabled=False):
    """Set attributes on the display widget."""
    attrs = {}
    attrs['class'] = 'span6 xlarge'
    if disabled or isinstance(model_field, ObjectIdField):
        attrs['class'] += ' disabled'
        attrs['readonly'] = 'readonly'
    return attrs


def get_form_field_class(model_field):
    """Gets the default form field  for a mongoenigne field."""

    FIELD_MAPPING = {
        IntField: forms.IntegerField,
        StringField: forms.CharField,
        FloatField: forms.FloatField,
        BooleanField: forms.BooleanField,
        DateTimeField: forms.DateTimeField,
        DecimalField: forms.DecimalField,
        URLField: forms.URLField,
~~        EmailField: forms.EmailField
    }

    return FIELD_MAPPING.get(model_field.__class__, forms.CharField)

```


## Example 4 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / users / forms.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/users/forms.py)

```python
import warnings
from itertools import groupby
from operator import itemgetter

from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.password_validation import (
    password_validators_help_text_html, validate_password)
from django.db import transaction
from django.db.models.fields import BLANK_CHOICE_DASH
from django.template.loader import render_to_string
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.locale import get_available_admin_languages, get_available_admin_time_zones
from wagtail.admin.widgets import AdminPageChooser
from wagtail.core import hooks
from wagtail.core.models import (
    PAGE_PERMISSION_TYPE_CHOICES, PAGE_PERMISSION_TYPES, GroupPagePermission, Page,
    UserPagePermissionsProxy)
from wagtail.users.models import UserProfile
from wagtail.utils import l18n

User = get_user_model()

# The standard fields each user model is expected to have, as a minimum.
standard_fields = set(['email', 'first_name', 'last_name', 'is_superuser', 'groups'])
# Custom fields
if hasattr(settings, 'WAGTAIL_USER_CUSTOM_FIELDS'):
    custom_fields = set(settings.WAGTAIL_USER_CUSTOM_FIELDS)
else:
    custom_fields = set()


class UsernameForm(forms.ModelForm):
    """
    Intelligently sets up the username field if it is in fact a username. If the
    User model has been swapped out, and the username field is an email or
    something else, don't touch it.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if User.USERNAME_FIELD == 'username':
            field = self.fields['username']
            field.regex = r"^[\w.@+-]+$"
            field.help_text = _("Required. 30 characters or fewer. Letters, "
                                "digits and @/./+/-/_ only.")
            field.error_messages = field.error_messages.copy()
            field.error_messages.update({
                'invalid': _("This value may contain only letters, numbers "
                             "and @/./+/-/_ characters.")})

    @property
    def username_field(self):
        return self[User.USERNAME_FIELD]

    def separate_username_field(self):
        return User.USERNAME_FIELD not in standard_fields


class UserForm(UsernameForm):
    required_css_class = "required"

    @property
    def password_required(self):
        return getattr(settings, 'WAGTAILUSERS_PASSWORD_REQUIRED', True)

    @property
    def password_enabled(self):
        return getattr(settings, 'WAGTAILUSERS_PASSWORD_ENABLED', True)

    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }

~~    email = forms.EmailField(required=True, label=_('Email'))
    first_name = forms.CharField(required=True, label=_('First Name'))
    last_name = forms.CharField(required=True, label=_('Last Name'))

    password1 = forms.CharField(
        label=_('Password'), required=False,
        widget=forms.PasswordInput,
        help_text=_("Leave blank if not changing."))
    password2 = forms.CharField(
        label=_("Password confirmation"), required=False,
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))

    is_superuser = forms.BooleanField(
        label=_("Administrator"), required=False,
        help_text=_('Administrators have full access to manage any object '
                    'or setting.'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.password_enabled:
            if self.password_required:
                self.fields['password1'].help_text = mark_safe(password_validators_help_text_html())
                self.fields['password1'].required = True
                self.fields['password2'].required = True
        else:
            del self.fields['password1']
            del self.fields['password2']

    # We cannot call this method clean_username since this the name of the
    # username field may be different, so clean_username would not be reliably
    # called. We therefore call _clean_username explicitly in _clean_fields.
    def _clean_username(self):
        username_field = User.USERNAME_FIELD
        # This method is called even if username if empty, contrary to clean_*
        # methods, so we have to check again here that data is defined.
        if username_field not in self.cleaned_data:
            return
        username = self.cleaned_data[username_field]

        users = User._default_manager.all()
        if self.instance.pk is not None:
            users = users.exclude(pk=self.instance.pk)
        if users.filter(**{username_field: username}).exists():
            self.add_error(User.USERNAME_FIELD, forms.ValidationError(
                self.error_messages['duplicate_username'],
                code='duplicate_username',
            ))
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password2 != password1:
            self.add_error('password2', forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            ))

        return password2

    def validate_password(self):
        """
        Run the Django password validators against the new password. This must
        be called after the user instance in self.instance is populated with
        the new data from the form, as some validators rely on attributes on
        the user model.
        """
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 == password2:
            validate_password(password1, user=self.instance)

    def _post_clean(self):
        super()._post_clean()
        try:
            self.validate_password()
        except forms.ValidationError as e:
            self.add_error('password2', e)

    def _clean_fields(self):
        super()._clean_fields()
        self._clean_username()

    def save(self, commit=True):
        user = super().save(commit=False)

        if self.password_enabled:
            password = self.cleaned_data['password1']
            if password:
                user.set_password(password)

        if commit:
            user.save()
            self.save_m2m()
        return user


class UserCreationForm(UserForm):
    class Meta:
        model = User
        fields = set([User.USERNAME_FIELD]) | standard_fields | custom_fields
        widgets = {
            'groups': forms.CheckboxSelectMultiple
        }


class UserEditForm(UserForm):
    password_required = False

    def __init__(self, *args, **kwargs):
        editing_self = kwargs.pop('editing_self', False)
        super().__init__(*args, **kwargs)

        if editing_self:
            del self.fields["is_active"]
            del self.fields["is_superuser"]

    class Meta:
        model = User
        fields = set([User.USERNAME_FIELD, "is_active"]) | standard_fields | custom_fields
        widgets = {
            'groups': forms.CheckboxSelectMultiple
        }


class GroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.registered_permissions = Permission.objects.none()
        for fn in hooks.get_hooks('register_permissions'):
            self.registered_permissions = self.registered_permissions | fn()
        self.fields['permissions'].queryset = self.registered_permissions.select_related('content_type')

    required_css_class = "required"

    error_messages = {
        'duplicate_name': _("A group with that name already exists."),
    }

    is_superuser = forms.BooleanField(
        label=_("Administrator"),
        required=False,
        help_text=_("Administrators have full access to manage any object or setting.")
    )

    class Meta:
        model = Group
        fields = ("name", "permissions", )
        widgets = {
            'permissions': forms.CheckboxSelectMultiple(),
        }

    def clean_name(self):
        # Since Group.name is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        name = self.cleaned_data["name"]
        try:
            Group._default_manager.exclude(pk=self.instance.pk).get(name=name)
        except Group.DoesNotExist:
            return name
        raise forms.ValidationError(self.error_messages['duplicate_name'])

    def save(self):
        # We go back to the object to read (in order to reapply) the
        # permissions which were set on this group, but which are not
        # accessible in the wagtail admin interface, as otherwise these would
        # be clobbered by this form.
        try:
            untouchable_permissions = self.instance.permissions.exclude(pk__in=self.registered_permissions)
            bool(untouchable_permissions)  # force this to be evaluated, as it's about to change
        except ValueError:
            # this form is not bound; we're probably creating a new group
            untouchable_permissions = []
        group = super().save()
        group.permissions.add(*untouchable_permissions)
        return group


class PagePermissionsForm(forms.Form):
    """
    Note 'Permissions' (plural). A single instance of this form defines the permissions
    that are assigned to an entity (i.e. group or user) for a specific page.
    """
    page = forms.ModelChoiceField(
        queryset=Page.objects.all(),
        widget=AdminPageChooser(show_edit_link=False, can_choose_root=True)
    )
    permission_types = forms.MultipleChoiceField(
        choices=PAGE_PERMISSION_TYPE_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple
    )


class BaseGroupPagePermissionFormSet(forms.BaseFormSet):
    permission_types = PAGE_PERMISSION_TYPES  # defined here for easy access from templates

    def __init__(self, data=None, files=None, instance=None, prefix='page_permissions'):
        if instance is None:
            instance = Group()

        self.instance = instance

        initial_data = []

        for page, page_permissions in groupby(
            instance.page_permissions.select_related('page').order_by('page'), lambda pp: pp.page
        ):
            initial_data.append({
                'page': page,
                'permission_types': [pp.permission_type for pp in page_permissions]
            })

        super().__init__(
            data, files, initial=initial_data, prefix=prefix
        )
        for form in self.forms:
            form.fields['DELETE'].widget = forms.HiddenInput()

    @property
    def empty_form(self):
        empty_form = super().empty_form
        empty_form.fields['DELETE'].widget = forms.HiddenInput()
        return empty_form

    def clean(self):
        """Checks that no two forms refer to the same page object"""
        if any(self.errors):
            # Don't bother validating the formset unless each form is valid on its own
            return

        pages = [
            form.cleaned_data['page']
            for form in self.forms
            # need to check for presence of 'page' in cleaned_data,
            # because a completely blank form passes validation
            if form not in self.deleted_forms and 'page' in form.cleaned_data
        ]
        if len(set(pages)) != len(pages):
            # pages list contains duplicates
            raise forms.ValidationError(_("You cannot have multiple permission records for the same page."))

    @transaction.atomic
    def save(self):
        if self.instance.pk is None:
            raise Exception(
                "Cannot save a GroupPagePermissionFormSet for an unsaved group instance"
            )

        # get a set of (page, permission_type) tuples for all ticked permissions
        forms_to_save = [
            form for form in self.forms
            if form not in self.deleted_forms and 'page' in form.cleaned_data
        ]

        final_permission_records = set()
        for form in forms_to_save:
            for permission_type in form.cleaned_data['permission_types']:
                final_permission_records.add((form.cleaned_data['page'], permission_type))

        # fetch the group's existing page permission records, and from that, build a list
        # of records to be created / deleted
        permission_ids_to_delete = []
        permission_records_to_keep = set()

        for pp in self.instance.page_permissions.all():
            if (pp.page, pp.permission_type) in final_permission_records:
                permission_records_to_keep.add((pp.page, pp.permission_type))
            else:
                permission_ids_to_delete.append(pp.pk)

        self.instance.page_permissions.filter(pk__in=permission_ids_to_delete).delete()

        permissions_to_add = final_permission_records - permission_records_to_keep
        GroupPagePermission.objects.bulk_create([
            GroupPagePermission(
                group=self.instance, page=page, permission_type=permission_type
            )
            for (page, permission_type) in permissions_to_add
        ])

    def as_admin_panel(self):
        return render_to_string('wagtailusers/groups/includes/page_permissions_formset.html', {
            'formset': self
        })


GroupPagePermissionFormSet = forms.formset_factory(
    PagePermissionsForm, formset=BaseGroupPagePermissionFormSet, extra=0, can_delete=True
)


class NotificationPreferencesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user_perms = UserPagePermissionsProxy(self.instance.user)
        if not user_perms.can_publish_pages():
            del self.fields['submitted_notifications']
        if not user_perms.can_edit_pages():
            del self.fields['approved_notifications']
            del self.fields['rejected_notifications']

    class Meta:
        model = UserProfile
        fields = ("submitted_notifications", "approved_notifications", "rejected_notifications")


def _get_language_choices():
    return sorted(BLANK_CHOICE_DASH + get_available_admin_languages(),
                  key=lambda l: l[1].lower())


class PreferredLanguageForm(forms.ModelForm):
    preferred_language = forms.ChoiceField(
        required=False, choices=_get_language_choices,
        label=_('Preferred language')
    )

    class Meta:
        model = UserProfile
        fields = ("preferred_language",)


~~class EmailForm(forms.ModelForm):
~~    email = forms.EmailField(required=True, label=_('Email'))

~~    class Meta:
~~        model = User
~~        fields = ("email",)


## ... source file continues with no further EmailField examples ...
```

