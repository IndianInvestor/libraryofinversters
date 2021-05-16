---
title: "Genetic Algorithm: a highly robust inversion scheme for geophysical applications (codes included)"
date: 2021-03-06
tags:
  [
    Genetic Algorithm,
    optimization,
    earthquake location problem,
    coffee cup size problem,
  ]
excerpt: "An introduction to the basics of genetic algorithm along  with a simple numerical example and solution of an earthquake location problem"
mathjax: "true"
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/intro-genetic-algorithm/killer-mosquito.webp"
classes:
  - wide
sidebar:
  nav: "all_posts_list"
category: geophysics
---

{% include toc %}

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4679544.svg)](https://doi.org/10.5281/zenodo.4679544)

## What is Optimization?

- “ The selection of a best element (with regard to some criteria) from some set of available alternatives” {Source: Wikipedia}
- Picking the “best” option from several ways of accomplishing the same task.
- We require a model which can give us the best result.

{% include google-adsense-inarticle.html %}

<figure>
 <img width="815" height="387" style="zoom: 60%;" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/intro-genetic-algorithm/best-route-finding-result.webp" alt="finding best routes">
  <figcaption>Optimum Route</figcaption>
</figure>

## Global vs. Local Optimization

Consider a hypothetical multi-modal function:

{% include google-adsense-inarticle.html %}

<img width="1610" height="1840" style="zoom: 60%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/lsq_method/fig2.jpg">
<figure>
  <figcaption>Hypothetical objective functions with global and local minima.</figcaption>
</figure>

## Genetic Algorithm

Genetic algorithm (GA), first proposed by John Holland in 1975 and described in Goldberg (1988), is based on analogies with biological evolution processes. The principle of GA is quite simple and mirrors what is perceived to occur in evolutionary mechanisms. The idea is to start with a given set of feasible trial solutions (either constrained or unconstrained) and iteratively evaluate objective (or fitness) function by keeping only those solutions that give the optimal value of the objective function and randomly mutate them to try and do even better and successive iterations. Thus, the beneficial mutations (that lead to optimal values) are kept while those that perform poorly are thrown away, i.e., the survival of the fittest.

Consider the unconstrained optimization problem with the objective function, \\(min f(\vec{x})\\) where \\(\vec{x}\\) is an (n) dimensional vector. Suppose \\(m\\) initial guesses are given for the values of \\(\vec{x}\\) so that

\begin{equation}
\label{eq:costFunc}
\begin{split}
guess \quad \textrm{j} \quad \textrm{is} \quad x_j
\end{split}
\end{equation}

Thus \\(m\\) solutions are evaluated and compared with each other in order to see which of the solutions generate the smallest objective function since our goal (in general) is to minimize it. We can order the guesses such that the first (p < m) give the smallest values of \(f (\vec{x})\). Arranging our data, we have

\begin{equation}
\label{eq:eq2}
\begin{split}
keep \quad x_j \quad \textrm{j} = 1,2,...,𝑝 .
\end{split}
\end{equation}

\begin{equation}
\begin{split}
keep \quad x_j \quad \textrm{𝑗} = 1,2,...,𝑝
\end{split}
\end{equation}

\begin{equation}
\begin{split}
discard \quad x_𝑗 = 𝑝+1,𝑝+2,...,𝑚
\end{split}
\end{equation}
Since the first \\(p\\) solutions are the best, these are kept in the next generation. In addition, we now generate \\(m-p\\) new trial solutions that are randomly mutated from the \\(p\\) best solutions. This process is repeated through a finite number of iterations with the hope that convergence to the optimal solution is achieved.

### Scheme

{% include google-adsense-inarticle.html %}

The steps involved in the Genetic Algorithm are:

1.  The initial population of model parameters is randomly chosen within the given search range.
2.  The simple GA undergoes a set of operations on the model population to produce the next generation: selection, coding, crossover, and mutation.
3.  In the selection scheme, the model parameters exhibiting the higher fitness value (lower objective function value relative to others) are selected and replicated with the given probability. The total population size remains constant; then, the population members are randomly paired among themselves.
4.  In the coding scheme, each population's decimal values are converted to a binary system, forming a long bit string (analogous to a chromosome).
5.  In the crossover scheme, some part of the long bit string of binary model parameters is exchanged with their corresponding pair to produce a new population.
6.  In the mutation scheme, some randomly selected sites (with a given probability) of the new set of the binary model population are switched.
7.  These sets of operations will continue until some pre-defined termination criteria for the technique are satisfied.

## The Optimum size of a coffee mug for a Café owner?

Here, the objective function is to minimize the loss of the Café owner. Let us make a very simple function for that.

\begin{equation}
\label{eq:mugCostFunc}
\begin{split}
y = 0.2 x^2 +50/x
\end{split}
\end{equation}

where \\(x\\) is the size of the coffee mug. If the coffee mug's size is too small, then the customers may not like it, and if the size is too large, then the owner will have to endure loss, hence the hypothetical function. We assumed that the price of the coffee is fixed.

<img width="1610" height="1840" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/intro-genetic-algorithm/coffee-size-func.webp" style="zoom:50%;" />
<figure>
  <figcaption>The plot of the above function. It has a minimum of 15.0 units.</figcaption>
</figure>

### Solution

Let us solve this iteratively:

#### Generation 1

| SI No. | Init Pop | Init Pop (binary) | Yi     | Yi/sum(Yi) | Weight | Mating Pool |
| ------ | -------- | ----------------- | ------ | ---------- | ------ | ----------- |
| 1      | 4.2      | 00101010          | 15.43  | 0.073      | 2      | 00101010    |
| 2      | 10.1     | 01100101          | 25.35  | 0.121      | 1      | 00101010    |
| 3      | 16.4     | 10100100          | 56.84  | 0.270      | 1      | 01100101    |
| 4      | 23.5     | 11101011          | 112.58 | 0.536      | 0      | 10100100    |

The average fitness in this generation is : `52.55`.

#### Generation 2

{% include google-adsense-inarticle.html %}

| Mating Pool(2)                                                                | Mate | Crrsovr Site | New Pop (bi)                                | New Pop (dec ) | Yi    | Yi/sum(Yi) | Weight | Mating Pool (3)                             |
| ----------------------------------------------------------------------------- | ---- | ------------ | ------------------------------------------- | -------------- | ----- | ---------- | ------ | ------------------------------------------- |
| <span style="color: green;">0010</span><span style="color: blue;">1010</span> | 4    | 4            | <span style="color: green;">00100100</span> | 3.6            | 16.48 | 0.141      | 1      | <span style="color: red;">00101101</span>   |
| <span style="color: red;">00101</span>010                                     | 3    | 5            | <span style="color: red;">00101101</span>   | 4.5            | 15.16 | 0.130      | 2      | <span style="color: red;">00101101</span>   |
| 01100<span style="color: red;">101</span>                                     | 2    | 5            | 01100010                                    | 9.8            | 24.31 | 0.208      | 1      | <span style="color: green;">00100100</span> |
| 1010<span style="color: green;">0100</span>                                   | 1    | 4            | <span style="color: blue;">10101010</span>  | 17.0           | 60.74 | 0.521      | 0      | 01100010                                    |

The average fitness in this generation is `29.17`. We can continue iterating as long as our termination criteria are satisfied. Some of the standard termination criteria are the tolerance value (the difference in the fitness of the generation compared to the previous generation), the maximum number of generations, etc.

### Fitness with generations

{% include google-adsense-inarticle.html %}

<figure>
 <img width="1192" height="976" style="zoom: 60%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/intro-genetic-algorithm/fitness-generations.webp">
  <figcaption>Fitness optimization with generations (lower is better in this case)</figcaption>
</figure>

## Earthquake location using Genetic Algorithm

In this series of earthquake location problems, we have used the Monte Carlo method for the earthquake location that gives us reliable results. The earthquake location problem was introduced in the [previous post](/geophysics/least-squares-method/).

{% assign postTitle0 = "Monte Carlo methods and earthquake location problem" %}
{% assign postLink0 = "/geophysics/monte-carlo-methods-and-earthquake-location/" %}
{% assign postExcerpt0 = "The common geophysical problems most often have multimodal objective function with many possible minima. In this post, we will look into the Monte Carlo methods to solve such a hypothetical earthquake location problem." %}

{% include single-post-ad.html postTitle=postTitle0 postLink=postLink0 postExcerpt=postExcerpt0 %}

Now, I applied GA from the direct search toolbox of MATLAB to find the solution of the best earthquake location parameters for the earthquake problem defined in [previous post](/geophysics/least-squares-method/) for 30 stations. The GA does not improve the solutions but similar to the Monte Carlo method; it allows a large model space to be searched for solutions. I used the lower and upper limits for the search of best parameters as defined in Table 1. After 85 generations of a run and terminated based on the tolerance criterion, the best parameters found by the GA are [2.9750 2.5202 -2.5535 6.6696 -0.0839]. Since GA is a stochastic optimization scheme, it is best practice to make a reasonable number of acceptable solutions and consider its mean as the final solution. For the 50 runs of the GA for the earthquake location problem, the estimated mean and std of the model parameters are shown in Table 2. The difference from the actual model parameters arises because of random noise in the observed arrival time data.

{% include google-adsense-inarticle.html %}

<p align="center"><strong>Table 1:</strong> Lower and upper limits used for the earthquake location problem
 using genetic algorithm</p>

<table align="center" style="width: 100%; display: table; margin: auto;">
<thead>
<tr>
<th>Model Parameter</th>
<th>Min Value</th>
<th>Max Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Earthquake x-coordinate</td>
<td>-3</td>
<td>3</td>
</tr>
<tr>
<td>Earthquake y-coordinate</td>
<td>-3</td>
<td>3</td>
</tr>
<tr>
<td>Earthquake z-coordinate</td>
<td>-3</td>
<td>0</td>
</tr>
<tr>
<td>Velocity</td>
<td>5</td>
<td>7</td>
</tr>
<tr>
<td>Origin Time</td>
<td>-1</td>
<td>1</td>
</tr>
</tbody>
</table>
<figure>
 <img width="2980" height="1304" style="zoom: 60%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/intro-genetic-algorithm/eq-location.webp">
    <figcaption><strong>The estimation of hypothetical earthquake location solution
 using Genetic Algorithm</strong><br>(a) Estimated location of a hypothetical earthquake using Genetic algorithm. The yellow ellipsoid shows the 1𝜎 confidence interval in the hypocenter location. (b) Fitness value versus generations. The best score value (0.106) and mean score (0.106) versus generation for estimating earthquake location parameters using genetic algorithm scheme.</figcaption>
</figure>

{% include google-adsense-inarticle.html %}


<p align="center"><strong>Table 2:</strong> Estimated model parameters for earthquake location using genetic
algorithm after 50 runs</p>

<table align="center" style="width: 100%; display: table; margin: auto;">
<thead>
<tr>
<th>Model Parameter</th>
<th>Estimated Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Earthquake x-coordinate</td>
<td>2.79 ± 0.15</td>
</tr>
<tr>
<td>Earthquake y-coordinate</td>
<td>2.35 ± 0.13</td>
</tr>
<tr>
<td>Earthquake z-coordinate</td>
<td>−2.11 ± 0.34</td>
</tr>
<tr>
<td>Velocity</td>
<td>6.87 ± 0.18</td>
</tr>
<tr>
<td>Origin Time</td>
<td>0±0.06</td>
</tr>
</tbody>
</table>

```matlab
lower=[-3 -3 -3 5 -1];
upper=[3 3 0 7 1];
options = optimoptions('ga','PlotFcn', @gaplotbestf,'Display','iter'); 6. x=ga(@(pp)fit_arrival_times(pp),5,[],[],[],[],lower,upper,[],options)

function E=fit_arrival_times(pp)
filename = 'arrival_times.csv';
[dobs, dpre] = read_arrivaltimes(filename);

stationlocations = read_stnloc('station_locations.csv', 2, 31);
d_pre = zeros(length(stationlocations),1);

for i=1:length(stationlocations)
    dist = sqrt((pp(1) - stationlocations(i,1))^2 + (pp(2) - stationlocations( i,2))^2 + (pp(3) - stationlocations(i,3))^2);
    arr = dist/pp(4) + pp(5);
    d_pre(i) = arr;
end
E=sum((dobs-d_pre).^2);
```

{% include google-adsense-inarticle.html %}

## Complete codes

Complete codes can be downloaded from my [github repository](https://github.com/earthinversion/PhD-Thesis-codes/tree/master/Genetic-algorithm)
