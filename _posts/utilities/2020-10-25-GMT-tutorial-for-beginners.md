---
title: "GMT tutorial for beginners (codes included)"
date: 2020-10-25
tags: [Generic Mapping Tools, visualization, gmt mapping, geospatial data visualization]
excerpt: "The Generic Mapping Tools is widely used across Earth and Planetary and other fields of studies to process data and generate high-quality illustrations. This post is the first introduction to beginners for getting started in GMT."
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure13.jpg"
classes:
  - wide
sidebar:
  nav: "all_posts_list"
category: utilities
redirect_from:
  - https://www.earthinversion.com/GMT_tutorial_for_beginners/
---

The [Generic Mapping Tools](https://www.generic-mapping-tools.org) is widely used across Earth and Planetary and other fields of studies to process data and generate high quality illustrations. This post is first introduction to beginners for getting started in GMT.

Please note that recently GMT version 6 has been released but this post is focussed on GMT version 5. For readers interested in GMT 6, I recommend beginners to get started with [pyGMT]({{ site.url }}{{ site.baseurl }}/utilities/pygmt-high-resolution-topographic-map-in-python/).

{% include toc %}

## How to install GMT

{% include google-adsense-inarticle.html %}

**In Ubuntu**: `sudo apt-get install gmt gmt-dcw gmt-gshhg`

**In Mac**: `brew install gmt`

**For other operating systems**, check [GMT website](http://gmt.soest.hawaii.edu/projects/gmt/wiki/Installing)

{% assign postTitle0 = "Easiest way to install GMT" %}
{% assign postLink0 = "https://youtu.be/6TO65Xc3bkI" %}
{% assign postExcerpt0 = "Install GMT 6.1.1 in a Pythonic way using anaconda." %}

{% include single-post-ad.html postTitle=postTitle0 postLink=postLink0 postExcerpt=postExcerpt0 %}

### Requirements:

Below is a list of examples, originally inspired from the [GMT](/utilities/High-quality-maps-using-the-modern-interface-to-the-Generic-Mapping-Tools/) documentation. For successfully running the codes, the user need to fulfill following requirements:

- Pre-installed [GMT](/utilities/High-quality-maps-using-the-modern-interface-to-the-Generic-Mapping-Tools/)-5, check by typing `gmt` in terminal.
- Pre-installed netcdf-5, check by typing `ncdump`.
- Pre-installed ghostview package, check by typing `gv`.
- Downloaded `ETOPO1_Bed_g_gmt4.grd` in the **Data** directory from the [NOAA website](https://www.ngdc.noaa.gov/mgg/global/relief/ETOPO1/data/bedrock/grid_registered/netcdf/).

## Examples:

{% assign postTitle0 = "PyGMT: High-Resolution Topographic Map in Python" %}
{% assign postLink0 = "/utilities/pygmt-high-resolution-topographic-map-in-python/" %}
{% assign postExcerpt0 = "If you prefer using Python for most of your scripting, then you should look into the PyGMT that is an implementation of GMT-6 in Python" %}

{% include single-post-ad.html postTitle=postTitle0 postLink=postLink0 postExcerpt=postExcerpt0 %}

Readers can download the package containing all the following examples from [here](https://github.com/earthinversion/GMT_tutorial_for_beginners.git). The package consists of three directories: Data, Scripts and Figures.

{% include google-adsense-display-ad.html %}

- The **Data** directory contains the data files required to run the scripts in the **Scripts** directory.
- The **Scripts** directory consists of all the bash scripts for all the later examples.
- The **Figures** directory consists of all the example plots from 1-24.

### Linear Plots

This script contains commands for making basemap for linear projections including the log-log plot. It also explains how to add title, xlabel, ylabel, tick-marks, background-color to the plot.

<p align="center">
  <img width="45%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure1.jpg">
  <img width="45%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure2.jpg">
</p>

{% include google-adsense-inarticle.html %}

<p align="center">
  <img width="30%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure3.jpg">
  <img width="30%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure4.jpg">
  <img width="30%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure5.jpg">
</p>

<script src="https://gist.github.com/earthinversion/e7b2ce53d4a2259b643e85d7262962c4.js"></script>

### Plotting maps with different projections

This example explains how to plot the Mercator projection, Alber's projection, Orthographic projection, Eckert projection.

<p align="center">
  <img width="45%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure6.jpg">
  <img width="45%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure7.jpg">
</p>

{% include google-adsense-inarticle.html %}

<p align="center">
  <img width="30%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure8.jpg">
  <img width="30%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure9.jpg">
  <img width="30%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure10.jpg">
</p>

<script src="https://gist.github.com/earthinversion/0901b4345641523553c9beed2d71ebd9.js"></script>

{% assign postLink0 = "https://www.facebook.com/earthinversionwebsite/posts/109883117873289" %}
{% include facebook_postads.html postLink=postLink0 %}

### Plotting lines and symbols

This example explains the use of `psxy` command to plot the lines and symbols. It also contains the commands to plot the earthquake epicenter with colors representing depths and symbol size representing magnitude.

{% include google-adsense-display-ad.html %}

<p align="center">
  <img width="30%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure11.jpg">
  <img width="30%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure12.jpg">
  <img width="30%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure13.jpg">
</p>

<script src="https://gist.github.com/earthinversion/698c624b1730f8fa2c8cb120f73a0ce7.js"></script>

### Customizing plots with texts

This example explains how to type texts onto the plots. The user can even type mathematical equations.

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure14.jpg">
</p>

<script src="https://gist.github.com/earthinversion/d47113c29487a1d9a428c29d08cf9029.js"></script>

### Contour lines in GMT

This bash example explains how to plot the contour lines using the command `grdcontour`. It also explains how to cut the large data set using the `grdcut` command and obtain the information about it using the `grdinfo`. It also explains how to do interpolation of data (**nearest neighbour** and **spline**).

{% include google-adsense-display-ad.html %}

<p align="center">
  <img width="45%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure15.jpg">
  <img width="45%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure16.jpg">
</p>

<p align="center">
  <img width="45%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure17.jpg">
  <img width="45%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure18.jpg">
</p>

<script src="https://gist.github.com/earthinversion/e08eaeb0d30d4bd151a6ee848b498bc8.js"></script>

### Colorbars and colorscales

This example contains the description of how to make the cpt files, and plot the colorbars using `psscale` command. It also explains plotting the relief data.

{% include google-adsense-display-ad.html %}

<p align="center">
  <img width="30%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure19.jpg">
  <img width="30%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure20.jpg">
  <img width="30%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure21.jpg">
</p>

<script src="https://gist.github.com/earthinversion/dfdbc359f46da73ff610308dbf8fb553.js"></script>

### Plotting NetCDF data in GMT

This example shows how to plot the multidimensional netcdf data in [GMT](/utilities/High-quality-maps-using-the-modern-interface-to-the-Generic-Mapping-Tools/).

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure22.jpg">
</p>

<script src="https://gist.github.com/earthinversion/1591437418d70a91c8b524204a3903a7.js"></script>

### Three dimensional plots: Mesh and Surface plots

This examples script includes how to plot the data as 3D plots using two methods: mesh plot, color-coded surface.

<p align="center">
  <img width="45%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure23.jpg">
  <img width="45%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-beginners/GMT_figure24.jpg">
</p>

{% include google-adsense-inarticle.html %}

<script src="https://gist.github.com/earthinversion/1d478940fd1b8c5f0157cc4d8e595b8e.js"></script>

