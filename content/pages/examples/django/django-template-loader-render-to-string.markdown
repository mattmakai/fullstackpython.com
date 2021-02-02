title: django.template.loader render_to_string Example Code
category: page
slug: django-template-loader-render-to-string-examples
sortorder: 500011393
toc: False
sidebartitle: django.template.loader render_to_string
meta: Python example code that shows how to use the render_to_string callable from the django.template.loader module of the Django project.


`render_to_string` is a callable within the `django.template.loader` module of the Django project.

<a href="/django-template-loader-get-template-examples.html">get_template</a>
and
<a href="/django-template-loader-select-template-examples.html">select_template</a>
are a couple of other callables within the `django.template.loader` package that also have code examples.

## Example 1 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / auth_app / views.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/auth_app/views.py)

```python
# views.py
import json
from urllib.request import Request, urlopen
from urllib.parse import urlencode

from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect, render
~~from django.template.loader import render_to_string
from django.core.mail import send_mail

from .forms import SignUpForm

User = get_user_model()


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urlencode(values).encode()
            req = Request(url, data=data)

            response = urlopen(req)
            result = json.loads(response.read().decode())
            if result['success']:
                user = form.save()
                user.is_active = True
                user.save()
                login(request, user)

                context = {
                    'email': user.email,
                    'protocol': 'https' if request.is_secure() else "http",
                    'domain': request.get_host(),
                }
~~                html = render_to_string('auth_app/email/welcome.html', context)
~~                text = render_to_string('auth_app/email/welcome.txt', context)
                send_mail(
                    'Welcome to DCCN Conference Registration System!',
                    message=text,
                    html_message=html,
                    recipient_list=[user.email],
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    fail_silently=False,
                )
                return redirect('register')
    else:
        form = SignUpForm()
    return render(request, 'auth_app/signup.html', {
        'site_key': settings.RECAPTCHA_SITE_KEY,
        'form': form,
    })


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'auth_app/password_reset_done.html'



## ... source file continues with no further render_to_string examples...

```


## Example 2 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / account / adapter.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/account/adapter.py)

```python
# adapter.py
from __future__ import unicode_literals

import hashlib
import json
import time
import warnings

from django import forms
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    get_backends,
    login as django_login,
    logout as django_logout,
)
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.password_validation import validate_password
from django.contrib.sites.shortcuts import get_current_site
from django.core.cache import cache
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import resolve_url
from django.template import TemplateDoesNotExist
~~from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _

from ..utils import (
    build_absolute_uri,
    email_address_exists,
    generate_unique_username,
    get_user_model,
    import_attribute,
)
from . import app_settings


class DefaultAccountAdapter(object):

    error_messages = {
        "username_blacklisted": _(
            "Username can not be used. Please use other username."
        ),
        "username_taken": AbstractUser._meta.get_field("username").error_messages[
            "unique"
        ],


## ... source file abbreviated to get to render_to_string examples ...


    def stash_user(self, request, user):
        request.session["account_user"] = user

    def unstash_user(self, request):
        return request.session.pop("account_user", None)

    def is_email_verified(self, request, email):
        ret = False
        verified_email = request.session.get("account_verified_email")
        if verified_email:
            ret = verified_email.lower() == email.lower()
        return ret

    def format_email_subject(self, subject):
        prefix = app_settings.EMAIL_SUBJECT_PREFIX
        if prefix is None:
            site = get_current_site(self.request)
            prefix = "[{name}] ".format(name=site.name)
        return prefix + force_str(subject)

    def get_from_email(self):
        return settings.DEFAULT_FROM_EMAIL

    def render_mail(self, template_prefix, email, context):
        to = [email] if isinstance(email, str) else email
~~        subject = render_to_string("{0}_subject.txt".format(template_prefix), context)
        subject = " ".join(subject.splitlines()).strip()
        subject = self.format_email_subject(subject)

        from_email = self.get_from_email()

        bodies = {}
        for ext in ["html", "txt"]:
            try:
                template_name = "{0}_message.{1}".format(template_prefix, ext)
~~                bodies[ext] = render_to_string(
                    template_name,
                    context,
                    self.request,
                ).strip()
            except TemplateDoesNotExist:
                if ext == "txt" and not bodies:
                    raise
        if "txt" in bodies:
            msg = EmailMultiAlternatives(subject, bodies["txt"], from_email, to)
            if "html" in bodies:
                msg.attach_alternative(bodies["html"], "text/html")
        else:
            msg = EmailMessage(subject, bodies["html"], from_email, to)
            msg.content_subtype = "html"  # Main content is now text/html
        return msg

    def send_mail(self, template_prefix, email, context):
        msg = self.render_mail(template_prefix, email, context)
        msg.send()

    def get_signup_redirect_url(self, request):
        return resolve_url(app_settings.SIGNUP_REDIRECT_URL)

    def get_login_redirect_url(self, request):


## ... source file abbreviated to get to render_to_string examples ...


        min_length = app_settings.PASSWORD_MIN_LENGTH
        if min_length and len(password) < min_length:
            raise forms.ValidationError(
                _("Password must be a minimum of {0} " "characters.").format(min_length)
            )
        validate_password(password, user)
        return password

    def validate_unique_email(self, email):
        if email_address_exists(email):
            raise forms.ValidationError(self.error_messages["email_taken"])
        return email

    def add_message(
        self,
        request,
        level,
        message_template,
        message_context=None,
        extra_tags="",
    ):
        if "django.contrib.messages" in settings.INSTALLED_APPS:
            try:
                if message_context is None:
                    message_context = {}
~~                message = render_to_string(
                    message_template,
                    message_context,
                    self.request,
                ).strip()
                if message:
                    messages.add_message(request, level, message, extra_tags=extra_tags)
            except TemplateDoesNotExist:
                pass

    def ajax_response(self, request, response, redirect_to=None, form=None, data=None):
        resp = {}
        status = response.status_code

        if redirect_to:
            status = 200
            resp["location"] = redirect_to
        if form:
            if request.method == "POST":
                if form.is_valid():
                    status = 200
                else:
                    status = 400
            else:
                status = 200


## ... source file continues with no further render_to_string examples...

```


## Example 3 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / templatetags / cms_tags.py**](https://github.com/divio/django-cms/blob/develop/cms/templatetags/cms_tags.py)

```python
# cms_tags.py
from collections import namedtuple, OrderedDict
from copy import copy
from datetime import datetime

from django import template
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import mail_managers
from django.db.models import Model
from django.middleware.common import BrokenLinkEmailsMiddleware
~~from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_text, smart_text
from django.utils.html import escape
from django.utils.http import urlencode
from django.utils.translation import (
    get_language,
    override as force_language,
    gettext_lazy as _,
)

from classytags.arguments import (Argument, MultiValueArgument,
                                  MultiKeywordArgument)
from classytags.core import Options, Tag
from classytags.helpers import InclusionTag, AsTag
from classytags.parser import Parser
from classytags.utils import flatten_context
from classytags.values import ListValue, StringValue

from cms.cache.page import get_page_url_cache, set_page_url_cache
from cms.exceptions import PlaceholderNotFound
from cms.models import Page, Placeholder as PlaceholderModel, CMSPlugin, StaticPlaceholder
from cms.plugin_pool import plugin_pool
from cms.toolbar.utils import get_toolbar_from_request
from cms.utils import get_current_site, get_language_from_request, get_site_id


## ... source file abbreviated to get to render_to_string examples ...


        Argument('edit_fields', default=None, required=False),
        Argument('language', default=None, required=False),
        Argument('filters', default=None, required=False),
        Argument('view_url', default=None, required=False),
        Argument('view_method', default=None, required=False),
        'as',
        Argument('varname', required=False, resolve=False),
    )

    def __init__(self, parser, tokens):
        self.parser = parser
        super().__init__(parser, tokens)

    def _is_editable(self, request):
        return (request and hasattr(request, 'toolbar') and request.toolbar.edit_mode_active)

    def get_template(self, context, **kwargs):
        if self._is_editable(context.get('request', None)):
            return self.edit_template
        return self.template

    def render_tag(self, context, **kwargs):
        context.push()
        template = self.get_template(context, **kwargs)
        data = self.get_context(context, **kwargs)
~~        output = render_to_string(template, flatten_context(data)).strip()
        context.pop()
        if kwargs.get('varname'):
            context[kwargs['varname']] = output
            return ''
        else:
            return output

    def _get_editable_context(self, context, instance, language, edit_fields,
                              view_method, view_url, querystring, editmode=True):
        request = context['request']
        if hasattr(request, 'toolbar'):
            lang = request.toolbar.toolbar_language
        else:
            lang = get_language()
        opts = instance._meta
        if getattr(instance, '_deferred', False):
            opts = opts.proxy_for_model._meta
        with force_language(lang):
            extra_context = {}
            if edit_fields == 'changelist':
                instance.get_plugin_name = u"%s %s list" % (smart_text(_('Edit')), smart_text(opts.verbose_name))
                extra_context['attribute_name'] = 'changelist'
            elif editmode:
                instance.get_plugin_name = u"%s %s" % (smart_text(_('Edit')), smart_text(opts.verbose_name))


## ... source file abbreviated to get to render_to_string examples ...


        extra_context = self._get_empty_context(context, instance, None,
                                                language, view_url,
                                                view_method, editmode=False)
        extra_context['render_model_add'] = True
        return extra_context


class CMSEditableObjectAddBlock(CMSEditableObject):
    name = 'render_model_add_block'
    options = Options(
        Argument('instance'),
        Argument('language', default=None, required=False),
        Argument('view_url', default=None, required=False),
        Argument('view_method', default=None, required=False),
        'as',
        Argument('varname', required=False, resolve=False),
        blocks=[('endrender_model_add_block', 'nodelist')],
    )

    def render_tag(self, context, **kwargs):
        context.push()
        template = self.get_template(context, **kwargs)
        data = self.get_context(context, **kwargs)
        data['content'] = kwargs['nodelist'].render(data)
        data['rendered_content'] = data['content']
~~        output = render_to_string(template, flatten_context(data))
        context.pop()
        if kwargs.get('varname'):
            context[kwargs['varname']] = output
            return ''
        else:
            return output

    def get_context(self, context, **kwargs):
        instance = kwargs.pop('instance')
        if isinstance(instance, Model) and not instance.pk:
            instance.pk = 0
        kwargs.pop('varname')
        kwargs.pop('nodelist')
        extra_context = self._get_empty_context(context, instance, None,
                                                editmode=False, **kwargs)
        extra_context['render_model_add'] = True
        return extra_context


class CMSEditableObjectBlock(CMSEditableObject):
    name = 'render_model_block'
    options = Options(
        Argument('instance'),
        Argument('edit_fields', default=None, required=False),
        Argument('language', default=None, required=False),
        Argument('view_url', default=None, required=False),
        Argument('view_method', default=None, required=False),
        'as',
        Argument('varname', required=False, resolve=False),
        blocks=[('endrender_model_block', 'nodelist')],
    )

    def render_tag(self, context, **kwargs):
        context.push()
        template = self.get_template(context, **kwargs)
        data = self.get_context(context, **kwargs)
        data['content'] = kwargs['nodelist'].render(data)
        data['rendered_content'] = data['content']
~~        output = render_to_string(template, flatten_context(data))
        context.pop()
        if kwargs.get('varname'):
            context[kwargs['varname']] = output
            return ''
        else:
            return output

    def get_context(self, context, **kwargs):
        kwargs.pop('varname')
        kwargs.pop('nodelist')
        extra_context = self._get_empty_context(context, **kwargs)
        extra_context['instance'] = kwargs.get('instance')
        extra_context['render_model_block'] = True
        return extra_context


class StaticPlaceholderNode(Tag):
    name = 'static_placeholder'
    options = PlaceholderOptions(
        Argument('code', required=True),
        MultiValueArgument('extra_bits', required=False, resolve=False),
        blocks=[
            ('endstatic_placeholder', 'nodelist'),
        ]


## ... source file continues with no further render_to_string examples...

```


## Example 4 from django-debug-toolbar
[django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)
([project documentation](https://github.com/jazzband/django-debug-toolbar)
and [PyPI page](https://pypi.org/project/django-debug-toolbar/))
grants a developer detailed request-response cycle information while
developing a [Django](/django.html) web application.
The code for django-debug-toolbar is
[open source](https://github.com/jazzband/django-debug-toolbar/blob/master/LICENSE)
and maintained by the developer community group known as
[Jazzband](https://jazzband.co/).

[**django-debug-toolbar / debug_toolbar / toolbar.py**](https://github.com/jazzband/django-debug-toolbar/blob/master/debug_toolbar/./toolbar.py)

```python
# toolbar.py

import uuid
from collections import OrderedDict

from django.apps import apps
from django.core.exceptions import ImproperlyConfigured
from django.template import TemplateSyntaxError
~~from django.template.loader import render_to_string
from django.urls import path
from django.utils.module_loading import import_string

from debug_toolbar import settings as dt_settings


class DebugToolbar:
    def __init__(self, request, get_response):
        self.request = request
        self.config = dt_settings.get_config().copy()
        panels = []
        for panel_class in reversed(self.get_panel_classes()):
            panel = panel_class(self, get_response)
            panels.append(panel)
            if panel.enabled:
                get_response = panel.process_request
        self.process_request = get_response
        self._panels = OrderedDict()
        while panels:
            panel = panels.pop()
            self._panels[panel.panel_id] = panel
        self.stats = {}
        self.server_timing_stats = {}
        self.store_id = None


    @property
    def panels(self):
        return list(self._panels.values())

    @property
    def enabled_panels(self):
        return [panel for panel in self._panels.values() if panel.enabled]

    def get_panel_by_id(self, panel_id):
        return self._panels[panel_id]


    def render_toolbar(self):
        if not self.should_render_panels():
            self.store()
        try:
            context = {"toolbar": self}
~~            return render_to_string("debug_toolbar/base.html", context)
        except TemplateSyntaxError:
            if not apps.is_installed("django.contrib.staticfiles"):
                raise ImproperlyConfigured(
                    "The debug toolbar requires the staticfiles contrib app. "
                    "Add 'django.contrib.staticfiles' to INSTALLED_APPS and "
                    "define STATIC_URL in your settings."
                )
            else:
                raise

    def should_render_panels(self):
        render_panels = self.config["RENDER_PANELS"]
        if render_panels is None:
            render_panels = self.request.META["wsgi.multiprocess"]
        return render_panels


    _store = OrderedDict()

    def store(self):
        if self.store_id:
            return
        self.store_id = uuid.uuid4().hex
        self._store[self.store_id] = self


## ... source file continues with no further render_to_string examples...

```


## Example 5 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / fields / folder.py**](https://github.com/divio/django-filer/blob/develop/filer/fields/folder.py)

```python
# folder.py
from __future__ import absolute_import

import warnings

from django import forms
from django.contrib.admin.sites import site
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
~~from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.safestring import mark_safe

from ..models import Folder
from ..utils.compatibility import truncate_words
from ..utils.model_label import get_model_label


class AdminFolderWidget(ForeignKeyRawIdWidget):
    choices = None
    input_type = 'hidden'
    is_hidden = False

    def render(self, name, value, attrs=None, renderer=None):
        obj = self.obj_for_value(value)
        css_id = attrs.get('id')
        css_id_folder = "%s_folder" % css_id
        css_id_description_txt = "%s_description_txt" % css_id
        if attrs is None:
            attrs = {}
        related_url = None

        if value:


## ... source file abbreviated to get to render_to_string examples ...


        if not related_url:
            related_url = reverse('admin:filer-directory_listing-last')
        params = self.url_parameters()
        params['_pick'] = 'folder'
        if params:
            url = '?' + urlencode(sorted(params.items()))
        else:
            url = ''
        if 'class' not in attrs:
            attrs['class'] = 'vForeignKeyRawIdAdminField'
        super_attrs = attrs.copy()
        hidden_input = super(ForeignKeyRawIdWidget, self).render(name, value, super_attrs)

        context = {
            'hidden_input': hidden_input,
            'lookup_url': '%s%s' % (related_url, url),
            'lookup_name': name,
            'span_id': css_id_description_txt,
            'object': obj,
            'clear_id': '%s_clear' % css_id,
            'descid': css_id_description_txt,
            'noimg': 'filer/icons/nofile_32x32.png',
            'foldid': css_id_folder,
            'id': css_id,
        }
~~        html = render_to_string('admin/filer/widgets/admin_folder.html', context)
        return mark_safe(html)

    def label_for_value(self, value):
        obj = self.obj_for_value(value)
        return '&nbsp;<strong>%s</strong>' % truncate_words(obj, 14)

    def obj_for_value(self, value):
        if not value:
            return None
        try:
            key = self.rel.get_related_field().name
            obj = self.rel.model._default_manager.get(**{key: value})
        except ObjectDoesNotExist:
            obj = None
        return obj

    class Media(object):
        js = (
            'filer/js/addons/popup_handling.js',
        )


class AdminFolderFormField(forms.ModelChoiceField):
    widget = AdminFolderWidget


## ... source file continues with no further render_to_string examples...

```


## Example 6 from django-haystack
[django-haystack](https://github.com/django-haystack/django-haystack)
([project website](http://haystacksearch.org/) and
[PyPI page](https://pypi.org/project/django-haystack/))
is a search abstraction layer that separates the Python search code
in a [Django](/django.html) web application from the search engine
implementation that it runs on, such as
[Apache Solr](http://lucene.apache.org/solr/),
[Elasticsearch](https://www.elastic.co/)
or [Whoosh](https://whoosh.readthedocs.io/en/latest/intro.html).

The django-haystack project is open source under the
[BSD license](https://github.com/django-haystack/django-haystack/blob/master/LICENSE).

[**django-haystack / haystack / panels.py**](https://github.com/django-haystack/django-haystack/blob/master/haystack/./panels.py)

```python
# panels.py
import datetime

from debug_toolbar.panels import DebugPanel
~~from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from haystack import connections


class HaystackDebugPanel(DebugPanel):

    name = "Haystack"
    has_content = True

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self._offset = dict(
            (alias, len(connections[alias].queries))
            for alias in connections.connections_info.keys()
        )
        self._search_time = 0
        self._queries = []
        self._backends = {}

    def nav_title(self):
        return _("Haystack")

    def nav_subtitle(self):


## ... source file abbreviated to get to render_to_string examples ...


            if query.get("additional_kwargs"):
                if query["additional_kwargs"].get("result_class"):
                    query["additional_kwargs"]["result_class"] = str(
                        query["additional_kwargs"]["result_class"]
                    )

            try:
                query["width_ratio"] = (float(query["time"]) / self._search_time) * 100
            except ZeroDivisionError:
                query["width_ratio"] = 0

            query["start_offset"] = width_ratio_tally
            width_ratio_tally += query["width_ratio"]

        context = self.context.copy()
        context.update(
            {
                "backends": sorted(
                    self._backends.items(), key=lambda x: -x[1]["time_spent"]
                ),
                "queries": [q for a, q in self._queries],
                "sql_time": self._search_time,
            }
        )

~~        return render_to_string("panels/haystack.html", context)



## ... source file continues with no further render_to_string examples...

```


## Example 7 from django-jet
[django-jet](https://github.com/geex-arts/django-jet)
([project documentation](https://jet.readthedocs.io/en/latest/),
[PyPI project page](https://pypi.org/project/django-jet/) and
[more information](http://jet.geex-arts.com/))
is a fancy [Django](/django.html) Admin panel replacement.

The django-jet project is open source under the
[GNU Affero General Public License v3.0](https://github.com/geex-arts/django-jet/blob/dev/LICENSE).

[**django-jet / jet / dashboard / dashboard.py**](https://github.com/geex-arts/django-jet/blob/dev/jet/dashboard/dashboard.py)

```python
# dashboard.py
from importlib import import_module
try:
    from django.core.urlresolvers import reverse
except ImportError: # Django 1.11
    from django.urls import reverse

~~from django.template.loader import render_to_string
from jet.dashboard import modules
from jet.dashboard.models import UserDashboardModule
from django.utils.translation import ugettext_lazy as _
from jet.ordered_set import OrderedSet
from jet.utils import get_admin_site_name, context_to_dict

try:
    from django.template.context_processors import csrf
except ImportError:
    from django.core.context_processors import csrf


class Dashboard(object):

    columns = 2

    children = None

    available_children = None
    app_label = None
    context = None
    modules = None

    class Media:


## ... source file abbreviated to get to render_to_string examples ...


            user=self.context['request'].user.pk
        ).all()

        if len(module_models) == 0:
            module_models = self.create_initial_module_models(self.context['request'].user)

        loaded_modules = []

        for module_model in module_models:
            module_cls = module_model.load_module()
            if module_cls is not None:
                module = module_cls(model=module_model, context=self.context)
                loaded_modules.append(module)

        self.modules = loaded_modules

    def render(self):
        context = context_to_dict(self.context)
        context.update({
            'columns': range(self.columns),
            'modules': self.modules,
            'app_label': self.app_label,
        })
        context.update(csrf(context['request']))

~~        return render_to_string('jet.dashboard/dashboard.html', context)

    def render_tools(self):
        context = context_to_dict(self.context)
        context.update({
            'children': self.children,
            'app_label': self.app_label,
            'available_children': self.available_children
        })
        context.update(csrf(context['request']))

~~        return render_to_string('jet.dashboard/dashboard_tools.html', context)

    def media(self):
        unique_css = OrderedSet()
        unique_js = OrderedSet()

        for js in getattr(self.Media, 'js', ()):
            unique_js.add(js)
        for css in getattr(self.Media, 'css', ()):
            unique_css.add(css)

        for module in self.modules:
            for js in getattr(module.Media, 'js', ()):
                unique_js.add(js)
            for css in getattr(module.Media, 'css', ()):
                unique_css.add(css)

        class Media:
            css = list(unique_css)
            js = list(unique_js)

        return Media


class AppIndexDashboard(Dashboard):


## ... source file continues with no further render_to_string examples...

```


## Example 8 from django-pipeline
[django-pipeline](https://github.com/jazzband/django-pipeline)
([project documentation](https://django-pipeline.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-pipeline/))
is a code library for handling and compressing
[static content assets](/static-content.html) when handling requests in
[Django](/django.html) web applications.

The django-pipeline project is open sourced under the
[MIT License](https://github.com/jazzband/django-pipeline/blob/master/LICENSE.txt)
and it is maintained by the developer community group
[Jazzband](https://jazzband.co/).

[**django-pipeline / pipeline / templatetags / pipeline.py**](https://github.com/jazzband/django-pipeline/blob/master/pipeline/templatetags/pipeline.py)

```python
# pipeline.py
import logging
import subprocess

from django.contrib.staticfiles.storage import staticfiles_storage

from django import template
from django.template.base import VariableDoesNotExist
~~from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from ..collector import default_collector
from ..conf import settings
from ..exceptions import CompilerError
from ..packager import Packager, PackageNotFound
from ..utils import guess_type

logger = logging.getLogger(__name__)

register = template.Library()


class PipelineMixin(object):
    request = None
    _request_var = None

    @property
    def request_var(self):
        if not self._request_var:
            self._request_var = template.Variable('request')
        return self._request_var

    def package_for(self, package_name, package_type):


## ... source file abbreviated to get to render_to_string examples ...


        method = getattr(self, f'render_{package_type}')

        return method(package, package.output_filename)

    def render_compressed_sources(self, package, package_name, package_type):
        if settings.PIPELINE_COLLECTOR_ENABLED:
            default_collector.collect(self.request)

        packager = Packager()
        method = getattr(self, f'render_individual_{package_type}')

        try:
            paths = packager.compile(package.paths)
        except CompilerError as e:
            if settings.SHOW_ERRORS_INLINE:
                method = getattr(self, f'render_error_{package_type}')
                return method(package_name, e)
            else:
                raise

        templates = packager.pack_templates(package)

        return method(package, paths, templates=templates)

    def render_error(self, package_type, package_name, e):
~~        return render_to_string('pipeline/compile_error.html', {
            'package_type': package_type,
            'package_name': package_name,
            'command': subprocess.list2cmdline(e.command),
            'errors': e.error_output,
        })


class StylesheetNode(PipelineMixin, template.Node):
    def __init__(self, name):
        self.name = name

    def render(self, context):
        super(StylesheetNode, self).render(context)
        package_name = template.Variable(self.name).resolve(context)

        try:
            package = self.package_for(package_name, 'css')
        except PackageNotFound:
            logger.warn("Package %r is unknown. Check PIPELINE['STYLESHEETS'] in your settings.", package_name)
            return ''  # fail silently, do not return anything if an invalid group is specified
        return self.render_compressed(package, package_name, 'css')

    def render_css(self, package, path):
        template_name = package.template_name or "pipeline/css.html"
        context = package.extra_context
        context.update({
            'type': guess_type(path, 'text/css'),
            'url': mark_safe(staticfiles_storage.url(path))
        })
~~        return render_to_string(template_name, context)

    def render_individual_css(self, package, paths, **kwargs):
        tags = [self.render_css(package, path) for path in paths]
        return '\n'.join(tags)

    def render_error_css(self, package_name, e):
        return super(StylesheetNode, self).render_error(
            'CSS', package_name, e)


class JavascriptNode(PipelineMixin, template.Node):
    def __init__(self, name):
        self.name = name

    def render(self, context):
        super(JavascriptNode, self).render(context)
        package_name = template.Variable(self.name).resolve(context)

        try:
            package = self.package_for(package_name, 'js')
        except PackageNotFound:
            logger.warn("Package %r is unknown. Check PIPELINE['JAVASCRIPT'] in your settings.", package_name)
            return ''  # fail silently, do not return anything if an invalid group is specified
        return self.render_compressed(package, package_name, 'js')

    def render_js(self, package, path):
        template_name = package.template_name or "pipeline/js.html"
        context = package.extra_context
        context.update({
            'type': guess_type(path, 'text/javascript'),
            'url': mark_safe(staticfiles_storage.url(path))
        })
~~        return render_to_string(template_name, context)

    def render_inline(self, package, js):
        context = package.extra_context
        context.update({
            'source': js
        })
~~        return render_to_string("pipeline/inline_js.html", context)

    def render_individual_js(self, package, paths, templates=None):
        tags = [self.render_js(package, js) for js in paths]
        if templates:
            tags.append(self.render_inline(package, templates))
        return '\n'.join(tags)

    def render_error_js(self, package_name, e):
        return super(JavascriptNode, self).render_error(
            'JavaScript', package_name, e)


@register.tag
def stylesheet(parser, token):
    try:
        tag_name, name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError('%r requires exactly one argument: the name of a group in the PIPELINE.STYLESHEETS setting' % token.split_contents()[0])
    return StylesheetNode(name)


@register.tag
def javascript(parser, token):
    try:


## ... source file continues with no further render_to_string examples...

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

[**django-wiki / src/wiki / decorators.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/./decorators.py)

```python
# decorators.py
from functools import wraps
from urllib.parse import quote as urlquote

from django.http import HttpResponseForbidden
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
~~from django.template.loader import render_to_string
from django.urls import reverse
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
~~            render_to_string(
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
                return redirect("wiki:root_create")
            except models.URLPath.DoesNotExist:
                try:
                    pathlist = list(
                        filter(
                            lambda x: x != "",
                            path.split("/"),
                        )
                    )
                    path = "/".join(pathlist[:-1])
                    parent = models.URLPath.get_by_path(path)
                    return HttpResponseRedirect(
                        reverse("wiki:create", kwargs={"path": parent.path})
                        + "?slug=%s" % pathlist[-1].lower()
                    )
                except models.URLPath.DoesNotExist:
                    return HttpResponseNotFound(
~~                        render_to_string(
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



## ... source file continues with no further render_to_string examples...

```


## Example 10 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / snippets / widgets.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/snippets/widgets.py)

```python
# widgets.py
import json

from django import forms
from django.contrib.admin.utils import quote
~~from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from wagtail.admin.staticfiles import versioned_static
from wagtail.admin.widgets import AdminChooser
from wagtail.admin.widgets.button import ListingButton


class AdminSnippetChooser(AdminChooser):

    def __init__(self, model, **kwargs):
        self.target_model = model
        name = self.target_model._meta.verbose_name
        self.choose_one_text = _('Choose %s') % name
        self.choose_another_text = _('Choose another %s') % name
        self.link_to_chosen_text = _('Edit this %s') % name

        super().__init__(**kwargs)

    def get_value_data(self, value):
        if value is None:
            return None
        elif isinstance(value, self.target_model):
            instance = value
        else:  # assume instance ID
            instance = self.target_model.objects.get(pk=value)

        app_label = self.target_model._meta.app_label
        model_name = self.target_model._meta.model_name
        quoted_id = quote(instance.pk)
        edit_url = reverse('wagtailsnippets:edit', args=[app_label, model_name, quoted_id])

        return {
            'id': instance.pk,
            'string': str(instance),
            'edit_url': edit_url,
        }

    def render_html(self, name, value_data, attrs):
        value_data = value_data or {}

        original_field_html = super().render_html(name, value_data.get('id'), attrs)

~~        return render_to_string("wagtailsnippets/widgets/snippet_chooser.html", {
            'widget': self,
            'original_field_html': original_field_html,
            'attrs': attrs,
            'value': bool(value_data),  # only used by chooser.html to identify blank values
            'display_title': value_data.get('string', ''),
            'edit_url': value_data.get('edit_url', ''),
        })

    def render_js_init(self, id_, name, value_data):
        model = self.target_model

        return "createSnippetChooser({id}, {model});".format(
            id=json.dumps(id_),
            model=json.dumps('{app}/{model}'.format(
                app=model._meta.app_label,
                model=model._meta.model_name)))

    @property
    def media(self):
        return forms.Media(js=[
            versioned_static('wagtailsnippets/js/snippet-chooser-modal.js'),
            versioned_static('wagtailsnippets/js/snippet-chooser.js'),
        ])



## ... source file continues with no further render_to_string examples...

```

