title: django.utils.translation pgettext_lazy Example Code
category: page
slug: django-utils-translation-pgettext-lazy-examples
sortorder: 500011508
toc: False
sidebartitle: django.utils.translation pgettext_lazy
meta: Python example code for the pgettext_lazy callable from the django.utils.translation module of the Django project.


pgettext_lazy is a callable within the django.utils.translation module of the Django project.


## Example 1 from django-wiki
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
from django.core import validators
from django.core.validators import RegexValidator
from django.forms.widgets import HiddenInput
from django.shortcuts import get_object_or_404
from django.urls import Resolver404, resolve
from django.utils import timezone
from django.utils.safestring import mark_safe
~~from django.utils.translation import gettext, gettext_lazy as _, pgettext_lazy
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


## ... source file abbreviated to get to pgettext_lazy examples ...


    slug = WikiSlugField(max_length=models.URLPath.SLUG_MAX_LENGTH)
    redirect = forms.BooleanField(
        label=_("Redirect pages"),
        help_text=_("Create a redirect page for every moved article?"),
        required=False,
    )

    def clean(self):
        cd = super().clean()
        if cd.get("slug"):
            dest_path = get_object_or_404(
                models.URLPath, pk=self.cleaned_data["destination"]
            )
            cd["slug"] = _clean_slug(cd["slug"], dest_path)
        return cd


class EditForm(forms.Form, SpamProtectionMixin):

    title = forms.CharField(label=_("Title"),)
    content = forms.CharField(
        label=_("Contents"), required=False, widget=getEditor().get_widget()
    )  # @UndefinedVariable

    summary = forms.CharField(
~~        label=pgettext_lazy("Revision comment", "Summary"),
        help_text=_(
            "Give a short reason for your edit, which will be stated in the revision log."
        ),
        required=False,
    )

    current_revision = forms.IntegerField(required=False, widget=forms.HiddenInput())

    def __init__(self, request, current_revision, *args, **kwargs):

        self.request = request
        self.no_clean = kwargs.pop("no_clean", False)
        self.preview = kwargs.pop("preview", False)
        self.initial_revision = current_revision
        self.presumed_revision = None
        if current_revision:
            provided_content = True
            content = kwargs.pop("content", None)
            if content is None:
                provided_content = False
                content = current_revision.content
            initial = {
                "content": content,
                "title": current_revision.title,


## ... source file abbreviated to get to pgettext_lazy examples ...


    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["prepend"] = mark_safe(self.prepend)
        return context


class CreateForm(forms.Form, SpamProtectionMixin):
    def __init__(self, request, urlpath_parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.urlpath_parent = urlpath_parent

    title = forms.CharField(label=_("Title"),)
    slug = WikiSlugField(
        label=_("Slug"),
        help_text=_(
            "This will be the address where your article can be found. Use only alphanumeric characters and - or _.<br>Note: If you change the slug later on, links pointing to this article are <b>not</b> updated."
        ),
        max_length=models.URLPath.SLUG_MAX_LENGTH,
    )
    content = forms.CharField(
        label=_("Contents"), required=False, widget=getEditor().get_widget()
    )  # @UndefinedVariable

    summary = forms.CharField(
~~        label=pgettext_lazy("Revision comment", "Summary"),
        help_text=_("Write a brief message for the article's history log."),
        required=False,
    )

    def clean_slug(self):
        return _clean_slug(self.cleaned_data["slug"], self.urlpath_parent)

    def clean(self):
        self.check_spam()
        return self.cleaned_data


class DeleteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.article = kwargs.pop("article")
        self.has_children = kwargs.pop("has_children")
        super().__init__(*args, **kwargs)

    confirm = forms.BooleanField(required=False, label=_("Yes, I am sure"))
    purge = forms.BooleanField(
        widget=HiddenInput(),
        required=False,
        label=_("Purge"),
        help_text=_(


## ... source file continues with no further pgettext_lazy examples...

```

