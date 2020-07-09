title: django.utils.module_loading import_string Example Code
category: page
slug: django-utils-module-loading-import-string-examples
sortorder: 500011481
toc: False
sidebartitle: django.utils.module_loading import_string
meta: Python example code for the import_string callable from the django.utils.module_loading module of the Django project.


import_string is a callable within the django.utils.module_loading module of the Django project.


## Example 1 from django-angular
[django-angular](https://github.com/jrief/django-angular)
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / forms / angular_base.py**](https://github.com/jrief/django-angular/blob/master/djng/forms/angular_base.py)

```python
# angular_base.py
from base64 import b64encode
from collections import UserList
import json
import warnings

from django.forms import forms
from django.http import QueryDict
from django.utils.html import format_html, format_html_join, escape, conditional_escape
from django.utils.encoding import force_text
~~from django.utils.module_loading import import_string
from django.utils.safestring import mark_safe, SafeText, SafeData
from django.core.exceptions import ValidationError, ImproperlyConfigured

from .fields import DefaultFieldMixin


class SafeTuple(SafeData, tuple):


class TupleErrorList(UserList, list):
    def __init__(self, initlist=None, error_class=None):
        super(TupleErrorList, self).__init__(initlist)

        if error_class is None:
            self.error_class = 'errorlist'
        else:
            self.error_class = 'errorlist {}'.format(error_class)

    def as_data(self):
        return ValidationError(self.data).error_list

    def get_json_data(self, escape_html=False):
        errors = []
        for error in self.as_data():


## ... source file abbreviated to get to import_string examples ...


        elif isinstance(label_css_classes, dict):
            for key in (self.name, '*',):
                extra_label_classes = label_css_classes.get(key)
                if hasattr(extra_label_classes, 'split'):
                    extra_label_classes = extra_label_classes.split()
                extra_label_classes = set(extra_label_classes or [])
                css_classes.update(extra_label_classes)
        if css_classes:
            attrs.update({'class': ' '.join(css_classes)})
        return super(NgBoundField, self).label_tag(contents, attrs, label_suffix='')


class BaseFieldsModifierMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs.update(formfield_callback=cls.formfield_callback)
        new_class = super(BaseFieldsModifierMetaclass, cls).__new__(cls, name, bases, attrs)
        cls.validate_formfields(new_class)
        return new_class

    @classmethod
    def formfield_callback(cls, modelfield, **kwargs):
        formfield = modelfield.formfield(**kwargs)

        if formfield:
            try:
~~                formfield_class = import_string('djng.forms.fields.' + formfield.__class__.__name__)
            except ImportError: # form field not declared by Django
                formfield_class = type(str(formfield.__class__.__name__), (DefaultFieldMixin, formfield.__class__), {})

            if hasattr(formfield, 'choices'):
                kwargs.update(choices_form_class=formfield_class)
            kwargs.update(form_class=formfield_class)
            formfield = modelfield.formfield(**kwargs)
        return formfield

    @classmethod
    def validate_formfields(cls, new_class):
        msg = "Please use the corresponding form fields from 'djng.forms.fields' for field '{} = {}(...)' " \
              "in form '{}', which inherits from 'NgForm' or 'NgModelForm'."
        for name, field in new_class.base_fields.items():
            if not isinstance(field, DefaultFieldMixin):
                raise ImproperlyConfigured(msg.format(name, field.__class__.__name__, new_class))


class NgFormBaseMixin(object):
    form_error_css_classes = 'djng-form-errors'
    field_error_css_classes = 'djng-field-errors'

    def __init__(self, *args, **kwargs):
        try:


## ... source file continues with no further import_string examples...

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

[**django-axes / axes / checks.py**](https://github.com/jazzband/django-axes/blob/master/axes/./checks.py)

```python
# checks.py
from django.core.checks import (  # pylint: disable=redefined-builtin
    Tags,
    Warning,
    register,
)
~~from django.utils.module_loading import import_string

from axes.backends import AxesBackend
from axes.conf import settings


class Messages:
    CACHE_INVALID = (
        "You are using the django-axes cache handler for login attempt tracking."
        " Your cache configuration is however invalid and will not work correctly with django-axes."
        " This can leave security holes in your login systems as attempts are not tracked correctly."
        " Reconfigure settings.AXES_CACHE and settings.CACHES per django-axes configuration documentation."
    )
    MIDDLEWARE_INVALID = (
        "You do not have 'axes.middleware.AxesMiddleware' in your settings.MIDDLEWARE."
    )
    BACKEND_INVALID = "You do not have 'axes.backends.AxesBackend' or a subclass in your settings.AUTHENTICATION_BACKENDS."
    SETTING_DEPRECATED = "You have a deprecated setting {deprecated_setting} configured in your project settings"


class Hints:
    CACHE_INVALID = None
    MIDDLEWARE_INVALID = None
    BACKEND_INVALID = (
        "AxesModelBackend was renamed to AxesBackend in django-axes version 5.0."


## ... source file abbreviated to get to import_string examples ...




@register(Tags.security, Tags.compatibility)
def axes_middleware_check(app_configs, **kwargs):  # pylint: disable=unused-argument
    warnings = []

    if "axes.middleware.AxesMiddleware" not in settings.MIDDLEWARE:
        warnings.append(
            Warning(
                msg=Messages.MIDDLEWARE_INVALID,
                hint=Hints.MIDDLEWARE_INVALID,
                id=Codes.MIDDLEWARE_INVALID,
            )
        )

    return warnings


@register(Tags.security, Tags.compatibility)
def axes_backend_check(app_configs, **kwargs):  # pylint: disable=unused-argument
    warnings = []

    found = False
    for name in settings.AUTHENTICATION_BACKENDS:
        try:
~~            backend = import_string(name)
        except ModuleNotFoundError as e:
            raise ModuleNotFoundError(
                "Can not find module path defined in settings.AUTHENTICATION_BACKENDS"
            ) from e
        except ImportError as e:
            raise ImportError(
                "Can not import backend class defined in settings.AUTHENTICATION_BACKENDS"
            ) from e

        if issubclass(backend, AxesBackend):
            found = True
            break

    if not found:
        warnings.append(
            Warning(
                msg=Messages.BACKEND_INVALID,
                hint=Hints.BACKEND_INVALID,
                id=Codes.BACKEND_INVALID,
            )
        )

    return warnings



## ... source file continues with no further import_string examples...

```


## Example 3 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / toolbar_pool.py**](https://github.com/divio/django-cms/blob/develop/cms/./toolbar_pool.py)

```python
# toolbar_pool.py
from collections import OrderedDict

from django.core.exceptions import ImproperlyConfigured
~~from django.utils.module_loading import autodiscover_modules, import_string

from cms.exceptions import ToolbarAlreadyRegistered, ToolbarNotRegistered
from cms.utils.conf import get_cms_setting


class ToolbarPool(object):
    def __init__(self):
        self.toolbars = OrderedDict()
        self._discovered = False
        self.force_register = False

    def discover_toolbars(self):
        if self._discovered:
            return
        toolbars = get_cms_setting('TOOLBARS')
        if toolbars:
            for path in toolbars:
~~                cls = import_string(path)
                self.force_register = True
                self.register(cls)
                self.force_register = False
        else:
            autodiscover_modules('cms_toolbars')
        self._discovered = True

    def clear(self):
        self.toolbars = OrderedDict()
        self._discovered = False

    def register(self, toolbar):
        if not self.force_register and get_cms_setting('TOOLBARS'):
            return toolbar
        from cms.toolbar_base import CMSToolbar
        if not issubclass(toolbar, CMSToolbar):
            raise ImproperlyConfigured('CMS Toolbar must inherit '
                                       'cms.toolbar_base.CMSToolbar, %r does not' % toolbar)
        name = "%s.%s" % (toolbar.__module__, toolbar.__name__)
        if name in self.toolbars.keys():
            raise ToolbarAlreadyRegistered("[%s] a toolbar with this name is already registered" % name)
        self.toolbars[name] = toolbar
        return toolbar



## ... source file continues with no further import_string examples...

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

[**django-debug-toolbar / debug_toolbar / apps.py**](https://github.com/jazzband/django-debug-toolbar/blob/master/debug_toolbar/./apps.py)

```python
# apps.py
import inspect

from django.apps import AppConfig
from django.conf import settings
from django.core.checks import Warning, register
from django.middleware.gzip import GZipMiddleware
~~from django.utils.module_loading import import_string
from django.utils.translation import gettext_lazy as _


class DebugToolbarConfig(AppConfig):
    name = "debug_toolbar"
    verbose_name = _("Debug Toolbar")


@register
def check_middleware(app_configs, **kwargs):
    from debug_toolbar.middleware import DebugToolbarMiddleware

    errors = []
    gzip_index = None
    debug_toolbar_indexes = []

    if settings.is_overridden("MIDDLEWARE_CLASSES"):
        errors.append(
            Warning(
                "debug_toolbar is incompatible with MIDDLEWARE_CLASSES setting.",
                hint="Use MIDDLEWARE instead of MIDDLEWARE_CLASSES",
                id="debug_toolbar.W004",
            )
        )


## ... source file abbreviated to get to import_string examples ...


        errors.append(
            Warning(
                "debug_toolbar.middleware.DebugToolbarMiddleware occurs "
                "multiple times in MIDDLEWARE.",
                hint="Load debug_toolbar.middleware.DebugToolbarMiddleware only "
                "once in MIDDLEWARE.",
                id="debug_toolbar.W002",
            )
        )
    elif gzip_index is not None and debug_toolbar_indexes[0] < gzip_index:
        errors.append(
            Warning(
                "debug_toolbar.middleware.DebugToolbarMiddleware occurs before "
                "django.middleware.gzip.GZipMiddleware in MIDDLEWARE.",
                hint="Move debug_toolbar.middleware.DebugToolbarMiddleware to "
                "after django.middleware.gzip.GZipMiddleware in MIDDLEWARE.",
                id="debug_toolbar.W003",
            )
        )

    return errors


def is_middleware_class(middleware_class, middleware_path):
    try:
~~        middleware_cls = import_string(middleware_path)
    except ImportError:
        return
    return inspect.isclass(middleware_cls) and issubclass(
        middleware_cls, middleware_class
    )



## ... source file continues with no further import_string examples...

```


## Example 5 from django-extensions
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

[**django-extensions / django_extensions / collision_resolvers.py**](https://github.com/django-extensions/django-extensions/blob/master/django_extensions/./collision_resolvers.py)

```python
# collision_resolvers.py
import inspect
import sys
from abc import abstractmethod, ABCMeta
from typing import (  # NOQA
    Dict,
    List,
    Optional,
    Tuple,
)

~~from django.utils.module_loading import import_string
from six import add_metaclass


@add_metaclass(ABCMeta)
class BaseCR:

    @classmethod
    def get_app_name_and_model(cls, full_model_path):  # type: (str) -> Tuple[str, str]
~~        model_class = import_string(full_model_path)
        return model_class._meta.app_config.name, model_class.__name__

    @abstractmethod
    def resolve_collisions(self, namespace):  # type: (Dict[str, List[str]]) -> Dict[str, str]
        pass


class LegacyCR(BaseCR):

    def resolve_collisions(self, namespace):
        result = {}
        for name, models in namespace.items():
            result[name] = models[-1]
        return result


@add_metaclass(ABCMeta)
class AppsOrderCR(LegacyCR):
    APP_PRIORITIES = None  # type: List[str]

    def resolve_collisions(self, namespace):
        assert self.APP_PRIORITIES is not None, "You must define APP_PRIORITIES in your resolver class!"
        result = {}
        for name, models in namespace.items():


## ... source file abbreviated to get to import_string examples ...


    MODIFICATION_STRING = "{model_name}_{app_name}"


class AppNamePrefixCustomOrderCR(AppNamePrefixCR, InstalledAppsOrderCR):

    pass


class AppNameSuffixCustomOrderCR(AppNameSuffixCR, InstalledAppsOrderCR):

    pass


class FullPathCustomOrderCR(FullPathCR, InstalledAppsOrderCR):

    pass


@add_metaclass(ABCMeta)
class AppLabelCR(PathBasedCR):

    MODIFICATION_STRING = None  # type: Optional[str]

    def transform_import(self, module_path):
        assert self.MODIFICATION_STRING is not None, "You must define MODIFICATION_STRING in your resolver class!"
~~        model_class = import_string(module_path)
        app_label, model_name = model_class._meta.app_label, model_class.__name__
        return self.MODIFICATION_STRING.format(app_label=app_label, model_name=model_name)


class AppLabelPrefixCR(AppLabelCR):

    MODIFICATION_STRING = "{app_label}_{model_name}"


class AppLabelSuffixCR(AppLabelCR):

    MODIFICATION_STRING = "{model_name}_{app_label}"


class CollisionResolvingRunner:
    def __init__(self):
        pass

    def run_collision_resolver(self, models_to_import):
        dictionary_of_names = self._get_dictionary_of_names(models_to_import)  # type: Dict[str, str]
        return self._get_dictionary_of_modules(dictionary_of_names)

    @classmethod
    def _get_dictionary_of_names(cls, models_to_import):  # type: (Dict[str, List[str]]) -> (Dict[str, str])
        from django.conf import settings
~~        collision_resolver_class = import_string(getattr(
            settings, 'SHELL_PLUS_MODEL_IMPORTS_RESOLVER',
            'django_extensions.collision_resolvers.LegacyCR'
        ))

        cls._assert_is_collision_resolver_class_correct(collision_resolver_class)
        result = collision_resolver_class().resolve_collisions(models_to_import)
        cls._assert_is_collision_resolver_result_correct(result)

        return result

    @classmethod
    def _assert_is_collision_resolver_result_correct(cls, result):
        assert isinstance(result, dict), "Result of resolve_collisions function must be a dict!"
        for key, value in result.items():
            assert isinstance(key, str), "key in collision resolver result should be str not %s" % key
            assert isinstance(value, str), "value in collision resolver result should be str not %s" % value

    @classmethod
    def _assert_is_collision_resolver_class_correct(cls, collision_resolver_class):
        assert inspect.isclass(collision_resolver_class) and issubclass(
            collision_resolver_class, BaseCR), "SHELL_PLUS_MODEL_IMPORTS_RESOLVER " \
                                               "must be subclass of BaseCR!"
        assert len(inspect.getfullargspec(collision_resolver_class.resolve_collisions).args) == 2, \
            "resolve_collisions function must take one argument!"


## ... source file continues with no further import_string examples...

```


## Example 6 from django-guardian
[django-guardian](https://github.com/django-guardian/django-guardian)
([project documentation](https://django-guardian.readthedocs.io/en/stable/)
and
[PyPI page](https://pypi.org/project/django-guardian/))
provides per-object permissions in [Django](/django.html) projects
by enhancing the existing authentication backend. The project's code
is open source under the
[MIT license](https://github.com/django-guardian/django-guardian/blob/devel/LICENSE).

[**django-guardian / guardian / ctypes.py**](https://github.com/django-guardian/django-guardian/blob/devel/guardian/./ctypes.py)

```python
# ctypes.py
from django.contrib.contenttypes.models import ContentType
~~from django.utils.module_loading import import_string

from guardian.conf import settings as guardian_settings


def get_content_type(obj):
~~    get_content_type_function = import_string(
        guardian_settings.GET_CONTENT_TYPE)
    return get_content_type_function(obj)


def get_default_content_type(obj):
    return ContentType.objects.get_for_model(obj)



## ... source file continues with no further import_string examples...

```


## Example 7 from django-import-export
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
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_str
~~from django.utils.module_loading import import_string
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
~~    TMP_STORAGE_CLASS = import_string(TMP_STORAGE_CLASS)


class ImportExportMixinBase:
    def get_model_info(self):
        app_label = self.model._meta.app_label
        return (app_label, self.model._meta.model_name)


class ImportMixin(ImportExportMixinBase):

    change_list_template = 'admin/import_export/change_list_import.html'
    import_template_name = 'admin/import_export/import.html'
    resource_class = None
    formats = DEFAULT_FORMATS
    from_encoding = "utf-8"
    skip_admin_log = None
    tmp_storage_class = None

    def get_skip_admin_log(self):
        if self.skip_admin_log is None:
            return SKIP_ADMIN_LOG
        else:
            return self.skip_admin_log



## ... source file continues with no further import_string examples...

```


## Example 8 from django-push-notifications
[django-push-notifications](https://github.com/jazzband/django-push-notifications)
is a [Django](/django.html) app for storing and interacting with
push notification services such as
[Google's Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/)
and
[Apple Notifications](https://developer.apple.com/notifications/).
The django-push-notification project's source code is available
open source under the
[MIT license](https://github.com/jazzband/django-push-notifications/blob/master/LICENSE).

[**django-push-notifications / push_notifications / conf / __init__.py**](https://github.com/jazzband/django-push-notifications/blob/master/push_notifications/conf/__init__.py)

```python
# __init__.py
~~from django.utils.module_loading import import_string

from .app import AppConfig  # noqa: F401
from .appmodel import AppModelConfig  # noqa: F401
from .legacy import LegacyConfig  # noqa: F401
from ..settings import PUSH_NOTIFICATIONS_SETTINGS as SETTINGS  # noqa: I001


manager = None


def get_manager(reload=False):
	global manager

	if not manager or reload is True:
~~		manager = import_string(SETTINGS["CONFIG"])()

	return manager


get_manager()



## ... source file continues with no further import_string examples...

```


## Example 9 from django-rest-framework
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

[**django-rest-framework / rest_framework / settings.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./settings.py)

```python
# settings.py
from django.conf import settings
from django.test.signals import setting_changed
~~from django.utils.module_loading import import_string

from rest_framework import ISO_8601

DEFAULTS = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_THROTTLE_CLASSES': [],
    'DEFAULT_CONTENT_NEGOTIATION_CLASS': 'rest_framework.negotiation.DefaultContentNegotiation',
    'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata',
    'DEFAULT_VERSIONING_CLASS': None,


## ... source file abbreviated to get to import_string examples ...


    'TEST_REQUEST_RENDERER_CLASSES',
    'UNAUTHENTICATED_USER',
    'UNAUTHENTICATED_TOKEN',
    'VIEW_NAME_FUNCTION',
    'VIEW_DESCRIPTION_FUNCTION'
]


REMOVED_SETTINGS = [
    'PAGINATE_BY', 'PAGINATE_BY_PARAM', 'MAX_PAGINATE_BY',
]


def perform_import(val, setting_name):
    if val is None:
        return None
    elif isinstance(val, str):
        return import_from_string(val, setting_name)
    elif isinstance(val, (list, tuple)):
        return [import_from_string(item, setting_name) for item in val]
    return val


def import_from_string(val, setting_name):
    try:
~~        return import_string(val)
    except ImportError as e:
        msg = "Could not import '%s' for API setting '%s'. %s: %s." % (val, setting_name, e.__class__.__name__, e)
        raise ImportError(msg)


class APISettings:
    def __init__(self, user_settings=None, defaults=None, import_strings=None):
        if user_settings:
            self._user_settings = self.__check_user_settings(user_settings)
        self.defaults = defaults or DEFAULTS
        self.import_strings = import_strings or IMPORT_STRINGS
        self._cached_attrs = set()

    @property
    def user_settings(self):
        if not hasattr(self, '_user_settings'):
            self._user_settings = getattr(settings, 'REST_FRAMEWORK', {})
        return self._user_settings

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError("Invalid API setting: '%s'" % attr)

        try:


## ... source file continues with no further import_string examples...

```


## Example 10 from django-sql-explorer
[django-sql-explorer](https://github.com/groveco/django-sql-explorer)
([PyPI page](https://pypi.org/project/django-sql-explorer/0.2/)),
also referred to as "SQL Explorer",
is a code library for the [Django](/django.html) Admin that allows
approved, authenticated users to view and execute direct database SQL
queries. The tool keeps track of executed queries so users can share them
with each other, as well as export results to downloadable formats.
django-sql-explorer is provided as open source under the
[MIT license](https://github.com/groveco/django-sql-explorer/blob/master/LICENSE).

[**django-sql-explorer / explorer / exporters.py**](https://github.com/groveco/django-sql-explorer/blob/master/explorer/./exporters.py)

```python
# exporters.py
from django.db import DatabaseError
from django.core.serializers.json import DjangoJSONEncoder
import json
import uuid
import string
import sys
from datetime import datetime
PY3 = sys.version_info[0] == 3
if PY3:
    import csv
else:
    import unicodecsv as csv

~~from django.utils.module_loading import import_string
from django.utils.text import slugify
from explorer import app_settings
from six import StringIO, BytesIO


def get_exporter_class(format):
    class_str = dict(getattr(app_settings, 'EXPLORER_DATA_EXPORTERS'))[format]
~~    return import_string(class_str)


class BaseExporter(object):

    name = ''
    content_type = ''
    file_extension = ''

    def __init__(self, query):
        self.query = query

    def get_output(self, **kwargs):
        value = self.get_file_output(**kwargs).getvalue()
        if PY3:
            return value
        else:
            return str(value)

    def get_file_output(self, **kwargs):
        res = self.query.execute_query_only()
        return self._get_output(res, **kwargs)

    def _get_output(self, res, **kwargs):
        raise NotImplementedError


## ... source file continues with no further import_string examples...

```


## Example 11 from django-taggit
[django-taggit](https://github.com/jazzband/django-taggit/)
([PyPI page](https://pypi.org/project/django-taggit/)) provides a way
to create, store, manage and use tags in a [Django](/django.html) project.
The code for django-taggit is
[open source](https://github.com/jazzband/django-taggit/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-taggit / taggit / utils.py**](https://github.com/jazzband/django-taggit/blob/master/taggit/./utils.py)

```python
# utils.py
from django.conf import settings
from django.utils.functional import wraps
~~from django.utils.module_loading import import_string


def _parse_tags(tagstring):
    if not tagstring:
        return []

    if "," not in tagstring and '"' not in tagstring:
        words = list(set(split_strip(tagstring, " ")))
        words.sort()
        return words

    words = []
    buffer = []
    to_be_split = []
    saw_loose_comma = False
    open_quote = False
    i = iter(tagstring)
    try:
        while True:
            c = next(i)
            if c == '"':
                if buffer:
                    to_be_split.append("".join(buffer))
                    buffer = []


## ... source file abbreviated to get to import_string examples ...




def _edit_string_for_tags(tags):
    names = []
    for tag in tags:
        name = tag.name
        if "," in name or " " in name:
            names.append('"%s"' % name)
        else:
            names.append(name)
    return ", ".join(sorted(names))


def require_instance_manager(func):
    @wraps(func)
    def inner(self, *args, **kwargs):
        if self.instance is None:
            raise TypeError("Can't call %s with a non-instance manager" % func.__name__)
        return func(self, *args, **kwargs)

    return inner


def get_func(key, default):
    func_path = getattr(settings, key, None)
~~    return default if func_path is None else import_string(func_path)


def parse_tags(tagstring):
    func = get_func("TAGGIT_TAGS_FROM_STRING", _parse_tags)
    return func(tagstring)


def edit_string_for_tags(tags):
    func = get_func("TAGGIT_STRING_FROM_TAGS", _edit_string_for_tags)
    return func(tags)



## ... source file continues with no further import_string examples...

```


## Example 12 from django-wiki
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

[**django-wiki / src/wiki / sites.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/./sites.py)

```python
# sites.py
from django.apps import apps
from django.urls import include
from django.urls import re_path
from django.utils.functional import LazyObject
~~from django.utils.module_loading import import_string
from wiki.conf import settings
from wiki.core.plugins import registry


class WikiSite:

    def __init__(self, name="wiki"):
        from wiki.views import accounts, article, deleted_list

        self.name = name

        self.root_view = getattr(self, "root_view", article.CreateRootView.as_view())
        self.root_missing_view = getattr(
            self, "root_missing_view", article.MissingRootView.as_view()
        )

        self.article_view = getattr(self, "article_view", article.ArticleView.as_view())
        self.article_create_view = getattr(
            self, "article_create_view", article.Create.as_view()
        )
        self.article_delete_view = getattr(
            self, "article_delete_view", article.Delete.as_view()
        )
        self.article_deleted_view = getattr(


## ... source file abbreviated to get to import_string examples ...


    def get_plugin_urls(self):
        urlpatterns = []
        for plugin in registry.get_plugins().values():
            slug = getattr(plugin, "slug", None)
            if slug:
                article_urlpatterns = plugin.urlpatterns.get("article", [])
                urlpatterns += [
                    re_path(
                        r"^(?P<article_id>[0-9]+)/plugin/" + slug + "/",
                        include(article_urlpatterns),
                    ),
                    re_path(
                        r"^(?P<path>.+/|)_plugin/" + slug + "/",
                        include(article_urlpatterns),
                    ),
                ]
                root_urlpatterns = plugin.urlpatterns.get("root", [])
                urlpatterns += [
                    re_path(r"^_plugin/" + slug + "/", include(root_urlpatterns)),
                ]
        return urlpatterns


class DefaultWikiSite(LazyObject):
    def _setup(self):
~~        WikiSiteClass = import_string(apps.get_app_config("wiki").default_site)
        self._wrapped = WikiSiteClass()


site = DefaultWikiSite()



## ... source file continues with no further import_string examples...

```


## Example 13 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / utils / loading.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/utils/loading.py)

```python
# loading.py
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
~~from django.utils.module_loading import import_string


def get_custom_form(form_setting):
    try:
~~        return import_string(getattr(settings, form_setting))
    except ImportError:
        raise ImproperlyConfigured(
            "%s refers to a form '%s' that is not available" %
            (form_setting, getattr(settings, form_setting))
        )



## ... source file continues with no further import_string examples...

```

