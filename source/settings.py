# -*- coding: utf-8 -*-

AUTHOR = u'Matt Makai'
SITENAME = u'Matt Makai'
SITEURL = 'http://www.fullstackpython.com'
TIMEZONE = 'America/New_York'

GITHUB_URL = 'https://github.com/makaimc/fullstackpython.com'
DISQUS_SITENAME = 'makaimc'
PDF_GENERATOR = False

DIRECT_TEMPLATES = ('index', 'sitemap', 'table-of-contents', 'email',
                    'blog', 'all')

ARTICLE_SAVE_AS = 'blog/{slug}.html'

SITEMAP_SAVE_AS = 'sitemap.xml'

BYLINE = '&copy; 2016 Matt Makai. All Rights Reserved.'
LINKS = ()

MARKUP = ('rst', 'markdown',)

SOCIAL = (
    ('Email', 'mailto:matthew.makai@gmail.com'),
    ('GitHub', 'https://github.com/makaimc'),
    ('Twitter', 'http://twitter.com/mattmakai'),
)

PROJECTS = ()

JINJA_EXTENSIONS = (['jinja2.ext.autoescape',])

