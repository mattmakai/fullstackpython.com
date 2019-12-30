title: django.core.management.base BaseCommand Example Code
category: page
slug: django-core-management-base-basecommand-examples
sortorder: 500012545
toc: False
sidebartitle: django.core.management.base BaseCommand
meta: Python code examples for Django management commands.


[BaseCommand](https://github.com/django/django/blob/master/django/core/management/base.py)
is a [Django](/django.html) object for creating new Django admin commands
that can be invoked with the `manage.py` script. The Django project team
as usual provides 
[fantastic documentation](https://docs.djangoproject.com/en/dev/howto/custom-management-commands/)
for creating your own commands. There are also some well-written community
tutorials on the subject such as
[How to Create Custom Django Management Commands](https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html)
by Vitor Freitas.


## Example 1 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and 
images in Django's admin interface. The project also installs a few
Django `manage.py` commands to make it easier to work with the files
and images that you upload. The project's code is available under the 
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / management / commands / generate_thumbnails.py**](https://github.com/divio/django-filer/blob/develop/filer/management/commands/generate_thumbnails.py)

```python
# -*- coding: utf-8 -*-
~~from django.core.management.base import BaseCommand

from filer.models.imagemodels import Image


~~class Command(BaseCommand):

~~    def handle(self, *args, **options):
        """
        Generates image thumbnails
        NOTE: To keep memory consumption stable avoid iteration 
        over the Image queryset
        """
        pks = Image.objects.all().values_list('id', flat=True)
        total = len(pks)
        for idx, pk in enumerate(pks):
            image = None
            try:
                image = Image.objects.get(pk=pk)
                self.stdout.write(u'Processing image {0} / {1} {2}'.\
                    format(idx + 1, total, image))
                self.stdout.flush()
                image.thumbnails
                image.icons
            except IOError as e:
                self.stderr.write('Failed to generate thumbnails: {0}'\
                    .format(str(e)))
                self.stderr.flush()
            finally:
                del image
```


