---
title: "Computing cross-correlation and spectrogram of two seismic traces (codes included)"
date: 2021-05-04
tags:
  [matplotlib, python, obspy, time-frequency analysis, obspy]
excerpt: "Read the seismic traces from the miniseed files and compute the cross-correlation and spectrogram"
mathjax: "true"
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/mseed-xcorr-spectrogram/spectrogram_layout1.png"
classes:
  - wide
sidebar:
  nav: "all_posts_list"
  subscribe_btn: "show"
category: techniques
---

{% include toc %}

I want to compute the relation between two seismic traces using the [cross-correlation](/geophysics/computing-cross-correlation-between-seismograms/). First I compute the spectrogram of each trace using the `spectrogram` method in Obspy. Then, I cross-correlate the two seismic traces and plot its time-domain cross-correlation function and spectrogram.

For details on how to compute [cross-correlation](/geophysics/computing-cross-correlation-between-seismograms/), visit my previous post:

{% assign postLink0 = "https://www.facebook.com/earthinversionwebsite/posts/121911240003810" %}
{% include facebook_postads.html postLink=postLink0 %}

## Compute and plot spectrogram of each traces

I have a mseed file `all_stream_HLZ_20071215_080316.mseed` that contains multiple traces. I used the first two traces for this study. 
For plotting the time series, I first read the data using the `read` function from Obspy and then plot the "data" and "times" methods avilable for the `Trace` object.


```python
from obspy import read
from obspy import read, Trace, UTCDateTime
import numpy as np
import pandas as pd
import noise
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [10,6]
plt.rcParams.update({'font.size': 18})
plt.style.use('seaborn')

filenameZ = 'all_stream_HLZ_20071215_080316.mseed'
fignameTrace = 'spectrogram_layout1.png'
figxcorr = 'spectrogram_layout2.png'
figxcorr2 = 'spectrogram_layout3.png'
st = read(filenameZ)
tr1 = st[0]
tr2 = st[1]

sta1 = tr1.stats['station']

fig, axx = plt.subplots(2,2, sharex=True, sharey='row')
axx[0, 0].plot(tr1.times(), tr1.data, 'k-', linewidth=0.2, label=tr1.stats['station'])
axx[0, 1].plot(tr2.times(), tr2.data, 'k-', linewidth=0.2, label=tr2.stats['station'])
axx[0, 0].set_title(f'Trace 1')
axx[0, 1].set_title(f'Trace 2')
axx[0, 0].set_ylabel('Amplitude')

tr1.spectrogram(log=True, wlen=50,show=False, axes=axx[1, 0], cmap='jet', samp_rate=tr1.stats.sampling_rate)
tr2.spectrogram(log=True, wlen=50,show=False, axes=axx[1, 1], cmap='jet', samp_rate=tr2.stats.sampling_rate)
axx[1, 0].set_title('Spectrogram 1')
axx[1, 1].set_title('Spectrogram 2')
axx[1, 0].set_xlabel('time (s)')
axx[1, 1].set_xlabel('time (s)')
axx[1, 0].set_ylabel('Amplitude')
plt.tight_layout()

## put legend
for col in axx[0,:]:
    ll = col.legend(loc=1)
    plt.setp(ll.get_texts(), color='red') #color legend

plt.savefig(fignameTrace, bbox_inches='tight', dpi=300)
plt.close('all')
```

{% include image_ea.html url="mseed-xcorr-spectrogram/spectrogram_layout1.png" description="Plot of the seismic traces and their corresponding spectrograms" %}


## Compute the cross correlation using the Pandas library

For computing the cross-correlation, I use the `crosscorr` function. Readers can refer to this function in [this post](https://www.earthinversion.com/geophysics/computing-cross-correlation-between-seismograms/). The steps for computing the cross-correlation is also very similar as the [previous post](https://www.earthinversion.com/geophysics/computing-cross-correlation-between-seismograms/). 

However, I obtained the spectrogram using the `spectrogram` method of Obspy. This method is well optimized for seismic data. There are several other spectrogram functions available in Python and most of them work in the same way. The obtained spectrogram for this post is using window length for fft of 50 seconds (`wlen`), and output the frequencies in logarithmic scale.

```python
### Cross Correlation using Pandas
series1, series2 = pd.Series(tr1.data),  pd.Series(tr2.data)
window = 1
maxlag = 500
lags = np.arange(-(maxlag), (maxlag), window)  # contrained
rs = np.nan_to_num([crosscorr(series1, series2, lag) for lag in lags])

traceCCF2 = Trace()
traceCCF2.data = rs
traceCCF2.times(reftime=tr1.stats.starttime)

fig, axx = plt.subplots(2,1)
axx[0].plot(lags, rs, 'k', linewidth=0.5)
axx[0].set_title('Cross Correlation')

traceCCF2.spectrogram(log=True, wlen=50,show=False, axes=axx[1], cmap='jet')
axx[1].set_title('Spectrogram')
plt.tight_layout()
plt.savefig(figxcorr2, bbox_inches='tight', dpi=300)
plt.close('all')
```

{% include image_ea.html url="mseed-xcorr-spectrogram/spectrogram_layout3.png" description="Spectrogram plot of the time series" %}