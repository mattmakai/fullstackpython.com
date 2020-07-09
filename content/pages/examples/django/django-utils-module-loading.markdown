title: django.utils module_loading Example Code
category: page
slug: django-utils-module-loading-examples
sortorder: 500011419
toc: False
sidebartitle: django.utils module_loading
meta: Python example code for the module_loading callable from the django.utils module of the Django project.


module_loading is a callable within the django.utils module of the Django project.


## Example 1 from django-sitetree
[django-sitetree](https://github.com/idlesign/django-sitetree)
([project documentation](https://django-sitetree.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-sitetree/))
is a [Django](/django.html) extension that makes it easier for
developers to add site trees, menus and breadcrumb navigation elements
to their web applications.

The django-sitetree project is provided as open source under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/idlesign/django-sitetree/blob/master/LICENSE).

[**django-sitetree / sitetree / sitetreeapp.py**](https://github.com/idlesign/django-sitetree/blob/master/sitetree/./sitetreeapp.py)

```python
# sitetreeapp.py
import warnings
from collections import defaultdict
from copy import deepcopy
from inspect import getfullargspec
from sys import exc_info
from threading import local
from typing import Callable, List, Optional, Dict, Union, Sequence, Any, Tuple

from django.conf import settings
from django.core.cache import cache
from django.db.models import signals, QuerySet
from django.template.base import (
    FilterExpression, Lexer, Parser, Token, Variable, VariableDoesNotExist, VARIABLE_TAG_START, Context)
from django.template.defaulttags import url as url_tag
from django.template.loader import get_template
~~from django.utils import module_loading
from django.utils.http import urlquote
from django.utils.translation import get_language

from .compat import TOKEN_BLOCK, TOKEN_TEXT, TOKEN_VAR
from .exceptions import SiteTreeError
from .settings import (
    ALIAS_TRUNK, ALIAS_THIS_CHILDREN, ALIAS_THIS_SIBLINGS, ALIAS_THIS_PARENT_SIBLINGS, ALIAS_THIS_ANCESTOR_CHILDREN,
    UNRESOLVED_ITEM_MARKER, RAISE_ITEMS_ERRORS_ON_DEBUG, CACHE_TIMEOUT, DYNAMIC_ONLY, ADMIN_APP_NAME, SITETREE_CLS)
from .utils import get_tree_model, get_tree_item_model, import_app_sitetree_module, generate_id_for

if False:  # pragma: nocover
    from django.contrib.auth.models import User  # noqa
    from .models import TreeItemBase, TreeBase

TypeDynamicTrees = Dict[str, Union[Dict[str, List['TreeBase']], List['TreeBase']]]

MODEL_TREE_CLASS = get_tree_model()
MODEL_TREE_ITEM_CLASS = get_tree_item_model()


_ITEMS_PROCESSOR: Optional[Callable] = None

_ITEMS_PROCESSOR_ARGS_LEN: int = 0



## ... source file abbreviated to get to module_loading examples ...


            base_item.in_current_branch = True
            if hasattr(base_item, 'parent') and base_item.parent is not None:
                self.tree_climber(tree_alias, self.get_item_by_id(tree_alias, base_item.parent.id))

    def resolve_var(
            self,
            varname: Union[str, 'TreeItemBase', FilterExpression],
            context: Context = None
    ) -> Any:
        context = context or self.current_page_context

        if isinstance(varname, FilterExpression):
            varname = varname.resolve(context)

        else:
            varname = varname.strip()

            try:
                varname = Variable(varname).resolve(context)
            except VariableDoesNotExist:
                varname = varname

        return varname


~~_SITETREE_CLS = module_loading.import_string(SITETREE_CLS) if SITETREE_CLS else SiteTree



## ... source file continues with no further module_loading examples...

```

