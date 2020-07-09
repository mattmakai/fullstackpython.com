title: django.utils.translation gettext Example Code
category: page
slug: django-utils-translation-gettext-examples
sortorder: 500011503
toc: False
sidebartitle: django.utils.translation gettext
meta: Python example code for the gettext callable from the django.utils.translation module of the Django project.


gettext is a callable within the django.utils.translation module of the Django project.


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
from django.core import exceptions, validators
from django.urls import reverse
~~from django.utils.translation import gettext, gettext_lazy as _, pgettext

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


## ... source file abbreviated to get to gettext examples ...


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
~~            self.fields['email'].label = gettext("E-mail")
            self.fields['email'].required = True
        else:
~~            self.fields['email'].label = gettext("E-mail (optional)")
            self.fields['email'].required = False
            self.fields['email'].widget.is_required = False
            if self.username_required:
                default_field_order = [
                    'username',
                    'email',
                    'email2',  # ignored when not present
                    'password1',
                    'password2'  # ignored when not present
                ]

        if not self.username_required:
            del self.fields["username"]

        set_form_field_order(
            self,
            getattr(self, 'field_order', None) or default_field_order)

    def clean_username(self):
        value = self.cleaned_data["username"]
        value = get_adapter().clean_username(value)
        return value

    def clean_email(self):


## ... source file continues with no further gettext examples...

```


## Example 2 from django-guardian
[django-guardian](https://github.com/django-guardian/django-guardian)
([project documentation](https://django-guardian.readthedocs.io/en/stable/)
and
[PyPI page](https://pypi.org/project/django-guardian/))
provides per-object permissions in [Django](/django.html) projects
by enhancing the existing authentication backend. The project's code
is open source under the
[MIT license](https://github.com/django-guardian/django-guardian/blob/devel/LICENSE).

[**django-guardian / guardian / admin.py**](https://github.com/django-guardian/django-guardian/blob/devel/guardian/./admin.py)

```python
# admin.py
from collections import OrderedDict

from django import forms
from django.conf import settings
from django.contrib import admin, messages
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, path
~~from django.utils.translation import gettext_lazy as _
~~from django.utils.translation import gettext
from guardian.forms import GroupObjectPermissionsForm, UserObjectPermissionsForm
from django.contrib.auth.models import Group
from guardian.shortcuts import (get_group_perms, get_groups_with_perms, get_perms_for_model, get_user_perms,
                                get_users_with_perms)


class AdminUserObjectPermissionsForm(UserObjectPermissionsForm):

    def get_obj_perms_field_widget(self):
        return FilteredSelectMultiple(_("Permissions"), False)


class AdminGroupObjectPermissionsForm(GroupObjectPermissionsForm):

    def get_obj_perms_field_widget(self):
        return FilteredSelectMultiple(_("Permissions"), False)


class GuardedModelAdminMixin:
    change_form_template = \
        'admin/guardian/model/change_form.html'
    obj_perms_manage_template = \
        'admin/guardian/model/obj_perms_manage.html'
    obj_perms_manage_user_template = \


## ... source file abbreviated to get to gettext examples ...


        context['groups_perms'] = groups_perms
        context['user_form'] = user_form
        context['group_form'] = group_form

        request.current_app = self.admin_site.name

        return render(request, self.get_obj_perms_manage_template(), context)

    def get_obj_perms_manage_template(self):
        if 'grappelli' in settings.INSTALLED_APPS:
            return 'admin/guardian/contrib/grappelli/obj_perms_manage.html'
        return self.obj_perms_manage_template

    def obj_perms_manage_user_view(self, request, object_pk, user_id):
        if not self.has_change_permission(request, None):
            post_url = reverse('admin:index', current_app=self.admin_site.name)
            return redirect(post_url)

        user = get_object_or_404(get_user_model(), pk=user_id)
        obj = get_object_or_404(self.get_queryset(request), pk=object_pk)
        form_class = self.get_obj_perms_manage_user_form(request)
        form = form_class(user, obj, request.POST or None)

        if request.method == 'POST' and form.is_valid():
            form.save_obj_perms()
~~            msg = gettext("Permissions saved.")
            messages.success(request, msg)
            info = (
                self.admin_site.name,
                self.model._meta.app_label,
                self.model._meta.model_name,
            )
            url = reverse(
                '%s:%s_%s_permissions_manage_user' % info,
                args=[obj.pk, user.pk]
            )
            return redirect(url)

        context = self.get_obj_perms_base_context(request, obj)
        context['user_obj'] = user
        context['user_perms'] = get_user_perms(user, obj)
        context['form'] = form

        request.current_app = self.admin_site.name

        return render(request, self.get_obj_perms_manage_user_template(), context)

    def get_obj_perms_manage_user_template(self):
        if 'grappelli' in settings.INSTALLED_APPS:
            return 'admin/guardian/contrib/grappelli/obj_perms_manage_user.html'
        return self.obj_perms_manage_user_template

    def get_obj_perms_user_select_form(self, request):
        return UserManage

    def get_obj_perms_group_select_form(self, request):
        return GroupManage

    def get_obj_perms_manage_user_form(self, request):
        return AdminUserObjectPermissionsForm

    def obj_perms_manage_group_view(self, request, object_pk, group_id):
        if not self.has_change_permission(request, None):
            post_url = reverse('admin:index', current_app=self.admin_site.name)
            return redirect(post_url)

        group = get_object_or_404(Group, id=group_id)
        obj = get_object_or_404(self.get_queryset(request), pk=object_pk)
        form_class = self.get_obj_perms_manage_group_form(request)
        form = form_class(group, obj, request.POST or None)

        if request.method == 'POST' and form.is_valid():
            form.save_obj_perms()
~~            msg = gettext("Permissions saved.")
            messages.success(request, msg)
            info = (
                self.admin_site.name,
                self.model._meta.app_label,
                self.model._meta.model_name,
            )
            url = reverse(
                '%s:%s_%s_permissions_manage_group' % info,
                args=[obj.pk, group.id]
            )
            return redirect(url)

        context = self.get_obj_perms_base_context(request, obj)
        context['group_obj'] = group
        context['group_perms'] = get_group_perms(group, obj)
        context['form'] = form

        request.current_app = self.admin_site.name

        return render(request, self.get_obj_perms_manage_group_template(), context)

    def get_obj_perms_manage_group_template(self):
        if 'grappelli' in settings.INSTALLED_APPS:
            return 'admin/guardian/contrib/grappelli/obj_perms_manage_group.html'


## ... source file continues with no further gettext examples...

```


## Example 3 from django-taggit
[django-taggit](https://github.com/jazzband/django-taggit/)
([PyPI page](https://pypi.org/project/django-taggit/)) provides a way
to create, store, manage and use tags in a [Django](/django.html) project.
The code for django-taggit is
[open source](https://github.com/jazzband/django-taggit/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-taggit / taggit / models.py**](https://github.com/jazzband/django-taggit/blob/master/taggit/./models.py)

```python
# models.py
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import IntegrityError, models, router, transaction
from django.utils.text import slugify
~~from django.utils.translation import gettext, gettext_lazy as _

try:
    from unidecode import unidecode
except ImportError:

    def unidecode(tag):
        return tag


class TagBase(models.Model):
    name = models.CharField(verbose_name=_("name"), unique=True, max_length=100)
    slug = models.SlugField(verbose_name=_("slug"), unique=True, max_length=100)

    def __str__(self):
        return self.name

    def __gt__(self, other):
        return self.name.lower() > other.name.lower()

    def __lt__(self, other):
        return self.name.lower() < other.name.lower()

    class Meta:
        abstract = True


## ... source file abbreviated to get to gettext examples ...


            while True:
                slug = self.slugify(self.name, i)
                if slug not in slugs:
                    self.slug = slug
                    return super().save(*args, **kwargs)
                i += 1
        else:
            return super().save(*args, **kwargs)

    def slugify(self, tag, i=None):
        slug = slugify(unidecode(tag))
        if i is not None:
            slug += "_%d" % i
        return slug


class Tag(TagBase):
    class Meta:
        verbose_name = _("tag")
        verbose_name_plural = _("tags")
        app_label = "taggit"


class ItemBase(models.Model):
    def __str__(self):
~~        return gettext("%(object)s tagged with %(tag)s") % {
            "object": self.content_object,
            "tag": self.tag,
        }

    class Meta:
        abstract = True

    @classmethod
    def tag_model(cls):
        field = cls._meta.get_field("tag")
        return field.remote_field.model

    @classmethod
    def tag_relname(cls):
        field = cls._meta.get_field("tag")
        return field.remote_field.related_name

    @classmethod
    def lookup_kwargs(cls, instance):
        return {"content_object": instance}

    @classmethod
    def tags_for(cls, model, instance=None, **extra_filters):
        kwargs = extra_filters or {}


## ... source file continues with no further gettext examples...

```


## Example 4 from django-wiki
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
            self.default_validators = [
                validators.validate_unicode_slug,
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
~~                gettext('A deleted article with slug "%s" already exists.')
                % already_urlpath.slug
            )
        else:
            raise forms.ValidationError(
~~                gettext('A slug named "%s" already exists.') % already_urlpath.slug
            )

    if settings.CHECK_SLUG_URL_AVAILABLE:
        try:
            match = resolve(urlpath.path + "/" + slug + "/")
            if match.app_name != "wiki":
                raise forms.ValidationError(
~~                    gettext("This slug conflicts with an existing URL.")
                )
        except Resolver404:
            pass

    return slug


User = get_user_model()
Group = apps.get_model(settings.GROUP_MODEL)


class SpamProtectionMixin:


    revision_model = models.ArticleRevision

    def check_spam(self):  # noqa
        request = self.request
        user = None
        ip_address = None
        if request.user.is_authenticated:
            user = request.user
        else:
            ip_address = request.META.get("REMOTE_ADDR", None)

        if not (user or ip_address):
            raise forms.ValidationError(
~~                gettext(
                    "Spam protection failed to find both a logged in user and an IP address."
                )
            )

        def check_interval(from_time, max_count, interval_name):
            from_time = timezone.now() - timedelta(
                minutes=settings.REVISIONS_MINUTES_LOOKBACK
            )
            revisions = self.revision_model.objects.filter(created__gte=from_time,)
            if user:
                revisions = revisions.filter(user=user)
            if ip_address:
                revisions = revisions.filter(ip_address=ip_address)
            revisions = revisions.count()
            if revisions >= max_count:
                raise forms.ValidationError(
~~                    gettext(
                        "Spam protection: You are only allowed to create or edit %(revisions)d article(s) per %(interval_name)s."
                    )
                    % {"revisions": max_count, "interval_name": interval_name}
                )

        if not settings.LOG_IPS_ANONYMOUS:
            return
        if request.user.has_perm("wiki.moderator"):
            return

        from_time = timezone.now() - timedelta(
            minutes=settings.REVISIONS_MINUTES_LOOKBACK
        )
        if request.user.is_authenticated:
            per_minute = settings.REVISIONS_PER_MINUTES
        else:
            per_minute = settings.REVISIONS_PER_MINUTES_ANONYMOUS
        check_interval(
            from_time,
            per_minute,
            _("minute")
            if settings.REVISIONS_MINUTES_LOOKBACK == 1
            else (_("%d minutes") % settings.REVISIONS_MINUTES_LOOKBACK),
        )


## ... source file abbreviated to get to gettext examples ...


                if not str(self.presumed_revision) == str(self.initial_revision.id):
                    newdata = {}
                    for k, v in data.items():
                        newdata[k] = v
                    newdata["current_revision"] = self.initial_revision.id
                    if provided_content:
                        self.presumed_revision = self.initial_revision.id
                    else:
                        newdata["content"] = simple_merge(
                            content, data.get("content", "")
                        )
                    newdata["title"] = current_revision.title
                    kwargs["data"] = newdata
                else:
                    kwargs["data"] = data

            kwargs["initial"] = initial

        super().__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data.get("title", None)
        title = (title or "").strip()
        if not title:
            raise forms.ValidationError(
~~                gettext("Article is missing title or has an invalid title")
            )
        return title

    def clean(self):
        if self.no_clean or self.preview:
            return self.cleaned_data
        if not str(self.initial_revision.id) == str(self.presumed_revision):
            raise forms.ValidationError(
~~                gettext(
                    "While you were editing, someone else changed the revision. Your contents have been automatically merged with the new contents. Please review the text below."
                )
            )
        if (
            "title" in self.cleaned_data
            and self.cleaned_data["title"] == self.initial_revision.title
            and self.cleaned_data["content"] == self.initial_revision.content
        ):
            raise forms.ValidationError(gettext("No changes made. Nothing to save."))
        self.check_spam()
        return self.cleaned_data


class SelectWidgetBootstrap(forms.Select):

    def __init__(self, attrs=None, choices=()):
        if attrs is None:
            attrs = {"class": ""}
        elif "class" not in attrs:
            attrs["class"] = ""
        attrs["class"] += " form-control"

        super().__init__(attrs, choices)



## ... source file abbreviated to get to gettext examples ...



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
            "Purge the article: Completely remove it (and all its contents) with no undo. Purging is a good idea if you want to free the slug such that users can create new articles in its place."
        ),
    )
    revision = forms.ModelChoiceField(
        models.ArticleRevision.objects.all(), widget=HiddenInput(), required=False
    )

    def clean(self):
        if not self.cleaned_data["confirm"]:
            raise forms.ValidationError(gettext("You are not sure enough!"))
        if self.cleaned_data["revision"] != self.article.current_revision:
            raise forms.ValidationError(
~~                gettext(
                    "While you tried to delete this article, it was modified. TAKE CARE!"
                )
            )
        return self.cleaned_data


class PermissionsForm(PluginSettingsFormMixin, forms.ModelForm):

    locked = forms.BooleanField(
        label=_("Lock article"),
        help_text=_("Deny all users access to edit this article."),
        required=False,
    )

    settings_form_headline = _("Permissions")
    settings_order = 5
    settings_write_access = False

    owner_username = forms.CharField(
        required=False,
        label=_("Owner"),
        help_text=_("Enter the username of the owner."),
    )
    group = forms.ModelChoiceField(


## ... source file continues with no further gettext examples...

```


## Example 5 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / images / wagtail_hooks.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/images/wagtail_hooks.py)

```python
# wagtail_hooks.py
from django.conf.urls import include, url
from django.urls import reverse
from django.utils.html import format_html
~~from django.utils.translation import gettext_lazy as _
~~from django.utils.translation import gettext, ngettext

import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.menu import MenuItem
from wagtail.admin.navigation import get_site_for_user
from wagtail.admin.rich_text import HalloPlugin
from wagtail.admin.search import SearchArea
from wagtail.admin.site_summary import SummaryItem
from wagtail.core import hooks
from wagtail.images import admin_urls, get_image_model, image_operations
from wagtail.images.api.admin.views import ImagesAdminAPIViewSet
from wagtail.images.forms import GroupImagePermissionFormSet
from wagtail.images.permissions import permission_policy
from wagtail.images.rich_text import ImageEmbedHandler
from wagtail.images.rich_text.contentstate import ContentstateImageConversionRule
from wagtail.images.rich_text.editor_html import EditorHTMLImageConversionRule


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        url(r'^images/', include(admin_urls, namespace='wagtailimages')),
    ]




## ... source file abbreviated to get to gettext examples ...


        reverse('wagtailimages:chooser')
    )


@hooks.register('register_rich_text_features')
def register_image_feature(features):
    features.register_embed_type(ImageEmbedHandler)

    features.register_editor_plugin(
        'hallo', 'image',
        HalloPlugin(
            name='hallowagtailimage',
            js=[
                'wagtailimages/js/image-chooser-modal.js',
                'wagtailimages/js/hallo-plugins/hallo-wagtailimage.js',
            ],
        )
    )

    features.register_converter_rule('editorhtml', 'image', EditorHTMLImageConversionRule)

    features.register_editor_plugin(
        'draftail', 'image', draftail_features.EntityFeature({
            'type': 'IMAGE',
            'icon': 'image',
~~            'description': gettext('Image'),
            'attributes': ['id', 'src', 'alt', 'format'],
            'whitelist': {
                'id': True,
            }
        }, js=[
            'wagtailimages/js/image-chooser-modal.js',
        ])
    )

    features.register_converter_rule('contentstate', 'image', ContentstateImageConversionRule)

    features.default_features.append('image')


@hooks.register('register_image_operations')
def register_image_operations():
    return [
        ('original', image_operations.DoNothingOperation),
        ('fill', image_operations.FillOperation),
        ('min', image_operations.MinMaxOperation),
        ('max', image_operations.MinMaxOperation),
        ('width', image_operations.WidthHeightOperation),
        ('height', image_operations.WidthHeightOperation),
        ('scale', image_operations.ScaleOperation),


## ... source file continues with no further gettext examples...

```

