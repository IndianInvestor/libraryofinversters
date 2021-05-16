---
title: "Exploratory Factor Analysis (codes included)"
date: 2020-11-23
tags: [factor analysis, python, factor analysis python example]
excerpt: "Factor Analysis is an exploratory data analysis method used to search influential underlying factors or latent variables from a set of observed variables"
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/exploratory_factor_analysis/fig3.png"
classes:
  - wide
sidebar:
  nav: "all_posts_list"
category: geophysics
---

{% include toc %}

Data with large number of measured variables have the possibility of having some variables to “overlap” due to its inherent dependency. **Factor Analysis (FA)** is an exploratory data analysis method used to search influential underlying factors or latent variables from a set of observed variables. It is a method for investigating whether a number of variables of interest Y1, Y2,..., Yl, are linearly related to a smaller number of unobservable factors F1, F2,..., Fk.

## Data and Methods

We have data for the Individuals entering web-based personality assessment tests for 25 personalities. These 25 variables (A1, A2, …, O5) can be organized by five putative factors: Agreeableness, Conscientiousness, Extraversion, Neuroticism, and Openness.

{% include google-adsense-inarticle.html %}

<p align="center">
  <img width="50%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/exploratory_factor_analysis/factor_variables.png">
</p>

The data for each 25 variables were collected on a 6 point response scale – 1 Very Inaccurate; 2 Moderately Inaccurate; 3 Slightly Inaccurate; 4 Slightly Accurate; 5 Moderately Accurate; 6 Very Accurate.

```python
# Import required libraries
import pandas as pd
from sklearn.datasets import load_iris
from factor_analyzer import FactorAnalyzer
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from factor_analyzer.factor_analyzer import calculate_kmo


matplotlib.rcParams['figure.figsize'] = (10.0, 6.0)

style.use('ggplot')

df= pd.read_csv("bfi.csv")
df.drop(['Unnamed: 0','gender', 'education', 'age'],axis=1,inplace=True)
# Dropping missing values rows
df.dropna(inplace=True)
```

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/exploratory_factor_analysis/fig2.jpg">
</p>

## The Factor Analysis Model

Factor analysis can statistically explain the variance among the observed variable and condense a set of the observed variable into the unobserved variable called factors. Observed variables are modeled as a linear combination of factors and error terms. Each factor explains a particular amount of variance in the observed variables and can help in data interpretations by reducing the number of variables.

{% include google-adsense-inarticle.html %}

<p align="center">
  <img width="60%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/exploratory_factor_analysis/fig3.png">
</p>

## What is the Factor?

The factor is a latent variable that describes the association among the number of observed variables. The maximum number of factors is equal to the number of observed variables. Every factor explains a certain variance in observed variables. The factors with the lowest amount of variance were dropped (source).

## What are factor loadings?

The factor loading is a matrix which shows the relationship of each variable to the underlying factor. It shows the correlation coefficient for the observed variable and factor. It shows the variance explained by the observed variables (source).

## Adequacy Test

Before we perform factor analysis, we need to evaluate the “factorability” of our dataset. Factorability means “can we find the factors in the dataset?”. There are two methods to check the factorability:

1. Bartlett’s Test
2. Kaiser-Meyer-Olkin Test

### Bartlett’s Test

{% include google-adsense-display-ad-horizontal.html %}

Bartlett’s test of sphericity checks whether or not the observed variables intercorrelate at all using the observed correlation matrix against the identity matrix. If the test found statistically insignificant, we should not employ a factor analysis.

```python
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
chi_square_value,p_value=calculate_bartlett_sphericity(df)
chi_square_value, p_value
```

{% include google-adsense-inarticle.html %}

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/exploratory_factor_analysis/fig4.jpg">
</p>

### Kaiser-Meyer-Olkin (KMO) Test

It is a statistic that indicates the proportion of variance in our variables that might be caused by underlying factors. High values (close to 1.0) generally indicate that a factor analysis may be useful with our data. If the value is less than 0.50, the results of the factor analysis probably won’t be very useful.

```python
from factor_analyzer.factor_analyzer import calculate_kmo
kmo_all,kmo_model=calculate_kmo(df)
```

{% include google-adsense-inarticle.html %}

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/exploratory_factor_analysis/fig5.jpg">
</p>

### Choosing the Number of Factors

The eigenvalue is a good criterion for determining the number of factors. Generally, an eigenvalue greater than 1 will be considered as selection criteria for the feature.

```python
# Create factor analysis object and perform factor analysis
fa = FactorAnalyzer()
fa.analyze(df, 25, rotation=None)
# Check Eigenvalues
ev, v = fa.get_eigenvalues()
ev
```

{% include google-adsense-inarticle.html %}

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/exploratory_factor_analysis/fig6.jpg">
</p>

Here, we can see only for 6-factors eigenvalues are greater than one. It means we need to choose only 6 factors (or unobserved variables).

```python
# Create scree plot using matplotlib
plt.scatter(range(1,df.shape[1]+1),ev.values)
plt.plot(range(1,df.shape[1]+1),ev.values)
plt.title('Scree Plot')
plt.xlabel('Factors')
plt.ylabel('Eigenvalue')
plt.axhline(y=1,c='k')
```

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/exploratory_factor_analysis/fig7.jpg">
</p>

## Performing Factor Analysis

{% include google-adsense-display-ad-horizontal.html %}

```python
# Create factor analysis object and perform factor analysis
fa = FactorAnalyzer()
fa.analyze(df, 6, rotation="varimax")
fa.loadings
```

{% include google-adsense-inarticle.html %}

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/exploratory_factor_analysis/fig8.jpg">
</p>

```python
import numpy as np
Z=np.abs(fa.loadings)
fig, ax = plt.subplots()
c = ax.pcolor(Z)
fig.colorbar(c, ax=ax)
ax.set_yticks(np.arange(fa.loadings.shape[0])+0.5, minor=False)
ax.set_xticks(np.arange(fa.loadings.shape[1])+0.5, minor=False)
ax.set_yticklabels(fa.loadings.index.values)
ax.set_xticklabels(fa.loadings.columns.values)
plt.show()
```

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/exploratory_factor_analysis/fig9.jpg">
</p>

- **Factor 1** has high factor loadings for E1,E2,E3,E4, and E5 (Extraversion)

- **Factor 2** has high factor loadings for N1, N2, N3, N4, and N5 (Neuroticism)

- **Factor 3** has high factor loadings for C1,C2,C3,C4, and C5 (Conscientiousness)

- **Factor 4** has high factor loadings for O1,O2,O3,O4, and O5 (Opennness)

- **Factor 5** has high factor loadings for A1,A2,A3,A4, and A5 (Agreeableness)

- **Factor 6** has none of the high loadings for any variable and is not easily interpretable. Its good if we take only five factors.

Let’s perform factor analysis for 5 factors.

```python
# Create factor analysis object and perform factor analysis using 5 factors
fa = FactorAnalyzer()
fa.analyze(df, 5, rotation="varimax")
fa.loadings
```

{% include google-adsense-inarticle.html %}

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/exploratory_factor_analysis/fig10.jpg">
</p>

```python
Z=np.abs(fa.loadings)
fig, ax = plt.subplots()
c = ax.pcolor(Z)
fig.colorbar(c, ax=ax)
ax.set_yticks(np.arange(fa.loadings.shape[0])+0.5, minor=False)
ax.set_xticks(np.arange(fa.loadings.shape[1])+0.5, minor=False)
ax.set_yticklabels(fa.loadings.index.values)
ax.set_xticklabels(fa.loadings.columns.values)
plt.show()
```

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/exploratory_factor_analysis/fig11.jpg">
</p>

Let us now obtain the variance for each factor:

```python
# Get variance of each factors
fa.get_factor_variance()
```

<p align="center">
  <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/exploratory_factor_analysis/fig12.jpg">
</p>

The total cumulative variance explained by the 5 factors is 100\*0.423619 = ~42%.

{% include google-adsense-inarticle.html %}

<iframe src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/exploratory_factor_analysis/eco-environmental-vulnerability-factor-analysis.html" width="100%" height="600"></iframe>

## References:

1. https://www.cs.princeton.edu/~bee/courses/scribe/lec_10_02_2013.pdf
2. https://www.datacamp.com/community/tutorials/introduction-factor-analysis
3. http://www.yorku.ca/ptryfos/f1400.pdf
4. https://www.mathworks.com/help/stats/examples/factor-analysis.html


