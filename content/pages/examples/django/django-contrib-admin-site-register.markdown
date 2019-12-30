title: django.contrib.admin.sites register Example Code
category: page
slug: django-contrib-admin-sites-register-examples
sortorder: 500010190
toc: False
sidebartitle: django.contrib.admin.sites register
meta: Python code examples for the admin module within django.contrib of the Django project. 


The [Django admin](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)
is an automatically-generated user interface for 
[Django models](/django-orm.html).  The 
[register function](https://github.com/django/django/blob/master/django/contrib/admin/sites.py)
is used to add models to the Django admin so that data for those models
can be created, deleted, updated and queried through the user interface.


## Example 1 from AuditLog
[Auditlog](https://github.com/jjkester/django-auditlog)
([project documentation](https://django-auditlog.readthedocs.io/en/latest/))
is a [Django](/django.html) app that logs changes to Python objects,
similar to the Django admin's logs but with more details and
output formats. Auditlog's source code is provided as open source under the
[MIT license](https://github.com/jjkester/django-auditlog/blob/master/LICENSE).

[**AuditLog / src / auditlog / admin.py**](https://github.com/jjkester/django-auditlog/blob/master/src/auditlog/admin.py)

```python
~~from django.contrib import admin
from .models import LogEntry
from .mixins import LogEntryAdminMixin
from .filters import ResourceTypeFilter


class LogEntryAdmin(admin.ModelAdmin, LogEntryAdminMixin):
    list_display = ['created', 'resource_url', 'action', 
                    'msg_short', 'user_url']
    search_fields = ['timestamp', 'object_repr', 'changes', 
                     'actor__first_name', 'actor__last_name']
    list_filter = ['action', ResourceTypeFilter]
    readonly_fields = ['created', 'resource_url', 'action', 
                       'user_url', 'msg']
    fieldsets = [
        (None, {'fields': ['created', 'user_url', 
                           'resource_url']}),
        ('Changes', {'fields': ['action', 'msg']}),
    ]


~~admin.site.register(LogEntry, LogEntryAdmin)
```


## Example 2 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / socialaccount / admin.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/socialaccount/admin.py)

```python
from django import forms
~~from django.contrib import admin

from allauth.account.adapter import get_adapter

from .models import SocialAccount, SocialApp, SocialToken


class SocialAppForm(forms.ModelForm):
    class Meta:
        model = SocialApp
        exclude = []
        widgets = {
            'client_id': forms.TextInput(attrs={'size': '100'}),
            'key': forms.TextInput(attrs={'size': '100'}),
            'secret': forms.TextInput(attrs={'size': '100'})
        }


class SocialAppAdmin(admin.ModelAdmin):
    form = SocialAppForm
    list_display = ('name', 'provider',)
    filter_horizontal = ('sites',)


class SocialAccountAdmin(admin.ModelAdmin):
    search_fields = []
    raw_id_fields = ('user',)
    list_display = ('user', 'uid', 'provider')
    list_filter = ('provider',)

    def get_search_fields(self, request):
        base_fields = get_adapter().get_user_search_fields()
        return list(map(lambda a: 'user__' + a, base_fields))


class SocialTokenAdmin(admin.ModelAdmin):
    raw_id_fields = ('app', 'account',)
    list_display = ('app', 'account', 'truncated_token', 
                    'expires_at')
    list_filter = ('app', 'app__provider', 'expires_at')

    def truncated_token(self, token):
        max_chars = 40
        ret = token.token
        if len(ret) > max_chars:
            ret = ret[0:max_chars] + '...(truncated)'
        return ret
    truncated_token.short_description = 'Token'


~~admin.site.register(SocialApp, SocialAppAdmin)
~~admin.site.register(SocialToken, SocialTokenAdmin)
~~admin.site.register(SocialAccount, SocialAccountAdmin)
```


## Example 3 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / admin / useradmin.py**](https://github.com/divio/django-cms/blob/develop/cms/admin/useradmin.py)

```python
# -*- coding: utf-8 -*-
from copy import deepcopy

from django.contrib import admin
`~from django.contrib.admin import site
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.utils.translation import ugettext

from cms.admin.forms import PageUserChangeForm, PageUserGroupForm
from cms.exceptions import NoPermissionsException
from cms.models import Page, PagePermission, PageUser, PageUserGroup
from cms.utils.compat.forms import UserAdmin
from cms.utils.conf import get_cms_setting
from cms.utils.permissions import (
    get_model_permission_codename,
    get_subordinate_groups,
    get_subordinate_users,
    get_user_permission_level,
)


user_model = get_user_model()
admin_class = UserAdmin
for model, admin_instance in site._registry.items():
    if model == user_model:
        admin_class = admin_instance.__class__


class GenericCmsPermissionAdmin(object):

    def get_subordinates(self, user, site):
        raise NotImplementedError

    def _has_change_permissions_permission(self, request):
        """
        User is able to add/change objects only if he haves 
        can change permission on some page.
        """
        site = Site.objects.get_current(request)

        try:
            get_user_permission_level(request.user, site)
        except NoPermissionsException:
            return False
        return True

    def get_form(self, request, obj=None, **kwargs):
        form_class = super(GenericCmsPermissionAdmin, 
                           self).get_form(request, obj, **kwargs)
        form_class._current_user = request.user
        return form_class

    def get_queryset(self, request):
        queryset = super(GenericCmsPermissionAdmin, self).\
                   get_queryset(request)
        site = Site.objects.get_current(request)
        user_ids = self.get_subordinates(request.user, site).\
                                         values_list('pk', flat=True)
        return queryset.filter(pk__in=user_ids)

    def has_add_permission(self, request):
        has_model_perm = super(GenericCmsPermissionAdmin, 
                               self).has_add_permission(request)

        if not has_model_perm:
            return False
        return self._has_change_permissions_permission(request)

    def has_change_permission(self, request, obj=None):
        has_model_perm = super(GenericCmsPermissionAdmin, 
                               self).has_change_permission(request, 
                                                           obj)

        if not has_model_perm:
            return False
        return self._has_change_permissions_permission(request)

    def has_delete_permission(self, request, obj=None):
        has_model_perm = super(GenericCmsPermissionAdmin, 
                               self).has_delete_permission(request, 
                                                           obj)

        if not has_model_perm:
            return False
        return self._has_change_permissions_permission(request)

    def has_view_permission(self, request, obj=None):
        # For django 2.1
        # Default is to return True if user got `change` perm, but 
        # we have to get in consideration also cms permission system
        return self.has_change_permission(request, obj)


class PageUserAdmin(GenericCmsPermissionAdmin, admin_class):
    form = PageUserChangeForm
    model = PageUser

    def get_subordinates(self, user, site):
        return get_subordinate_users(user, site).\
               values_list('pk', flat=True)

    def get_readonly_fields(self, request, obj=None):
        fields = super(PageUserAdmin, 
                       self).get_readonly_fields(request, obj)

        if not request.user.is_superuser:
            # Non superusers can't set superuser status on
            # their subordinates.
            fields = list(fields) + ['is_superuser']
        return fields

    def save_model(self, request, obj, form, change):
        if not change:
            # By default set the staff flag to True
            # when a PageUser is first created
            obj.is_staff = True
            # Set the created_by field to the current user
            obj.created_by = request.user
        super(PageUserAdmin, self).save_model(request, obj, 
                                              form, change)


class PageUserGroupAdmin(GenericCmsPermissionAdmin, 
                         admin.ModelAdmin):
    form = PageUserGroupForm
    list_display = ('name', 'created_by')

    fieldsets = [
        (None, {'fields': ('name',)}),
    ]

    def get_fieldsets(self, request, obj=None):
        """
        Nobody can grant more than he haves, so check for 
        user permissions to Page and User model and render 
        fieldset depending on them.
        """
        fieldsets = deepcopy(self.fieldsets)
        perm_models = (
            (Page, ugettext('Page permissions')),
            (PageUser, ugettext('User & Group permissions')),
            (PagePermission, 
             ugettext('Page permissions management')),
        )
        for i, perm_model in enumerate(perm_models):
            fields = []
            model, title = perm_model
            name = model.__name__.lower()
            for key in ('add', 'change', 'delete'):
                perm_code = get_model_permission_codename(\
                            model, action=key)
                if request.user.has_perm(perm_code):
                    fields.append('can_%s_%s' % (key, name))
            if fields:
                fieldsets.insert(2 + i, (title, 
                                         {'fields': (fields,)}))
        return fieldsets

    def get_subordinates(self, user, site):
        return get_subordinate_groups(user, 
                                      site).values_list('pk', 
                                                        flat=True)


if get_cms_setting('PERMISSION'):
~~    admin.site.register(PageUser, PageUserAdmin)
~~    admin.site.register(PageUserGroup, PageUserGroupAdmin)
```


## Example 4 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / admin / __init__.py**](https://github.com/divio/django-filer/blob/develop/filer/admin/__init__.py)

```python
# -*- coding: utf-8 -*-
~~from django.contrib import admin

from ..models import (Clipboard, File, Folder, 
                      FolderPermission, ThumbnailOption)
from ..settings import FILER_IMAGE_MODEL
from ..utils.loader import load_model
from .clipboardadmin import ClipboardAdmin
from .fileadmin import FileAdmin
from .folderadmin import FolderAdmin
from .imageadmin import ImageAdmin
from .permissionadmin import PermissionAdmin
from .thumbnailoptionadmin import ThumbnailOptionAdmin


Image = load_model(FILER_IMAGE_MODEL)


~~admin.site.register(Folder, FolderAdmin)
~~admin.site.register(File, FileAdmin)
~~admin.site.register(Clipboard, ClipboardAdmin)
~~admin.site.register(Image, ImageAdmin)
~~admin.site.register(FolderPermission, PermissionAdmin)
~~admin.site.register(ThumbnailOption, ThumbnailOptionAdmin)
```
