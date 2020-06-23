title: django.contrib.admin.sites site code examples
category: page
slug: django-contrib-admin-sites-site-examples
sortorder: 500011027
toc: False
sidebartitle: django.contrib.admin.sites site
meta: Python example code for the site function from the django.contrib.admin.sites module of the Django project.


site is a function within the django.contrib.admin.sites module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / tests / test_admin.py**](https://github.com/divio/django-cms/blob/develop/cms/tests/test_admin.py)

```python
# test_admin.py
import json
import datetime

from djangocms_text_ckeditor.cms_plugins import TextPlugin
from djangocms_text_ckeditor.models import Text
from django.contrib import admin
from django.contrib.admin.models import LogEntry
~~from django.contrib.admin.sites import site
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.sites.models import Site
from django.urls import reverse
from django.http import (Http404, HttpResponseBadRequest,
                         HttpResponseNotFound)
from django.utils.encoding import force_text, smart_str
from django.utils import timezone

from cms import api
from cms.api import create_page, create_title, add_plugin, publish_page
from cms.admin.pageadmin import PageAdmin
from cms.constants import TEMPLATE_INHERITANCE_MAGIC
from cms.models import StaticPlaceholder
from cms.models.pagemodel import Page, PageType
from cms.models.permissionmodels import GlobalPagePermission, PagePermission
from cms.models.placeholdermodel import Placeholder
from cms.models.pluginmodel import CMSPlugin
from cms.models.titlemodels import Title
from cms.test_utils import testcases as base
from cms.test_utils.testcases import (
    CMSTestCase, URL_CMS_PAGE_DELETE, URL_CMS_PAGE,URL_CMS_TRANSLATION_DELETE,
    URL_CMS_PAGE_CHANGE_LANGUAGE, URL_CMS_PAGE_CHANGE,
    URL_CMS_PAGE_PUBLISHED,
)
from cms.utils.conf import get_cms_setting
from cms.utils.urlutils import admin_reverse


class AdminTestsBase(CMSTestCase):
    @property
    def admin_class(self):
~~        return site._registry[Page]

    def _get_guys(self, admin_only=False, use_global_permissions=True):
        admin_user = self.get_superuser()

        if admin_only:
            return admin_user
        staff_user = self._get_staff_user(use_global_permissions)
        return admin_user, staff_user

    def _get_staff_user(self, use_global_permissions=True):
        USERNAME = 'test'

        if get_user_model().USERNAME_FIELD == 'email':
            normal_guy = get_user_model().objects.create_user(USERNAME, 'test@test.com', 'test@test.com')
        else:
            normal_guy = get_user_model().objects.create_user(USERNAME, 'test@test.com', USERNAME)

        normal_guy.is_staff = True
        normal_guy.is_active = True
        perms = Permission.objects.filter(
            codename__in=['change_page', 'change_title', 'add_page', 'add_title', 'delete_page', 'delete_title']
        )
        normal_guy.save()
        normal_guy.user_permissions.set(perms)
        if use_global_permissions:
            gpp = GlobalPagePermission.objects.create(
                user=normal_guy,
                can_change=True,
                can_delete=True,
                can_change_advanced_settings=False,
                can_publish=True,
                can_change_permissions=False,
                can_move_page=True,
            )
            gpp.sites.set(Site.objects.all())
        return normal_guy


class AdminTestCase(AdminTestsBase):

    def test_extension_not_in_admin(self):
        admin_user, staff = self._get_guys()
        with self.login_user_context(admin_user):
            request = self.get_request(URL_CMS_PAGE_CHANGE % 1, 'en',)
~~            response = site.index(request)
            self.assertNotContains(response, '/mytitleextension/')
            self.assertNotContains(response, '/mypageextension/')

    def test_2apphooks_with_same_namespace(self):
        PAGE1 = 'Test Page'
        PAGE2 = 'Test page 2'
        APPLICATION_URLS = 'project.sampleapp.urls'

        admin_user, normal_guy = self._get_guys()

        current_site = Site.objects.get(pk=1)

        page = create_page(PAGE1, "nav_playground.html", "en",
                           site=current_site, created_by=admin_user)
        page2 = create_page(PAGE2, "nav_playground.html", "en",
                            site=current_site, created_by=admin_user)

        page.application_urls = APPLICATION_URLS
        page.application_namespace = "space1"
        page.save()
        page2.application_urls = APPLICATION_URLS
        page2.save()

        page_data = {


## ... source file abbreviated to get to site examples ...


        admin_user = self.get_superuser()
        create_page("home", "nav_playground.html", "en",
                           created_by=admin_user, published=True)
        page = create_page("delete-page", "nav_playground.html", "en",
                           created_by=admin_user, published=True)
        create_page('child-page', "nav_playground.html", "de",
                    created_by=admin_user, published=True, parent=page)
        body = page.placeholders.get(slot='body')
        add_plugin(body, 'TextPlugin', 'en', body='text')
        page.publish('en')
        with self.login_user_context(admin_user):
            data = {'post': 'yes'}
            response = self.client.post(URL_CMS_PAGE_DELETE % page.pk, data)
            self.assertRedirects(response, URL_CMS_PAGE)

    def test_search_fields(self):
        superuser = self.get_superuser()
        from django.contrib.admin import site

        with self.login_user_context(superuser):
~~            for model, admin_instance in site._registry.items():
                if model._meta.app_label != 'cms':
                    continue
                if not admin_instance.search_fields:
                    continue
                url = admin_reverse('cms_%s_changelist' % model._meta.model_name)
                response = self.client.get('%s?q=1' % url)
                errmsg = response.content
                self.assertEqual(response.status_code, 200, errmsg)

    def test_pagetree_filtered(self):
        superuser = self.get_superuser()
        create_page("root-page", "nav_playground.html", "en",
                    created_by=superuser, published=True)
        with self.login_user_context(superuser):
            url = admin_reverse('cms_page_changelist')
            response = self.client.get('%s?template__exact=nav_playground.html' % url)
            errmsg = response.content
            self.assertEqual(response.status_code, 200, errmsg)

    def test_delete_translation(self):
        admin_user = self.get_superuser()
        page = create_page("delete-page-translation", "nav_playground.html", "en",
                           created_by=admin_user, published=True)
        create_title("de", "delete-page-translation-2", page, slug="delete-page-translation-2")


## ... source file abbreviated to get to site examples ...


        page_admin = PageAdmin(Page, None)
        page_admin._current_page = page
        page.publish("en")
        draft_page = page.get_draft_object()
        admin_url = reverse("admin:cms_page_edit_title_fields", args=(
            draft_page.pk, language
        ))

        post_data = {
            'title': "A Title"
        }
        with self.login_user_context(admin_user):
            self.client.post(admin_url, post_data)
            draft_page = Page.objects.get(pk=page.pk).get_draft_object()
            self.assertTrue(draft_page.is_dirty('en'))


class NoDBAdminTests(CMSTestCase):
    @property
    def admin_class(self):
~~        return site._registry[Page]

    def test_lookup_allowed_site__exact(self):
        self.assertTrue(self.admin_class.lookup_allowed('site__exact', '1'))

    def test_lookup_allowed_published(self):
        self.assertTrue(self.admin_class.lookup_allowed('published', value='1'))


class PluginPermissionTests(AdminTestsBase):
    def setUp(self):
        self._page = create_page('test page', 'nav_playground.html', 'en')
        self._placeholder = self._page.placeholders.all()[0]

    def _get_admin(self):
        User = get_user_model()

        fields = dict(email="admin@django-cms.org", is_staff=True, is_active=True)

        if (User.USERNAME_FIELD != 'email'):
            fields[User.USERNAME_FIELD] = "admin"

        admin_user = User(**fields)

        admin_user.set_password('admin')


## ... source file abbreviated to get to site examples ...


        page2_data = {
            'reverse_id': 'p1',
            'template': 'col_two.html',
        }

        with self.login_user_context(superuser):
            response = self.client.post(page2_endpoint, page2_data)
            expected_error = (
                '<ul class="errorlist">'
                '<li>A page with this reverse URL id exists already.</li></ul>'
            )
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, expected_error.format(page2.pk), html=True)

    def test_advanced_settings_endpoint(self):
        admin_user = self.get_superuser()
        site = Site.objects.get_current()
        page = create_page('Page 1', 'nav_playground.html', 'en')
        page_data = {
            'language': 'en',
~~            'site': site.pk,
            'template': 'col_two.html',
        }
        path = admin_reverse('cms_page_advanced', args=(page.pk,))

        with self.login_user_context(admin_user):
            en_path = path + u"?language=en"
            redirect_path = admin_reverse('cms_page_changelist') + '?language=en'
            response = self.client.post(en_path, page_data)
            self.assertRedirects(response, redirect_path)
            self.assertEqual(Page.objects.get(pk=page.pk).template, 'col_two.html')

        page_data['language'] = 'de'
        page_data['template'] = 'nav_playground.html'

        with self.login_user_context(admin_user):
            de_path = path + u"?language=de"
            redirect_path = admin_reverse('cms_page_change', args=(page.pk,)) + '?language=de'
            response = self.client.post(de_path, page_data)
            self.assertRedirects(response, redirect_path)
            self.assertEqual(Page.objects.get(pk=page.pk).template, 'col_two.html')

        de_translation = create_title('de', title='Page 1', page=page.reload())
        de_translation.slug = ''
        de_translation.save()


## ... source file continues with no further site examples...

```

