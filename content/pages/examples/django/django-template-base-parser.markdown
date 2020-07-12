title: django.template.base Parser Example Code
category: page
slug: django-template-base-parser-examples
sortorder: 500011367
toc: False
sidebartitle: django.template.base Parser
meta: Python example code for the Parser class from the django.template.base module of the Django project.


Parser is a class within the django.template.base module of the Django project.


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

[**django-sitetree / sitetree / fields.py**](https://github.com/idlesign/django-sitetree/blob/master/sitetree/./fields.py)

```python
# fields.py
from typing import Optional

from django import template
~~from django.template.base import Parser, Token
from django.forms import ChoiceField
from django.utils.safestring import mark_safe

from .compat import TOKEN_BLOCK
from .templatetags.sitetree import sitetree_tree
from .utils import get_tree_model, get_tree_item_model
from .settings import ITEMS_FIELD_ROOT_ID

if False:  # pragma: nocover
    from .models import TreeItemBase, TreeBase  # noqa


MODEL_TREE_CLASS = get_tree_model()
MODEL_TREE_ITEM_CLASS = get_tree_item_model()


class TreeItemChoiceField(ChoiceField):
    template: str = 'admin/sitetree/tree/tree_combo.html'
    root_title: str = '---------'

    def __init__(
            self,
            tree: 'TreeBase' = None,
            required: bool = True,


## ... source file abbreviated to get to Parser examples ...


        super().__init__(
            required=required, widget=widget, label=label, initial=initial,
            help_text=help_text, *args, **kwargs)

        self.tree = None
        self.choices_init(tree)

    def choices_init(self, tree: Optional['TreeBase']):
        if not tree:
            return

        if isinstance(tree, MODEL_TREE_CLASS):
            tree = tree.alias

        self.tree = tree
        self.choices = self._build_choices()

    def _build_choices(self):
        tree_token = f'sitetree_tree from "{self.tree}" template "{self.template}"'

        context_kwargs = {'current_app': 'admin'}
        context = template.Context(context_kwargs)
        context.update({'request': object()})

        choices_str = sitetree_tree(
~~            Parser(None), Token(token_type=TOKEN_BLOCK, contents=tree_token)
        ).render(context)

        tree_choices = [(ITEMS_FIELD_ROOT_ID, self.root_title)]

        for line in choices_str.splitlines():
            if line.strip():
                splitted = line.split(':::')
                tree_choices.append((splitted[0], mark_safe(splitted[1])))

        return tree_choices

    def clean(self, value):
        if not value:
            return None

        try:
            return MODEL_TREE_ITEM_CLASS.objects.get(pk=value)

        except MODEL_TREE_ITEM_CLASS.DoesNotExist:
            return None



## ... source file continues with no further Parser examples...

```

