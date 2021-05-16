---
title: "Easily integrate Custom Functions in MATLAB with Python (codes included)"
date: 2021-03-05
tags: [MATLAB, eigen functions, matlab engine api, matlab compiler, matlab runtime, python]
excerpt: "How can we use the MATLAB functions in Python? MATLAB implementation are usually reliable as it is developed by the professionals. But the advantages of using Python for scripting is immense."
mathjax: "true"
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/matlab_python/matlabpluspython.webp"
classes:
  - wide
sidebar:
  nav: "all_posts_list"
category: utilities
redirect_from:
  - /geophysics/MATLAB-function-in-Python/
---

{% include toc %}



## Introduction

MATLAB implementation are usually quite reliable as it is developed by the professionals. But the advantages of using Python is immense. In this post, I will show how you can benefit the MATLAB function in your Python script.

## Defining custom function in MATLAB

{% include google-adsense-inarticle.html %}

Let us make a custom function in MATLAB that we can use in Python. For the purpose of demonstration, I will use a very simple function but the same idea applies to any function.

### Eigenvalues and eigenvectors in MATLAB

```matlab
function [V,D] = eigFunc(A)
%returns diagonal matrix D of eigenvalues and matrix V 
% whose columns are the corresponding right eigenvectors, 
% so that A*V = V*D.
[V, D] = eig(A);
end
```

{% include google-adsense-inarticle.html %}

I saved the above function as `eigFunc`. This function takes in a square matrix as input and outputs diagonal matrix `D` of eigenvalues and matrix `V` whose columns are the corresponding right eigenvectors [[see eig function in MATLAB](https://www.mathworks.com/help/matlab/ref/eig.html)].

Let's first use this function in MATLAB for test purpose.

```matlab
clear; close all; clc
A = gallery('lehmer',4);

[V,D] = eigFunc(A)

```

This returns:

```
V =

    0.0693   -0.4422   -0.8105    0.3778
   -0.3618    0.7420   -0.1877    0.5322
    0.7694    0.0486    0.3010    0.5614
   -0.5219   -0.5014    0.4662    0.5088


D =

    0.2078         0         0         0
         0    0.4078         0         0
         0         0    0.8482         0
         0         0         0    2.5362
```

This works great in MATLAB as expected (coz the function is exact copy of the `eig` function in MATLAB. But how can we use this function in Python?

{% assign postTitle0 = "Time-Frequency Analysis in MATLAB" %}
{% assign postLink0 = "/geophysics/time-frequency-analysis-in-matlab/" %}
{% assign postExcerpt0 = "A signal has one or more frequency components in it and can be viewed from two different standpoints: time-domain and frequency domain. In general, signals are recorded in time-domain but analyzing signals in frequency domain makes the task easier. For example, differential and convolution operations in time domain become simple algebraic operation in the frequency domain" %}

{% include single-post-ad.html postTitle=postTitle0 postLink=postLink0 postExcerpt=postExcerpt0 %}

## Call MATLAB in Python

### Using MATLAB Engine API for Python

The easiest way to use the matlab function in Python is by using the `matlab.engine`. You can install `matlab` library by following these two ways. 

{% include google-adsense-inarticle.html %}

#### Install from inside MATLAB:

```matlab
cd (fullfile(matlabroot,'extern','engines','python'))
system('python setup.py install')
```

#### Install directly from terminal:

Navigate to the MATLAB source location and compile the python

```
python setup.py install
```

Please note that this MATLAB engine API will be installed for the the specific version of `python`. If you are using anaconda, you can inspect the version of Python you are installing the MATLAB engine API for. It is essentially the same way you install other Python libraries. For details, visit [here](https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html).

{% include google-adsense-inarticle.html %}

```python
import matlab
import matlab.engine
eng = matlab.engine.start_matlab()
A = [[1.0000,    0.5000,    0.3333,    0.2500],
     [0.5000,    1.0000,    0.6667,    0.5000],
     [0.3333,    0.6667,    1.0000,    0.7500],
     [0.2500,    0.5000,    0.7500,    1.0000]]
A = matlab.double(A)
V, D = eng.eigFunc(A, nargout=2)
print("V: ", V)
print("D: ", D)

eng.quit()
```

Here is the output:

```
V:  [[0.06939950784450351,-0.4421928183150595,-0.8104910184495989,0.37782737957175255],				[-0.3619020163563876,0.7419860358173743,-0.18770341448628555,0.5322133795757004],[0.7693553355549393,0.04873539080548356,0.30097912769034274,0.5613633351323756],[-0.5218266058004974,-0.5015447096377744,0.4661365700065611,0.5087893432606572]]

D:  [[0.20775336892808516,0.0,0.0,0.0],[0.0,0.40783672775946245,0.0,0.0],[0.0,0.0,0.8482416513967358,0.0],[0.0,0.0,0.0,2.536168251915717]]
```

The results are same as before. The `nargout` argument tells the matlab based function to output `2` results here.

{% assign postTitle0 = "Test your scientific hypothesis in MATLAB" %}
{% assign postLink0 = "/statistics/hypothesis-testing/" %}
{% assign postExcerpt0 = "Numerical validation of hypothesis: Is the mean of one population significantly different than the other?" %}

{% include single-post-ad.html postTitle=postTitle0 postLink=postLink0 postExcerpt=postExcerpt0 %}

## Create Python Package: Using MATLAB Compiler & MATLAB Runtime

This is all well and good if you have MATLAB installed in your system. But what if you wanna give your Python script so someone who does not have MATLAB installed on their system. In that case, you can build a Python library using the `library compiler` app in MATLAB. For details, visit [Generate a Python Package and Build a Python Application](https://www.mathworks.com/help/compiler_sdk/gs/create-a-python-application-with-matlab-code.html).



<figure class="half">
 <img width="3584" height="2240" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/matlab_python/click-lib-compiler.webp"  alt="select library compiler app in matlab">
 <img width="3584" height="2240" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/matlab_python/fill-in-lib-information.webp"  alt="fill in information">
 <figcaption>(a) Select library compiler app in MATLAB (b) Fill in information regarding the Python library</figcaption>
</figure>

{% include google-adsense-inarticle.html %}

<figure class="half">
 <img width="3584" height="2240" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/matlab_python/select-matlab-function.webp"  alt="select library compiler app in matlab">
 <img width="3584" height="2240" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/matlab_python/add-example-script.webp"  alt="Add example MATLAB script">
 <figcaption>(a) Select MATLAB function to generate the Python library (b) Add example MATLAB script </figcaption>
</figure>

{% include google-adsense-inarticle.html %}

<figure class="half">
 <img width="3584" height="2240" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/matlab_python/package-application.webp"  alt="Click to package application">
 <img width="3584" height="2240" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/matlab_python/wait-for-packaging.webp"  alt="Wait for the python library to generate">
    <figcaption>(a) Click on <code>package</code> to generate standalone component (b) Wait for the task to finish </figcaption>
</figure>



#### MATLAB Runtime installation

Please note that, the user need to install MATLAB runtime for successfully using this library. MATLAB runtime helps in running compiled MATLAB applications or components without installing MATLAB. The runtime can be downloaded from [here](https://www.mathworks.com/products/compiler/matlab-runtime.html) for Windows, Mac and Linux OS and it is free to download.

#### Import MATLAB based library for Python

```matlab
import eigFunc
eigFuncAnalyzer = eigFunc.initialize() #calls the matlab runtime
A = [[1.0000,    0.5000,    0.3333,    0.2500],
     [0.5000,    1.0000,    0.6667,    0.5000],
     [0.3333,    0.6667,    1.0000,    0.7500],
     [0.2500,    0.5000,    0.7500,    1.0000]]
A = array.array(A) %not tested
V, D = eigFuncAnalyzer.eigFunc(A, nargout=2)
print("V: ", V)
print("D: ", D)
eigFuncAnalyzer.terminate()
```

Please note that you can design your `eigFunc.m` in a way that you can simply load the mat data and you can use `scipy.io.savemat` function to save the python data to mat format. For details see the [scipy documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.savemat.html).

{% include google-adsense-display-ad.html %}

## Data Type Conversions

|                MATLAB                | PYTHON        |
| :----------------------------------: | ------------- |
|            double, single            | float         |
|    complex single complex double     | complex       |
| (u)int8, (u)int16, (u)int32,(u)int64 | int           |
|                 NaN                  | float(nan)    |
|                 Inf                  | float(inf)    |
|             String, char             | str           |
|               Logical                | bool          |
|              Structure               | dict          |
|               Vectors                | array.array() |
|              Cell array              | list, tuple   |



## References

1.  [How to Call MATLAB from Python](https://www.youtube.com/watch?v=OocdPu1Tcrg)
2.  [Call MATLAB Functions from Python](https://www.mathworks.com/help/matlab/matlab_external/call-matlab-functions-from-python.html)
3.  [Generate a Python Package and Build a Python Application](https://www.mathworks.com/help/compiler_sdk/gs/create-a-python-application-with-matlab-code.html)

