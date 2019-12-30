title: django.http HttpResponseBadRequest Python Code Examples
category: page
slug: django-http-httpresponsebadrequest-examples
sortorder: 500013430
toc: False
sidebartitle: django.http HttpResponseBadRequest
meta: Example Python code for using the HttpResponseBadRequest object provided by Django in the django.http module.


[HttpResponseBadRequest](https://docs.djangoproject.com/en/stable/ref/request-response/#django.http.HttpResponseBadRequest)
([source code](https://github.com/django/django/blob/master/django/http/response.py))
returns the 
[HTTP 400 status code](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) 
from a [Django](/django.html) web application view. The HTTP 400 status code
indicates that a request could not be understood by the server because of 
to malformed syntax and the request should be modified before being resent
to the server.


## Example 1 from django-angular
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


## ... source code abbreviated to get to the example ...


class JSONResponseMixin(JSONBaseMixin):
    """
    A mixin for View classes that dispatches requests containing 
    the private HTTP header ``DjNg-Remote-Method`` onto a method of an 
    instance of this class, with the given method name. This named method 
    must be decorated with ``@allow_remote_invocation`` and shall return a
    list or dictionary which is serializable to JSON.
    The returned HTTP responses are of 
    kind ``application/json;charset=UTF-8``.
    """
    def get(self, request, *args, **kwargs):
        if not request.is_ajax():
            return self._dispatch_super(request, *args, **kwargs)
        if 'action' in kwargs:
            warnings.warn("Using the keyword 'action' in URLresolvers is "
                          "deprecated. Please use 'invoke_method' instead", 
                          DeprecationWarning)
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
            if not hasattr(handler, 'allow_rmi'):
                return HttpResponseForbidden("Method '{0}.{1}' has no "
                                             "decorator '@allow_remote_"
                                             "invocation'"
                                             .format(self.__class__.__name__, 
                                                     remote_method))
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
            warnings.warn("Using the keyword 'action' inside the payload "
                          "is deprecated. Please use 'djangoRMI' from "
                          "module 'djng.forms'", DeprecationWarning)
            remote_method = in_data.pop('action')
        else:
            remote_method = request.META.get('HTTP_DJNG_REMOTE_METHOD')
        handler = remote_method and getattr(self, remote_method, None)
        if not callable(handler):
            return self._dispatch_super(request, *args, **kwargs)
        if not hasattr(handler, 'allow_rmi'):
            return HttpResponseForbidden("Method '{0}.{1}' has no decorator "
                                         "'@allow_remote_invocation'"
                                         .format(self.__class__.__name__, 
                                                 remote_method), 403)
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
~~        return HttpResponseBadRequest('This view can not handle method {0}'.\
~~                                      format(request.method), status=405)

```


## Example 2 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / tests / test_admin.py**](https://github.com/divio/django-cms/blob/develop/cms/tests/test_admin.py)

```python
# -*- coding: utf-8 -*-
import json
import datetime

from djangocms_text_ckeditor.cms_plugins import TextPlugin
from djangocms_text_ckeditor.models import Text
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.admin.sites import site
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.sites.models import Site
from django.urls import reverse
~~from django.http import (Http404, HttpResponseBadRequest,
~~                         HttpResponseNotFound)
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
        return site._registry[Page]

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
            response = site.index(request)
            self.assertNotContains(response, '/mytitleextension/')
            self.assertNotContains(response, '/mypageextension/')

    def test_2apphooks_with_same_namespace(self):
        PAGE1 = 'Test Page'
        PAGE2 = 'Test page 2'
        APPLICATION_URLS = 'project.sampleapp.urls'

        admin_user, normal_guy = self._get_guys()

        current_site = Site.objects.get(pk=1)

        # The admin creates the page
        page = create_page(PAGE1, "nav_playground.html", "en",
                           site=current_site, created_by=admin_user)
        page2 = create_page(PAGE2, "nav_playground.html", "en",
                            site=current_site, created_by=admin_user)

        page.application_urls = APPLICATION_URLS
        page.application_namespace = "space1"
        page.save()
        page2.application_urls = APPLICATION_URLS
        page2.save()

        # The admin edits the page (change the page name for ex.)
        page_data = {
            'title': PAGE2,
            'slug': page2.get_slug(),
            'template': page2.template,
            'application_urls': 'SampleApp',
            'application_namespace': 'space1',
        }

        with self.login_user_context(admin_user):
            resp = self.client.post(base.URL_CMS_PAGE_ADVANCED_CHANGE % page.pk, page_data)
            self.assertEqual(resp.status_code, 302)
            self.assertEqual(Page.objects.filter(application_namespace="space1").count(), 1)
            resp = self.client.post(base.URL_CMS_PAGE_ADVANCED_CHANGE % page2.pk, page_data)
            self.assertEqual(resp.status_code, 200)
            page_data['application_namespace'] = 'space2'
            resp = self.client.post(base.URL_CMS_PAGE_ADVANCED_CHANGE % page2.pk, page_data)
            self.assertEqual(resp.status_code, 302)

    def test_delete(self):
        admin_user = self.get_superuser()
        create_page("home", "nav_playground.html", "en",
                           created_by=admin_user, published=True)
        page = create_page("delete-page", "nav_playground.html", "en",
                           created_by=admin_user, published=True)
        create_page('child-page', "nav_playground.html", "en",
                    created_by=admin_user, published=True, parent=page)
        body = page.placeholders.get(slot='body')
        add_plugin(body, 'TextPlugin', 'en', body='text')
        page.publish('en')
        with self.login_user_context(admin_user):
            data = {'post': 'yes'}
            response = self.client.post(URL_CMS_PAGE_DELETE % page.pk, data)
            self.assertRedirects(response, URL_CMS_PAGE)

    def test_delete_diff_language(self):
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
            for model, admin_instance in site._registry.items():
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
        create_title("es-mx", "delete-page-translation-es", page, slug="delete-page-translation-es")
        with self.login_user_context(admin_user):
            response = self.client.get(URL_CMS_TRANSLATION_DELETE % page.pk, {'language': 'de'})
            self.assertEqual(response.status_code, 200)
            response = self.client.post(URL_CMS_TRANSLATION_DELETE % page.pk, {'language': 'de'})
            self.assertRedirects(response, URL_CMS_PAGE)
            response = self.client.get(URL_CMS_TRANSLATION_DELETE % page.pk, {'language': 'es-mx'})
            self.assertEqual(response.status_code, 200)
            response = self.client.post(URL_CMS_TRANSLATION_DELETE % page.pk, {'language': 'es-mx'})
            self.assertRedirects(response, URL_CMS_PAGE)

    def test_change_dates(self):
        admin_user, staff = self._get_guys()

        with self.settings(USE_TZ=False, TIME_ZONE='UTC'):

            page = create_page('test-page', 'nav_playground.html', 'en')
            page.publish('en')
            draft = page.get_draft_object()

            original_date = draft.publication_date
            original_end_date = draft.publication_end_date
            new_date = timezone.now() - datetime.timedelta(days=1)
            new_end_date = timezone.now() + datetime.timedelta(days=1)
            url = admin_reverse('cms_page_dates', args=(draft.pk,))
            with self.login_user_context(admin_user):
                response = self.client.post(url, {
                    'publication_date_0': new_date.date(),
                    'publication_date_1': new_date.strftime("%H:%M:%S"),
                    'publication_end_date_0': new_end_date.date(),
                    'publication_end_date_1': new_end_date.strftime("%H:%M:%S"),
                })
                self.assertEqual(response.status_code, 302)
                draft = Page.objects.get(pk=draft.pk)
                self.assertNotEqual(draft.publication_date.timetuple(), original_date.timetuple())
                self.assertEqual(draft.publication_date.timetuple(), new_date.timetuple())
                self.assertEqual(draft.publication_end_date.timetuple(), new_end_date.timetuple())
                if original_end_date:
                    self.assertNotEqual(draft.publication_end_date.timetuple(), original_end_date.timetuple())

        with self.settings(USE_TZ=True, TIME_ZONE='UTC'):

            page = create_page('test-page-2', 'nav_playground.html', 'en')
            page.publish('en')
            draft = page.get_draft_object()

            original_date = draft.publication_date
            original_end_date = draft.publication_end_date
            new_date = timezone.localtime(timezone.now()) - datetime.timedelta(days=1)
            new_end_date = timezone.localtime(timezone.now()) + datetime.timedelta(days=1)
            url = admin_reverse('cms_page_dates', args=(draft.pk,))
            with self.login_user_context(admin_user):
                response = self.client.post(url, {
                    'language': 'en',
                    'publication_date_0': new_date.date(),
                    'publication_date_1': new_date.strftime("%H:%M:%S"),
                    'publication_end_date_0': new_end_date.date(),
                    'publication_end_date_1': new_end_date.strftime("%H:%M:%S"),
                })
                self.assertEqual(response.status_code, 302)
                draft = Page.objects.get(pk=draft.pk)
                self.assertNotEqual(draft.publication_date.timetuple(), original_date.timetuple())
                self.assertEqual(timezone.localtime(draft.publication_date).timetuple(), new_date.timetuple())
                self.assertEqual(timezone.localtime(draft.publication_end_date).timetuple(), new_end_date.timetuple())
                if original_end_date:
                    self.assertNotEqual(draft.publication_end_date.timetuple(), original_end_date.timetuple())

    def test_change_template(self):
        template = get_cms_setting('TEMPLATES')[0][0]
        admin_user, staff = (self.get_superuser(), self.get_staff_user_with_no_permissions())

        with self.login_user_context(admin_user):
            response = self.client.post(
                self.get_admin_url(Page, 'change_template', 1),
                {'template': template}
            )
            self.assertEqual(response.status_code, 404)

        with self.login_user_context(staff):
            response = self.client.post(
                self.get_admin_url(Page, 'change_template', 1),
                {'template': template}
            )
            self.assertEqual(response.status_code, 403)

        page = create_page('test-page', template, 'en')

        with self.login_user_context(staff):
            response = self.client.post(
                self.get_admin_url(Page, 'change_template', page.pk),
                {'template': template}
            )
            self.assertEqual(response.status_code, 403)

        with self.login_user_context(admin_user):
            response = self.client.post(
                self.get_admin_url(Page, 'change_template', page.pk),
                {'template': 'doesntexist'}
            )
            self.assertEqual(response.status_code, 400)
            response = self.client.post(
                self.get_admin_url(Page, 'change_template', page.pk),
                {'template': template}
            )
            self.assertEqual(response.status_code, 200)

    def test_changelist_items(self):
        admin_user = self.get_superuser()
        first_level_page = create_page('level1', 'nav_playground.html', 'en')
        second_level_page_top = create_page('level21', "nav_playground.html", "en",
                                            created_by=admin_user, published=True, parent=first_level_page)
        second_level_page_bottom = create_page('level22', "nav_playground.html", "en",
                                               created_by=admin_user, published=True,
                                               parent=self.reload(first_level_page))
        third_level_page = create_page('level3', "nav_playground.html", "en",
                                       created_by=admin_user, published=True, parent=second_level_page_top)
        self.assertEqual(Page.objects.all().count(), 4)

        with self.login_user_context(admin_user):
            response = self.client.get(self.get_admin_url(Page, 'changelist'))
            cms_page_nodes = response.context_data['tree']['items']
            self.assertEqual(cms_page_nodes[0], first_level_page)
            self.assertEqual(cms_page_nodes[1], second_level_page_top)
            self.assertEqual(cms_page_nodes[2], third_level_page)
            self.assertEqual(cms_page_nodes[3], second_level_page_bottom)

    def test_changelist_get_results(self):
        admin_user = self.get_superuser()
        first_level_page = create_page('level1', 'nav_playground.html', 'en', published=True)
        second_level_page_top = create_page('level21', "nav_playground.html", "en",
                                            created_by=admin_user, published=True,
                                            parent=first_level_page)
        second_level_page_bottom = create_page('level22', "nav_playground.html", "en", # nopyflakes
                                               created_by=admin_user, published=True,
                                               parent=self.reload(first_level_page))
        third_level_page = create_page('level3', "nav_playground.html", "en", # nopyflakes
                                       created_by=admin_user, published=True,
                                       parent=second_level_page_top)
        fourth_level_page = create_page('level23', "nav_playground.html", "en", # nopyflakes
                                        created_by=admin_user,
                                        parent=self.reload(first_level_page))
        self.assertEqual(Page.objects.all().count(), 9)
        endpoint = self.get_admin_url(Page, 'changelist')

        with self.login_user_context(admin_user):
            response = self.client.get(endpoint)
            self.assertEqual(response.context_data['tree']['items'].count(), 5)

        with self.login_user_context(admin_user):
            response = self.client.get(endpoint + '?q=level23')
            self.assertEqual(response.context_data['tree']['items'].count(), 1)

        with self.login_user_context(admin_user):
            response = self.client.get(endpoint + '?q=level2')
            self.assertEqual(response.context_data['tree']['items'].count(), 3)

    def test_unihandecode_doesnt_break_404_in_admin(self):
        self.get_superuser()

        if get_user_model().USERNAME_FIELD == 'email':
            self.client.login(username='admin@django-cms.org', password='admin@django-cms.org')
        else:
            self.client.login(username='admin', password='admin')

        response = self.client.get(URL_CMS_PAGE_CHANGE_LANGUAGE % (1, 'en'))
        self.assertEqual(response.status_code, 404)

    def test_empty_placeholder_with_nested_plugins(self):
        # It's important that this test clears a placeholder
        # which only has nested plugins.
        # This allows us to catch a strange bug that happened
        # under these conditions with the new related name handling.
        page_en = create_page("EmptyPlaceholderTestPage (EN)", "nav_playground.html", "en")
        ph = page_en.placeholders.get(slot="body")

        column_wrapper = add_plugin(ph, "MultiColumnPlugin", "en")

        add_plugin(ph, "ColumnPlugin", "en", parent=column_wrapper)
        add_plugin(ph, "ColumnPlugin", "en", parent=column_wrapper)

        # before cleaning the de placeholder
        self.assertEqual(ph.get_plugins('en').count(), 3)

        admin_user, staff = self._get_guys()
        endpoint = self.get_clear_placeholder_url(ph, language='en')

        with self.login_user_context(admin_user):
            response = self.client.post(endpoint, {'test': 0})

        self.assertEqual(response.status_code, 302)

        # After cleaning the de placeholder, en placeholder must still have all the plugins
        self.assertEqual(ph.get_plugins('en').count(), 0)

    def test_empty_placeholder_in_correct_language(self):
        """
        Test that Cleaning a placeholder only affect current language contents
        """
        # create some objects
        page_en = create_page("EmptyPlaceholderTestPage (EN)", "nav_playground.html", "en")
        ph = page_en.placeholders.get(slot="body")

        # add the text plugin to the en version of the page
        add_plugin(ph, "TextPlugin", "en", body="Hello World EN 1")
        add_plugin(ph, "TextPlugin", "en", body="Hello World EN 2")

        # creating a de title of the page and adding plugins to it
        create_title("de", page_en.get_title(), page_en, slug=page_en.get_slug())
        add_plugin(ph, "TextPlugin", "de", body="Hello World DE")
        add_plugin(ph, "TextPlugin", "de", body="Hello World DE 2")
        add_plugin(ph, "TextPlugin", "de", body="Hello World DE 3")

        # before cleaning the de placeholder
        self.assertEqual(ph.get_plugins('en').count(), 2)
        self.assertEqual(ph.get_plugins('de').count(), 3)

        admin_user, staff = self._get_guys()
        endpoint = self.get_clear_placeholder_url(ph, language='de')

        with self.login_user_context(admin_user):
            response = self.client.post(endpoint, {'test': 0})

        self.assertEqual(response.status_code, 302)

        # After cleaning the de placeholder, en placeholder must still have all the plugins
        self.assertEqual(ph.get_plugins('en').count(), 2)
        self.assertEqual(ph.get_plugins('de').count(), 0)


class AdminTests(AdminTestsBase):
    # TODO: needs tests for actual permissions, not only superuser/normaluser

    def setUp(self):
        self.page = create_page("testpage", "nav_playground.html", "en")

    def get_admin(self):
        User = get_user_model()

        fields = dict(email="admin@django-cms.org", is_staff=True, is_superuser=True)

        if (User.USERNAME_FIELD != 'email'):
            fields[User.USERNAME_FIELD] = "admin"

        usr = User(**fields)
        usr.set_password(getattr(usr, User.USERNAME_FIELD))
        usr.save()
        return usr

    def get_permless(self):
        User = get_user_model()

        fields = dict(email="permless@django-cms.org", is_staff=True)

        if (User.USERNAME_FIELD != 'email'):
            fields[User.USERNAME_FIELD] = "permless"

        usr = User(**fields)
        usr.set_password(getattr(usr, User.USERNAME_FIELD))
        usr.save()
        return usr

    def get_page(self):
        return self.page

    def test_change_publish_unpublish(self):
        page = self.get_page()
        permless = self.get_permless()
        with self.login_user_context(permless):
            request = self.get_request()
            response = self.admin_class.publish_page(request, page.pk, "en")
            self.assertEqual(response.status_code, 405)
            page = self.reload(page)
            self.assertFalse(page.is_published('en'))

            request = self.get_request(post_data={'no': 'data'})
            response = self.admin_class.publish_page(request, page.pk, "en")
            self.assertEqual(response.status_code, 403)
            page = self.reload(page)
            self.assertFalse(page.is_published('en'))

        admin_user = self.get_admin()
        with self.login_user_context(admin_user):
            request = self.get_request(post_data={'no': 'data'})
            response = self.admin_class.publish_page(request, page.pk, "en")
            self.assertEqual(response.status_code, 302)

            page = self.reload(page)
            self.assertTrue(page.is_published('en'))

            response = self.admin_class.unpublish(request, page.pk, "en")
            self.assertEqual(response.status_code, 302)

            page = self.reload(page)
            self.assertFalse(page.is_published('en'))

    def test_change_status_adds_log_entry(self):
        page = self.get_page()
        admin_user = self.get_admin()
        with self.login_user_context(admin_user):
            request = self.get_request(post_data={'no': 'data'})
            self.assertFalse(LogEntry.objects.count())
            response = self.admin_class.publish_page(request, page.pk, "en")
            self.assertEqual(response.status_code, 302)
            self.assertEqual(1, LogEntry.objects.count())
            self.assertEqual(page.pk, int(LogEntry.objects.all()[0].object_id))

    def test_change_innavigation(self):
        page = self.get_page()
        permless = self.get_permless()
        admin_user = self.get_admin()
        with self.login_user_context(permless):
            request = self.get_request()
            response = self.admin_class.change_innavigation(request, page.pk)
            self.assertEqual(response.status_code, 405)
        with self.login_user_context(permless):
            request = self.get_request(post_data={'no': 'data'})
            response = self.admin_class.change_innavigation(request, page.pk)
            self.assertEqual(response.status_code, 403)
        with self.login_user_context(permless):
            request = self.get_request(post_data={'no': 'data'})
            self.assertEqual(response.status_code, 403)
        with self.login_user_context(admin_user):
            request = self.get_request(post_data={'no': 'data'})
            self.assertRaises(Http404, self.admin_class.change_innavigation,
                              request, page.pk + 100)
        with self.login_user_context(permless):
            request = self.get_request(post_data={'no': 'data'})
            response = self.admin_class.change_innavigation(request, page.pk)
            self.assertEqual(response.status_code, 403)
        with self.login_user_context(admin_user):
            request = self.get_request(post_data={'no': 'data'})
            old = page.in_navigation
            response = self.admin_class.change_innavigation(request, page.pk)
            self.assertEqual(response.status_code, 204)
            page = self.reload(page)
            self.assertEqual(old, not page.in_navigation)

    def test_publish_page_requires_perms(self):
        permless = self.get_permless()
        with self.login_user_context(permless):
            request = self.get_request()
            request.method = "POST"
            response = self.admin_class.publish_page(request, Page.objects.drafts().first().pk, "en")
            self.assertEqual(response.status_code, 403)

    def test_remove_plugin_requires_post(self):
        ph = self.page.placeholders.all()[0]
        plugin = add_plugin(ph, 'TextPlugin', 'en', body='test')
        admin_user = self.get_admin()
        with self.login_user_context(admin_user):
            endpoint = self.get_delete_plugin_uri(plugin, container=self.page)
            response = self.client.get(endpoint)
            self.assertEqual(response.status_code, 200)

    def test_move_language(self):
        page = self.get_page()
        source, target = list(page.placeholders.all())[:2]
        col = add_plugin(source, 'MultiColumnPlugin', 'en')
        sub_col = add_plugin(source, 'ColumnPlugin', 'en', target=col)
        col2 = add_plugin(source, 'MultiColumnPlugin', 'de')

        admin_user = self.get_admin()
        with self.login_user_context(admin_user):
            data = {
                'plugin_id': sub_col.pk,
                'placeholder_id': source.id,
                'plugin_parent': col2.pk,
                'target_language': 'de'
            }
            endpoint = self.get_move_plugin_uri(sub_col)
            response = self.client.post(endpoint, data)
            self.assertEqual(response.status_code, 200)
        sub_col = CMSPlugin.objects.get(pk=sub_col.pk)
        self.assertEqual(sub_col.language, "de")
        self.assertEqual(sub_col.parent_id, col2.pk)

    def test_preview_page(self):
        permless = self.get_permless()
        with self.login_user_context(permless):
            request = self.get_request()
            self.assertRaises(Http404, self.admin_class.preview_page, request, 404, "en")
        page = self.get_page()
        page.publish("en")
        page.set_as_homepage()

        new_site = Site.objects.create(id=2, domain='django-cms.org', name='django-cms')
        new_page = create_page("testpage", "nav_playground.html", "fr", site=new_site, published=True)

        base_url = page.get_absolute_url()
        with self.login_user_context(permless):
            request = self.get_request('/?public=true')
            response = self.admin_class.preview_page(request, page.pk, 'en')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response['Location'], '%s?%s&language=en' % (base_url, get_cms_setting('CMS_TOOLBAR_URL__EDIT_ON')))
            request = self.get_request()
            response = self.admin_class.preview_page(request, page.pk, 'en')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response['Location'], '%s?%s&language=en' % (base_url, get_cms_setting('CMS_TOOLBAR_URL__EDIT_ON')))

            # Switch active site
            request.session['cms_admin_site'] = new_site.pk

            # Preview page attached to active site but not to current site
            response = self.admin_class.preview_page(request, new_page.pk, 'fr')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response['Location'],
                             'http://django-cms.org/fr/testpage/?%s&language=fr' % get_cms_setting('CMS_TOOLBAR_URL__EDIT_ON'))

    def test_too_many_plugins_global(self):
        conf = {
            'body': {
                'limits': {
                    'global': 1,
                },
            },
        }
        admin_user = self.get_admin()
        url = admin_reverse('cms_page_add_plugin')
        with self.settings(CMS_PERMISSION=False, CMS_PLACEHOLDER_CONF=conf):
            page = create_page('somepage', 'nav_playground.html', 'en')
            body = page.placeholders.get(slot='body')
            add_plugin(body, 'TextPlugin', 'en', body='text')
            with self.login_user_context(admin_user):
                data = {
                    'plugin_type': 'TextPlugin',
                    'placeholder_id': body.pk,
                    'target_language': 'en',
                }
                response = self.client.post(url, data)
~~                self.assertEqual(response.status_code, 
~~                                 HttpResponseBadRequest.status_code)

    def test_too_many_plugins_type(self):
        conf = {
            'body': {
                'limits': {
                    'TextPlugin': 1,
                },
            },
        }
        admin_user = self.get_admin()
        url = admin_reverse('cms_page_add_plugin')
        with self.settings(CMS_PERMISSION=False, CMS_PLACEHOLDER_CONF=conf):
            page = create_page('somepage', 'nav_playground.html', 'en')
            body = page.placeholders.get(slot='body')
            add_plugin(body, 'TextPlugin', 'en', body='text')
            with self.login_user_context(admin_user):
                data = {
                    'plugin_type': 'TextPlugin',
                    'placeholder_id': body.pk,
                    'target_language': 'en',
                    'plugin_parent': '',
                }
                response = self.client.post(url, data)
~~                self.assertEqual(response.status_code, 
~~                                 HttpResponseBadRequest.status_code)


## ... source file continues with no further HttpResponseBadRequest examples ...
```


## Example 3 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / admin / views.py**](https://github.com/divio/django-filer/blob/develop/filer/admin/views.py)

```python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib import admin
from django.contrib.admin import widgets
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
~~from django.http.response import HttpResponseBadRequest
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from .. import settings as filer_settings
from ..models import Clipboard, Folder, FolderRoot, tools
from .tools import AdminContext, admin_url_params_encoded, popup_status


class NewFolderForm(forms.ModelForm):
    class Meta(object):
        model = Folder
        fields = ('name',)
        widgets = {
            'name': widgets.AdminTextInputWidget,
        }


@login_required
def make_folder(request, folder_id=None):
    if not folder_id:
        folder_id = request.GET.get('parent_id')
    if not folder_id:
        folder_id = request.POST.get('parent_id')
    if folder_id:
        try:
            folder = Folder.objects.get(id=folder_id)
        except Folder.DoesNotExist:
            raise PermissionDenied
    else:
        folder = None

    if request.user.is_superuser:
        pass
    elif folder is None:
        # regular users may not add root folders unless configured otherwise
        if not filer_settings.FILER_ALLOW_REGULAR_USERS_TO_ADD_ROOT_FOLDERS:
            raise PermissionDenied
    elif not folder.has_add_children_permission(request):
        # the user does not have the permission to add subfolders
        raise PermissionDenied

    if request.method == 'POST':
        new_folder_form = NewFolderForm(request.POST)
        if new_folder_form.is_valid():
            new_folder = new_folder_form.save(commit=False)
            if (folder or FolderRoot()).contains_folder(new_folder.name):
                new_folder_form._errors['name'] = new_folder_form.error_class(
                    [_('Folder with this name already exists.')])
            else:
                context = admin.site.each_context(request)
                new_folder.parent = folder
                new_folder.owner = request.user
                new_folder.save()
                return render(request, 'admin/filer/dismiss_popup.html', context)
    else:
        new_folder_form = NewFolderForm()

    context = admin.site.each_context(request)
    context.update({
        'opts': Folder._meta,
        'new_folder_form': new_folder_form,
        'is_popup': popup_status(request),
        'filer_admin_context': AdminContext(request),
    })
    return render(request, 'admin/filer/folder/new_folder_form.html', context)


@login_required
def paste_clipboard_to_folder(request):
~~    if True:
~~        # TODO: cleanly remove Clipboard code if it is no longer needed
~~        return HttpResponseBadRequest('not implemented anymore')

    if request.method == 'POST':
        folder = Folder.objects.get(id=request.POST.get('folder_id'))
        clipboard = Clipboard.objects.get(id=request.POST.get('clipboard_id'))
        if folder.has_add_children_permission(request):
            tools.move_files_from_clipboard_to_folder(clipboard, folder)
            tools.discard_clipboard(clipboard)
        else:
            raise PermissionDenied
    redirect = request.GET.get('redirect_to', '')
    if not redirect:
        redirect = request.POST.get('redirect_to', '')
    return HttpResponseRedirect(
        '{0}?order_by=-modified_at{1}'.format(
            redirect,
            admin_url_params_encoded(request, first_separator='&'),
        )
    )


@login_required
def discard_clipboard(request):
~~    if True:
~~        # TODO: cleanly remove Clipboard code if it is no longer needed
~~        return HttpResponseBadRequest('not implemented anymore')

    if request.method == 'POST':
        clipboard = Clipboard.objects.get(id=request.POST.get('clipboard_id'))
        tools.discard_clipboard(clipboard)
    return HttpResponseRedirect(
        '{0}{1}'.format(
            request.POST.get('redirect_to', ''),
            admin_url_params_encoded(request, first_separator='&'),
        )
    )


@login_required
def delete_clipboard(request):
~~    if True:
~~        # TODO: cleanly remove Clipboard code if it is no longer needed
~~        return HttpResponseBadRequest('not implemented anymore')

    if request.method == 'POST':
        clipboard = Clipboard.objects.get(id=request.POST.get('clipboard_id'))
        tools.delete_clipboard(clipboard)
    return HttpResponseRedirect(
        '{0}{1}'.format(
            request.POST.get('redirect_to', ''),
            admin_url_params_encoded(request, first_separator='&'),
        )
    )

```


