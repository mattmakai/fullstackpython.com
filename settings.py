# -*- coding: utf-8 -*-

AUTHOR = u'Matt Makai'
SITENAME = u'Full Stack Python'
SITEURL = 'https://www.fullstackpython.com'
TIMEZONE = 'America/New_York'
GITHUB_URL = 'https://github.com/mattmakai/fullstackpython.com'
PDF_GENERATOR = False
DIRECT_TEMPLATES = ('index', 'sitemap', 'table-of-contents', 'email',
                    'blog', 'example', 'all',) #'pdf-book', 'epub-book')

ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_URL = 'blog/{slug}.html'
SITEMAP_SAVE_AS = 'sitemap.xml'
FEED_RSS = 'feed'
LINKS = ()
MARKUP = ('rst', 'markdown',)
SOCIAL = (
    ('Email', 'mailto:matthew.makai@gmail.com'),
    ('GitHub', 'https://github.com/mattmakai'),
    ('Twitter', 'http://twitter.com/mattmakai'),
)
PROJECTS = ()
JINJA_EXTENSIONS = (['jinja2.ext.autoescape',])
