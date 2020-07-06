title: django.views.decorators.http require_GET Example Code
category: page
slug: django-views-decorators-http-require-get-examples
sortorder: 500011518
toc: False
sidebartitle: django.views.decorators.http require_GET
meta: Python example code for the require_GET callable from the django.views.decorators.http module of the Django project.


require_GET is a callable within the django.views.decorators.http module of the Django project.


## Example 1 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / submissions / views.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/submissions/views.py)

```python
# views.py
import mimetypes

from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseForbidden, \
    HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
~~from django.views.decorators.http import require_POST, require_GET

from conferences.models import Conference
from conferences.utilities import validate_chair_access
from submissions.forms import CreateSubmissionForm, SubmissionDetailsForm, \
    AuthorCreateForm, AuthorsReorderForm, AuthorDeleteForm, \
    UploadReviewManuscriptForm, InviteAuthorForm, UploadAttachmentForm, \
    UpdateSubmissionStatusForm
from submissions.models import Submission, Author, Attachment
from submissions.utilities import is_authorized_edit, \
    is_authorized_view_attachment


def _create_submission(request, form):
    if request.method == 'POST':
        if form.is_valid():
            submission = form.save()

            submission.created_by = request.user
            submission.save()
            Author.objects.create(
                submission=submission,
                order=1,
                user=request.user
            )


## ... source file abbreviated to get to require_GET examples ...


            'submission': submission,
            'form': form,
        })
    return HttpResponseForbidden()


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
        return HttpResponseForbidden()


@login_required
~~@require_GET
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
    return HttpResponseForbidden()


@login_required
def submission_overview(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    deadline = ''

    show_finish = not submission.reached_overview
    if show_finish:
        submission.reached_overview = True


## ... source file abbreviated to get to require_GET examples ...


    submission = get_object_or_404(Submission, pk=pk)
    if submission.authors_editable_by(request.user):
        form = AuthorsReorderForm(submission, request.POST)
        if form.is_valid():
            form.save()
        return redirect('submissions:authors', pk=pk)
    return HttpResponseForbidden()


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
    return HttpResponseForbidden()


@login_required
~~@require_GET
def camera_ready(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    if submission.status not in [Submission.ACCEPTED, Submission.IN_PRINT,
                                 Submission.PUBLISHED]:
        raise Http404
    return render(request, 'submissions/camera_ready.html', context={
        'submission': submission,
        'editable': True,
    })


@login_required
~~@require_GET
def download_attachment(request, pk, att_pk):
    submission = get_object_or_404(Submission, pk=pk)
    attachment = Attachment.objects.get(pk=att_pk)
    if not is_authorized_view_attachment(request.user, submission):
        return HttpResponseForbidden()
    if attachment.file:
        filename = attachment.get_file_name()
        mtype = mimetypes.guess_type(filename)[0]
        response = HttpResponse(attachment.file.file, content_type=mtype)
        response['Content-Disposition'] = f'filename={filename}'
        return response
    raise Http404


@login_required
@require_POST
def upload_attachment(request, pk, att_pk):
    submission = get_object_or_404(Submission, pk=pk)
    attachment = get_object_or_404(Attachment, pk=att_pk)
    if not is_authorized_edit(request.user, submission):
        return HttpResponseForbidden()
    form = UploadAttachmentForm(
        request.POST, request.FILES, instance=attachment)
    old_file = attachment.file.file if attachment.file else None


## ... source file continues with no further require_GET examples...

```


## Example 2 from django-jet
[django-jet](https://github.com/geex-arts/django-jet)
([project documentation](https://jet.readthedocs.io/en/latest/),
[PyPI project page](https://pypi.org/project/django-jet/) and
[more information](http://jet.geex-arts.com/))
is a fancy [Django](/django.html) Admin panel replacement.

The django-jet project is open source under the
[GNU Affero General Public License v3.0](https://github.com/geex-arts/django-jet/blob/dev/LICENSE).

[**django-jet / jet / views.py**](https://github.com/geex-arts/django-jet/blob/dev/jet/./views.py)

```python
# views.py
~~from django.views.decorators.http import require_POST, require_GET
from jet.forms import AddBookmarkForm, RemoveBookmarkForm, ToggleApplicationPinForm, ModelLookupForm
from jet.models import Bookmark
from jet.utils import JsonResponse


@require_POST
def add_bookmark_view(request):
    result = {'error': False}
    form = AddBookmarkForm(request, request.POST)

    if form.is_valid():
        bookmark = form.save()
        result.update({
            'id': bookmark.pk,
            'title': bookmark.title,
            'url': bookmark.url
        })
    else:
        result['error'] = True

    return JsonResponse(result)


@require_POST


## ... source file abbreviated to get to require_GET examples ...



        if form.is_valid():
            form.save()
        else:
            result['error'] = True
    except Bookmark.DoesNotExist:
        result['error'] = True

    return JsonResponse(result)


@require_POST
def toggle_application_pin_view(request):
    result = {'error': False}
    form = ToggleApplicationPinForm(request, request.POST)

    if form.is_valid():
        pinned = form.save()
        result['pinned'] = pinned
    else:
        result['error'] = True

    return JsonResponse(result)


~~@require_GET
def model_lookup_view(request):
    result = {'error': False}

    form = ModelLookupForm(request, request.GET)

    if form.is_valid():
        items, total = form.lookup()
        result['items'] = items
        result['total'] = total
    else:
        result['error'] = True

    return JsonResponse(result)



## ... source file continues with no further require_GET examples...

```

