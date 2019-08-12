title: Minification
category: page
slug: minification
sortorder: 0419
toc: False
sidebartitle: Minification
meta: Minification reduces the size of web assets to make pages and applications load quicker.


Minification is the process of reducing the size of 
[static content assets](/static-content.html) that need to be transferred 
from a [web server](/web-servers.html) to the web browser client. The goal
of minification is to make webpages and web applications load faster, 
*without changing how the assets are ultimately used after being downloaded*.

[Cascading Style Sheet (CSS) files](/cascading-style-sheets.html), 
[JavaScript](/javascript.html) and even HTML can be minified. The techniques 
to minify an HTML file differ from a CSS file because the file's contents
and syntax are different.


## CSS Minification example
Let's say your web application has a CSS file with the following four lines
to add some padding around every element with the `pad-me` class:

```
.pad-me { padding-top: 10px;
          padding-right: 5px;
          padding-left: 5px;
          padding-bottom: 10px; }
```

That example has 122 characters. A CSS minifier would take the above four 
lines and convert them to the following single line:

```
.pad-me{padding:10px 5px 5px 10px}
```

The result would have only a single line with 35 characters, that's 87 less 
characters that would need to be sent from the web server to the web browser!
The minification process reduced the single CSS class by 71% but kept the exact
same result when the web browser applies `pad-me` to all elements with that
class.

The file size savings can be a major benefit when applied across hundreds or
thousands of lines in a typical CSS file. When you also multiply that savings 
across every client that downloads the CSS from your web server or CDN it becomes
clear that minification is a powerful way to improve the efficiency of your 
production web application.


### CSS minification resources
* [CSS minifier](https://cssminifier.com/) is an online form to copy and paste
  CSS then retrieve the minified results on the same page.


### JavaScript minification resources
* [JavaScript minifier](https://javascript-minifier.com/) is similar to the
  above CSS minifier but works with JavaScript syntax.


