---
title: "Working with Obspy and Basemap (codes included)"
date: 2020-11-06
tags: [obspy, basemap]
excerpt: "This post is aimed to resolve the issues regarding the conflicts of using obspy and basemap libraries together."
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/obspy-basemap/basemap_catalog_plot.png"
classes:
  - wide
sidebar:
  nav: "all_posts_list"
category: utilities
---

{% include toc %}

Many people have inquired me regarding the conflicts of using Basemap and Obspy together. The conflicts mostly come with the incompatibility of the matplotlib version used in the relatively newer version of Obspy and the Basemap library. Please note that the Basemap library is no longer supported and the readers are recommended to migrate to other libraries for plotting such as Cartopy or [pyGMT](file:///Users/utpalkumar50/GoogleDrive/earthinversion/_posts/utilities/%7B%7B%20site.url%20%7D%7D%7B%7B%20site.baseurl%20%7D%7D/utilities/pygmt-high-resolution-topographic-map-in-python/). However, these libraries are still under development so it is understandable if readers want to stick with the Basemap for the time being.

This post do not claim to solve the issues but it shows a way to work with the two together.

{% include google-adsense-display-ad.html %}

## Installing Anaconda environment for Obspy and Basemap

Basemap is easy to install using Anaconda, so I most often take this path. I will start by creating a "Python 3.6" anaconda environment. Why Python 3.6? Well, I know that it works. The reader is advised to explore the newer version of Python.

You can download my installation of this environment from [here](https://gist.github.com/earthinversion/db6ec86dcb138b6744409c9d21a415b9/archive/366875a9cf8c3ecda614e768233366f2d09507b9.zip). For installing the environment from the downloaded `obsbase.yml` file, run:

```
conda env create -f obsbase.yml
```

For step by step installation, follow:

```
conda create -n obsbase python=3.6
```

Then activate the `obsbase` environment.

```
conda activate obsbase
```

After that I will install Basemap first so that libraries which comes next (Obspy in this case) try first to resolve conflicts with Basemap if any or install the compatible version.

```
conda install -c conda-forge basemap
```

Then I install Obspy:

```
conda install -c conda-forge obspy
```

Now, we have the working version of both Obspy and Basemap. Let's test it.

## Download seismic stream using Obspy and remove instrument response

{% include google-adsense-display-ad.html %}

I use this script because it can possibly throw `Attribute Error with numpy.fft.fftpack` when removing the response of the stream.

<script src="https://gist.github.com/earthinversion/5a05d08c4f80284b2c81595f6e1179d4.js"></script>

In my case, it runs just fine.

```
1 Trace(s) in Stream:
IU.TATO.00.BHZ | 2020-10-19T20:53:39.019538Z - 2020-10-19T21:09:38.969538Z | 20.0 Hz, 19200 samples
```

<p align="center"> <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/obspy-basemap/myStream.png"> </p>

## Plot with the help of **Basemap**

Now, let us run an example basemap script with Obspy. I copied this script from the Obspy [webpage](https://docs.obspy.org/tutorial/code_snippets/basemap_plot_with_beachballs.html) for the quick test.

{% include google-adsense-inarticle.html %}

```python
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

from obspy import read_inventory, read_events

# Set up a custom basemap, example is taken from basemap users' manual
fig, ax = plt.subplots()

# setup albers equal area conic basemap
# lat_1 is first standard parallel.
# lat_2 is second standard parallel.
# lon_0, lat_0 is central point.
m = Basemap(
   width=8000000,
   height=7000000,
   resolution="c",
   projection="aea",
   lat_1=40.0,
   lat_2=60,
   lon_0=35,
   lat_0=50,
   ax=ax,
)
m.drawcoastlines()
m.drawcountries()
m.fillcontinents(color="wheat", lake_color="skyblue")
# draw parallels and meridians.
m.drawparallels(np.arange(-80.0, 81.0, 20.0))
m.drawmeridians(np.arange(-180.0, 181.0, 20.0))
m.drawmapboundary(fill_color="skyblue")
ax.set_title("Albers Equal Area Projection")

# we need to attach the basemap object to the figure, so that obspy knows about
# it and reuses it
fig.bmap = m

# now let's plot some data on the custom basemap:
inv = read_inventory()
inv.plot(fig=fig, show=False)
cat = read_events()
cat.plot(fig=fig, show=False, title="", colorbar=False)

plt.savefig("basemap_catalog_plot.png", dpi=300, bbox_inches="tight")
```

{% include google-adsense-inarticle.html %}

<p align="center"> <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/obspy-basemap/basemap_catalog_plot.png"> </p>