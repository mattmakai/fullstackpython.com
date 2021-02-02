title: django.template.loaders.filesystem Loader Example Code
category: page
slug: django-template-loaders-filesystem-loader-examples
sortorder: 500011398
toc: False
sidebartitle: django.template.loaders.filesystem Loader
meta: Example code for understanding how to use the Loader class from the django.template.loaders.filesystem module of the Django project.


`Loader` is a class within the `django.template.loaders.filesystem` module of the Django project.



## Example 1 from django-markdown-view
[django-markdown-view](https://github.com/rgs258/django-markdown-view)
([PyPI package information](https://pypi.org/project/django-markdown-view/))
is a Django extension for serving [Markdown](/markdown.html) files as
[Django templates](/django-templates.html). The project is open
sourced under the
[BSD 3-Clause "New" or "Revised" license](https://github.com/rgs258/django-markdown-view/blob/master/LICENSE).

[**django-markdown-view / markdown_view / loaders.py**](https://github.com/rgs258/django-markdown-view/blob/master/markdown_view/./loaders.py)

```python
# loaders.py
from django.conf import settings
from django.core.exceptions import SuspiciousFileOperation
from django.template import Origin
~~from django.template.loaders.filesystem import Loader as FilesystemLoader
from django.template.utils import get_app_template_dirs
from django.utils._os import safe_join

from markdown_view.constants import DEFAULT_MARKDOWN_VIEW_LOADER_TEMPLATES_DIR


class MarkdownLoader(FilesystemLoader):

    def get_dirs(self):
        base_dir = getattr(
            settings,
            "MARKDOWN_VIEW_BASE_DIR",
            getattr(
                settings,
                "BASE_DIR",
                None)
        )
        dirs = [*get_app_template_dirs(
            getattr(
                settings,
                "MARKDOWN_VIEW_LOADER_TEMPLATES_DIR",
                DEFAULT_MARKDOWN_VIEW_LOADER_TEMPLATES_DIR
            )
        )]


## ... source file continues with no further Loader examples...

```

