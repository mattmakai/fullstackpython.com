title: django.db.models.query_utils Q Example Code
category: page
slug: django-db-models-query-utils-q-examples
sortorder: 500011247
toc: False
sidebartitle: django.db.models.query_utils Q
meta: Python example code for the Q constant from the django.db.models.query_utils module of the Django project.


Q is a constant within the django.db.models.query_utils module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / utils / placeholder.py**](https://github.com/divio/django-cms/blob/develop/cms/utils/placeholder.py)

```python
# placeholder.py
import operator
import warnings
from collections import OrderedDict

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
~~from django.db.models.query_utils import Q
from django.template import TemplateSyntaxError, NodeList, Variable, Context, Template, engines
from django.template.base import VariableNode
from django.template.loader import get_template
from django.template.loader_tags import BlockNode, ExtendsNode, IncludeNode

from six import string_types

from sekizai.helpers import get_varname

from cms.exceptions import DuplicatePlaceholderWarning
from cms.utils.conf import get_cms_setting


def _get_nodelist(tpl):
    if hasattr(tpl, 'template'):
        return tpl.template.nodelist
    else:
        return tpl.nodelist


def get_context():
    if engines is not None:
        context = Context()
        context.template = Template('')


## ... source file abbreviated to get to Q examples ...



    def copy(self, **kwargs):
        return False

    def get_copy_languages(self, **kwargs):
        return []


class MLNGPlaceholderActions(PlaceholderNoAction):
    can_copy = True

    def copy(self, target_placeholder, source_language, fieldname, model, target_language, **kwargs):
        from cms.utils.copy_plugins import copy_plugins_to
        trgt = model.objects.get(**{fieldname: target_placeholder})
        src = model.objects.get(master=trgt.master, language_code=source_language)

        source_placeholder = getattr(src, fieldname, None)
        if not source_placeholder:
            return False
        return copy_plugins_to(source_placeholder.get_plugins_list(),
                               target_placeholder, target_language)

    def get_copy_languages(self, placeholder, model, fieldname, **kwargs):
        manager = model.objects
        src = manager.get(**{fieldname: placeholder})
~~        query = Q(master=src.master)
~~        query &= Q(**{'%s__cmsplugin__isnull' % fieldname: False})
        query &= -Q(pk=src.pk)

        language_codes = manager.filter(query).values_list('language_code', flat=True).distinct()
        return [(lc, dict(settings.LANGUAGES)[lc]) for lc in language_codes]


def restore_sekizai_context(context, changes):
    varname = get_varname()
    sekizai_container = context.get(varname)
    for key, values in changes.items():
        sekizai_namespace = sekizai_container[key]
        for value in values:
            sekizai_namespace.append(value)


def _scan_placeholders(nodelist, node_class=None, current_block=None, ignore_blocks=None):
    from cms.templatetags.cms_tags import Placeholder

    if not node_class:
        node_class = Placeholder

    nodes = []

    if ignore_blocks is None:


## ... source file continues with no further Q examples...

```

