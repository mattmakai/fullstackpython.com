title: Markdown
category: page
slug: markdown
sortorder: 0323
toc: False
sidebartitle: Markdown
meta: Markdown is a type of markup language often used to document Python projects. Learn more about Markdown on Full Stack Python.


Markdown is a common markup language frequently used by developers to write 
Python project documention.

<img src="/img/logos/markdown.png" width="100%" alt="Unofficial Markdown logo.">


## Markdown's origin
Markdown was originally 
[developed by John Gruber](https://daringfireball.net/projects/markdown/)
in 2004. The markup language's lightweight design helped it gain rapid
adoption by software developers and designers. The format's simplicity also
makes it easier to write parsers to convert the structured syntax into
other formats such as HTML and JSON.


## Markdown resources
Markdown does not have an extensive set of strict rules like some other
text formats so you should be able to read up on the basics with these
articles then write a few practice documents to be comfortable with it.
The following resources are really helpful when you are getting started
or need a quick reference on a less commonly-used feature such as tables
or block quotes.

* [Say yes to Markdown, no to MS Word](https://medium.com/@drodil/say-yes-to-markdown-no-to-ms-word-be4692e7a8cd)
  provides a really awesome overview of why Markdown is a more usable file
  format than Microsoft Word and similar proprietary file types. The article
  also has a good list of useful Markdown-related tools such as a 
  [Markdown-to-PDF converter](https://github.com/alanshaw/markdown-pdf)
  (a NodeJS package but easy enough to use with a basic development 
  environment).

* [Markdown syntax](https://daringfireball.net/projects/markdown/syntax)
  is the defacto standard and wonderful reading for both initial learning 
  and random reference.

* [Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
  is a quick reference that is a shortened version of the above Markdown
  syntax page.

* [Markdown parsers in Python](http://lepture.com/en/2014/markdown-parsers-in-python)
  reviews many of the most common Python Markdown parser implementations
  to give insight into the advantages and disadvantages of each one.

* [reStructuredText vs Markdown for documentation](http://zverovich.net/2016/06/16/rst-vs-markdown.html)
  brings up some really good points about the downsides to Markdown's
  simplicity. First, a lot of documentation needs more complex output that
  is not possible with vanilla Markdown so you need to drop into plain old
  HTML, which defeats the purpose of using a markup language. Second, some
  of the syntax around inserting blank lines by adding spaces at the end
  of lines is confusing if someone is using a 
  [text editor or development environment](/text-editors-ides.html) that
  is not configured to show blank spaces. Worse yet, if your editor is set to
  remove blank spaces at the end of lines, which is fairly common among
  developers, then you can mistakenly break the formatting intended by 
  the original author. Overall this is a good piece to read for a balanced
  view of Markdown and the reasons it provides are one reason why I use
  both Markdown and reStructuredText depending on the project.
  
* The Python Package Index (PyPI) 
  [supports Markdown as of 2018](https://dustingram.com/articles/2018/03/16/markdown-descriptions-on-pypi)
  although there are still some tweaks being made to the flavors that can be
  used such as GitHub-flavored Markdown.

* [PowerShell and Markdown](https://ephos.github.io/posts/2018-8-1-PowerShell-Markdown)
  shows how to work with Markdown in [PowerShell](/powershell.html) 
  including customizing colors and listing some quirks you may need to get 
  around.

* [reStructuredText vs. Markdown for technical documentation](https://eli.thegreenplace.net/2017/restructuredtext-vs-markdown-for-technical-documentation/)
  compares Markdown and reStructuredText specifically for documenting
  software and explains where each one has advantages.

* [Reach for Markdown, not LaTeX](https://blog.jez.io/reach-for-markdown/)
  examines the virtues of using straight Markdown along with tools such
  as [pandoc](https://pandoc.org/) to convert from one file format to 
  another, including how to use Markdown for presentations and not just 
  regular documentation.

* [Markdown page](https://github.com/oscarmorrison/md-page) is a JavaScript
  file that makes it easy to render plain old Markdown as a webpage.
