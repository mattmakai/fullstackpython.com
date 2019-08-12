title: Markup Languages
category: page
slug: markup-languages
sortorder: 0322
toc: False
sidebartitle: Markup Languages
meta: Markup languages allow annotations on text documents where the syntax is different and parsable from the plain text.


Markup languages provide pre-defined, parsable syntax within text documents 
that is used for annotations. For example, within a [Markdown](/markdown.html)
document, the syntax 
`[this is a link to Full Stack Python](https://www.fullstackpython.com)`
indicates the text "this is a link to Full Stack Python" should be annotated
with a link to "https://www.fullstackpython.com/" when run through a Markdown 
parser and then transformed into HTML output.


### Markup language resources
* [Reach for Markdown, not LaTeX](https://blog.jez.io/reach-for-markdown/)
  argues for the simplicity of Markdown versus the steep learning curve and
  less easily adopted LaTeX for creating documents.

* [Yet Another Markup LOL?](https://urcomputeringpal.com/2018/09/09/yaml)
  explains the virtues and the significant downsides of tooling for the
  [YAML markup language](http://yaml.org/). Mistakes in configuration files 
  that use YAML or any markup language often fly past 
  [testing](/testing.html) and 
  [continuous integration](/continuous-integration.html) services that
  catch errors in regular code. The post also introduces a couple of tools
  that can help with specific YAML issues, especially when using Kubernetes.
