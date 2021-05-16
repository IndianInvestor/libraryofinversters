---
title: "Time Series Analysis in Python: Filtering or Smoothing Data (codes included)"
date: 2020-10-21
tags: [lowpass filter, smoothing, data analysis, python]
classes:
  - wide
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/time-series-analysis-filtering.png"
sidebar:
  nav: "all_posts_list"
category: techniques
---

In this post, we will see how we can use Python to [low-pass filter](/techniques/signal-denoising-using-fast-fourier-transform/#perform-fast-fourier-transform) the 10 year long daily fluctuations of GPS time series. We need to use the “Scipy” package of Python.

The only important thing to keep in mind is the understanding of Nyquist frequency. The Nyquist or folding frequency half of the sampling rate of the discrete signal. To understand the concept of [Nyquist frequency and aliasing](/techniques/signal-denoising-using-fast-fourier-transform/), the reader is advised to visit this post. For [filtering](/techniques/signal-denoising-using-fast-fourier-transform/) the time-series, we use the fraction of Nyquist frequency (cut-off frequency).

{% assign postLink0 = "https://www.facebook.com/earthinversionwebsite/posts/120387736822827" %}
{% include facebook_postads.html postLink=postLink0 %}

{% include toc %}

## Code Description

Following are the codes and line by line explanation for performing the [filtering](/techniques/signal-denoising-using-fast-fourier-transform/) in a few steps:

### Import Libraries

- import [`numpy`](https://www.earthinversion.com/utilities/introduction-to-scientific-computing-using-numpy-python/) module for efficiently executing numerical operations
- import the `pyplot` from the [matplotlib](/techniques/advanced-2D-plots-with-matplotlib/) library
- predefine figure window size, and default figure settings
- use [matplotlib](/techniques/advanced-2D-plots-with-matplotlib/) `ggplot` style. I personally like to use "ggplot" style of graph for my work but it depends on the user's preference whether they wanna use it.

{% assign postLink0 = "https://www.facebook.com/earthinversionwebsite/posts/113134847548116" %}
{% include facebook_postads.html postLink=postLink0 %}


```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from matplotlib import rcParams
rcParams['figure.figsize'] = (10.0, 6.0) #predefine the size of the figure window
rcParams.update({'font.size': 14}) # setting the default fontsize for the figure
rcParams['axes.labelweight'] = 'bold' #Bold font style for axes labels
from matplotlib import style
style.use('ggplot')
```

### Load data

We load the data in the mat format (skipped) but this code will work for any sort of time series. If you have MiniSeed data, you can easily [convert that to the MATLAB or mat format](/utilities/converting-mseed-data-to-mat-and-analyzing-in-matlab/) using the following utility:
{% assign postLink0 = "https://www.facebook.com/earthinversionwebsite/posts/119749130220021" %}
{% include facebook_postads.html postLink=postLink0 %}

{% include google-adsense-inarticle.html %}

```python
# loading data part skipped (can be done using scipy for mat format data)
dN=np.array(data['dN'])
dE=np.array(data['dE'])
dU=np.array(data['dU'])
slat=np.array(data['slat'])[0]
slon=np.array(data['slon'])[0]
tdata=np.array(data['tdata'])[0]
stn_name=np.array(stn_info['stn_name'])[0]
stns=[stn_name[i][0] for i in range(len(stn_name))]
```

### Visualizing the original and the Filtered Time Series

```python
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
indx=np.where( (tdata > 2012) & (tdata < 2016) )
ax.plot(tdata[indx],dU[indx,0][0],'k-',lw=0.5)
```

### Filtering of the time series

```python
fs=1/24/3600 #1 day in Hz (sampling frequency)

nyquist = fs / 2 # 0.5 times the sampling frequency
cutoff=0.1 # fraction of nyquist frequency, here  it is 5 days
print('cutoff= ',1/cutoff*nyquist*24*3600,' days') #cutoff=  4.999999999999999  days
b, a = signal.butter(5, cutoff, btype='lowpass') #low pass filter


dUfilt = signal.filtfilt(b, a, dU[:,0])
dUfilt=np.array(dUfilt)
dUfilt=dUfilt.transpose()
```

- Continue plotting on the exisitng figure window

```python
ax.plot(tdata[indx],dUfilt[indx],'b',linewidth=1)

ax.set_xlabel('Time in years',fontsize=18)
ax.set_ylabel('Stations',fontsize=18)
plt.savefig('test.png',dpi=150,bbox_inches='tight')
```

## Complete Script:

<script src="https://gist.github.com/earthinversion/bc4900b3c51afc72c7566b6a3c0fca4b.js"></script>

{% assign postLink0 = "https://www.facebook.com/earthinversionwebsite/posts/108717261323208" %}
{% include facebook_postads.html postLink=postLink0 %}

## Output Figure:

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/time-series-analysis-filtering.png">
</p>

{% include google-adsense-inarticle.html %}

This post was last modified at {{ "now" | date: "%Y-%m-%d %H:%M" }}.


