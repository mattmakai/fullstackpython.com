title: django.template.defaultfilters title Example Code
category: page
slug: django-template-defaultfilters-title-examples
sortorder: 500011388
toc: False
sidebartitle: django.template.defaultfilters title
meta: Python example code that shows how to use the title callable from the django.template.defaultfilters module of the Django project.


`title` is a callable within the `django.template.defaultfilters` module of the Django project.

<a href="/django-template-defaultfilters-escape-examples.html">escape</a>,
<a href="/django-template-defaultfilters-filesizeformat-examples.html">filesizeformat</a>,
<a href="/django-template-defaultfilters-safe-examples.html">safe</a>,
<a href="/django-template-defaultfilters-slugify-examples.html">slugify</a>,
<a href="/django-template-defaultfilters-striptags-examples.html">striptags</a>,
and <a href="/django-template-defaultfilters-truncatechars-examples.html">truncatechars</a>
are several other callables with code examples from the same `django.template.defaultfilters` package.

## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / models / placeholdermodel.py**](https://github.com/divio/django-cms/blob/develop/cms/models/placeholdermodel.py)

```python
# placeholdermodel.py

import warnings

from datetime import datetime, timedelta

from django.contrib import admin
from django.db import models
~~from django.template.defaultfilters import title
from django.utils.encoding import force_text
from django.utils.translation import gettext_lazy as _

from cms.cache.placeholder import clear_placeholder_cache
from cms.exceptions import LanguageError
from cms.utils import get_site_id
from cms.utils.i18n import get_language_object
from cms.utils.urlutils import admin_reverse
from cms.constants import (
    EXPIRE_NOW,
    MAX_EXPIRATION_TTL,
    PUBLISHER_STATE_DIRTY,
)
from cms.utils import get_language_from_request
from cms.utils import permissions
from cms.utils.conf import get_cms_setting


class Placeholder(models.Model):
    slot = models.CharField(_("slot"), max_length=255, db_index=True, editable=False)
    default_width = models.PositiveSmallIntegerField(_("width"), null=True, editable=False)
    cache_placeholder = True
    is_static = False
    is_editable = True


## ... source file abbreviated to get to title examples ...


            slot=self.slot,
            location=hex(id(self)),
        )
        return display

    def clear(self, language=None):
        if language:
            qs = self.cmsplugin_set.filter(language=language)
        else:
            qs = self.cmsplugin_set.all()
        qs = qs.order_by('-depth').select_related()
        for plugin in qs:
            inst, cls = plugin.get_plugin_instance()
            if inst and getattr(inst, 'cmsplugin_ptr', False):
                inst.cmsplugin_ptr._no_reorder = True
                inst._no_reorder = True
                inst.delete(no_mp=True)
            else:
                plugin._no_reorder = True
                plugin.delete(no_mp=True)

    def get_label(self):
        from cms.utils.placeholder import get_placeholder_conf

        template = self.page.get_template() if self.page else None
~~        name = get_placeholder_conf("name", self.slot, template=template, default=title(self.slot))
        name = _(name)
        return name

    def get_extra_context(self, template=None):
        from cms.utils.placeholder import get_placeholder_conf
        return get_placeholder_conf("extra_context", self.slot, template, {})

    def get_add_url(self):
        return self._get_url('add_plugin')

    def get_edit_url(self, plugin_pk):
        return self._get_url('edit_plugin', plugin_pk)

    def get_move_url(self):
        return self._get_url('move_plugin')

    def get_delete_url(self, plugin_pk):
        return self._get_url('delete_plugin', plugin_pk)

    def get_changelist_url(self):
        return self._get_url('changelist')

    def get_clear_url(self):
        return self._get_url('clear_placeholder', self.pk)


## ... source file continues with no further title examples...

```

