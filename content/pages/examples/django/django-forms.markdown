title: django.forms Example Code
category: page
slug: django-forms-examples
sortorder: 500013100
toc: False
sidebartitle: django.forms
meta: Python code examples for the forms module in the Django open source project. 


[forms](https://github.com/django/django/tree/master/django/forms) is a 
module within the [Django](/django.html) project for safely handling user
input in a [web application](/web-development.html).


## Example 1 from mezzanine
[mezzanine](https://github.com/stephenmcd/mezzanine) is a 
[Django](/django.html)-based content management system (CMS) with code
that is open source under the
[BSD 2-Clause "Simplified" License](https://github.com/stephenmcd/mezzanine/blob/master/LICENSE).

[**mezzanine/forms/forms.py**](https://github.com/stephenmcd/mezzanine/blob/master/mezzanine/forms/forms.py)

```python
from __future__ import unicode_literals
from future.builtins import int, range, str

from datetime import date, datetime
from os.path import join, split
from uuid import uuid4

~~from django import forms
~~try:
~~    from django.forms.widgets import SelectDateWidget
~~except ImportError:
~~    # Django 1.8
~~    from django.forms.extras.widgets import SelectDateWidget

from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.template import Template
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from django.utils.timezone import now

from mezzanine.conf import settings
~~from mezzanine.forms import fields
~~from mezzanine.forms.models import FormEntry, FieldEntry
from mezzanine.utils.email import split_addresses as split_choices


fs = FileSystemStorage(location=settings.FORMS_UPLOAD_ROOT)

##############################
# Each type of export filter #
##############################

# Text matches
FILTER_CHOICE_CONTAINS = "1"
FILTER_CHOICE_DOESNT_CONTAIN = "2"

# Exact matches
FILTER_CHOICE_EQUALS = "3"
FILTER_CHOICE_DOESNT_EQUAL = "4"

# Greater/less than
FILTER_CHOICE_BETWEEN = "5"

# Multiple values
FILTER_CHOICE_CONTAINS_ANY = "6"
FILTER_CHOICE_CONTAINS_ALL = "7"
FILTER_CHOICE_DOESNT_CONTAIN_ANY = "8"
FILTER_CHOICE_DOESNT_CONTAIN_ALL = "9"

##########################
# Export filters grouped #
##########################

# Text fields
TEXT_FILTER_CHOICES = (
    ("", _("Nothing")),
    (FILTER_CHOICE_CONTAINS, _("Contains")),
    (FILTER_CHOICE_DOESNT_CONTAIN, _("Doesn't contain")),
    (FILTER_CHOICE_EQUALS, _("Equals")),
    (FILTER_CHOICE_DOESNT_EQUAL, _("Doesn't equal")),
)

# Choices with single value entries
CHOICE_FILTER_CHOICES = (
    ("", _("Nothing")),
    (FILTER_CHOICE_CONTAINS_ANY, _("Equals any")),
    (FILTER_CHOICE_DOESNT_CONTAIN_ANY, _("Doesn't equal any")),
)

# Choices with multiple value entries
MULTIPLE_FILTER_CHOICES = (
    ("", _("Nothing")),
    (FILTER_CHOICE_CONTAINS_ANY, _("Contains any")),
    (FILTER_CHOICE_CONTAINS_ALL, _("Contains all")),
    (FILTER_CHOICE_DOESNT_CONTAIN_ANY, _("Doesn't contain any")),
    (FILTER_CHOICE_DOESNT_CONTAIN_ALL, _("Doesn't contain all")),
)

# Dates
DATE_FILTER_CHOICES = (
    ("", _("Nothing")),
    (FILTER_CHOICE_BETWEEN, _("Is between")),
)

# The filter function for each filter type
FILTER_FUNCS = {
    FILTER_CHOICE_CONTAINS:
        lambda val, field: val.lower() in field.lower(),
    FILTER_CHOICE_DOESNT_CONTAIN:
        lambda val, field: val.lower() not in field.lower(),
    FILTER_CHOICE_EQUALS:
        lambda val, field: val.lower() == field.lower(),
    FILTER_CHOICE_DOESNT_EQUAL:
        lambda val, field: val.lower() != field.lower(),
    FILTER_CHOICE_BETWEEN:
        lambda val_from, val_to, field: (
            (not val_from or val_from <= field) and
            (not val_to or val_to >= field)
        ),
    FILTER_CHOICE_CONTAINS_ANY:
        lambda val, field: set(val) & set(split_choices(field)),
    FILTER_CHOICE_CONTAINS_ALL:
        lambda val, field: set(val) == set(split_choices(field)),
    FILTER_CHOICE_DOESNT_CONTAIN_ANY:
        lambda val, field: not set(val) & set(split_choices(field)),
    FILTER_CHOICE_DOESNT_CONTAIN_ALL:
        lambda val, field: set(val) != set(split_choices(field)),
}

# Export form fields for each filter type grouping
~~text_filter_field = forms.ChoiceField(label=" ", required=False,
~~                                      choices=TEXT_FILTER_CHOICES)
~~choice_filter_field = forms.ChoiceField(label=" ", required=False,
~~                                        choices=CHOICE_FILTER_CHOICES)
~~multiple_filter_field = forms.ChoiceField(label=" ", required=False,
~~                                          choices=MULTIPLE_FILTER_CHOICES)
~~date_filter_field = forms.ChoiceField(label=" ", required=False,
~~                                      choices=DATE_FILTER_CHOICES)


~~class FormForForm(forms.ModelForm):
    """
    Form with a set of fields dynamically assigned, directly based on the
    given ``forms.models.Form`` instance.
    """

    class Meta:
        model = FormEntry
        exclude = ("form", "entry_time")

~~    def __init__(self, form, context, *args, **kwargs):
        """
        Dynamically add each of the form fields for the given form model
        instance and its related field model instances.
        """
~~        self.form = form
~~        self.form_fields = form.fields.visible()
        initial = kwargs.pop("initial", {})
        # If a FormEntry instance is given to edit, populate initial
        # with its field values.
        field_entries = {}
        if kwargs.get("instance"):
            for field_entry in kwargs["instance"].fields.all():
                field_entries[field_entry.field_id] = field_entry.value
        super(FormForForm, self).__init__(*args, **kwargs)
        # Create the form fields.
~~        for field in self.form_fields:
~~            field_key = "field_%s" % field.id
~~            field_class = fields.CLASSES[field.field_type]
~~            field_widget = fields.WIDGETS.get(field.field_type)
~~            field_args = {"label": field.label, "required": field.required,
~~                          "help_text": field.help_text}
~~            arg_names = field_class.__init__.__code__.co_varnames
~~            if "max_length" in arg_names:
~~                field_args["max_length"] = settings.FORMS_FIELD_MAX_LENGTH
~~            if "choices" in arg_names:
~~                choices = list(field.get_choices())
~~                if (field.field_type == fields.SELECT and
~~                        field.default not in [c[0] for c in choices]):
~~                    choices.insert(0, ("", field.placeholder_text))
~~                field_args["choices"] = choices
~~            if field_widget is not None:
~~                field_args["widget"] = field_widget
            #
            #   Initial value for field, in order of preference:
            #
            # - If a form model instance is given (eg we're editing a
            #   form response), then use the instance's value for the
            #   field.
            # - If the developer has provided an explicit "initial"
            #   dict, use it.
            # - The default value for the field instance as given in
            #   the admin.
            #
            initial_val = None
~~            try:
~~                initial_val = field_entries[field.id]
~~            except KeyError:
~~                try:
~~                    initial_val = initial[field_key]
~~                except KeyError:
~~                    initial_val = str(Template(field.default).render(context))
~~            if initial_val:
~~                if field.is_a(*fields.MULTIPLE):
~~                    initial_val = split_choices(initial_val)
~~                elif field.field_type == fields.CHECKBOX:
~~                    initial_val = initial_val != "False"
~~                self.initial[field_key] = initial_val
~~            self.fields[field_key] = field_class(**field_args)
~~
~~            if field.field_type == fields.DOB:
~~                _now = datetime.now()
~~                years = list(range(_now.year, _now.year - 120, -1))
~~                self.fields[field_key].widget.years = years
~~
~~            # Add identifying type attr to the field for styling.
~~            setattr(self.fields[field_key], "type",
~~                    field_class.__name__.lower())
~~            if (field.required and settings.FORMS_USE_HTML5 and
~~                    field.field_type != fields.CHECKBOX_MULTIPLE):
~~                self.fields[field_key].widget.attrs["required"] = ""
~~            if field.placeholder_text and not field.default:
~~                text = field.placeholder_text
~~                self.fields[field_key].widget.attrs["placeholder"] = text

~~    def save(self, **kwargs):
~~        """
~~        Create a ``FormEntry`` instance and related ``FieldEntry``
~~        instances for each form field.
~~        """
~~        entry = super(FormForForm, self).save(commit=False)
~~        entry.form = self.form
~~        entry.entry_time = now()
~~        entry.save()
~~        entry_fields = entry.fields.values_list("field_id", flat=True)
~~        new_entry_fields = []
~~        for field in self.form_fields:
~~            field_key = "field_%s" % field.id
~~            value = self.cleaned_data[field_key]
~~            if value and self.fields[field_key].widget.needs_multipart_form:
~~                value = fs.save(join("forms", str(uuid4()), value.name), value)
~~            if isinstance(value, list):
~~                value = ", ".join([v.strip() for v in value])
~~            if field.id in entry_fields:
~~                field_entry = entry.fields.get(field_id=field.id)
~~                field_entry.value = value
~~                field_entry.save()
~~            else:
~~                new = {"entry": entry, "field_id": field.id, "value": value}
~~                new_entry_fields.append(FieldEntry(**new))
~~        if new_entry_fields:
~~            FieldEntry.objects.bulk_create(new_entry_fields)
~~        return entry

    def email_to(self):
        """
        Return the value entered for the first field of type
        ``forms.EmailField``.
        """
        for field in self.form_fields:
            if issubclass(fields.CLASSES[field.field_type], forms.EmailField):
                return self.cleaned_data["field_%s" % field.id]
        return None


~~class EntriesForm(forms.Form):
    """
    Form with a set of fields dynamically assigned that can be used to
    filter entries for the given ``forms.models.Form`` instance.
    """

~~    def __init__(self, form, request, *args, **kwargs):
        """
        Iterate through the fields of the ``forms.models.Form`` instance and
        create the form fields required to control including the field in
        the export (with a checkbox) or filtering the field which differs
        across field types. User a list of checkboxes when a fixed set of
        choices can be chosen from, a pair of date fields for date ranges,
        and for all other types provide a textbox for text search.
        """
~~        self.form = form
~~        self.request = request
~~        self.form_fields = form.fields.all()
~~        self.entry_time_name = str(FormEntry._meta.get_field(
~~            "entry_time").verbose_name)
~~        super(EntriesForm, self).__init__(*args, **kwargs)
~~        for field in self.form_fields:
~~            field_key = "field_%s" % field.id
~~            # Checkbox for including in export.
~~            self.fields["%s_export" % field_key] = forms.BooleanField(
~~                label=field.label, initial=True, required=False)
~~            if field.is_a(*fields.CHOICES):
~~                # A fixed set of choices to filter by.
~~                if field.is_a(fields.CHECKBOX):
~~                    choices = ((True, _("Checked")), (False, _("Not checked")))
~~                else:
~~                    choices = field.get_choices()
~~                contains_field = forms.MultipleChoiceField(label=" ",
~~                    choices=choices, widget=forms.CheckboxSelectMultiple(),
~~                    required=False)
~~                self.fields["%s_filter" % field_key] = choice_filter_field
~~                self.fields["%s_contains" % field_key] = contains_field
~~            elif field.is_a(*fields.MULTIPLE):
~~                # A fixed set of choices to filter by, with multiple
~~                # possible values in the entry field.
~~                contains_field = forms.MultipleChoiceField(label=" ",
~~                    choices=field.get_choices(),
~~                    widget=forms.CheckboxSelectMultiple(),
~~                    required=False)
~~                self.fields["%s_filter" % field_key] = multiple_filter_field
~~                self.fields["%s_contains" % field_key] = contains_field
~~            elif field.is_a(*fields.DATES):
~~                # A date range to filter by.
~~                self.fields["%s_filter" % field_key] = date_filter_field
~~                self.fields["%s_from" % field_key] = forms.DateField(
~~                    label=" ", widget=SelectDateWidget(), required=False)
~~                self.fields["%s_to" % field_key] = forms.DateField(
~~                    label=_("and"), widget=SelectDateWidget(), required=False)
~~            else:
~~                # Text box for search term to filter by.
~~                contains_field = forms.CharField(label=" ", required=False)
~~                self.fields["%s_filter" % field_key] = text_filter_field
~~                self.fields["%s_contains" % field_key] = contains_field
~~        # Add ``FormEntry.entry_time`` as a field.
~~        field_key = "field_0"
~~        self.fields["%s_export" % field_key] = forms.BooleanField(initial=True,
~~            label=FormEntry._meta.get_field("entry_time").verbose_name,
~~            required=False)
~~        self.fields["%s_filter" % field_key] = date_filter_field
~~        self.fields["%s_from" % field_key] = forms.DateField(
~~            label=" ", widget=SelectDateWidget(), required=False)
~~        self.fields["%s_to" % field_key] = forms.DateField(
~~            label=_("and"), widget=SelectDateWidget(), required=False)

~~    def __iter__(self):
~~        """
~~        Yield pairs of include checkbox / filters for each field.
~~        """
~~        for field_id in [f.id for f in self.form_fields] + [0]:
~~            prefix = "field_%s_" % field_id
~~            fields = [f for f in super(EntriesForm, self).__iter__()
~~                      if f.name.startswith(prefix)]
~~            yield fields[0], fields[1], fields[2:]

~~    def columns(self):
~~        """
~~        Returns the list of selected column names.
~~        """
~~        fields = [f.label for f in self.form_fields
~~                  if self.cleaned_data["field_%s_export" % f.id]]
~~        if self.cleaned_data["field_0_export"]:
~~            fields.append(self.entry_time_name)
~~        return fields

~~    def rows(self, csv=False):
        """
        Returns each row based on the selected criteria.
        """

        # Store the index of each field against its ID for building each
        # entry row with columns in the correct order. Also store the IDs of
        # fields with a type of FileField or Date-like for special handling of
        # their values.
~~        field_indexes = {}
~~        file_field_ids = []
~~        date_field_ids = []
~~        for field in self.form_fields:
~~            if self.cleaned_data["field_%s_export" % field.id]:
~~                field_indexes[field.id] = len(field_indexes)
~~                if field.is_a(fields.FILE):
~~                    file_field_ids.append(field.id)
~~                elif field.is_a(*fields.DATES):
~~                    date_field_ids.append(field.id)
~~        num_columns = len(field_indexes)
~~        include_entry_time = self.cleaned_data["field_0_export"]
~~        if include_entry_time:
~~            num_columns += 1

        # Get the field entries for the given form and filter by entry_time
        # if specified.
~~        field_entries = FieldEntry.objects.filter(
~~            entry__form=self.form).order_by(
~~            "-entry__id").select_related("entry")
~~        if self.cleaned_data["field_0_filter"] == FILTER_CHOICE_BETWEEN:
~~            time_from = self.cleaned_data["field_0_from"]
~~            time_to = self.cleaned_data["field_0_to"]
~~            if time_from and time_to:
~~                field_entries = field_entries.filter(
~~                    entry__entry_time__range=(time_from, time_to))

        # Loop through each field value ordered by entry, building up each
        # entry as a row. Use the ``valid_row`` flag for marking a row as
        # invalid if it fails one of the filtering criteria specified.
~~        current_entry = None
~~        current_row = None
~~        valid_row = True
~~        for field_entry in field_entries:
~~            if field_entry.entry_id != current_entry:
~~                # New entry, write out the current row and start a new one.
~~                if valid_row and current_row is not None:
~~                    if not csv:
~~                        current_row.insert(0, current_entry)
~~                    yield current_row
~~                current_entry = field_entry.entry_id
~~                current_row = [""] * num_columns
~~                valid_row = True
~~                if include_entry_time:
~~                    current_row[-1] = field_entry.entry.entry_time
~~            field_value = field_entry.value or ""

~~            field_id = field_entry.field_id
~~            filter_type = self.cleaned_data.get("field_%s_filter" % field_id)
~~            filter_args = None
~~            if filter_type:
~~                if filter_type == FILTER_CHOICE_BETWEEN:
~~                    f, t = "field_%s_from" % field_id, "field_%s_to" % field_id
~~                    filter_args = [self.cleaned_data[f], self.cleaned_data[t]]
~~                else:
~~                    field_name = "field_%s_contains" % field_id
~~                    filter_args = self.cleaned_data[field_name]
~~                    if filter_args:
~~                        filter_args = [filter_args]
~~            if filter_args:
                # Convert dates before checking filter.
~~                if field_id in date_field_ids:
~~                    y, m, d = field_value.split(" ")[0].split("-")
~~                    dte = date(int(y), int(m), int(d))
~~                    filter_args.append(dte)
~~                else:
~~                    filter_args.append(field_value)
~~                filter_func = FILTER_FUNCS[filter_type]
~~                if not filter_func(*filter_args):
~~                    valid_row = False
            # Create download URL for file fields.
~~            if field_entry.value and field_id in file_field_ids:
~~                url = reverse("admin:form_file", args=(field_entry.id,))
~~                field_value = self.request.build_absolute_uri(url)
~~                if not csv:
~~                    parts = (field_value, split(field_entry.value)[1])
~~                    field_value = mark_safe("<a href=\"%s\">%s</a>" % parts)
            # Only use values for fields that were selected.
~~            try:
~~                current_row[field_indexes[field_id]] = field_value
~~            except KeyError:
~~                pass
        # Output the final row.
~~        if valid_row and current_row is not None:
~~            if not csv:
~~                current_row.insert(0, current_entry)
~~            yield current_row
```


## Example 2 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth) 
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) code library for easily adding local and social 
authentication flows to Django projects. Its code is available as open 
source under the 
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).

[**django-allauth/allauth/account/forms.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/account/forms.py)

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


~~class PasswordField(forms.CharField):

~~    def __init__(self, *args, **kwargs):
~~        render_value = kwargs.pop('render_value',
~~                                  app_settings.PASSWORD_INPUT_RENDER_VALUE)
~~        kwargs['widget'] = forms.PasswordInput(render_value=render_value,
~~                                               attrs={'placeholder':
~~                                                      kwargs.get("label")})
~~        super(PasswordField, self).__init__(*args, **kwargs)


class SetPasswordField(PasswordField):

    def __init__(self, *args, **kwargs):
        super(SetPasswordField, self).__init__(*args, **kwargs)
        self.user = None

    def clean(self, value):
        value = super(SetPasswordField, self).clean(value)
        value = get_adapter().clean_password(value, user=self.user)
        return value


~~class LoginForm(forms.Form):

~~    password = PasswordField(label=_("Password"))
~~    remember = forms.BooleanField(label=_("Remember Me"),
~~                                  required=False)

~~    user = None
~~    error_messages = {
~~        'account_inactive':
~~        _("This account is currently inactive."),

~~        'email_password_mismatch':
~~        _("The e-mail address and/or password you specified are not correct."),

~~        'username_password_mismatch':
~~        _("The username and/or password you specified are not correct."),
~~    }

~~    def __init__(self, *args, **kwargs):
~~        self.request = kwargs.pop('request', None)
~~        super(LoginForm, self).__init__(*args, **kwargs)
~~        if app_settings.AUTHENTICATION_METHOD == AuthenticationMethod.EMAIL:
~~            login_widget = forms.TextInput(attrs={'type': 'email',
~~                                                  'placeholder':
~~                                                  _('E-mail address'),
~~                                                  'autofocus': 'autofocus'})
~~            login_field = forms.EmailField(label=_("E-mail"),
~~                                           widget=login_widget)
~~        elif app_settings.AUTHENTICATION_METHOD \
~~                == AuthenticationMethod.USERNAME:
~~            login_widget = forms.TextInput(attrs={'placeholder':
~~                                                  _('Username'),
~~                                                  'autofocus': 'autofocus'})
~~            login_field = forms.CharField(
~~                label=_("Username"),
~~                widget=login_widget,
~~                max_length=get_username_max_length())
~~        else:
~~            assert app_settings.AUTHENTICATION_METHOD \
~~                == AuthenticationMethod.USERNAME_EMAIL
~~            login_widget = forms.TextInput(attrs={'placeholder':
~~                                                  _('Username or e-mail'),
~~                                                  'autofocus': 'autofocus'})
~~            login_field = forms.CharField(label=pgettext("field label",
~~                                                         "Login"),
~~                                          widget=login_widget)
~~        self.fields["login"] = login_field
~~        set_form_field_order(self, ["login", "password", "remember"])
~~        if app_settings.SESSION_REMEMBER is not None:
~~            del self.fields['remember']

# source file continues from here with a few more good forms examples
```


## Example 3 from heritagesites
[heritagesites](https://github.com/Michael-Cantley/heritagesites) is a
[Django](/django.html) web application with a [MySQL](/mysql.html)
backend that displays 
[UNESCO heritage sites](https://whc.unesco.org/en/list/). The project
code is open source under the 
[MIT license](https://github.com/Michael-Cantley/heritagesites/blob/master/LICENSE).

[**heritagesites/heritagesites/forms.py**](https://github.com/Michael-Cantley/heritagesites/blob/master/heritagesites/forms.py)

```python
# forms.py
~~from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from heritagesites.models import HeritageSite


~~class HeritageSiteForm(forms.ModelForm):
~~    class Meta:
~~        model = HeritageSite
~~        fields = '__all__'

~~    def __init__(self, *args, **kwargs):
~~        super().__init__(*args, **kwargs)
~~        self.helper = FormHelper()
~~        self.helper.form_method = 'post'
~~        self.helper.add_input(Submit('submit', 'submit'))
```


## Example 4 from edX
[edX](https://github.com/edx)
([project website](https://open.edx.org/))
is an open source platform for teaching online courses that is widely
used in academia and industry. The platform code is available under the 
[GNU Affero General Public License v3.0](https://github.com/edx/edx-platform/blob/master/LICENSE).

[**edx-platform/openedx/core/djangoapps/util/forms.py**]("https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/util/forms.py)

```python
from __future__ import absolute_import

from django.core.exceptions import ValidationError
~~from django.forms import Field, MultipleHiddenInput, NullBooleanField, Select


~~class MultiValueField(Field):
    """
    Field class that supports a set of values for a single form field.
    The field input can be specified as:
        1. a comma-separated-list (foo:bar1,bar2,bar3), or
        2. a repeated field in a MultiValueDict (foo:bar1, foo:bar2, foo:bar3)
        3. a combination of the above (foo:bar1,bar2, foo:bar3)
    Note that there is currently no way to pass a value that includes a comma.
    The resulting field value is a python set of the values as strings.
    """
~~    widget = MultipleHiddenInput

~~    def to_python(self, list_of_string_values):
        """
        Convert the form input to a list of strings
        """
~~        values = super(MultiValueField, self).to_python(list_of_string_values) or set()

~~        if values:
            # combine all values if there were multiple specified individually
~~            values = ','.join(values)

            # parse them into a set
~~            values = set(values.split(',')) if values else set()

~~        return values

~~    def validate(self, values):
        """
        Ensure no empty values were passed
        """
~~        if values and "" in values:
~~            raise ValidationError("This field cannot be empty.")


~~class ExtendedNullBooleanField(NullBooleanField):
    """
    A field whose valid values are None, True, 'True', 'true', '1',
    False, 'False', 'false' and '0'.
    """

    NULL_BOOLEAN_CHOICES = (
        (None, ""),
        (True, True),
        (True, "True"),
        (True, "true"),
        (True, "1"),
        (False, False),
        (False, "False"),
        (False, "false"),
        (False, "0"),
    )

~~    widget = Select(choices=NULL_BOOLEAN_CHOICES)

~~    def to_python(self, value):
~~        return to_bool(value)


def to_bool(value):
    """
    Explicitly checks for the string 'True', 'False', 'true',
    'false', '1' and '0' and returns boolean True or False.
    Returns None if value is not passed at all and raises an
    exception for any other value.
    """
    if value in (True, 'True', 'true', '1'):
        return True
    elif value in (False, 'False', 'false', '0'):
        return False
    elif not value:
        return None
    else:
        raise ValidationError("Invalid Boolean Value.")
```


## Example 5 from django-registration (redux)
[django-registration (redux)](https://github.com/macropin/django-registration)
([project documentation](https://django-registration-redux.readthedocs.io/en/latest/))
is a [Django](/django.html) code library for one-phase, two-phase and 
three-phase registration flows. The code is available 
[open source](https://github.com/macropin/django-registration/blob/master/LICENSE). 

[**django-registration / registration / forms.py**](https://github.com/macropin/django-registration/blob/master/registration/forms.py)

```python
"""
Forms and validation code for user registration.
Note that all of these forms assume Django's bundle default ``User``
model; since it's not possible for a form to anticipate in advance the
needs of custom user models, you will need to write your own forms if
you're using a custom model.
"""
from __future__ import unicode_literals

~~from django import forms
~~from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

from .users import UserModel
from .users import UsernameField

User = UserModel()


~~class RegistrationForm(UserCreationForm):
    """
    Form for registering a new user account.
    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.
    Subclasses should feel free to add any additional validation they
    need, but should avoid defining a ``save()`` method -- the actual
    saving of collected user data is delegated to the active
    registration backend.
    """
    required_css_class = 'required'
~~    email = forms.EmailField(label=_("E-mail"))

    class Meta:
        model = User
        fields = (UsernameField(), "email")


class RegistrationFormUsernameLowercase(RegistrationForm):
    """
    A subclass of :class:`RegistrationForm` which enforces unique 
    case insensitive usernames, make all usernames to lower case.
    """
    def clean_username(self):
        username = self.cleaned_data.get('username', '').lower()
        if User.objects.filter(**{UsernameField(): username}).exists():
~~            raise forms.ValidationError(_\
~~              ('A user with that username already exists.'))

        return username


class RegistrationFormTermsOfService(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which adds a required checkbox
    for agreeing to a site's Terms of Service.
    """
~~    tos = forms.BooleanField(widget=forms.CheckboxInput,
~~             label=_('I have read and agree to the Terms of Service'),
~~             error_messages={'required': _\
~~             ("You must agree to the terms to register")})


class RegistrationFormUniqueEmail(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which enforces uniqueness of
    email addresses.
    """
    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.
        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
~~            raise forms.ValidationError(_\
~~                ("This email address is already in use. " + \
~~                 "Please supply a different email address."))
        return self.cleaned_data['email']


class RegistrationFormNoFreeEmail(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which disallows registration with
    email addresses from popular free webmail services; moderately
    useful for preventing automated spam registrations.
    To change the list of banned domains, subclass this form and
    override the attribute ``bad_domains``.
    """
    bad_domains = ['aim.com', 'aol.com', 'email.com', 'gmail.com',
                   'googlemail.com', 'hotmail.com', 'hushmail.com',
                   'msn.com', 'mail.ru', 'mailinator.com', 'live.com',
                   'yahoo.com', 'outlook.com']

    def clean_email(self):
        """
        Check the supplied email address against a list of known free
        webmail domains.
        """
        email_domain = self.cleaned_data['email'].split('@')[1]
        if email_domain in self.bad_domains:
            raise forms.ValidationError(_("Registration using free " + \
                "email addresses is prohibited. Please supply a " + \
                "different email address."))
        return self.cleaned_data['email']


~~class ResendActivationForm(forms.Form):
~~    required_css_class = 'required'
~~    email = forms.EmailField(label=_("E-mail"))
```
