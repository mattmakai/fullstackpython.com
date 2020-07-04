title: SciPy and NumPy
category: page
slug: scipy-numpy
sortorder: 0317
toc: False
sidebartitle: SciPy & NumPy
meta: SciPy is an umbrella project for many open source data analysis libraries such as NumPy, pandas and Matplotlib.


[SciPy](https://www.scipy.org/) is a collection of open source code libraries 
for math, science and engineering. [NumPy](https://www.numpy.org/),
[Matplotlib](/matplotlib.html) and [pandas](/pandas.html) are libraries
that fall under the SciPy project umbrella.

<img src="/img/logos/scipy.png" width="100%" alt="SciPy project logo.">

[NumPy](http://www.numpy.org/) ([source code](https://github.com/numpy/numpy))
is a Python code library that adds scientific computing capabilities such as
N-dimensional array objects, FORTRAN and C++ code integration, linear algebra
and Fourier transformations. NumPy serves as a required dependency for many
other scientific computing packages such as [pandas](/pandas.html).

<img src="/img/logos/numpy.jpg" width="100%" alt="NumPy logo.">

[Blaze](http://blaze.pydata.org/) is a similar, but separate, ecosystem 
with additional tools for wrangling, cleaning, processing and analyzing data.


### SciPy resources
Take a look at the pages on [Matplotlib](/matplotlib.html) and 
[pandas](/pandas.html) for tutorials specific to those projects. The 
following resources are broader walkthroughs for the SciPy ecosystem:

* [SciPy Lecture notes](http://www.scipy-lectures.org/) goes into the 
  overall Python scientific computing ecosystem and how to use it.

* The [SciPy Cookbook](http://scipy-cookbook.readthedocs.io/) contains
  instructions for various SciPy packages that were previously hosted
  on the SciPy wiki.

* [Robots and Generative Art and Python, oh my!](https://www.generativehut.com/post/robots-and-generative-art-and-python-oh-my)
  uses Scipy, Numpy, and [Matplotlib](/matplotlib.html) to generate
  some nice looking art that can even be written to paper using a
  plotter. This is a very cool example project that ties together
  the scientific world and the art world.

* [Lectures in Quantitative Economics: SciPy](https://lectures.quantecon.org/py/scipy.html)
  provides a good overview of SciPy compared to the specific NumPy
  project, as well as explanations for the wrappers SciPy provides 
  over lower-level FORTRAN libraries.

* [A plea for stability in the SciPy ecosystem](http://blog.khinsen.net/posts/2017/11/16/a-plea-for-stability-in-the-scipy-ecosystem/)
  presents concerns from one scientist's perspective about how fast the 
  Python programming ecosystem changes and that code can become backwards 
  incompatible in only a few years. The issue is that many science projects
  last decades and therefore cannot follow the rate of change as easily
  as typical software development projects.


### NumPy resources
* [From Python to NumPy](http://www.labri.fr/perso/nrougier/from-python-to-numpy/)
  is an awesome resource that shows how to use your basic
  Python knowledge to learn how to do vectorization with NumPy.

* [The ultimate beginner's guide to NumPy](https://towardsdatascience.com/the-ultimate-beginners-guide-to-numpy-f5a2f99aef54)
  explains how to install and import NumPy, then digs into using arrays for
  computation and how to perform operations that get the results you need
  for your data analysis.

* [Math to Code](https://mathtocode.com/) provides an interactive
  tutorial to learn how to implement math in NumPy.

* [101 NumPy Exercises for Data Analysis](https://www.machinelearningplus.com/python/101-numpy-exercises-python/)

* [NumPy: creating and manipulating numerical data](http://www.scipy-lectures.org/intro/numpy/index.html)

* [Python NumPy Array Tutorial](https://www.datacamp.com/community/tutorials/python-numpy-tutorial)
  is a starter tutorial specifically focused on using and working
  with NumPy's powerful arrays. 

* [Beyond Numpy Arrays in Python](https://matthewrocklin.com/blog//work/2018/05/27/beyond-numpy)
  is a predecessor to a 
  [Numpy Enhancement Proposal](https://github.com/numpy/numpy/pull/11189) 
  that recommends how to prepare the scientific computing ecosystme for 
  GPU, distributed and sparse arrays.

* [Probability distribution explorer](http://bois.caltech.edu/distribution_explorer/)
  contains graphs for understanding how different probabilities look
  when plotted. There is also code for implementing the visuals in NumPy
  and SciPy.


### Example NumPy code
* [SmoothLife](https://github.com/duckythescientist/SmoothLife) is an 
  implementation of [Conway's Game of Life](https://bitstorm.org/gameoflife/)
  using NumPy. The project uses a continuous space rather than the 
  traditional discrete board.

* [Advanced Numpy Techniques](https://nbviewer.jupyter.org/github/vlad17/np-learn/blob/master/presentation.ipynb?flush_cache=true)
  is a [Jupyter Notebook](/jupyter-notebook.html) with code on 
  beyond-the-basics NumPy features.
