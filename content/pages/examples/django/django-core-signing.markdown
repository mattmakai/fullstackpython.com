title: django.core signing code examples
category: page
slug: django-core-signing-examples
sortorder: 500011085
toc: False
sidebartitle: django.core signing
meta: Python example code for the signing function from the django.core module of the Django project.


signing is a function within the django.core module of the Django project.


## Example 1 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / account / models.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/account/models.py)

```python
# models.py
from __future__ import unicode_literals

import datetime

~~from django.core import signing
from django.db import models, transaction
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _

from .. import app_settings as allauth_app_settings
from . import app_settings, signals
from .adapter import get_adapter
from .managers import EmailAddressManager, EmailConfirmationManager
from .utils import user_email


class EmailAddress(models.Model):

    user = models.ForeignKey(allauth_app_settings.USER_MODEL,
                             verbose_name=_('user'),
                             on_delete=models.CASCADE)
    email = models.EmailField(unique=app_settings.UNIQUE_EMAIL,
                              max_length=app_settings.EMAIL_MAX_LENGTH,
                              verbose_name=_('e-mail address'))
    verified = models.BooleanField(verbose_name=_('verified'), default=False)
    primary = models.BooleanField(verbose_name=_('primary'), default=False)

    objects = EmailAddressManager()


## ... source file abbreviated to get to signing examples ...


                                         email_address=email_address)
            return email_address

    def send(self, request=None, signup=False):
        get_adapter(request).send_confirmation_mail(request, self, signup)
        self.sent = timezone.now()
        self.save()
        signals.email_confirmation_sent.send(sender=self.__class__,
                                             request=request,
                                             confirmation=self,
                                             signup=signup)


class EmailConfirmationHMAC:

    def __init__(self, email_address):
        self.email_address = email_address

    @property
    def key(self):
~~        return signing.dumps(
            obj=self.email_address.pk,
            salt=app_settings.SALT)

    @classmethod
    def from_key(cls, key):
        try:
            max_age = (
                60 * 60 * 24 * app_settings.EMAIL_CONFIRMATION_EXPIRE_DAYS)
~~            pk = signing.loads(
                key,
                max_age=max_age,
                salt=app_settings.SALT)
            ret = EmailConfirmationHMAC(EmailAddress.objects.get(pk=pk))
        except (signing.SignatureExpired,
~~                signing.BadSignature,
                EmailAddress.DoesNotExist):
            ret = None
        return ret

    def confirm(self, request):
        if not self.email_address.verified:
            email_address = self.email_address
            get_adapter(request).confirm_email(request, email_address)
            signals.email_confirmed.send(sender=self.__class__,
                                         request=request,
                                         email_address=email_address)
            return email_address

    def send(self, request=None, signup=False):
        get_adapter(request).send_confirmation_mail(request, self, signup)
        signals.email_confirmation_sent.send(sender=self.__class__,
                                             request=request,
                                             confirmation=self,
                                             signup=signup)



## ... source file continues with no further signing examples...

```


## Example 2 from django-angular
[django-angular](https://github.com/jrief/django-angular)
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / forms / fields.py**](https://github.com/jrief/django-angular/blob/master/djng/forms/fields.py)

```python
# fields.py
import re
import mimetypes

from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
~~from django.core import signing
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


## ... source file abbreviated to get to signing examples ...


    pass


class TypedMultipleChoiceField(MultipleFieldMixin, fields.TypedMultipleChoiceField):
    pass


class UUIDField(DefaultFieldMixin, fields.UUIDField):
    def get_potential_errors(self):
        errors = self.get_input_required_errors()
        errors.extend(self.get_min_max_length_errors())
        return errors


class FileFieldMixin(DefaultFieldMixin):
    def to_python(self, value):
        try:
            current_file = None
            if ':' in value['current_file']:
                current_file = self.signer.unsign(value['current_file'])
~~        except signing.BadSignature:
            raise ValidationError("Got bogus upstream data")
        except (KeyError, TypeError):
            pass

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
~~        except signing.BadSignature:
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
~~    signer = signing.Signer()

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
~~    signer = signing.Signer()

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


## ... source file continues with no further signing examples...

```

