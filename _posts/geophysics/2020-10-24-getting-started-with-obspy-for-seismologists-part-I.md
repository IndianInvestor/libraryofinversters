---
title: "Getting started with Obspy:  Downloading waveform data (codes included)"
date: 2020-10-24
tags: [obspy, python, seismology, downloading-data, visualization]
excerpt: "Obspy is an open-source Python framework developed for the processing of seismological data. In this post, I will introduce how to use Obspy along with some details of the required Python steps."
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/obspy-part-I/myStream.png"
redirect_from:
  - /geophysics/Getting-started-with-Obspy-for-seismologists-Part-I/
classes:
  - wide
sidebar:
  nav: "all_posts_list"
category: geophysics
---

Obspy is getting popular everyday among seismologists for data analysis and for quick visualization in some cases. But I found that it is still difficult for some researchers to transition from traditional tools like SAC, SEISAN, etc to modern and flexible Obspy. The main reason is not the complexity of Obspy but their unfamiliarity to Python. Python adds immense dynamics and flexibility to Obspy. In my opinion, the greatest feature of Python is to act as a wrapper for all major programming languages and also provide the native capability to perform all sorts of mathematical and graphical operations. Obspy plays on the strength of Python. In this post, I will introduce how to use Obspy along with some details of the required Python steps.

{% include google-adsense-display-ad-horizontal.html %}

{% include toc %}

### Introduction

Obspy is an open-source Python framework developed for the processing of seismological data. The strength of Obspy is that it works with several file formats, contains modules for accessing data from several open-access data centers and has modules for routine seismological processing.

### Installation

{% include google-adsense-display-ad-horizontal.html %}

If you do not have Obspy installed in your computer then you can install following [these steps](https://github.com/obspy/obspy/wiki#installation). I recommend installation via [Anaconda](https://github.com/obspy/obspy/wiki/Installation-via-Anaconda).

For this tutorial, you can install all the necessary libraries using the environment file: <a href="{{site.url}}{{site.baseurl}}/downloads/earthinversion_env.yml" download="Codes">
<img src="https://img.icons8.com/carbon-copy/100/000000/download-2.png" alt="seismicSection" width="40" height="40">
</a>

For installing the environment with all the libraries:

```
conda env create -f earthinversion_env.yml
```

Then you can activate the environment:

```
conda activate earthinversion
```

### Downloading waveform data for a particular station

Obspy can download waveform data from open-access data centers using the specified details. For this example, we arbitrarily select the recent major earthquake ["2020-10-19 Mww7.6 South Of Alaska"](https://ds.iris.edu/ds/nodes/dmc/tools/event/11327190). We select the station: IU.TATO (Taipei, Taiwan).

First we import all the necessary modules:

```python
from obspy import read
from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import matplotlib.pyplot as plt
```

Then we set `IRIS` as our client for downloading data. There are several other data clients available. For more visit [this page](https://docs.obspy.org/packages/obspy.clients.fdsn.html).

```python
client = Client(
   "IRIS"
)
```

Now, let us select a station for downloading the data. In practice you may wanna select the event first and then search for all the available stations for that event. We will look into that case later.

```python
net = "IU"  # network of the station
sta = "TATO"  # station code
loc = "00"  # to specify the instrument at the station
chan = "BHZ"
```

Let us download the data for 2020-10-19 [Mww7.6 South Of Alaska earthquake](https://ds.iris.edu/wilber3/find_stations/11327190). We can specify the event using the time range within which the event falls. Obspy uses `UTCDateTime` module for that (not to be confused with the `datetime`. module, which has similar functions.

We first define the event time and then define the start and end time of the waveforms to request. Here, we will request waveforms one minute before the origin time and 15 minutes after the origin time.

```python
eventTime = UTCDateTime("2020-10-19T20:54:39")
starttime = eventTime - 60  # 1 minute before the event
endtime = eventTime + 15 * 60  # 15 minutes after the event
```

Now, we download the waveforms and store it into a `Stream` object. Streams are list-like objects which contain multiple `Trace` objects, i.e. gap-less continuous time series and related header/meta information.

```python
myStream = client.get_waveforms(net, sta, loc, chan, starttime, endtime)
print(myStream)
```

```
1 Trace(s) in Stream:
IU.TATO.00.BHZ | 2020-10-19T20:53:39.019538Z - 2020-10-19T21:09:38.969538Z | 20.0 Hz, 19200 samples
```

We can see that the stream contains one trace because we requested only one waveforms corresponding to one channel. Next, we would like to inspect the contents of this stream. We can have quick interactive plot of the stream using the `plot` method.

```python
myStream.plot()
```

If you want to save the plot, you can redirect the plot to file using the `outfile` argument. We can also select the `starttime` and `endtime` of the plot to hide other parts in the original waveform. Besides, we can perform several other modifications using the arguments in the plot method.

```python
myStream.plot(
    outfile="myStream.png",
    starttime=None,
    endtime=None,
    size=(800, 250),
    dpi=100,
    color="blue",
    bgcolor="white",
    face_color="white",
    transparent=False,
    number_of_ticks=6,
    tick_rotation=45,
    type="relative",
    linewidth=0.5,
    linestyle="-",
)
```

Obspy can output into formats such as png, pdf, ps, eps and svg. The `type` argument specifies the type of plot. There are several type of the plot in Obspy but in general there are two: normal or relative. The different is in the x-axis display of time.

{% include google-adsense-display-ad-horizontal.html %}

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/obspy-part-I/myStream.png">
</p>

Next step is to write the downloaded data into a file for later use. We can do this using the `write` method of `stream` object.

```python
myStream.write("myStream.mseed", format="MSEED")
```

Obspy supports several other [file formats](https://docs.obspy.org/packages/autogen/obspy.core.stream.Stream.write.html#supported-formats).

## Complete script for downloading data and plotting

 <script src="https://gist.github.com/earthinversion/5a05d08c4f80284b2c81595f6e1179d4.js"></script>

## Complete script for downloading all broadband components

<script src="https://gist.github.com/earthinversion/e983c9b3c9bb12e00a48c7d892cd4546.js"></script>


