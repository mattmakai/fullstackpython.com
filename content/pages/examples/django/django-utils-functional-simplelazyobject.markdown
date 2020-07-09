title: django.utils.functional SimpleLazyObject Example Code
category: page
slug: django-utils-functional-simplelazyobject-examples
sortorder: 500011456
toc: False
sidebartitle: django.utils.functional SimpleLazyObject
meta: Python example code for the SimpleLazyObject class from the django.utils.functional module of the Django project.


SimpleLazyObject is a class within the django.utils.functional module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / cms_menus.py**](https://github.com/divio/django-cms/blob/develop/cms/./cms_menus.py)

```python
# cms_menus.py
from django.db.models.query import Prefetch, prefetch_related_objects
from django.urls import reverse
~~from django.utils.functional import SimpleLazyObject
from django.utils.translation import override as force_language

from cms import constants
from cms.api import get_page_draft
from cms.apphook_pool import apphook_pool
from cms.models import EmptyTitle
from cms.utils.conf import get_cms_setting
from cms.utils.i18n import (
    get_fallback_languages,
    get_public_languages,
    hide_untranslated,
    is_valid_site_language,
)
from cms.utils.permissions import get_view_restrictions
from cms.utils.page import get_page_queryset
from cms.utils.page_permissions import user_can_view_all_pages

from menus.base import Menu, NavigationNode, Modifier
from menus.menu_pool import menu_pool


def get_visible_nodes(request, pages, site):
    user = request.user
    _get_page_draft = get_page_draft
    public_for = get_cms_setting('PUBLIC_FOR')
    can_see_unrestricted = public_for == 'all' or (public_for == 'staff' and user.is_staff)

    if not user.is_authenticated and not can_see_unrestricted:
        return []

    if user_can_view_all_pages(user, site):
        return list(pages)

    draft_pages = [_get_page_draft(page) for page in pages]
    restricted_pages = get_view_restrictions(draft_pages)

    if not restricted_pages:
        return list(pages) if can_see_unrestricted else []

    user_id = user.pk
~~    user_groups = SimpleLazyObject(lambda: frozenset(user.groups.values_list('pk', flat=True)))
    is_auth_user = user.is_authenticated

    def user_can_see_page(page):
        page_id = page.pk if page.publisher_is_draft else page.publisher_public_id
        page_permissions = restricted_pages.get(page_id, [])

        if not page_permissions:
            return can_see_unrestricted

        if not is_auth_user:
            return False

        for perm in page_permissions:
            if perm.user_id == user_id or perm.group_id in user_groups:
                return True
        return False
    return [page for page in pages if user_can_see_page(page)]


def get_menu_node_for_page(renderer, page, language, fallbacks=None):
    if fallbacks is None:
        fallbacks = []

    attr = {


## ... source file continues with no further SimpleLazyObject examples...

```

