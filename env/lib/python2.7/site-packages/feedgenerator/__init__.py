"""
Syndication feed generation library -- used for generating RSS, etc.

Sample usage:

>>> import feedgenerator
>>> feed = feedgenerator.Rss201rev2Feed(
...     title="Poynter E-Media Tidbits",
...     link="http://www.poynter.org/column.asp?id=31",
...     description="A group Weblog by the sharpest minds in online media/journalism/publishing.",
...     language="en",
... )
>>> feed.add_item(
...     title="Hello",
...     link="http://www.holovaty.com/test/",
...     description="Testing."
... )
>>> with open('test.rss', 'w') as fp:
...     feed.write(fp, 'utf-8')

For definitions of the different versions of RSS, see:
http://web.archive.org/web/20110718035220/http://diveintomark.org/archives/2004/02/04/incompatible-rss
"""
from .django.utils.feedgenerator import *
