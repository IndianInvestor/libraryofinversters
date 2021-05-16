---
title: "PyGMT: High-Resolution Topographic Map in Python (codes included)"
date: 2020-08-15
tags:
  [
    seismology,
    topography,
    GMT,
    Generic Mapping Tools,
    visualization,
    geospatial data visualization, 
    geospatial data visualization python
    python
  ]
excerpt: "A simple tutorial on how to plot high resolution topographic map using GMT tools in Python"
classes:
  - wide
redirect_from:
  - /pygmt-high-resolution-topographic-map-in-python/
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/pygmt/topo-plot.png"
sidebar:
  nav: "all_posts_list"
category: utilities
---

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/pygmt/topo-plot.png">
  <figcaption>Topographic Map of Southern India</figcaption>
</p>
{% include toc %}

## Introduction
If you have been working in seismology, then you must have come across [Generic Mapping Tools (GMT) software](https://www.generic-mapping-tools.org). It is widely used software, not only in seismology but across the Earth, Ocean, and Planetary sciences and beyond. It is a free, open-source software used to generate publication quality maps or illustrations, process data and make animations. Recently, GMT built API (Application Programming Interface) for MATLAB, Julia and Python. In this post, we will explore the Python wrapper library for the GMP API - [PyGMT](https://www.pygmt.org/). Using the GMT from Python script allows enormous capabilities.

{% assign postLink0 = "https://www.facebook.com/earthinversionwebsite/posts/108772077984393" %}
{% include facebook_postads.html postLink=postLink0 %}



The API reference for PyGMT can be accessed from [here](https://www.pygmt.org/latest/api/index.html) and is strongly recommended. Although PyGMT project is still in completion, there are many functionalities available.


## Step-by-step guide for PyGMT using an example
In this post, we will demonstrate the PyGMT implementation by plotting the topographic map of southern India. We will also plot some markers on the map.

<p align="center"><iframe src="https://assets.pinterest.com/ext/embed.html?id=794744665493240384" height="295" width="345" frameborder="0" scrolling="no" ></iframe></p>

{% include google-adsense-display-ad.html %}

### Importing Libraries

The first thing I like to do is to import all the necessary libraries for the task. This keeps the code organized.

<p align="center">
   <iframe src="https://assets.pinterest.com/ext/embed.html?id=794744665493240277" height="295" width="345" frameborder="0" scrolling="no" ></iframe>
</p>

```python
import pygmt
```

```python
minlon, maxlon = 60, 95
minlat, maxlat = 0, 25
```



### Define topographic data source

The topographic data can be accessed from various sources. In this snippet below, I listed a couple of sources.

```python
#define etopo data file
# topo_data = 'path_to_local_data_file'
topo_data = '@earth_relief_30s' #30 arc second global relief (SRTM15+V2.1 @ 1.0 km)
# topo_data = '@earth_relief_15s' #15 arc second global relief (SRTM15+V2.1)
# topo_data = '@earth_relief_03s' #3 arc second global relief (SRTM3S)
```



### Initialize the pyGMT figure

Similar to the [matplotlib](/techniques/advanced-2D-plots-with-matplotlib/)'s `fig = plt.Figure()`, PyGMT begins with the creation of Figure instance.

```python
# Visualization
fig = pygmt.Figure()
```

{% include google-adsense-display-ad.html %}

### Define CPT file
```python
# make color pallets
pygmt.makecpt(
    cmap='topo',
    series='-8000/8000/1000',
    continuous=True
)
```



### Plot the high resolution topography from the data source

Now, we provide the `topo_data`, `region` and the `projection` for the figure to plot. The `region` can also be provided in the form of ISO country code strings, e.g. `TW` for Taiwan, `IN` for India, etc. For more ISO codes, check the wikipedia page [here](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes). In this example, we used the `projection` of `M4i`, which specifies four-inch wide Mercator projection. For more projection options, check [here](https://docs.generic-mapping-tools.org/latest/proj-codes.html).

```python
#plot high res topography
fig.grdimage(
    grid=topo_data,
    region=[minlon, maxlon, minlat, maxlat],
    projection='M4i'
    )
```

{% include google-adsense-display-ad.html %}

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/pygmt/topo-plot-test1.png">
</p>

```python
#plot high res topography
fig.grdimage(
    grid=topo_data,
    region=[minlon, maxlon, minlat, maxlat],
    projection='M4i',
    frame=True
    )
```


<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/pygmt/topo-plot-test2.png">
</p>

```python
#plot high res topography
fig.grdimage(
    grid=topo_data,
    region=[minlon, maxlon, minlat, maxlat],
    projection='M4i',
    shading=True,
    frame=True
    )
```

{% include google-adsense-display-ad.html %}
<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/pygmt/topo-plot-test3.png">
</p>



### Plot the coastlines/shorelines on the map

`Figure.coast` can be used to plot continents, shorelines, rivers, and borders on maps. For details, visit [pygmt.Figure.coast](https://www.pygmt.org/latest/api/generated/pygmt.Figure.coast.html#pygmt.Figure.coast).

```python
fig.coast(
    region=[minlon, maxlon, minlat, maxlat],
    projection='M4i',
    shorelines=True,
    frame=True
    )
```


<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/pygmt/topo-plot-test4.png">
</p>



### Plot the topographic contour lines

We can also plot the topographic contour lines to emphasize the change in topography. Here, I used the contour intervals of 4000 km and only show contours with elevation less than 0km.

```python
fig.grdcontour(
    grid=topo_data,
    interval=4000,
    annotation="4000+f6p",
    limit="-8000/0",
    pen="a0.15p"
    )
```

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/pygmt/topo-plot-test5.png">
</p>



### Plot data on the topographic map
```python
## Generate fake coordinates in the range for plotting
lons = minlon + np.random.rand(10)*(maxlon-minlon)
lats = minlat + np.random.rand(10)*(maxlat-minlat)
```

```python
# plot data points
fig.plot(
    x=lons,
    y=lats,
    style='c0.1i',
    color='red',
    pen='black',
    label='something',
    )
```

We plot the locations by red cicles. You can change the markers to any other marker supported by GMT, for example `a0.1i` will produce stars of size 0.1 inches.

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/pygmt/topo-plot-test6.png">
</p>


### Plot colorbar for the topography

Default is horizontal colorbar

```python
# Plot colorbar
fig.colorbar(
    frame='+l"Topography"'
    )
```

{% include google-adsense-display-ad.html %}

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/pygmt/topo-plot-test7.png">
</p>

For vertical colorbar:

```python
# For vertical colorbar
fig.colorbar(
frame='+l"Topography"',
position="x11.5c/6.6c+w6c+jTC+v"
)
```

We can define the location of the colorbar using the string `x11.5c/6.6c+w6c+jTC+v`. `+v` specifies the vertical colorbar.

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/pygmt/topo-plot-test8.png">
</p>



### Output the figure to a file

Similar to `matplotlib`, PyGMT shows the figure by

```python
# save figure
fig.show() #fig.show(method='external')
```

To save figure to png. PyGMT crops the figure by default and has output figure resolution of 300 dpi for `png` and 720 dpi for `pdf`. There are several other output formats available as well.

```python
# save figure
fig.savefig("topo-plot.png", crop=True, dpi=300, transparent=True)
```

```python
fig.savefig("topo-plot.pdf", crop=True, dpi=720)
```

If you want to save all formats (e.g., pdf, eps, tif) then 

```python
allformat = 1

if allformat:
    fig.savefig("topo-plot.pdf", crop=True, dpi=720)
    fig.savefig("topo-plot.eps", crop=True, dpi=300)
    fig.savefig("topo-plot.tif", crop=True, dpi=300, anti_alias=True)

```
{% assign postLink0 = "https://www.facebook.com/earthinversionwebsite/posts/109883117873289" %}
{% include facebook_postads.html postLink=postLink0 %}

### Complete Script

{% include google-adsense-inarticle.html %}

<script src="https://gist.github.com/earthinversion/84104f759cb0af67fd18f3006bbc2ade.js"></script>

## Plot Focal Mechanism on a Map

How would you plot the focal mechanism on a map? This can be simply done in GMT using the command `psmeca`. But PyGMT do not support `psmeca` so far. So, we use a workaround. We call the GMT module using the PyGMT's `pygmt.clib.Session` class. This we do using the context manager `with` in Python.

{% include google-adsense-inarticle.html %}

<script src="https://gist.github.com/earthinversion/46e6bdfacdf1e355d5e368c1582c2759.js"></script>

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/pyGMT-fm/fm-plot.png">
  <figcaption>Randomly generated focal mechanisms plotted on topographic map of India</figcaption>
</p>

## Plotting interstation paths between two stations

The following script uses the `sel_pair_csv` file for the coordinates of the pairs of stations. The `sel_pair_csv` file is a csv file that is formatted like:

```
   stn1     stlo1    stla1  stn2     stlo2    stla2
0  A002  121.4669  25.1258  B077  120.7874  23.8272
1  A002  121.4669  25.1258  B117  120.4684  24.1324
2  A002  121.4669  25.1258  B123  120.5516  24.0161
3  A002  121.4669  25.1258  B174  120.8055  24.2269
4  A002  121.4669  25.1258  B183  120.4163  23.8759
```

<script src="https://gist.github.com/earthinversion/c3babdf1a77afbfab0bbe5d4c49bcee1.js"></script>

{% include google-adsense-inarticle.html %}

<p align="center">
  <img width="50%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/pygmt/interstation_map.png">
  <figcaption>Interstation paths (red lines) for 5056 pairs of stations in Taiwan</figcaption>
</p>
## Event-Station Map 

<script src="https://gist.github.com/earthinversion/cbf0f331e979400884dced1bfa4d0fa8.js"></script>

Here, I used the [Mollweide projection](https://www.pygmt.org/latest/projections/misc/misc_mollweide.html#sphx-glr-projections-misc-misc-mollweide-py) but this code can be applied for any other projections with a little tweak. 

The first few lines of the data file are:

```
network,station,channel,stla,stlo,stel,evla,evlo,evdp,starttime,endtime,samplingRate,dist,baz
TW,GWUB,HHZ,24.5059,121.1131,2159.0,-58.5981,-26.4656,164.66,2018-12-11T02:25:32.000002Z,2018-12-11T03:56:31.990002Z,100.0,15445.41,205.14
TW,LXIB,HHZ,24.0211,121.4133,1327.0,-58.5981,-26.4656,164.66,2018-12-11T02:25:32.000000Z,2018-12-11T03:56:31.990000Z,100.0,15409.58,204.75
TW,VCHM,HHZ,23.2087,119.4295,60.0,-58.5981,-26.4656,164.66,2018-12-11T02:25:32.000000Z,2018-12-11T03:56:31.990000Z,100.0,15242.27,205.4
TW,VDOS,HHZ,20.701,116.7306,5.0,-58.5981,-26.4656,164.66,2018-12-11T02:25:32.000000Z,2018-12-11T03:56:31.990000Z,100.0,14871.63,205.6
TW,VNAS,HHZ,10.3774,114.365,2.0,-58.5981,-26.4656,164.66,2018-12-11T02:25:32.000000Z,2018-12-11T03:56:31.990000Z,100.0,13726.26,203.23
TW,VWDT,HHZ,23.7537,121.1412,2578.0,-58.5981,-26.4656,164.66,2018-12-11T02:25:32.000000Z,2018-12-11T03:56:31.990000Z,100.0,15371.08,204.77
TW,VWUC,HHZ,24.9911,119.4492,42.0,-58.5981,-26.4656,164.66,2018-12-11T02:25:32.000000Z,2018-12-11T03:56:31.990000Z,100.0,15420.85,206.25
TW,YD07,HHZ,25.1756,121.62,442.0,-58.5981,-26.4656,164.66,2018-12-11T02:25:32.000000Z,2018-12-11T03:56:31.990000Z,100.0,15534.34,205.2
TW,HOPB,HHZ,24.3328,121.6929,160.0,-58.5981,-26.4656,164.66,2018-12-11T02:25:32.003130Z,2018-12-11T03:56:31.993130Z,100.0,15452.83,204.75
TW,SYNB,HHZ,23.2482,120.9862,2352.0,-58.5981,-26.4656,164.66,2018-12-11T02:25:32.003131Z,2018-12-11T03:56:31.993131Z,100.0,15313.6,204.62
TW,DYSB,HHZ,24.8208,121.4049,1000.0,-58.5981,-26.4656,164.66,2018-12-11T02:25:32.008393Z,2018-12-11T03:56:31.998393Z,100.0,15489.54,205.14
TW,FUSB,HHZ,24.7597,121.5875,690.0,-58.5981,-26.4656,164.66,2018-12-11T02:25:32.008394Z,2018-12-11T03:56:31.998394Z,100.0,15491.23,205.01
TW,HGSD,HHZ,23.4921,121.4239,134.8,-58.5981,-26.4656,164.66,2018-12-11T02:25:32.008393Z,2018-12-11T03:56:31.998393Z,100.0,15356.77,204.5
---
```

{% include google-adsense-inarticle.html %}

<p align="center">
  <img width="2537" height="1188" max-width="60%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/pygmt/event_map_test_event.webp">
  <figcaption>Event Station Map</figcaption>
</p>

## References

<!-- <h2 id="references">References <a href="#top"><i class="fa fa-arrow-circle-up" aria-hidden="true"></i></a></h2> -->

<ol>
  <li>Uieda, L., Wessel, P., 2019. PyGMT: Accessing the Generic Mapping Tools from Python. AGUFM 2019, NS21B--0813.</li>
  <li>Wessel, P., Luis, J.F., Uieda, L., Scharroo, R., Wobbe, F., Smith, W.H.F., Tian, D., 2019. The Generic Mapping Tools Version 6. Geochemistry, Geophys. Geosystems 20, 5556–5564. https://doi.org/10.1029/2019GC008515</li>
</ol>


