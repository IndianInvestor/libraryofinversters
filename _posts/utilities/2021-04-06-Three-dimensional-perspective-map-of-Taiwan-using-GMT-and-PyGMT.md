---
title: "Three-dimensional perspective map of Taiwan using GMT and PyGMT (codes included)"
date: 2021-04-06
tags: [GMT, GMT6, pygmt, three-dimensional map, geospatial data visualization, geospatial data visualization python, python]
excerpt: "We learn how to make the three-dimensional map using both GMT and PyGMT"
mathjax: "true"
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-pygmt-3dmap/topo-plot_3d.png"
classes:
  - wide
sidebar:
  nav: "all_posts_list"
category: utilities


---

{% include toc %}

We learn how to make the three-dimensional map using both [GMT](/utilities/High-quality-maps-using-the-modern-interface-to-the-Generic-Mapping-Tools/) and PyGMT. Python lovers may choose to use the PyGMT version and others might prefer the GMT version, but both versions are necessarily using the same core library. PyGMT is simply the Python wrapper of GMT. However, since it is coded in Python, it can be quite flexible for several applications.

{% assign postLink0 = "https://www.facebook.com/earthinversionwebsite/posts/108772077984393" %}
{% include facebook_postads.html postLink=postLink0 %}

## Using GMT to plot the 3-D perspective map of Taiwan

```bash
#!/usr/bin/bash

minlon=120
maxlon=122.1

minlat=21.8
maxlat=25.6

gmt begin taiwan png
    gmt basemap -R${minlon}/${maxlon}/${minlat}/${maxlat}/-6/4 -JM3i -JZ0.8i -p150/25 -B -Bz2+l"Topo (km)" -BSEwnZ
    gmt grdview @earth_relief_01m -R${minlon}/${maxlon}/${minlat}/${maxlat}/-6000/4000 -p -C -I+d -N-6000+ggray -Qi500 -Wthin
    gmt basemap -p -TdjTL+w3c+l+o-2c/-1c
gmt end
```

{% include google-adsense-inarticle.html %}

The script is very straightforward. We first define the map coordinates, the used the [GMT](/utilities/High-quality-maps-using-the-modern-interface-to-the-Generic-Mapping-Tools/)6 interface to plot it.

We first start with the `basemap` and define the region and the vertical range of the map. Here, we call the range of the vertical axis from -6 to 4 units. We used the Mercator projection (`-JM`) and scale the vertical axis to be `0.8i` and the perspective is set to 150 degrees of azimuth and 25 degrees of elevation (`-p150/25`). We label the vertical axis every 2 units - `-Bz2`. Note that [GMT](/utilities/High-quality-maps-using-the-modern-interface-to-the-Generic-Mapping-Tools/)6 can automatically retrieve topographic data if it is not locally available, and if we give the data path as `@earth_relief_01m`.


{% include google-adsense-inarticle.html %}
<figure>
 <img src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-pygmt-3dmap/taiwan.png"  alt="taiwan 3d map using GMT6">
 <figcaption>Three dimensional perspective map of Taiwan using GMT6</figcaption>
</figure>



## Using PyGMT to plot the 3-D perspective map of Taiwan

```python
import pygmt

minlon, maxlon = 120., 122.1
minlat, maxlat = 21.8, 25.6

# Load sample earth relief data
grid = pygmt.datasets.load_earth_relief(resolution="03s", region=[minlon, maxlon, minlat, maxlat])

frame =  ["xa1f0.25","ya1f0.25", "z2000+lmeters", "wSEnZ"]

pygmt.makecpt(
        cmap='geo',
        series=f'-6000/4000/100',
        continuous=True
    )
fig = pygmt.Figure()
fig.grdview(
    grid=grid,
    region=[minlon, maxlon, minlat, maxlat, -6000, 4000],
    perspective=[150, 30],
    frame=frame,
    projection="M15c",
    zsize="4c",
    surftype="i",
    plane="-6000+gazure",
    shading=0,
    # Set the contour pen thickness to "1p"
    contourpen="1p",
)
fig.basemap(
    perspective=True,
    rose="jTL+w3c+l+o-2c/-1c" #map directional rose at the top left corner 
)

fig.colorbar(perspective=True, frame=["a2000", "x+l'Elevation in (m)'", "y+lm"])
fig.savefig("topo-plot_3d.png", crop=True, dpi=300)
```

{% include google-adsense-inarticle.html %}

This plot is almost the same as before but with slight modifications. The first thing to notice is the topographic data resolution (3s data used). We also clip the standard `geo` colormap to the range of -6000 to 4000 meters. The perspective, in this case, is 150 degrees azimuth and 30 degrees of elevation. The azimuth ranges from -180 to 180 degrees and elevation from 0 to 90 degrees. We set the shading to 0 (ranges from -1 to 1). As in the [GMT](/utilities/High-quality-maps-using-the-modern-interface-to-the-Generic-Mapping-Tools/) case, we plot the map directional rose at the top left corner.

{% include google-adsense-inarticle.html %}

<figure>
 <img src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/gmt-pygmt-3dmap/topo-plot_3d.png"  alt="taiwan 3d map using PyGMT">
 <figcaption>Three dimensional perspective map of Taiwan using PyGMT</figcaption>
</figure>



Please note that there's difference in the map scale for the GMT and PyGMT case. This comes because of the different scales we took in the two cases. We took `-JM3i`or 3 inch Mercator projection in the case of GMT and `M15c` or 15 cm Mercator in case of PyGMT.