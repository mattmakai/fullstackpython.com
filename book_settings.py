# -*- coding: utf-8 -*-
AUTHOR = u'Matthew Makai'
SITENAME = u'Full Stack Python'
SITEURL = 'https://www.fullstackpython.com'
TIMEZONE = 'America/New_York'

GITHUB_URL = 'https://github.com/mattmakai/fullstackpython.com'
PDF_GENERATOR = False
DIRECT_TEMPLATES = ('pdf-book', 'epub-book')
PLUGINS = ['plugins.pelican-toc',]

ARTICLE_SAVE_AS = 'blog/{slug}.html'
SITEMAP_SAVE_AS = 'sitemap.xml'

FEED_DOMAIN = 'https://www.fullstackpython.com'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = ()

MARKUP = ('rst', 'markdown',)

SOCIAL = (
    ('Email', 'mailto:matthew.makai@gmail.com'),
    ('GitHub', 'https://github.com/mattmakai'),
    ('Twitter', 'http://twitter.com/mattmakai'),
)

PROJECTS = ()

JINJA_EXTENSIONS = (['jinja2.ext.autoescape',])
