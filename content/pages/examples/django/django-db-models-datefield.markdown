title: django.db.models DateField Example Code
category: page
slug: django-db-models-datefield-examples
sortorder: 500012820
toc: False
sidebartitle: django.db.models DateField
meta: Python code examples for the DateField class used in the Django ORM, found within the django.db.models module of the Django project. 


[DateField](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
is a [Django ORM](/django-orm.html) mapping from your Python code to an
date-type column in your [relational database](/databases.html).

The [Django](/django.html) project has documentation for
[DateField](https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.DateField)
as well as all of the other column fields that are supported by the 
framework.

Note that `DateField` is defined within the 
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
~~from django.db import models
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
    integer = models.IntegerField(blank=True, null=True)
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
~~    date = models.DateField()
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
~~from django.db import models
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
~~    birthday = models.DateField(verbose_name=_("Birthday"), null=True)
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


## Example 3 from django-floppyforms
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
~~from django.db import models as db_models
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
~~    db_models.DateField: {'form_class': fields.DateField},
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


## Example 4 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / search / models.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/search/models.py)

```python
import datetime

from django.conf import settings
~~from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from wagtail.search.utils import MAX_QUERY_STRING_LENGTH, normalise_query_string


class Query(models.Model):
    query_string = models.CharField(max_length=MAX_QUERY_STRING_LENGTH, unique=True)

    def save(self, *args, **kwargs):
        # Normalise query string
        self.query_string = normalise_query_string(self.query_string)

        super().save(*args, **kwargs)

    def add_hit(self, date=None):
        if date is None:
            date = timezone.now().date()
        daily_hits, created = QueryDailyHits.objects.get_or_create(query=self, date=date)
        daily_hits.hits = models.F('hits') + 1
        daily_hits.save()

    def __str__(self):
        return self.query_string

    @property
    def hits(self):
        hits = self.daily_hits.aggregate(models.Sum('hits'))['hits__sum']
        return hits if hits else 0

    @classmethod
    def garbage_collect(cls):
        """
        Deletes all Query records that have no daily hits or editors picks
        """
        extra_filter_kwargs = {'editors_picks__isnull': True, } if hasattr(cls, 'editors_picks') \
            else {}
        cls.objects.filter(daily_hits__isnull=True, **extra_filter_kwargs).delete()

    @classmethod
    def get(cls, query_string):
        return cls.objects.get_or_create(query_string=normalise_query_string(query_string))[0]

    @classmethod
    def get_most_popular(cls, date_since=None):
        # TODO: Implement date_since
        return (cls.objects.filter(daily_hits__isnull=False)
                .annotate(_hits=models.Sum('daily_hits__hits'))
                .distinct().order_by('-_hits'))


class QueryDailyHits(models.Model):
    query = models.ForeignKey(Query, db_index=True, 
                              related_name='daily_hits', 
                              on_delete=models.CASCADE)
~~    date = models.DateField()
    hits = models.IntegerField(default=0)

    @classmethod
    def garbage_collect(cls, days=None):
        """
        Deletes all QueryDailyHits records that are older than a set number of days
        """
        days = getattr(settings, 'WAGTAILSEARCH_HITS_MAX_AGE', 7) if days is None else days
        min_date = timezone.now().date() - datetime.timedelta(days)

        cls.objects.filter(date__lt=min_date).delete()

    class Meta:
        unique_together = (
            ('query', 'date'),
        )
        verbose_name = _('Query Daily Hits')
        verbose_name_plural = _('Query Daily Hits')
```


