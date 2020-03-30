title: Learning pandas by Exploring COVID-19 Data
slug: learn-pandas-basic-commands-explore-covid-19-data
meta: Use the pandas data analysis tool to explore the free COVID-19 data set provided by the European Centre for Disease Prevention and Control.
category: post
date: 2020-03-28
modified: 2020-03-28
newsletter: False
headerimage: /img/200328-covid-19-pandas/header.jpg
headeralt: pandas logo. Copyright the PyData Foundation.


The 
[European Centre for Disease Prevention and Control](https://www.ecdc.europa.eu/en) 
provides 
[daily-updated worldwide COVID-19 data](https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide)
that is easy to download in JSON, CSV or XML formats. In this tutorial,
we will use the [pandas](/pandas.html) data analysis tool on the
comma-separated values (CSV) data to learn some of the basic pandas
commands and explore what is contained within the data set.


## Configuring our development environment
Make sure you have Python 3 installed. As of right now, 
[Python 3.8.2](https://www.python.org/downloads/) is the latest.

During this tutorial we're also going to use 
[pandas](https://pandas.pydata.org/).

Install it now into a new virtual environment with the following
commands:

```bash
python -m venv covidpandas
source covidpandas/bin/activate

pip install pandas
```

We are now ready to get the COVID-19 data and start analyzing it with
pandas.


## Obtaining the COVID-19 data
Go to the 
[download today’s data on the geographic distribution of COVID-19 cases worldwide](https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide) 
page in your web browser. It should look something like the following
screenshot. 

<img src="/img/200328-covid-19-pandas/covid-19-data-download.png" width="100%" class="shot rnd outl" alt="Download the CSV version of the COVID-19 data.">

There should be a link to download the
data in CSV format, but the organization has changed the page layout
several times in the past few weeks, which makes it difficult to find
formats other than Excel (XLSX). If you have trouble obtaining the
CSV version, just download 
[this one from GitHub](https://raw.githubusercontent.com/fullstackpython/blog-code-examples/master/pandas-covid-19/covid-19-cases-march-28-2020.csv)
which is pegged to a copy downloaded on March 28th, 2020.



## Importing the CSV into pandas
We have the data in a CSV now we need to import it into a pandas
DataFrame.

Start by running the Python REPL:

```bash
python

>>>
```

The REPL is ready to go, now we need to import pandas so we can read
the data we downloaded.

```python
from pandas import read_csv

df = read_csv("covid-19-cases-march-28-2020.csv")
```

Don't worry if you get an error like
`UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe7...`. 
Run this command instead which explicitly sets the file encoding 
so pandas can properly read the CSV.

```python
# make sure the file name of the csv matches your file's name!
df = read_csv("covid-19-cases-march-28-2020.csv", encoding="ISO-8859-1")
```

We now have our data loaded into a 
[pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)
and can start running code to poke and prod and what's inside the
data set.


## Running pandas commands
Let's first take a peek at what a sample of the data looks like. I
typically run the `head` and `tail` functions when I open something
up to find out what are contained in the first five and last five rows.

```python
df.head()
```

You should see six lines of output: one as the columns header and the
first five rows of data from the CSV:

```
      dateRep  day  month  year  cases  deaths countriesAndTerritories geoId countryterritoryCode  popData2018
0  28/03/2020   28      3  2020     16       1             Afghanistan    AF                  AFG   37172386.0
1  27/03/2020   27      3  2020      0       0             Afghanistan    AF                  AFG   37172386.0
2  26/03/2020   26      3  2020     33       0             Afghanistan    AF                  AFG   37172386.0
3  25/03/2020   25      3  2020      2       0             Afghanistan    AF                  AFG   37172386.0
4  24/03/2020   24      3  2020      6       1             Afghanistan    AF                  AFG   37172386.0
```

The `tail` function looks at the last five rows in a DataFrame.

```
df.tail()
```

`tail` output will look something like this:

```
         dateRep  day  month  year  cases  deaths countriesAndTerritories geoId countryterritoryCode  popData2018
7315  25/03/2020   25      3  2020      0       0                Zimbabwe    ZW                  ZWE   14439018.0
7316  24/03/2020   24      3  2020      0       1                Zimbabwe    ZW                  ZWE   14439018.0
7317  23/03/2020   23      3  2020      0       0                Zimbabwe    ZW                  ZWE   14439018.0
7318  22/03/2020   22      3  2020      1       0                Zimbabwe    ZW                  ZWE   14439018.0
7319  21/03/2020   21      3  2020      1       0                Zimbabwe    ZW                  ZWE   14439018.0
```

Note that you can also pass an integer into `head` or `tail` like
`df.head(10)` to get the first or last **n** number of rows.

It looks like based on the `tail` function we have around 7320 rows of
data (since the first row is 0 indexed). We can confirm how much
data is in each column with the `count` function.

```
df.count()
```

`count`'s output will look like:

```
dateRep                    7320
day                        7320
month                      7320
year                       7320
cases                      7320
deaths                     7320
countriesAndTerritories    7320
geoId                      7306
countryterritoryCode       7254
popData2018                7311
dtype: int64
```

What if we want to look at one of those columns and find, for example,
the highest value of cases?

```
df.cases.max()
```

In this data set we get 18695 as the output. What about looking at
standard statistical measures across all columns? That's where the
`describe` function comes in handy.

```
df.describe()
```

`describe` presents standard statistical measures such as min, max,
median and mean for everything in your data set. In this case we
receive as output:

```
               day        month         year         cases       deaths   popData2018
count  7320.000000  7320.000000  7320.000000   7320.000000  7320.000000  7.311000e+03
mean     16.828142     2.249454  2019.990847     80.870355     3.687158  7.130483e+07
std       8.322981     1.256463     0.095239    608.270244    35.327689  2.140624e+08
min       1.000000     1.000000  2019.000000     -9.000000     0.000000  1.000000e+03
25%      10.000000     1.000000  2020.000000      0.000000     0.000000  4.137309e+06
50%      18.000000     2.000000  2020.000000      0.000000     0.000000  1.072767e+07
75%      24.000000     3.000000  2020.000000      5.000000     0.000000  5.139301e+07
max      31.000000    12.000000  2020.000000  18695.000000   971.000000  1.392730e+09
```

How about a quick view into whether or not columns' data are correlated
with each other? The `corr` function is what we need.

```
df.corr()
```

For our data set, `corr` outputs:

```
                  day     month      year     cases    deaths  popData2018
day          1.000000  0.203006 -0.163665  0.063629  0.060075    -0.040677
month        0.203006  1.000000 -0.745912  0.062494  0.052707    -0.039131
year        -0.163665 -0.745912  1.000000  0.012715  0.010032    -0.006294
cases        0.063629  0.062494  0.012715  1.000000  0.716968     0.136580
deaths       0.060075  0.052707  0.010032  0.716968  1.000000     0.082229
popData2018 -0.040677 -0.039131 -0.006294  0.136580  0.082229     1.000000
```

Not surprisingly, we see 1.000000 correlation between a column and itself.
We'd have to worry if we didn't see that result! For other columns it may
not make sense to look at their correlation. This is where you need to 
think about the data. There is often correlation between completely unrelated
columns just because the data is structured a certain way. 

If you are a developer like me without a rigorous background in statistics
(Stats 200 in college was a **long** time ago), you may need to brush up
on your stats knowledge before you are able to say whether something in the
data matters or not.

Let's keep going exploring the data. We can select columns and determine how
many unique items are held within it. For example, how many unique countries
and territories are listed?

```
df.countriesAndTerritories.nunique()
```

In this case the result should be 196.


## Asking questions of the data
Those functions are fine for basic querying to learn what's in the
data set, but how do we ask real questions by stringing together some 
commands?

We now know there are 7320 rows in this set since we used the `count`
function above. Each row represents a single day within a country. Now
to ask a question. How many days across these countries were there 10
or more cases reported?

Let's create a new dataframe named df2 with the rows that only have
10 or more cases reported on that day, then count the number of rows
within it.

```
df2 = df[df['cases']>=10]
df2.count()
```

That should give us the value 1531. There have been 1531 instances
of 10 or more COVID-19 cases reported on a single day, across the
196 countries or terrorities listed. But the 1531 is hard to explain
to people. We should pick out a single country and show how many times
10 or more cases were reported on one day. How about a smaller
country like Vietnam that is not being reported on as much as China,
the United States or Italy?

```
df2[df2['countriesAndTerritories']=='Vietnam']
```

This will give us the full output of data by column:

```
         dateRep  day  month  year  cases  deaths countriesAndTerritories geoId countryterritoryCode  popData2018
7217  28/03/2020   28      3  2020     16       0                 Vietnam    VN                  VNM   95540395.0
7219  26/03/2020   26      3  2020     14       0                 Vietnam    VN                  VNM   95540395.0
7220  25/03/2020   25      3  2020     11       0                 Vietnam    VN                  VNM   95540395.0
7222  23/03/2020   23      3  2020     24       0                 Vietnam    VN                  VNM   95540395.0
7226  19/03/2020   19      3  2020     15       0                 Vietnam    VN                  VNM   95540395.0
```

We can also use the `count` function here to confirm there have been
five days in which 10 or more new cases have been reported in Vietnam
so far:

```
df2[df2['countriesAndTerritories']=='Vietnam'].count()
```

We get the output of 5 for the columns. Unfortunately, when you look at
the full data it appears these rows are all very recent and the virus
is just beginning to spread more widely there. Let's hope they along
with every other country is able to turn the tide, flatten the curve
and keep more people from getting sick as we continue onwards.

That's a good spot to leave off, but we covered a lot of pandas ground
in this tutorial!


## What's next?
We just imported and took a look at what's in the European Centre 
for Disease Prevention and Control's COVID-19 data set using
[pandas](/pandas.html). That was a quick tour of some basic pandas
commands and I strongly recommend you peruse the 
[DataFrame documentation list](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html)
to learn about all of the other handy functions that this tool
provides to developers.

You can also get an idea of what to code next in your Python project by 
reading the 
[Full Stack Python table of contents page](/table-of-contents.html).

Questions? Contact me via Twitter 
[@fullstackpython](https://twitter.com/fullstackpython)
or [@mattmakai](https://twitter.com/mattmakai). I'm also on GitHub with
the username [mattmakai](https://github.com/mattmakai).

Something wrong with this post? Fork 
[this page's source on GitHub](https://github.com/mattmakai/fullstackpython.com/blob/master/content/posts/200328-explore-covid-pandas.markdown)
and submit a pull request.
