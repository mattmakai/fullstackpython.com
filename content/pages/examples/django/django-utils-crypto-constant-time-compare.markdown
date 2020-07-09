title: django.utils.crypto constant_time_compare Example Code
category: page
slug: django-utils-crypto-constant-time-compare-examples
sortorder: 500011429
toc: False
sidebartitle: django.utils.crypto constant_time_compare
meta: Python example code for the constant_time_compare callable from the django.utils.crypto module of the Django project.


constant_time_compare is a callable within the django.utils.crypto module of the Django project.


## Example 1 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / core / forms.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/core/forms.py)

```python
# forms.py
from django import forms
~~from django.utils.crypto import constant_time_compare
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy


class PasswordViewRestrictionForm(forms.Form):
    password = forms.CharField(label=gettext_lazy("Password"), widget=forms.PasswordInput)
    return_url = forms.CharField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        self.restriction = kwargs.pop('instance')
        super().__init__(*args, **kwargs)

    def clean_password(self):
        data = self.cleaned_data['password']
~~        if not constant_time_compare(data, self.restriction.password):
            raise forms.ValidationError(_("The password you have entered is not correct. Please try again."))

        return data



## ... source file continues with no further constant_time_compare examples...

```

