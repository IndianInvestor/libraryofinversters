---
title: "The easy way to compute and visualize the time & frequency domain correlation (codes included)"
date: 2021-2-16
tags: [seismology, time-frequency analysis, python]
excerpt: "In geophysics, it is important to understand and identify the complex and unknown relationships between two time-series. Cross-correlation is an established and reliable tool to compute the degree to which the two seismic time-series are dependent on each other."
mathjax: "true"
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/geophysical-cross-correlation/pexels-burak-k-186461.jpg"
classes:
  - wide
sidebar:
  nav: "all_posts_list"
category: geophysics

---

{% include toc %}



## Introduction

Cross-correlation is an established and reliable tool to compute the degree to which the two seismic time-series are dependent on each other. Several studies have relied on the cross-correlation method to obtain the inference on the seismic data. For details on cross-correlation methods, we refer the reader to previous works [see references].

It is essential to understand and identify the complex and unknown relationships between two time-series for obtaining meaningful inference from our data. In this post, we will take the geophysical data for understanding purposes. For general readers, I recommend to ignore the field specific examples and stay along, as the concept of correlation is mathematical and can be applied on data related to any field.

{% include google-adsense-inarticle.html %}

<figure>
 <img width="2647" height="1515" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/geophysical-cross-correlation/pexels-burak-k-186461.jpg" alt="">
  <figcaption>Photo by Burak K from Pexels</figcaption>
</figure>

In seismology, several applications are based on finding the time shift of one time-series relative to other such as ambient noise [cross-correlation](/geophysics/computing-cross-correlation-between-seismograms/) (to find the empirical Green's functions between two recording stations), inversion for the source (e.g., gCAP) and structure studies  (e.g., full-waveform inversion), template matching etc. 

In this post, we will see how we can compute [cross-correlation](/geophysics/computing-cross-correlation-between-seismograms/) between seismic time-series and extract the time-shift information of the relation between the two seismic signals in the time and frequency domain.

## Time domain cross-correlation function

The correlation between two-stochastic processes A and B (expressed in terms of time-series as \\(A(t)\\) and \\(B(t)\\)) can be expresses as  (see ref. 1):

\begin{equation}
\label{eq:square}
\begin{split}
\rho (\tau) = \frac{\sum_i A(t_i-\tau) B(t_i)}{[\sum_i A(t_i)^2\sum_iB(t_i)^2]^{1/2}}
\end{split}
\end{equation}

The above equation is the sample [cross-correlation](/geophysics/computing-cross-correlation-between-seismograms/) function between two time-series with a finite time shift \\(\tau\\). It is important to note that the correlation \\(\rho\\) by its face value alone does not dictate whether or not the correlation in question is significant, unless the *degrees of freedom* (DOF) of the processes, which signifies the information content (or entropy), is also specified (see Chao and Chung, 2019 for details).

{% include google-adsense-inarticle.html %}

## Compute Cross-correlation

Let us now look into how we can compute the time domain cross correlation between two time series. For this task, I arbitrarily took two seismic velocity time-series:

### Arbitrarily selected data

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from synthetic_tests_lib import crosscorr


time_series = ['BO.ABU', 'BO.NOK']
dirName = "data/"
fs = 748  # take 748 samples only
MR = len(time_series)
Y = np.zeros((MR, fs))
dictVals = {}
for ind, series in enumerate(time_series):
    filename = dirName + series + ".txt"
    df = pd.read_csv(filename, names=[
                     'time', 'U'], skiprows=1, delimiter='\s+')  # reading file as pandas dataframe to work easily

    # this code block is required as the different time series has not even sampling, so dealing with each data point separately comes handy
    # can be replaced by simply `yvalues = df['U]`
    yvalues = []
    for i in range(1, fs+1):
        val = df.loc[df['time'] == i]['U'].values[0]
        yvalues.append(val)

    dictVals[time_series[ind]] = yvalues


timeSeriesDf = pd.DataFrame(dictVals)
```

The above code reads the txt file containing the vertical component located in the directory (`dirName`) and trim the data for arbitraily taken `fs` samples. We can read each `txt` file interatively and save the data column into a dictionary. This dictionary is next converted into [pandas](/utilities/how-to-start-using-pandas-immediately-for-earth-data-analysis/) dataframe to avail all the tools in pandas library.
The above code reads the txt file containing the vertical component located in the directory (`dirName`) and trim the data for arbitraily taken `fs` samples. We can read each `txt` file interatively and save the data column into a dictionary. This dictionary is next converted into [pandas](/utilities/how-to-start-using-pandas-immediately-for-earth-data-analysis/) dataframe to avail all the tools in pandas library.

Please note that there are several different ways to read the data and preference of that way depends on the user and the data format.

{% include google-adsense-inarticle.html %}

To plot the time-series, I used `matplotlib`.

```python
# plot time series
# simple `timeSeriesDf.plot()` is a quick way to plot
fig, ax = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
ax[0].plot(timeSeriesDf[time_series[0]], color='b', label=time_series[0])
ax[0].legend()
ax[1].plot(timeSeriesDf[time_series[1]], color='r', label=time_series[1])
ax[1].legend()
plt.savefig('data_viz.jpg', dpi=300, bbox_inches='tight')
plt.close('all')
```

{% include google-adsense-inarticle.html %}

<figure>
 <img width="2647" height="1515" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/geophysical-cross-correlation/data_viz.webp" alt="data preview">
  <figcaption>Data Visualization</figcaption>
</figure>

### Compute the cross-correlation in time-domain

```python
d1, d2 = timeSeriesDf[time_series[ind1]], timeSeriesDf[time_series[ind2]]
window = 10
# lags = np.arange(-(fs), (fs), 1)  # uncontrained
lags = np.arange(-(200), (200), 1)  # contrained
rs = np.nan_to_num([crosscorr(d1, d2, lag) for lag in lags])

print(
    "xcorr {}-{}".format(time_series[ind1], time_series[ind2]), lags[np.argmax(rs)], np.max(rs))

```

In the above code, I have used the `crosscorr` function to compute the correlation between the pair of time-series for a series of lag values. The lag values has been contrained between -200 to 200 to avoid artifacts.

```python
# Time lagged cross correlation
def crosscorr(datax, datay, lag=0):
    """ Lag-N cross correlation. 
    Shifted data filled with NaNs 

    Parameters
    ----------
    lag : int, default 0
    datax, datay : pandas.Series objects of equal length
    Returns
    ----------
    crosscorr : float
    """
    return datax.corr(datay.shift(lag))

```

Here, as you can notice that the `crosscorr` makes use of the [pandas `corr` method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html) and hence, the `d1` and `d2` is required to be pandas Series object. 

I obtained the correlation between the above pair of time-series to be `0.19`with a lag of `36`.

{% include google-adsense-inarticle.html %}

```
xcorr BO.ABU-BO.NOK 36 0.19727959397327688
```

<figure>
 <img width="2647" height="1515" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/geophysical-cross-correlation/data_xcorr.webp" alt="data cross-correlation in time domain">
  <figcaption>Time-domain cross-correlation of arbitraily taken real time-series</figcaption>
</figure>

{% include google-adsense-inarticle.html %}

### Frequency-domain approach of cross-correlation for obtaining time shifts



```python
shift = compute_shift(
    timeSeriesDf[time_series[ind1]], timeSeriesDf[time_series[ind2]])

print(shift)
```

This gives:

```
-36
```

Where, the function `compute_shift` is simply:

```python
def cross_correlation_using_fft(x, y):
    f1 = fft(x)
    f2 = fft(np.flipud(y))
    cc = np.real(ifft(f1 * f2))
    return fftshift(cc)

def compute_shift(x, y):
    assert len(x) == len(y)
    c = cross_correlation_using_fft(x, y)
    assert len(c) == len(x)
    zero_index = int(len(x) / 2) - 1
    shift = zero_index - np.argmax(c)
    return shift
```

{% include google-adsense-inarticle.html %}

Here, the shift of `shift` means that `y` starts `shift` time steps before `x`.



### Generate synthetic pair of time series

Although the results obtained seems plausible, as we used the arbitrary pair of real time series, we do not know if we have obtained the correct results. So, we apply the above methods on synthetic pair of time-series with known time-shifts.

{% include google-adsense-inarticle.html %}

Let us use the `scipy.signal` fucntion to  generate two unit impulse function. We then apply low pass filter of order 4 and with center frequency of 0.2 to smoothen the edges (Note that the results will be same even without the filter).

```python
# Delta Function
length = 100
amp1, amp2 = 1, 1
x = np.arange(0, length)
to = 10
timeshift = 30
t1 = to+timeshift
series1 = signal.unit_impulse(length, idx=to)
series2 = signal.unit_impulse(length, idx=t1)

# low pass filter to smoothen the edges (just to make the signal look pretty)
b, a = signal.butter(4, 0.2)
series1 = signal.lfilter(b, a, series1)
series2 = signal.lfilter(b, a, series2)

fig, ax = plt.subplots(2, 1, figsize=(8, 6), sharex=False)

ax[0].plot(x, series1, c='b', lw=0.5)
ax[0].axvline(x=to, c='b', lw=0.5,
              ls='--', label=f'x={to}')
ax[0].plot(x, series2+0.1, c='r', lw=0.5)
ax[0].axvline(x=to+timeshift, c='r', lw=0.5,
              ls='--', label=f'x={to+timeshift}')
ax[0].set_yticks([0, 0.1])
ax[0].legend()
ax[0].set_yticklabels(['Series 1', 'Series 2'], fontsize=8)

d1, d2 = pd.Series(series2), pd.Series(series1)
lags = np.arange(-(50), (50), 1)

rs = np.nan_to_num([crosscorr(d1, d2, lag) for lag in lags])
maxrs, minrs = np.max(rs), np.min(rs)
if np.abs(maxrs) >= np.abs(minrs):
    corrval = maxrs
else:
    corrval = minrs

ax[1].plot(lags, rs, 'k', label='Xcorr (s1 vs s2), maxcorr: {:.2f}'.format(
    corrval), lw=0.5)
# ax[1].axvline(x=timeshift, c='r', lw=0.5, ls='--')
ax[1].axvline(x=lags[np.argmax(rs)], c='r', lw=0.5,
              ls='--', label='max time correlation')
ax[1].legend(fontsize=6)
plt.subplots_adjust(hspace=0.25, wspace=0.1)
plt.savefig('xcorr_fn_delta.png', bbox_inches='tight', dpi=300)
plt.close('all')
```

{% include google-adsense-inarticle.html %}

<figure>
 <img width="2083" height="1515" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/geophysical-cross-correlation/xcorr_fn_delta.webp" alt=" cross-correlation in time domain for low-pass filtered unit impulse function">
  <figcaption>Time-domain cross-correlation of low-pass filtered unit impulse function</figcaption>
</figure>

## References

1.  [Chao, B.F., Chung, C.H., 2019. On Estimating the Cross Correlation and Least Squares Fit of One Data Set to Another With Time Shift. Earth Sp. Sci. 6, 1409–1415. https://doi.org/10.1029/2018EA000548](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2018EA000548)
2.  [Robinson, E., & Treitel, S. (1980). *Geophysical signal analysis*. Englewood Cliffs, NJ: Prentice‐Hall.](http://scholar.google.com/scholar_lookup?hl=en&publication_year=1980&author=E.+Robinson&author=S.+Treitel&title=Geophysical+signal+analysis)
3.  [Template matching using fast normalized cross correlation](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/4387/1/Template-matching-using-fast-normalized-cross-correlation/10.1117/12.421129.short?SSO=1)
4.  [Qingkai's Blog: "Signal Processing: Cross-correlation in the frequency domain"](http://qingkaikong.blogspot.com/2016/10/signal-processing-cross-correlation-in.html)
5.  [How to Calculate Correlation Between Variables in Python](https://machinelearningmastery.com/how-to-use-correlation-to-understand-the-relationship-between-variables/)



## Download Codes

{% include google-adsense-inarticle.html %}

All the above codes can be downloaded from my [Github repo](https://github.com/earthinversion/geophysical-cross-correlation.git).

