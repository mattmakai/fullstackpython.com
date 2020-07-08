title: django.db.models.query prefetch_related_objects Example Code
category: page
slug: django-db-models-query-prefetch-related-objects-examples
sortorder: 500011244
toc: False
sidebartitle: django.db.models.query prefetch_related_objects
meta: Python example code for the prefetch_related_objects callable from the django.db.models.query module of the Django project.


prefetch_related_objects is a callable within the django.db.models.query module of the Django project.


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
~~from django.db.models.query import Prefetch, prefetch_related_objects
from django.urls import reverse
from django.utils.functional import SimpleLazyObject
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


## ... source file abbreviated to get to prefetch_related_objects examples ...


            .distinct()
        )

        if not self.renderer.draft_mode_active:
            pages = pages.select_related('publisher_public__node')
        pages = get_visible_nodes(request, pages, site)

        if not pages:
            return []

        try:
            homepage = [page for page in pages if page.is_home][0]
        except IndexError:
            homepage = None

        titles = Title.objects.filter(
            language__in=languages,
            publisher_is_draft=self.renderer.draft_mode_active,
        )

        lookup = Prefetch(
            'title_set',
            to_attr='filtered_translations',
            queryset=titles,
        )
~~        prefetch_related_objects(pages, lookup)
        blank_title_cache = {language: EmptyTitle(language=language) for language in languages}

        if lang not in blank_title_cache:
            blank_title_cache[lang] = EmptyTitle(language=lang)

        node_id_to_page = {}

        def _page_to_node(page):
            page.title_cache = blank_title_cache.copy()

            for trans in page.filtered_translations:
                page.title_cache[trans.language] = trans
            menu_node =  get_menu_node_for_page(
                self.renderer,
                page,
                language=lang,
                fallbacks=fallbacks,
            )
            return menu_node

        menu_nodes = []

        for page in pages:
            node = page.node


## ... source file continues with no further prefetch_related_objects examples...

```

