title: django.http HttpResponseRedirect Python Code Examples
category: page
slug: django-http-httpresponseredirect-examples
sortorder: 500013470
toc: False
sidebartitle: django.http HttpResponseRedirect
meta: Example Python code for using the HttpResponseRedirect object provided by Django in the django.http module.


[HttpResponseRedirect](https://docs.djangoproject.com/en/stable/ref/request-response/#django.http.HttpResponseRedirect)
is a subclass of
[HttpResponse](/django-http-httpresponse-examples.html)
([source code](https://github.com/django/django/blob/master/django/http/response.py))
in the [Django](/django.html) [web framework](/web-frameworks.html) that 
returns the 
[HTTP 302 status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/302),
indicating the URL resource was found but temporarily moved to a different
URL. This class is most frequently used as a return object from a 
Django view.

Use the 
[HttpResponsePermanentRedirect](/django-http-responses-httpresponsepermanentredirect-examples.html) 
response object if you instead want to return a 301 *permanent*
redirect to a new URL.


## Example 1 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / socialaccount / helpers.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/socialaccount/helpers.py)

```python
from django.contrib import messages
from django.forms import ValidationError
~~from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from allauth.account import app_settings as account_settings
from allauth.account.adapter import get_adapter as get_account_adapter
from allauth.account.utils import complete_signup, perform_login, user_username
from allauth.exceptions import ImmediateHttpResponse

from . import app_settings, signals
from .adapter import get_adapter
from .models import SocialLogin
from .providers.base import AuthError, AuthProcess


def _process_signup(request, sociallogin):
    auto_signup = get_adapter(request).is_auto_signup_allowed(
        request,
        sociallogin)
~~    if not auto_signup:
~~        request.session['socialaccount_sociallogin'] = sociallogin.serialize()
~~        url = reverse('socialaccount_signup')
~~        ret = HttpResponseRedirect(url)
    else:
        # Ok, auto signup it is, at least the e-mail address is ok.
        # We still need to check the username though...
        if account_settings.USER_MODEL_USERNAME_FIELD:
            username = user_username(sociallogin.user)
            try:
                get_account_adapter(request).clean_username(username)
            except ValidationError:
                # This username is no good ...
                user_username(sociallogin.user, '')
        # FIXME: This part contains a lot of duplication of logic
        # ("closed" rendering, create user, send email, in active
        # etc..)
        if not get_adapter(request).is_open_for_signup(
                request,
                sociallogin):
            return render(
                request,
                "account/signup_closed." +
                account_settings.TEMPLATE_EXTENSION)
        get_adapter(request).save_user(request, sociallogin, form=None)
        ret = complete_social_signup(request, sociallogin)
    return ret


def _login_social_account(request, sociallogin):
    return perform_login(request, sociallogin.user,
                         email_verification=app_settings.EMAIL_VERIFICATION,
                         redirect_url=sociallogin.get_redirect_url(request),
                         signal_kwargs={"sociallogin": sociallogin})


def render_authentication_error(request,
                                provider_id,
                                error=AuthError.UNKNOWN,
                                exception=None,
                                extra_context=None):
~~    try:
~~        if extra_context is None:
~~            extra_context = {}
~~        get_adapter(request).authentication_error(
~~            request,
~~            provider_id,
~~            error=error,
~~            exception=exception,
~~            extra_context=extra_context)
~~    except ImmediateHttpResponse as e:
~~        return e.response
~~    if error == AuthError.CANCELLED:
~~        return HttpResponseRedirect(reverse('socialaccount_login_cancelled'))
    context = {
        'auth_error': {
            'provider': provider_id,
            'code': error,
            'exception': exception
        }
    }
    context.update(extra_context)
    return render(
        request,
        "socialaccount/authentication_error." +
        account_settings.TEMPLATE_EXTENSION,
        context
    )


def _add_social_account(request, sociallogin):
~~    if request.user.is_anonymous:
~~        # This should not happen. Simply redirect to the connections
~~        # view (which has a login required)
~~        return HttpResponseRedirect(reverse('socialaccount_connections'))
    level = messages.INFO
    message = 'socialaccount/messages/account_connected.txt'
    action = None
    if sociallogin.is_existing:
        if sociallogin.user != request.user:
            # Social account of other user. For now, this scenario
            # is not supported. Issue is that one cannot simply
            # remove the social account from the other user, as
            # that may render the account unusable.
            level = messages.ERROR
            message = 'socialaccount/messages/account_connected_other.txt'
        else:
            # This account is already connected -- we give the opportunity
            # for customized behaviour through use of a signal.
            action = 'updated'
            message = 'socialaccount/messages/account_connected_updated.txt'
            signals.social_account_updated.send(
                sender=SocialLogin,
                request=request,
                sociallogin=sociallogin)
    else:
        # New account, let's connect
        action = 'added'
        sociallogin.connect(request, request.user)
        signals.social_account_added.send(sender=SocialLogin,
                                          request=request,
                                          sociallogin=sociallogin)
    default_next = get_adapter(request).get_connect_redirect_url(
        request,
        sociallogin.account)
    next_url = sociallogin.get_redirect_url(request) or default_next
    get_account_adapter(request).add_message(
        request, level, message,
        message_context={
            'sociallogin': sociallogin,
            'action': action
        }
    )
~~    return HttpResponseRedirect(next_url)


def complete_social_login(request, sociallogin):
    assert not sociallogin.is_existing
    sociallogin.lookup()
    try:
        get_adapter(request).pre_social_login(request, sociallogin)
        signals.pre_social_login.send(sender=SocialLogin,
                                      request=request,
                                      sociallogin=sociallogin)
        process = sociallogin.state.get('process')
        if process == AuthProcess.REDIRECT:
            return _social_login_redirect(request, sociallogin)
        elif process == AuthProcess.CONNECT:
            return _add_social_account(request, sociallogin)
        else:
            return _complete_social_login(request, sociallogin)
    except ImmediateHttpResponse as e:
        return e.response


def _social_login_redirect(request, sociallogin):
    next_url = sociallogin.get_redirect_url(request) or '/'
~~    return HttpResponseRedirect(next_url)


def _complete_social_login(request, sociallogin):
    if request.user.is_authenticated:
        get_account_adapter(request).logout(request)
    if sociallogin.is_existing:
        # Login existing user
        ret = _login_social_account(request, sociallogin)
        signals.social_account_updated.send(
            sender=SocialLogin,
            request=request,
            sociallogin=sociallogin)
    else:
        # New social user
        ret = _process_signup(request, sociallogin)
    return ret


def complete_social_signup(request, sociallogin):
    return complete_signup(request,
                           sociallogin.user,
                           app_settings.EMAIL_VERIFICATION,
                           sociallogin.get_redirect_url(request),
                           signal_kwargs={'sociallogin': sociallogin})


# TODO: Factor out callable importing functionality
# See: account.utils.user_display
def import_path(path):
    modname, _, attr = path.rpartition('.')
    m = __import__(modname, fromlist=[attr])
    return getattr(m, attr)

```


## Example 2 from django-axes
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

[**django-axes / axes / tests / test_utils.py**](https://github.com/jazzband/django-axes/blob/master/axes/tests/test_utils.py)

```python
from datetime import timedelta
from hashlib import md5
from unittest.mock import patch

~~from django.http import (JsonResponse, HttpResponseRedirect, 
~~                         HttpResponse, HttpRequest)
from django.test import override_settings, RequestFactory

from axes.apps import AppConfig
from axes.models import AccessAttempt
from axes.tests.base import AxesTestCase
from axes.helpers import (
    get_cache_timeout,
    get_client_str,
    get_client_username,
    get_client_cache_key,
    get_client_parameters,
    get_cool_off_iso8601,
    get_lockout_response,
    is_client_ip_address_blacklisted,
    is_client_ip_address_whitelisted,
    is_ip_address_in_blacklist,
    is_ip_address_in_whitelist,
    is_client_method_whitelisted,
    toggleable,
)


## ... source code abbreviated to get to the example ...


class LockoutResponseTestCase(AxesTestCase):
    def setUp(self):
        self.request = HttpRequest()

    @override_settings(AXES_COOLOFF_TIME=42)
    def test_get_lockout_response_cool_off(self):
        get_lockout_response(request=self.request)

    @override_settings(AXES_LOCKOUT_TEMPLATE='example.html')
    @patch('axes.helpers.render')
    def test_get_lockout_response_lockout_template(self, render):
        self.assertFalse(render.called)
        get_lockout_response(request=self.request)
        self.assertTrue(render.called)

~~    @override_settings(AXES_LOCKOUT_URL='https://example.com')
~~    def test_get_lockout_response_lockout_url(self):
~~        response = get_lockout_response(request=self.request)
~~        self.assertEqual(type(response), HttpResponseRedirect)

    def test_get_lockout_response_lockout_json(self):
        self.request.is_ajax = lambda: True
        response = get_lockout_response(request=self.request)
        self.assertEqual(type(response), JsonResponse)

    def test_get_lockout_response_lockout_response(self):
        response = get_lockout_response(request=self.request)
        self.assertEqual(type(response), HttpResponse)

```


## Example 3 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / admin / placeholderadmin.py**](https://github.com/divio/django-cms/blob/develop/cms/admin/placeholderadmin.py)

```python
# -*- coding: utf-8 -*-
import uuid
import warnings

from django.conf.urls import url
from django.contrib.admin.helpers import AdminForm
from django.contrib.admin.utils import get_deleted_objects
from django.core.exceptions import PermissionDenied
from django.db import router, transaction
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    HttpResponseNotFound,
~~    HttpResponseRedirect,
)
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template.response import TemplateResponse
from django.utils import six
from django.utils.six.moves.urllib.parse import parse_qsl, urlparse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_text
from django.utils import translation
from django.utils.translation import ugettext as _
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.http import require_POST

from cms import operations
from cms.admin.forms import PluginAddValidationForm
from cms.constants import SLUG_REGEXP
from cms.exceptions import PluginLimitReached
from cms.models.placeholdermodel import Placeholder
from cms.models.placeholderpluginmodel import PlaceholderReference
from cms.models.pluginmodel import CMSPlugin
from cms.plugin_pool import plugin_pool
from cms.signals import pre_placeholder_operation, post_placeholder_operation
from cms.toolbar.utils import get_plugin_tree_as_json
from cms.utils import copy_plugins, get_current_site
from cms.utils.compat import DJANGO_2_0
from cms.utils.conf import get_cms_setting
from cms.utils.i18n import get_language_code, get_language_list
from cms.utils.plugins import has_reached_plugin_limit, reorder_plugins
from cms.utils.urlutils import admin_reverse


## ... source code abbreviated to get to the examples ...


    @xframe_options_sameorigin
    def delete_plugin(self, request, plugin_id):
        plugin = self._get_plugin_from_id(plugin_id)

        if not self.has_delete_plugin_permission(request, plugin):
            return HttpResponseForbidden(force_text(
                _("You do not have permission to delete this plugin")))

        opts = plugin._meta
        using = router.db_for_write(opts.model)
        if DJANGO_2_0:
            get_deleted_objects_additional_kwargs = {
                'opts': opts,
                'using': using,
                'user': request.user,
            }
        else:
            get_deleted_objects_additional_kwargs = {'request': request}
        deleted_objects, __, perms_needed, protected = get_deleted_objects(
            [plugin], admin_site=self.admin_site,
            **get_deleted_objects_additional_kwargs
        )

        if request.POST:  # The user has already confirmed the deletion.
            if perms_needed:
                raise PermissionDenied(_("You do not have permission to delete this plugin"))
            obj_display = force_text(plugin)
            placeholder = plugin.placeholder
            plugin_tree_order = placeholder.get_plugin_tree_order(
                language=plugin.language,
                parent_id=plugin.parent_id,
            )

            operation_token = self._send_pre_placeholder_operation(
                request,
                operation=operations.DELETE_PLUGIN,
                plugin=plugin,
                placeholder=placeholder,
                tree_order=plugin_tree_order,
            )

            plugin.delete()
            placeholder.mark_as_dirty(plugin.language, clear_cache=False)
            reorder_plugins(
                placeholder=placeholder,
                parent_id=plugin.parent_id,
                language=plugin.language,
            )

            self.log_deletion(request, plugin, obj_display)
            self.message_user(request, _('The %(name)s plugin "%(obj)s" was deleted successfully.') % {
                'name': force_text(opts.verbose_name), 'obj': force_text(obj_display)})

            # Avoid query by removing the plugin being deleted
            # from the tree order list
            new_plugin_tree_order = list(plugin_tree_order)
            new_plugin_tree_order.remove(plugin.pk)

            self._send_post_placeholder_operation(
                request,
                operation=operations.DELETE_PLUGIN,
                token=operation_token,
                plugin=plugin,
                placeholder=placeholder,
                tree_order=new_plugin_tree_order,
            )
~~            return HttpResponseRedirect( \
~~                       admin_reverse('index', 
~~                                     current_app=self.admin_site.name))

        plugin_name = force_text(plugin.get_plugin_class().name)

        if perms_needed or protected:
            title = _("Cannot delete %(name)s") % {"name": plugin_name}
        else:
            title = _("Are you sure?")
        context = {
            "title": title,
            "object_name": plugin_name,
            "object": plugin,
            "deleted_objects": deleted_objects,
            "perms_lacking": perms_needed,
            "protected": protected,
            "opts": opts,
            "app_label": opts.app_label,
        }
        request.current_app = self.admin_site.name
        return TemplateResponse(
            request, "admin/cms/page/plugin/delete_confirmation.html", context
        )

    @xframe_options_sameorigin
    def clear_placeholder(self, request, placeholder_id):
        placeholder = get_object_or_404(Placeholder, pk=placeholder_id)
        language = request.GET.get('language')

        if placeholder.pk == request.toolbar.clipboard.pk:
            # User is clearing the clipboard, no need for permission
            # checks here as the clipboard is unique per user.
            # There could be a case where a plugin has relationship to
            # an object the user does not have permission to delete.
            placeholder.clear(language)
~~            return HttpResponseRedirect( \
~~                       admin_reverse('index', 
~~                                      current_app=self.admin_site.name))

        if not self.has_clear_placeholder_permission(request, placeholder, language):
            return HttpResponseForbidden(force_text(_("You do not have permission to clear this placeholder")))

        opts = Placeholder._meta
        using = router.db_for_write(Placeholder)
        plugins = placeholder.get_plugins_list(language)

        if DJANGO_2_0:
            get_deleted_objects_additional_kwargs = {
                'opts': opts,
                'using': using,
                'user': request.user,
            }
        else:
            get_deleted_objects_additional_kwargs = {'request': request}
        deleted_objects, __, perms_needed, protected = get_deleted_objects(
            plugins, admin_site=self.admin_site,
            **get_deleted_objects_additional_kwargs
        )

        obj_display = force_text(placeholder)

        if request.POST:
            # The user has already confirmed the deletion.
            if perms_needed:
                return HttpResponseForbidden(force_text(_("You do not have permission to clear this placeholder")))

            operation_token = self._send_pre_placeholder_operation(
                request,
                operation=operations.CLEAR_PLACEHOLDER,
                plugins=plugins,
                placeholder=placeholder,
            )

            placeholder.clear(language)
            placeholder.mark_as_dirty(language, clear_cache=False)

            self.log_deletion(request, placeholder, obj_display)
            self.message_user(request, _('The placeholder "%(obj)s" was cleared successfully.') % {
                'obj': obj_display})

            self._send_post_placeholder_operation(
                request,
                operation=operations.CLEAR_PLACEHOLDER,
                token=operation_token,
                plugins=plugins,
                placeholder=placeholder,
            )
~~            return HttpResponseRedirect( \
~~                         admin_reverse('index', 
~~                                       current_app=self.admin_site.name))

        if perms_needed or protected:
            title = _("Cannot delete %(name)s") % {"name": obj_display}
        else:
            title = _("Are you sure?")

        context = {
            "title": title,
            "object_name": _("placeholder"),
            "object": placeholder,
            "deleted_objects": deleted_objects,
            "perms_lacking": perms_needed,
            "protected": protected,
            "opts": opts,
            "app_label": opts.app_label,
        }
        request.current_app = self.admin_site.name
        return TemplateResponse(request, "admin/cms/page/plugin/delete_confirmation.html", context)

```


## Example 4 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / admin / fileadmin.py**](https://github.com/divio/django-filer/blob/develop/filer/admin/fileadmin.py)

```python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django import forms
from django.contrib.admin.utils import unquote
~~from django.http import HttpResponseRedirect
from django.urls import reverse
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

    @classmethod
    def build_fieldsets(cls, extra_main_fields=(), extra_advanced_fields=(),
                        extra_fieldsets=()):
        fieldsets = (
            (None, {
                'fields': (
                    'name',
                    'owner',
                    'description',
                ) + extra_main_fields,
            }),
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
        """
        Overrides the default to be able to forward to the directory listing
        instead of the default change_list_view
        """
        if (
            request.POST
            and '_continue' not in request.POST
            and '_saveasnew' not in request.POST
            and '_addanother' not in request.POST
        ):
            # Popup in pick mode or normal mode. In both cases we want to go
            # back to the folder list view after save. And not the useless file
            # list view.
            if obj.folder:
                url = reverse('admin:filer-directory_listing',
                              kwargs={'folder_id': obj.folder.id})
            else:
                url = reverse(
                    'admin:filer-directory_listing-unfiled_images')
            url = "{0}{1}".format(
                url,
                admin_url_params_encoded(request),
            )
~~            return HttpResponseRedirect(url)
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
        """
        Overrides the default to enable redirecting to the directory view after
        deletion of a image.

        we need to fetch the object and find out who the parent is
        before super, because super will delete the object and make it
        impossible to find out the parent folder to redirect to.
        """
        try:
            obj = self.get_queryset(request).get(pk=unquote(object_id))
            parent_folder = obj.folder
        except self.model.DoesNotExist:
            parent_folder = None

        if request.POST:
            # Return to folder listing, since there is no usable file listing.
            super(FileAdmin, self).delete_view(
                request=request, object_id=object_id,
                extra_context=extra_context)
            if parent_folder:
                url = reverse('admin:filer-directory_listing',
                              kwargs={'folder_id': parent_folder.id})
            else:
                url = reverse('admin:filer-directory_listing-unfiled_images')
            url = "{0}{1}".format(
                url,
                admin_url_params_encoded(request)
            )
~~            return HttpResponseRedirect(url)

        return super(FileAdmin, self).delete_view(
            request=request, object_id=object_id,
            extra_context=extra_context)

    def get_model_perms(self, request):
        """
        It seems this is only used for the list view. NICE :-)
        """
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
    display_canonical.short_description = _('canonical URL')


FileAdmin.fieldsets = FileAdmin.build_fieldsets()

```


## Example 5 from django-jet
[django-jet](https://github.com/geex-arts/django-jet)
([project documentation](https://jet.readthedocs.io/en/latest/),
[PyPI project page](https://pypi.org/project/django-jet/) and
[more information](http://jet.geex-arts.com/))
is a fancy [Django](/django.html) Admin panel replacement.

The django-jet project is open source under the
[GNU Affero General Public License v3.0](https://github.com/geex-arts/django-jet/blob/dev/LICENSE).

[**django-jet / jet / dashboard / views.py**](https://github.com/geex-arts/django-jet/blob/dev/jet/dashboard/views.py)

```python
from django.contrib import messages
from django.core.exceptions import ValidationError
try:
    from django.core.urlresolvers import reverse
except ImportError: # Django 1.11
    from django.urls import reverse

from django.forms.formsets import formset_factory
~~from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST, require_GET
from jet.dashboard.forms import UpdateDashboardModulesForm, AddUserDashboardModuleForm, \
    UpdateDashboardModuleCollapseForm, RemoveDashboardModuleForm, ResetDashboardForm
from jet.dashboard.models import UserDashboardModule
from jet.utils import JsonResponse, get_app_list, SuccessMessageMixin, user_is_authenticated
from django.views.generic import UpdateView
from django.utils.translation import ugettext_lazy as _


class UpdateDashboardModuleView(SuccessMessageMixin, UpdateView):
    model = UserDashboardModule
    fields = ('title',)
    template_name = 'jet.dashboard/update_module.html'
    success_message = _('Widget was successfully updated')
    object = None
    module = None

    def has_permission(self, request):
        return request.user.is_active and request.user.is_staff

    def get_success_url(self):
        if self.object.app_label:
            return reverse('admin:app_list', kwargs={'app_label': self.object.app_label})
        else:
            return reverse('admin:index')

    def get_module(self):
        object = self.object if getattr(self, 'object', None) is not None else self.get_object()
        return object.load_module()

    def get_settings_form_kwargs(self):
        kwargs = {
            'initial': self.module.settings
        }

        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def get_settings_form(self):
        if self.module.settings_form:
            form = self.module.settings_form(**self.get_settings_form_kwargs())
            if hasattr(form, 'set_module'):
                form.set_module(self.module)
            return form

    def get_children_formset_kwargs(self):
        kwargs = {
            'initial': self.module.children,
            'prefix': 'children',
        }

        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def get_children_formset(self):
        if self.module.child_form:
            return formset_factory(self.module.child_form, can_delete=True, extra=1)(**self.get_children_formset_kwargs())

    def clean_children_data(self, children):
        children = list(filter(
            lambda item: isinstance(item, dict) and item and item.get('DELETE') is not True,
            children
        ))
        for item in children:
            item.pop('DELETE')
        return children

    def get_current_app(self):
        app_list = get_app_list({'request': self.request})

        for app in app_list:
            if app.get('app_label', app.get('name')) == self.object.app_label:
                return app

    def get_context_data(self, **kwargs):
        data = super(UpdateDashboardModuleView, self).get_context_data(**kwargs)
        data['title'] = _('Change')
        data['module'] = self.module
        data['settings_form'] = self.get_settings_form()
        data['children_formset'] = self.get_children_formset()
        data['child_name'] = self.module.child_name if self.module.child_name else _('Items')
        data['child_name_plural'] = self.module.child_name_plural if self.module.child_name_plural else _('Items')
        data['app'] = self.get_current_app()
        return data

~~    def dispatch(self, request, *args, **kwargs):
~~        if not self.has_permission(request):
~~            index_path = reverse('admin:index')
~~            return HttpResponseRedirect(index_path)

        self.object = self.get_object()
        self.module = self.get_module()(model=self.object)
        return super(UpdateDashboardModuleView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        settings_form = self.get_settings_form()
        children_formset = self.get_children_formset()

        data = request.POST.copy()

        if settings_form:
            if settings_form.is_valid():
                settings = settings_form.cleaned_data
                data['settings'] = self.module.dump_settings(settings)
            else:
                return self.form_invalid(self.get_form(self.get_form_class()))

        if children_formset:
            if children_formset.is_valid():
                self.module.children = self.clean_children_data(children_formset.cleaned_data)
                data['children'] = self.module.dump_children()
            else:
                return self.form_invalid(self.get_form(self.get_form_class()))

        request.POST = data

        return super(UpdateDashboardModuleView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        if 'settings' in form.data:
            form.instance.settings = form.data['settings']
        if 'children' in form.data:
            form.instance.children = form.data['children']
        return super(UpdateDashboardModuleView, self).form_valid(form)

## ... source code continues with no further HttpResponseRedirect examples ...
```

