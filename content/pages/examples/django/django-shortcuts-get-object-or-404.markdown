title: django.shortcuts get_object_or_404 Example Code
category: page
slug: django-shortcuts-get-object-or-404-examples
sortorder: 500011346
toc: False
sidebartitle: django.shortcuts get_object_or_404
meta: Python example code for the get_object_or_404 callable from the django.shortcuts module of the Django project.


get_object_or_404 is a callable within the django.shortcuts module of the Django project.


## Example 1 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / proceedings / views.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/proceedings/views.py)

```python
# views.py
from django.http import JsonResponse
~~from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST

from conferences.utilities import validate_chair_access
from proceedings.forms import UpdateVolumeForm
from proceedings.models import CameraReady


@require_POST
def update_volume(request, camera_id):
~~    camera = get_object_or_404(CameraReady, id=camera_id)
    validate_chair_access(request.user, camera.submission.conference)
    form = UpdateVolumeForm(request.POST, instance=camera)
    if form.is_valid():
        form.save()
        return JsonResponse(status=200, data={})
    return JsonResponse(status=500, data={})



## ... source file continues with no further get_object_or_404 examples...

```


## Example 2 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / admin / placeholderadmin.py**](https://github.com/divio/django-cms/blob/develop/cms/admin/placeholderadmin.py)

```python
# placeholderadmin.py
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
    HttpResponseRedirect,
)
~~from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_text
from django.utils import translation
from django.utils.translation import ugettext as _
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.http import require_POST

from six.moves.urllib.parse import parse_qsl, urlparse

from six import get_unbound_function, get_method_function

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


## ... source file abbreviated to get to get_object_or_404 examples ...


            token=token,
            origin=self._get_operation_origin(request),
            **kwargs
        )
        return token

    def _send_post_placeholder_operation(self, request, operation, token, **kwargs):
        if not request.GET.get('cms_path'):
            return

        post_placeholder_operation.send(
            sender=self.__class__,
            operation=operation,
            request=request,
            language=self._get_operation_language(request),
            token=token,
            origin=self._get_operation_origin(request),
            **kwargs
        )

    def _get_plugin_from_id(self, plugin_id):
        queryset = CMSPlugin.objects.values_list('plugin_type', flat=True)
        plugin_type = get_list_or_404(queryset, pk=plugin_id)[0]
        plugin_class = plugin_pool.get_plugin(plugin_type)
        real_queryset = plugin_class.get_render_queryset().select_related('parent', 'placeholder')
~~        return get_object_or_404(real_queryset, pk=plugin_id)

    def get_urls(self):
        info = "%s_%s" % (self.model._meta.app_label, self.model._meta.model_name)
        pat = lambda regex, fn: url(regex, self.admin_site.admin_view(fn), name='%s_%s' % (info, fn.__name__))
        url_patterns = [
            pat(r'copy-plugins/$', self.copy_plugins),
            pat(r'add-plugin/$', self.add_plugin),
            pat(r'edit-plugin/(%s)/$' % SLUG_REGEXP, self.edit_plugin),
            pat(r'delete-plugin/(%s)/$' % SLUG_REGEXP, self.delete_plugin),
            pat(r'clear-placeholder/(%s)/$' % SLUG_REGEXP, self.clear_placeholder),
            pat(r'move-plugin/$', self.move_plugin),
        ]
        return url_patterns + super(PlaceholderAdminMixin, self).get_urls()

    def has_add_plugin_permission(self, request, placeholder, plugin_type):
        return placeholder.has_add_plugin_permission(request.user, plugin_type)

    def has_change_plugin_permission(self, request, plugin):
        placeholder = plugin.placeholder
        return placeholder.has_change_plugin_permission(request.user, plugin)

    def has_delete_plugin_permission(self, request, plugin):
        placeholder = plugin.placeholder
        return placeholder.has_delete_plugin_permission(request.user, plugin)


## ... source file abbreviated to get to get_object_or_404 examples ...



        plugin = getattr(plugin_instance, 'saved_object', None)

        if plugin:
            plugin.placeholder.mark_as_dirty(plugin.language, clear_cache=False)

        if plugin_instance._operation_token:
            tree_order = placeholder.get_plugin_tree_order(plugin.parent_id)
            self._send_post_placeholder_operation(
                request,
                operation=operations.ADD_PLUGIN,
                token=plugin_instance._operation_token,
                plugin=plugin,
                placeholder=plugin.placeholder,
                tree_order=tree_order,
            )
        return response

    @method_decorator(require_POST)
    @xframe_options_sameorigin
    @transaction.atomic
    def copy_plugins(self, request):
        source_placeholder_id = request.POST['source_placeholder_id']
        target_language = request.POST['target_language']
        target_placeholder_id = request.POST['target_placeholder_id']
~~        source_placeholder = get_object_or_404(Placeholder, pk=source_placeholder_id)
~~        target_placeholder = get_object_or_404(Placeholder, pk=target_placeholder_id)

        if not target_language or not target_language in get_language_list():
            return HttpResponseBadRequest(force_text(_("Language must be set to a supported language!")))

        copy_to_clipboard = target_placeholder.pk == request.toolbar.clipboard.pk
        source_plugin_id = request.POST.get('source_plugin_id', None)

        if copy_to_clipboard and source_plugin_id:
            new_plugin = self._copy_plugin_to_clipboard(
                request,
                source_placeholder,
                target_placeholder,
            )
            new_plugins = [new_plugin]
        elif copy_to_clipboard:
            new_plugin = self._copy_placeholder_to_clipboard(
                request,
                source_placeholder,
                target_placeholder,
            )
            new_plugins = [new_plugin]
        else:
            new_plugins = self._add_plugins_from_placeholder(
                request,
                source_placeholder,
                target_placeholder,
            )
        data = get_plugin_tree_as_json(request, new_plugins)
        return HttpResponse(data, content_type='application/json')

    def _copy_plugin_to_clipboard(self, request, source_placeholder, target_placeholder):
        source_language = request.POST['source_language']
        source_plugin_id = request.POST.get('source_plugin_id')
        target_language = request.POST['target_language']

~~        source_plugin = get_object_or_404(
            CMSPlugin,
            pk=source_plugin_id,
            language=source_language,
        )

        old_plugins = (
            CMSPlugin
            .get_tree(parent=source_plugin)
            .filter(placeholder=source_placeholder)
            .order_by('path')
        )

        if not self.has_copy_plugins_permission(request, old_plugins):
            message = _('You do not have permission to copy these plugins.')
            raise PermissionDenied(force_text(message))

        target_placeholder.clear()

        plugin_pairs = copy_plugins.copy_plugins_to(
            old_plugins,
            to_placeholder=target_placeholder,
            to_language=target_language,
        )
        return plugin_pairs[0][0]


## ... source file abbreviated to get to get_object_or_404 examples ...



        if placeholder != source_placeholder:
            try:
                template = self.get_placeholder_template(request, placeholder)
                has_reached_plugin_limit(placeholder, plugin.plugin_type,
                                         target_language, template=template)
            except PluginLimitReached as er:
                return HttpResponseBadRequest(er)

        exclude_from_order_check = ['__COPY__', str(plugin.pk)]
        ordered_plugin_ids = [int(pk) for pk in order if pk not in exclude_from_order_check]
        plugins_in_tree_count = (
            placeholder
            .get_plugins(target_language)
            .filter(parent=parent_id, pk__in=ordered_plugin_ids)
            .count()
        )

        if len(ordered_plugin_ids) != plugins_in_tree_count:
            message = _('order parameter references plugins in different trees')
            return HttpResponseBadRequest(force_text(message))

        move_a_plugin = not move_a_copy and not move_to_clipboard

        if parent_id and plugin.parent_id != parent_id:
~~            target_parent = get_object_or_404(CMSPlugin, pk=parent_id)

            if move_a_plugin and target_parent.placeholder_id != placeholder.pk:
                return HttpResponseBadRequest(force_text(
                    _('parent must be in the same placeholder')))

            if move_a_plugin and target_parent.language != target_language:
                return HttpResponseBadRequest(force_text(
                    _('parent must be in the same language as '
                      'plugin_language')))
        elif parent_id:
            target_parent = plugin.parent
        else:
            target_parent = None

        new_plugin = None
        fetch_tree = False

        if move_a_copy and plugin.plugin_type == "PlaceholderPlugin":
            new_plugins = self._paste_placeholder(
                request,
                plugin=plugin,
                target_language=target_language,
                target_placeholder=placeholder,
                tree_order=order,


## ... source file abbreviated to get to get_object_or_404 examples ...


            return HttpResponseRedirect(admin_reverse('index', current_app=self.admin_site.name))

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
~~        placeholder = get_object_or_404(Placeholder, pk=placeholder_id)
        language = request.GET.get('language')

        if placeholder.pk == request.toolbar.clipboard.pk:
            placeholder.clear(language)
            return HttpResponseRedirect(admin_reverse('index', current_app=self.admin_site.name))

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


## ... source file continues with no further get_object_or_404 examples...

```


## Example 3 from django-filer
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
~~    filer_file = get_object_or_404(File, pk=file_id, is_public=True)
    if (not filer_file.file or int(uploaded_at) != filer_file.canonical_time):
        raise Http404('No %s matches the given query.' % File._meta.object_name)
    return redirect(filer_file.url)



## ... source file continues with no further get_object_or_404 examples...

```


## Example 4 from django-flexible-subscriptions
[django-flexible-subscriptions](https://github.com/studybuffalo/django-flexible-subscriptions)
([project documentation](https://django-flexible-subscriptions.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-flexible-subscriptions/))
provides boilerplate code for adding subscription and recurrent billing
to [Django](/django.html) web applications. Various payment providers
can be added on the back end to run the transactions.

The django-flexible-subscriptions project is open sourced under the
[GNU General Public License v3.0](https://github.com/studybuffalo/django-flexible-subscriptions/blob/master/LICENSE).

[**django-flexible-subscriptions / subscriptions / views.py**](https://github.com/studybuffalo/django-flexible-subscriptions/blob/master/subscriptions/./views.py)

```python
# views.py
from copy import copy

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import HiddenInput
from django.forms.models import inlineformset_factory
from django.http import HttpResponseRedirect
from django.http.response import HttpResponseNotAllowed, HttpResponseNotFound
~~from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.utils import timezone

from subscriptions import models, forms, abstract


class DashboardView(PermissionRequiredMixin, abstract.TemplateView):
    permission_required = 'subscriptions.subscriptions'
    raise_exception = True
    template_name = 'subscriptions/dashboard.html'


class TagListView(PermissionRequiredMixin, abstract.ListView):
    model = models.PlanTag
    permission_required = 'subscriptions.subscriptions'
    raise_exception = True
    context_object_name = 'tags'
    template_name = 'subscriptions/tag_list.html'


class TagCreateView(
        PermissionRequiredMixin, SuccessMessageMixin, abstract.CreateView
):


## ... source file abbreviated to get to get_object_or_404 examples ...



class PlanListDetailListView(PermissionRequiredMixin, abstract.DetailView):
    model = models.PlanList
    pk_url_kwarg = 'plan_list_id'
    permission_required = 'subscriptions.subscriptions'
    raise_exception = True
    context_object_name = 'plan_list'
    template_name = 'subscriptions/plan_list_detail_list.html'


class PlanListDetailCreateView(
        PermissionRequiredMixin, SuccessMessageMixin, abstract.CreateView
):
    model = models.PlanListDetail
    fields = [
        'plan', 'plan_list', 'html_content', 'subscribe_button_text', 'order'
    ]
    permission_required = 'subscriptions.subscriptions'
    raise_exception = True
    success_message = 'Subscription plan successfully added to plan list'
    template_name = 'subscriptions/plan_list_detail_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

~~        context['plan_list'] = get_object_or_404(
            models.PlanList, id=self.kwargs.get('plan_list_id', None)
        )

        return context

    def get_success_url(self):
        return reverse_lazy(
            'dfs_plan_list_detail_list',
            kwargs={'plan_list_id': self.kwargs['plan_list_id']},
        )


class PlanListDetailUpdateView(
        PermissionRequiredMixin, SuccessMessageMixin, abstract.UpdateView
):
    model = models.PlanListDetail
    permission_required = 'subscriptions.subscriptions'
    raise_exception = True
    fields = [
        'plan', 'plan_list', 'html_content', 'subscribe_button_text', 'order'
    ]
    success_message = 'Plan list details successfully updated'
    pk_url_kwarg = 'plan_list_detail_id'
    template_name = 'subscriptions/plan_list_detail_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

~~        context['plan_list'] = get_object_or_404(
            models.PlanList, id=self.kwargs.get('plan_list_id', None)
        )

        return context

    def get_success_url(self):
        return reverse_lazy(
            'dfs_plan_list_detail_list',
            kwargs={'plan_list_id': self.kwargs['plan_list_id']},
        )


class PlanListDetailDeleteView(PermissionRequiredMixin, abstract.DeleteView):
    model = models.PlanListDetail
    permission_required = 'subscriptions.subscriptions'
    raise_exception = True
    context_object_name = 'plan_list_detail'
    pk_url_kwarg = 'plan_list_detail_id'
    success_message = 'Subscription plan successfully removed from plan list'
    template_name = 'subscriptions/plan_list_detail_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

~~        context['plan_list'] = get_object_or_404(
            models.PlanList, id=self.kwargs.get('plan_list_id', None)
        )

        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PlanListDetailDeleteView, self).delete(
            request, *args, **kwargs
        )

    def get_success_url(self):
        return reverse_lazy(
            'dfs_plan_list_detail_list',
            kwargs={'plan_list_id': self.kwargs['plan_list_id']},
        )


class SubscribeList(abstract.TemplateView):
    context_object_name = 'plan_list'
    template_name = 'subscriptions/subscribe_list.html'

    def get(self, request, *args, **kwargs):
        plan_list = models.PlanList.objects.filter(active=True).first()


## ... source file abbreviated to get to get_object_or_404 examples ...


                self.get_context_data(plan_list=plan_list, details=details)
            )

            return response

        return HttpResponseNotFound('No subscription plans are available')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['plan_list'] = kwargs['plan_list']
        context['details'] = kwargs['details']

        return context


class SubscribeView(LoginRequiredMixin, abstract.TemplateView):
    confirmation = False
    payment_form = forms.PaymentForm
    subscription_plan = None
    success_url = 'dfs_subscribe_thank_you'
    template_preview = 'subscriptions/subscribe_preview.html'
    template_confirmation = 'subscriptions/subscribe_confirmation.html'

    def get_object(self):
~~        return get_object_or_404(
            models.SubscriptionPlan, id=self.request.POST.get('plan_id', None)
        )

    def get_context_data(self, **kwargs):
        context = super(SubscribeView, self).get_context_data(**kwargs)

        context['confirmation'] = self.confirmation

        context['plan'] = self.subscription_plan

        return context

    def get_template_names(self):
        conf_templates = [self.template_confirmation]
        prev_templates = [self.template_preview]

        return conf_templates if self.confirmation else prev_templates

    def get_success_url(self, **kwargs):
        return reverse_lazy(self.success_url, kwargs=kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])



## ... source file abbreviated to get to get_object_or_404 examples ...


        try:
            return models.SubscriptionTransaction.objects.get(
                id=self.kwargs['transaction_id'],
                user=self.request.user,
            )
        except models.SubscriptionTransaction.DoesNotExist:
            return None

    def get_context_data(self, **kwargs):
        context = super(SubscribeThankYouView, self).get_context_data(**kwargs)

        context[self.context_object_name] = self.get_object()

        return context


class SubscribeCancelView(LoginRequiredMixin, abstract.DetailView):
    model = models.UserSubscription
    context_object_name = 'subscription'
    pk_url_kwarg = 'subscription_id'
    success_message = 'Subscription successfully cancelled'
    success_url = 'dfs_subscribe_user_list'
    template_name = 'subscriptions/subscribe_cancel.html'

    def get_object(self, queryset=None):
~~        return get_object_or_404(
            self.model,
            user=self.request.user,
            id=self.kwargs['subscription_id'],
        )

    def get_success_url(self):
        return reverse_lazy(self.success_url)

    def post(self, request, *args, **kwargs):  # pylint: disable=unused-argument
        subscription = self.get_object()
        subscription.date_billing_end = copy(subscription.date_billing_next)
        subscription.date_billing_next = None
        subscription.cancelled = True
        subscription.save()

        messages.success(self.request, self.success_message)

        return HttpResponseRedirect(self.get_success_url())



## ... source file continues with no further get_object_or_404 examples...

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


## ... source file abbreviated to get to get_object_or_404 examples ...


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
            return redirect(post_url)

        from django.contrib.admin.utils import unquote
~~        obj = get_object_or_404(self.get_queryset(
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


## ... source file abbreviated to get to get_object_or_404 examples ...


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
            post_url = reverse('admin:index', current_app=self.admin_site.name)
            return redirect(post_url)

~~        user = get_object_or_404(get_user_model(), pk=user_id)
~~        obj = get_object_or_404(self.get_queryset(request), pk=object_pk)
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

~~        group = get_object_or_404(Group, id=group_id)
~~        obj = get_object_or_404(self.get_queryset(request), pk=object_pk)
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
            return redirect(url)

        context = self.get_obj_perms_base_context(request, obj)
        context['group_obj'] = group
        context['group_perms'] = get_group_perms(group, obj)
        context['form'] = form

        request.current_app = self.admin_site.name


## ... source file continues with no further get_object_or_404 examples...

```


## Example 6 from django-rest-framework
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

[**django-rest-framework / rest_framework / generics.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./generics.py)

```python
# generics.py
from django.core.exceptions import ValidationError
from django.db.models.query import QuerySet
from django.http import Http404
~~from django.shortcuts import get_object_or_404 as _get_object_or_404

from rest_framework import mixins, views
from rest_framework.settings import api_settings


~~def get_object_or_404(queryset, *filter_args, **filter_kwargs):
    try:
        return _get_object_or_404(queryset, *filter_args, **filter_kwargs)
    except (TypeError, ValueError, ValidationError):
        raise Http404


class GenericAPIView(views.APIView):
    queryset = None
    serializer_class = None

    lookup_field = 'pk'
    lookup_url_kwarg = None

    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS

    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
        return queryset

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
~~        obj = get_object_or_404(queryset, **filter_kwargs)

        self.check_object_permissions(self.request, obj)

        return obj

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def get_serializer_class(self):
        assert self.serializer_class is not None, (
            "'%s' should either include a `serializer_class` attribute, "
            "or override the `get_serializer_class()` method."
            % self.__class__.__name__
        )

        return self.serializer_class

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self


## ... source file continues with no further get_object_or_404 examples...

```


## Example 7 from django-sql-explorer
[django-sql-explorer](https://github.com/groveco/django-sql-explorer)
([PyPI page](https://pypi.org/project/django-sql-explorer/0.2/)),
also referred to as "SQL Explorer",
is a code library for the [Django](/django.html) Admin that allows
approved, authenticated users to view and execute direct database SQL
queries. The tool keeps track of executed queries so users can share them
with each other, as well as export results to downloadable formats.
django-sql-explorer is provided as open source under the
[MIT license](https://github.com/groveco/django-sql-explorer/blob/master/LICENSE).

[**django-sql-explorer / explorer / views.py**](https://github.com/groveco/django-sql-explorer/blob/master/explorer/./views.py)

```python
# views.py
import re
import six
from collections import Counter

try:
    from django.urls import reverse_lazy
except ImportError:
    from django.core.urlresolvers import reverse_lazy

import django
from django.db import DatabaseError
from django.db.models import Count
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
~~from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, DeleteView
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import LoginView

from explorer import app_settings
from explorer.connections import connections
from explorer.exporters import get_exporter_class
from explorer.forms import QueryForm
from explorer.models import Query, QueryLog, MSG_FAILED_BLACKLIST
from explorer.tasks import execute_query
from explorer.utils import (
    url_get_rows,
    url_get_query_id,
    url_get_log_id,
    url_get_params,
    safe_login_prompt,
    fmt_sql,
    allowed_query_pks,


## ... source file abbreviated to get to get_object_or_404 examples ...



def _export(request, query, download=True):
    format = request.GET.get('format', 'csv')
    exporter_class = get_exporter_class(format)
    query.params = url_get_params(request)
    delim = request.GET.get('delim')
    exporter = exporter_class(query)
    try:
        output = exporter.get_output(delim=delim)
    except DatabaseError as e:
        msg = "Error executing query %s: %s" % (query.title, e)
        return HttpResponse(msg, status=500)
    response = HttpResponse(output, content_type=exporter.content_type)
    if download:
        response['Content-Disposition'] = 'attachment; filename="%s"' % (
            exporter.get_filename()
        )
    return response


class DownloadQueryView(PermissionRequiredMixin, View):

    permission_required = 'view_permission'

    def get(self, request, query_id, *args, **kwargs):
~~        query = get_object_or_404(Query, pk=query_id)
        return _export(request, query)


class DownloadFromSqlView(PermissionRequiredMixin, View):

    permission_required = 'view_permission'

    def post(self, request, *args, **kwargs):
        sql = request.POST.get('sql')
        connection = request.POST.get('connection')
        query = Query(sql=sql, connection=connection, title='')
        ql = query.log(request.user)
        query.title = 'Playground - %s' % ql.id
        return _export(request, query)


class StreamQueryView(PermissionRequiredMixin, View):

    permission_required = 'view_permission'

    def get(self, request, query_id, *args, **kwargs):
~~        query = get_object_or_404(Query, pk=query_id)
        return _export(request, query, download=False)


class EmailCsvQueryView(PermissionRequiredMixin, View):

    permission_required = 'view_permission'

    def post(self, request, query_id, *args, **kwargs):
        if request.is_ajax():
            email = request.POST.get('email', None)
            if email:
                execute_query.delay(query_id, email)
                return JsonResponse({'message': 'message was sent successfully'})
        return JsonResponse({}, status=403)


class SchemaView(PermissionRequiredMixin, View):
    permission_required = 'change_permission'

    @method_decorator(xframe_options_sameorigin)
    def dispatch(self, *args, **kwargs):
        return super(SchemaView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):


## ... source file abbreviated to get to get_object_or_404 examples ...


class CreateQueryView(PermissionRequiredMixin, ExplorerContextMixin, CreateView):

    permission_required = 'change_permission'

    def form_valid(self, form):
        form.instance.created_by_user = self.request.user
        return super(CreateQueryView, self).form_valid(form)

    form_class = QueryForm
    template_name = 'explorer/query.html'


class DeleteQueryView(PermissionRequiredMixin, ExplorerContextMixin, DeleteView):

    permission_required = 'change_permission'
    model = Query
    success_url = reverse_lazy("explorer_index")


class PlayQueryView(PermissionRequiredMixin, ExplorerContextMixin, View):

    permission_required = 'change_permission'

    def get(self, request):
        if url_get_query_id(request):
~~            query = get_object_or_404(Query, pk=url_get_query_id(request))
            return self.render_with_sql(request, query, run_query=False)

        if url_get_log_id(request):
~~            log = get_object_or_404(QueryLog, pk=url_get_log_id(request))
            query = Query(sql=log.sql, title="Playground", connection=log.connection)
            return self.render_with_sql(request, query)

        return self.render()

    def post(self, request):
        sql = request.POST.get('sql')
        show = url_get_show(request)
        query = Query(sql=sql, title="Playground", connection=request.POST.get('connection'))
        passes_blacklist, failing_words = query.passes_blacklist()
        error = MSG_FAILED_BLACKLIST % ', '.join(failing_words) if not passes_blacklist else None
        run_query = not bool(error) if show else False
        return self.render_with_sql(request, query, run_query=run_query, error=error)

    def render(self):
        return self.render_template('explorer/play.html', {'title': 'Playground', 'form': QueryForm()})

    def render_with_sql(self, request, query, run_query=True, error=None):
        rows = url_get_rows(request)
        fullscreen = url_get_fullscreen(request)
        template = 'fullscreen' if fullscreen else 'play'
        form = QueryForm(request.POST if len(request.POST) else None, instance=query)
        return self.render_template('explorer/%s.html' % template, query_viewmodel(request.user,
                                                                                   query,


## ... source file abbreviated to get to get_object_or_404 examples ...


        show = url_get_show(request)
        rows = url_get_rows(request)
        vm = query_viewmodel(request.user, query, form=form, run_query=show, rows=rows)
        fullscreen = url_get_fullscreen(request)
        template = 'fullscreen' if fullscreen else 'query'
        return self.render_template('explorer/%s.html' % template, vm)

    def post(self, request, query_id):
        if not app_settings.EXPLORER_PERMISSION_CHANGE(request.user):
            return HttpResponseRedirect(
                reverse_lazy('query_detail', kwargs={'query_id': query_id})
            )
        show = url_get_show(request)
        query, form = QueryView.get_instance_and_form(request, query_id)
        success = form.is_valid() and form.save()
        vm = query_viewmodel(request.user,
                             query,
                             form=form,
                             run_query=show,
                             rows=url_get_rows(request),
                             message="Query saved." if success else None)
        return self.render_template('explorer/query.html', vm)

    @staticmethod
    def get_instance_and_form(request, query_id):
~~        query = get_object_or_404(Query, pk=query_id)
        query.params = url_get_params(request)
        form = QueryForm(request.POST if len(request.POST) else None, instance=query)
        return query, form


def query_viewmodel(user, query, title=None, form=None, message=None, run_query=True, error=None, rows=app_settings.EXPLORER_DEFAULT_ROWS):
    res = None
    ql = None
    if run_query:
        try:
            res, ql = query.execute_with_logging(user)
        except DatabaseError as e:
            error = str(e)
    has_valid_results = not error and res and run_query
    ret = {
        'tasks_enabled': app_settings.ENABLE_TASKS,
        'params': query.available_params(),
        'title': title,
        'shared': query.shared,
        'query': query,
        'form': form,
        'message': message,
        'error': error,
        'rows': rows,


## ... source file continues with no further get_object_or_404 examples...

```


## Example 8 from django-taggit
[django-taggit](https://github.com/jazzband/django-taggit/)
([PyPI page](https://pypi.org/project/django-taggit/)) provides a way
to create, store, manage and use tags in a [Django](/django.html) project.
The code for django-taggit is
[open source](https://github.com/jazzband/django-taggit/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-taggit / taggit / views.py**](https://github.com/jazzband/django-taggit/blob/master/taggit/views.py)

```python
# views.py
from django.contrib.contenttypes.models import ContentType
~~from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView

from taggit.models import Tag, TaggedItem


def tagged_object_list(request, slug, queryset, **kwargs):
    if callable(queryset):
        queryset = queryset()
    kwargs["slug"] = slug
    tag_list_view = type(
        "TagListView",
        (TagListMixin, ListView),
        {"model": queryset.model, "queryset": queryset},
    )
    return tag_list_view.as_view()(request, **kwargs)


class TagListMixin:
    tag_suffix = "_tag"

    def dispatch(self, request, *args, **kwargs):
        slug = kwargs.pop("slug")
~~        self.tag = get_object_or_404(Tag, slug=slug)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(
            pk__in=TaggedItem.objects.filter(
                tag=self.tag, content_type=ContentType.objects.get_for_model(qs.model)
            ).values_list("object_id", flat=True)
        )

    def get_template_names(self):
        if self.tag_suffix:
            self.template_name_suffix = self.tag_suffix + self.template_name_suffix
        return super().get_template_names()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "extra_context" not in context:
            context["extra_context"] = {}
        context["extra_context"]["tag"] = self.tag
        return context



## ... source file continues with no further get_object_or_404 examples...

```


## Example 9 from django-wiki
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
__all__ = [
    "UserCreationForm",
    "UserUpdateForm",
    "WikiSlugField",
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
~~from django.shortcuts import get_object_or_404
from django.urls import Resolver404, resolve
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.translation import gettext, gettext_lazy as _, pgettext_lazy
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


## ... source file abbreviated to get to get_object_or_404 examples ...


        ),
    )
    content = forms.CharField(
        label=_("Type in some contents"),
        help_text=_(
            "This is just the initial contents of your article. After creating it, you can use more complex features like adding plugins, meta data, related articles etc..."
        ),
        required=False,
        widget=getEditor().get_widget(),
    )  # @UndefinedVariable


class MoveForm(forms.Form):

    destination = forms.CharField(label=_("Destination"))
    slug = WikiSlugField(max_length=models.URLPath.SLUG_MAX_LENGTH)
    redirect = forms.BooleanField(
        label=_("Redirect pages"),
        help_text=_("Create a redirect page for every moved article?"),
        required=False,
    )

    def clean(self):
        cd = super().clean()
        if cd.get("slug"):
~~            dest_path = get_object_or_404(
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
        label=pgettext_lazy("Revision comment", "Summary"),
        help_text=_(
            "Give a short reason for your edit, which will be stated in the revision log."
        ),
        required=False,
    )

    current_revision = forms.IntegerField(required=False, widget=forms.HiddenInput())

    def __init__(self, request, current_revision, *args, **kwargs):


## ... source file continues with no further get_object_or_404 examples...

```


## Example 10 from gadget-board
[gadget-board](https://github.com/mik4el/gadget-board) is a
[Django](/django.html),
[Django REST Framework (DRF)](/django-rest-framework-drf.html) and
[Angular](/angular.html) web application that is open source under the
[Apache2 license](https://github.com/mik4el/gadget-board/blob/master/LICENSE).

[**gadget-board / web / gadgets / permissions.py**](https://github.com/mik4el/gadget-board/blob/master/web/gadgets/permissions.py)

```python
# permissions.py
from rest_framework import permissions
~~from django.shortcuts import get_object_or_404
from .models import Gadget


class CanUserAddGadgetData(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == "POST":
            if request.user.is_authenticated:
~~                gadget = get_object_or_404(Gadget, slug=view.kwargs['gadget_slug'])
                if request.user in gadget.users_can_upload.all():
                    return True
        return False

    def has_object_permission(self, request, view, obj):
        return False



## ... source file continues with no further get_object_or_404 examples...

```


## Example 11 from wagtail
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
~~    restriction = get_object_or_404(PageViewRestriction, id=page_view_restriction_id)
~~    page = get_object_or_404(Page, id=page_id).specific

    if request.method == 'POST':
        form = PasswordViewRestrictionForm(request.POST, instance=restriction)
        if form.is_valid():
            restriction.mark_as_passed(request)

            return redirect(form.cleaned_data['return_url'])
    else:
        form = PasswordViewRestrictionForm(instance=restriction)

    action_url = reverse('wagtailcore_authenticate_with_password', args=[restriction.id, page.id])
    return page.serve_password_required_response(request, form, action_url)



## ... source file continues with no further get_object_or_404 examples...

```

