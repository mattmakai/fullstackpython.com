title: django.core.exceptions SuspiciousFileOperation Example Code
category: page
slug: django-core-exceptions-suspiciousfileoperation-examples
sortorder: 500011106
toc: False
sidebartitle: django.core.exceptions SuspiciousFileOperation
meta: Python example code for the SuspiciousFileOperation class from the django.core.exceptions module of the Django project.


SuspiciousFileOperation is a class within the django.core.exceptions module of the Django project.


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
~~from django.core.exceptions import SuspiciousFileOperation
from django.template import Origin
from django.template.loaders.filesystem import Loader as FilesystemLoader
from django.template.utils import get_app_template_dirs
from django.utils._os import safe_join


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
        dirs = [*get_app_template_dirs('')]
        if base_dir:
            dirs.extend([base_dir])
        return dirs

    def get_template_sources(self, template_name):
        if template_name.endswith('.md'):
            template_split = template_name.split("/")
            template_split.reverse()
            template_app_dir = template_split.pop()
            template_split.reverse()
            for template_dir in self.get_dirs():
                if template_dir.endswith(template_app_dir):
                    try:
                        name = safe_join(template_dir, *template_split)
~~                    except SuspiciousFileOperation:
                        continue

                    yield Origin(
                        name=name,
                        template_name=template_name,
                        loader=self,
                    )



## ... source file continues with no further SuspiciousFileOperation examples...

```

