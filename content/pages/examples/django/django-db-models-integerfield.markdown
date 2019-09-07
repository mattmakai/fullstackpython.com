title: django.db.models IntegerField Example Code
category: page
slug: django-db-models-integerfield-examples
sortorder: 50105
toc: False
sidebartitle: django.db.models IntegerField
meta: Python code examples for the IntegerField class used in the Django ORM, found within the django.db.models module of the Django project. 


[IntegerField](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
is a [Django ORM](/django-orm.html) mapping from your Python code to an
integer-type column in your [relational database](/databases.html).

The [Django](/django.html) project has wonderful documentation for
[IntegerField](https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.IntegerField)
as well as all of the other column fields.

Note that `IntegerField` is defined within the 
[django.db.models.fields](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
module but is typically referenced from
[django.db.models](https://github.com/django/django/tree/master/django/db/models)
rather than including the `fields` module reference.


## Example 1 from AuditLog
[Auditlog](https://github.com/jjkester/django-auditlog)
([project documentation](https://django-auditlog.readthedocs.io/en/latest/))
is a [Django](/django.html) app that logs changes to Python objects,
similar to the Django admin's logs but with more details and
output formats. Auditlog's source code is provided as open source under the
[MIT license](https://github.com/jjkester/django-auditlog/blob/master/LICENSE).

[**AuditLog / src / auditlog_tests / models.py**](https://github.com/jjkester/django-auditlog/blob/master/src/auditlog_tests/models.py)

```python
import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models
from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog

from multiselectfield import MultiSelectField


@auditlog.register()
class SimpleModel(models.Model):
    """
    A simple model with no special things going on.
    """

    text = models.TextField(blank=True)
    boolean = models.BooleanField(default=False)
~~    integer = models.IntegerField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now=True)

    history = AuditlogHistoryField()


class AltPrimaryKeyModel(models.Model):
    """
    A model with a non-standard primary key.
    """

    key = models.CharField(max_length=100, primary_key=True)

    text = models.TextField(blank=True)
    boolean = models.BooleanField(default=False)
    integer = models.IntegerField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now=True)

    history = AuditlogHistoryField(pk_indexable=False)


class UUIDPrimaryKeyModel(models.Model):
    """
    A model with a UUID primary key.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    text = models.TextField(blank=True)
    boolean = models.BooleanField(default=False)
    integer = models.IntegerField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now=True)

    history = AuditlogHistoryField(pk_indexable=False)


class ProxyModel(SimpleModel):
    """
    A model that is a proxy for another model.
    """

    class Meta:
        proxy = True


class RelatedModel(models.Model):
    """
    A model with a foreign key.
    """

    related = models.ForeignKey(to='self', on_delete=models.CASCADE)

    history = AuditlogHistoryField()


class ManyRelatedModel(models.Model):
    """
    A model with a many to many relation.
    """

    related = models.ManyToManyField('self')

    history = AuditlogHistoryField()


@auditlog.register(include_fields=['label'])
class SimpleIncludeModel(models.Model):
    """
    A simple model used for register's include_fields kwarg
    """

    label = models.CharField(max_length=100)
    text = models.TextField(blank=True)

    history = AuditlogHistoryField()


class SimpleExcludeModel(models.Model):
    """
    A simple model used for register's exclude_fields kwarg
    """

    label = models.CharField(max_length=100)
    text = models.TextField(blank=True)

    history = AuditlogHistoryField()


class SimpleMappingModel(models.Model):
    """
    A simple model used for register's mapping_fields kwarg
    """

    sku = models.CharField(max_length=100)
    vtxt = models.CharField(verbose_name='Version', max_length=100)
    not_mapped = models.CharField(max_length=100)

    history = AuditlogHistoryField()


class AdditionalDataIncludedModel(models.Model):
    """
    A model where get_additional_data is defined which allows for logging extra
    information about the model in JSON
    """

    label = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    related = models.ForeignKey(to=SimpleModel, on_delete=models.CASCADE)

    history = AuditlogHistoryField()

    def get_additional_data(self):
        """
        Returns JSON that captures a snapshot of additional details of the
        model instance. This method, if defined, is accessed by auditlog
        manager and added to each logentry instance on creation.
        """
        object_details = {
            'related_model_id': self.related.id,
            'related_model_text': self.related.text
        }
        return object_details


class DateTimeFieldModel(models.Model):
    """
    A model with a DateTimeField, used to test DateTimeField
    changes are detected properly.
    """
    label = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    date = models.DateField()
    time = models.TimeField()
    naive_dt = models.DateTimeField(null=True, blank=True)

    history = AuditlogHistoryField()


class ChoicesFieldModel(models.Model):
    """
    A model with a CharField restricted to a set of choices.
    This model is used to test the changes_display_dict method.
    """
    RED = 'r'
    YELLOW = 'y'
    GREEN = 'g'

    STATUS_CHOICES = (
        (RED, 'Red'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
    )

    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    multiselect = MultiSelectField(max_length=3, choices=STATUS_CHOICES, max_choices=3)
    multiplechoice = models.CharField(max_length=3, choices=STATUS_CHOICES)

    history = AuditlogHistoryField()


class CharfieldTextfieldModel(models.Model):
    """
    A model with a max length CharField and a Textfield.
    This model is used to test the changes_display_dict
    method's ability to truncate long text.
    """

    longchar = models.CharField(max_length=255)
    longtextfield = models.TextField()

    history = AuditlogHistoryField()


class PostgresArrayFieldModel(models.Model):
    """
    Test auditlog with Postgres's ArrayField
    """
    RED = 'r'
    YELLOW = 'y'
    GREEN = 'g'

    STATUS_CHOICES = (
        (RED, 'Red'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
    )

    arrayfield = ArrayField(models.CharField(max_length=1, choices=STATUS_CHOICES), size=3)

    history = AuditlogHistoryField()


class NoDeleteHistoryModel(models.Model):
    integer = models.IntegerField(blank=True, null=True)

    history = AuditlogHistoryField(delete_related=False)


auditlog.register(AltPrimaryKeyModel)
auditlog.register(UUIDPrimaryKeyModel)
auditlog.register(ProxyModel)
auditlog.register(RelatedModel)
auditlog.register(ManyRelatedModel)
auditlog.register(ManyRelatedModel.related.through)
auditlog.register(SimpleExcludeModel, exclude_fields=['text'])
auditlog.register(SimpleMappingModel, mapping_fields={'sku': 'Product No.'})
auditlog.register(AdditionalDataIncludedModel)
auditlog.register(DateTimeFieldModel)
auditlog.register(ChoicesFieldModel)
auditlog.register(CharfieldTextfieldModel)
auditlog.register(PostgresArrayFieldModel)
auditlog.register(NoDeleteHistoryModel)
```


## Example 2 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / users / models.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/users/models.py)

```python
import io
from datetime import date

import pyavagen
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.files.base import ContentFile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django_countries.fields import CountryField

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name=_('Email address'), unique=True)

    date_joined = models.DateTimeField(
        verbose_name=_('Date joined'),
        auto_now_add=True
    )

    is_active = models.BooleanField(
        verbose_name=_('Active'),
        default=True
    )

    has_finished_registration = models.BooleanField(
        default=False
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    # TODO: uncomment this later:
    # def get_absolute_url(self):
    #     return reverse('user-detail', kwargs={'pk': self.id})

    def __str__(self):
        return f'{self.pk}: {self.email}'


def get_avatar_full_path(instance, filename):
    ext = filename.split('.')[-1]
    path = f'{settings.MEDIA_PUBLIC_ROOT}/avatars'
    name = f'{instance.pk}_{instance.avatar_version:04d}'
    return f'{path}/{name}.{ext}'


class Profile(models.Model):
    ROLES = (
        (None, _('Select your role')),
        ('Student', _('Student')),
        ('PhD Student', _('PhD Student')),
        ('Assistant', _('Assistant')),
        ('Researcher', _('Researcher')),
        ('Assistant Professor', _('Assistant Professor')),
        ('Associate Professor', _('Associate Professor')),
        ('Professor', _('Professor')),
        ('Head of Department', _('Head of Department')),
        ('Head of Faculty', _('Head of Faculty')),
        ('Head of Laboratory', _('Head of Laboratory')),
        ('Vice Rector', _('Vice Rector')),
        ('Rector', _('Rector')),
        ('Software Developer', _('Software Developer')),
        ('Engineer', _('Engineer')),
        ('Technician', _('Technician')),
        ('Economist', _('Economist')),
        ('Lawyer', _('Lawyer')),
        ('Instructor', _('Instructor')),
        ('Consultant', _('Consultant')),
        ('Manager', _('Manager')),
        ('Administrator', _('Administrator')),
        ('Analyst', _('Analyst')),
        ('Journalist', _('Journalist')),
        ('Writer', _('Writer')),
        ('Editor', _('Editor')),
        ('Librarian', _('Librarian')),
        ('Vice Director', _('Vice Director')),
        ('Chief Executive Officer', _('Chief Executive Officer')),
        ('Retired', _('Retired')),
        ('Other', _('Other')),
    )

    DEGREE = (
        (None, _('Select your degree')),
        ('Undergraduate', _('Undergraduate')),
        ('Bachelor', _('Bachelor')),
        ('Master', _('Master')),
        ('PhD', _('PhD')),
        ('Candidate of Sciences', _('Candidate of Sciences')),
        ('Doctor of Sciences', _('Doctor of Sciences')),
    )

    LANGUAGES = (
        ('ENG', _('English')),
        ('RUS', _('Russian')),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(
        max_length=100, verbose_name=_("First Name in English")
    )
    last_name = models.CharField(
        max_length=100, verbose_name=_("Last Name in English")
    )
    first_name_rus = models.CharField(
        max_length=100, default="", verbose_name=_("First Name in Russian",),
        blank=True,
    )
    middle_name_rus = models.CharField(
        max_length=100, default="", verbose_name=_("Middle Name in Russian"),
        blank = True,
    )
    last_name_rus = models.CharField(
        max_length=100, default="", verbose_name=_("Last Name in Russian"),
        blank=True,
    )
    country = CountryField(null=True, verbose_name=_("Country"))
    city = models.CharField(max_length=100, verbose_name=_("City in English"))
    birthday = models.DateField(verbose_name=_("Birthday"), null=True)
    affiliation = models.CharField(
        max_length=100, verbose_name=_("Name of your organization in English"),
    )
    role = models.CharField(
        choices=ROLES, max_length=30, null=True,
        verbose_name=_('Primary role in organization')
    )
    degree = models.CharField(
        choices=DEGREE, max_length=30, null=True,
        verbose_name=_('Degree')
    )
    ieee_member = models.BooleanField(
        verbose_name=_('I am an IEEE Member'), default=False
    )

    preferred_language = models.CharField(
        choices=LANGUAGES, max_length=3, default='ENG'
    )

    avatar = models.ImageField(upload_to=get_avatar_full_path, blank=True)
    avatar_version = models.IntegerField(default=0, blank=True, editable=False)

    @property
    def email(self):
        return self.user.email

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_name_rus(self):
        return ' '.join(
            (self.first_name_rus, self.middle_name_rus, self.last_name_rus)
        )

    def has_name_rus(self):
        return bool(self.get_full_name_rus().strip())

    def age(self):
        today = date.today()
        born = self.birthday
        rest = 1 if (today.month, today.day) < (born.month, born.day) else 0
        return today.year - born.year - rest

    def __str__(self):
        return self.get_full_name()


def generate_avatar(profile):
    img_io = io.BytesIO()
    avatar = pyavagen.Avatar(
        pyavagen.CHAR_SQUARE_AVATAR,
        size=500,
        string=profile.get_full_name(),
        blur_radius=100
    )
    avatar.generate().save(img_io, format='PNG', quality=100)
    img_content = ContentFile(img_io.getvalue(), f'{profile.pk}.png')
    return img_content


def change_avatar(profile, image_file):
    if profile.avatar:
        profile.avatar.delete()
    profile.avatar_version += 1
    profile.avatar = image_file
    profile.save()
    return profile


class Subscriptions(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    trans_email = models.BooleanField(
        default=False,
        verbose_name=_('I agree to receive transactional emails from DCCN '
                       'Registration System corresponding to actions related '
                       'to me (e.g., submission status update, adding me as '
                       'a co-author, invitations for review, etc.)')
    )

    info_email = models.BooleanField(
        default=False,
        verbose_name=_('I agree to receive informational emails related to '
                       'DCCN 2019 and future DCCN events')
    )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        profile.avatar = generate_avatar(profile)
        Subscriptions.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    instance.subscriptions.save()
```


## Example 3 from django-angular
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
from django.forms import fields, models as model_fields, widgets
from django.utils.html import format_html
from django.utils.module_loading import import_string
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _, ungettext_lazy

from djng import app_settings
from .widgets import DropFileWidget, DropImageWidget


class DefaultFieldMixin(object):
    render_label = True

    def has_subwidgets(self):
        return False

    def get_potential_errors(self):
        return self.get_input_required_errors()

    def get_input_required_errors(self):
        errors = []
        if self.required:
            self.widget.attrs['ng-required'] = 'true'
            for key, msg in self.error_messages.items():
                if key == 'required':
                    errors.append(('$error.required', msg))
        return errors

    def get_min_max_length_errors(self):
        errors = []
        if getattr(self, 'min_length', None):
            self.widget.attrs['ng-minlength'] = self.min_length
        if getattr(self, 'max_length', None):
            self.widget.attrs['ng-maxlength'] = self.max_length
        for item in self.validators:
            if getattr(item, 'code', None) == 'min_length':
                message = ungettext_lazy(
                    'Ensure this value has at least %(limit_value)d character',
                    'Ensure this value has at least %(limit_value)d characters',
                    'limit_value')
                errors.append(('$error.minlength', message % {'limit_value': self.min_length}))
            if getattr(item, 'code', None) == 'max_length':
                message = ungettext_lazy(
                    'Ensure this value has at most %(limit_value)d character',
                    'Ensure this value has at most %(limit_value)d characters',
                    'limit_value')
                errors.append(('$error.maxlength', message % {'limit_value': self.max_length}))
        return errors

    def get_min_max_value_errors(self):
        errors = []
        if isinstance(getattr(self, 'min_value', None), int):
            self.widget.attrs['min'] = self.min_value
        if isinstance(getattr(self, 'max_value', None), int):
            self.widget.attrs['max'] = self.max_value
        errkeys = []
        for key, msg in self.error_messages.items():
            if key == 'min_value':
                errors.append(('$error.min', msg))
                errkeys.append(key)
            if key == 'max_value':
                errors.append(('$error.max', msg))
                errkeys.append(key)
        for item in self.validators:
            if getattr(item, 'code', None) == 'min_value' and 'min_value' not in errkeys:
                errors.append(('$error.min', item.message % {'limit_value': self.min_value}))
                errkeys.append('min_value')
            if getattr(item, 'code', None) == 'max_value' and 'max_value' not in errkeys:
                errors.append(('$error.max', item.message % {'limit_value': self.max_value}))
                errkeys.append('max_value')
        return errors

    def get_invalid_value_errors(self, ng_error_key):
        errors = []
        errkeys = []
        for key, msg in self.error_messages.items():
            if key == 'invalid':
                errors.append(('$error.{0}'.format(ng_error_key), msg))
                errkeys.append(key)
        for item in self.validators:
            if getattr(item, 'code', None) == 'invalid' and 'invalid' not in errkeys:
                errmsg = getattr(item, 'message', _("This input self does not contain valid data."))
                errors.append(('$error.{0}'.format(ng_error_key), errmsg))
                errkeys.append('invalid')
        return errors

    def update_widget_attrs(self, bound_field, attrs):
        """
        Update the dictionary of attributes used  while rendering the input widget
        """
        bound_field.form.update_widget_attrs(bound_field, attrs)
        widget_classes = self.widget.attrs.get('class', None)
        if widget_classes:
            if 'class' in attrs:
                attrs['class'] += ' ' + widget_classes
            else:
                attrs.update({'class': widget_classes})
        return attrs


class Field(DefaultFieldMixin, fields.Field):
    pass


class CharField(DefaultFieldMixin, fields.CharField):
    def get_potential_errors(self):
        errors = self.get_input_required_errors()
        errors.extend(self.get_min_max_length_errors())
        return errors


class DecimalField(DefaultFieldMixin, fields.DecimalField):
    def get_potential_errors(self):
        errors = self.get_input_required_errors()
        self.widget.attrs['ng-minlength'] = 1
        if isinstance(self.max_digits, int) and self.max_digits > 0:
            self.widget.attrs['ng-maxlength'] = self.max_digits + 1
        errors.extend(self.get_min_max_value_errors())
        errors.extend(self.get_invalid_value_errors('number'))
        return errors


class EmailField(DefaultFieldMixin, fields.EmailField):
    def get_potential_errors(self):
        self.widget.attrs['email-pattern'] = self.get_email_regex()
        errors = self.get_input_required_errors()
        errors.extend(self.get_invalid_value_errors('email'))
        return errors

    def get_email_regex(self):
        """
        Return a regex pattern matching valid email addresses. Uses the same
        logic as the django validator, with the folowing exceptions:

        - Internationalized domain names not supported
        - IP addresses not supported
        - Strips lookbehinds (not supported in javascript regular expressions)
        """
        validator = self.default_validators[0]
        user_regex = validator.user_regex.pattern.replace('\Z', '@')
        domain_patterns = ([re.escape(domain) + '$' for domain in
                            validator.domain_whitelist] +
                           [validator.domain_regex.pattern.replace('\Z', '$')])
        domain_regex = '({0})'.format('|'.join(domain_patterns))
        email_regex = user_regex + domain_regex
        return re.sub(r'\(\?\<[^()]*?\)', '', email_regex)  # Strip lookbehinds


class DateField(DefaultFieldMixin, fields.DateField):
    def get_potential_errors(self):
        errors = self.get_input_required_errors()
        errors.extend(self.get_invalid_value_errors('date'))
        return errors


class DateTimeField(DefaultFieldMixin, fields.DateTimeField):
    def get_potential_errors(self):
        errors = self.get_input_required_errors()
        errors.extend(self.get_invalid_value_errors('datetime'))
        return errors


class TimeField(DefaultFieldMixin, fields.TimeField):
    def get_potential_errors(self):
        errors = self.get_input_required_errors()
        errors.extend(self.get_invalid_value_errors('time'))
        return errors


class DurationField(DefaultFieldMixin, fields.DurationField):
    def get_potential_errors(self):
        errors = self.get_input_required_errors()
        errors.extend(self.get_invalid_value_errors('duration'))
        return errors


class FloatField(DefaultFieldMixin, fields.FloatField):
    """
    The internal ``django.forms.FloatField`` does not handle the step value in its number widget.
    """
    def __init__(self, *args, **kwargs):
        self.step = kwargs.pop('step', None)
        super(FloatField, self).__init__(*args, **kwargs)

    def widget_attrs(self, widget):
        attrs = super(FloatField, self).widget_attrs(widget)
        attrs.update(step=self.step)
        return attrs

    def get_potential_errors(self):
        errors = self.get_input_required_errors()
        errors.extend(self.get_min_max_value_errors())
        errors.extend(self.get_invalid_value_errors('number'))
        return errors


class IntegerField(DefaultFieldMixin, fields.IntegerField):
    def get_potential_errors(self):
        errors = self.get_input_required_errors()
        errors.extend(self.get_min_max_value_errors())
        errors.extend(self.get_invalid_value_errors('number'))
        return errors


class SlugField(DefaultFieldMixin, fields.SlugField):
    pass


class RegexField(DefaultFieldMixin, fields.RegexField):
    # Presumably Python Regex can't be translated 1:1 into JS regex. Any hints on how to convert these?
    def get_potential_errors(self):
        self.widget.attrs['ng-pattern'] = '/{0}/'.format(self.regex.pattern)
        errors = self.get_input_required_errors()
        errors.extend(self.get_min_max_length_errors())
        errors.extend(self.get_invalid_value_errors('pattern'))
        return errors


class BooleanField(DefaultFieldMixin, fields.BooleanField):
    render_label = False

    def has_subwidgets(self):
        return True

    def update_widget_attrs(self, bound_field, attrs):
        bound_field.form.update_widget_attrs(bound_field, attrs)
        return attrs

    def update_widget_rendering_context(self, context):
        context['widget'].update(field_label=self.label)
        return context

    def get_converted_widget(self, widgets_module):
        if not isinstance(self.widget, widgets.CheckboxInput):
            return
        try:
            new_widget = import_string(widgets_module + '.CheckboxInput')(self.label)
        except ImportError:
            new_widget = import_string('djng.forms.widgets.CheckboxInput')(self.label)
        new_widget.__dict__.update(self.widget.__dict__)
        return new_widget


class NullBooleanField(DefaultFieldMixin, fields.NullBooleanField):
    pass


class URLField(DefaultFieldMixin, fields.URLField):
    pass


class MultipleFieldMixin(DefaultFieldMixin):
    def get_multiple_choices_required(self):
        """
        Add only the required message, but no 'ng-required' attribute to the input fields,
        otherwise all Checkboxes of a MultipleChoiceField would require the property "checked".
        """
        errors = []
        if self.required:
            msg = _("At least one checkbox has to be selected.")
            errors.append(('$error.multifield', msg))
        return errors


class ChoiceField(MultipleFieldMixin, fields.ChoiceField):
    def __init__(self, *args, **kwargs):
        super(ChoiceField, self).__init__(*args, **kwargs)
        if isinstance(self.widget, widgets.Select) and self.initial is None and len(self.choices):
            self.initial = self.choices[0][0]

    def has_subwidgets(self):
        return isinstance(self.widget, widgets.RadioSelect)

    def get_potential_errors(self):
        if isinstance(self.widget, widgets.RadioSelect):
            errors = self.get_multiple_choices_required()
        else:
            errors = self.get_input_required_errors()
        return errors

    def update_widget_attrs(self, bound_field, attrs):
        bound_field.form.update_widget_attrs(bound_field, attrs)
        if isinstance(self.widget, widgets.RadioSelect):
            if self.required and 'ng-model' in attrs:
                require_model = format_html("!{}", attrs['ng-model'])
                attrs.update({'ng-required': require_model})
        return attrs

    def get_converted_widget(self, widgets_module):
        if not isinstance(self.widget, widgets.RadioSelect):
            return
        try:
            new_widget = import_string(widgets_module + '.RadioSelect')()
        except ImportError:
            new_widget = import_string('djng.forms.widgets.RadioSelect')()
        new_widget.__dict__ = self.widget.__dict__
        return new_widget


class ModelChoiceField(MultipleFieldMixin, model_fields.ModelChoiceField):
    pass


class TypedChoiceField(MultipleFieldMixin, fields.TypedChoiceField):
    def get_potential_errors(self):
        if isinstance(self.widget, widgets.RadioSelect):
            errors = self.get_multiple_choices_required()
        else:
            errors = self.get_input_required_errors()
        return errors


class MultipleChoiceField(MultipleFieldMixin, fields.MultipleChoiceField):
    def has_subwidgets(self):
        return isinstance(self.widget, widgets.CheckboxSelectMultiple)

    def get_potential_errors(self):
        if isinstance(self.widget, widgets.CheckboxSelectMultiple):
            errors = self.get_multiple_choices_required()
        else:
            errors = self.get_input_required_errors()
        return errors

    def update_widget_attrs(self, bound_field, attrs):
        from django import VERSION

        bound_field.form.update_widget_attrs(bound_field, attrs)
        if VERSION < (1, 11) and isinstance(self.widget, widgets.CheckboxSelectMultiple):
            attrs.update(multifields_required=self.required)
        return attrs

    def get_converted_widget(self, widgets_module):
        if not isinstance(self.widget, widgets.CheckboxSelectMultiple):
            return
        try:
            new_widget = import_string(widgets_module + '.CheckboxSelectMultiple')()
        except ImportError:
            new_widget = import_string('djng.forms.widgets.CheckboxSelectMultiple')()
        new_widget.__dict__ = self.widget.__dict__
        return new_widget

    def implode_multi_values(self, name, data):
        """
        Due to the way Angular organizes it model, when Form data is sent via a POST request,
        then for this kind of widget, the posted data must to be converted into a format suitable
        for Django's Form validation.
        """
        mkeys = [k for k in data.keys() if k.startswith(name + '.')]
        mvls = [data.pop(k)[0] for k in mkeys]
        if mvls:
            data.setlist(name, mvls)

    def convert_ajax_data(self, field_data):
        """
        Due to the way Angular organizes it model, when this Form data is sent using Ajax,
        then for this kind of widget, the sent data has to be converted into a format suitable
        for Django's Form validation.
        """
        data = [key for key, val in field_data.items() if val]
        return data

    def update_widget_rendering_context(self, context):
        if isinstance(self.widget, widgets.CheckboxSelectMultiple):
            context['widget']['attrs']['djng-multifields-required'] = str(self.required).lower()
            ng_model = mark_safe(context['widget']['attrs'].pop('ng-model', ''))
            if ng_model:
                for group, options, index in context['widget']['optgroups']:
                    for option in options:
                        option['name'] = format_html('{name}.{value}', **option)
                        option['attrs']['ng-model'] = format_html('{0}[\'{value}\']', ng_model, **option)
        return context


class ModelMultipleChoiceField(MultipleFieldMixin, model_fields.ModelMultipleChoiceField):
    pass


class TypedMultipleChoiceField(MultipleFieldMixin, fields.TypedMultipleChoiceField):
    """
    TODO: this class must be adopted to upcoming use-cases.
    """
    pass


class UUIDField(DefaultFieldMixin, fields.UUIDField):
    def get_potential_errors(self):
        errors = self.get_input_required_errors()
        errors.extend(self.get_min_max_length_errors())
        return errors


class FileFieldMixin(DefaultFieldMixin):
    def to_python(self, value):
        # handle previously existing file
        try:
            current_file = None
            if ':' in value['current_file']:
                current_file = self.signer.unsign(value['current_file'])
        except signing.BadSignature:
            raise ValidationError("Got bogus upstream data")
        except (KeyError, TypeError):
            pass

        # handle new uploaded image
        try:
            obj = ''
            if ':' in value['temp_name']:
                temp_name = self.signer.unsign(value['temp_name'])
                temp_file = self.storage.open(temp_name, 'rb')
                file_size = self.storage.size(temp_name)
                if file_size < settings.FILE_UPLOAD_MAX_MEMORY_SIZE:
                    obj = InMemoryUploadedFile(
                        file=temp_file,
                        field_name=None,
                        name=value['file_name'],
                        charset=value['charset'],
                        content_type=value['content_type'],
                        content_type_extra=value['content_type_extra'],
                        size=file_size,
                    )
                else:
                    obj = TemporaryUploadedFile(
                        value['file_name'],
                        value['content_type'],
                        0,
                        value['charset'],
                        content_type_extra=value['content_type_extra'],
                    )
                    while True:
                        chunk = temp_file.read(0x10000)
                        if not chunk:
                            break
                        obj.file.write(chunk)
                    obj.file.seek(0)
                    obj.file.size = file_size
                self.storage.delete(temp_name)
                self.remove_current(current_file)
            elif value['temp_name'] == 'delete':
                self.remove_current(current_file)
        except signing.BadSignature:
            raise ValidationError("Got bogus upstream data")
        except (IOError, KeyError, TypeError):
            obj = current_file
        except Exception as excp:
            raise ValidationError("File upload failed. {}: {}".format(excp.__class__.__name__, excp))
        return obj

    def remove_current(self, filename):
        if filename:
            default_storage.delete(filename)


class FileField(FileFieldMixin, fields.FileField):
    storage = app_settings.upload_storage
    signer = signing.Signer()

    def __init__(self, *args, **kwargs):
        accept = kwargs.pop('accept', '*/*')
        fileupload_url = kwargs.pop('fileupload_url', reverse_lazy('fileupload'))
        area_label = kwargs.pop('area_label', _("Drop file here or click to upload"))
        attrs = {
            'accept': accept,
            'ngf-pattern': accept,
        }
        kwargs.update(widget=DropFileWidget(area_label, fileupload_url, attrs=attrs))
        super(FileField, self).__init__(*args, **kwargs)

    @classmethod
    def preview(cls, file_obj):
        available_name = cls.storage.get_available_name(file_obj.name)
        temp_name = cls.storage.save(available_name, file_obj)
        extension = mimetypes.guess_extension(file_obj.content_type)
        if extension:
            extension = extension[1:]
        else:
            extension = '_blank'
        icon_url = staticfiles_storage.url('djng/icons/{}.png'.format(extension))
        return {
            'url': 'url({})'.format(icon_url),
            'temp_name': cls.signer.sign(temp_name),
            'file_name': file_obj.name,
            'file_size': file_obj.size,
            'charset': file_obj.charset,
            'content_type': file_obj.content_type,
            'content_type_extra': file_obj.content_type_extra,
        }


class ImageField(FileFieldMixin, fields.ImageField):
    storage = app_settings.upload_storage
    signer = signing.Signer()

    def __init__(self, *args, **kwargs):
        if 'easy_thumbnails' not in settings.INSTALLED_APPS:
            raise ImproperlyConfigured("'djng.forms.fields.ImageField' requires 'easy-thubnails' to be installed")
        accept = kwargs.pop('accept', 'image/*')
        fileupload_url = kwargs.pop('fileupload_url', reverse_lazy('fileupload'))
        area_label = kwargs.pop('area_label', _("Drop image here or click to upload"))
        attrs = {
            'accept': accept,
            'ngf-pattern': accept,
        }
        kwargs.update(widget=DropImageWidget(area_label, fileupload_url, attrs=attrs))
        super(ImageField, self).__init__(*args, **kwargs)

    def remove_current(self, image_name):
        from easy_thumbnails.models import Source, Thumbnail

        try:
            source = Source.objects.get(name=image_name)
            for thumb in Thumbnail.objects.filter(source=source):
                default_storage.delete(thumb.name)
                thumb.delete()
            source.delete()
        except Source.DoesNotExist:
            pass
        super(ImageField, self).remove_current(image_name)

    @classmethod
    def preview(cls, file_obj):
        from easy_thumbnails.files import get_thumbnailer
        from easy_thumbnails.templatetags.thumbnail import data_uri

        available_name = cls.storage.get_available_name(file_obj.name)
        temp_name = cls.storage.save(available_name, file_obj)
        thumbnailer = get_thumbnailer(cls.storage.path(temp_name), relative_name=available_name)
        thumbnail = thumbnailer.generate_thumbnail(app_settings.THUMBNAIL_OPTIONS)
        return {
            'url': 'url({})'.format(data_uri(thumbnail)),
            'temp_name': cls.signer.sign(temp_name),
            'file_name': file_obj.name,
            'file_size': file_obj.size,
            'charset': file_obj.charset,
            'content_type': file_obj.content_type,
            'content_type_extra': file_obj.content_type_extra,
        }
```


## Example 4 from django-axes
[django-axes](https://github.com/jazzband/django-axes/)
([project documentation](https://django-axes.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-axes/)
is a code library for [Django](/django.html) projects to track failed
login attempts against a web application. The goal of the project is
to make it easier for you to stop people and scripts from hacking your
Django-powered website.

The code for django-axes is
[open source under the MIT license](https://github.com/jazzband/django-axes/blob/master/LICENSE)
and maintained by the group of developers known as
[Jazzband](https://jazzband.co/).

[**django-axes / axes / migrations / 0001_initial.py**](https://github.com/jazzband/django-axes/blob/master/axes/migrations/0001_initial.py)

```python
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessAttempt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_agent', models.CharField(max_length=255)),
                ('ip_address', models.GenericIPAddressField(null=True, verbose_name='IP Address')),
                ('username', models.CharField(max_length=255, null=True)),
                ('trusted', models.BooleanField(default=False)),
                ('http_accept', models.CharField(max_length=1025, verbose_name='HTTP Accept')),
                ('path_info', models.CharField(max_length=255, verbose_name='Path')),
                ('attempt_time', models.DateTimeField(auto_now_add=True)),
                ('get_data', models.TextField(verbose_name='GET Data')),
                ('post_data', models.TextField(verbose_name='POST Data')),
                ('failures_since_start', models.PositiveIntegerField(verbose_name='Failed Logins')),
            ],
            options={
                'ordering': ['-attempt_time'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccessLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_agent', models.CharField(max_length=255)),
                ('ip_address', models.GenericIPAddressField(null=True, verbose_name='IP Address')),
                ('username', models.CharField(max_length=255, null=True)),
                ('trusted', models.BooleanField(default=False)),
                ('http_accept', models.CharField(max_length=1025, verbose_name='HTTP Accept')),
                ('path_info', models.CharField(max_length=255, verbose_name='Path')),
                ('attempt_time', models.DateTimeField(auto_now_add=True)),
                ('logout_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'ordering': ['-attempt_time'],
                'abstract': False,
            },
        ),
    ]
```


## Example 5 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / migrations / 0018_create_pagenode.py**](https://github.com/divio/django-cms/blob/develop/cms/migrations/0018_create_pagenode.py)

```python
# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-03 19:50
from __future__ import unicode_literals

import django
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion

from . import IrreversibleMigration


def get_descendants(root):
    """
    Returns the a generator of primary keys which represent
    descendants of the given page ID (root_id)
    """
    # Note this is done because get_descendants() can't be trusted
    # as the tree can be corrupt.

    for child in root.children.order_by('path').iterator():
        yield child

        for child in get_descendants(child):
            yield child


def create_page_nodes(apps, schema_editor):
    Page = apps.get_model('cms', 'Page')
    TreeNode = apps.get_model('cms', 'TreeNode')
    db_alias = schema_editor.connection.alias
    root_draft_pages = Page.objects.using(db_alias).filter(
        publisher_is_draft=True,
        parent__isnull=True,
    )

    create_node = TreeNode.objects.using(db_alias).create

    nodes_by_page = {}

    for root in root_draft_pages:
        node = create_node(
            site_id=root.site_id,
            path=root.path,
            depth=root.depth,
            numchild=root.numchild,
            parent=None,
        )

        nodes_by_page[root.pk] = node

        for descendant in get_descendants(root):
            node = create_node(
                site_id=descendant.site_id,
                path=descendant.path,
                depth=descendant.depth,
                numchild=descendant.numchild,
                parent=nodes_by_page[descendant.parent_id],
            )
            nodes_by_page[descendant.pk] = node


class Migration(IrreversibleMigration):

    dependencies = [
        ('sites', '0001_initial'),
        ('cms', '0017_pagetype'),
    ]
    replaces = [('cms', '0018_pagenode')]

    operations = [
        migrations.CreateModel(
            name='TreeNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='cms.TreeNode')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='djangocms_nodes', to='sites.Site', verbose_name='site')),
            ],
            options={
                'ordering': ('path',),
                'default_permissions': [],
            },
        ),
        migrations.RunPython(create_page_nodes),
        migrations.AddField(
            model_name='page',
            name='node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cms_pages',
                                    to='cms.TreeNode'),
        ),
        migrations.AddField(
            model_name='page',
            name='migration_0018_control',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('node', 'publisher_is_draft')]),
        ),
        migrations.AlterModelManagers(
            name='pageusergroup',
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
    ]
```


## Example 6 from django-extensions
[django-extensions](https://github.com/django-extensions/django-extensions)
([project documentation](https://django-extensions.readthedocs.io/en/latest/)
and [PyPI page](https://pypi.org/project/django-extensions/))
is a [Django](/django.html) project that adds a bunch of additional
useful commands to the `manage.py` interface. This 
[GoDjango video](https://www.youtube.com/watch?v=1F6G3ONhr4k) provides a 
quick overview of what you get when you install it into your Python
environment.

The django-extensions project is open sourced under the
[MIT license](https://github.com/django-extensions/django-extensions/blob/master/LICENSE).

[**django-extensions / django_extensions / utils / dia2django.py**](https://github.com/django-extensions/django-extensions/blob/master/django_extensions/utils/dia2django.py)

```python
# -*- coding: utf-8 -*-
"""
Author Igor Támara igor@tamarapatino.org
Use this little program as you wish, if you
include it in your work, let others know you
are using it preserving this note, you have
the right to make derivative works, Use it
at your own risk.
Tested to work on(etch testing 13-08-2007):
  Python 2.4.4 (#2, Jul 17 2007, 11:56:54)
  [GCC 4.1.3 20070629 (prerelease) (Debian 4.1.2-13)] on linux2
"""

import codecs
import gzip
import re
import sys
from xml.dom.minidom import Node, parseString

import six

dependclasses = ["User", "Group", "Permission", "Message"]

# Type dictionary translation types SQL -> Django
tsd = {
    "text": "TextField",
    "date": "DateField",
    "varchar": "CharField",
    "int": "IntegerField",
    "float": "FloatField",
    "serial": "AutoField",
    "boolean": "BooleanField",
    "numeric": "FloatField",
    "timestamp": "DateTimeField",
    "bigint": "IntegerField",
    "datetime": "DateTimeField",
    "time": "TimeField",
    "bool": "BooleanField",
}

# convert varchar -> CharField
v2c = re.compile(r'varchar\((\d+)\)')


def index(fks, id):
    """
    Look for the id on fks, fks is an array of arrays, each array has on [1]
    the id of the class in a dia diagram.  When not present returns None, else
    it returns the position of the class with id on fks
    """
    for i, j in fks.items():
        if fks[i][1] == id:
            return i
    return None


def addparentstofks(rels, fks):
    """
    Get a list of relations, between parents and sons and a dict of
    clases named in dia, and modifies the fks to add the parent as fk to get
    order on the output of classes and replaces the base class of the son, to
    put the class parent name.
    """
    for j in rels:
        son = index(fks, j[1])
        parent = index(fks, j[0])
        fks[son][2] = fks[son][2].replace("models.Model", parent)
        if parent not in fks[son][0]:
            fks[son][0].append(parent)


def dia2django(archivo):
    models_txt = ''
    f = codecs.open(archivo, "rb")
    # dia files are gzipped
    data = gzip.GzipFile(fileobj=f).read()
    ppal = parseString(data)
    # diagram -> layer -> object -> UML - Class -> name, (attribs : composite -> name,type)
    datos = ppal.getElementsByTagName("dia:diagram")[0].getElementsByTagName("dia:layer")[0].getElementsByTagName("dia:object")
    clases = {}
    herit = []
    imports = six.u("")
    for i in datos:
        # Look for the classes
        if i.getAttribute("type") == "UML - Class":
            myid = i.getAttribute("id")
            for j in i.childNodes:
                if j.nodeType == Node.ELEMENT_NODE and j.hasAttributes():
                    if j.getAttribute("name") == "name":
                        actclas = j.getElementsByTagName("dia:string")[0].childNodes[0].data[1:-1]
                        myname = "\nclass %s(models.Model) :\n" % actclas
                        clases[actclas] = [[], myid, myname, 0]
                    if j.getAttribute("name") == "attributes":
                        for l in j.getElementsByTagName("dia:composite"):
                            if l.getAttribute("type") == "umlattribute":
                                # Look for the attribute name and type
                                for k in l.getElementsByTagName("dia:attribute"):
                                    if k.getAttribute("name") == "name":
                                        nc = k.getElementsByTagName("dia:string")[0].childNodes[0].data[1:-1]
                                    elif k.getAttribute("name") == "type":
                                        tc = k.getElementsByTagName("dia:string")[0].childNodes[0].data[1:-1]
                                    elif k.getAttribute("name") == "value":
                                        val = k.getElementsByTagName("dia:string")[0].childNodes[0].data[1:-1]
                                        if val == '##':
                                            val = ''
                                    elif k.getAttribute("name") == "visibility" and k.getElementsByTagName("dia:enum")[0].getAttribute("val") == "2":
                                        if tc.replace(" ", "").lower().startswith("manytomanyfield("):
                                            # If we find a class not in our model that is marked as being to another model
                                            newc = tc.replace(" ", "")[16:-1]
                                            if dependclasses.count(newc) == 0:
                                                dependclasses.append(newc)
                                        if tc.replace(" ", "").lower().startswith("foreignkey("):
                                            # If we find a class not in our model that is marked as being to another model
                                            newc = tc.replace(" ", "")[11:-1]
                                            if dependclasses.count(newc) == 0:
                                                dependclasses.append(newc)

                                # Mapping SQL types to Django
                                varch = v2c.search(tc)
                                if tc.replace(" ", "").startswith("ManyToManyField("):
                                    myfor = tc.replace(" ", "")[16:-1]
                                    if actclas == myfor:
                                        # In case of a recursive type, we use 'self'
                                        tc = tc.replace(myfor, "'self'")
                                    elif clases[actclas][0].count(myfor) == 0:
                                        # Adding related class
                                        if myfor not in dependclasses:
                                            # In case we are using Auth classes or external via protected dia visibility
                                            clases[actclas][0].append(myfor)
                                    tc = "models." + tc
                                    if len(val) > 0:
                                        tc = tc.replace(")", "," + val + ")")
                                elif tc.find("Field") != -1:
                                    if tc.count("()") > 0 and len(val) > 0:
                                        tc = "models.%s" % tc.replace(")", "," + val + ")")
                                    else:
                                        tc = "models.%s(%s)" % (tc, val)
                                elif tc.replace(" ", "").startswith("ForeignKey("):
                                    myfor = tc.replace(" ", "")[11:-1]
                                    if actclas == myfor:
                                        # In case of a recursive type, we use 'self'
                                        tc = tc.replace(myfor, "'self'")
                                    elif clases[actclas][0].count(myfor) == 0:
                                        # Adding foreign classes
                                        if myfor not in dependclasses:
                                            # In case we are using Auth classes
                                            clases[actclas][0].append(myfor)
                                    tc = "models." + tc
                                    if len(val) > 0:
                                        tc = tc.replace(")", "," + val + ")")
                                elif varch is None:
                                    tc = "models." + tsd[tc.strip().lower()] + "(" + val + ")"
                                else:
                                    tc = "models.CharField(max_length=" + varch.group(1) + ")"
                                    if len(val) > 0:
                                        tc = tc.replace(")", ", " + val + " )")
                                if not (nc == "id" and tc == "AutoField()"):
                                    clases[actclas][2] += "    %s = %s\n" % (nc, tc)
        elif i.getAttribute("type") == "UML - Generalization":
            mycons = ['A', 'A']
            a = i.getElementsByTagName("dia:connection")
            for j in a:
                if len(j.getAttribute("to")):
                    mycons[int(j.getAttribute("handle"))] = j.getAttribute("to")
            print(mycons)
            if 'A' not in mycons:
                herit.append(mycons)
        elif i.getAttribute("type") == "UML - SmallPackage":
            a = i.getElementsByTagName("dia:string")
            for j in a:
                if len(j.childNodes[0].data[1:-1]):
                    imports += six.u("from %s.models import *" % j.childNodes[0].data[1:-1])

    addparentstofks(herit, clases)
    # Ordering the appearance of classes
    # First we make a list of the classes each classs is related to.
    ordered = []
    for j, k in six.iteritems(clases):
        k[2] += "\n    def %s(self):\n        return u\"\"\n" % (("__str__" if six.PY3 else "__unicode__"),)
        for fk in k[0]:
            if fk not in dependclasses:
                clases[fk][3] += 1
        ordered.append([j] + k)

    i = 0
    while i < len(ordered):
        mark = i
        j = i + 1
        while j < len(ordered):
            if ordered[i][0] in ordered[j][1]:
                mark = j
            j += 1
        if mark == i:
            i += 1
        else:
            # swap %s in %s" % ( ordered[i] , ordered[mark]) to make ordered[i] to be at the end
            if ordered[i][0] in ordered[mark][1] and ordered[mark][0] in ordered[i][1]:
                # Resolving simplistic circular ForeignKeys
                print("Not able to resolve circular ForeignKeys between %s and %s" % (ordered[i][1], ordered[mark][0]))
                break
            a = ordered[i]
            ordered[i] = ordered[mark]
            ordered[mark] = a
        if i == len(ordered) - 1:
            break
    ordered.reverse()
    if imports:
        models_txt = str(imports)
    for i in ordered:
        models_txt += '%s\n' % str(i[3])

    return models_txt


if __name__ == '__main__':
    if len(sys.argv) == 2:
        dia2django(sys.argv[1])
    else:
        print(" Use:\n \n   " + sys.argv[0] + " diagram.dia\n\n")
```


## Example 7 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / migrations / 0011_auto_20190418_0137.py**](https://github.com/divio/django-filer/blob/develop/filer/migrations/0011_auto_20190418_0137.py)

```python
# -*- coding: utf-8 -*-
# Generated by Django 2.2 on 2019-04-25 11:29
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0010_auto_20180414_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='folder',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='folder',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterIndexTogether(
            name='folder',
            index_together={('tree_id', 'lft')},
        ),
    ]
```


## Example 8 from django-floppyforms
[django-floppyforms](https://github.com/jazzband/django-floppyforms)
([project documentation](https://django-floppyforms.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-floppyforms/))
is a [Django](/django.html) code library for better control
over rendering HTML forms in your [templates](/template-engines.html).

The django-floppyforms code is provided as
[open source](https://github.com/jazzband/django-floppyforms/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-floppyforms / floppyforms / __future__ / models.py**](https://github.com/jazzband/django-floppyforms/blob/master/floppyforms/__future__/models.py)

```python
# flake8: noqa
import django
from django.db import models as db_models
from django.forms.models import (ModelForm as _ModelForm,
                                 ModelFormMetaclass as _ModelFormMetaclass,
                                 modelform_factory as _modelform_factory,
                                 modelformset_factory as _modelformset_factory,
                                 inlineformset_factory as _inlineformset_factory,
                                 model_to_dict, fields_for_model, BaseModelForm,
                                 BaseModelFormSet,
                                 BaseInlineFormSet)
if django.VERSION < (1, 9):
    from django.forms.models import save_instance
from django.utils import six

from floppyforms import fields
from floppyforms.forms import LayoutRenderer
from floppyforms.models import (ModelChoiceField, ModelMultipleChoiceField)
from floppyforms.widgets import Textarea


__all__ = (
    'ModelForm', 'BaseModelForm', 'model_to_dict', 'fields_for_model',
    'ModelChoiceField', 'ModelMultipleChoiceField',
    'BaseModelFormSet', 'modelformset_factory', 'BaseInlineFormSet',
    'inlineformset_factory',
)
if django.VERSION < (1, 9):
    __all__ += ('save_instance',)


if django.VERSION > (1, 7):
    from django.forms.models import ALL_FIELDS

    __all__ = __all__ + ('ALL_FIELDS',)


FORMFIELD_OVERRIDES = {
    db_models.BooleanField: {'form_class': fields.BooleanField},
    db_models.CharField: {'form_class': fields.CharField},
    db_models.CommaSeparatedIntegerField: {'form_class': fields.CharField},
    db_models.DateField: {'form_class': fields.DateField},
    db_models.DateTimeField: {'form_class': fields.DateTimeField},
    db_models.DecimalField: {'form_class': fields.DecimalField},
    db_models.EmailField: {'form_class': fields.EmailField},
    db_models.FilePathField: {'form_class': fields.FilePathField},
    db_models.FloatField: {'form_class': fields.FloatField},
    db_models.IntegerField: {'form_class': fields.IntegerField},
    db_models.BigIntegerField: {'form_class': fields.IntegerField},
    db_models.GenericIPAddressField: {'form_class': fields.GenericIPAddressField},
    db_models.NullBooleanField: {'form_class': fields.NullBooleanField},
    db_models.PositiveIntegerField: {'form_class': fields.IntegerField},
    db_models.PositiveSmallIntegerField: {'form_class': fields.IntegerField},
    db_models.SlugField: {'form_class': fields.SlugField},
    db_models.SmallIntegerField: {'form_class': fields.IntegerField},
    db_models.TextField: {'form_class': fields.CharField, 'widget': Textarea},
    db_models.TimeField: {'form_class': fields.TimeField},
    db_models.URLField: {'form_class': fields.URLField},
    # Binary field is never editable, so we don't need to convert it.

    db_models.FileField: {'form_class': fields.FileField},
    db_models.ImageField: {'form_class': fields.ImageField},

    db_models.ForeignKey: {'form_class': ModelChoiceField},
    db_models.ManyToManyField: {'form_class': ModelMultipleChoiceField},
    db_models.OneToOneField: {'form_class': ModelChoiceField},
}
if django.VERSION < (1, 9):
    FORMFIELD_OVERRIDES[db_models.IPAddressField] = {'form_class': fields.IPAddressField}

for value in FORMFIELD_OVERRIDES.values():
    value['choices_form_class'] = fields.TypedChoiceField


def formfield_callback(db_field, **kwargs):
    defaults = FORMFIELD_OVERRIDES.get(db_field.__class__, {}).copy()
    defaults.update(kwargs)
    return db_field.formfield(**defaults)


class ModelFormMetaclass(_ModelFormMetaclass):
    def __new__(mcs, name, bases, attrs):
        if not attrs.get('formfield_callback'):
            attrs['formfield_callback'] = formfield_callback
        return super(ModelFormMetaclass, mcs).__new__(mcs, name, bases, attrs)


class ModelForm(six.with_metaclass(ModelFormMetaclass, LayoutRenderer, _ModelForm)):
    pass


def modelform_factory(model, form=ModelForm, fields=None, exclude=None,
                      formfield_callback=formfield_callback, *args, **kwargs):
    return _modelform_factory(model, form, fields, exclude, formfield_callback,
                              *args, **kwargs)


def modelformset_factory(model, form=ModelForm,
                         formfield_callback=formfield_callback,
                         *args, **kwargs):
    return _modelformset_factory(model, form, formfield_callback,
                                 *args, **kwargs)


def inlineformset_factory(parent_model, model, form=ModelForm,
                          formset=BaseInlineFormSet, fk_name=None,
                          fields=None, exclude=None, extra=3, can_order=False,
                          can_delete=True, max_num=None,
                          formfield_callback=formfield_callback,
                          *args, **kwargs):
    return _inlineformset_factory(parent_model, model, form, formset, fk_name,
                                  fields, exclude, extra, can_order,
                                  can_delete, max_num, formfield_callback,
                                  *args, **kwargs)
```


## Example 9 from django-mongonaut
[django-mongonaut](https://github.com/jazzband/django-mongonaut)
([project documentation](https://django-mongonaut.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-mongonaut/))
provides an introspective interface for working with
[MongoDB](/mongodb.html) via mongoengine. The project has its own new code
to map MongoDB to the [Django](/django.html) Admin interface.

django-mongonaut's highlighted features include:

    * Automatic introspection of mongoengine documents
    * The ability to constrain who sees what and what they can do
    * Full control for adding, editing and deleting documents

The django-mongonaut project is open sourced under the
[MIT License](https://github.com/jazzband/django-mongonaut/blob/master/LICENSE.txt)
and it is maintained by the developer community group
[Jazzband](https://jazzband.co/).

[**django-mongonaut / mongonaut / forms / widgets.py**](https://github.com/jazzband/django-mongonaut/blob/master/mongonaut/forms/widgets.py)

```python
# -*- coding: utf-8 -*-

""" Widgets for mongonaut forms"""

from django import forms

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
        EmailField: forms.EmailField
    }

    return FIELD_MAPPING.get(model_field.__class__, forms.CharField)
```


## Example 10 from django-push-notifications
[django-push-notifications](https://github.com/jazzband/django-push-notifications)
is a [Django](/django.html) app for storing and interacting with
push notification services such as
[Google's Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/)
and
[Apple Notifications](https://developer.apple.com/notifications/).
The django-push-notification project's source code is available
open source under the
[MIT license](https://github.com/jazzband/django-push-notifications/blob/master/LICENSE).

[**django-push-notifications / push_notifications / migrations / 0001_initial.py**](https://github.com/jazzband/django-push-notifications/blob/master/push_notifications/migrations/0001_initial.py)

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models

import push_notifications.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='APNSDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name', blank=True)),
                ('active', models.BooleanField(default=True, help_text='Inactive devices will not be sent notifications', verbose_name='Is active')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date', null=True)),
                ('device_id', models.UUIDField(help_text='UDID / UIDevice.identifierForVendor()', max_length=32, null=True, verbose_name='Device ID', blank=True, db_index=True)),
                ('registration_id', models.CharField(unique=True, max_length=64, verbose_name='Registration ID')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'APNS device',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GCMDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name', blank=True)),
                ('active', models.BooleanField(default=True, help_text='Inactive devices will not be sent notifications', verbose_name='Is active')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date', null=True)),
                ('device_id', push_notifications.fields.HexIntegerField(help_text='ANDROID_ID / TelephonyManager.getDeviceId() (always as hex)', null=True, verbose_name='Device ID', blank=True, db_index=True)),
                ('registration_id', models.TextField(verbose_name='Registration ID')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'GCM device',
            },
            bases=(models.Model,),
        ),
    ]
```


## Example 12 from django-taggit
[django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)
([source code](https://github.com/jazzband/django-debug-toolbar) and
[PyPI page](https://pypi.org/project/django-taggit/)) provides a way
to create, store, manage and use tags in a [Django](/django.html) project.
The code for django-taggit is
[open source](https://github.com/jazzband/django-taggit/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-taggit / taggit/migrations / 0001_initial.py**](https://github.com/jazzband/django-taggit/blob/master/taggit/migrations/0001_initial.py)

```python
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("contenttypes", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        help_text="",
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="", unique=True, max_length=100, verbose_name="Name"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="", unique=True, max_length=100, verbose_name="Slug"
                    ),
                ),
            ],
            options={"verbose_name": "Tag", "verbose_name_plural": "Tags"},
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="TaggedItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        help_text="",
                        verbose_name="ID",
                    ),
                ),
                (
                    "object_id",
                    models.IntegerField(
                        help_text="", verbose_name="Object id", db_index=True
                    ),
                ),
                (
                    "content_type",
                    models.ForeignKey(
                        related_name="taggit_taggeditem_tagged_items",
                        verbose_name="Content type",
                        to="contenttypes.ContentType",
                        help_text="",
                        on_delete=models.CASCADE,
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        related_name="taggit_taggeditem_items",
                        to="taggit.Tag",
                        help_text="",
                        on_delete=models.CASCADE,
                    ),
                ),
            ],
            options={
                "verbose_name": "Tagged Item",
                "verbose_name_plural": "Tagged Items",
            },
            bases=(models.Model,),
        ),
    ]
```


## Example 13 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail/core / models.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/core/models.py)

```python
import json
import logging
from collections import defaultdict
from io import StringIO
from urllib.parse import urlparse
from warnings import warn

from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core import checks
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.core.handlers.base import BaseHandler
from django.core.handlers.wsgi import WSGIRequest
from django.db import models, transaction
from django.db.models import Case, Q, Value, When
from django.db.models.functions import Concat, Substr
from django.http import Http404
from django.template.response import TemplateResponse
from django.urls import reverse
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.text import capfirst, slugify
from django.utils.translation import ugettext_lazy as _
from modelcluster.models import (
    ClusterableModel, get_all_child_m2m_relations, get_all_child_relations)
from treebeard.mp_tree import MP_Node

from wagtail.core.query import PageQuerySet, TreeQuerySet
from wagtail.core.signals import page_published, page_unpublished
from wagtail.core.sites import get_site_for_hostname
from wagtail.core.url_routing import RouteResult
from wagtail.core.utils import WAGTAIL_APPEND_SLASH, camelcase_to_underscore, resolve_model_string
from wagtail.search import index
from wagtail.utils.deprecation import RemovedInWagtail29Warning


logger = logging.getLogger('wagtail.core')

PAGE_TEMPLATE_VAR = 'page'


class SiteManager(models.Manager):
    def get_by_natural_key(self, hostname, port):
        return self.get(hostname=hostname, port=port)


class Site(models.Model):
    hostname = models.CharField(verbose_name=_('hostname'), max_length=255, db_index=True)
    port = models.IntegerField(
        verbose_name=_('port'),
        default=80,
        help_text=_(
            "Set this to something other than 80 if you need a specific port number to appear in URLs"
            " (e.g. development on port 8000). Does not affect request handling (so port forwarding still works)."
        )
    )
    site_name = models.CharField(
        verbose_name=_('site name'),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Human-readable name for the site.")
    )
    root_page = models.ForeignKey('Page', verbose_name=_('root page'), related_name='sites_rooted_here', on_delete=models.CASCADE)
    is_default_site = models.BooleanField(
        verbose_name=_('is default site'),
        default=False,
        help_text=_(
            "If true, this site will handle requests for all other hostnames that do not have a site entry of their own"
        )
    )

    objects = SiteManager()

    class Meta:
        unique_together = ('hostname', 'port')
        verbose_name = _('site')
        verbose_name_plural = _('sites')

    def natural_key(self):
        return (self.hostname, self.port)

    def __str__(self):
        if self.site_name:
            return(
                self.site_name
                + (" [default]" if self.is_default_site else "")
            )
        else:
            return(
                self.hostname
                + ("" if self.port == 80 else (":%d" % self.port))
                + (" [default]" if self.is_default_site else "")
            )

    @staticmethod
    def find_for_request(request):
        """
        Find the site object responsible for responding to this HTTP
        request object. Try:

        * unique hostname first
        * then hostname and port
        * if there is no matching hostname at all, or no matching
          hostname:port combination, fall back to the unique default site,
          or raise an exception

        NB this means that high-numbered ports on an extant hostname may
        still be routed to a different hostname which is set as the default
        """

        hostname = request.get_host().split(':')[0]
        port = request.get_port()
        return get_site_for_hostname(hostname, port)

    @property
    def root_url(self):
        if self.port == 80:
            return 'http://%s' % self.hostname
        elif self.port == 443:
            return 'https://%s' % self.hostname
        else:
            return 'http://%s:%d' % (self.hostname, self.port)

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude)
        # Only one site can have the is_default_site flag set
        try:
            default = Site.objects.get(is_default_site=True)
        except Site.DoesNotExist:
            pass
        except Site.MultipleObjectsReturned:
            raise
        else:
            if self.is_default_site and self.pk != default.pk:
                raise ValidationError(
                    {'is_default_site': [
                        _(
                            "%(hostname)s is already configured as the default site."
                            " You must unset that before you can save this site as default."
                        )
                        % {'hostname': default.hostname}
                    ]}
                )

    @staticmethod
    def get_site_root_paths():
        """
        Return a list of (id, root_path, root_url) tuples, most specific path
        first - used to translate url_paths into actual URLs with hostnames
        """
        result = cache.get('wagtail_site_root_paths')

        if result is None:
            result = [
                (site.id, site.root_page.url_path, site.root_url)
                for site in Site.objects.select_related('root_page').order_by(
                    '-root_page__url_path', '-is_default_site', 'hostname')
            ]
            cache.set('wagtail_site_root_paths', result, 3600)

        return result


PAGE_MODEL_CLASSES = []


def get_page_models():
    """
    Returns a list of all non-abstract Page model classes defined in this project.
    """
    return PAGE_MODEL_CLASSES


def get_default_page_content_type():
    """
    Returns the content type to use as a default for pages whose content type
    has been deleted.
    """
    return ContentType.objects.get_for_model(Page)


class BasePageManager(models.Manager):
    def get_queryset(self):
        return self._queryset_class(self.model).order_by('path')


PageManager = BasePageManager.from_queryset(PageQuerySet)


class PageBase(models.base.ModelBase):
    """Metaclass for Page"""
    def __init__(cls, name, bases, dct):
        super(PageBase, cls).__init__(name, bases, dct)

        if 'template' not in dct:
            # Define a default template path derived from the app name and model name
            cls.template = "%s/%s.html" % (cls._meta.app_label, camelcase_to_underscore(name))

        if 'ajax_template' not in dct:
            cls.ajax_template = None

        cls._clean_subpage_models = None  # to be filled in on first call to cls.clean_subpage_models
        cls._clean_parent_page_models = None  # to be filled in on first call to cls.clean_parent_page_models

        # All pages should be creatable unless explicitly set otherwise.
        # This attribute is not inheritable.
        if 'is_creatable' not in dct:
            cls.is_creatable = not cls._meta.abstract

        if not cls._meta.abstract:
            # register this type in the list of page content types
            PAGE_MODEL_CLASSES.append(cls)


class AbstractPage(MP_Node):
    """
    Abstract superclass for Page. According to Django's inheritance rules, managers set on
    abstract models are inherited by subclasses, but managers set on concrete models that are extended
    via multi-table inheritance are not. We therefore need to attach PageManager to an abstract
    superclass to ensure that it is retained by subclasses of Page.
    """
    objects = PageManager()

    class Meta:
        abstract = True


class Page(AbstractPage, index.Indexed, ClusterableModel, metaclass=PageBase):
    title = models.CharField(
        verbose_name=_('title'),
        max_length=255,
        help_text=_("The page title as you'd like it to be seen by the public")
    )
    # to reflect title of a current draft in the admin UI
    draft_title = models.CharField(
        max_length=255,
        editable=False
    )
    slug = models.SlugField(
        verbose_name=_('slug'),
        allow_unicode=True,
        max_length=255,
        help_text=_("The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/")
    )
    content_type = models.ForeignKey(
        'contenttypes.ContentType',
        verbose_name=_('content type'),
        related_name='pages',
        on_delete=models.SET(get_default_page_content_type)
    )
    live = models.BooleanField(verbose_name=_('live'), default=True, editable=False)
    has_unpublished_changes = models.BooleanField(
        verbose_name=_('has unpublished changes'),
        default=False,
        editable=False
    )
    url_path = models.TextField(verbose_name=_('URL path'), blank=True, editable=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('owner'),
        null=True,
        blank=True,
        editable=True,
        on_delete=models.SET_NULL,
        related_name='owned_pages'
    )

    seo_title = models.CharField(
        verbose_name=_("page title"),
        max_length=255,
        blank=True,
        help_text=_("Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.")
    )

    show_in_menus_default = False
    show_in_menus = models.BooleanField(
        verbose_name=_('show in menus'),
        default=False,
        help_text=_("Whether a link to this page will appear in automatically generated menus")
    )
    search_description = models.TextField(verbose_name=_('search description'), blank=True)

    go_live_at = models.DateTimeField(
        verbose_name=_("go live date/time"),
        blank=True,
        null=True
    )
    expire_at = models.DateTimeField(
        verbose_name=_("expiry date/time"),
        blank=True,
        null=True
    )
    expired = models.BooleanField(verbose_name=_('expired'), default=False, editable=False)

    locked = models.BooleanField(verbose_name=_('locked'), default=False, editable=False)

    first_published_at = models.DateTimeField(
        verbose_name=_('first published at'),
        blank=True,
        null=True,
        db_index=True
    )
    last_published_at = models.DateTimeField(
        verbose_name=_('last published at'),
        null=True,
        editable=False
    )
    latest_revision_created_at = models.DateTimeField(
        verbose_name=_('latest revision created at'),
        null=True,
        editable=False
    )
    live_revision = models.ForeignKey(
        'PageRevision',
        related_name='+',
        verbose_name='live revision',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        editable=False
    )

    search_fields = [
        index.SearchField('title', partial_match=True, boost=2),
        index.AutocompleteField('title'),
        index.FilterField('title'),
        index.FilterField('id'),
        index.FilterField('live'),
        index.FilterField('owner'),
        index.FilterField('content_type'),
        index.FilterField('path'),
        index.FilterField('depth'),
        index.FilterField('locked'),
        index.FilterField('show_in_menus'),
        index.FilterField('first_published_at'),
        index.FilterField('last_published_at'),
        index.FilterField('latest_revision_created_at'),
    ]

    # Do not allow plain Page instances to be created through the Wagtail admin
    is_creatable = False

    # Define the maximum number of instances this page type can have. Default to unlimited.
    max_count = None

    # Define the maximum number of instances this page can have under a specific parent. Default to unlimited.
    max_count_per_parent = None

    # An array of additional field names that will not be included when a Page is copied.
    exclude_fields_in_copy = []

    # Define these attributes early to avoid masking errors. (Issue #3078)
    # The canonical definition is in wagtailadmin.edit_handlers.
    content_panels = []
    promote_panels = []
    settings_panels = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.id:
            # this model is being newly created
            # rather than retrieved from the db;
            if not self.content_type_id:
                # set content type to correctly represent the model class
                # that this was created as
                self.content_type = ContentType.objects.get_for_model(self)
            if 'show_in_menus' not in kwargs:
                # if the value is not set on submit refer to the model setting
                self.show_in_menus = self.show_in_menus_default

    def __str__(self):
        return self.title

    def set_url_path(self, parent):
        """
        Populate the url_path field based on this page's slug and the specified parent page.
        (We pass a parent in here, rather than retrieving it via get_parent, so that we can give
        new unsaved pages a meaningful URL when previewing them; at that point the page has not
        been assigned a position in the tree, as far as treebeard is concerned.
        """
        if parent:
            self.url_path = parent.url_path + self.slug + '/'
        else:
            # a page without a parent is the tree root, which always has a url_path of '/'
            self.url_path = '/'

        return self.url_path

    @staticmethod
    def _slug_is_available(slug, parent_page, page=None):
        """
        Determine whether the given slug is available for use on a child page of
        parent_page. If 'page' is passed, the slug is intended for use on that page
        (and so it will be excluded from the duplicate check).
        """
        if parent_page is None:
            # the root page's slug can be whatever it likes...
            return True

        siblings = parent_page.get_children()
        if page:
            siblings = siblings.not_page(page)

        return not siblings.filter(slug=slug).exists()

    def _get_autogenerated_slug(self, base_slug):
        candidate_slug = base_slug
        suffix = 1
        parent_page = self.get_parent()

        while not Page._slug_is_available(candidate_slug, parent_page, self):
            # try with incrementing suffix until we find a slug which is available
            suffix += 1
            candidate_slug = "%s-%d" % (base_slug, suffix)

        return candidate_slug

    def full_clean(self, *args, **kwargs):
        # Apply fixups that need to happen before per-field validation occurs

        if not self.slug:
            # Try to auto-populate slug from title
            base_slug = slugify(self.title, allow_unicode=True)

            # only proceed if we get a non-empty base slug back from slugify
            if base_slug:
                self.slug = self._get_autogenerated_slug(base_slug)

        if not self.draft_title:
            self.draft_title = self.title

        super().full_clean(*args, **kwargs)

    def clean(self):
        super().clean()
        if not Page._slug_is_available(self.slug, self.get_parent(), self):
            raise ValidationError({'slug': _("This slug is already in use")})

    @transaction.atomic
    # ensure that changes are only committed when we have updated all descendant URL paths, to preserve consistency
    def save(self, *args, **kwargs):
        self.full_clean()

        update_descendant_url_paths = False
        is_new = self.id is None

        if is_new:
            # we are creating a record. If we're doing things properly, this should happen
            # through a treebeard method like add_child, in which case the 'path' field
            # has been set and so we can safely call get_parent
            self.set_url_path(self.get_parent())
        else:
            # Check that we are committing the slug to the database
            # Basically: If update_fields has been specified, and slug is not included, skip this step
            if not ('update_fields' in kwargs and 'slug' not in kwargs['update_fields']):
                # see if the slug has changed from the record in the db, in which case we need to
                # update url_path of self and all descendants
                old_record = Page.objects.get(id=self.id)
                if old_record.slug != self.slug:
                    self.set_url_path(self.get_parent())
                    update_descendant_url_paths = True
                    old_url_path = old_record.url_path
                    new_url_path = self.url_path

        result = super().save(*args, **kwargs)

        if update_descendant_url_paths:
            self._update_descendant_url_paths(old_url_path, new_url_path)

        # Check if this is a root page of any sites and clear the 'wagtail_site_root_paths' key if so
        if Site.objects.filter(root_page=self).exists():
            cache.delete('wagtail_site_root_paths')

        # Log
        if is_new:
            cls = type(self)
            logger.info(
                "Page created: \"%s\" id=%d content_type=%s.%s path=%s",
                self.title,
                self.id,
                cls._meta.app_label,
                cls.__name__,
                self.url_path
            )

        return result

    def delete(self, *args, **kwargs):
        # Ensure that deletion always happens on an instance of Page, not a specific subclass. This
        # works around a bug in treebeard <= 3.0 where calling SpecificPage.delete() fails to delete
        # child pages that are not instances of SpecificPage
        if type(self) is Page:
            # this is a Page instance, so carry on as we were
            return super().delete(*args, **kwargs)
        else:
            # retrieve an actual Page instance and delete that instead of self
            return Page.objects.get(id=self.id).delete(*args, **kwargs)

    @classmethod
    def check(cls, **kwargs):
        errors = super(Page, cls).check(**kwargs)

        # Check that foreign keys from pages are not configured to cascade
        # This is the default Django behaviour which must be explicitly overridden
        # to prevent pages disappearing unexpectedly and the tree being corrupted

        # get names of foreign keys pointing to parent classes (such as page_ptr)
        field_exceptions = [field.name
                            for model in [cls] + list(cls._meta.get_parent_list())
                            for field in model._meta.parents.values() if field]

        for field in cls._meta.fields:
            if isinstance(field, models.ForeignKey) and field.name not in field_exceptions:
                if field.remote_field.on_delete == models.CASCADE:
                    errors.append(
                        checks.Warning(
                            "Field hasn't specified on_delete action",
                            hint="Set on_delete=models.SET_NULL and make sure the field is nullable or set on_delete=models.PROTECT. Wagtail does not allow simple database CASCADE because it will corrupt its tree storage.",
                            obj=field,
                            id='wagtailcore.W001',
                        )
                    )

        if not isinstance(cls.objects, PageManager):
            errors.append(
                checks.Error(
                    "Manager does not inherit from PageManager",
                    hint="Ensure that custom Page managers inherit from wagtail.core.models.PageManager",
                    obj=cls,
                    id='wagtailcore.E002',
                )
            )

        try:
            cls.clean_subpage_models()
        except (ValueError, LookupError) as e:
            errors.append(
                checks.Error(
                    "Invalid subpage_types setting for %s" % cls,
                    hint=str(e),
                    id='wagtailcore.E002'
                )
            )

        try:
            cls.clean_parent_page_models()
        except (ValueError, LookupError) as e:
            errors.append(
                checks.Error(
                    "Invalid parent_page_types setting for %s" % cls,
                    hint=str(e),
                    id='wagtailcore.E002'
                )
            )

        return errors

    def _update_descendant_url_paths(self, old_url_path, new_url_path):
        (Page.objects
            .filter(path__startswith=self.path)
            .exclude(pk=self.pk)
            .update(url_path=Concat(
                Value(new_url_path),
                Substr('url_path', len(old_url_path) + 1))))

    #: Return this page in its most specific subclassed form.
    @cached_property
    def specific(self):
        """
        Return this page in its most specific subclassed form.
        """
        # the ContentType.objects manager keeps a cache, so this should potentially
        # avoid a database lookup over doing self.content_type. I think.
        content_type = ContentType.objects.get_for_id(self.content_type_id)
        model_class = content_type.model_class()
        if model_class is None:
            # Cannot locate a model class for this content type. This might happen
            # if the codebase and database are out of sync (e.g. the model exists
            # on a different git branch and we haven't rolled back migrations before
            # switching branches); if so, the best we can do is return the page
            # unchanged.
            return self
        elif isinstance(self, model_class):
            # self is already the an instance of the most specific class
            return self
        else:
            return content_type.get_object_for_this_type(id=self.id)

    #: Return the class that this page would be if instantiated in its
    #: most specific form
    @cached_property
    def specific_class(self):
        """
        Return the class that this page would be if instantiated in its
        most specific form
        """
        content_type = ContentType.objects.get_for_id(self.content_type_id)
        return content_type.model_class()

    def route(self, request, path_components):
        if path_components:
            # request is for a child of this page
            child_slug = path_components[0]
            remaining_components = path_components[1:]

            try:
                subpage = self.get_children().get(slug=child_slug)
            except Page.DoesNotExist:
                raise Http404

            return subpage.specific.route(request, remaining_components)

        else:
            # request is for this very page
            if self.live:
                return RouteResult(self)
            else:
                raise Http404

    def get_admin_display_title(self):
        """
        Return the title for this page as it should appear in the admin backend;
        override this if you wish to display extra contextual information about the page,
        such as language. By default, returns ``draft_title``.
        """
        # Fall back on title if draft_title is blank (which may happen if the page was created
        # in a fixture or migration that didn't explicitly handle draft_title)
        return self.draft_title or self.title

    def save_revision(self, user=None, submitted_for_moderation=False, approved_go_live_at=None, changed=True):
        self.full_clean()

        # Create revision
        revision = self.revisions.create(
            content_json=self.to_json(),
            user=user,
            submitted_for_moderation=submitted_for_moderation,
            approved_go_live_at=approved_go_live_at,
        )

        update_fields = []

        self.latest_revision_created_at = revision.created_at
        update_fields.append('latest_revision_created_at')

        self.draft_title = self.title
        update_fields.append('draft_title')

        if changed:
            self.has_unpublished_changes = True
            update_fields.append('has_unpublished_changes')

        if update_fields:
            self.save(update_fields=update_fields)

        # Log
        logger.info("Page edited: \"%s\" id=%d revision_id=%d", self.title, self.id, revision.id)

        if submitted_for_moderation:
            logger.info("Page submitted for moderation: \"%s\" id=%d revision_id=%d", self.title, self.id, revision.id)

        return revision

    def get_latest_revision(self):
        return self.revisions.order_by('-created_at', '-id').first()

    def get_latest_revision_as_page(self):
        if not self.has_unpublished_changes:
            # Use the live database copy in preference to the revision record, as:
            # 1) this will pick up any changes that have been made directly to the model,
            #    such as automated data imports;
            # 2) it ensures that inline child objects pick up real database IDs even if
            #    those are absent from the revision data. (If this wasn't the case, the child
            #    objects would be recreated with new IDs on next publish - see #1853)
            return self.specific

        latest_revision = self.get_latest_revision()

        if latest_revision:
            return latest_revision.as_page_object()
        else:
            return self.specific

    def unpublish(self, set_expired=False, commit=True):
        if self.live:
            self.live = False
            self.has_unpublished_changes = True
            self.live_revision = None

            if set_expired:
                self.expired = True

            if commit:
                self.save()

            page_unpublished.send(sender=self.specific_class, instance=self.specific)

            logger.info("Page unpublished: \"%s\" id=%d", self.title, self.id)

            self.revisions.update(approved_go_live_at=None)

    def get_context(self, request, *args, **kwargs):
        return {
            PAGE_TEMPLATE_VAR: self,
            'self': self,
            'request': request,
        }

    def get_template(self, request, *args, **kwargs):
        if request.is_ajax():
            return self.ajax_template or self.template
        else:
            return self.template

    def serve(self, request, *args, **kwargs):
        request.is_preview = getattr(request, 'is_preview', False)

        return TemplateResponse(
            request,
            self.get_template(request, *args, **kwargs),
            self.get_context(request, *args, **kwargs)
        )

    def is_navigable(self):
        """
        Return true if it's meaningful to browse subpages of this page -
        i.e. it currently has subpages,
        or it's at the top level (this rule necessary for empty out-of-the-box sites to have working navigation)
        """
        return (not self.is_leaf()) or self.depth == 2

    def _get_site_root_paths(self, request=None):
        """
        Return ``Site.get_site_root_paths()``, using the cached copy on the
        request object if available.
        """
        # if we have a request, use that to cache site_root_paths; otherwise, use self
        cache_object = request if request else self
        try:
            return cache_object._wagtail_cached_site_root_paths
        except AttributeError:
            cache_object._wagtail_cached_site_root_paths = Site.get_site_root_paths()
            return cache_object._wagtail_cached_site_root_paths

    def get_url_parts(self, request=None):
        """
        Determine the URL for this page and return it as a tuple of
        ``(site_id, site_root_url, page_url_relative_to_site_root)``.
        Return None if the page is not routable.

        This is used internally by the ``full_url``, ``url``, ``relative_url``
        and ``get_site`` properties and methods; pages with custom URL routing
        should override this method in order to have those operations return
        the custom URLs.

        Accepts an optional keyword argument ``request``, which may be used
        to avoid repeated database / cache lookups. Typically, a page model
        that overrides ``get_url_parts`` should not need to deal with
        ``request`` directly, and should just pass it to the original method
        when calling ``super``.
        """

        possible_sites = [
            (pk, path, url)
            for pk, path, url in self._get_site_root_paths(request)
            if self.url_path.startswith(path)
        ]

        if not possible_sites:
            return None

        site_id, root_path, root_url = possible_sites[0]

        if hasattr(request, 'site'):
            for site_id, root_path, root_url in possible_sites:
                if site_id == request.site.pk:
                    break
            else:
                site_id, root_path, root_url = possible_sites[0]

        page_path = reverse(
            'wagtail_serve', args=(self.url_path[len(root_path):],))

        # Remove the trailing slash from the URL reverse generates if
        # WAGTAIL_APPEND_SLASH is False and we're not trying to serve
        # the root path
        if not WAGTAIL_APPEND_SLASH and page_path != '/':
            page_path = page_path.rstrip('/')

        return (site_id, root_url, page_path)

    def get_full_url(self, request=None):
        """Return the full URL (including protocol / domain) to this page, or None if it is not routable"""
        url_parts = self.get_url_parts(request=request)

        if url_parts is None:
            # page is not routable
            return

        site_id, root_url, page_path = url_parts

        return root_url + page_path

    full_url = property(get_full_url)

    def get_url(self, request=None, current_site=None):
        """
        Return the 'most appropriate' URL for referring to this page from the pages we serve,
        within the Wagtail backend and actual website templates;
        this is the local URL (starting with '/') if we're only running a single site
        (i.e. we know that whatever the current page is being served from, this link will be on the
        same domain), and the full URL (with domain) if not.
        Return None if the page is not routable.

        Accepts an optional but recommended ``request`` keyword argument that, if provided, will
        be used to cache site-level URL information (thereby avoiding repeated database / cache
        lookups) and, via the ``request.site`` attribute, determine whether a relative or full URL
        is most appropriate.
        """
        # ``current_site`` is purposefully undocumented, as one can simply pass the request and get
        # a relative URL based on ``request.site``. Nonetheless, support it here to avoid
        # copy/pasting the code to the ``relative_url`` method below.
        if current_site is None and request is not None:
            current_site = getattr(request, 'site', None)
        url_parts = self.get_url_parts(request=request)

        if url_parts is None:
            # page is not routable
            return

        site_id, root_url, page_path = url_parts

        if (current_site is not None and site_id == current_site.id) or len(self._get_site_root_paths(request)) == 1:
            # the site matches OR we're only running a single site, so a local URL is sufficient
            return page_path
        else:
            return root_url + page_path

    url = property(get_url)

    def relative_url(self, current_site, request=None):
        """
        Return the 'most appropriate' URL for this page taking into account the site we're currently on;
        a local URL if the site matches, or a fully qualified one otherwise.
        Return None if the page is not routable.

        Accepts an optional but recommended ``request`` keyword argument that, if provided, will
        be used to cache site-level URL information (thereby avoiding repeated database / cache
        lookups).
        """
        return self.get_url(request=request, current_site=current_site)

    def get_site(self):
        """
        Return the Site object that this page belongs to.
        """

        url_parts = self.get_url_parts()

        if url_parts is None:
            # page is not routable
            return

        site_id, root_url, page_path = url_parts

        return Site.objects.get(id=site_id)

    @classmethod
    def get_indexed_objects(cls):
        content_type = ContentType.objects.get_for_model(cls)
        return super(Page, cls).get_indexed_objects().filter(content_type=content_type)

    def get_indexed_instance(self):
        # This is accessed on save by the wagtailsearch signal handler, and in edge
        # cases (e.g. loading test fixtures), may be called before the specific instance's
        # entry has been created. In those cases, we aren't ready to be indexed yet, so
        # return None.
        try:
            return self.specific
        except self.specific_class.DoesNotExist:
            return None

    @classmethod
    def clean_subpage_models(cls):
        """
        Returns the list of subpage types, normalised as model classes.
        Throws ValueError if any entry in subpage_types cannot be recognised as a model name,
        or LookupError if a model does not exist (or is not a Page subclass).
        """
        if cls._clean_subpage_models is None:
            subpage_types = getattr(cls, 'subpage_types', None)
            if subpage_types is None:
                # if subpage_types is not specified on the Page class, allow all page types as subpages
                cls._clean_subpage_models = get_page_models()
            else:
                cls._clean_subpage_models = [
                    resolve_model_string(model_string, cls._meta.app_label)
                    for model_string in subpage_types
                ]

                for model in cls._clean_subpage_models:
                    if not issubclass(model, Page):
                        raise LookupError("%s is not a Page subclass" % model)

        return cls._clean_subpage_models

    @classmethod
    def clean_parent_page_models(cls):
        """
        Returns the list of parent page types, normalised as model classes.
        Throws ValueError if any entry in parent_page_types cannot be recognised as a model name,
        or LookupError if a model does not exist (or is not a Page subclass).
        """

        if cls._clean_parent_page_models is None:
            parent_page_types = getattr(cls, 'parent_page_types', None)
            if parent_page_types is None:
                # if parent_page_types is not specified on the Page class, allow all page types as subpages
                cls._clean_parent_page_models = get_page_models()
            else:
                cls._clean_parent_page_models = [
                    resolve_model_string(model_string, cls._meta.app_label)
                    for model_string in parent_page_types
                ]

                for model in cls._clean_parent_page_models:
                    if not issubclass(model, Page):
                        raise LookupError("%s is not a Page subclass" % model)

        return cls._clean_parent_page_models

    @classmethod
    def allowed_parent_page_models(cls):
        """
        Returns the list of page types that this page type can be a subpage of,
        as a list of model classes
        """
        return [
            parent_model for parent_model in cls.clean_parent_page_models()
            if cls in parent_model.clean_subpage_models()
        ]

    @classmethod
    def allowed_subpage_models(cls):
        """
        Returns the list of page types that this page type can have as subpages,
        as a list of model classes
        """
        return [
            subpage_model for subpage_model in cls.clean_subpage_models()
            if cls in subpage_model.clean_parent_page_models()
        ]

    @classmethod
    def creatable_subpage_models(cls):
        """
        Returns the list of page types that may be created under this page type,
        as a list of model classes
        """
        return [
            page_model for page_model in cls.allowed_subpage_models()
            if page_model.is_creatable
        ]

    @classmethod
    def can_exist_under(cls, parent):
        """
        Checks if this page type can exist as a subpage under a parent page
        instance.

        See also: :func:`Page.can_create_at` and :func:`Page.can_move_to`
        """
        return cls in parent.specific_class.allowed_subpage_models()

    @classmethod
    def can_create_at(cls, parent):
        """
        Checks if this page type can be created as a subpage under a parent
        page instance.
        """
        can_create = cls.is_creatable and cls.can_exist_under(parent)

        if cls.max_count is not None:
            can_create = can_create and cls.objects.count() < cls.max_count

        if cls.max_count_per_parent is not None:
            can_create = can_create and parent.get_children().type(cls).count() < cls.max_count_per_parent

        return can_create

    def can_move_to(self, parent):
        """
        Checks if this page instance can be moved to be a subpage of a parent
        page instance.
        """
        return self.can_exist_under(parent)

    @classmethod
    def get_verbose_name(cls):
        """
        Returns the human-readable "verbose name" of this page model e.g "Blog page".
        """
        # This is similar to doing cls._meta.verbose_name.title()
        # except this doesn't convert any characters to lowercase
        return capfirst(cls._meta.verbose_name)

    @property
    def status_string(self):
        if not self.live:
            if self.expired:
                return _("expired")
            elif self.approved_schedule:
                return _("scheduled")
            else:
                return _("draft")
        else:
            if self.approved_schedule:
                return _("live + scheduled")
            elif self.has_unpublished_changes:
                return _("live + draft")
            else:
                return _("live")

    @property
    def approved_schedule(self):
        return self.revisions.exclude(approved_go_live_at__isnull=True).exists()

    def has_unpublished_subtree(self):
        """
        An awkwardly-defined flag used in determining whether unprivileged editors have
        permission to delete this article. Returns true if and only if this page is non-live,
        and it has no live children.
        """
        return (not self.live) and (not self.get_descendants().filter(live=True).exists())

    @transaction.atomic  # only commit when all descendants are properly updated
    def move(self, target, pos=None):
        """
        Extension to the treebeard 'move' method to ensure that url_path is updated too.
        """
        old_url_path = Page.objects.get(id=self.id).url_path
        super().move(target, pos=pos)
        # treebeard's move method doesn't actually update the in-memory instance, so we need to work
        # with a freshly loaded one now
        new_self = Page.objects.get(id=self.id)
        new_url_path = new_self.set_url_path(new_self.get_parent())
        new_self.save()
        new_self._update_descendant_url_paths(old_url_path, new_url_path)

        # Log
        logger.info("Page moved: \"%s\" id=%d path=%s", self.title, self.id, new_url_path)

    def copy(self, recursive=False, to=None, update_attrs=None, copy_revisions=True, keep_live=True, user=None, process_child_object=None, exclude_fields=None):
        # Fill dict with self.specific values
        specific_self = self.specific
        default_exclude_fields = ['id', 'path', 'depth', 'numchild', 'url_path', 'path', 'index_entries']
        exclude_fields = default_exclude_fields + specific_self.exclude_fields_in_copy + (exclude_fields or [])
        specific_dict = {}

        for field in specific_self._meta.get_fields():
            # Ignore explicitly excluded fields
            if field.name in exclude_fields:
                continue

            # Ignore reverse relations
            if field.auto_created:
                continue

            # Ignore m2m relations - they will be copied as child objects
            # if modelcluster supports them at all (as it does for tags)
            if field.many_to_many:
                continue

            # Ignore parent links (page_ptr)
            if isinstance(field, models.OneToOneField) and field.remote_field.parent_link:
                continue

            specific_dict[field.name] = getattr(specific_self, field.name)

        # copy child m2m relations
        for related_field in get_all_child_m2m_relations(specific_self):
            field = getattr(specific_self, related_field.name)
            if field and hasattr(field, 'all'):
                values = field.all()
                if values:
                    specific_dict[related_field.name] = values

        # New instance from prepared dict values, in case the instance class implements multiple levels inheritance
        page_copy = self.specific_class(**specific_dict)

        if not keep_live:
            page_copy.live = False
            page_copy.has_unpublished_changes = True
            page_copy.live_revision = None
            page_copy.first_published_at = None
            page_copy.last_published_at = None

        if user:
            page_copy.owner = user

        if update_attrs:
            for field, value in update_attrs.items():
                setattr(page_copy, field, value)

        if to:
            if recursive and (to == self or to.is_descendant_of(self)):
                raise Exception("You cannot copy a tree branch recursively into itself")
            page_copy = to.add_child(instance=page_copy)
        else:
            page_copy = self.add_sibling(instance=page_copy)

        # A dict that maps child objects to their new ids
        # Used to remap child object ids in revisions
        child_object_id_map = defaultdict(dict)

        # Copy child objects
        specific_self = self.specific
        for child_relation in get_all_child_relations(specific_self):
            accessor_name = child_relation.get_accessor_name()

            if accessor_name in exclude_fields:
                continue

            parental_key_name = child_relation.field.attname
            child_objects = getattr(specific_self, accessor_name, None)

            if child_objects:
                for child_object in child_objects.all():
                    old_pk = child_object.pk
                    child_object.pk = None
                    setattr(child_object, parental_key_name, page_copy.id)

                    if process_child_object is not None:
                        process_child_object(specific_self, page_copy, child_relation, child_object)

                    child_object.save()

                    # Add mapping to new primary key (so we can apply this change to revisions)
                    child_object_id_map[accessor_name][old_pk] = child_object.pk

        # Copy revisions
        if copy_revisions:
            for revision in self.revisions.all():
                revision.pk = None
                revision.submitted_for_moderation = False
                revision.approved_go_live_at = None
                revision.page = page_copy

                # Update ID fields in content
                revision_content = json.loads(revision.content_json)
                revision_content['pk'] = page_copy.pk

                for child_relation in get_all_child_relations(specific_self):
                    accessor_name = child_relation.get_accessor_name()
                    try:
                        child_objects = revision_content[accessor_name]
                    except KeyError:
                        # KeyErrors are possible if the revision was created
                        # before this child relation was added to the database
                        continue

                    for child_object in child_objects:
                        child_object[child_relation.field.name] = page_copy.pk

                        # Remap primary key to copied versions
                        # If the primary key is not recognised (eg, the child object has been deleted from the database)
                        # set the primary key to None
                        child_object['pk'] = child_object_id_map[accessor_name].get(child_object['pk'], None)

                revision.content_json = json.dumps(revision_content)

                # Save
                revision.save()

        # Create a new revision
        # This code serves a few purposes:
        # * It makes sure update_attrs gets applied to the latest revision
        # * It bumps the last_revision_created_at value so the new page gets ordered as if it was just created
        # * It sets the user of the new revision so it's possible to see who copied the page by looking at its history
        latest_revision = page_copy.get_latest_revision_as_page()

        if update_attrs:
            for field, value in update_attrs.items():
                setattr(latest_revision, field, value)

        latest_revision_as_page_revision = latest_revision.save_revision(user=user, changed=False)
        if keep_live:
            page_copy.live_revision = latest_revision_as_page_revision
            page_copy.last_published_at = latest_revision_as_page_revision.created_at
            page_copy.first_published_at = latest_revision_as_page_revision.created_at
            page_copy.save()

        # Log
        logger.info("Page copied: \"%s\" id=%d from=%d", page_copy.title, page_copy.id, self.id)

        # Copy child pages
        if recursive:
            for child_page in self.get_children():
                child_page.specific.copy(
                    recursive=True,
                    to=page_copy,
                    copy_revisions=copy_revisions,
                    keep_live=keep_live,
                    user=user,
                    process_child_object=process_child_object,
                )

        return page_copy

    copy.alters_data = True

    def permissions_for_user(self, user):
        """
        Return a PagePermissionsTester object defining what actions the user can perform on this page
        """
        user_perms = UserPagePermissionsProxy(user)
        return user_perms.for_page(self)

    def make_preview_request(self, original_request=None, preview_mode=None, extra_request_attrs=None):
        """
        Simulate a request to this page, by constructing a fake HttpRequest object that is (as far
        as possible) representative of a real request to this page's front-end URL, and invoking
        serve_preview with that request (and the given preview_mode).

        Used for previewing / moderation and any other place where we
        want to display a view of this page in the admin interface without going through the regular
        page routing logic.

        If you pass in a real request object as original_request, additional information (e.g. client IP, cookies)
        will be included in the dummy request.
        """
        dummy_meta = self._get_dummy_headers(original_request)
        request = WSGIRequest(dummy_meta)

        # Add a flag to let middleware know that this is a dummy request.
        request.is_dummy = True

        if extra_request_attrs:
            for k, v in extra_request_attrs.items():
                setattr(request, k, v)

        page = self

        # Build a custom django.core.handlers.BaseHandler subclass that invokes serve_preview as
        # the eventual view function called at the end of the middleware chain, rather than going
        # through the URL resolver
        class Handler(BaseHandler):
            def _get_response(self, request):
                response = page.serve_preview(request, preview_mode)
                if hasattr(response, 'render') and callable(response.render):
                    response = response.render()
                return response

        # Invoke this custom handler.
        handler = Handler()
        handler.load_middleware()
        return handler.get_response(request)

    def _get_dummy_headers(self, original_request=None):
        """
        Return a dict of META information to be included in a faked HttpRequest object to pass to
        serve_preview.
        """
        url = self.full_url
        if url:
            url_info = urlparse(url)
            hostname = url_info.hostname
            path = url_info.path
            port = url_info.port or (443 if url_info.scheme == 'https' else 80)
            scheme = url_info.scheme
        else:
            # Cannot determine a URL to this page - cobble one together based on
            # whatever we find in ALLOWED_HOSTS
            try:
                hostname = settings.ALLOWED_HOSTS[0]
                if hostname == '*':
                    # '*' is a valid value to find in ALLOWED_HOSTS[0], but it's not a valid domain name.
                    # So we pretend it isn't there.
                    raise IndexError
            except IndexError:
                hostname = 'localhost'
            path = '/'
            port = 80
            scheme = 'http'

        http_host = hostname
        if port != (443 if scheme == 'https' else 80):
            http_host = '%s:%s' % (http_host, port)
        dummy_values = {
            'REQUEST_METHOD': 'GET',
            'PATH_INFO': path,
            'SERVER_NAME': hostname,
            'SERVER_PORT': port,
            'SERVER_PROTOCOL': 'HTTP/1.1',
            'HTTP_HOST': http_host,
            'wsgi.version': (1, 0),
            'wsgi.input': StringIO(),
            'wsgi.errors': StringIO(),
            'wsgi.url_scheme': scheme,
            'wsgi.multithread': True,
            'wsgi.multiprocess': True,
            'wsgi.run_once': False,
        }

        # Add important values from the original request object, if it was provided.
        HEADERS_FROM_ORIGINAL_REQUEST = [
            'REMOTE_ADDR', 'HTTP_X_FORWARDED_FOR', 'HTTP_COOKIE', 'HTTP_USER_AGENT', 'HTTP_AUTHORIZATION',
            'wsgi.version', 'wsgi.multithread', 'wsgi.multiprocess', 'wsgi.run_once',
        ]
        if settings.SECURE_PROXY_SSL_HEADER:
            HEADERS_FROM_ORIGINAL_REQUEST.append(settings.SECURE_PROXY_SSL_HEADER[0])
        if original_request:
            for header in HEADERS_FROM_ORIGINAL_REQUEST:
                if header in original_request.META:
                    dummy_values[header] = original_request.META[header]

        return dummy_values

    def dummy_request(self, original_request=None, **meta):
        warn(
            "Page.dummy_request is deprecated. Use Page.make_preview_request instead",
            category=RemovedInWagtail29Warning
        )

        dummy_values = self._get_dummy_headers(original_request)

        # Add additional custom metadata sent by the caller.
        dummy_values.update(**meta)

        request = WSGIRequest(dummy_values)

        # Add a flag to let middleware know that this is a dummy request.
        request.is_dummy = True

        # Apply middleware to the request
        handler = BaseHandler()
        handler.load_middleware()
        handler._middleware_chain(request)

        return request

    DEFAULT_PREVIEW_MODES = [('', _('Default'))]

    @property
    def preview_modes(self):
        """
        A list of (internal_name, display_name) tuples for the modes in which
        this page can be displayed for preview/moderation purposes. Ordinarily a page
        will only have one display mode, but subclasses of Page can override this -
        for example, a page containing a form might have a default view of the form,
        and a post-submission 'thankyou' page
        """
        return Page.DEFAULT_PREVIEW_MODES

    @property
    def default_preview_mode(self):
        return self.preview_modes[0][0]

    def serve_preview(self, request, mode_name):
        """
        Return an HTTP response for use in page previews. Normally this would be equivalent
        to self.serve(request), since we obviously want the preview to be indicative of how
        it looks on the live site. However, there are a couple of cases where this is not
        appropriate, and custom behaviour is required:

        1) The page has custom routing logic that derives some additional required
        args/kwargs to be passed to serve(). The routing mechanism is bypassed when
        previewing, so there's no way to know what args we should pass. In such a case,
        the page model needs to implement its own version of serve_preview.

        2) The page has several different renderings that we would like to be able to see
        when previewing - for example, a form page might have one rendering that displays
        the form, and another rendering to display a landing page when the form is posted.
        This can be done by setting a custom preview_modes list on the page model -
        Wagtail will allow the user to specify one of those modes when previewing, and
        pass the chosen mode_name to serve_preview so that the page model can decide how
        to render it appropriately. (Page models that do not specify their own preview_modes
        list will always receive an empty string as mode_name.)

        Any templates rendered during this process should use the 'request' object passed
        here - this ensures that request.user and other properties are set appropriately for
        the wagtail user bar to be displayed. This request will always be a GET.
        """
        request.is_preview = True

        return self.serve(request)

    def get_cached_paths(self):
        """
        This returns a list of paths to invalidate in a frontend cache
        """
        return ['/']

    def get_sitemap_urls(self, request=None):
        return [
            {
                'location': self.get_full_url(request),
                # fall back on latest_revision_created_at if last_published_at is null
                # (for backwards compatibility from before last_published_at was added)
                'lastmod': (self.last_published_at or self.latest_revision_created_at),
            }
        ]

    def get_static_site_paths(self):
        """
        This is a generator of URL paths to feed into a static site generator
        Override this if you would like to create static versions of subpages
        """
        # Yield path for this page
        yield '/'

        # Yield paths for child pages
        for child in self.get_children().live():
            for path in child.specific.get_static_site_paths():
                yield '/' + child.slug + path

    def get_ancestors(self, inclusive=False):
        """
        Returns a queryset of the current page's ancestors, starting at the root page
        and descending to the parent, or to the current page itself if ``inclusive`` is true.
        """
        return Page.objects.ancestor_of(self, inclusive)

    def get_descendants(self, inclusive=False):
        """
        Returns a queryset of all pages underneath the current page, any number of levels deep.
        If ``inclusive`` is true, the current page itself is included in the queryset.
        """
        return Page.objects.descendant_of(self, inclusive)

    def get_siblings(self, inclusive=True):
        """
        Returns a queryset of all other pages with the same parent as the current page.
        If ``inclusive`` is true, the current page itself is included in the queryset.
        """
        return Page.objects.sibling_of(self, inclusive)

    def get_next_siblings(self, inclusive=False):
        return self.get_siblings(inclusive).filter(path__gte=self.path).order_by('path')

    def get_prev_siblings(self, inclusive=False):
        return self.get_siblings(inclusive).filter(path__lte=self.path).order_by('-path')

    def get_view_restrictions(self):
        """Return a query set of all page view restrictions that apply to this page"""
        return PageViewRestriction.objects.filter(page__in=self.get_ancestors(inclusive=True))

    password_required_template = getattr(settings, 'PASSWORD_REQUIRED_TEMPLATE', 'wagtailcore/password_required.html')

    def serve_password_required_response(self, request, form, action_url):
        """
        Serve a response indicating that the user has been denied access to view this page,
        and must supply a password.
        form = a Django form object containing the password input
            (and zero or more hidden fields that also need to be output on the template)
        action_url = URL that this form should be POSTed to
        """
        context = self.get_context(request)
        context['form'] = form
        context['action_url'] = action_url
        return TemplateResponse(request, self.password_required_template, context)

    def with_content_json(self, content_json):
        """
        Returns a new version of the page with field values updated to reflect changes
        in the provided ``content_json`` (which usually comes from a previously-saved
        page revision).

        Certain field values are preserved in order to prevent errors if the returned
        page is saved, such as ``id``, ``content_type`` and some tree-related values.
        The following field values are also preserved, as they are considered to be
        meaningful to the page as a whole, rather than to a specific revision:

        * ``draft_title``
        * ``live``
        * ``has_unpublished_changes``
        * ``owner``
        * ``locked``
        * ``latest_revision_created_at``
        * ``first_published_at``
        """

        obj = self.specific_class.from_json(content_json)

        # These should definitely never change between revisions
        obj.pk = self.pk
        obj.content_type = self.content_type

        # Override possibly-outdated tree parameter fields
        obj.path = self.path
        obj.depth = self.depth
        obj.numchild = self.numchild

        # Update url_path to reflect potential slug changes, but maintining the page's
        # existing tree position
        obj.set_url_path(self.get_parent())

        # Ensure other values that are meaningful for the page as a whole (rather than
        # to a specific revision) are preserved
        obj.draft_title = self.draft_title
        obj.live = self.live
        obj.has_unpublished_changes = self.has_unpublished_changes
        obj.owner = self.owner
        obj.locked = self.locked
        obj.latest_revision_created_at = self.latest_revision_created_at
        obj.first_published_at = self.first_published_at

        return obj

    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')


class Orderable(models.Model):
    sort_order = models.IntegerField(null=True, blank=True, editable=False)
    sort_order_field = 'sort_order'

    class Meta:
        abstract = True
        ordering = ['sort_order']


class SubmittedRevisionsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(submitted_for_moderation=True)


class PageRevision(models.Model):
    page = models.ForeignKey('Page', verbose_name=_('page'), related_name='revisions', on_delete=models.CASCADE)
    submitted_for_moderation = models.BooleanField(
        verbose_name=_('submitted for moderation'),
        default=False,
        db_index=True
    )
    created_at = models.DateTimeField(db_index=True, verbose_name=_('created at'))
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_('user'), null=True, blank=True,
        on_delete=models.SET_NULL
    )
    content_json = models.TextField(verbose_name=_('content JSON'))
    approved_go_live_at = models.DateTimeField(verbose_name=_('approved go live at'), null=True, blank=True)

    objects = models.Manager()
    submitted_revisions = SubmittedRevisionsManager()

    def save(self, *args, **kwargs):
        # Set default value for created_at to now
        # We cannot use auto_now_add as that will override
        # any value that is set before saving
        if self.created_at is None:
            self.created_at = timezone.now()

        super().save(*args, **kwargs)
        if self.submitted_for_moderation:
            # ensure that all other revisions of this page have the 'submitted for moderation' flag unset
            self.page.revisions.exclude(id=self.id).update(submitted_for_moderation=False)

    def as_page_object(self):
        return self.page.specific.with_content_json(self.content_json)

    def approve_moderation(self):
        if self.submitted_for_moderation:
            logger.info("Page moderation approved: \"%s\" id=%d revision_id=%d", self.page.title, self.page.id, self.id)
            self.publish()

    def reject_moderation(self):
        if self.submitted_for_moderation:
            logger.info("Page moderation rejected: \"%s\" id=%d revision_id=%d", self.page.title, self.page.id, self.id)
            self.submitted_for_moderation = False
            self.save(update_fields=['submitted_for_moderation'])

    def is_latest_revision(self):
        if self.id is None:
            # special case: a revision without an ID is presumed to be newly-created and is thus
            # newer than any revision that might exist in the database
            return True
        latest_revision = PageRevision.objects.filter(page_id=self.page_id).order_by('-created_at', '-id').first()
        return (latest_revision == self)

    def publish(self):
        page = self.as_page_object()
        if page.go_live_at and page.go_live_at > timezone.now():
            page.has_unpublished_changes = True
            # Instead set the approved_go_live_at of this revision
            self.approved_go_live_at = page.go_live_at
            self.save()
            # And clear the the approved_go_live_at of any other revisions
            page.revisions.exclude(id=self.id).update(approved_go_live_at=None)
            # if we are updating a currently live page skip the rest
            if page.live_revision:
                return
            # if we have a go_live in the future don't make the page live
            page.live = False
        else:
            page.live = True
            # at this point, the page has unpublished changes iff there are newer revisions than this one
            page.has_unpublished_changes = not self.is_latest_revision()
            # If page goes live clear the approved_go_live_at of all revisions
            page.revisions.update(approved_go_live_at=None)
        page.expired = False  # When a page is published it can't be expired

        # Set first_published_at, last_published_at and live_revision
        # if the page is being published now
        if page.live:
            now = timezone.now()
            page.last_published_at = now
            page.live_revision = self

            if page.first_published_at is None:
                page.first_published_at = now
        else:
            # Unset live_revision if the page is going live in the future
            page.live_revision = None

        page.save()
        self.submitted_for_moderation = False
        page.revisions.update(submitted_for_moderation=False)

        if page.live:
            page_published.send(sender=page.specific_class, instance=page.specific, revision=self)

            logger.info("Page published: \"%s\" id=%d revision_id=%d", page.title, page.id, self.id)
        elif page.go_live_at:
            logger.info(
                "Page scheduled for publish: \"%s\" id=%d revision_id=%d go_live_at=%s",
                page.title,
                page.id,
                self.id,
                page.go_live_at.isoformat()
            )

    def get_previous(self):
        return self.get_previous_by_created_at(page=self.page)

    def get_next(self):
        return self.get_next_by_created_at(page=self.page)

    def __str__(self):
        return '"' + str(self.page) + '" at ' + str(self.created_at)

    class Meta:
        verbose_name = _('page revision')
        verbose_name_plural = _('page revisions')


PAGE_PERMISSION_TYPES = [
    ('add', _("Add"), _("Add/edit pages you own")),
    ('edit', _("Edit"), _("Edit any page")),
    ('publish', _("Publish"), _("Publish any page")),
    ('bulk_delete', _("Bulk delete"), _("Delete pages with children")),
    ('lock', _("Lock"), _("Lock/unlock any page")),
]

PAGE_PERMISSION_TYPE_CHOICES = [
    (identifier, long_label)
    for identifier, short_label, long_label in PAGE_PERMISSION_TYPES
]


class GroupPagePermission(models.Model):
    group = models.ForeignKey(Group, verbose_name=_('group'), related_name='page_permissions', on_delete=models.CASCADE)
    page = models.ForeignKey('Page', verbose_name=_('page'), related_name='group_permissions', on_delete=models.CASCADE)
    permission_type = models.CharField(
        verbose_name=_('permission type'),
        max_length=20,
        choices=PAGE_PERMISSION_TYPE_CHOICES
    )

    class Meta:
        unique_together = ('group', 'page', 'permission_type')
        verbose_name = _('group page permission')
        verbose_name_plural = _('group page permissions')

    def __str__(self):
        return "Group %d ('%s') has permission '%s' on page %d ('%s')" % (
            self.group.id, self.group,
            self.permission_type,
            self.page.id, self.page
        )


class UserPagePermissionsProxy:
    """Helper object that encapsulates all the page permission rules that this user has
    across the page hierarchy."""

    def __init__(self, user):
        self.user = user

        if user.is_active and not user.is_superuser:
            self.permissions = GroupPagePermission.objects.filter(group__user=self.user).select_related('page')

    def revisions_for_moderation(self):
        """Return a queryset of page revisions awaiting moderation that this user has publish permission on"""

        # Deal with the trivial cases first...
        if not self.user.is_active:
            return PageRevision.objects.none()
        if self.user.is_superuser:
            return PageRevision.submitted_revisions.all()

        # get the list of pages for which they have direct publish permission
        # (i.e. they can publish any page within this subtree)
        publishable_pages_paths = self.permissions.filter(
            permission_type='publish'
        ).values_list('page__path', flat=True).distinct()
        if not publishable_pages_paths:
            return PageRevision.objects.none()

        # compile a filter expression to apply to the PageRevision.submitted_revisions manager:
        # return only those pages whose paths start with one of the publishable_pages paths
        only_my_sections = Q(page__path__startswith=publishable_pages_paths[0])
        for page_path in publishable_pages_paths[1:]:
            only_my_sections = only_my_sections | Q(page__path__startswith=page_path)

        # return the filtered queryset
        return PageRevision.submitted_revisions.filter(only_my_sections)

    def for_page(self, page):
        """Return a PagePermissionTester object that can be used to query whether this user has
        permission to perform specific tasks on the given page"""
        return PagePermissionTester(self, page)

    def explorable_pages(self):
        """Return a queryset of pages that the user has access to view in the
        explorer (e.g. add/edit/publish permission). Includes all pages with
        specific group permissions and also the ancestors of those pages (in
        order to enable navigation in the explorer)"""
        # Deal with the trivial cases first...
        if not self.user.is_active:
            return Page.objects.none()
        if self.user.is_superuser:
            return Page.objects.all()

        explorable_pages = Page.objects.none()

        # Creates a union queryset of all objects the user has access to add,
        # edit and publish
        for perm in self.permissions.filter(
            Q(permission_type="add")
            | Q(permission_type="edit")
            | Q(permission_type="publish")
            | Q(permission_type="lock")
        ):
            explorable_pages |= Page.objects.descendant_of(
                perm.page, inclusive=True
            )

        # For all pages with specific permissions, add their ancestors as
        # explorable. This will allow deeply nested pages to be accessed in the
        # explorer. For example, in the hierarchy A>B>C>D where the user has
        # 'edit' access on D, they will be able to navigate to D without having
        # explicit access to A, B or C.
        page_permissions = Page.objects.filter(group_permissions__in=self.permissions)
        for page in page_permissions:
            explorable_pages |= page.get_ancestors()

        # Remove unnecessary top-level ancestors that the user has no access to
        fca_page = page_permissions.first_common_ancestor()
        explorable_pages = explorable_pages.filter(path__startswith=fca_page.path)

        return explorable_pages

    def editable_pages(self):
        """Return a queryset of the pages that this user has permission to edit"""
        # Deal with the trivial cases first...
        if not self.user.is_active:
            return Page.objects.none()
        if self.user.is_superuser:
            return Page.objects.all()

        editable_pages = Page.objects.none()

        for perm in self.permissions.filter(permission_type='add'):
            # user has edit permission on any subpage of perm.page
            # (including perm.page itself) that is owned by them
            editable_pages |= Page.objects.descendant_of(perm.page, inclusive=True).filter(owner=self.user)

        for perm in self.permissions.filter(permission_type='edit'):
            # user has edit permission on any subpage of perm.page
            # (including perm.page itself) regardless of owner
            editable_pages |= Page.objects.descendant_of(perm.page, inclusive=True)

        return editable_pages

    def can_edit_pages(self):
        """Return True if the user has permission to edit any pages"""
        return self.editable_pages().exists()

    def publishable_pages(self):
        """Return a queryset of the pages that this user has permission to publish"""
        # Deal with the trivial cases first...
        if not self.user.is_active:
            return Page.objects.none()
        if self.user.is_superuser:
            return Page.objects.all()

        publishable_pages = Page.objects.none()

        for perm in self.permissions.filter(permission_type='publish'):
            # user has publish permission on any subpage of perm.page
            # (including perm.page itself)
            publishable_pages |= Page.objects.descendant_of(perm.page, inclusive=True)

        return publishable_pages

    def can_publish_pages(self):
        """Return True if the user has permission to publish any pages"""
        return self.publishable_pages().exists()


class PagePermissionTester:
    def __init__(self, user_perms, page):
        self.user = user_perms.user
        self.user_perms = user_perms
        self.page = page
        self.page_is_root = page.depth == 1  # Equivalent to page.is_root()

        if self.user.is_active and not self.user.is_superuser:
            self.permissions = set(
                perm.permission_type for perm in user_perms.permissions
                if self.page.path.startswith(perm.page.path)
            )

    def can_add_subpage(self):
        if not self.user.is_active:
            return False
        specific_class = self.page.specific_class
        if specific_class is None or not specific_class.creatable_subpage_models():
            return False
        return self.user.is_superuser or ('add' in self.permissions)

    def can_edit(self):
        if not self.user.is_active:
            return False
        if self.page_is_root:  # root node is not a page and can never be edited, even by superusers
            return False
        return (
            self.user.is_superuser
            or ('edit' in self.permissions)
            or ('add' in self.permissions and self.page.owner_id == self.user.pk)
        )

    def can_delete(self):
        if not self.user.is_active:
            return False
        if self.page_is_root:  # root node is not a page and can never be deleted, even by superusers
            return False

        if self.user.is_superuser:
            # superusers require no further checks
            return True

        # if the user does not have bulk_delete permission, they may only delete leaf pages
        if 'bulk_delete' not in self.permissions and not self.page.is_leaf():
            return False

        if 'edit' in self.permissions:
            # if the user does not have publish permission, we also need to confirm that there
            # are no published pages here
            if 'publish' not in self.permissions:
                pages_to_delete = self.page.get_descendants(inclusive=True)
                if pages_to_delete.live().exists():
                    return False

            return True

        elif 'add' in self.permissions:
            pages_to_delete = self.page.get_descendants(inclusive=True)
            if 'publish' in self.permissions:
                # we don't care about live state, but all pages must be owned by this user
                # (i.e. eliminating pages owned by this user must give us the empty set)
                return not pages_to_delete.exclude(owner=self.user).exists()
            else:
                # all pages must be owned by this user and non-live
                # (i.e. eliminating non-live pages owned by this user must give us the empty set)
                return not pages_to_delete.exclude(live=False, owner=self.user).exists()

        else:
            return False

    def can_unpublish(self):
        if not self.user.is_active:
            return False
        if (not self.page.live) or self.page_is_root:
            return False
        if self.page.locked:
            return False

        return self.user.is_superuser or ('publish' in self.permissions)

    def can_publish(self):
        if not self.user.is_active:
            return False
        if self.page_is_root:
            return False

        return self.user.is_superuser or ('publish' in self.permissions)

    def can_set_view_restrictions(self):
        return self.can_publish()

    def can_unschedule(self):
        return self.can_publish()

    def can_lock(self):
        return self.user.is_superuser or ('lock' in self.permissions)

    def can_publish_subpage(self):
        """
        Niggly special case for creating and publishing a page in one go.
        Differs from can_publish in that we want to be able to publish subpages of root, but not
        to be able to publish root itself. (Also, can_publish_subpage returns false if the page
        does not allow subpages at all.)
        """
        if not self.user.is_active:
            return False
        specific_class = self.page.specific_class
        if specific_class is None or not specific_class.creatable_subpage_models():
            return False

        return self.user.is_superuser or ('publish' in self.permissions)

    def can_reorder_children(self):
        """
        Keep reorder permissions the same as publishing, since it immediately affects published pages
        (and the use-cases for a non-admin needing to do it are fairly obscure...)
        """
        return self.can_publish_subpage()

    def can_move(self):
        """
        Moving a page should be logically equivalent to deleting and re-adding it (and all its children).
        As such, the permission test for 'can this be moved at all?' should be the same as for deletion.
        (Further constraints will then apply on where it can be moved *to*.)
        """
        return self.can_delete()

    def can_copy(self):
        return not self.page_is_root

    def can_move_to(self, destination):
        # reject the logically impossible cases first
        if self.page == destination or destination.is_descendant_of(self.page):
            return False

        # reject moves that are forbidden by subpage_types / parent_page_types rules
        # (these rules apply to superusers too)
        if not self.page.specific.can_move_to(destination):
            return False

        # shortcut the trivial 'everything' / 'nothing' permissions
        if not self.user.is_active:
            return False
        if self.user.is_superuser:
            return True

        # check that the page can be moved at all
        if not self.can_move():
            return False

        # Inspect permissions on the destination
        destination_perms = self.user_perms.for_page(destination)

        # we always need at least add permission in the target
        if 'add' not in destination_perms.permissions:
            return False

        if self.page.live or self.page.get_descendants().filter(live=True).exists():
            # moving this page will entail publishing within the destination section
            return ('publish' in destination_perms.permissions)
        else:
            # no publishing required, so the already-tested 'add' permission is sufficient
            return True

    def can_copy_to(self, destination, recursive=False):
        # reject the logically impossible cases first
        # recursive can't copy to the same tree otherwise it will be on infinite loop
        if recursive and (self.page == destination or destination.is_descendant_of(self.page)):
            return False

        # reject inactive users early
        if not self.user.is_active:
            return False

        # reject early if pages of this type cannot be created at the destination
        if not self.page.specific_class.can_create_at(destination):
            return False

        # skip permission checking for super users
        if self.user.is_superuser:
            return True

        # Inspect permissions on the destination
        destination_perms = self.user_perms.for_page(destination)

        if not destination.specific_class.creatable_subpage_models():
            return False

        # we always need at least add permission in the target
        if 'add' not in destination_perms.permissions:
            return False

        return True

    def can_view_revisions(self):
        return not self.page_is_root


class BaseViewRestriction(models.Model):
    NONE = 'none'
    PASSWORD = 'password'
    GROUPS = 'groups'
    LOGIN = 'login'

    RESTRICTION_CHOICES = (
        (NONE, _("Public")),
        (LOGIN, _("Private, accessible to logged-in users")),
        (PASSWORD, _("Private, accessible with the following password")),
        (GROUPS, _("Private, accessible to users in specific groups")),
    )

    restriction_type = models.CharField(
        max_length=20, choices=RESTRICTION_CHOICES)
    password = models.CharField(verbose_name=_('password'), max_length=255, blank=True)
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True)

    def accept_request(self, request):
        if self.restriction_type == BaseViewRestriction.PASSWORD:
            passed_restrictions = request.session.get(self.passed_view_restrictions_session_key, [])
            if self.id not in passed_restrictions:
                return False

        elif self.restriction_type == BaseViewRestriction.LOGIN:
            if not request.user.is_authenticated:
                return False

        elif self.restriction_type == BaseViewRestriction.GROUPS:
            if not request.user.is_superuser:
                current_user_groups = request.user.groups.all()

                if not any(group in current_user_groups for group in self.groups.all()):
                    return False

        return True

    def mark_as_passed(self, request):
        """
        Update the session data in the request to mark the user as having passed this
        view restriction
        """
        has_existing_session = (settings.SESSION_COOKIE_NAME in request.COOKIES)
        passed_restrictions = request.session.setdefault(self.passed_view_restrictions_session_key, [])
        if self.id not in passed_restrictions:
            passed_restrictions.append(self.id)
            request.session[self.passed_view_restrictions_session_key] = passed_restrictions
        if not has_existing_session:
            # if this is a session we've created, set it to expire at the end
            # of the browser session
            request.session.set_expiry(0)

    class Meta:
        abstract = True
        verbose_name = _('view restriction')
        verbose_name_plural = _('view restrictions')


class PageViewRestriction(BaseViewRestriction):
    page = models.ForeignKey(
        'Page', verbose_name=_('page'), related_name='view_restrictions', on_delete=models.CASCADE
    )

    passed_view_restrictions_session_key = 'passed_page_view_restrictions'

    class Meta:
        verbose_name = _('page view restriction')
        verbose_name_plural = _('page view restrictions')


class BaseCollectionManager(models.Manager):
    def get_queryset(self):
        return TreeQuerySet(self.model).order_by('path')


CollectionManager = BaseCollectionManager.from_queryset(TreeQuerySet)


class CollectionViewRestriction(BaseViewRestriction):
    collection = models.ForeignKey(
        'Collection',
        verbose_name=_('collection'),
        related_name='view_restrictions',
        on_delete=models.CASCADE
    )

    passed_view_restrictions_session_key = 'passed_collection_view_restrictions'

    class Meta:
        verbose_name = _('collection view restriction')
        verbose_name_plural = _('collection view restrictions')


class Collection(MP_Node):
    """
    A location in which resources such as images and documents can be grouped
    """
    name = models.CharField(max_length=255, verbose_name=_('name'))

    objects = CollectionManager()

    def __str__(self):
        return self.name

    def get_ancestors(self, inclusive=False):
        return Collection.objects.ancestor_of(self, inclusive)

    def get_descendants(self, inclusive=False):
        return Collection.objects.descendant_of(self, inclusive)

    def get_siblings(self, inclusive=True):
        return Collection.objects.sibling_of(self, inclusive)

    def get_next_siblings(self, inclusive=False):
        return self.get_siblings(inclusive).filter(path__gte=self.path).order_by('path')

    def get_prev_siblings(self, inclusive=False):
        return self.get_siblings(inclusive).filter(path__lte=self.path).order_by('-path')

    def get_view_restrictions(self):
        """Return a query set of all collection view restrictions that apply to this collection"""
        return CollectionViewRestriction.objects.filter(collection__in=self.get_ancestors(inclusive=True))

    @staticmethod
    def order_for_display(queryset):
        return queryset.annotate(
            display_order=Case(
                When(depth=1, then=Value('')),
                default='name')
        ).order_by('display_order')

    class Meta:
        verbose_name = _('collection')
        verbose_name_plural = _('collections')


def get_root_collection_id():
    return Collection.get_first_root_node().id


class CollectionMember(models.Model):
    """
    Base class for models that are categorised into collections
    """
    collection = models.ForeignKey(
        Collection,
        default=get_root_collection_id,
        verbose_name=_('collection'),
        related_name='+',
        on_delete=models.CASCADE
    )

    search_fields = [
        index.FilterField('collection'),
    ]

    class Meta:
        abstract = True


class GroupCollectionPermission(models.Model):
    """
    A rule indicating that a group has permission for some action (e.g. "create document")
    within a specified collection.
    """
    group = models.ForeignKey(
        Group,
        verbose_name=_('group'),
        related_name='collection_permissions',
        on_delete=models.CASCADE
    )
    collection = models.ForeignKey(
        Collection,
        verbose_name=_('collection'),
        related_name='group_permissions',
        on_delete=models.CASCADE
    )
    permission = models.ForeignKey(
        Permission,
        verbose_name=_('permission'),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "Group %d ('%s') has permission '%s' on collection %d ('%s')" % (
            self.group.id, self.group,
            self.permission,
            self.collection.id, self.collection
        )

    class Meta:
        unique_together = ('group', 'collection', 'permission')
        verbose_name = _('group collection permission')
        verbose_name_plural = _('group collection permissions')
```


