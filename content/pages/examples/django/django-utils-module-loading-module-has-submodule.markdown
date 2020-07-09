title: django.utils.module_loading module_has_submodule Example Code
category: page
slug: django-utils-module-loading-module-has-submodule-examples
sortorder: 500011482
toc: False
sidebartitle: django.utils.module_loading module_has_submodule
meta: Python example code for the module_has_submodule callable from the django.utils.module_loading module of the Django project.


module_has_submodule is a callable within the django.utils.module_loading module of the Django project.


## Example 1 from django-haystack
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

[**django-haystack / haystack / utils / loading.py**](https://github.com/django-haystack/django-haystack/blob/master/haystack/utils/loading.py)

```python
# loading.py
import copy
import inspect
import threading
import warnings
from collections import OrderedDict

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
~~from django.utils.module_loading import module_has_submodule

from haystack import constants
from haystack.exceptions import NotHandled, SearchFieldError
from haystack.utils import importlib
from haystack.utils.app_loading import haystack_get_app_modules


def import_class(path):
    path_bits = path.split(".")
    class_name = path_bits.pop()
    module_path = ".".join(path_bits)
    module_itself = importlib.import_module(module_path)

    if not hasattr(module_itself, class_name):
        raise ImportError(
            "The Python module '%s' has no '%s' class." % (module_path, class_name)
        )

    return getattr(module_itself, class_name)


def load_backend(full_backend_path):
    path_bits = full_backend_path.split(".")



## ... source file abbreviated to get to module_has_submodule examples ...


        self._indexes = {}
        self.fields = OrderedDict()
        self._built = False
        self.excluded_indexes = excluded_indexes or []
        self.excluded_indexes_ids = {}
        self.document_field = constants.DOCUMENT_FIELD
        self._fieldnames = {}
        self._facet_fieldnames = {}

    @property
    def indexes(self):
        warnings.warn(
            "'UnifiedIndex.indexes' was deprecated in Haystack v2.3.0. Please use UnifiedIndex.get_indexes()."
        )
        return self._indexes

    def collect_indexes(self):
        indexes = []

        for app_mod in haystack_get_app_modules():
            try:
                search_index_module = importlib.import_module(
                    "%s.search_indexes" % app_mod.__name__
                )
            except ImportError:
~~                if module_has_submodule(app_mod, "search_indexes"):
                    raise

                continue

            for item_name, item in inspect.getmembers(
                search_index_module, inspect.isclass
            ):
                if getattr(item, "haystack_use_for_indexing", False) and getattr(
                    item, "get_model", None
                ):
                    class_path = "%s.search_indexes.%s" % (app_mod.__name__, item_name)

                    if class_path in self.excluded_indexes or self.excluded_indexes_ids.get(
                        item_name
                    ) == id(
                        item
                    ):
                        self.excluded_indexes_ids[str(item_name)] = id(item)
                        continue

                    indexes.append(item())

        return indexes



## ... source file continues with no further module_has_submodule examples...

```


## Example 2 from django-sitetree
[django-sitetree](https://github.com/idlesign/django-sitetree)
([project documentation](https://django-sitetree.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-sitetree/))
is a [Django](/django.html) extension that makes it easier for
developers to add site trees, menus and breadcrumb navigation elements
to their web applications.

The django-sitetree project is provided as open source under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/idlesign/django-sitetree/blob/master/LICENSE).

[**django-sitetree / sitetree / utils.py**](https://github.com/idlesign/django-sitetree/blob/master/sitetree/./utils.py)

```python
# utils.py
from importlib import import_module
from types import ModuleType
from typing import Any, Sequence, Type, Union, List, Optional, Tuple

from django.apps import apps
from django.contrib.auth.models import Permission
from django.core.exceptions import ImproperlyConfigured
~~from django.utils.module_loading import module_has_submodule

from . import settings

if False:  # pragma: nocover
    from .models import TreeItemBase, TreeBase  # noqa


TypePermission = Union[str, int, Permission]

apps_get_model = apps.get_model


def generate_id_for(obj: Any):
    return id(obj)


def tree(alias: str, title: str = '', items: Sequence['TreeItemBase'] = None, **kwargs) -> 'TreeBase':
    tree_obj = get_tree_model()(alias=alias, title=title, **kwargs)
    tree_obj.id = generate_id_for(tree_obj)
    tree_obj.is_dynamic = True

    if items is not None:
        tree_obj.dynamic_items = []



## ... source file abbreviated to get to module_has_submodule examples ...


            cleaned_permissions.append(perm)

    item_obj.permissions = cleaned_permissions or []
    item_obj.access_perm_type = item_obj.PERM_TYPE_ALL if perms_mode_all else item_obj.PERM_TYPE_ANY

    if item_obj.permissions:
        item_obj.access_restricted = True

    if children is not None:
        for child in children:
            child.parent = item_obj
            item_obj.dynamic_children.append(child)

    return item_obj


def import_app_sitetree_module(app: str) -> Optional[ModuleType]:
    module_name = settings.APP_MODULE_NAME
    module = import_module(app)

    try:
        sub_module = import_module(f'{app}.{module_name}')
        return sub_module

    except ImportError:
~~        if module_has_submodule(module, module_name):
            raise
        return None


def import_project_sitetree_modules() -> List[ModuleType]:
    from django.conf import settings as django_settings

    submodules = []
    for app in django_settings.INSTALLED_APPS:
        module = import_app_sitetree_module(app)
        if module is not None:
            submodules.append(module)

    return submodules


def get_app_n_model(settings_entry_name: str) -> Tuple[str, str]:
    try:
        app_name, model_name = getattr(settings, settings_entry_name).split('.')

    except ValueError:
        raise ImproperlyConfigured(
            f'`SITETREE_{settings_entry_name}` must have the following format: `app_name.model_name`.')



## ... source file continues with no further module_has_submodule examples...

```


## Example 3 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / utils / apps.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/utils/apps.py)

```python
# apps.py
from importlib import import_module

from django.apps import apps
~~from django.utils.module_loading import module_has_submodule


def get_app_modules():
    for app in apps.get_app_configs():
        yield app.name, app.module


def get_app_submodules(submodule_name):
    for name, module in get_app_modules():
~~        if module_has_submodule(module, submodule_name):
            yield name, import_module('%s.%s' % (name, submodule_name))



## ... source file continues with no further module_has_submodule examples...

```

