title: django.http HttpResponseForbidden Python Code Examples
category: page
slug: django-http-httpresponseforbidden-examples
sortorder: 500013440
toc: False
sidebartitle: django.http HttpResponseForbidden
meta: Example Python code for using the HttpResponseForbidden object provided by Django in the django.http module.


[HttpResponseForbidden](https://docs.djangoproject.com/en/stable/ref/request-response/#django.http.HttpResponseForbidden)
([source code](https://github.com/django/django/blob/master/django/http/response.py))
returns the 403 status code to an inbound HTTP request in a 
[Django](/django.html) web application. You would most likely use the
HttpResponseForbidden class if a user fails a security check on a view
because they do not have access to some data or part of a secured
application.


## Example 1 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / submissions / views.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/submissions/views.py)

```python
import mimetypes

from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
~~from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_GET

from conferences.models import Conference
from submissions.forms import CreateSubmissionForm, SubmissionDetailsForm, \
    AuthorCreateForm, AuthorsReorderForm, AuthorDeleteForm, \
    UploadReviewManuscriptForm, InviteAuthorForm
from submissions.models import Submission, Author


def _create_submission(request, form):
    if request.method == 'POST':
        if form.is_valid():
            submission = form.save()

            # Set creator and create first author:
            submission.created_by = request.user
            submission.save()
            Author.objects.create(
                submission=submission,
                order=1,
                user=request.user
            )

            messages.success(request, f'Created submission #{submission.pk}')
            return redirect('submissions:details', pk=submission.pk)

    return render(request, 'submissions/create.html', {
        'form': form,
    })


@login_required
def create_submission(request):
    if request.method == 'POST':
        form = CreateSubmissionForm(request.POST)
    else:
        form = CreateSubmissionForm()
    return _create_submission(request, form)


@login_required
def create_submission_for(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    if request.method == 'POST':
        form = CreateSubmissionForm(request.POST)
    else:
        form = CreateSubmissionForm(initial={'conference': conference.pk})
    return _create_submission(request, form)


@login_required
def submission_details(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    if submission.is_viewable_by(request.user):
        if request.method == 'POST':
            if submission.details_editable_by(request.user):
                form = SubmissionDetailsForm(request.POST, instance=submission)
                if form.is_valid():
                    form.save()
                    if submission.reached_overview:
                        return redirect('submissions:overview', pk=pk)
                    return redirect('submissions:authors', pk=pk)
            else:
~~                return HttpResponseForbidden()
        else:
            form = SubmissionDetailsForm(instance=submission)
        return render(request, 'submissions/details.html', {
            'submission': submission,
            'form': form,
        })
~~    return HttpResponseForbidden()


@login_required
def submission_authors(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    if submission.is_viewable_by(request.user):
        return render(request, 'submissions/authors.html', {
            'submission': submission,
        })
~~    return HttpResponseForbidden()


@login_required
def edit_manuscript(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    if submission.is_viewable_by(request.user):
        if request.method == 'POST':
            if submission.review_manuscript_editable_by(request.user):
                form = UploadReviewManuscriptForm(
                    request.POST,
                    request.FILES,
                    instance=submission
                )
                # We save current file (if any) for two reasons:
                # 1) if this file is not empty and user uploaded a new file, we
                #    are going to delete this old file (in case of valid form);
                #    and
                # 2) it is going to be assigned instead of TemporaryUploadedFile
                #    object in case of form validation error.
                old_file = (submission.review_manuscript.file
                            if submission.review_manuscript else None)
                if form.is_valid():
                    # If the form is valid and user provided a new file, we
                    # delete original file first. Otherwise Django will add a
                    # random suffix which will break our storage strategy.
                    if old_file and request.FILES:
                        submission.review_manuscript.storage.delete(
                            old_file.name
                        )
                    form.save()
                    return redirect('submissions:overview', pk=pk)
                else:
                    # If the form is invalid (e.g. title is not provided),
                    # but the user tried to upload a file, a new
                    # TemporaryUploadedFile object will be created and,
                    # which is more important, it will be assigned to
                    # `note.document` field. We want to avoid this to make sure
                    # that until the form is completely valid previous file
                    # is not re-written. To do it we assign the `old_file`
                    # value to both cleaned_data and note.document:
                    form.cleaned_data['review_manuscript'] = old_file
                    submission.review_manuscript.document = old_file
            else:
~~                return HttpResponseForbidden()
        else:
            form = UploadReviewManuscriptForm(instance=submission)
        return render(request, 'submissions/manuscript.html', {
            'submission': submission,
            'form': form,
        })
~~    return HttpResponseForbidden()


@login_required
@require_POST
def delete_manuscript(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    if submission.review_manuscript_editable_by(request.user):
        file_name = submission.get_review_manuscript_name()
        if submission.review_manuscript:
            submission.review_manuscript.delete()
        return render(
            request,
            'submissions/components/file_deleted_message.html', {
                'alert_class': 'warning',
                'file_name': file_name,
            })
    else:
~~        return HttpResponseForbidden()


@login_required
@require_GET
def download_manuscript(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    if submission.is_manuscript_viewable_by(request.user):
        if submission.review_manuscript:
            filename = submission.get_review_manuscript_name()
            mtype = mimetypes.guess_type(filename)[0]
            response = HttpResponse(
                submission.review_manuscript.file,
                content_type=mtype
            )
            response['Content-Disposition'] = f'filename={filename}'
            return response
        raise Http404
~~    return HttpResponseForbidden()


@login_required
def submission_overview(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    if submission.status == 'SUBMIT':
        deadline = submission.conference.submission_stage.end_date
    elif submission.status == 'REVIEW':
        deadline = submission.conference.review_stage.end_date
    else:
        deadline = None

    # If the overview page is visited for the first time, we display finish
    # flag. For the following visits, show close:
    show_finish = not submission.reached_overview
    if show_finish:
        submission.reached_overview = True
        submission.save()
        messages.success(
            request,
            f'Submission #{pk} "{submission.title}" was successfully created!'
        )

    if submission.is_viewable_by(request.user):
        return render(request, 'submissions/overview.html', {
            'submission': submission,
            'deadline': deadline,
            'show_finish': show_finish,
        })
~~    return HttpResponseForbidden()


@login_required
@require_POST
def submission_delete(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    if submission.is_deletable_by(request.user):
        # TODO: send letters to authors
        messages.warning(
            request,
            f'Submission #{pk} "{submission.title}" was deleted'
        )
        if submission.review_manuscript:
            submission.review_manuscript.delete()
        submission.delete()
        return redirect('home')
~~    return HttpResponseForbidden()


#
# Authors:
#
@login_required
@require_POST
def delete_author(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    if submission.authors_editable_by(request.user):
        form = AuthorDeleteForm(submission, request.POST)
        if form.is_valid():
            form.save()
        return redirect('submissions:authors', pk=pk)
~~    return HttpResponseForbidden()


@login_required
@require_POST
def create_author(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    if submission.authors_editable_by(request.user):
        form = AuthorCreateForm(submission, request.POST)
        if form.is_valid():
            form.save()
        return redirect('submissions:authors', pk=pk)
~~    return HttpResponseForbidden()


@login_required
@require_POST
def order_authors(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    if submission.authors_editable_by(request.user):
        form = AuthorsReorderForm(submission, request.POST)
        if form.is_valid():
            form.save()
        return redirect('submissions:authors', pk=pk)
~~    return HttpResponseForbidden()


@login_required
@require_POST
def send_invitation(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    if submission.authors_editable_by(request.user):
        form = InviteAuthorForm(request.POST)
        if form.is_valid():
            form.save(request, submission)
            messages.success(request, _('Invitation sent'))
        else:
            messages.warning(request, _('Errors while sending invitation'))
        return redirect('submissions:authors', pk=pk)
~~    return HttpResponseForbidden()

```


## Example 2 from django-angular
[django-angular](https://github.com/jrief/django-angular)
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / views / mixins.py**](https://github.com/jrief/django-angular/blob/master/djng/views/mixins.py)

```python
# -*- coding: utf-8 -*-
import json
import warnings
from django.core.serializers.json import DjangoJSONEncoder
~~from django.http import (HttpResponse, HttpResponseBadRequest, 
~~                         HttpResponseForbidden)


def allow_remote_invocation(func, method='auto'):
    """
    All methods which shall be callable through a given Ajax 'action' must be
    decorated with @allowed_action. This is required for safety reasons. It
    inhibits the caller to invoke all available methods of a class.
    """
    setattr(func, 'allow_rmi', method)
    return func


def allowed_action(func):
    warnings.warn("Decorator `@allowed_action` is deprecated. "
                  "Use `@allow_remote_invocation` instead.", 
                  DeprecationWarning)
    return allow_remote_invocation(func)


class JSONResponseException(Exception):
    """
    Exception class for triggering HTTP 4XX responses with JSON content, where expected.
    """
    status_code = 400

    def __init__(self, message=None, status=None, *args, **kwargs):
        if status is not None:
            self.status_code = status
        super(JSONResponseException, self).__init__(message, *args, **kwargs)


class JSONBaseMixin(object):
    """
    Basic mixin for encoding HTTP responses in JSON format.
    """
    json_encoder = DjangoJSONEncoder
    json_content_type = 'application/json;charset=UTF-8'

    def json_response(self, response_data, status=200, **kwargs):
        out_data = json.dumps(response_data, cls=self.json_encoder, **kwargs)
        response = HttpResponse(out_data, self.json_content_type, status=status)
        response['Cache-Control'] = 'no-cache'
        return response


class JSONResponseMixin(JSONBaseMixin):
    """
    A mixin for View classes that dispatches requests containing the private HTTP header
    ``DjNg-Remote-Method`` onto a method of an instance of this class, with the given method name.
    This named method must be decorated with ``@allow_remote_invocation`` and shall return a
    list or dictionary which is serializable to JSON.
    The returned HTTP responses are of kind ``application/json;charset=UTF-8``.
    """
    def get(self, request, *args, **kwargs):
        if not request.is_ajax():
            return self._dispatch_super(request, *args, **kwargs)
        if 'action' in kwargs:
            warnings.warn("Using the keyword 'action' in URLresolvers is deprecated. Please use 'invoke_method' instead", DeprecationWarning)
            remote_method = kwargs['action']
        else:
            remote_method = kwargs.get('invoke_method')
        if remote_method:
            # method for invocation is determined programmatically
            handler = getattr(self, remote_method)
        else:
            # method for invocation is determined by HTTP header
            remote_method = request.META.get('HTTP_DJNG_REMOTE_METHOD')
            handler = remote_method and getattr(self, remote_method, None)
            if not callable(handler):
                return self._dispatch_super(request, *args, **kwargs)
~~            if not hasattr(handler, 'allow_rmi'):
~~                return HttpResponseForbidden("Method '{0}.{1}' has no "
~~                                             "decorator "
~~                                             "'@allow_remote_invocation'"
~~                                             .format(self.__class__.__name__, 
~~                                                     remote_method))
        try:
            response_data = handler()
        except JSONResponseException as e:
            return self.json_response({'message': e.args[0]}, e.status_code)
        return self.json_response(response_data)

    def post(self, request, *args, **kwargs):
        if not request.is_ajax():
            return self._dispatch_super(request, *args, **kwargs)
        try:
            in_data = json.loads(request.body.decode('utf-8'))
        except ValueError:
            in_data = request.body.decode('utf-8')
        if 'action' in in_data:
            warnings.warn("Using the keyword 'action' inside the payload is deprecated. Please use 'djangoRMI' from module 'djng.forms'", DeprecationWarning)
            remote_method = in_data.pop('action')
        else:
            remote_method = request.META.get('HTTP_DJNG_REMOTE_METHOD')
        handler = remote_method and getattr(self, remote_method, None)
        if not callable(handler):
            return self._dispatch_super(request, *args, **kwargs)
~~        if not hasattr(handler, 'allow_rmi'):
~~            return HttpResponseForbidden("Method '{0}.{1}' has no "
~~                                         "decorator "
~~                                         "'@allow_remote_invocation'"
~~                                         .format(self.__class__.__name__, 
~~                                                 remote_method), 403)
        try:
            response_data = handler(in_data)
        except JSONResponseException as e:
            return self.json_response({'message': e.args[0]}, e.status_code)
        return self.json_response(response_data)

    def _dispatch_super(self, request, *args, **kwargs):
        base = super(JSONResponseMixin, self)
        handler = getattr(base, request.method.lower(), None)
        if callable(handler):
            return handler(request, *args, **kwargs)
        # HttpResponseNotAllowed expects permitted methods.
        return HttpResponseBadRequest('This view can not handle method {0}'.format(request.method), status=405)

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
~~from django.http import (
~~    HttpResponse,
~~    HttpResponseBadRequest,
~~    HttpResponseForbidden,
~~    HttpResponseNotFound,
~~    HttpResponseRedirect,
~~)
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


## ... source file abbreviated to get to HttpResponseForbidden examples ...


class PlaceholderAdminMixin(object):

    def _get_attached_admin(self, placeholder):
        return placeholder._get_attached_admin(admin_site=self.admin_site)

    def _get_operation_language(self, request):
        # Unfortunately the ?language GET query
        # has a special meaning on the CMS.
        # It allows users to see another language while maintaining
        # the same url. This complicates language detection.
        site = get_current_site()
        parsed_url = urlparse(request.GET['cms_path'])
        queries = dict(parse_qsl(parsed_url.query))
        language = queries.get('language')

        if not language:
            language = translation.get_language_from_path(parsed_url.path)
        return get_language_code(language, site_id=site.pk)

    def _get_operation_origin(self, request):
        return urlparse(request.GET['cms_path']).path

    def _send_pre_placeholder_operation(self, request, operation, **kwargs):
        token = str(uuid.uuid4())

        if not request.GET.get('cms_path'):
            warnings.warn('All custom placeholder admin endpoints require '
                          'a "cms_path" GET query which points to the path '
                          'where the request originates from.'
                          'This backwards compatible shim will be removed on 3.5 '
                          'and an HttpBadRequest response will be returned instead.',
                          UserWarning)
            return token

        pre_placeholder_operation.send(
            sender=self.__class__,
            operation=operation,
            request=request,
            language=self._get_operation_language(request),
            token=token,
            origin=self._get_operation_origin(request),
            **kwargs
        )
        return token

    def _send_post_placeholder_operation(self, request, operation, 
                                         token, **kwargs):
        if not request.GET.get('cms_path'):
            # No need to re-raise the warning
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
        # CMSPluginBase subclass
        plugin_class = plugin_pool.get_plugin(plugin_type)
        real_queryset = plugin_class.get_render_queryset().\
                        select_related('parent', 'placeholder')
        return get_object_or_404(real_queryset, pk=plugin_id)

    def get_urls(self):
        """
        Register the plugin specific urls (add/edit/copy/remove/move)
        """
        info = "%s_%s" % (self.model._meta.app_label, self.model._meta.model_name)
        pat = lambda regex, fn: url(regex, 
                                    self.admin_site.admin_view(fn), 
                                    name='%s_%s' % (info, fn.__name__))
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

    def has_copy_plugins_permission(self, request, plugins):
        # Plugins can only be copied to the clipboard
        placeholder = request.toolbar.clipboard
        return placeholder.has_add_plugins_permission(request.user, plugins)

    def has_copy_from_clipboard_permission(self, request, placeholder, 
                                           plugins):
        return placeholder.has_add_plugins_permission(request.user, 
                                                      plugins)

    def has_copy_from_placeholder_permission(self, request, source_placeholder, 
                                             target_placeholder, plugins):
        if not source_placeholder.has_add_plugins_permission(request.user, plugins):
            return False
        return target_placeholder.has_add_plugins_permission(request.user, plugins)

    def has_move_plugin_permission(self, request, plugin, target_placeholder):
        placeholder = plugin.placeholder
        return placeholder.has_move_plugin_permission(request.user, 
                                                      plugin, 
                                                      target_placeholder)

    def has_clear_placeholder_permission(self, request, placeholder, 
                                         language=None):
        if language:
            languages = [language]
        else:
            # fetch all languages this placeholder contains
            # based on it's plugins
            languages = (
                placeholder
                .cmsplugin_set
                .values_list('language', flat=True)
                .distinct()
                .order_by()
            )
        return placeholder.has_clear_permission(request.user, languages)

    def get_placeholder_template(self, request, placeholder):
        pass

    @xframe_options_sameorigin
    def add_plugin(self, request):
        """
        Shows the add plugin form and saves it on POST.

        Requires the following GET parameters:
            - cms_path
            - placeholder_id
            - plugin_type
            - plugin_language
            - plugin_parent (optional)
            - plugin_position (optional)
        """
        form = PluginAddValidationForm(request.GET)

        if not form.is_valid():
            # list() is necessary for python 3 compatibility.
            # errors is s dict mapping fields to a list of errors
            # for that field.
            error = list(form.errors.values())[0][0]
            return HttpResponseBadRequest(force_text(error))

        plugin_data = form.cleaned_data
        placeholder = plugin_data['placeholder_id']
        plugin_type = plugin_data['plugin_type']

~~        if not self.has_add_plugin_permission(request, placeholder, plugin_type):
~~            message = force_text(_('You do not have permission to add a plugin'))
~~            return HttpResponseForbidden(message)

        parent = plugin_data.get('plugin_parent')

        if parent:
            position = parent.cmsplugin_set.count()
        else:
            position = CMSPlugin.objects.filter(
                parent__isnull=True,
                language=plugin_data['plugin_language'],
                placeholder=placeholder,
            ).count()

        plugin_data['position'] = position

        plugin_class = plugin_pool.get_plugin(plugin_type)
        plugin_instance = plugin_class(plugin_class.model, self.admin_site)

        # Setting attributes on the form class is perfectly fine.
        # The form class is created by modelform factory every time
        # this get_form() method is called.
        plugin_instance._cms_initial_attributes = {
            'language': plugin_data['plugin_language'],
            'placeholder': plugin_data['placeholder_id'],
            'parent': plugin_data.get('plugin_parent', None),
            'plugin_type': plugin_data['plugin_type'],
            'position': plugin_data['position'],
        }

        response = plugin_instance.add_view(request)

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
        """
        POST request should have the following data:

        - cms_path
        - source_language
        - source_placeholder_id
        - source_plugin_id (optional)
        - target_language
        - target_placeholder_id
        - target_plugin_id (deprecated/unused)
        """
        source_placeholder_id = request.POST['source_placeholder_id']
        target_language = request.POST['target_language']
        target_placeholder_id = request.POST['target_placeholder_id']
        source_placeholder = get_object_or_404(Placeholder, pk=source_placeholder_id)
        target_placeholder = get_object_or_404(Placeholder, pk=target_placeholder_id)

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

        source_plugin = get_object_or_404(
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

        # Empty the clipboard
        target_placeholder.clear()

        plugin_pairs = copy_plugins.copy_plugins_to(
            old_plugins,
            to_placeholder=target_placeholder,
            to_language=target_language,
        )
        return plugin_pairs[0][0]

    def _copy_placeholder_to_clipboard(self, request, source_placeholder, target_placeholder):
        source_language = request.POST['source_language']
        target_language = request.POST['target_language']

        # User is copying the whole placeholder to the clipboard.
        old_plugins = source_placeholder.get_plugins_list(language=source_language)

        if not self.has_copy_plugins_permission(request, old_plugins):
            message = _('You do not have permission to copy this placeholder.')
            raise PermissionDenied(force_text(message))

        # Empty the clipboard
        target_placeholder.clear()

        # Create a PlaceholderReference plugin which in turn
        # creates a blank placeholder called "clipboard"
        # the real clipboard has the reference placeholder inside but the plugins
        # are inside of the newly created blank clipboard.
        # This allows us to wrap all plugins in the clipboard under one plugin
        reference = PlaceholderReference.objects.create(
            name=source_placeholder.get_label(),
            plugin_type='PlaceholderPlugin',
            language=target_language,
            placeholder=target_placeholder,
        )

        copy_plugins.copy_plugins_to(
            old_plugins,
            to_placeholder=reference.placeholder_ref,
            to_language=target_language,
        )
        return reference

    def _add_plugins_from_placeholder(self, request, source_placeholder, target_placeholder):
        # Plugins are being copied from a placeholder in another language
        # using the "Copy from language" placeholder operation.
        source_language = request.POST['source_language']
        target_language = request.POST['target_language']

        old_plugins = source_placeholder.get_plugins_list(language=source_language)

        # Check if the user can copy plugins from source placeholder to
        # target placeholder.
        has_permissions = self.has_copy_from_placeholder_permission(
            request,
            source_placeholder,
            target_placeholder,
            old_plugins,
        )

        if not has_permissions:
            message = _('You do not have permission to copy these plugins.')
            raise PermissionDenied(force_text(message))

        target_tree_order = target_placeholder.get_plugin_tree_order(
            language=target_language,
            parent_id=None,
        )

        operation_token = self._send_pre_placeholder_operation(
            request,
            operation=operations.ADD_PLUGINS_FROM_PLACEHOLDER,
            plugins=old_plugins,
            source_language=source_language,
            source_placeholder=source_placeholder,
            target_language=target_language,
            target_placeholder=target_placeholder,
            target_order=target_tree_order,
        )

        copied_plugins = copy_plugins.copy_plugins_to(
            old_plugins,
            to_placeholder=target_placeholder,
            to_language=target_language,
        )

        new_plugin_ids = (new.pk for new, old in copied_plugins)

        # Creates a list of PKs for the top-level plugins ordered by
        # their position.
        top_plugins = (pair for pair in copied_plugins if not pair[0].parent_id)
        top_plugins_pks = [p[0].pk for p in sorted(top_plugins, key=lambda pair: pair[1].position)]

        # All new plugins are added to the bottom
        target_tree_order = target_tree_order + top_plugins_pks

        reorder_plugins(
            target_placeholder,
            parent_id=None,
            language=target_language,
            order=target_tree_order,
        )
        target_placeholder.mark_as_dirty(target_language, clear_cache=False)

        new_plugins = CMSPlugin.objects.filter(pk__in=new_plugin_ids).order_by('path')
        new_plugins = list(new_plugins)

        self._send_post_placeholder_operation(
            request,
            operation=operations.ADD_PLUGINS_FROM_PLACEHOLDER,
            token=operation_token,
            plugins=new_plugins,
            source_language=source_language,
            source_placeholder=source_placeholder,
            target_language=target_language,
            target_placeholder=target_placeholder,
            target_order=target_tree_order,
        )
        return new_plugins

    @xframe_options_sameorigin
    def edit_plugin(self, request, plugin_id):
        try:
            plugin_id = int(plugin_id)
        except ValueError:
            return HttpResponseNotFound(force_text(_("Plugin not found")))

        obj = self._get_plugin_from_id(plugin_id)

        # CMSPluginBase subclass instance
        plugin_instance = obj.get_plugin_class_instance(admin=self.admin_site)

~~        if not self.has_change_plugin_permission(request, obj):
~~            return HttpResponseForbidden(force_text(_("You do not have "
~~                                                      "permission to edit"
~~                                                      " this plugin")))

        response = plugin_instance.change_view(request, str(plugin_id))

        plugin = getattr(plugin_instance, 'saved_object', None)

        if plugin:
            plugin.placeholder.mark_as_dirty(plugin.language, clear_cache=False)

        if plugin_instance._operation_token:
            self._send_post_placeholder_operation(
                request,
                operation=operations.CHANGE_PLUGIN,
                token=plugin_instance._operation_token,
                old_plugin=obj,
                new_plugin=plugin,
                placeholder=plugin.placeholder,
            )
        return response


## ... source file abbreviated to get to more examples ...


    @xframe_options_sameorigin
    def delete_plugin(self, request, plugin_id):
        plugin = self._get_plugin_from_id(plugin_id)

~~        if not self.has_delete_plugin_permission(request, plugin):
~~            return HttpResponseForbidden(force_text(
~~                _("You do not have permission to delete this plugin")))

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
        placeholder = get_object_or_404(Placeholder, pk=placeholder_id)
        language = request.GET.get('language')

        if placeholder.pk == request.toolbar.clipboard.pk:
            # User is clearing the clipboard, no need for permission
            # checks here as the clipboard is unique per user.
            # There could be a case where a plugin has relationship to
            # an object the user does not have permission to delete.
            placeholder.clear(language)
            return HttpResponseRedirect(admin_reverse('index', current_app=self.admin_site.name))

~~        if not self.has_clear_placeholder_permission(request, 
~~                                                     placeholder, 
~~                                                     language):
~~            return HttpResponseForbidden(force_text(_("You do not have "
~~                                                      "permission to clear "
~~                                                      "this placeholder")))

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

~~        if request.POST:
~~            # The user has already confirmed the deletion.
~~            if perms_needed:
~~                return HttpResponseForbidden(force_text(_("You do not have "
~~                                                          "permission to "
~~                                                          "clear this " 
~~                                                          "placeholder")))

            operation_token = self._send_pre_placeholder_operation(
                request,
                operation=operations.CLEAR_PLACEHOLDER,
                plugins=plugins,
                placeholder=placeholder,
            )

            placeholder.clear(language)
            placeholder.mark_as_dirty(language, clear_cache=False)

            self.log_deletion(request, placeholder, obj_display)
            self.message_user(request, _('The placeholder "%(obj)s" '
                                         'was cleared successfully.') % {
                'obj': obj_display})

            self._send_post_placeholder_operation(
                request,
                operation=operations.CLEAR_PLACEHOLDER,
                token=operation_token,
                plugins=plugins,
                placeholder=placeholder,
            )
            return HttpResponseRedirect(admin_reverse('index', 
                                        current_app=self.admin_site.name))

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
        return TemplateResponse(request, 
                                "admin/cms/page/plugin/delete_confirmation.html", 
                                context)

```


## Example 4 from django-oauth-toolkit
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

[**django-oauth-toolkit / oauth2_provider / views / mixins.py**](https://github.com/jazzband/django-oauth-toolkit/blob/master/oauth2_provider/views/mixins.py)

```python
import logging

from django.core.exceptions import ImproperlyConfigured
~~from django.http import HttpResponseForbidden

from ..exceptions import FatalClientError
from ..scopes import get_scopes_backend
from ..settings import oauth2_settings


log = logging.getLogger("oauth2_provider")

SAFE_HTTP_METHODS = ["GET", "HEAD", "OPTIONS"]


## ... source code abbreviated to get to the examples ...


class ProtectedResourceMixin(OAuthLibMixin):
    """
    Helper mixin that implements OAuth2 protection on request dispatch,
    specially useful for Django Generic Views
    """
    def dispatch(self, request, *args, **kwargs):
        # let preflight OPTIONS requests pass
        if request.method.upper() == "OPTIONS":
            return super().dispatch(request, *args, **kwargs)

        # check if the request is valid and the protected resource may be accessed
~~        valid, r = self.verify_request(request)
~~        if valid:
~~            request.resource_owner = r.user
~~            return super().dispatch(request, *args, **kwargs)
~~        else:
~~            return HttpResponseForbidden()


class ReadWriteScopedResourceMixin(ScopedResourceMixin, OAuthLibMixin):
    """
    Helper mixin that implements "read and write scopes" behavior
    """
    required_scopes = []
    read_write_scope = None

    def __new__(cls, *args, **kwargs):
        provided_scopes = get_scopes_backend().get_all_scopes()
        read_write_scopes = [oauth2_settings.READ_SCOPE, oauth2_settings.WRITE_SCOPE]

        if not set(read_write_scopes).issubset(set(provided_scopes)):
            raise ImproperlyConfigured(
                "ReadWriteScopedResourceMixin requires following scopes {}"
                ' to be in OAUTH2_PROVIDER["SCOPES"] list in settings'.format(read_write_scopes)
            )

        return super().__new__(cls, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.method.upper() in SAFE_HTTP_METHODS:
            self.read_write_scope = oauth2_settings.READ_SCOPE
        else:
            self.read_write_scope = oauth2_settings.WRITE_SCOPE

        return super().dispatch(request, *args, **kwargs)

    def get_scopes(self, *args, **kwargs):
        scopes = super().get_scopes(*args, **kwargs)

        # this returns a copy so that self.required_scopes is not modified
        return scopes + [self.read_write_scope]

```


## Example 5 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / tests / middleware.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/tests/middleware.py)

```python
# middleware.py
~~from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin


class BlockDodgyUserAgentMiddleware(MiddlewareMixin):
    """Used to test that we're correctly handling responses 
    returned from middleware during page
    previews. If a client with user agent "EvilHacker" calls 
    an admin view that performs a
    preview, the request to /admin/... will pass this 
    middleware, but the fake request used for
    the preview (which keeps the user agent header, 
    but uses the URL path of the front-end page)
    will trigger a Forbidden response. In this case, 
    the expected behaviour is to return that
    response back to the user.
    """

    def process_request(self, request):
~~        if not request.path.startswith('/admin/') and \
~~               request.META.get('HTTP_USER_AGENT') == 'EvilHacker':
~~            return HttpResponseForbidden("Forbidden")

```

