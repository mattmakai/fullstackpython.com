title: django.forms IntegerField Python Code Examples
category: page
slug: django-forms-integerfield-examples
sortorder: 500013125
toc: False
sidebartitle: django.forms IntegerField
meta: View Python code examples that show how to use the IntegerField class within the forms module of the Django open source project. 


[IntegerField](https://github.com/django/django/blob/master/django/forms/fields.py)
([documentation](https://docs.djangoproject.com/en/stable/ref/forms/fields/#integerfield)),
from the [Django](/django.html) `forms` module, enables safe handling of 
integer numbers data collected via an HTTP POST request from an
[HTML](/hypertext-markup-language-html.html) form submission.

Note that IntegerField can either be imported from `django.forms` or 
`django.forms.fields`. `django.forms` is more commonly used because it
is less characters to type for the equivalent effect.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / admin / forms.py**](https://github.com/divio/django-cms/blob/develop/cms/admin/forms.py)

```python
# -*- coding: utf-8 -*-
~~from django import forms
from django.apps import apps
from django.contrib.auth import get_user_model, get_permission_codename
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.forms.utils import ErrorList
from django.forms.widgets import HiddenInput
from django.template.defaultfilters import slugify
from django.utils.encoding import force_text
from django.utils.translation import ugettext, ugettext_lazy as _

from cms import api
from cms.apphook_pool import apphook_pool
from cms.cache.permissions import clear_permission_cache
from cms.exceptions import PluginLimitReached
from cms.extensions import extension_pool
from cms.constants import PAGE_TYPES_ID, PUBLISHER_STATE_DIRTY, ROOT_USER_LEVEL
from cms.forms.validators import validate_relative_url, validate_url_uniqueness
from cms.forms.widgets import UserSelectAdminWidget, AppHookSelect, ApplicationConfigSelect
from cms.models import (CMSPlugin, Page, PageType, PagePermission, PageUser, PageUserGroup, Title,
                        Placeholder, GlobalPagePermission, TreeNode)
from cms.models.permissionmodels import User
from cms.plugin_pool import plugin_pool
from cms.signals.apphook import set_restart_trigger
from cms.utils.conf import get_cms_setting
from cms.utils.compat.forms import UserChangeForm
from cms.utils.i18n import get_language_list, get_language_object
from cms.utils.permissions import (
    get_current_user,
    get_subordinate_users,
    get_subordinate_groups,
    get_user_permission_level,
)
from menus.menu_pool import menu_pool


## ... source file abbreviated to get to IntegerField examples ...


~~class AdvancedSettingsForm(forms.ModelForm):
    from cms.forms.fields import PageSmartLinkField

    _user = None
    _site = None
    _language = None

    application_urls = forms.ChoiceField(label=_('Application'),
                                         choices=(), required=False,
                                         help_text=_('Hook application to this page.'))
    overwrite_url = forms.CharField(label=_('Overwrite URL'), max_length=255, required=False,
                                    help_text=_('Keep this field empty if standard path should be used.'))

    xframe_options = forms.ChoiceField(
        choices=Page._meta.get_field('xframe_options').choices,
        label=_('X Frame Options'),
        help_text=_('Whether this page can be embedded in other pages or websites'),
        initial=Page._meta.get_field('xframe_options').default,
        required=False
    )

    redirect = PageSmartLinkField(label=_('Redirect'), required=False,
                                  help_text=_('Redirects to this URL.'),
                                  placeholder_text=_('Start typing...'),
                                  ajax_view='admin:cms_page_get_published_pagelist',
    )

    # This is really a 'fake' field which does not correspond to any Page attribute
    # But creates a stub field to be populate by js
    application_configs = forms.CharField(
        label=_('Application configurations'),
        required=False,
        widget=ApplicationConfigSelect,
    )
    fieldsets = (
        (None, {
            'fields': ('overwrite_url', 'redirect'),
        }),
        (_('Language independent options'), {
            'fields': ('template', 'reverse_id', 'soft_root', 'navigation_extenders',
                       'application_urls', 'application_namespace', 'application_configs',
                       'xframe_options',)
        })
    )

    class Meta:
        model = Page
        fields = [
            'template', 'reverse_id', 'overwrite_url', 'redirect', 'soft_root', 'navigation_extenders',
            'application_urls', 'application_namespace', "xframe_options",
        ]

    def __init__(self, *args, **kwargs):
        super(AdvancedSettingsForm, self).__init__(*args, **kwargs)
        self.title_obj = self.instance.get_title_obj(
            language=self._language,
            fallback=False,
            force_reload=True,
        )

        if 'navigation_extenders' in self.fields:
            navigation_extenders = self.get_navigation_extenders()
            self.fields['navigation_extenders'].widget = forms.Select(
                {}, [('', "---------")] + navigation_extenders)
        if 'application_urls' in self.fields:
            # Prepare a dict mapping the apps by class name ('PollApp') to
            # their app_name attribute ('polls'), if any.
            app_namespaces = {}
            app_configs = {}
            for hook in apphook_pool.get_apphooks():
                app = apphook_pool.get_apphook(hook[0])
                if app.app_name:
                    app_namespaces[hook[0]] = app.app_name
                if app.app_config:
                    app_configs[hook[0]] = app

            self.fields['application_urls'].widget = AppHookSelect(
                attrs={'id': 'application_urls'},
                app_namespaces=app_namespaces
            )
            self.fields['application_urls'].choices = [('', "---------")] + apphook_pool.get_apphooks()

            page_data = self.data if self.data else self.initial
            if app_configs:
                self.fields['application_configs'].widget = ApplicationConfigSelect(
                    attrs={'id': 'application_configs'},
                    app_configs=app_configs,
                )

                if page_data.get('application_urls', False) and page_data['application_urls'] in app_configs:
                    configs = app_configs[page_data['application_urls']].get_configs()
                    self.fields['application_configs'].widget.choices = [(config.pk, force_text(config)) for config in configs]

                    try:
                        config = configs.get(namespace=self.initial['application_namespace'])
                        self.fields['application_configs'].initial = config.pk
                    except ObjectDoesNotExist:
                        # Provided apphook configuration doesn't exist (anymore),
                        # just skip it
                        # The user will choose another value anyway
                        pass

        if 'redirect' in self.fields:
            self.fields['redirect'].widget.language = self._language
            self.fields['redirect'].initial = self.title_obj.redirect

        if 'overwrite_url' in self.fields and self.title_obj.has_url_overwrite:
            self.fields['overwrite_url'].initial = self.title_obj.path

    def get_apphooks(self):
        for hook in apphook_pool.get_apphooks():
            yield (hook[0], apphook_pool.get_apphook(hook[0]))

    def get_apphooks_with_config(self):
        return {key: app for key, app in self.get_apphooks() if app.app_config}

    def get_navigation_extenders(self):
        return menu_pool.get_menus_by_attribute("cms_enabled", True)

    def _check_unique_namespace_instance(self, namespace):
        return Page.objects.drafts().on_site(self._site).filter(
            application_namespace=namespace
        ).exclude(pk=self.instance.pk).exists()

    def clean(self):
        cleaned_data = super(AdvancedSettingsForm, self).clean()

        if self._errors:
            # Fail fast if there's errors in the form
            return cleaned_data

        # Language has been validated already
        # so we know it exists.
        language_name = get_language_object(
            self._language,
            site_id=self._site.pk,
        )['name']

        if not self.title_obj.slug:
            # This covers all cases where users try to edit
            # page advanced settings without setting a title slug
            # for page titles that already exist.
            message = _("Please set the %(language)s slug "
                        "before editing its advanced settings.")
            raise ValidationError(message % {'language': language_name})

        if 'reverse_id' in self.fields:
            reverse_id = cleaned_data['reverse_id']
            if reverse_id:
                lookup = Page.objects.drafts().on_site(self._site).filter(reverse_id=reverse_id)
                if lookup.exclude(pk=self.instance.pk).exists():
                    self._errors['reverse_id'] = self.error_class(
                        [_('A page with this reverse URL id exists already.')])
~~        apphook = cleaned_data.get('application_urls', None)
~~        # The field 'application_namespace' is a misnomer. It should be
~~        # 'instance_namespace'.
~~        instance_namespace = cleaned_data.get('application_namespace', None)
~~        application_config = cleaned_data.get('application_configs', None)
~~        if apphook:
~~            apphooks_with_config = self.get_apphooks_with_config()

~~            # application_config wins over application_namespace
~~            if apphook in apphooks_with_config and application_config:
~~                # the value of the application config namespace is saved in
~~                # the 'usual' namespace field to be backward compatible
~~                # with existing apphooks
~~                try:
~~                    appconfig_pk = forms.IntegerField(required=True).to_python(application_config)
~~                except ValidationError:
~~                    self._errors['application_configs'] = ErrorList([
~~                        _('Invalid application config value')
~~                    ])
~~                    return self.cleaned_data

~~                try:
~~                    config = apphooks_with_config[apphook].get_configs().get(pk=appconfig_pk)
~~                except ObjectDoesNotExist:
~~                    self._errors['application_configs'] = ErrorList([
~~                        _('Invalid application config value')
~~                    ])
~~                    return self.cleaned_data

~~                if self._check_unique_namespace_instance(config.namespace):
~~                    # Looks like there's already one with the default instance
~~                    # namespace defined.
~~                    self._errors['application_configs'] = ErrorList([
~~                        _('An application instance using this configuration already exists.')
~~                    ])
~~                else:
~~                    self.cleaned_data['application_namespace'] = config.namespace
~~            else:
~~                if instance_namespace:
~~                    if self._check_unique_namespace_instance(instance_namespace):
~~                        self._errors['application_namespace'] = ErrorList([
~~                            _('An application instance with this name already exists.')
~~                        ])
~~                else:
~~                    # The attribute on the apps 'app_name' is a misnomer, it should be
~~                    # 'application_namespace'.
~~                    application_namespace = apphook_pool.get_apphook(apphook).app_name
~~                    if application_namespace and not instance_namespace:
~~                        if self._check_unique_namespace_instance(application_namespace):
~~                            # Looks like there's already one with the default instance
~~                            # namespace defined.
~~                            self._errors['application_namespace'] = ErrorList([
~~                                _('An application instance with this name already exists.')
~~                            ])
~~                        else:
~~                            # OK, there are zero instances of THIS app that use the
~~                            # default instance namespace, so, since the user didn't
~~                            # provide one, we'll use the default. NOTE: The following
~~                            # line is really setting the "instance namespace" of the
~~                            # new app to the app’s "application namespace", which is
~~                            # the default instance namespace.
~~                            self.cleaned_data['application_namespace'] = application_namespace

~~        if instance_namespace and not apphook:
~~            self.cleaned_data['application_namespace'] = None

~~        if application_config and not apphook:
~~            self.cleaned_data['application_configs'] = None
~~        return self.cleaned_data


## ... source file abbreviated to get to IntegerField examples ...


class PageTreeForm(forms.Form):

~~    position = forms.IntegerField(initial=0, required=True)
    target = forms.ModelChoiceField(queryset=Page.objects.none(), required=False)

    def __init__(self, *args, **kwargs):
        self.page = kwargs.pop('page')
        self._site = kwargs.pop('site', Site.objects.get_current())
        super(PageTreeForm, self).__init__(*args, **kwargs)
        self.fields['target'].queryset = Page.objects.drafts().filter(
            node__site=self._site,
            is_page_type=self.page.is_page_type,
        )

    def get_root_nodes(self):
        # TODO: this needs to avoid using the pages accessor directly
        nodes = TreeNode.get_root_nodes()
        return nodes.exclude(cms_pages__is_page_type=not(self.page.is_page_type))

~~    def get_tree_options(self):
~~        position = self.cleaned_data['position']
~~        target_page = self.cleaned_data.get('target')
~~        parent_node = target_page.node if target_page else None

~~        if parent_node:
~~            return self._get_tree_options_for_parent(parent_node, position)
~~        return self._get_tree_options_for_root(position)

    def _get_tree_options_for_root(self, position):
        siblings = self.get_root_nodes().filter(site=self._site)

        try:
            target_node = siblings[position]
        except IndexError:
            # The position requested is not occupied.
            # Add the node as the last root node,
            # relative to the current site.
            return (siblings.reverse()[0], 'right')
        return (target_node, 'left')

    def _get_tree_options_for_parent(self, parent_node, position):
        if position == 0:
            return (parent_node, 'first-child')

        siblings = parent_node.get_children().filter(site=self._site)

        try:
            target_node = siblings[position]
        except IndexError:
            # The position requested is not occupied.
            # Add the node to be the parent's first child
            return (parent_node, 'last-child')
        return (target_node, 'left')


## ... source file continues with no further IntegerField examples ...

```


## Example 2 from django-jet
[django-jet](https://github.com/geex-arts/django-jet)
([project documentation](https://jet.readthedocs.io/en/latest/),
[PyPI project page](https://pypi.org/project/django-jet/) and
[more information](http://jet.geex-arts.com/))
is a fancy [Django](/django.html) Admin panel replacement.

The django-jet project is open source under the
[GNU Affero General Public License v3.0](https://github.com/geex-arts/django-jet/blob/dev/LICENSE).

[**django-jet / jet / dashboard / forms.py**](https://github.com/geex-arts/django-jet/blob/dev/jet/dashboard/forms.py)

```python
import json
~~from django import forms
from django.core.exceptions import ValidationError
from jet.dashboard.models import UserDashboardModule
from jet.dashboard.utils import get_current_dashboard
from jet.utils import user_is_authenticated


class UpdateDashboardModulesForm(forms.Form):
    app_label = forms.CharField(required=False)
    modules = forms.CharField()
    modules_objects = []

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(UpdateDashboardModulesForm, self).__init__(*args, **kwargs)

    def clean(self):
        data = super(UpdateDashboardModulesForm, self).clean()

        if not user_is_authenticated(self.request.user) or not self.request.user.is_staff:
            raise ValidationError('error')

        try:
            modules = json.loads(data['modules'])

            for module in modules:
                db_module = UserDashboardModule.objects.get(
                    user=self.request.user.pk,
                    app_label=data['app_label'] if data['app_label'] else None,
                    pk=module['id']
                )

                column = module['column']
                order = module['order']

                if db_module.column != column or db_module.order != order:
                    db_module.column = column
                    db_module.order = order

                    self.modules_objects.append(db_module)
        except Exception:
            raise ValidationError('error')

        return data

    def save(self):
        for module in self.modules_objects:
            module.save()


class AddUserDashboardModuleForm(forms.ModelForm):
    type = forms.CharField()
~~    module = forms.IntegerField()
    module_cls = None

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(AddUserDashboardModuleForm, self).__init__(*args, **kwargs)

    class Meta:
        model = UserDashboardModule
        fields = ['app_label']

    def clean_app_label(self):
        data = self.cleaned_data['app_label']
        return data if data != '' else None

    def clean(self):
        data = super(AddUserDashboardModuleForm, self).clean()

        if not user_is_authenticated(self.request.user) or not self.request.user.is_staff:
            raise ValidationError('error')

        if 'app_label' in data:
            index_dashboard_cls = get_current_dashboard('app_index' if data['app_label'] else 'index')
            index_dashboard = index_dashboard_cls({'request': self.request}, app_label=data['app_label'])

~~            if 'type' in data:
~~                if data['type'] == 'children':
~~                    module = index_dashboard.children[data['module']]
~~                elif data['type'] == 'available_children':
~~                    module = index_dashboard.available_children[data['module']]()
~~                else:
~~                    raise ValidationError('error')

~~                self.module_cls = module
        return data

    def save(self, commit=True):
        self.instance.title = self.module_cls.title
        self.instance.module = self.module_cls.fullname()
        self.instance.user = self.request.user.pk
        self.instance.column = 0
        self.instance.order = -1
        self.instance.settings = self.module_cls.dump_settings()
        self.instance.children = self.module_cls.dump_children()

        return super(AddUserDashboardModuleForm, self).save(commit)

## ... source file continues with no further IntegerField examples ...

```


## Example 3 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / submissions / forms.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/submissions/forms.py)

```python
# forms.py
~~from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models import Max
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

from gears.widgets import CustomFileInput
from .models import Submission, Author

User = get_user_model()


MIN_TOPICS_REQUIRED = 1
MAX_TOPICS_REQUIRED = 3


## ... source file abbreviated to get to IntegerField examples ...


class AuthorCreateForm(forms.Form):
~~    user_pk = forms.IntegerField()

    def __init__(self, submission, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.submission = submission
        self.user = None

~~    def clean_user_pk(self):
~~        user_pk = self.cleaned_data['user_pk']
~~        self.user = User.objects.get(pk=user_pk)
~~        for author in self.submission.authors.all():
~~            if author.user.pk == self.user.pk:
~~                raise ValidationError(f'Author already added')
~~        return self.cleaned_data['user_pk']

    def save(self, commit=True):
        authors = self.submission.authors
        max_order = authors.aggregate(Max('order'))['order__max']
        author = Author.objects.create(
            user=self.user,
            submission=self.submission,
            order=1 if max_order is None else max_order + 1
        )
        if commit:
            author.save()
        return author


class AuthorDeleteForm(forms.Form):
~~    author_pk = forms.IntegerField()

    def __init__(self, submission, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.submission = submission
        self.author = None

~~    def clean_author_pk(self):
~~        # Check that we are not deleting the creator
~~        author_pk = self.cleaned_data['author_pk']
~~        self.author = Author.objects.get(pk=author_pk)
~~        creator = self.submission.created_by
~~        if self.author.user.pk == creator.pk:
~~            raise ValidationError(_('Can not delete submission creator'))
~~        if self.author.submission.pk != self.submission.pk:
~~            raise ValidationError(_('Can not delete alien author'))
~~        return self.cleaned_data['author_pk']

    def save(self, commit=True):
        if commit:
            self.author.delete()

## ... source file continues with no further IntegerField examples ...
```



## Example 4 from django-mongonaut
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

[**django-mongonaut / mongonaut / forms / widgets.py**](https://github.com/jazzband/django-mongonaut/blob/master/mongonaut/forms/widgets.py)

```python
# -*- coding: utf-8 -*-

""" Widgets for mongonaut forms"""

~~from django import forms

from mongoengine.base import ObjectIdField
from mongoengine.fields import BooleanField
from mongoengine.fields import DateTimeField
from mongoengine.fields import EmbeddedDocumentField
from mongoengine.fields import ListField
from mongoengine.fields import ReferenceField
from mongoengine.fields import FloatField
from mongoengine.fields import EmailField
from mongoengine.fields import DecimalField
from mongoengine.fields import URLField
from mongoengine.fields import IntField
from mongoengine.fields import StringField
from mongoengine.fields import GeoPointField


def get_widget(model_field, disabled=False):
    """Choose which widget to display for a field."""

    attrs = get_attrs(model_field, disabled)

    if hasattr(model_field, "max_length") and not model_field.max_length:
        return forms.Textarea(attrs=attrs)

    elif isinstance(model_field, DateTimeField):
        return forms.DateTimeInput(attrs=attrs)

    elif isinstance(model_field, BooleanField):
        return forms.CheckboxInput(attrs=attrs)

    elif isinstance(model_field, ReferenceField) or model_field.choices:
        return forms.Select(attrs=attrs)

    elif (isinstance(model_field, ListField) or
          isinstance(model_field, EmbeddedDocumentField) or
          isinstance(model_field, GeoPointField)):
        return None

    else:
        return forms.TextInput(attrs=attrs)


def get_attrs(model_field, disabled=False):
    """Set attributes on the display widget."""
    attrs = {}
    attrs['class'] = 'span6 xlarge'
    if disabled or isinstance(model_field, ObjectIdField):
        attrs['class'] += ' disabled'
        attrs['readonly'] = 'readonly'
    return attrs


def get_form_field_class(model_field):
    """Gets the default form field  for a mongoenigne field."""

    FIELD_MAPPING = {
~~        IntField: forms.IntegerField,
        StringField: forms.CharField,
        FloatField: forms.FloatField,
        BooleanField: forms.BooleanField,
        DateTimeField: forms.DateTimeField,
        DecimalField: forms.DecimalField,
        URLField: forms.URLField,
        EmailField: forms.EmailField
    }

    return FIELD_MAPPING.get(model_field.__class__, forms.CharField)

```


## Example 5 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / images / forms.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/images/forms.py)

```python
# forms.py
~~from django import forms
from django.forms.models import modelform_factory
from django.utils.text import capfirst
from django.utils.translation import ugettext as _

from wagtail.admin import widgets
from wagtail.admin.forms.collections import (
    BaseCollectionMemberForm, collection_member_permission_formset_factory)
from wagtail.images.fields import WagtailImageField
from wagtail.images.formats import get_image_formats
from wagtail.images.models import Image
from wagtail.images.permissions import permission_policy as images_permission_policy


# Callback to allow us to override the default form field for the image file field
def formfield_for_dbfield(db_field, **kwargs):
    # Check if this is the file field
    if db_field.name == 'file':
        return WagtailImageField(label=capfirst(db_field.verbose_name), **kwargs)

    # For all other fields, just call its formfield() method.
    return db_field.formfield(**kwargs)


class BaseImageForm(BaseCollectionMemberForm):
    permission_policy = images_permission_policy


def get_image_form(model):
    fields = model.admin_form_fields
    if 'collection' not in fields:
        # force addition of the 'collection' field, because leaving it out can
        # cause dubious results when multiple collections exist (e.g adding the
        # document to the root collection where the user may not have permission) -
        # and when only one collection exists, it will get hidden anyway.
        fields = list(fields) + ['collection']

    return modelform_factory(
        model,
        form=BaseImageForm,
        fields=fields,
        formfield_callback=formfield_for_dbfield,
        # set the 'file' widget to a FileInput rather than the default ClearableFileInput
        # so that when editing, we don't get the 'currently: ...' banner which is
        # a bit pointless here
        widgets={
            'tags': widgets.AdminTagWidget,
            'file': forms.FileInput(),
            'focal_point_x': forms.HiddenInput(attrs={'class': 'focal_point_x'}),
            'focal_point_y': forms.HiddenInput(attrs={'class': 'focal_point_y'}),
            'focal_point_width': forms.HiddenInput(attrs={'class': 'focal_point_width'}),
            'focal_point_height': forms.HiddenInput(attrs={'class': 'focal_point_height'}),
        })


class ImageInsertionForm(forms.Form):
    """
    Form for selecting parameters of the image (e.g. format) prior to insertion
    into a rich text area
    """
    format = forms.ChoiceField(
        choices=[(format.name, format.label) for format in get_image_formats()],
        widget=forms.RadioSelect
    )
    alt_text = forms.CharField()


class URLGeneratorForm(forms.Form):
    filter_method = forms.ChoiceField(
        label=_("Filter"),
        choices=(
            ('original', _("Original size")),
            ('width', _("Resize to width")),
            ('height', _("Resize to height")),
            ('min', _("Resize to min")),
            ('max', _("Resize to max")),
            ('fill', _("Resize to fill")),
        ),
    )
~~    width = forms.IntegerField(label=_("Width"), min_value=0)
~~    height = forms.IntegerField(label=_("Height"), min_value=0)
~~    closeness = forms.IntegerField(label=_("Closeness"), min_value=0, initial=0)


GroupImagePermissionFormSet = collection_member_permission_formset_factory(
    Image,
    [
        ('add_image', _("Add"), _("Add/edit images you own")),
        ('change_image', _("Edit"), _("Edit any image")),
    ],
    'wagtailimages/permissions/includes/image_permissions_formset.html'
)

```


