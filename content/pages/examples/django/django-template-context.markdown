title: django.template Context Example Code
category: page
slug: django-template-context-examples
sortorder: 500011357
toc: False
sidebartitle: django.template Context
meta: Example code for understanding how to use the Context class from the django.template module of the Django project.


`Context` is a class within the `django.template` module of the Django project.

<a href="/django-template-engine-examples.html">Engine</a>,
<a href="/django-template-library-examples.html">Library</a>,
<a href="/django-template-node-examples.html">Node</a>,
<a href="/django-template-nodelist-examples.html">NodeList</a>,
<a href="/django-template-origin-examples.html">Origin</a>,
<a href="/django-template-requestcontext-examples.html">RequestContext</a>,
<a href="/django-template-template-examples.html">Template</a>,
<a href="/django-template-templatedoesnotexist-examples.html">TemplateDoesNotExist</a>,
<a href="/django-template-templatesyntaxerror-examples.html">TemplateSyntaxError</a>,
<a href="/django-template-variable-examples.html">Variable</a>,
<a href="/django-template-context-examples.html">context</a>,
<a href="/django-template-engine-examples.html">engine</a>,
<a href="/django-template-library-examples.html">library</a>,
and <a href="/django-template-loader-examples.html">loader</a>
are several other callables with code examples from the same `django.template` package.

## Example 1 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / chair_mail / models.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/chair_mail/models.py)

```python
# models.py
from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.db.models import ForeignKey, OneToOneField, TextField, CharField, \
    SET_NULL, CASCADE, BooleanField, UniqueConstraint
from django.db.models.signals import post_save
from django.dispatch import receiver
~~from django.template import Template, Context
from django.utils import timezone
from markdown import markdown
from html2text import html2text

from chair_mail.context import get_conference_context, get_user_context, \
    get_submission_context, get_frame_context
from conferences.models import Conference
from submissions.models import Submission
from users.models import User

MSG_TYPE_USER = 'user'
MSG_TYPE_SUBMISSION = 'submission'

MESSAGE_TYPE_CHOICES = (
    (MSG_TYPE_USER, 'Message to users'),
    (MSG_TYPE_SUBMISSION, 'Message to submissions'),
)


class EmailFrame(models.Model):
    text_html = models.TextField()
    text_plain = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)

    @staticmethod
    def render(frame_template, conference, subject, body):
        context_data = get_frame_context(conference, subject, body)
~~        context = Context(context_data, autoescape=False)
        return Template(frame_template).render(context)

    def render_html(self, subject, body):
        return EmailFrame.render(
            self.text_html, self.conference, subject, body
        )

    def render_plain(self, subject, body):
        text_plain = self.text_plain
        if not text_plain:
            text_plain = html2text(self.text_html)
        return EmailFrame.render(
            text_plain, self.conference, subject, body
        )


class EmailSettings(models.Model):
    frame = models.ForeignKey(EmailFrame, on_delete=models.SET_NULL, null=True)
    conference = models.OneToOneField(
        Conference, null=True, blank=True, on_delete=models.CASCADE,
        related_name='email_settings',
    )




## ... source file abbreviated to get to Context examples ...



    group_message = models.OneToOneField(
        GroupMessage, on_delete=models.CASCADE, parent_link=True)

    @property
    def message_type(self):
        return MSG_TYPE_USER

    @staticmethod
    def create(subject, body, conference, objects_to):
        msg = UserMessage.objects.create(
            subject=subject, body=body, conference=conference)
        for user in objects_to:
            msg.recipients.add(user)
        msg.save()
        return msg

    def send(self, sender):
        self.sent = False
        self.sent_by = sender
        self.save()

        frame = self.conference.email_settings.frame
        conference_context = get_conference_context(self.conference)
        for user in self.recipients.all():
~~            context = Context({
                **conference_context,
                **get_user_context(user, self.conference)
            }, autoescape=False)
            email = EmailMessage.create(
                group_message=self.group_message,
                user_to=user,
                context=context,
                frame=frame
            )
            email.send(sender)

        self.sent_at = timezone.now()
        self.sent = True
        self.save()
        return self


class SubmissionMessage(GroupMessage):
    recipients = models.ManyToManyField(
        Submission, related_name='group_emails')

    group_message = models.OneToOneField(
        GroupMessage, on_delete=models.CASCADE, parent_link=True)

    @property
    def message_type(self):
        return MSG_TYPE_SUBMISSION

    @staticmethod
    def create(subject, body, conference, objects_to):
        msg = SubmissionMessage.objects.create(
            subject=subject, body=body, conference=conference)
        for submission in objects_to:
            msg.recipients.add(submission)
        msg.save()
        return msg

    def send(self, sender):
        self.sent = False
        self.sent_by = sender
        self.save()

        frame = self.conference.email_settings.frame
        conference_context = get_conference_context(self.conference)
        for submission in self.recipients.all():
            submission_context = get_submission_context(submission)
            for author in submission.authors.all():
                user = author.user
~~                context = Context({
                    **conference_context,
                    **submission_context,
                    **get_user_context(user, self.conference)
                }, autoescape=False)
                email = EmailMessage.create(
                    group_message=self.group_message,
                    user_to=user,
                    context=context,
                    frame=frame
                )
                email.send(sender)

        self.sent_at = timezone.now()
        self.sent = True
        self.save()
        return self


def get_group_message_model(msg_type):
    return {
        MSG_TYPE_USER: UserMessage,
        MSG_TYPE_SUBMISSION: SubmissionMessage,
    }[msg_type]



## ... source file continues with no further Context examples...

```


## Example 2 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / account / tests.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/account/tests.py)

```python
# tests.py
from __future__ import absolute_import

import json
import uuid
from datetime import timedelta

from django import forms
from django.conf import settings
from django.contrib.auth.models import AbstractUser, AnonymousUser
from django.contrib.sites.models import Site
from django.core import mail, validators
from django.core.exceptions import ValidationError
from django.db import models
from django.http import HttpResponseRedirect
~~from django.template import Context, Template
from django.test.client import Client, RequestFactory
from django.test.utils import override_settings
from django.urls import reverse
from django.utils.timezone import now

from allauth.account.forms import BaseSignupForm, ResetPasswordForm, SignupForm
from allauth.account.models import (
    EmailAddress,
    EmailConfirmation,
    EmailConfirmationHMAC,
)
from allauth.tests import Mock, TestCase, patch
from allauth.utils import get_user_model, get_username_max_length

from . import app_settings
from .adapter import get_adapter
from .auth_backends import AuthenticationBackend
from .signals import user_logged_in, user_logged_out
from .utils import (
    filter_users_by_username,
    url_str_to_user_pk,
    user_pk_to_url_str,
    user_username,
)


## ... source file continues with no further Context examples...

```


## Example 3 from django-appmail
[Django-Appmail](https://github.com/yunojuno/django-appmail)
([PyPI package information](https://pypi.org/project/django-appmail/))
is a [Django](/django.html) app for handling transactional email templates.
While the project began development as a way to work with the Mandrill
transactional [API](/application-programming-interfaces.html), it is
not exclusive to that API. The project simply provides a way to store
and render email content. The library does not send or receive emails.

Django-Appmail is open sourced under the
[MIT license](https://github.com/yunojuno/django-appmail/blob/master/LICENSE).

[**django-appmail / appmail / models.py**](https://github.com/yunojuno/django-appmail/blob/master/appmail/./models.py)

```python
# models.py
from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models, transaction
from django.http import HttpRequest
~~from django.template import Context, Template, TemplateDoesNotExist, TemplateSyntaxError
from django.utils.timezone import now as tz_now
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _lazy

from . import helpers
from .compat import JSONField
from .settings import (
    ADD_EXTRA_HEADERS,
    CONTEXT_PROCESSORS,
    LOG_SENT_EMAILS,
    VALIDATE_ON_SAVE,
)

User = get_user_model()


class EmailTemplateQuerySet(models.query.QuerySet):
    def active(self) -> EmailTemplateQuerySet:
        return self.filter(is_active=True)

    def current(
        self, name: str, language: str = settings.LANGUAGE_CODE
    ) -> EmailTemplateQuerySet:
        return (


## ... source file abbreviated to get to Context examples ...



    def save(self, *args: Any, **kwargs: Any) -> EmailTemplate:
        if self.pk is None:
            self.test_context = helpers.get_context(
                self.subject + self.body_text + self.body_html
            )
        validate = kwargs.pop("validate", VALIDATE_ON_SAVE)
        if validate:
            self.clean()
        super(EmailTemplate, self).save(*args, **kwargs)
        return self

    def clean(self) -> None:
        validation_errors = {}
        validation_errors.update(self._validate_body(EmailTemplate.CONTENT_TYPE_PLAIN))
        validation_errors.update(self._validate_body(EmailTemplate.CONTENT_TYPE_HTML))
        validation_errors.update(self._validate_subject())
        if validation_errors:
            raise ValidationError(validation_errors)

    def render_subject(
        self,
        context: dict,
        processors: List[Callable[[HttpRequest], dict]] = CONTEXT_PROCESSORS,
    ) -> str:
~~        ctx = Context(helpers.patch_context(context, processors), autoescape=False)
        return Template(self.subject).render(ctx)

    def _validate_subject(self) -> Dict[str, str]:
        try:
            self.render_subject({})
        except TemplateDoesNotExist as ex:
            return {"subject": _lazy("Template does not exist: {}".format(ex))}
        except TemplateSyntaxError as ex:
            return {"subject": str(ex)}
        else:
            return {}

    def render_body(
        self,
        context: dict,
        content_type: str = CONTENT_TYPE_PLAIN,
        processors: List[Callable[[HttpRequest], dict]] = CONTEXT_PROCESSORS,
    ) -> str:
        if content_type not in EmailTemplate.CONTENT_TYPES:
            raise ValueError(_(f"Invalid content type. Value supplied: {content_type}"))
        if content_type == EmailTemplate.CONTENT_TYPE_PLAIN:
~~            ctx = Context(helpers.patch_context(context, processors), autoescape=False)
            return Template(self.body_text).render(ctx)
        if content_type == EmailTemplate.CONTENT_TYPE_HTML:
~~            ctx = Context(helpers.patch_context(context, processors))
            return Template(self.body_html).render(ctx)
        raise ValueError(f"Invalid content_type '{content_type}'.")

    def _validate_body(self, content_type: str) -> Dict[str, str]:
        if content_type == EmailTemplate.CONTENT_TYPE_PLAIN:
            field_name = "body_text"
        elif content_type == EmailTemplate.CONTENT_TYPE_HTML:
            field_name = "body_html"
        else:
            raise ValueError("Invalid template content_type.")
        try:
            self.render_body({}, content_type=content_type)
        except TemplateDoesNotExist as ex:
            return {field_name: _("Template does not exist: {}".format(ex))}
        except TemplateSyntaxError as ex:
            return {field_name: str(ex)}
        else:
            return {}

    def clone(self) -> EmailTemplate:
        self.pk = None
        self.version += 1
        return self.save()



## ... source file continues with no further Context examples...

```


## Example 4 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / plugin_rendering.py**](https://github.com/divio/django-cms/blob/develop/cms/./plugin_rendering.py)

```python
# plugin_rendering.py
from collections import OrderedDict

from functools import partial

from classytags.utils import flatten_context

from django.contrib.sites.models import Site
~~from django.template import Context
from django.utils.functional import cached_property
from django.utils.module_loading import import_string
from django.utils.safestring import mark_safe

from cms.cache.placeholder import get_placeholder_cache, set_placeholder_cache
from cms.toolbar.utils import (
    get_placeholder_toolbar_js,
    get_plugin_toolbar_js,
    get_toolbar_from_request,
)
from cms.utils import get_language_from_request
from cms.utils.conf import get_cms_setting
from cms.utils.permissions import has_plugin_permission
from cms.utils.placeholder import get_toolbar_plugin_struct, restore_sekizai_context
from cms.utils.plugins import get_plugin_restrictions


def _unpack_plugins(parent_plugin):
    found_plugins = []

    for plugin in parent_plugin.child_plugin_instances or []:
        found_plugins.append(plugin)

        if plugin.child_plugin_instances:


## ... source file abbreviated to get to Context examples ...


        placeholder_cache = self._rendered_plugins_by_placeholder.setdefault(instance.placeholder_id, {})
        placeholder_cache.setdefault('plugins', []).append(instance)
        return self.get_plugin_toolbar_js(instance, page=page)

    def render_plugins(self, placeholder, language, page=None):
        template = page.get_template() if page else None
        plugins = self.get_plugins_to_render(placeholder, language, template)

        for plugin in plugins:
            plugin._placeholder_cache = placeholder
            yield self.render_plugin(plugin, page=page)


class LegacyRenderer(ContentRenderer):

    load_structure = True
    placeholder_edit_template = (
    )

    def get_editable_placeholder_context(self, placeholder, page=None):
        context = super().get_editable_placeholder_context(placeholder, page)
        context['plugin_menu_js'] = self.get_placeholder_plugin_menu(placeholder, page=page)
        return context


~~class PluginContext(Context):

    def __init__(self, dict_, instance, placeholder, processors=None, current_app=None):
        dict_ = flatten_context(dict_)
        super().__init__(dict_)

        if not processors:
            processors = []

        for path in get_cms_setting('PLUGIN_CONTEXT_PROCESSORS'):
            processor = import_string(path)
            self.update(processor(instance, placeholder, self))
        for processor in processors:
            self.update(processor(instance, placeholder, self))



## ... source file continues with no further Context examples...

```


## Example 5 from django-easy-timezones
[django-easy-timezones](https://github.com/Miserlou/django-easy-timezones)
([project website](https://www.gun.io/blog/django-easy-timezones))
is a Django
[middleware](https://docs.djangoproject.com/en/2.2/topics/http/middleware/)
[code library](https://pypi.org/project/django-easy-timezones/)
to simplify handling time data in your applications using
users' geolocation data.

[**django-easy-timezones / easy_timezones / views.py**](https://github.com/Miserlou/django-easy-timezones/blob/master/easy_timezones/./views.py)

```python
# views.py
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
~~from django.template import RequestContext, Template, Context

from datetime import datetime

def with_tz(request):
    
    dt = datetime.now() 
    t = Template('{% load tz %}{% localtime on %}{% get_current_timezone as TIME_ZONE %}{{ TIME_ZONE }}{% endlocaltime %}') 
    c = RequestContext(request)
    response = t.render(c)
    return HttpResponse(response)

def without_tz(request):
    
    t = Template('{% load tz %}{% get_current_timezone as TIME_ZONE %}{{ TIME_ZONE }}') 
    c = RequestContext(request)
    response = t.render(c)
    return HttpResponse(response)



## ... source file continues with no further Context examples...

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

[**django-extensions / django_extensions / management / modelviz.py**](https://github.com/django-extensions/django-extensions/blob/master/django_extensions/management/modelviz.py)

```python
# modelviz.py

import datetime
import os
import re

from django.apps import apps
from django.db.models.fields.related import (
    ForeignKey, ManyToManyField, OneToOneField, RelatedField,
)
from django.contrib.contenttypes.fields import GenericRelation
~~from django.template import Context, Template, loader
from django.utils.encoding import force_str
from django.utils.safestring import mark_safe
from django.utils.translation import activate as activate_language


__version__ = "1.1"
__license__ = "Python"
__author__ = "Bas van Oostveen <v.oostveen@gmail.com>",
__contributors__ = [
    "Antonio Cavedoni <http://cavedoni.com/>"
    "Stefano J. Attardi <http://attardi.org/>",
    "Carlo C8E Miron",
    "Andre Campos <cahenan@gmail.com>",
    "Justin Findlay <jfindlay@gmail.com>",
    "Alexander Houben <alexander@houben.ch>",
    "Joern Hees <gitdev@joernhees.de>",
    "Kevin Cherepski <cherepski@gmail.com>",
    "Jose Tomas Tocino <theom3ga@gmail.com>",
    "Adam Dobrawy <naczelnik@jawnosc.tk>",
    "Mikkel Munch Mortensen <https://www.detfalskested.dk/>",
    "Andrzej Bistram <andrzej.bistram@gmail.com>",
    "Daniel Lipsitt <danlipsitt@gmail.com>",
]


## ... source file abbreviated to get to Context examples ...


                if '.' in field.remote_field.model:
                    app_label, model_name = field.remote_field.model.split('.', 1)
                else:
                    app_label = field.model._meta.app_label
                    model_name = field.remote_field.model
                target_model = apps.get_model(app_label, model_name)
        else:
            target_model = field.remote_field.model

        _rel = self.get_relation_context(target_model, field, label, extras)

        if _rel not in model['relations'] and self.use_model(_rel['target']):
            return _rel

    def get_abstract_models(self, appmodels):
        abstract_models = []
        for appmodel in appmodels:
            abstract_models += [
                abstract_model for abstract_model in appmodel.__bases__
                if hasattr(abstract_model, '_meta') and abstract_model._meta.abstract
            ]
        abstract_models = list(set(abstract_models))  # remove duplicates
        return abstract_models

    def get_app_context(self, app):
~~        return Context({
            'name': '"%s"' % app.name,
            'app_name': "%s" % app.name,
            'cluster_app_name': "cluster_%s" % app.name.replace(".", "_"),
            'models': []
        })

    def get_appmodel_attributes(self, appmodel):
        if self.relations_as_fields:
            attributes = [field for field in appmodel._meta.local_fields]
        else:
            attributes = [field for field in appmodel._meta.local_fields if not
                          isinstance(field, RelatedField)]
        return attributes

    def get_appmodel_abstracts(self, appmodel):
        return [
            abstract_model.__name__ for abstract_model in appmodel.__bases__
            if hasattr(abstract_model, '_meta') and abstract_model._meta.abstract
        ]

    def get_appmodel_context(self, appmodel, appmodel_abstracts):
        context = {
            'model': appmodel,
            'app_name': appmodel.__module__.replace(".", "_"),


## ... source file abbreviated to get to Context examples ...


            for model_pattern in self.exclude_models:
                model_pattern = '^%s$' % model_pattern.replace('*', '.*')
                if re.search(model_pattern, model_name):
                    return False
        return not self.include_models

    def skip_field(self, field):
        if self.exclude_columns:
            if self.verbose_names and field.verbose_name:
                if field.verbose_name in self.exclude_columns:
                    return True
            if field.name in self.exclude_columns:
                return True
        return False


def generate_dot(graph_data, template='django_extensions/graph_models/digraph.dot'):
    if isinstance(template, str):
        template = loader.get_template(template)

    if not isinstance(template, Template) and not (hasattr(template, 'template') and isinstance(template.template, Template)):
        raise Exception("Default Django template loader isn't used. "
                        "This can lead to the incorrect template rendering. "
                        "Please, check the settings.")

~~    c = Context(graph_data).flatten()
    dot = template.render(c)

    return dot


def generate_graph_data(*args, **kwargs):
    generator = ModelGraph(*args, **kwargs)
    generator.generate_graph_data()
    return generator.get_graph_data()


def use_model(model, include_models, exclude_models):
    generator = ModelGraph([], include_models=include_models, exclude_models=exclude_models)
    return generator.use_model(model)



## ... source file continues with no further Context examples...

```


## Example 7 from django-floppyforms
[django-floppyforms](https://github.com/jazzband/django-floppyforms)
([project documentation](https://django-floppyforms.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-floppyforms/))
is a [Django](/django.html) code library for better control
over rendering HTML forms in your [templates](/template-engines.html).

The django-floppyforms code is provided as
[open source](https://github.com/jazzband/django-floppyforms/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-floppyforms / floppyforms / compat.py**](https://github.com/jazzband/django-floppyforms/blob/master/floppyforms/./compat.py)

```python
# compat.py
from contextlib import contextmanager

import django
~~from django.template import Context
from django.utils.datastructures import MultiValueDict

MULTIVALUE_DICT_TYPES = (MultiValueDict,)


REQUIRED_CONTEXT_ATTRIBTUES = (
    '_form_config',
    '_form_render',
)


class DictContext(dict):
    pass


if django.VERSION < (1, 8):
    def get_template(context, template_name):
        from django.template.loader import get_template
        return get_template(template_name)

    def get_context(context):
~~        if not isinstance(context, Context):
~~            context = Context(context)
        return context

else:
    def get_template(context, template_name):
        return context.template.engine.get_template(template_name)

    def get_context(context):
        return context


def flatten_context(context):
~~    if isinstance(context, Context):
        flat = {}
        for d in context.dicts:
            flat.update(d)
        return flat
    else:
        return context


def flatten_contexts(*contexts):
    new_context = DictContext()
    for context in contexts:
        if context is not None:
            new_context.update(flatten_context(context))
            for attr in REQUIRED_CONTEXT_ATTRIBTUES:
                if hasattr(context, attr):
                    setattr(new_context, attr, getattr(context, attr))
    return new_context


@contextmanager
def render_context(context_instance, context):
    if context_instance is not None:
        with context_instance.push(context):
            yield context_instance


## ... source file continues with no further Context examples...

```


## Example 8 from django-jet
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
~~from django.template import Context
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
    from django.urls import reverse, resolve, NoReverseMatch

from django.contrib.admin import AdminSite
from django.utils.encoding import smart_text
from django.utils.text import capfirst
from django.contrib import messages
from django.utils.encoding import force_text
from django.utils.functional import Promise


## ... source file abbreviated to get to Context examples ...


            item['items'] = item['models']
            return item
        app_list = list(map(map_item, original_app_list.values()))

    current_found = False

    for app in app_list:
        if not current_found:
            for model in app['items']:
                if not current_found and model.get('url') and context['request'].path.startswith(model['url']):
                    model['current'] = True
                    current_found = True
                else:
                    model['current'] = False

            if not current_found and app.get('url') and context['request'].path.startswith(app['url']):
                app['current'] = True
                current_found = True
            else:
                app['current'] = False

    return app_list


def context_to_dict(context):
~~    if isinstance(context, Context):
        flat = {}
        for d in context.dicts:
            flat.update(d)
        context = flat

    return context


def user_is_authenticated(user):
    if not hasattr(user.is_authenticated, '__call__'):
        return user.is_authenticated
    else:
        return user.is_authenticated()



## ... source file continues with no further Context examples...

```


## Example 9 from django-markdown-view
[django-markdown-view](https://github.com/rgs258/django-markdown-view)
([PyPI package information](https://pypi.org/project/django-markdown-view/))
is a Django extension for serving [Markdown](/markdown.html) files as
[Django templates](/django-templates.html). The project is open
sourced under the
[BSD 3-Clause "New" or "Revised" license](https://github.com/rgs258/django-markdown-view/blob/master/LICENSE).

[**django-markdown-view / markdown_view / views.py**](https://github.com/rgs258/django-markdown-view/blob/master/markdown_view/./views.py)

```python
# views.py
import logging

import markdown
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
~~from django.template import Engine, Template, Context
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView

from markdown_view.constants import (
    DEFAULT_MARKDOWN_VIEW_LOADERS,
    DEFAULT_MARKDOWN_VIEW_EXTENSIONS, DEFAULT_MARKDOWN_VIEW_TEMPLATE,
    DEFAULT_MARKDOWN_VIEW_USE_REQUEST_CONTEXT, DEFAULT_MARKDOWN_VIEW_EXTRA_CONTEXT,
    DEFAULT_MARKDOWN_VIEW_TEMPLATE_USE_HIGHLIGHT_JS, DEFAULT_MARKDOWN_VIEW_TEMPLATE_USE_TOC,
)

logger = logging.getLogger(__name__)


class MarkdownView(TemplateView):
    file_name = None

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.file_name:
            engine = Engine(loaders=getattr(
                settings, "MARKDOWN_VIEW_LOADERS", DEFAULT_MARKDOWN_VIEW_LOADERS)
            )
            template = engine.get_template(self.file_name)
            md = markdown.Markdown(extensions=getattr(
                settings,
                "MARKDOWN_VIEW_EXTENSIONS",
                DEFAULT_MARKDOWN_VIEW_EXTENSIONS
            ))
            template = Template(
                "{{% load static %}}{}".format(md.convert(template.source))
            )
            render_context_base = {}
            if getattr(
                    settings,
                    "MARKDOWN_VIEW_USE_REQUEST_CONTEXT",
                    DEFAULT_MARKDOWN_VIEW_USE_REQUEST_CONTEXT
            ):
                render_context_base = context
~~            render_context = Context({
                **render_context_base,
                **(getattr(
                    settings,
                    "MARKDOWN_VIEW_EXTRA_CONTEXT",
                    DEFAULT_MARKDOWN_VIEW_EXTRA_CONTEXT
                ))
            })
            context.update({
                "markdown_content": mark_safe(template.render(render_context)),
                "use_highlight_js": getattr(
                    settings,
                    "MARKDOWN_VIEW_TEMPLATE_USE_HIGHLIGHT_JS",
                    DEFAULT_MARKDOWN_VIEW_TEMPLATE_USE_HIGHLIGHT_JS
                ),
                "use_toc": False,
            })

            if getattr(
                    settings,
                    "MARKDOWN_VIEW_TEMPLATE_USE_TOC",
                    DEFAULT_MARKDOWN_VIEW_TEMPLATE_USE_TOC
            ):
                context.update({
                    "markdown_toc": mark_safe(md.toc),


## ... source file continues with no further Context examples...

```


## Example 10 from django-smithy
[django-smithy](https://github.com/jamiecounsell/django-smithy) is
a [Django](/django.html) code library that allows users to send
HTTP requests from the Django admin user interface. The code for
the project is open source under the
[MIT license](https://github.com/jamiecounsell/django-smithy/blob/master/LICENSE).

[**django-smithy / smithy / helpers.py**](https://github.com/jamiecounsell/django-smithy/blob/master/smithy/./helpers.py)

```python
# helpers.py
~~from django.template import Template, Context
from requests_toolbelt.utils import dump

def render_with_context(template, context):
    template = Template(template)
~~    context = Context(context)
    return template.render(context)

def parse_dump_result(fun, obj):
    prefixes = dump.PrefixSettings('', '')
    try:
        result = bytearray()
        fun(obj, prefixes, result)
        return result.decode('utf-8')
    except Exception:
        return "Could not parse request as a string"



## ... source file continues with no further Context examples...

```


## Example 11 from django-tables2
[django-tables2](https://github.com/jieter/django-tables2)
([projection documentation](https://django-tables2.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-tables2/))
is a code library for [Django](/django.html) that simplifies creating and
displaying tables in [Django templates](/django-templates.html),
especially with more advanced features such as pagination and sorting.
The project and its code are
[available as open source](https://github.com/jieter/django-tables2/blob/master/LICENSE).

[**django-tables2 / django_tables2 / columns / templatecolumn.py**](https://github.com/jieter/django-tables2/blob/master/django_tables2/columns/templatecolumn.py)

```python
# templatecolumn.py
~~from django.template import Context, Template
from django.template.loader import get_template
from django.utils.html import strip_tags

from .base import Column, library


@library.register
class TemplateColumn(Column):

    empty_values = ()

    def __init__(self, template_code=None, template_name=None, extra_context=None, **extra):
        super().__init__(**extra)
        self.template_code = template_code
        self.template_name = template_name
        self.extra_context = extra_context or {}

        if not self.template_code and not self.template_name:
            raise ValueError("A template must be provided")

    def render(self, record, table, value, bound_column, **kwargs):
~~        context = getattr(table, "context", Context())
        additional_context = {
            "default": bound_column.default,
            "column": bound_column,
            "record": record,
            "value": value,
            "row_counter": kwargs["bound_row"].row_counter,
        }
        additional_context.update(self.extra_context)
        with context.update(additional_context):
            if self.template_code:
                return Template(self.template_code).render(context)
            else:
                return get_template(self.template_name).render(context.flatten())

    def value(self, **kwargs):
        html = super().value(**kwargs)
        return strip_tags(html) if isinstance(html, str) else html



## ... source file continues with no further Context examples...

```

