---
title: "Estimation of the degrees of freedom for time series (codes included)"
date: 2020-12-2
tags: [degrees of freedom, statistics, techniques, time series, python]
excerpt: "Numerical tests to understand the degrees of freedom in time series"
mathjax: "true"
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/estimating_dof/Autocorr_pU.png"
classes:
  - wide
sidebar:
  nav: "all_posts_list"
  subscribe_btn: "show"
category: geophysics
---

{% include toc %}

## Introduction

The correlation between two (real) stochastic processes A and B, which are sampled as two (real) time series, A(t) and B(t) can be written as

$$
\begin{aligned}
\rho (\tau) = \sum_i A(t_i - \tau) B(t_i)/[\sum_i A(t_i)^2 \sum_i B(t_i)^2]^{1/2}
\end{aligned}
$$

A dimensionless number between 1 and −1 (the Cauchy‐Schwarz inequality), the correlation \\(\rho\\) by its face value alone does not dictate whether or not the correlation in question is significant, unless the degrees of freedom (DOF) of the processes, which signifies the information content (or entropy), is also specified. As discussed in the previous post, two time series with predominant linear trends (very low DOF) can have a very high
\\(\rho\\), which can hardly be construed as evidence for a meaningful physical relationship.

{% include google-adsense-inarticle.html %}

A relatively high
\\(\rho\\) for low DOF may be less significant than a relatively low
\\(\rho\\) at high DOF and vice versa.

Given the DOF of processes A and B, what is the probability at which the obtained
\\(\rho\\) can reject the null hypothesis that A and B are actually uncorrelated? The probability
\\(P_c\\)
​
for the correlation value to exceed a certain \\(|\rho|\\) (between 0 and 1) for random samples with DOF =
\\(\nu\\)is given by

$$
\begin{aligned}
P_c(\rho; \nu) = 1/\sqrt(\pi) \frac{\Gamma[(\nu + 1)/2]}{\Gamma (\nu / 2)} \int_{|\rho|}^{1} (1-x^2)^{(\nu - 2)/2} dx
\end{aligned}
$$

where \\(\Gamma (z) = \int\_{0}^{\inf} x^{z−1} e^{−x} dx\\) is the Gamma function. The significance level is 2\\(Pc\\) accounting for both positive and negative \\(\rho\\) values, and the confidence level is 1‐2\\(P_c\\), for given \\(\nu\\).

## How to find the degrees of freedom of time series?

For a Gaussian (white) time series with N independent numbers, the DOF is equal to \\(N-2\\); the loss of 2 degrees of freedom is to account for the specification of the mean and standard deviation. However, the DOF for nonwhite time series is smaller than \\(N-2\\) given to the fact that the sampled values are not completely independent of each other. There are several schemes for the estimation of DOF (for details see Wang et. al., 1999).

We need to apply several statistical analysis of time series to understand variability, regular and irregular oscillations, characteristics of these oscillations,and the physical processes that give rise to each of these oscillations.

{% include google-adsense-inarticle.html %}

Autocorrelation can be used to estimate the dominant periods in the time series. The autocovariance is the covariance of a variable with itself at some other time, measured by a time lag (or lead) \\(\tau\\). The typical autocorrelation function tells us that data points in a time series are not independent from each other. For a time series of red noise, it has been suggested that the degree of freedom can be determined as following (Panofsky and Brier, 1958):

$$
\begin{aligned}
DOF = \frac{N \Delta t}{2T_e}
\end{aligned}
$$

Here \\(T_e\\) is the e-folding decay time of autocorrelation (where autocorrelation drops to \\(1/e\\)). \\(\Delta t\\) is the time interval between data.

We can obtain an estimate of the degrees of freedom of a time series.

```python
from statsmodels.tsa.stattools import acf
from statsmodels.graphics import tsaplots
import matplotlib.pyplot as plt
import numpy as np
from time_series import pU

for i,val in enumerate(acf(pU)):
    if val < 1/np.exp(1):
        print(i,val)
        Te = i
        val_Te = val
        break
dof = (len(pU)*1)/(2*Te)
print(f"Num degrees of freedom is {dof}")
fig = tsaplots.plot_acf(pU, lags=100,alpha=0.05)
plt.plot(Te,val_Te,'bo')
plt.axhline(val_Te,color='b',label='Te')
plt.legend(loc=0)
plt.xlabel('Lags')
plt.ylabel('Correlation')
plt.title(f'Autocorrelation pU, dof = {dof}',fontsize=14)
plt.savefig(f'Autocorr_pU.png',bbox_inches='tight')
plt.close('all')
```

{% include google-adsense-inarticle.html %}

## References

1. Chao, B. F., and C. H. Chung (2019), On Estimating the Cross Correlation and Least Squares Fit of One Data Set to Another With Time Shift, Earth and Space Science, 6(8), 1409–1415, doi:10.1029/2018EA000548.
2. Wang, X., S. S. Shen, X. Wang, and S. S. Shen (1999), Estimation of Spatial Degrees of Freedom of a Climate Field, http://dx.doi.org/10.1175/1520-0442(1999)012<1280:EOSDOF>2.0.CO;2, 12(5), 1280–1291, doi:10.1175/1520-0442(1999)012<1280:EOSDOF>2.0.CO;2.
3. Panofsky, H.A. and Brier, G.W., 1958. Some applications of statistics to meteorology. Mineral Industries Extension Services, College of Mineral Industries, Pennsylvania State University.


