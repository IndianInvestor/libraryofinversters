---
title: "Plotting the geospatial data clipped by coastlines in Python (codes included)"
date: 2020-05-20
tags: [mapping, techniques, python, geospatial data visualization, geospatial data visualization python, kriging, pykrige, Ordinary Kriging]
excerpt: "In geosciences, we most frequently have to make geospatial plots, but the available data is unevenly distributed and irregular. We like to show the data, in general, for the whole region and one way of performing, so it to do the geospatial interpolation of the data."
mathjax: "true"
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/clipping_coastline_data/fig4.png"
classes:
  - wide
sidebar:
  nav: "all_posts_list"
category: geophysics
---

{% include toc %}

## Introduction

In geosciences, we most frequently have to make geospatial plots, but the available data is unevenly distributed and irregular (Figure 1). We like to show the data, in general, for the whole region and one way of performing, so it to do the geospatial interpolation of the data. Geospatial interpolation means merely that we obtain the interpolated values of the data at regular grid points, both longitudinally and latitudinally. After obtaining these values, if we plot the data, then the grid points is most likely to extend out of the coastline constrain of our study. We wish to plot the data inside the coastline borders of the area, which is our area of study. We can do that by just removing all the grid points outside the perimeter. One way to clip the data outside the coastline path is to remove the grid points outside the region manually, but this method is quite tedious. We, programmers, love being lazy, and that helps us to seek better ways.


{% include image.html url="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/clipping_coastline_data/fig1.png" description="Figure 1: Scatter plot of the data. The size and color of the circles represent the data values." %}

{% include google-adsense-inarticle.html %}

In this post, we aim to do

1. The interpolation of these data values using the ordinary kriging method and
2. plot the output within the coastline border of Taiwan.

If you want to inspect the spatial and temporal pattern in the geospatial data, you can consider doing the [Empirical Orthogonal Function Analysis](/geophysics/empirical-orthogonal-function-analysis-to-inspect-spatial-coherency-of-geospatial-data/). It helps us to get rid of the noise and shows the most dominant pattern in the data.

For implementing the ordinary kriging interpolation, we will use the “pykrige” kriging toolkit available for Python. The package can be easily installed using the “pip” or “conda” package manager for Python.

## Importing necessary modules

{% include google-adsense-inarticle.html %}

```python
import numpy as np
import pandas as pd
import glob
from pykrige.ok import OrdinaryKriging
from pykrige.kriging_tools import write_asc_grid
import pykrige.kriging_tools as kt
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Path, PathPatch
```

{% include google-adsense-inarticle.html %}

<p align="center">
  <img width="100%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/clipping_coastline_data/fig2.png">
  <figcaption style="text-align: center;">Figure 2: Data in the tabular format</figcaption>
</p>

## Reading data

{% include google-adsense-display-ad-horizontal.html %}

The first step for interpolation is to read the available data. Our data is of the format shown in Figure 2. Let’s say we want to interpolate for the “R_FACTOR”. We first read this data file. We can easily do that using the “[pandas](/utilities/how-to-start-using-pandas-immediately-for-earth-data-analysis/)” in Python.

```python
datafile='datafilename.txt'
df=pd.read_csv(datafile,delimiter='s+')
```

Now, we have [read the whole tabular data](/utilities/how-to-start-using-pandas-immediately-for-earth-data-analysis/), but we need only the “R_FACTOR”, “St.Lat”, and “St.Lon” columns.

```python
lons=np.array(df['St.Lon'])
lats=np.array(df['St.Lat'])
data=np.array(df[data])
```

## Kriging data

{% include google-adsense-display-ad-horizontal.html %}

Now, we have our required data available in the three variables. We can, now, define the grid points where we seek the interpolated values.

```python
grid_space = 0.01
grid_lon = np.arange(np.amin(lons), np.amax(lons), grid_space) #grid_space is the desired delta/step of the output array
grid_lat = np.arange(np.amin(lats), np.amax(lats), grid_space)
```

The minimum and maximum of the longitude and latitude are chosen based on the data.

We use the “ordinary kriging” function of “pykrige” package to interpolate our data at the defined grid points. For more details, the user can refer to the [manual of the “pykrige” package](https://media.readthedocs.org/pdf/pykrige/latest/pykrige.pdf).

```python
OK = OrdinaryKriging(lons, lats, data, variogram_model='gaussian', verbose=True, enable_plotting=False,nlags=20)
z1, ss1 = OK.execute('grid', grid_lon, grid_lat)
```

“z1” is the interpolated values of “R_FACTOR” at the grid_lon and grid_lat values.

## Plotting interpolation

{% include google-adsense-display-ad-horizontal.html %}

Now, we wish to plot the interpolated values. We will use the “basemap” module to plot the geographic data.

```python
xintrp, yintrp = np.meshgrid(grid_lon, grid_lat)
fig, ax = plt.subplots(figsize=(10,10))
m = Basemap(llcrnrlon=lons.min()-0.1,llcrnrlat=lats.min()-0.1,urcrnrlon=lons.max()+0.1,urcrnrlat=lats.max()+0.1, projection='merc', resolution='h',area_thresh=1000.,ax=ax)
```

We, first, made the 2D meshgrid using the grid points and then call the basemap object “m” with the Mercator projection. The constraints of the basemap object can be manually defined instead of the minimum and maximum of the latitude and longitude values as used.

```python
m.drawcoastlines() #draw coastlines on the map
x,y=m(xintrp, yintrp) # convert the coordinates into the map scales
ln,lt=m(lons,lats)
cs=ax.contourf(x, y, z1, np.linspace(0, 4500, ncols),extend='both',cmap='jet') #plot the data on the map.
cbar=m.colorbar(cs,location='right',pad="7%") #plot the colorbar on the map
# draw parallels.
parallels = np.arange(21.5,26.0,0.5)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=14, linewidth=0.0) #Draw the latitude labels on the map

# draw meridians
meridians = np.arange(119.5,122.5,0.5)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=14, linewidth=0.0)
```

{% include google-adsense-inarticle.html %}

<p align="center">
  <img width="50%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/clipping_coastline_data/fig3.png">
  <figcaption style="text-align: center;">Figure 3: Interpolated values without masking the outer region.</figcaption>
</p>

This will give us the plot of the interpolated values (Figure 3). Here, we do not seek the plot outside the coastline boundary of Taiwan. We wish to mask the data outside the boundary.

## Masking unnecessary parts in the map

{% include google-adsense-display-ad-horizontal.html %}

```python
##getting the limits of the map:
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
map_edges = np.array([[x0,y0],[x1,y0],[x1,y1],[x0,y1]])
##getting all polygons used to draw the coastlines of the map
polys = [p.boundary for p in m.landpolygons]

##combining with map edges
polys = [map_edges]+polys[:]
##creating a PathPatch
codes = [
[Path.MOVETO]+[Path.LINETO for p in p[1:]]
for p in polys
]

polys_lin = [v for p in polys for v in p]

codes_lin = [xx for cs in codes for xx in cs]

path = Path(polys_lin, codes_lin)
patch = PathPatch(path,facecolor='white', lw=0)
```

{% assign postTitle0 = "Topographic map clipped by coastlines" %}
{% assign postLink0 = "/utilities/plotting-clipped-coastline-relief-map/" %}
{% assign postExcerpt0 = "In this post, I used the same approach but instead of the geospatial dataset, Iused the 1-arc minute topographic map" %}

{% include single-post-ad.html postTitle=postTitle0 postLink=postLink0 postExcerpt=postExcerpt0 %}

Here, the ‘facecolor’ of the ‘pathpatch’ defines the color of the masking. We kept is ‘white,’ but the user can define any color they like.

```python
##masking the data outside the inland of Taiwan
ax.add_patch(patch)
```

{% include google-adsense-inarticle.html %}

<p align="center">
  <img width="50%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/clipping_coastline_data/fig4.png">
  <figcaption style="text-align: center;">Figure 4: Interpolated values with the masking of the outer region.</figcaption>
</p>

```python
plt.show() #to display the plot
# plt.savefig('figurename.png',dpi=300,bbox_inches='tight') #to save the figure in png format
plt.close('all')
```

## Conclusions
In this post, I have shown how one can interpolate geospatial data with the kriging. Then I also showed how to plot the interpolation results on a map and then clip the results outlside the coastlines. I have also made other posts for [clipping the data (topographic) on the coastlines](/utilities/plotting-clipped-coastline-relief-map/) in a similar way.