title: django.urls reverse Example Code
category: page
slug: django-urls-reverse-examples
sortorder: 500011411
toc: False
sidebartitle: django.urls reverse
meta: Python example code for the reverse callable from the django.urls module of the Django project.


reverse is a callable within the django.urls module of the Django project.


## Example 1 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / chair / forms.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/chair/forms.py)

```python
# forms.py
from functools import reduce

from django import forms
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q, F, Count, Max, Subquery, OuterRef, Value
from django.db.models.functions import Concat
from django.forms import MultipleChoiceField, ChoiceField, Form
~~from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from django_countries import countries

from conferences.models import Conference, ArtifactDescriptor
from gears.widgets import CustomCheckboxSelectMultiple, CustomFileInput
from review.models import Reviewer, Review, ReviewStats
from review.utilities import get_average_score
from submissions.models import Submission, Attachment
from users.models import Profile

User = get_user_model()


def clean_data_to_int(iterable, empty=None):
    return [int(x) if x != '' else None for x in iterable]


def q_or(disjuncts, default=True):
    if disjuncts:
        return reduce(lambda acc, d: acc | d, disjuncts)
    return Q(pk__isnull=(not default))  # otherwise, check whether PK is null




## ... source file abbreviated to get to reverse examples ...


                record[self.ORDER_COLUMN] = order

            if self.ID_COLUMN in columns:
                record[self.ID_COLUMN] = sub.pk

            if self.TITLE_COLUMN in columns:
                record[self.TITLE_COLUMN] = sub.title

            if self.AUTHORS_COLUMN in columns:
                names = [get_user_name(profiles[a.user_id]) for a in authors]
                record[self.AUTHORS_COLUMN] = '; '.join(names)

            if self.COUNTRY_COLUMN in columns:
                countries_list = [
                    profiles[a.user_id].get_country_display() for a in authors]
                countries_list = list(set(countries_list))  # remove duplicates
                countries_list.sort()
                record[self.COUNTRY_COLUMN] = '; '.join(countries_list)

            if self.STYPE_COLUMN in columns:
                record[self.STYPE_COLUMN] = (
                    sub.stype.get_language_display() if sub.stype else '')

            if self.REVIEW_PAPER_COLUMN in columns:
                record[self.REVIEW_PAPER_COLUMN] = request.build_absolute_uri(
~~                    reverse('submissions:download-manuscript', args=[sub.pk]))

            if self.REVIEW_SCORE_COLUMN in columns:
                score = get_average_score(sub)
                score_string = f'{score:.1f}' if score else '-'
                record[self.REVIEW_SCORE_COLUMN] = score_string

            if self.STATUS_COLUMN in columns:
                record[self.STATUS_COLUMN] = sub.get_status_display()

            if self.TOPICS_COLUMN in columns:
                record[self.TOPICS_COLUMN] = '; '.join(sub.topics.values_list(
                    'name', flat=True))


            result.append(record)
        return result



## ... source file continues with no further reverse examples...

```


## Example 2 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / socialaccount / adapter.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/socialaccount/adapter.py)

```python
# adapter.py
from __future__ import absolute_import

from django.core.exceptions import ValidationError
~~from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from ..account import app_settings as account_settings
from ..account.adapter import get_adapter as get_account_adapter
from ..account.app_settings import EmailVerificationMethod
from ..account.models import EmailAddress
from ..account.utils import user_email, user_field, user_username
from ..utils import (
    deserialize_instance,
    email_address_exists,
    import_attribute,
    serialize_instance,
    valid_email_or_none,
)
from . import app_settings


class DefaultSocialAccountAdapter(object):

    error_messages = {
        'email_taken':
        _("An account already exists with this e-mail address."
          " Please sign in to that account first, then connect"
          " your %s account.")


## ... source file abbreviated to get to reverse examples ...


            get_account_adapter().save_user(request, u, form)
        else:
            get_account_adapter().populate_username(request, u)
        sociallogin.save(request)
        return u

    def populate_user(self,
                      request,
                      sociallogin,
                      data):
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        name = data.get('name')
        user = sociallogin.user
        user_username(user, username or '')
        user_email(user, valid_email_or_none(email) or '')
        name_parts = (name or '').partition(' ')
        user_field(user, 'first_name', first_name or name_parts[0])
        user_field(user, 'last_name', last_name or name_parts[2])
        return user

    def get_connect_redirect_url(self, request, socialaccount):
        assert request.user.is_authenticated
~~        url = reverse('socialaccount_connections')
        return url

    def validate_disconnect(self, account, accounts):
        if len(accounts) == 1:
            if not account.user.has_usable_password():
                raise ValidationError(_("Your account has no password set"
                                        " up."))
            if app_settings.EMAIL_VERIFICATION \
                    == EmailVerificationMethod.MANDATORY:
                if EmailAddress.objects.filter(user=account.user,
                                               verified=True).count() == 0:
                    raise ValidationError(_("Your account has no verified"
                                            " e-mail address."))

    def is_auto_signup_allowed(self, request, sociallogin):
        auto_signup = app_settings.AUTO_SIGNUP
        if auto_signup:
            email = user_email(sociallogin.user)
            if email:
                if account_settings.UNIQUE_EMAIL:
                    if email_address_exists(email):
                        auto_signup = False
            elif app_settings.EMAIL_REQUIRED:
                auto_signup = False


## ... source file continues with no further reverse examples...

```


## Example 3 from django-angular
[django-angular](https://github.com/jrief/django-angular)
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / urls.py**](https://github.com/jrief/django-angular/blob/master/djng/./urls.py)

```python
# urls.py
import warnings
~~from django.urls import reverse
from django.conf.urls import url
from django.http.response import HttpResponsePermanentRedirect


warnings.warn("Reversing URL's using urlpatterns is deprecated. Please use the middleware instead",
    DeprecationWarning)


def angular_reverse(request, *args, **kwargs):
    url_name = request.GET.get('djng_url_name')
    url_args = request.GET.getlist('djng_url_args', None)
    url_kwargs = {}

    prefix = 'djng_url_kwarg_'
    for param in request.GET:
        if param.startswith(prefix):
            url_kwargs[param[len(prefix):]] = request.GET[param]

~~    url = reverse(url_name, args=url_args, kwargs=url_kwargs)
    return HttpResponsePermanentRedirect(url)


urlpatterns = [
    url(r'^reverse/$', angular_reverse),
]



## ... source file continues with no further reverse examples...

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

[**django-axes / axes / tests / test_handlers.py**](https://github.com/jazzband/django-axes/blob/master/axes/tests/test_handlers.py)

```python
# test_handlers.py
from unittest.mock import MagicMock, patch

from django.test import override_settings
~~from django.urls import reverse
from django.utils import timezone
from django.utils.timezone import timedelta

from axes.conf import settings
from axes.handlers.proxy import AxesProxyHandler
from axes.helpers import get_client_str
from axes.models import AccessAttempt, AccessLog
from axes.tests.base import AxesTestCase


@override_settings(AXES_HANDLER="axes.handlers.base.AxesHandler")
class AxesHandlerTestCase(AxesTestCase):
    def test_base_handler_reset_attempts_raises(self):
        with self.assertRaises(NotImplementedError):
            AxesProxyHandler.reset_attempts()

    def test_base_handler_reset_logs_raises(self):
        with self.assertRaises(NotImplementedError):
            AxesProxyHandler.reset_logs()

    def test_base_handler_raises_on_undefined_is_allowed_to_authenticate(self):
        with self.assertRaises(NotImplementedError):
            AxesProxyHandler.is_allowed(self.request, {})



## ... source file abbreviated to get to reverse examples ...


    @override_settings(
        AXES_NEVER_LOCKOUT_WHITELIST=True, AXES_IP_WHITELIST=["127.0.0.1"]
    )
    def test_is_allowed_with_whitelisted_ip_address(self):
        self.assertTrue(AxesProxyHandler.is_allowed(self.request))

    @override_settings(AXES_NEVER_LOCKOUT_GET=True)
    def test_is_allowed_with_whitelisted_method(self):
        self.request.method = "GET"
        self.assertTrue(AxesProxyHandler.is_allowed(self.request))

    @override_settings(AXES_LOCK_OUT_AT_FAILURE=False)
    def test_is_allowed_no_lock_out(self):
        self.assertTrue(AxesProxyHandler.is_allowed(self.request))

    @override_settings(AXES_ONLY_ADMIN_SITE=True)
    def test_only_admin_site(self):
        request = MagicMock()
        request.path = "/test/"
        self.assertTrue(AxesProxyHandler.is_allowed(self.request))

    def test_is_admin_site(self):
        request = MagicMock()
        tests = (  # (AXES_ONLY_ADMIN_SITE, URL, Expected)
            (True, "/test/", True),
~~            (True, reverse("admin:index"), False),
            (False, "/test/", False),
~~            (False, reverse("admin:index"), False),
        )

        for setting_value, url, expected in tests:
            with override_settings(AXES_ONLY_ADMIN_SITE=setting_value):
                request.path = url
                self.assertEqual(AxesProxyHandler().is_admin_site(request), expected)

    @override_settings(ROOT_URLCONF="axes.tests.urls_empty")
    @override_settings(AXES_ONLY_ADMIN_SITE=True)
    def test_is_admin_site_no_admin_site(self):
        request = MagicMock()
        request.path = "/admin/"
        self.assertTrue(AxesProxyHandler().is_admin_site(self.request))


class AxesProxyHandlerTestCase(AxesTestCase):
    def setUp(self):
        self.sender = MagicMock()
        self.credentials = MagicMock()
        self.request = MagicMock()
        self.user = MagicMock()
        self.instance = MagicMock()

    @patch("axes.handlers.proxy.AxesProxyHandler.implementation", None)


## ... source file continues with no further reverse examples...

```


## Example 5 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / page_rendering.py**](https://github.com/divio/django-cms/blob/develop/cms/./page_rendering.py)

```python
# page_rendering.py
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template.response import TemplateResponse
~~from django.urls import Resolver404, resolve, reverse

from cms import __version__
from cms.cache.page import set_page_cache
from cms.models import Page
from cms.utils.conf import get_cms_setting
from cms.utils.page import get_page_template_from_request
from cms.utils.page_permissions import user_can_change_page, user_can_view_page


def render_page(request, page, current_language, slug):
    context = {}
    context['lang'] = current_language
    context['current_page'] = page
    context['has_change_permissions'] = user_can_change_page(request.user, page)
    context['has_view_permissions'] = user_can_view_page(request.user, page)

    if not context['has_view_permissions']:
        return _handle_no_page(request)

    template = get_page_template_from_request(request)
    response = TemplateResponse(request, template, context)
    response.add_post_render_callback(set_page_cache)

    xframe_options = page.get_xframe_options()


## ... source file abbreviated to get to reverse examples ...


    return response


def render_object_structure(request, obj):
    context = {
        'object': obj,
        'cms_toolbar': request.toolbar,
    }
    return render(request, 'cms/toolbar/structure.html', context)


def _handle_no_page(request):
    try:
        resolve('%s$' % request.path)
    except Resolver404 as e:
        exc = Http404(dict(path=request.path, tried=e.args[0]['tried']))
        raise exc
    raise Http404('CMS Page not found: %s' % request.path)


def _render_welcome_page(request):
    context = {
        'cms_version': __version__,
        'cms_edit_on': get_cms_setting('CMS_TOOLBAR_URL__EDIT_ON'),
        'django_debug': settings.DEBUG,
~~        'next_url': reverse('pages-root'),
    }
    return TemplateResponse(request, "cms/welcome.html", context)



## ... source file continues with no further reverse examples...

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

[**django-extensions / django_extensions / admin / widgets.py**](https://github.com/django-extensions/django-extensions/blob/master/django_extensions/admin/widgets.py)

```python
# widgets.py
import six
from six.moves import urllib
from django import forms
from django.contrib.admin.sites import site
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django.template.loader import render_to_string
from django.templatetags.static import static
~~from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.text import Truncator


class ForeignKeySearchInput(ForeignKeyRawIdWidget):

    widget_template = None
    search_path = None

    def _media(self):
        js_files = [
            static('django_extensions/js/jquery.bgiframe.js'),
            static('django_extensions/js/jquery.ajaxQueue.js'),
            static('django_extensions/js/jquery.autocomplete.js'),
        ]

        return forms.Media(
            css={'all': (static('django_extensions/css/jquery.autocomplete.css'), )},
            js=js_files,
        )
    media = property(_media)

    def label_for_value(self, value):
        key = self.rel.get_related_field().name
        obj = self.rel.model._default_manager.get(**{key: value})

        return Truncator(obj).words(14, truncate='...')

    def __init__(self, rel, search_fields, attrs=None):
        self.search_fields = search_fields
        super().__init__(rel, site, attrs)

    def render(self, name, value, attrs=None, renderer=None):
        if attrs is None:
            attrs = {}
        opts = self.rel.model._meta
        app_label = opts.app_label
        model_name = opts.object_name.lower()
~~        related_url = reverse('admin:%s_%s_changelist' % (app_label, model_name))
        if not self.search_path:
            self.search_path = urllib.parse.urljoin(related_url, 'foreignkey_autocomplete/')
        params = self.url_parameters()
        if params:
            url = '?' + '&amp;'.join(['%s=%s' % (k, v) for k, v in params.items()])
        else:
            url = ''

        if 'class' not in attrs:
            attrs['class'] = 'vForeignKeyRawIdAdminField'
        output = [forms.TextInput.render(self, name, value, attrs)]

        if value:
            label = self.label_for_value(value)
        else:
            label = six.u('')

        context = {
            'url': url,
            'related_url': related_url,
            'search_path': self.search_path,
            'search_fields': ','.join(self.search_fields),
            'app_label': app_label,
            'model_name': model_name,


## ... source file continues with no further reverse examples...

```


## Example 7 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / admin / fileadmin.py**](https://github.com/divio/django-filer/blob/develop/filer/admin/fileadmin.py)

```python
# fileadmin.py
from __future__ import absolute_import

from django import forms
from django.contrib.admin.utils import unquote
from django.http import HttpResponseRedirect
~~from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

from .. import settings
from ..models import File
from .permissions import PrimitivePermissionAwareModelAdmin
from .tools import AdminContext, admin_url_params_encoded, popup_status


class FileAdminChangeFrom(forms.ModelForm):
    class Meta(object):
        model = File
        exclude = ()


class FileAdmin(PrimitivePermissionAwareModelAdmin):
    list_display = ('label',)
    list_per_page = 10
    search_fields = ['name', 'original_filename', 'sha1', 'description']
    raw_id_fields = ('owner',)
    readonly_fields = ('sha1', 'display_canonical')

    form = FileAdminChangeFrom



## ... source file abbreviated to get to reverse examples ...


            (_('Advanced'), {
                'fields': (
                    'file',
                    'sha1',
                    'display_canonical',
                ) + extra_advanced_fields,
                'classes': ('collapse',),
            }),
        ) + extra_fieldsets
        if settings.FILER_ENABLE_PERMISSIONS:
            fieldsets = fieldsets + (
                (None, {
                    'fields': ('is_public',)
                }),
            )
        return fieldsets

    def response_change(self, request, obj):
        if (
            request.POST
            and '_continue' not in request.POST
            and '_saveasnew' not in request.POST
            and '_addanother' not in request.POST
        ):
            if obj.folder:
~~                url = reverse('admin:filer-directory_listing',
                              kwargs={'folder_id': obj.folder.id})
            else:
~~                url = reverse(
                    'admin:filer-directory_listing-unfiled_images')
            url = "{0}{1}".format(
                url,
                admin_url_params_encoded(request),
            )
            return HttpResponseRedirect(url)
        return super(FileAdmin, self).response_change(request, obj)

    def render_change_form(self, request, context, add=False, change=False,
                           form_url='', obj=None):
        info = self.model._meta.app_label, self.model._meta.model_name
        extra_context = {'show_delete': True,
                         'history_url': 'admin:%s_%s_history' % info,
                         'is_popup': popup_status(request),
                         'filer_admin_context': AdminContext(request)}
        context.update(extra_context)
        return super(FileAdmin, self).render_change_form(
            request=request, context=context, add=add, change=change,
            form_url=form_url, obj=obj)

    def delete_view(self, request, object_id, extra_context=None):
        try:
            obj = self.get_queryset(request).get(pk=unquote(object_id))
            parent_folder = obj.folder
        except self.model.DoesNotExist:
            parent_folder = None

        if request.POST:
            super(FileAdmin, self).delete_view(
                request=request, object_id=object_id,
                extra_context=extra_context)
            if parent_folder:
~~                url = reverse('admin:filer-directory_listing',
                              kwargs={'folder_id': parent_folder.id})
            else:
~~                url = reverse('admin:filer-directory_listing-unfiled_images')
            url = "{0}{1}".format(
                url,
                admin_url_params_encoded(request)
            )
            return HttpResponseRedirect(url)

        return super(FileAdmin, self).delete_view(
            request=request, object_id=object_id,
            extra_context=extra_context)

    def get_model_perms(self, request):
        return {
            'add': False,
            'change': False,
            'delete': False,
        }

    def display_canonical(self, instance):
        canonical = instance.canonical_url
        if canonical:
            return mark_safe('<a href="%s">%s</a>' % (canonical, canonical))
        else:
            return '-'
    display_canonical.allow_tags = True


## ... source file continues with no further reverse examples...

```


## Example 8 from django-guardian
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
~~from django.urls import reverse, path
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext
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


## ... source file abbreviated to get to reverse examples ...


                path('<object_pk>/permissions/group-manage/<group_id>/',
                     view=self.admin_site.admin_view(
                         self.obj_perms_manage_group_view),
                     name='%s_%s_permissions_manage_group' % info),
            ]
            urls = myurls + urls
        return urls

    def get_obj_perms_base_context(self, request, obj):
        context = self.admin_site.each_context(request)
        context.update({
            'adminform': {'model_admin': self},
            'media': self.media,
            'object': obj,
            'app_label': self.model._meta.app_label,
            'opts': self.model._meta,
            'original': str(obj),
            'has_change_permission': self.has_change_permission(request, obj),
            'model_perms': get_perms_for_model(obj),
            'title': _("Object permissions"),
        })
        return context

    def obj_perms_manage_view(self, request, object_pk):
        if not self.has_change_permission(request, None):
~~            post_url = reverse('admin:index', current_app=self.admin_site.name)
            return redirect(post_url)

        from django.contrib.admin.utils import unquote
        obj = get_object_or_404(self.get_queryset(
            request), pk=unquote(object_pk))
        users_perms = OrderedDict(
            sorted(
                get_users_with_perms(obj, attach_perms=True,
                                     with_group_users=False).items(),
                key=lambda user: getattr(
                    user[0], get_user_model().USERNAME_FIELD)
            )
        )

        groups_perms = OrderedDict(
            sorted(
                get_groups_with_perms(obj, attach_perms=True).items(),
                key=lambda group: group[0].name
            )
        )

        if request.method == 'POST' and 'submit_manage_user' in request.POST:
            user_form = self.get_obj_perms_user_select_form(
                request)(request.POST)
            group_form = self.get_obj_perms_group_select_form(
                request)(request.POST)
            info = (
                self.admin_site.name,
                self.model._meta.app_label,
                self.model._meta.model_name,
            )
            if user_form.is_valid():
                user_id = user_form.cleaned_data['user'].pk
~~                url = reverse(
                    '%s:%s_%s_permissions_manage_user' % info,
                    args=[obj.pk, user_id]
                )
                return redirect(url)
        elif request.method == 'POST' and 'submit_manage_group' in request.POST:
            user_form = self.get_obj_perms_user_select_form(
                request)(request.POST)
            group_form = self.get_obj_perms_group_select_form(
                request)(request.POST)
            info = (
                self.admin_site.name,
                self.model._meta.app_label,
                self.model._meta.model_name,
            )
            if group_form.is_valid():
                group_id = group_form.cleaned_data['group'].id
~~                url = reverse(
                    '%s:%s_%s_permissions_manage_group' % info,
                    args=[obj.pk, group_id]
                )
                return redirect(url)
        else:
            user_form = self.get_obj_perms_user_select_form(request)()
            group_form = self.get_obj_perms_group_select_form(request)()

        context = self.get_obj_perms_base_context(request, obj)
        context['users_perms'] = users_perms
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
~~            post_url = reverse('admin:index', current_app=self.admin_site.name)
            return redirect(post_url)

        user = get_object_or_404(get_user_model(), pk=user_id)
        obj = get_object_or_404(self.get_queryset(request), pk=object_pk)
        form_class = self.get_obj_perms_manage_user_form(request)
        form = form_class(user, obj, request.POST or None)

        if request.method == 'POST' and form.is_valid():
            form.save_obj_perms()
            msg = gettext("Permissions saved.")
            messages.success(request, msg)
            info = (
                self.admin_site.name,
                self.model._meta.app_label,
                self.model._meta.model_name,
            )
~~            url = reverse(
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
~~            post_url = reverse('admin:index', current_app=self.admin_site.name)
            return redirect(post_url)

        group = get_object_or_404(Group, id=group_id)
        obj = get_object_or_404(self.get_queryset(request), pk=object_pk)
        form_class = self.get_obj_perms_manage_group_form(request)
        form = form_class(group, obj, request.POST or None)

        if request.method == 'POST' and form.is_valid():
            form.save_obj_perms()
            msg = gettext("Permissions saved.")
            messages.success(request, msg)
            info = (
                self.admin_site.name,
                self.model._meta.app_label,
                self.model._meta.model_name,
            )
~~            url = reverse(
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
        return self.obj_perms_manage_group_template

    def get_obj_perms_manage_group_form(self, request):
        return AdminGroupObjectPermissionsForm


class GuardedModelAdmin(GuardedModelAdminMixin, admin.ModelAdmin):


## ... source file continues with no further reverse examples...

```


## Example 9 from django-import-export
[django-import-export](https://github.com/django-import-export/django-import-export)
([documentation](https://django-import-export.readthedocs.io/en/latest/)
and [PyPI page](https://pypi.org/project/django-import-export/))
is a [Django](/django.html) code library for importing and exporting data
from the Django Admin. The tool supports many export and import formats
such as CSV, JSON and YAML. django-import-export is open source under the
[BSD 2-Clause "Simplified" License](https://github.com/django-import-export/django-import-export/blob/master/LICENSE).

[**django-import-export / import_export / admin.py**](https://github.com/django-import-export/django-import-export/blob/master/import_export/./admin.py)

```python
# admin.py
from datetime import datetime

import django
from django import forms
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin, messages
from django.contrib.admin.models import ADDITION, CHANGE, DELETION, LogEntry
from django.contrib.auth import get_permission_codename
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
~~from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_str
from django.utils.module_loading import import_string
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_POST

from .formats.base_formats import DEFAULT_FORMATS
from .forms import ConfirmImportForm, ExportForm, ImportForm, export_action_form_factory
from .resources import modelresource_factory
from .results import RowResult
from .signals import post_export, post_import
from .tmp_storages import TempFolderStorage

SKIP_ADMIN_LOG = getattr(settings, 'IMPORT_EXPORT_SKIP_ADMIN_LOG', False)
TMP_STORAGE_CLASS = getattr(settings, 'IMPORT_EXPORT_TMP_STORAGE_CLASS',
                            TempFolderStorage)


if isinstance(TMP_STORAGE_CLASS, str):
    TMP_STORAGE_CLASS = import_string(TMP_STORAGE_CLASS)


class ImportExportMixinBase:
    def get_model_info(self):


## ... source file abbreviated to get to reverse examples ...



            result = self.process_dataset(dataset, confirm_form, request, *args, **kwargs)

            tmp_storage.remove()

            return self.process_result(result, request)

    def process_dataset(self, dataset, confirm_form, request, *args, **kwargs):

        res_kwargs = self.get_import_resource_kwargs(request, form=confirm_form, *args, **kwargs)
        resource = self.get_import_resource_class()(**res_kwargs)

        imp_kwargs = self.get_import_data_kwargs(request, form=confirm_form, *args, **kwargs)
        return resource.import_data(dataset,
                                    dry_run=False,
                                    raise_errors=True,
                                    file_name=confirm_form.cleaned_data['original_file_name'],
                                    user=request.user,
                                    **imp_kwargs)

    def process_result(self, result, request):
        self.generate_log_entries(result, request)
        self.add_success_message(result, request)
        post_import.send(sender=None, model=self.model)

~~        url = reverse('admin:%s_%s_changelist' % self.get_model_info(),
                      current_app=self.admin_site.name)
        return HttpResponseRedirect(url)

    def generate_log_entries(self, result, request):
        if not self.get_skip_admin_log():
            logentry_map = {
                RowResult.IMPORT_TYPE_NEW: ADDITION,
                RowResult.IMPORT_TYPE_UPDATE: CHANGE,
                RowResult.IMPORT_TYPE_DELETE: DELETION,
            }
            content_type_id = ContentType.objects.get_for_model(self.model).pk
            for row in result:
                if row.import_type != row.IMPORT_TYPE_ERROR and row.import_type != row.IMPORT_TYPE_SKIP:
                    LogEntry.objects.log_action(
                        user_id=request.user.pk,
                        content_type_id=content_type_id,
                        object_id=row.object_id,
                        object_repr=row.object_repr,
                        action_flag=logentry_map[row.import_type],
                        change_message=_("%s through import_export" % row.import_type),
                    )

    def add_success_message(self, result, request):
        opts = self.model._meta


## ... source file continues with no further reverse examples...

```


## Example 10 from django-inline-actions
[django-inline-actions](https://github.com/escaped/django-inline-actions)
([PyPI package information](https://pypi.org/project/django-inline-actions/))
is an extension that adds actions to the [Django](/django.html)
Admin InlineModelAdmin and ModelAdmin changelists. The project is open
sourced under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/escaped/django-inline-actions/blob/master/LICENSE).

[**django-inline-actions / inline_actions / actions.py**](https://github.com/escaped/django-inline-actions/blob/master/inline_actions/./actions.py)

```python
# actions.py
from django.contrib import messages
from django.shortcuts import redirect
~~from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class ViewAction:
    inline_actions = ['view_action']

    def view_action(self, request, obj, parent_obj=None):
~~        url = reverse(
            'admin:{}_{}_change'.format(
                obj._meta.app_label,
                obj._meta.model_name,
            ),
            args=(obj.pk,)
        )
        return redirect(url)
    view_action.short_description = _("View")


class DeleteAction:
    def get_inline_actions(self, request, obj=None):
        actions = super().get_inline_actions(request, obj)
        if self.has_delete_permission(request, obj):
            actions.append('delete_action')
        return actions

    def delete_action(self, request, obj, parent_obj=None):
        if self.has_delete_permission(request):
            obj.delete()
            messages.info(request, "`{}` deleted.".format(obj))
    delete_action.short_description = _("Delete")




## ... source file continues with no further reverse examples...

```


## Example 11 from django-jet
[django-jet](https://github.com/geex-arts/django-jet)
([project documentation](https://jet.readthedocs.io/en/latest/),
[PyPI project page](https://pypi.org/project/django-jet/) and
[more information](http://jet.geex-arts.com/))
is a fancy [Django](/django.html) Admin panel replacement.

The django-jet project is open source under the
[GNU Affero General Public License v3.0](https://github.com/geex-arts/django-jet/blob/dev/LICENSE).

[**django-jet / jet / utils.py**](https://github.com/geex-arts/django-jet/blob/dev/jet/./utils.py)

```python
# utils.py
import datetime
import json
from django.template import Context
from django.utils import translation
from jet import settings
from jet.models import PinnedApplication

try:
    from django.apps.registry import apps
except ImportError:
    try:
        from django.apps import apps # Fix Django 1.7 import issue
    except ImportError:
        pass
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
try:
    from django.core.urlresolvers import reverse, resolve, NoReverseMatch
except ImportError: # Django 1.11
~~    from django.urls import reverse, resolve, NoReverseMatch

from django.contrib.admin import AdminSite
from django.utils.encoding import smart_text
from django.utils.text import capfirst
from django.contrib import messages
from django.utils.encoding import force_text
from django.utils.functional import Promise
from django.contrib.admin.options import IncorrectLookupParameters
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict  # Python 2.6


class JsonResponse(HttpResponse):

    def __init__(self, data, encoder=DjangoJSONEncoder, safe=True, **kwargs):
        if safe and not isinstance(data, dict):
            raise TypeError('In order to allow non-dict objects to be '
                'serialized set the safe parameter to False')


## ... source file abbreviated to get to reverse examples ...


def get_app_list(context, order=True):
    admin_site = get_admin_site(context)
    request = context['request']

    app_dict = {}
    for model, model_admin in admin_site._registry.items():
        app_label = model._meta.app_label
        try:
            has_module_perms = model_admin.has_module_permission(request)
        except AttributeError:
            has_module_perms = request.user.has_module_perms(app_label) # Fix Django < 1.8 issue

        if has_module_perms:
            perms = model_admin.get_model_perms(request)

            if True in perms.values():
                info = (app_label, model._meta.model_name)
                model_dict = {
                    'name': capfirst(model._meta.verbose_name_plural),
                    'object_name': model._meta.object_name,
                    'perms': perms,
                    'model_name': model._meta.model_name
                }
                if perms.get('change', False):
                    try:
~~                        model_dict['admin_url'] = reverse('admin:%s_%s_changelist' % info, current_app=admin_site.name)
                    except NoReverseMatch:
                        pass
                if perms.get('add', False):
                    try:
~~                        model_dict['add_url'] = reverse('admin:%s_%s_add' % info, current_app=admin_site.name)
                    except NoReverseMatch:
                        pass
                if app_label in app_dict:
                    app_dict[app_label]['models'].append(model_dict)
                else:
                    try:
                        name = apps.get_app_config(app_label).verbose_name
                    except NameError:
                        name = app_label.title()
                    app_dict[app_label] = {
                        'name': name,
                        'app_label': app_label,
~~                        'app_url': reverse(
                            'admin:app_list',
                            kwargs={'app_label': app_label},
                            current_app=admin_site.name,
                        ),
                        'has_module_perms': has_module_perms,
                        'models': [model_dict],
                    }

    app_list = list(app_dict.values())

    if order:
        app_list.sort(key=lambda x: x['name'].lower())

        for app in app_list:
            app['models'].sort(key=lambda x: x['name'])

    return app_list


def get_admin_site(context):
    try:
        current_resolver = resolve(context.get('request').path)
        index_resolver = resolve(reverse('%s:index' % current_resolver.namespaces[0]))



## ... source file abbreviated to get to reverse examples ...


        return instance.related_label()
    return smart_text(instance)


class SuccessMessageMixin(object):
    success_message = ''

    def form_valid(self, form):
        response = super(SuccessMessageMixin, self).form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data


def get_model_queryset(admin_site, model, request, preserved_filters=None):
    model_admin = admin_site._registry.get(model)

    if model_admin is None:
        return

    try:
~~        changelist_url = reverse('%s:%s_%s_changelist' % (
            admin_site.name,
            model._meta.app_label,
            model._meta.model_name
        ))
    except NoReverseMatch:
        return

    changelist_filters = None

    if preserved_filters:
        changelist_filters = preserved_filters.get('_changelist_filters')

    if changelist_filters:
        changelist_url += '?' + changelist_filters

    if model_admin:
        queryset = model_admin.get_queryset(request)
    else:
        queryset = model.objects

    list_display = model_admin.get_list_display(request)
    list_display_links = model_admin.get_list_display_links(request, list_display)
    list_filter = model_admin.get_list_filter(request)
    search_fields = model_admin.get_search_fields(request) \


## ... source file abbreviated to get to reverse examples ...


            'url': model.get('admin_url'),
            'url_blank': False,
            'name': model['model_name'],
            'object_name': model['object_name'],
            'label': model.get('name', model['object_name']),
            'has_perms': any(model.get('perms', {}).values()),
        }, app['models'])),
        'pinned': app['app_label'] in pinned_apps,
        'custom': False
    }, original_app_list)


def get_menu_item_url(url, original_app_list):
    if isinstance(url, dict):
        url_type = url.get('type')

        if url_type == 'app':
            return original_app_list[url['app_label']]['url']
        elif url_type == 'model':
            models = dict(map(
                lambda x: (x['name'], x['url']),
                original_app_list[url['app_label']]['models']
            ))
            return models[url['model']]
        elif url_type == 'reverse':
~~            return reverse(url['name'], args=url.get('args'), kwargs=url.get('kwargs'))
    elif isinstance(url, str):
        return url


def get_menu_items(context):
    pinned_apps = PinnedApplication.objects.filter(user=context['user'].pk).values_list('app_label', flat=True)
    original_app_list = OrderedDict(map(lambda app: (app['app_label'], app), get_original_menu_items(context)))
    custom_app_list = settings.JET_SIDE_MENU_ITEMS
    custom_app_list_deprecated = settings.JET_SIDE_MENU_CUSTOM_APPS

    if custom_app_list not in (None, False):
        if isinstance(custom_app_list, dict):
            admin_site = get_admin_site(context)
            custom_app_list = custom_app_list.get(admin_site.name, [])

        app_list = []

        def get_menu_item_app_model(app_label, data):
            item = {'has_perms': True}

            if 'name' in data:
                parts = data['name'].split('.', 2)

                if len(parts) > 1:


## ... source file continues with no further reverse examples...

```


## Example 12 from django-loginas
[django-loginas](https://github.com/skorokithakis/django-loginas)
([PyPI package information](https://pypi.org/project/django-loginas/))
is [Django](/django.html) code library for admins to log into an application
as another user, typically for debugging purposes.

django-loginas is open source under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/skorokithakis/django-loginas/blob/master/LICENSE).

[**django-loginas / loginas / tests / tests.py**](https://github.com/skorokithakis/django-loginas/blob/master/loginas/tests/tests.py)

```python
# tests.py
from __future__ import absolute_import, print_function, unicode_literals

import unittest
from datetime import timedelta

import django
from django.conf import settings as django_settings
from django.contrib.auth.models import User
from django.contrib.messages.storage.cookie import CookieStorage
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.test import Client, TestCase
from django.test.utils import override_settings as override_settings_orig
from django.utils import timezone
from loginas import settings as la_settings

try:
    from django.core.urlresolvers import reverse
except ImportError:
~~    from django.urls import reverse

try:
    from urllib.parse import urlsplit
except ImportError:
    from urlparse import urlsplit  # type: ignore


try:
    import imp

    reload = imp.reload  # @ReservedAssignment
except ImportError:
    pass


class override_settings(override_settings_orig):

    def enable(self):
        super(override_settings, self).enable()
        from loginas import settings as loginas_settings

        reload(loginas_settings)

    def disable(self):


## ... source file abbreviated to get to reverse examples ...


    raise PermissionDenied("You can't login as target user")


class WrongAuthBackend:

    def authenticate(self, *args, **kwargs):
        return None


class ViewTest(TestCase):


    def setUp(self):
        self.client = Client(enforce_csrf_checks=True)
        self.client.get("/")  # To get the CSRF token for next request
        assert django_settings.CSRF_COOKIE_NAME in self.client.cookies
        self.target_user = User.objects.create(username="target")

    def get_csrf_token_payload(self):
        return {"csrfmiddlewaretoken": self.client.cookies[django_settings.CSRF_COOKIE_NAME].value}

    def get_target_url(self, target_user=None):
        if target_user is None:
            target_user = self.target_user
        response = self.client.post(
~~            reverse("loginas-user-login", kwargs={"user_id": target_user.id}), data=self.get_csrf_token_payload()
        )
        self.assertEqual(response.status_code, 302)
        return response

    def assertCurrentUserIs(self, user):
        id_ = str(user.id if user is not None else None).encode("utf-8")
        r = self.client.post(reverse("current_user"), data=self.get_csrf_token_payload())
        self.assertEqual(r.content, id_)

    def assertLoginError(self, resp, message=None):
        self.assertEqual(urlsplit(resp["Location"])[2], "/")
        message = message or "You do not have permission to do that."
        messages = CookieStorage(resp)._decode(resp.cookies["messages"].value)
        self.assertIn((40, message), [(m.level, m.message) for m in messages])

    def assertLoginSuccess(self, resp, user):
        self.assertEqual(urlsplit(resp["Location"])[2], django_settings.LOGIN_REDIRECT_URL)
        msg = la_settings.MESSAGE_LOGIN_SWITCH.format(username=user.__dict__[la_settings.USERNAME_FIELD])
        messages = CookieStorage(resp)._decode(resp.cookies["messages"].value)
        self.assertIn(msg, "".join([m.message for m in messages]))

    def assertRaisesExact(self, exception, func, *args, **kwargs):
        try:
            func(*args, **kwargs)


## ... source file abbreviated to get to reverse examples ...


        self.assertCurrentUserIs(user)

    @unittest.skipIf(django.VERSION[:2] < (1, 10), "Django < 1.10 allows to authenticate as inactive user")
    def test_auth_backends_user_not_found(self):
        superuser = create_user("me", "pass", is_superuser=True, is_staff=True)
        self.assertTrue(self.client.login(username="me", password="pass"))
        self.assertCurrentUserIs(superuser)
        inactive_user = create_user("name", "pass", is_active=False)
        with self.settings(
            AUTHENTICATION_BACKENDS=("django.contrib.auth.backends.ModelBackend", "tests.WrongAuthBackend")
        ):
            message = "Could not find an appropriate authentication backend"
            self.assertLoginError(self.get_target_url(target_user=inactive_user), message=message)
        self.assertCurrentUserIs(superuser)

    @override_settings(CAN_LOGIN_AS=can_login_as_always_raise_permission_denied)
    def test_can_login_as_permission_denied(self):
        message = "You can't login as target user"
        self.assertLoginError(self.get_target_url(), message=message)

    def test_as_anonymous_user(self):
        self.assertLoginError(self.get_target_url())
        self.assertCurrentUserIs(None)

    def test_get_405_method_not_allowed(self):
~~        url = reverse("loginas-user-login", kwargs={"user_id": "0"})
        r = self.client.get(url)
        self.assertEqual(r.status_code, 405)

    def test_missing_csrf_token_403_forbidden(self):
~~        url = reverse("loginas-user-login", kwargs={"user_id": "0"})
        r = self.client.post(url)
        self.assertEqual(r.status_code, 403)

    @override_settings(LOGINAS_REDIRECT_URL="/another-redirect")
    def test_loginas_redirect_url(self):
        create_user("me", "pass", is_superuser=True, is_staff=True)
        self.assertTrue(self.client.login(username="me", password="pass"))

        response = self.client.post(
~~            reverse("loginas-user-login", kwargs={"user_id": self.target_user.id}), data=self.get_csrf_token_payload()
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(urlsplit(response["Location"])[2], "/another-redirect")

    def test_restore_original_user(self):

        original_user = create_user("me", "pass", is_superuser=True, is_staff=True)
        self.assertTrue(self.client.login(username="me", password="pass"))
        response = self.get_target_url()
        self.assertLoginSuccess(response, self.target_user)

~~        url = reverse("loginas-user-login", kwargs={"user_id": self.target_user.id})
        self.client.get(url)
        self.assertCurrentUserIs(self.target_user)

~~        url = reverse("loginas-logout")
        self.client.get(url)
        self.assertCurrentUserIs(original_user)

    @override_settings(LOGINAS_LOGOUT_REDIRECT_URL="/another-redirect")
    def test_loginas_redirect_url_again(self):
        create_user("me", "pass", is_superuser=True, is_staff=True)
        self.assertTrue(self.client.login(username="me", password="pass"))
        response = self.client.get(reverse("loginas-logout"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(urlsplit(response["Location"])[2], "/another-redirect")

    def test_last_login_not_updated(self):
        last_login = timezone.now() - timedelta(hours=1)
        self.target_user.last_login = last_login
        self.target_user.save()
        create_user("me", "pass", is_superuser=True, is_staff=True)
        self.assertTrue(self.client.login(username="me", password="pass"))
        response = self.get_target_url()
        self.assertLoginSuccess(response, self.target_user)
        self.assertCurrentUserIs(self.target_user)
        target_user = User.objects.get(id=self.target_user.id)  # refresh from db
        self.assertEqual(target_user.last_login, last_login)

    @override_settings(LOGINAS_UPDATE_LAST_LOGIN=True)


## ... source file continues with no further reverse examples...

```


## Example 13 from django-mongonaut
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

[**django-mongonaut / mongonaut / views.py**](https://github.com/jazzband/django-mongonaut/blob/master/mongonaut/./views.py)

```python
# views.py
import math

from django.contrib import messages
~~from django.urls import reverse
from django.forms import Form
from django.http import HttpResponseForbidden
from django.http import Http404
from django.utils.functional import cached_property
from django.views.generic.edit import DeletionMixin
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from mongoengine.fields import EmbeddedDocumentField, ListField

from mongonaut.forms import MongoModelForm
from mongonaut.mixins import MongonautFormViewMixin
from mongonaut.mixins import MongonautViewMixin
from mongonaut.utils import is_valid_object_id


class IndexView(MongonautViewMixin, ListView):

    template_name = "mongonaut/index.html"
    queryset = []
    permission = 'has_view_permission'

    def get_queryset(self):
        return self.get_mongoadmins()


## ... source file abbreviated to get to reverse examples ...


        context['app_label'] = self.app_label
        context['document_name'] = self.document_name
        context['keys'] = ['id', ]
        context['embedded_documents'] = []
        context['list_fields'] = []
        for key in sorted([x for x in self.document._fields.keys() if x != 'id']):
            if isinstance(self.document._fields[key], EmbeddedDocumentField):
                context['embedded_documents'].append(key)
                continue
            if isinstance(self.document._fields[key], ListField):
                context['list_fields'].append(key)
                continue
            context['keys'].append(key)
        return context


class DocumentEditFormView(MongonautViewMixin, FormView, MongonautFormViewMixin):

    template_name = "mongonaut/document_edit_form.html"
    form_class = Form
    success_url = '/'
    permission = 'has_edit_permission'

    def get_success_url(self):
        self.set_mongonaut_base()
~~        return reverse('document_detail_edit_form', kwargs={'app_label': self.app_label, 'document_name': self.document_name, 'id': self.kwargs.get('id')})

    def get_context_data(self, **kwargs):
        context = super(DocumentEditFormView, self).get_context_data(**kwargs)
        self.set_mongoadmin()
        context = self.set_permissions_in_context(context)
        self.document_type = getattr(self.models, self.document_name)
        self.ident = self.kwargs.get('id')
        self.document = self.document_type.objects.get(pk=self.ident)

        context['document'] = self.document
        context['app_label'] = self.app_label
        context['document_name'] = self.document_name
~~        context['form_action'] = reverse('document_detail_edit_form', args=[self.kwargs.get('app_label'),
                                                                            self.kwargs.get('document_name'),
                                                                            self.kwargs.get('id')])

        return context

    def get_form(self): #get_form(self, Form) leads to "get_form() missing 1 required positional argument: 'Form'" error."
        self.set_mongoadmin()
        context = self.set_permissions_in_context({})

        if not context['has_edit_permission']:
            return HttpResponseForbidden("You do not have permissions to edit this content.")

        self.document_type = getattr(self.models, self.document_name)
        self.ident = self.kwargs.get('id')
        try:
            self.document = self.document_type.objects.get(pk=self.ident)
        except self.document_type.DoesNotExist:
            raise Http404
        self.form = Form()

        if self.request.method == 'POST':
            self.form = self.process_post_form('Your changes have been saved.')
        else:
            self.form = MongoModelForm(model=self.document_type, instance=self.document).get_form()
        return self.form


class DocumentAddFormView(MongonautViewMixin, FormView, MongonautFormViewMixin):

    template_name = "mongonaut/document_add_form.html"
    form_class = Form
    success_url = '/'
    permission = 'has_add_permission'

    def get_success_url(self):
        self.set_mongonaut_base()
~~        return reverse('document_detail', kwargs={'app_label': self.app_label, 'document_name': self.document_name, 'id': str(self.new_document.id)})

    def get_context_data(self, **kwargs):
        context = super(DocumentAddFormView, self).get_context_data(**kwargs)
        self.set_mongoadmin()
        context = self.set_permissions_in_context(context)
        self.document_type = getattr(self.models, self.document_name)

        context['app_label'] = self.app_label
        context['document_name'] = self.document_name
~~        context['form_action'] = reverse('document_detail_add_form', args=[self.kwargs.get('app_label'),
                                                                           self.kwargs.get('document_name')])

        return context

    def get_form(self):
        self.set_mongonaut_base()
        self.document_type = getattr(self.models, self.document_name)
        self.form = Form()

        if self.request.method == 'POST':
            self.form = self.process_post_form('Your new document has been added and saved.')
        else:
            self.form = MongoModelForm(model=self.document_type).get_form()
        return self.form


class DocumentDeleteView(DeletionMixin, MongonautViewMixin, TemplateView):

    success_url = "/"
    template_name = "mongonaut/document_delete.html"

    def get_success_url(self):
        self.set_mongonaut_base()
        messages.add_message(self.request, messages.INFO, 'Your document has been deleted.')
~~        return reverse('document_list', kwargs={'app_label': self.app_label, 'document_name': self.document_name})

    def get_object(self):
        self.set_mongoadmin()
        self.document_type = getattr(self.models, self.document_name)
        self.ident = self.kwargs.get('id')
        self.document = self.document_type.objects.get(pk=self.ident)
        return self.document



## ... source file continues with no further reverse examples...

```


## Example 14 from django-oauth-toolkit
[django-oauth-toolkit](https://github.com/jazzband/django-oauth-toolkit)
([project website](http://dot.evonove.it/) and
[PyPI package information](https://pypi.org/project/django-oauth-toolkit/1.2.0/))
is a code library for adding and handling [OAuth2](https://oauth.net/)
flows within your [Django](/django.html) web application and
[API](/application-programming-interfaces.html).

The django-oauth-toolkit project is open sourced under the
[FreeBSD license](https://github.com/jazzband/django-oauth-toolkit/blob/master/LICENSE)
and it is maintained by the developer community group
[Jazzband](https://jazzband.co/).

[**django-oauth-toolkit / oauth2_provider / models.py**](https://github.com/jazzband/django-oauth-toolkit/blob/master/oauth2_provider/./models.py)

```python
# models.py
import logging
from datetime import timedelta
from urllib.parse import parse_qsl, urlparse

from django.apps import apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db import models, transaction
~~from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .generators import generate_client_id, generate_client_secret
from .scopes import get_scopes_backend
from .settings import oauth2_settings
from .validators import RedirectURIValidator, WildcardSet


logger = logging.getLogger(__name__)


class AbstractApplication(models.Model):
    CLIENT_CONFIDENTIAL = "confidential"
    CLIENT_PUBLIC = "public"
    CLIENT_TYPES = (
        (CLIENT_CONFIDENTIAL, _("Confidential")),
        (CLIENT_PUBLIC, _("Public")),
    )

    GRANT_AUTHORIZATION_CODE = "authorization-code"
    GRANT_IMPLICIT = "implicit"
    GRANT_PASSWORD = "password"
    GRANT_CLIENT_CREDENTIALS = "client-credentials"


## ... source file abbreviated to get to reverse examples ...



        grant_types = (
            AbstractApplication.GRANT_AUTHORIZATION_CODE,
            AbstractApplication.GRANT_IMPLICIT,
        )

        redirect_uris = self.redirect_uris.strip().split()
        allowed_schemes = set(s.lower() for s in self.get_allowed_schemes())

        if redirect_uris:
            validator = RedirectURIValidator(WildcardSet())
            for uri in redirect_uris:
                validator(uri)
                scheme = urlparse(uri).scheme
                if scheme not in allowed_schemes:
                    raise ValidationError(_(
                        "Unauthorized redirect scheme: {scheme}"
                    ).format(scheme=scheme))

        elif self.authorization_grant_type in grant_types:
            raise ValidationError(_(
                "redirect_uris cannot be empty with grant_type {grant_type}"
            ).format(grant_type=self.authorization_grant_type))

    def get_absolute_url(self):
~~        return reverse("oauth2_provider:detail", args=[str(self.id)])

    def get_allowed_schemes(self):
        return oauth2_settings.ALLOWED_REDIRECT_URI_SCHEMES

    def allows_grant_type(self, *grant_types):
        return self.authorization_grant_type in grant_types

    def is_usable(self, request):
        return True


class ApplicationManager(models.Manager):
    def get_by_natural_key(self, client_id):
        return self.get(client_id=client_id)


class Application(AbstractApplication):
    objects = ApplicationManager()

    class Meta(AbstractApplication.Meta):
        swappable = "OAUTH2_PROVIDER_APPLICATION_MODEL"

    def natural_key(self):
        return (self.client_id,)


## ... source file continues with no further reverse examples...

```


## Example 15 from django-rest-framework
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

[**django-rest-framework / rest_framework / reverse.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./reverse.py)

```python
# reverse.py
from django.urls import NoReverseMatch
~~from django.urls import reverse as django_reverse
from django.utils.functional import lazy

from rest_framework.settings import api_settings
from rest_framework.utils.urls import replace_query_param


def preserve_builtin_query_params(url, request=None):
    if request is None:
        return url

    overrides = [
        api_settings.URL_FORMAT_OVERRIDE,
    ]

    for param in overrides:
        if param and (param in request.GET):
            value = request.GET[param]
            url = replace_query_param(url, param, value)

    return url


~~def reverse(viewname, args=None, kwargs=None, request=None, format=None, **extra):
    scheme = getattr(request, 'versioning_scheme', None)
    if scheme is not None:
        try:
            url = scheme.reverse(viewname, args, kwargs, request, format, **extra)
        except NoReverseMatch:
            url = _reverse(viewname, args, kwargs, request, format, **extra)
    else:
        url = _reverse(viewname, args, kwargs, request, format, **extra)

    return preserve_builtin_query_params(url, request)


def _reverse(viewname, args=None, kwargs=None, request=None, format=None, **extra):
    if format is not None:
        kwargs = kwargs or {}
        kwargs['format'] = format
    url = django_reverse(viewname, args=args, kwargs=kwargs, **extra)
    if request:
        return request.build_absolute_uri(url)
    return url


reverse_lazy = lazy(reverse, str)



## ... source file continues with no further reverse examples...

```


## Example 16 from django-sql-explorer
[django-sql-explorer](https://github.com/groveco/django-sql-explorer)
([PyPI page](https://pypi.org/project/django-sql-explorer/0.2/)),
also referred to as "SQL Explorer",
is a code library for the [Django](/django.html) Admin that allows
approved, authenticated users to view and execute direct database SQL
queries. The tool keeps track of executed queries so users can share them
with each other, as well as export results to downloadable formats.
django-sql-explorer is provided as open source under the
[MIT license](https://github.com/groveco/django-sql-explorer/blob/master/LICENSE).

[**django-sql-explorer / explorer / models.py**](https://github.com/groveco/django-sql-explorer/blob/master/explorer/./models.py)

```python
# models.py
from __future__ import unicode_literals

import logging
from time import time
import six

from django.db import models, DatabaseError
try:
~~    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

from django.conf import settings

from explorer import app_settings
from explorer.utils import (
    passes_blacklist,
    swap_params,
    extract_params,
    shared_dict_update,
    get_s3_bucket,
    get_params_for_url,
    get_valid_connection
)

MSG_FAILED_BLACKLIST = "Query failed the SQL blacklist: %s"


logger = logging.getLogger(__name__)

@six.python_2_unicode_compatible
class Query(models.Model):
    title = models.CharField(max_length=255)


## ... source file abbreviated to get to reverse examples ...


        return swap_params(self.sql, self.available_params())

    def execute_query_only(self):
        return QueryResult(self.final_sql(), get_valid_connection(self.connection))

    def execute_with_logging(self, executing_user):
        ql = self.log(executing_user)
        ret = self.execute()
        ql.duration = ret.duration
        ql.save()
        return ret, ql

    def execute(self):
        ret = self.execute_query_only()
        ret.process()
        return ret

    def available_params(self):

        p = extract_params(self.sql)
        if self.params:
            shared_dict_update(p, self.params)
        return p

    def get_absolute_url(self):
~~        return reverse("query_detail", kwargs={'query_id': self.id})

    @property
    def params_for_url(self):
        return get_params_for_url(self)

    def log(self, user=None):
        if user:
            try:
                is_anonymous = user.is_anonymous()
            except TypeError:
                is_anonymous = user.is_anonymous
            if is_anonymous:
                user = None
        ql = QueryLog(sql=self.final_sql(), query_id=self.id, run_by_user=user, connection=self.connection)
        ql.save()
        return ql

    @property
    def shared(self):
        return self.id in set(sum(app_settings.EXPLORER_GET_USER_QUERY_VIEWS().values(), []))

    @property
    def snapshots(self):
        if app_settings.ENABLE_TASKS:


## ... source file continues with no further reverse examples...

```


## Example 17 from django-tables2
[django-tables2](https://github.com/jieter/django-tables2)
([projection documentation](https://django-tables2.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-tables2/))
is a code library for [Django](/django.html) that simplifies creating and
displaying tables in [Django templates](/django-templates.html),
especially with more advanced features such as pagination and sorting.
The project and its code are
[available as open source](https://github.com/jieter/django-tables2/blob/master/LICENSE).

[**django-tables2 / django_tables2 / columns / base.py**](https://github.com/jieter/django-tables2/blob/master/django_tables2/columns/base.py)

```python
# base.py
from collections import OrderedDict
from itertools import islice

from django.core.exceptions import ImproperlyConfigured
~~from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import SafeData
from django.utils.text import capfirst

from ..utils import (
    Accessor,
    AttributeDict,
    OrderBy,
    OrderByTuple,
    call_with_appropriate,
    computed_values,
)


class Library:

    def __init__(self):
        self.columns = []

    def register(self, column):
        if not hasattr(column, "from_field"):
            raise ImproperlyConfigured(
                "{} is not a subclass of Column".format(column.__class__.__name__)
            )


## ... source file abbreviated to get to reverse examples ...


                    "for linkify=True, '{}' must have a method get_absolute_url".format(
                        str(context)
                    )
                )
        return context.get_absolute_url()

    def call_reverse(self, record):

        def resolve_if_accessor(val):
            return val.resolve(record) if isinstance(val, Accessor) else val

        params = self.reverse_args.copy()

        params["viewname"] = resolve_if_accessor(params["viewname"])
        if params.get("urlconf", None):
            params["urlconf"] = resolve_if_accessor(params["urlconf"])
        if params.get("args", None):
            params["args"] = [resolve_if_accessor(a) for a in params["args"]]
        if params.get("kwargs", None):
            params["kwargs"] = {
                key: resolve_if_accessor(val) for key, val in params["kwargs"].items()
            }
        if params.get("current_app", None):
            params["current_app"] = resolve_if_accessor(params["current_app"])

~~        return reverse(**params)

    def get_attrs(self, **kwargs):
        attrs = AttributeDict(self.attrs or {})
        attrs["href"] = self.compose_url(**kwargs)

        return attrs

    def __call__(self, content, **kwargs):
        attrs = self.get_attrs(**kwargs)
        if attrs["href"] is None:
            return content

        return format_html("<a {}>{}</a>", attrs.as_html(), content)


@library.register
class Column:

    creation_counter = 0
    empty_values = (None, "")

    link = None

    _explicit = False


## ... source file continues with no further reverse examples...

```


## Example 18 from django-webshell
[django-webshell](https://github.com/onrik/django-webshell) is an extension
for executing arbitrary code in the
[Django admin](https://docs.djangoproject.com/en/stable/ref/contrib/admin/),
similar to how you can run code by using the `django manage.py shell`
command from the terminal.

The django-webshell project is provided as open source under the
[MIT license](https://github.com/onrik/django-webshell/blob/master/LICENSE).

[**django-webshell / webshell / tests.py**](https://github.com/onrik/django-webshell/blob/master/webshell/./tests.py)

```python
# tests.py
from django.test import TestCase
from django.conf import settings
from django.contrib.auth import get_user_model
try:
    from django.core.urlresolvers import reverse
except ImportError:
~~    from django.urls import reverse

from webshell.models import Script

User = get_user_model()


class WebshellTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='user', is_staff=True, is_superuser=True)
        self.user.set_password('123456')
        self.user.save()
~~        self.url = reverse('execute-script')
        self.login_url = '%s?next=%s' % (settings.LOGIN_URL, self.url)

    def login(self):
        self.assertTrue(self.client.login(
            username=self.user.username, password='123456'))

    def test_wrong_method(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 405)

    def test_login_required(self):
        response = self.client.post(self.url)
        self.assertRedirects(response, self.login_url, 302, 404)

    def test_superuser_required(self):
        self.user.is_superuser = False
        self.user.save()
        self.login()
        response = self.client.post(self.url)
        self.assertRedirects(response, self.login_url, 302, 404)

    def test_success(self):
        self.login()

        response = self.client.post(self.url, data={'source': 'print(1)'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'1\n')

    def test_success_exception(self):
        self.login()

        response = self.client.post(self.url, data={'source': '[1][1]'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'IndexError: list index out of range', response.content)

    def test_admin(self):
        self.login()

        script = Script.objects.create(name='Test')

        urls = (
~~            reverse('admin:webshell_script_add'),
~~            reverse('admin:webshell_script_change', args=[script.id]),
~~            reverse('admin:webshell_script_changelist'),
        )

        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)



## ... source file continues with no further reverse examples...

```


## Example 19 from django-wiki
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

[**django-wiki / src/wiki / decorators.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/./decorators.py)

```python
# decorators.py
from functools import wraps

from django.http import HttpResponseForbidden
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.template.loader import render_to_string
~~from django.urls import reverse
from django.utils.http import urlquote
from wiki.conf import settings
from wiki.core.exceptions import NoRootURL


def response_forbidden(request, article, urlpath, read_denied=False):
    if request.user.is_anonymous:
        qs = request.META.get("QUERY_STRING", "")
        if qs:
            qs = urlquote("?" + qs)
        else:
            qs = ""
        return redirect(settings.LOGIN_URL + "?next=" + request.path + qs)
    else:
        return HttpResponseForbidden(
            render_to_string(
                "wiki/permission_denied.html",
                context={
                    "article": article,
                    "urlpath": urlpath,
                    "read_denied": read_denied,
                },
                request=request,
            )


## ... source file abbreviated to get to reverse examples ...


    can_write=False,
    deleted_contents=False,
    not_locked=False,
    can_delete=False,
    can_moderate=False,
    can_create=False,
):

    def wrapper(request, *args, **kwargs):
        from . import models

        path = kwargs.pop("path", None)
        article_id = kwargs.pop("article_id", None)

        if path is not None:
            try:
                urlpath = models.URLPath.get_by_path(path, select_related=True)
            except NoRootURL:
                return redirect("wiki:root_create")
            except models.URLPath.DoesNotExist:
                try:
                    pathlist = list(filter(lambda x: x != "", path.split("/"),))
                    path = "/".join(pathlist[:-1])
                    parent = models.URLPath.get_by_path(path)
                    return HttpResponseRedirect(
~~                        reverse("wiki:create", kwargs={"path": parent.path})
                        + "?slug=%s" % pathlist[-1].lower()
                    )
                except models.URLPath.DoesNotExist:
                    return HttpResponseNotFound(
                        render_to_string(
                            "wiki/error.html",
                            context={"error_type": "ancestors_missing"},
                            request=request,
                        )
                    )
            if urlpath.article:
                article = urlpath.article
            else:
~~                return_url = reverse("wiki:get", kwargs={"path": urlpath.parent.path})
                urlpath.delete()
                return HttpResponseRedirect(return_url)

        elif article_id:
            articles = models.Article.objects

            article = get_object_or_404(articles, id=article_id)
            try:
                urlpath = models.URLPath.objects.get(articles__article=article)
            except (
                models.URLPath.DoesNotExist,
                models.URLPath.MultipleObjectsReturned,
            ):
                urlpath = None

        else:
            raise TypeError("You should specify either article_id or path")

        if not deleted_contents:
            if urlpath:
                if urlpath.is_deleted():  # This also checks all ancestors
                    return redirect("wiki:deleted", path=urlpath.path)
            else:
                if article.current_revision and article.current_revision.deleted:


## ... source file continues with no further reverse examples...

```


## Example 20 from graphite-web
[Graphite](https://github.com/graphite-project/graphite-web)
([project website](http://graphiteapp.org/),
[documentation](https://graphite.readthedocs.io/en/latest/) and
[PyPI package information](https://pypi.org/project/graphite-web/))
is a metrics collection and visualization tool, built with both
Python and JavaScript. Metrics are collected by a Node.js application
and displayed using a [Django](/django.html) web application,
called "Graphite-Web", which is one of three core projects under
the Graphite umbrella (the other two are
[Carbon](https://github.com/graphite-project/carbon) and
[Whisper](https://github.com/graphite-project/whisper)).

Graphite is provided as open sourced under the
[Apache License 2.0](https://github.com/graphite-project/whisper/blob/master/LICENSE).

[**graphite-web / webapp / tests / test_metrics.py**](https://github.com/graphite-project/graphite-web/blob/master/webapp/tests/test_metrics.py)

```python
# test_metrics.py
import copy
import os
import shutil
import time

from mock import patch

from django.conf import settings
try:
~~    from django.urls import reverse
except ImportError:  # Django < 1.10
    from django.core.urlresolvers import reverse
from .base import TestCase

import whisper

from graphite.util import unpickle, msgpack, json


class MetricsTester(TestCase):
    db = os.path.join(settings.WHISPER_DIR, 'test.wsp')
    hostcpu = os.path.join(settings.WHISPER_DIR, 'hosts/hostname/cpu.wsp')

    def wipe_whisper(self):
        try:
            os.remove(self.db)
        except OSError:
            pass

    def create_whisper_hosts(self, ts=None):
        worker1 = self.hostcpu.replace('hostname', 'worker1')
        worker2 = self.hostcpu.replace('hostname', 'worker2')
        try:
            os.makedirs(worker1.replace('cpu.wsp', ''))
            os.makedirs(worker2.replace('cpu.wsp', ''))
        except OSError:
            pass

        whisper.create(worker1, [(1, 60)])
        whisper.create(worker2, [(1, 60)])

        ts = ts or int(time.time())
        whisper.update(worker1, 1, ts)
        whisper.update(worker2, 2, ts)

    def wipe_whisper_hosts(self):
        try:
            os.remove(self.hostcpu.replace('hostname', 'worker1'))
            os.remove(self.hostcpu.replace('hostname', 'worker2'))
            shutil.rmtree(self.hostcpu.replace('hostname/cpu.wsp', ''))
        except OSError:
            pass

    def test_index_json(self):
        self.create_whisper_hosts()
        self.addCleanup(self.wipe_whisper_hosts)

~~        url = reverse('metrics_index')

        request = {}
        response = self.client.post(url, request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data[0], 'hosts.worker1.cpu')
        self.assertEqual(data[1], 'hosts.worker2.cpu')


        request = {'jsonp': 'callback'}
        response = self.client.post(url, request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.split(b"(")[1].strip(b")"))
        self.assertEqual(data[0], 'hosts.worker1.cpu')
        self.assertEqual(data[1], 'hosts.worker2.cpu')

        def mock_STORE_get_index(self, requestContext=None):
            raise Exception('test')

        with patch('graphite.metrics.views.STORE.get_index', mock_STORE_get_index):
            request = {}
            response = self.client.post(url, request)
            self.assertEqual(response.status_code, 500)
            data = json.loads(response.content)
            self.assertEqual(data, [])

    def test_find_view(self):
        ts = int(time.time())

        self.create_whisper_hosts(ts)
        self.addCleanup(self.wipe_whisper_hosts)

~~        url = reverse('metrics_find')

        response = self.client.post(url, {})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b"Bad Request: Missing required parameter 'query'")

        response = self.client.post(url, {
            'query': '*',
            'from': 'now-1h',
            'until': 'now-2h',
        })
        self.assertEqual(response.status_code, 400)
        self.assertRegex(response.content, b"^Bad Request: Failed to instantiate find query: Invalid interval start=[0-9]+ end=[0-9]+$")

        response = self.client.post(url, {
            'query': '*',
            'wildcards': '123a',
        })
        self.assertEqual(response.status_code, 400)
        self.assertRegex(response.content, b"^Bad Request: Invalid int value u?'123a' for param wildcards: invalid literal for int\\(\\) with base 10: u?'123a'$")

        response = self.client.post(url, {
            'query': '*',
            'from': 'now-1mmminute', # "mmminute" is misspelled
        })


## ... source file abbreviated to get to reverse examples ...



            request['query']='hosts.*.cpu'
            content = test_find_view_basics(request)
            data = json.loads(content.split(b"(")[1].strip(b")"))
            self.assertEqual(len(data), 2)

            self.assertEqual(data[0]['path'], 'hosts.worker1.cpu')
            self.assertEqual(data[0]['is_leaf'], True)
            self.assertEqual(len(data[0]['intervals']), 1)
            self.assertIn(int(data[0]['intervals'][0]['end']), [ts, ts - 1])

            self.assertEqual(data[1]['path'], 'hosts.worker2.cpu')
            self.assertEqual(data[1]['is_leaf'], True)
            self.assertEqual(len(data[1]['intervals']), 1)
            self.assertIn(int(data[1]['intervals'][0]['end']), [ts, ts - 1])

            request['query']='other'
            content = test_find_view_basics(request)
            data = json.loads(content.split(b"(")[1].strip(b")"))
            self.assertEqual(data, [])

    def test_expand_view(self):
        self.create_whisper_hosts()
        self.addCleanup(self.wipe_whisper_hosts)

~~        url = reverse('metrics_expand')

        request = {'query': '*'}
        response = self.client.post(url, request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['results'], [u'hosts'])

        request = {'query': ''}
        response = self.client.post(url, request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['results'], [u''])

    def test_get_metadata_view(self):
        self.create_whisper_hosts()
        self.addCleanup(self.wipe_whisper_hosts)

~~        url = reverse('metrics_get_metadata')

        request = {'metric': 'hosts.worker1.cpu', 'key': 'a'}
        response = self.client.post(url, request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['hosts.worker1.cpu']['error'], "Unexpected error occurred in CarbonLink.get_metadata(hosts.worker1.cpu, a)")

    def test_set_metadata_view(self):
        self.create_whisper_hosts()
        self.addCleanup(self.wipe_whisper_hosts)

~~        url = reverse('metrics_set_metadata')

        request = {'metric': 'hosts.worker1.cpu', 'key': 'a', 'value': 'b'}
        response = self.client.get(url, request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['hosts.worker1.cpu']['error'], "Unexpected error occurred in CarbonLink.set_metadata(hosts.worker1.cpu, a)")

        request = {'operations': '[{ "metric": "hosts.worker1.cpu", "key": "a", "value": "b" }]'}
        response = self.client.post(url, request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['hosts.worker1.cpu']['error'], "Unexpected error occurred in bulk CarbonLink.set_metadata(hosts.worker1.cpu)")



## ... source file continues with no further reverse examples...

```


## Example 21 from register
[register](https://github.com/ORGAN-IZE/register) is a [Django](/django.html),
[Bootstrap](/bootstrap-css.html), [PostgreSQL](/postgresql.html) project that is
open source under the
[GNU General Public License v3.0](https://github.com/ORGAN-IZE/register/blob/master/LICENSE).
This web application makes it easier for people to register as organ donors.
You can see the application live at
[https://register.organize.org/](https://register.organize.org/).

[**register / registration / views.py**](https://github.com/ORGAN-IZE/register/blob/master/registration/./views.py)

```python
# views.py
from __future__ import unicode_literals

import logging
import collections
import datetime
import json
import random

import dateutil.parser
import django.contrib.messages
~~import django.urls
import django.http
import django.shortcuts
import django.views.generic.edit
import django.forms
import django.utils
from django.core.cache import cache
from django.conf import settings
from formtools.wizard.forms import ManagementForm
from formtools.wizard.storage import get_storage
from formtools.wizard.views import NamedUrlSessionWizardView
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

from axes import utils
import dateutil.parser

import cobrand.models
import widget.models
import fiftythree.client
import forms

logger = logging.getLogger(__name__)

SESSION_REGISTRATION_CONFIGURATION = 'registration_configuration'


## ... source file abbreviated to get to reverse examples ...


            secure=False, httponly=True)
        return response


class StateLookupView(MinorRestrictedMixin, django.views.generic.edit.FormView):
    template_name = 'registration/start.html'
    form_class = forms.StateLookupForm
    accepts_registration = True

    def get(self, request, *args, **kwargs):
        clean_session(request.session)
        clean_next_of_kin_email_session(request.session)
        setup_external_source_session(request)
        if self.request.GET.get('email') and self.request.GET.get('postal_code'):
            email = self.request.GET['email']
            postal_code = self.request.GET['postal_code']
            form = self.form_class(data={'email': email, 'postal_code': postal_code})
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        return super(StateLookupView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        if self.accepts_registration:
~~            return django.urls.reverse(
                'register', kwargs={'step': '1',})
        else:
~~            return django.urls.reverse('unsupported_state')

    def get_initial(self):
        initial = self.initial.copy()
        if 'email' in self.request.GET:
            initial['email'] = self.request.GET['email']
        if 'postal_code' in self.request.GET:
            initial['postal_code'] = self.request.GET['postal_code']
        return initial

    def get_context_data(self, **kwargs):
        data = super(StateLookupView, self).get_context_data(**kwargs)
        data['update'] = self.is_update
        if data['update']:
            data['page_title'] = _('Update your registration')
        else:
            data['page_title'] = _('Let&rsquo;s Begin...')

        return data

    @property
    def is_update(self):
        return self.kwargs.get('update') is True

    def submit_email(self, data):


## ... source file abbreviated to get to reverse examples ...


class WaitingListFilmRedirectView(django.views.generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return '/?reg_source=waitinglistfilm'


class UnsupportedStateView(django.views.generic.TemplateView):
    template_name = 'registration/unsupported_state.html'

    def get(self, request, *args, **kwargs):
        redirect_url = self.request.session.get(SESSION_REDIRECT_URL)
        if not redirect_url:
            return django.shortcuts.redirect('start')
        context = self.get_context_data(**kwargs)
        context['state'] = self.request.session[SESSION_STATE]
        context['state_name'] = self.request.session[SESSION_STATE_NAME]
        return self.render_to_response(context)


class StateRedirectView(django.views.generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        redirect_url = self.request.session.get(SESSION_REDIRECT_URL)
        clean_session(self.request.session)
        if redirect_url:
            return redirect_url
        else:
~~            return django.urls.reverse('start')


class RegistrationWizardView(MinorRestrictedMixin, NamedUrlSessionWizardView):
    form_list = [forms.StateLookupForm, ]
    page_titles = collections.OrderedDict()
    page_fieldsets = collections.OrderedDict()
    page_explanatory_texts = collections.OrderedDict()
    page_count = 0
    configuration = None
    api_error_key = 'api_error'

    def check_configuration(self):
        if not self.configuration and (SESSION_REGISTRATION_CONFIGURATION not in self.request.session):
            return False
        else:
            return True

    def process_registration_configuration(self):
        self.configuration = self.request.session[SESSION_REGISTRATION_CONFIGURATION]
        license_id_formats = None
        if SESSION_LICENSE_ID_FORMATS in self.request.session:
            license_id_formats = self.request.session[SESSION_LICENSE_ID_FORMATS]

        validate_organ_tissue_selection = False


## ... source file continues with no further reverse examples...

```


## Example 22 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / snippets / models.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/snippets/models.py)

```python
# models.py
from django.contrib.admin.utils import quote
from django.core import checks
~~from django.urls import reverse

from wagtail.admin.checks import check_panels_in_model
from wagtail.admin.models import get_object_usage

SNIPPET_MODELS = []


def get_snippet_models():
    return SNIPPET_MODELS


def register_snippet(model):
    if model not in SNIPPET_MODELS:
        model.get_usage = get_object_usage
        model.usage_url = get_snippet_usage_url
        SNIPPET_MODELS.append(model)
        SNIPPET_MODELS.sort(key=lambda x: x._meta.verbose_name)

        @checks.register('panels')
        def modeladmin_model_check(app_configs, **kwargs):
            errors = check_panels_in_model(model, 'snippets')
            return errors

    return model


def get_snippet_usage_url(self):
~~    return reverse('wagtailsnippets:usage', args=(
        self._meta.app_label, self._meta.model_name, quote(self.pk)))



## ... source file continues with no further reverse examples...

```

