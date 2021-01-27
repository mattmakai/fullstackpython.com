title: django.template.defaultfilters safe Example Code
category: page
slug: django-template-defaultfilters-safe-examples
sortorder: 500011385
toc: False
sidebartitle: django.template.defaultfilters safe
meta: Python example code that shows how to use the safe callable from the django.template.defaultfilters module of the Django project.


`safe` is a callable within the `django.template.defaultfilters` module of the Django project.

<a href="/django-template-defaultfilters-escape-examples.html">escape</a>,
<a href="/django-template-defaultfilters-filesizeformat-examples.html">filesizeformat</a>,
<a href="/django-template-defaultfilters-slugify-examples.html">slugify</a>,
<a href="/django-template-defaultfilters-striptags-examples.html">striptags</a>,
<a href="/django-template-defaultfilters-title-examples.html">title</a>,
and <a href="/django-template-defaultfilters-truncatechars-examples.html">truncatechars</a>
are several other callables with code examples from the same `django.template.defaultfilters` package.

## Example 1 from django-floppyforms
[django-floppyforms](https://github.com/jazzband/django-floppyforms)
([project documentation](https://django-floppyforms.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-floppyforms/))
is a [Django](/django.html) code library for better control
over rendering HTML forms in your [templates](/template-engines.html).

The django-floppyforms code is provided as
[open source](https://github.com/jazzband/django-floppyforms/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-floppyforms / floppyforms / gis / widgets.py**](https://github.com/jazzband/django-floppyforms/blob/master/floppyforms/gis/widgets.py)

```python
# widgets.py
from django.conf import settings
~~from django.template.defaultfilters import safe
from django.utils import translation

import floppyforms as forms

from urllib.parse import urlencode

try:
    from django.contrib.gis import gdal, geos
except ImportError:


__all__ = ('GeometryWidget', 'GeometryCollectionWidget',
           'PointWidget', 'MultiPointWidget',
           'LineStringWidget', 'MultiLineStringWidget',
           'PolygonWidget', 'MultiPolygonWidget',
           'BaseGeometryWidget', 'BaseMetacartaWidget',
           'BaseOsmWidget', 'BaseGMapWidget')


class BaseGeometryWidget(forms.Textarea):
    display_wkt = False
    map_width = 600
    map_height = 400
    map_srid = 4326


## ... source file abbreviated to get to safe examples ...


    map_srid = 3857
    template_name = 'floppyforms/gis/osm.html'

    class Media:
        js = (
            'floppyforms/openlayers/OpenLayers.js',
            'https://www.openstreetmap.org/openlayers/OpenStreetMap.js',
            'floppyforms/js/MapWidget.js',
        )


class BaseGMapWidget(BaseGeometryWidget):
    map_srid = 3857
    template_name = 'floppyforms/gis/google.html'
    google_maps_api_key = None

    @property
    def media(self):
        qs_dict = {'v': '3'}
        if self.google_maps_api_key is not None:
            qs_dict['key'] = self.google_maps_api_key

        js = (
            'floppyforms/openlayers/OpenLayers.js',
            'floppyforms/js/MapWidget.js',
~~            safe('https://maps.google.com/maps/api/js?' + urlencode(qs_dict))
        )
        return forms.Media(js=js)



## ... source file continues with no further safe examples...

```

