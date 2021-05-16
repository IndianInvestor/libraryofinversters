---
title: "Time Series Analysis in Geophysics (codes included)"
date: 2020-10-27
tags: [time series, analysis, loading, visualization]
excerpt: "Time-series analysis is essential in most fields of science, including geophysics, economics, etc. Most of the geophysical data comes in a time-series format, including the seismic recordings. In this part of the series of time series analysis, we will see how we can quickly load the data and visualize it."
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/timeSeriesAnalysisGeophysics/fig8.png"
classes:
  - wide
sidebar:
  nav: "all_posts_list"
category: geophysics
---

{% include toc %}

Time-series analysis is essential in most fields of science, including geophysics, economics, etc. Most of the geophysical data comes in a time-series format, including the seismic recordings. In this part of the series of tutorial, we will see how we can quickly load the data, and visualize it.

## Prerequisites

This tutorial does not require the reader to have any basic understanding of Python or any programming language. But we expect the reader to have installed the jupyter notebook on their system. If the reader has not installed it yet, then they can follow the previous post where we went through the steps involved in getting started with Python.

## What is Time-series?

Time-series is a collection of data at fixed time intervals. This can be analyzed to obtain long-term trends, statistics, and many other sorts of inferences depending on the subject.

## Data

{% include google-adsense-display-ad-horizontal.html %}

We also need some data to undergo the analysis. We demonstrate the analysis using our GPS data. It can be downloaded from [here](https://drive.google.com/drive/folders/1PDNrQ-ATM_q3MqeN-z4Nog6EwJaETMHx?usp=sharing).

{% assign postLink0 = "https://www.facebook.com/earthinversionwebsite/posts/108717261323208" %}
{% include facebook_postads.html postLink=postLink0 %}

## Let’s get started

The first step is always to start the Python interpreter. In our case, we will use the jupyter notebook.

{% include google-adsense-display-ad-horizontal.html %}

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/timeSeriesAnalysisGeophysics/fig1.png">
</p>

Jupyter notebook can be started using the terminal. Firstly, navigate to your directory containing the data and the type “jupyter notebook” on your terminal.

```
jupyter notebook
```

Next, we create a new Python 3 notebook, rename it as pythontut1. Then, we need to import some of the libraries:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from matplotlib.pyplot import rcParams
rcParams['figure.figsize'] = 15, 6
```

### Loading the data
{% include google-adsense-display-ad-horizontal.html %}

Now, we load the data using the [pandas](/utilities/how-to-start-using-pandas-immediately-for-earth-data-analysis/) library functions. Here, we use the function read_csv. But, before that let’s observe the format of the data:

```
!head 0498.COR
```

The prefix “!” can be used to execute any Linux command in the notebook.

{% include google-adsense-display-ad-horizontal.html %}

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/timeSeriesAnalysisGeophysics/fig2.png">
</p>

We can see that the data has no header information, and 8 columns. The columns are namely, “year”, “latitude”, “longitude”, “Height”, “dN”, “dE”, “dU”.

So, now we read the data and set the above names to the different columns.

```python
df=pd.read_csv("0498.COR", header=None, delimiter='\s+', names=['Year',"Lat","Long","Hgt","dN","dE","dU","nav"])
df.head()
```

{% assign postLink0 = "https://www.facebook.com/earthinversionwebsite/posts/113136297547971" %}
{% include facebook_postads.html postLink=postLink0 %}


It is essential to understand the above command. We gave the argument of the filename, header (default is the first line), delimiter (default is a comma) and the names of each column, respectively. Then we output the first 5 lines of the data using the df.head() command.

{% include google-adsense-display-ad-horizontal.html %}

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/timeSeriesAnalysisGeophysics/fig3.png">
</p>

Our data is now loaded, and if we want to extract any section of the data, we can easily do that.

```python
df['Year'].head()
df[['Year','Lat']].head()
```

{% include google-adsense-display-ad-horizontal.html %}

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/timeSeriesAnalysisGeophysics/fig4.png">
</p>

Here, we have used the column names to extract the two columns only. We can also use the index values.

```python
df.loc[:,"Year"].head()
df.iloc[:,3].head()
```

{% include google-adsense-display-ad-horizontal.html %}

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/timeSeriesAnalysisGeophysics/fig5.png">
</p>

When we use “.loc” method to extract the section of the data, then we need to use the column name whereas when we use the “.iloc” method then we use the index values. Here, df.iloc[:,3] extracts all the rows of the 3rd column (“Hgt”).

### Analysis

Now, we have the data loaded. Let’s plot the “dN”, “dE”, and “dU” values versus the year. Before doing that, let’s set the “Year” column as the index column.

{% assign postLink0 = "https://www.facebook.com/earthinversionwebsite/posts/113134847548116" %}
{% include facebook_postads.html postLink=postLink0 %}

```python
df.set_index("Year", inplace=True)
df.head()
```

{% include google-adsense-display-ad-horizontal.html %}

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/timeSeriesAnalysisGeophysics/fig6.png">
</p>

We can see the “Year” column as the index of the data frame now. Plotting using Pandas is extremely easy.

```
df.plot()
```

{% include google-adsense-display-ad-horizontal.html %}

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/timeSeriesAnalysisGeophysics/fig7.png">
</p>

We can also customize the plot easily.

```python
df.plot(y=['dN',"dE","dU"],grid=True)
plt.ylabel("Amplitude")
plt.suptitle("GPS Data Visualization")
plt.title("0498")
```

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/timeSeriesAnalysisGeophysics/fig8.png">
</p>

If we want to save the figure, then we can use the command:

```python
plt.savefig('0498Data.pdf',dpi=300,bbox_inches='tight')
```

{% include google-adsense-display-ad-horizontal.html %}

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/timeSeriesAnalysisGeophysics/fig9.png">
</p>

This saves the figure as the pdf file named “0498Data.pdf”. The format can be set to any type “.png”, “.jpg”, ‘.eps”, etc. We set the resolution to be 300 dpi. This can be varied depending on our need. Lastly, “bbox_inches =‘tight’” crops our figure to remove all the unnecessary space.

## Next Tutorial

We have loaded the data and visualized it. But we can see that our data has some trend and seasonality. In the future tutorial, we will learn how to remove that.


