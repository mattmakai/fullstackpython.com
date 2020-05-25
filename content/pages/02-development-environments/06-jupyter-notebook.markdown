title: Jupyter Notebook
category: page
slug: jupyter-notebook
sortorder: 0206
toc: False
sidebartitle: Jupyter Notebook
meta: Jupyter Notebook, formerly named iPython Notebook, is a powerful Python code execution environment often used for data analysis.


[Jupyter Notebook](http://jupyter.org/) 
([open source code](https://github.com/jupyter/notebook)), which began 
as the iPython Notebook project, is a 
[development environment](/development-environments.html) for writing
and executing Python code. Jupyter Notebook is often used for exploratory 
[data analysis](/data-analysis.html) and visualization. 

<a href="http://jupyter.org/" style="border:none"><img src="/img/logos/jupyter.png" width="100%" alt="Jupyter Notebook project logo." class="shot"></a>

Project Jupyter is the top-level project name for all of the subprojects under 
development, which includes Jupyter Notebook. Jupyter Notebooks can also run 
code for other programming languages such as [Julia](https://julialang.org/) and 
[R](https://www.r-project.org/).


### How does Jupyter Notebook work?
The key piece of Jupyter Notebook infrastructure is a web application that
runs locally for creating and sharing documents that contain embedded code and 
execution results.

<img src="/img/visuals/jupyter-screenshot.jpg" width="100%" alt="Screenshot of Jupyter Notebook running in the browser and server in terminal." class="shot">

<div class="well see-also">Jupyter Notebook is an implementation of the <a href="/text-editors-ides.html">text editors and IDEs</a> concept. Learn how these parts fit together in the <a href="/development-environments.html">development environments</a> chapter or view <a href="/table-of-contents.html">all topics</a>.</div>


### How are IPython Notebook and Jupyter Notebook related?
IPython Notebook was the original project that proved that there was great
demand among data scientists and programmers for an interactive, repeatable
development environment. Jupyter Notebook became the new official name for the
overall project during 
[The Big Split](https://blog.jupyter.org/the-big-split-9d7b88a031a7)
after the IPython Notebook project matured into distinct submodules such as the 
interactive shell, notebook document format and user interface widgets tools.
However, the IPython Notebook name sticks around as the Python backend for
Jupyter Notebook which is seriously confusing if you are searching the internet
and come across both current and old articles that use all of these names
interchangeably.


### Jupyter Notebook beginner tutorials
Jupyter Notebook's powerful analysis and visualization environment can be 
intimidating even for experienced developers that are new to the tool. The
following tutorials will explain the basics so you can quickly figure out
your own productive workflow.

* [Jupyter Notebook for Beginners: A Tutorial](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)
  is a great place to start if you have never before used the tool.
  The guide covers installation, terminology, the user interface and
  how to publish your notebooks to the web. Screenshots walk you
  through some of the more confusing bits as you are getting up
  and running.

* [First Python Notebook](http://www.firstpythonnotebook.org/) is a free
  guide on analyzing data with Python and Jupyter Notebook. It covers
  many "Hello, World!"-style examples in both data analysis topics and
  more general software development areas like Git, GitHub and Markdown.

* [IPython Or Jupyter?](https://www.datacamp.com/community/blog/ipython-jupyter)
  covers the evolution of the Notebook concept from its origins in the IPython
  Notebook implementation through the 
  [IPython and Jupyter split](https://blog.jupyter.org/the-big-split-9d7b88a031a7)
  that happened in 2015 that separated IPython Notebook into logical subprojects.
  The post kicks off with some fun lesser-known historical context on other
  data science notebook projects such as MATLAB and Mathematica to set the stage 
  for IPython and Jupyter's creation.

* [How to use Jupyter Notebooks in 2020 (Part 1: The data science landscape)](https://ljvmiranda921.github.io/notebook/2020/03/06/jupyter-notebooks-in-2020/)
  is a high-level overview post that starts a series on Jupyter Notebooks.
  This first post covers why a tool like Jupyter Notebook is needed in
  the broader landscape of data science.
  [Part 2](https://ljvmiranda921.github.io/notebook/2020/03/16/jupyter-notebooks-in-2020-part-2/)
  examines the growth of the Jupyter ecosystem and the jump from exploratory
  analysis notebooks to production notebooks.

* [Jupyter Notebook Best Practices](https://levelup.gitconnected.com/jupyter-notebook-best-practices-fc326eb5cd22)
  contains tips for beginners such as learning shortcuts and properly 
  documenting the analysis you work on.

* [How to Version Control Jupyter Notebooks](https://nextjournal.com/schmudde/how-to-version-control-jupyter)
  explains how Jupyter Notebooks are stored in JSON, the issues with that
  format for [source control](/source-control.html) and how to get
  around the problem.


### Example Notebooks
Example Notebooks are easy to fire up and see how other people are working.
These resources are highly recommended after you read a couple of tutorials
and play around with the tool.

* [Peter Norvig's collection of Jupyter Notebooks](http://norvig.com/ipython/README.html)
  is a an incredible resource for example projects.

* [Building and Exploring a Map of Reddit with Python](https://lmcinnes.github.io/subreddit_mapping/)
  is a detailed notebook that digs into public Reddit data while explaining
  the "what" and "why" along the way.

* This 
  [gallery of interesting Jupyter Notebooks](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks)
  provides many great examples across numerous programming languages.

* [jupyter-samples](https://github.com/ibm-et/jupyter-samples) 
  contains an extensive set of notebooks along with public data
  sets that can be used for analysis.

* [learn-python3](https://github.com/jerry-git/learn-python3) is geared
  towards Python beginners who want to learn basic syntax and standard
  library features such as about string manipulation, functions and 
  iteration.


### Intermediate to advanced Jupyter Notebook tutorials
Once you get the hang of the basics there are a slew of ways to connect
your notebooks to third party [APIs](/application-programming-interfaces.html)
and use more advanced Python libraries with your code. These walkthroughs
cover a range of topics from niche tricks to common but advanced situations
like advanced interactive visualizations.

* [Advanced Jupyter Notebook Tricks — Part I](https://blog.dominodatalab.com/lesser-known-ways-of-using-notebooks/)
  and 
  [Building Interactive Dashboards with Jupyter (Part 2)](https://blog.dominodatalab.com/interactive-dashboards-in-jupyter/)
  have a ton more details on ways to set up Jupyter Notebooks as dashboards
  and export results to other formats.

* [Creating Interactive Dashboards from Jupyter Notebooks](https://pbpython.com/interactive-dashboards.html)
  shows how to use public Reddit data for a data analysis project as
  an example to display in dashboards running in a Jupyter Notebook.

* [mapboxgl-jupyter](https://github.com/mapbox/mapboxgl-jupyter) library along
  with the 
  [quickstart](https://github.com/mapbox/mapboxgl-jupyter/blob/master/docs/viz.md)
  show you how to visualize geospatial data within your notebooks.

* [Reproducible Data Analysis in Jupyter](https://jakevdp.github.io/blog/2017/03/03/reproducible-data-analysis-in-jupyter/)
  is a fantastic series of videos by 
  [Jake Vanderplas](https://github.com/jakevdp) that shows how to move your
  code from the interactive Jupyter environment into packaged, tested Python
  code that is suitable for [deployment](/deployment.html) to a production 
  environment.

* [28 Jupyter Notebook tips, tricks and shortcuts](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)
  explains many of the lesser-known keyboard shortcuts and mechanisms
  to output settings.

* [Boost Your Jupyter Notebook Productivity](https://towardsdatascience.com/jupyter-notebook-hints-1f26b08429ad)
  covers hotkeys, data plotting, shell commands, timing and other topics
  you will eventually want to handle within your notebooks as you get 
  comfortable in the environment.

* [Making Publication Ready Python Notebooks](http://blog.juliusschulz.de/blog/ultimate-ipython-notebook)
  explores the plugins that the author uses when creating and exporting
  reports from Jupyter.

* PyData has an extensive
  [list of Jupyter Notebook talks](https://www.youtube.com/user/PyDataTV/search?query=jupyter)
  from past events. 
  [JupyterCon](https://www.youtube.com/playlist?list=PL055Epbe6d5aP6Ru42r7hk68GTSaclYgi)
  has a similarly extensive talks list that is also worth watching.

* [Integrate Google Sheets and Jupyter Notebooks](http://www.countingcalculi.com/explanations/google_sheets_and_jupyter_notebooks/)
  answers the common question of how to extract data directly from a Google
  Sheet and start working with it in your Jupyter Notebook. The screenshots 
  help a lot to make sure you avoid getting lost in the sea of menus along
  the way.

* [Analyzing Cryptocurrency Markets using Python](https://blog.patricktriest.com/analyzing-cryptocurrencies-python/)
  uses a freely-available Bitcoin API as a source data set 
  for a data analysis and visualization project in Jupyter.

* [nbdev: use Jupyter Notebooks for everything](https://www.fast.ai/2019/12/02/nbdev/)
  shows how to use the [nbdev](https://nbdev.fast.ai/) tool to create a literate
  programming environment within a Jupyter Notebook so that you can do
  all of your debugging and refactoring there rather than switching between 
  a more traditional IDE and Jupyter.

* [Running Jupyter Notebooks on GPU on AWS: a starter guide](https://blog.keras.io/running-jupyter-notebooks-on-gpu-on-aws-a-starter-guide.html)
  explains how to run notebooks on Amazon Web Services using a 
  graphics-processing unit (video card), which for some machine learning
  situations can result in significantly faster execution times.

* [Python & Big Data: Airflow & Jupyter Notebook with Hadoop 3, Spark & Presto](http://tech.marksblogg.com/python-big-data-airflow-jupyter-notebook-hadoop-3-hive-presto.html)
  walks through a data pipeline that combines several commonly-used
  [data analysis](/data-analysis.html) tools with a Jupyter Notebook.

* [Ansible-jupyter-kernel](https://github.com/ansible/ansible-jupyter-kernel)
  is a kernel that allows you to run [Ansible](/ansible.html) tasks and 
  playbooks from within your Jupyter environment.

* [Jupyter Notebooks in the IDE](https://towardsdatascience.com/jupyter-notebooks-in-the-ide-visual-studio-code-versus-pycharm-5e72218eb3e8)
  explains how to use Jupyter files in Visual Studio Code or 
  [PyCharm](/pycharm.html) with Jupytext, which defines the
  pairing information and notebook kernel.

* [The Notebook Wars](https://yihui.name/en/2018/09/notebook-war/) is not a
  tutorial but instead points to the weaknesses that become apparent when
  using Jupyter and the current generation of notebook projects. The
  article raises many good points about barriers to entry although you
  could also argue some of these issues have been mitigated by Jupyter, just
  not as much as some people would like to see. Overall there is a lot to
  enjoy reading here and reflect on so that the community can continue making
  Jupyter a fantastic environment for development.

* [Creating Presentations with Jupyter Notebook](http://www.blog.pythonlibrary.org/2018/09/25/creating-presentations-with-jupyter-notebook/)
  shows how to make slides out of your cells so you can present your
  work like a traditional presentation.

* The number of open source Jupyter Notebooks on GitHub is exploding and
  [this post attempts to estimate the growth](https://kyso.io/KyleOS/nbestimate)
  using Python, [pandas](/pandas.html) and a scraped data set.

* [Reproducible Jupyter Notebooks with Docker](https://blog.reviewnb.com/reproducible-notebooks/)
  explains when to use [Docker](/docker.html) in combination with Jupyter
  Notebooks as well as the instructions for creating a dockerfile to build
  your images.

* [JupyterLab GPU Dashboards](https://github.com/rapidsai/jupyterlab-nvdashboard)
  contains a [Bokeh](/bokeh.html) server and TypeScript code for displaying
  GPU utilization charts.
