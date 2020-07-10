title: django.shortcuts redirect Example Code
category: page
slug: django-shortcuts-redirect-examples
sortorder: 500011347
toc: False
sidebartitle: django.shortcuts redirect
meta: Python example code for the redirect callable from the django.shortcuts module of the Django project.


redirect is a callable within the django.shortcuts module of the Django project.


## Example 1 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / registration / views.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/registration/views.py)

```python
# views.py
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
~~from django.shortcuts import render, redirect

from users.models import generate_avatar
from users.forms import PersonalForm, ProfessionalForm, SubscriptionsForm

User = get_user_model()


@login_required
def personal(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = PersonalForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            profile.avatar = generate_avatar(profile)
            profile.save()
~~            return redirect('register-professional')
    else:
        form = PersonalForm(instance=profile)
    return render(request, 'registration/personal.html', {
        'form': form
    })

@login_required
def professional(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfessionalForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
~~            return redirect('register-subscriptions')
    else:
        form = ProfessionalForm(instance=profile)
    return render(request, 'registration/professional.html', {
        'form': form
    })


@login_required
def subscriptions(request):
    subscriptions = request.user.subscriptions
    if request.method == 'POST':
        form = SubscriptionsForm(request.POST, instance=subscriptions)
        if form.is_valid():
            form.save()
            request.user.has_finished_registration = True
            request.user.save()
~~            return redirect('home')
    else:
        form = SubscriptionsForm(instance=subscriptions)
    return render(request, 'registration/subscriptions.html', {
        'form': form
    })



## ... source file continues with no further redirect examples...

```


## Example 2 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / account / views.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/account/views.py)

```python
# views.py
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import (
    Http404,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
~~from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import TemplateResponseMixin, TemplateView, View
from django.views.generic.edit import FormView

from ..exceptions import ImmediateHttpResponse
from ..utils import get_form_class, get_request_param
from . import app_settings, signals
from .adapter import get_adapter
from .forms import (
    AddEmailForm,
    ChangePasswordForm,
    LoginForm,
    ResetPasswordForm,
    ResetPasswordKeyForm,
    SetPasswordForm,
    SignupForm,
    UserTokenForm,
)
from .models import EmailAddress, EmailConfirmation, EmailConfirmationHMAC
from .utils import (
    complete_signup,
    get_login_redirect_url,


## ... source file abbreviated to get to redirect examples ...


        try:
            self.object = self.get_object()
            if app_settings.CONFIRM_EMAIL_ON_GET:
                return self.post(*args, **kwargs)
        except Http404:
            self.object = None
        ctx = self.get_context_data()
        return self.render_to_response(ctx)

    def post(self, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm(self.request)
        get_adapter(self.request).add_message(
            self.request,
            messages.SUCCESS,
            'account/messages/email_confirmed.txt',
            {'email': confirmation.email_address.email})
        if app_settings.LOGIN_ON_EMAIL_CONFIRMATION:
            resp = self.login_on_confirm(confirmation)
            if resp is not None:
                return resp
        redirect_url = self.get_redirect_url()
        if not redirect_url:
            ctx = self.get_context_data()
            return self.render_to_response(ctx)
~~        return redirect(redirect_url)

    def login_on_confirm(self, confirmation):
        user_pk = None
        user_pk_str = get_adapter(self.request).unstash_user(self.request)
        if user_pk_str:
            user_pk = url_str_to_user_pk(user_pk_str)
        user = confirmation.email_address.user
        if user_pk == user.pk and self.request.user.is_anonymous:
            return perform_login(self.request,
                                 user,
                                 app_settings.EmailVerificationMethod.NONE,
                                 redirect_url=self.get_redirect_url)

        return None

    def get_object(self, queryset=None):
        key = self.kwargs['key']
        emailconfirmation = EmailConfirmationHMAC.from_key(key)
        if not emailconfirmation:
            if queryset is None:
                queryset = self.get_queryset()
            try:
                emailconfirmation = queryset.get(key=key.lower())
            except EmailConfirmation.DoesNotExist:


## ... source file abbreviated to get to redirect examples ...


        return get_form_class(app_settings.FORMS,
                              'reset_password_from_key',
                              self.form_class)

    def dispatch(self, request, uidb36, key, **kwargs):
        self.request = request
        self.key = key

        if self.key == INTERNAL_RESET_URL_KEY:
            self.key = self.request.session.get(INTERNAL_RESET_SESSION_KEY, '')
            token_form = UserTokenForm(
                data={'uidb36': uidb36, 'key': self.key})
            if token_form.is_valid():
                self.reset_user = token_form.reset_user
                return super(PasswordResetFromKeyView, self).dispatch(request,
                                                                      uidb36,
                                                                      self.key,
                                                                      **kwargs)
        else:
            token_form = UserTokenForm(
                data={'uidb36': uidb36, 'key': self.key})
            if token_form.is_valid():
                self.request.session[INTERNAL_RESET_SESSION_KEY] = self.key
                redirect_url = self.request.path.replace(
                    self.key, INTERNAL_RESET_URL_KEY)
~~                return redirect(redirect_url)

        self.reset_user = None
        response = self.render_to_response(
            self.get_context_data(token_fail=True)
        )
        return _ajax_response(self.request, response, form=token_form)

    def get_context_data(self, **kwargs):
        ret = super(PasswordResetFromKeyView, self).get_context_data(**kwargs)
        ret['action_url'] = reverse(
            'account_reset_password_from_key',
            kwargs={'uidb36': self.kwargs['uidb36'],
                    'key': self.kwargs['key']})
        return ret

    def get_form_kwargs(self):
        kwargs = super(PasswordResetFromKeyView, self).get_form_kwargs()
        kwargs["user"] = self.reset_user
        kwargs["temp_key"] = self.key
        return kwargs

    def form_valid(self, form):
        form.save()
        get_adapter(self.request).add_message(


## ... source file abbreviated to get to redirect examples ...



        return super(PasswordResetFromKeyView, self).form_valid(form)


password_reset_from_key = PasswordResetFromKeyView.as_view()


class PasswordResetFromKeyDoneView(TemplateView):
    template_name = (
        "account/password_reset_from_key_done." +
        app_settings.TEMPLATE_EXTENSION)


password_reset_from_key_done = PasswordResetFromKeyDoneView.as_view()


class LogoutView(TemplateResponseMixin, View):

    template_name = "account/logout." + app_settings.TEMPLATE_EXTENSION
    redirect_field_name = "next"

    def get(self, *args, **kwargs):
        if app_settings.LOGOUT_ON_GET:
            return self.post(*args, **kwargs)
        if not self.request.user.is_authenticated:
~~            response = redirect(self.get_redirect_url())
            return _ajax_response(self.request, response)
        ctx = self.get_context_data()
        response = self.render_to_response(ctx)
        return _ajax_response(self.request, response)

    def post(self, *args, **kwargs):
        url = self.get_redirect_url()
        if self.request.user.is_authenticated:
            self.logout()
~~        response = redirect(url)
        return _ajax_response(self.request, response)

    def logout(self):
        adapter = get_adapter(self.request)
        adapter.add_message(
            self.request,
            messages.SUCCESS,
            'account/messages/logged_out.txt')
        adapter.logout(self.request)

    def get_context_data(self, **kwargs):
        ctx = kwargs
        redirect_field_value = get_request_param(self.request,
                                                 self.redirect_field_name)
        ctx.update({
            "redirect_field_name": self.redirect_field_name,
            "redirect_field_value": redirect_field_value})
        return ctx

    def get_redirect_url(self):
        return (
            get_next_redirect_url(
                self.request,
                self.redirect_field_name) or get_adapter(


## ... source file continues with no further redirect examples...

```


## Example 3 from django-axes
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

[**django-axes / axes / helpers.py**](https://github.com/jazzband/django-axes/blob/master/axes/./helpers.py)

```python
# helpers.py
from datetime import timedelta
from hashlib import md5
from logging import getLogger
from string import Template
from typing import Callable, Optional, Type, Union
from urllib.parse import urlencode

from django.core.cache import caches, BaseCache
from django.http import HttpRequest, HttpResponse, JsonResponse, QueryDict
~~from django.shortcuts import render, redirect
from django.utils.module_loading import import_string

import ipware.ip

from axes.conf import settings
from axes.models import AccessBase

log = getLogger(__name__)


def get_cache() -> BaseCache:

    return caches[getattr(settings, "AXES_CACHE", "default")]


def get_cache_timeout() -> Optional[int]:

    cool_off = get_cool_off()
    if cool_off is None:
        return None
    return int(cool_off.total_seconds())


def get_cool_off() -> Optional[timedelta]:


## ... source file abbreviated to get to redirect examples ...


        "failure_limit": get_failure_limit(request, credentials),
        "username": get_client_username(request, credentials) or "",
    }

    cool_off = get_cool_off()
    if cool_off:
        context.update(
            {
                "cooloff_time": get_cool_off_iso8601(
                    cool_off
                ),  # differing old name is kept for backwards compatibility
                "cooloff_timedelta": cool_off,
            }
        )

    if request.is_ajax():
        return JsonResponse(context, status=status)

    if settings.AXES_LOCKOUT_TEMPLATE:
        return render(request, settings.AXES_LOCKOUT_TEMPLATE, context, status=status)

    if settings.AXES_LOCKOUT_URL:
        lockout_url = settings.AXES_LOCKOUT_URL
        query_string = urlencode({"username": context["username"]})
        url = "{}?{}".format(lockout_url, query_string)
~~        return redirect(url)

    return HttpResponse(get_lockout_message(), status=status)


def is_ip_address_in_whitelist(ip_address: str) -> bool:
    if not settings.AXES_IP_WHITELIST:
        return False

    return ip_address in settings.AXES_IP_WHITELIST


def is_ip_address_in_blacklist(ip_address: str) -> bool:
    if not settings.AXES_IP_BLACKLIST:
        return False

    return ip_address in settings.AXES_IP_BLACKLIST


def is_client_ip_address_whitelisted(request):

    if settings.AXES_NEVER_LOCKOUT_WHITELIST and is_ip_address_in_whitelist(
        request.axes_ip_address
    ):
        return True


## ... source file continues with no further redirect examples...

```


## Example 4 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / views.py**](https://github.com/divio/django-filer/blob/develop/filer/./views.py)

```python
# views.py
from __future__ import absolute_import, unicode_literals

from django.http import Http404
~~from django.shortcuts import get_object_or_404, redirect

from .models import File


def canonical(request, uploaded_at, file_id):
    filer_file = get_object_or_404(File, pk=file_id, is_public=True)
    if (not filer_file.file or int(uploaded_at) != filer_file.canonical_time):
        raise Http404('No %s matches the given query.' % File._meta.object_name)
~~    return redirect(filer_file.url)



## ... source file continues with no further redirect examples...

```


## Example 5 from django-guardian
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
~~from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, path
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


## ... source file abbreviated to get to redirect examples ...


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
            post_url = reverse('admin:index', current_app=self.admin_site.name)
~~            return redirect(post_url)

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
                url = reverse(
                    '%s:%s_%s_permissions_manage_user' % info,
                    args=[obj.pk, user_id]
                )
~~                return redirect(url)
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
                url = reverse(
                    '%s:%s_%s_permissions_manage_group' % info,
                    args=[obj.pk, group_id]
                )
~~                return redirect(url)
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
            post_url = reverse('admin:index', current_app=self.admin_site.name)
~~            return redirect(post_url)

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
            url = reverse(
                '%s:%s_%s_permissions_manage_user' % info,
                args=[obj.pk, user.pk]
            )
~~            return redirect(url)

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
~~            return redirect(post_url)

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
            url = reverse(
                '%s:%s_%s_permissions_manage_group' % info,
                args=[obj.pk, group.id]
            )
~~            return redirect(url)

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


class UserManage(forms.Form):
    user = forms.CharField(label=_("User identification"),


## ... source file continues with no further redirect examples...

```


## Example 6 from django-inline-actions
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
~~from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class ViewAction:
    inline_actions = ['view_action']

    def view_action(self, request, obj, parent_obj=None):
        url = reverse(
            'admin:{}_{}_change'.format(
                obj._meta.app_label,
                obj._meta.model_name,
            ),
            args=(obj.pk,)
        )
~~        return redirect(url)
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


class DefaultActionsMixin(ViewAction,
                          DeleteAction):
    inline_actions = []



## ... source file continues with no further redirect examples...

```


## Example 7 from django-loginas
[django-loginas](https://github.com/skorokithakis/django-loginas)
([PyPI package information](https://pypi.org/project/django-loginas/))
is [Django](/django.html) code library for admins to log into an application
as another user, typically for debugging purposes.

django-loginas is open source under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/skorokithakis/django-loginas/blob/master/LICENSE).

[**django-loginas / loginas / views.py**](https://github.com/skorokithakis/django-loginas/blob/master/loginas/./views.py)

```python
# views.py
from django.contrib import messages
from django.contrib.admin.utils import unquote
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
~~from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST

from . import settings as la_settings
from .utils import login_as, restore_original_login

try:
    from importlib import import_module
except ImportError:
    from django.utils.importlib import import_module  # type: ignore


try:
    from django.contrib.auth import get_user_model

    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User  # type: ignore


def _load_module(path):

    i = path.rfind(".")


## ... source file abbreviated to get to redirect examples ...


        can_login_as = getattr(mod, attr)
    except AttributeError:
        raise ImproperlyConfigured("Module {0} does not define a {1} " "function.".format(module, attr))
    return can_login_as


@csrf_protect
@require_POST
def user_login(request, user_id):
    user = User.objects.get(pk=unquote(user_id))

    if isinstance(la_settings.CAN_LOGIN_AS, str):
        can_login_as = _load_module(la_settings.CAN_LOGIN_AS)
    elif hasattr(la_settings.CAN_LOGIN_AS, "__call__"):
        can_login_as = la_settings.CAN_LOGIN_AS
    else:
        raise ImproperlyConfigured("The CAN_LOGIN_AS setting is neither a valid module nor callable.")
    no_permission_error = None
    try:
        if not can_login_as(request, user):
            no_permission_error = _("You do not have permission to do that.")
    except PermissionDenied as e:
        no_permission_error = str(e)
    if no_permission_error is not None:
        messages.error(request, no_permission_error, extra_tags=la_settings.MESSAGE_EXTRA_TAGS, fail_silently=True)
~~        return redirect(request.META.get("HTTP_REFERER", "/"))

    try:
        login_as(user, request)
    except ImproperlyConfigured as e:
        messages.error(request, str(e), extra_tags=la_settings.MESSAGE_EXTRA_TAGS, fail_silently=True)
~~        return redirect(request.META.get("HTTP_REFERER", "/"))

~~    return redirect(la_settings.LOGIN_REDIRECT)


def user_logout(request):
    restore_original_login(request)

~~    return redirect(la_settings.LOGOUT_REDIRECT)



## ... source file continues with no further redirect examples...

```


## Example 8 from django-wiki
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
~~from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse
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
~~        return redirect(settings.LOGIN_URL + "?next=" + request.path + qs)
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
        )


def get_article(  # noqa: max-complexity=23
    func=None,
    can_read=True,
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
~~                return redirect("wiki:root_create")
            except models.URLPath.DoesNotExist:
                try:
                    pathlist = list(filter(lambda x: x != "", path.split("/"),))
                    path = "/".join(pathlist[:-1])
                    parent = models.URLPath.get_by_path(path)
                    return HttpResponseRedirect(
                        reverse("wiki:create", kwargs={"path": parent.path})
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
                return_url = reverse("wiki:get", kwargs={"path": urlpath.parent.path})
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
~~                    return redirect("wiki:deleted", path=urlpath.path)
            else:
                if article.current_revision and article.current_revision.deleted:
~~                    return redirect("wiki:deleted", article_id=article.id)

        if article.current_revision.locked and not_locked:
            return response_forbidden(request, article, urlpath)

        if can_read and not article.can_read(request.user):
            return response_forbidden(request, article, urlpath, read_denied=True)

        if (can_write or can_create) and not article.can_write(request.user):
            return response_forbidden(request, article, urlpath)

        if can_create and not (
            request.user.is_authenticated or settings.ANONYMOUS_CREATE
        ):
            return response_forbidden(request, article, urlpath)

        if can_delete and not article.can_delete(request.user):
            return response_forbidden(request, article, urlpath)

        if can_moderate and not article.can_moderate(request.user):
            return response_forbidden(request, article, urlpath)

        kwargs["urlpath"] = urlpath

        return func(request, article, *args, **kwargs)


## ... source file continues with no further redirect examples...

```


## Example 9 from register
[register](https://github.com/ORGAN-IZE/register) is a [Django](/django.html),
[Bootstrap](/bootstrap-css.html), [PostgreSQL](/postgresql.html) project that is
open source under the
[GNU General Public License v3.0](https://github.com/ORGAN-IZE/register/blob/master/LICENSE).
This web application makes it easier for people to register as organ donors.
You can see the application live at
[https://register.organize.org/](https://register.organize.org/).

[**register / registration / middleware.py**](https://github.com/ORGAN-IZE/register/blob/master/registration/./middleware.py)

```python
# middleware.py
import django.middleware.locale
~~import django.shortcuts
from django.utils import translation
from django.utils.deprecation import MiddlewareMixin


class RequestLocaleMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == 'GET':
            language = request.GET.get('lang')
            if language:
                translation.activate(language)
                request.session[translation.LANGUAGE_SESSION_KEY] = translation.get_language()
                query = request.GET.copy()
                del query['lang']
                path = '?'.join([request.path, query.urlencode()])
~~                return django.shortcuts.redirect(path)



## ... source file continues with no further redirect examples...

```


## Example 10 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / core / views.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/core/views.py)

```python
# views.py
from django.http import Http404, HttpResponse
~~from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from wagtail.core import hooks
from wagtail.core.forms import PasswordViewRestrictionForm
from wagtail.core.models import Page, PageViewRestriction, Site


def serve(request, path):
    site = Site.find_for_request(request)
    if not site:
        raise Http404

    path_components = [component for component in path.split('/') if component]
    page, args, kwargs = site.root_page.specific.route(request, path_components)

    for fn in hooks.get_hooks('before_serve_page'):
        result = fn(page, request, args, kwargs)
        if isinstance(result, HttpResponse):
            return result

    return page.serve(request, *args, **kwargs)


def authenticate_with_password(request, page_view_restriction_id, page_id):
    restriction = get_object_or_404(PageViewRestriction, id=page_view_restriction_id)
    page = get_object_or_404(Page, id=page_id).specific

    if request.method == 'POST':
        form = PasswordViewRestrictionForm(request.POST, instance=restriction)
        if form.is_valid():
            restriction.mark_as_passed(request)

~~            return redirect(form.cleaned_data['return_url'])
    else:
        form = PasswordViewRestrictionForm(instance=restriction)

    action_url = reverse('wagtailcore_authenticate_with_password', args=[restriction.id, page.id])
    return page.serve_password_required_response(request, form, action_url)



## ... source file continues with no further redirect examples...

```

