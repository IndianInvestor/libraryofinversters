---
title: "How to start using Pandas immediately for Earth Data Analysis (codes included)"
date: 2021-04-14
tags: [pandas dataframe, scientific computing, python]
excerpt: "This tutorial gives a brief description of scientific computing using Pandas by introducing Series, DataFrame, Pandas common operations, methods, conditional operations, groupby operations, and reading and writing data"
mathjax: "true"
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/pandas-python.png"
classes:
  - wide
sidebar:
  nav: "all_posts_list"
category: utilities
---

{% include toc %}

Pandas (stands for Panel Data library) is an open-source library for Python that comes with many tools that make the task of data analysis several folds easier. It is built upon the Numpy Library in Python. For details on Numpy, please check my previous post:

{% assign postLink0 = "https://www.facebook.com/earthinversionwebsite/posts/114090434119224" %}
{% include facebook_postads.html postLink=postLink0 %}

In this tutorial, we will focus on two main data structures Pandas has - Series and DataFrames. We will see how we can perform `groupby` operations and read/write tabular data directly using Pandas.

{% include image.html url="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/pandas-python.png" description="" %}

## Pandas Series

Pandas series is similar to [numpy](/utilities/introduction-to-scientific-computing-using-numpy-python/) array but it can have "named index". Naming indexes helps a lot in data analysis.

Let's create a series:

### Create Pandas Series: Method 1 (detailed way)

```python
import numpy as np
import pandas as pd

np.random.seed(0)
labels = ['x', 'y', 'z' ]
arr = np.random.randn(3)
```

This gives a [numpy](/utilities/introduction-to-scientific-computing-using-numpy-python/) array:

```bash
[1.76405235 0.40015721 0.97873798]
```

Now, let's create a dictionary using the above labels and array:

```python
mydict = {lab:val for lab, val in zip(labels, arr)}
print(mydict)
```

=>

```python
{'x': 1.764052345967664, 'y': 0.4001572083672233, 'z': 0.9787379841057392}
```

We can simply use this dictionary to create a Pandas series

```python
myseries = pd.Series(data = mydict)
print(myseries)
```

=>

```bash
x    1.764052
y    0.400157
z    0.978738
dtype: float64
```

{% include google-adsense-inarticle.html %}

### Create Pandas Series: Method 2

We can also create Pandas series directly:

```python
myseries2 = pd.Series(data = arr, index = labels)
print(myseries2)
```

=>

```bash
x    1.764052
y    0.400157
z    0.978738
dtype: float64
```

Here, our data was all float (also interpreted by Pandas). But we can mix different data types together and Pandas will still be fine.


### Extract information from Pandas Series

We can use the index to extract the information from the series.

```python
print(myseries2['x'])
```

=>

```bash
1.764052345967664
```

### Operations on Pandas Series

Let us define two series and perform operations on them

```python
labels1 = ['x', 'y', 'z' ]
arr1 = np.random.randn(3)
labels2 = ['xx', 'y', 'z' ]

arr2 = np.random.randn(3)
myseries1 = pd.Series(data = arr1, index = labels1)
myseries2 = pd.Series(data = arr2, index = labels2)

print("myseries1: \n",myseries1)
print("myseries2: \n",myseries2)
```

=>

```bash
myseries1:
x   -0.187184
y    1.532779
z    1.469359
dtype: float64

myseries2:
xx    0.154947
y     0.378163
z    -0.887786
dtype: float64
```

Now, let's sum the two above series

```python
myseries = myseries1 + myseries2
print(myseries)
```

=>

```bash
x          NaN
xx         NaN
y     1.910942
z     0.581573
dtype: float64
```

You can notice that the pandas is quite forgiving. Even though there was no data for `xx` in `myseries1` and `x` in `myseries2`, Pandas did not throw errors but fill the missing values with NaN for us.

## Pandas DataFrames

{% include google-adsense-inarticle.html %}

When we combine multiple series with common index, then we get DataFrame.  

### Create `DataFrame` from random matrix

```python
mymat = np.random.randn(5,3)
mydf = pd.DataFrame(data=mymat)
print(mydf)
```

⇒

```markdown
	0         1         2
0  0.955057  0.190794  1.978757
1  2.605967  0.683509  0.302665
2  1.693723 -1.706086 -1.159119
3 -0.134841  0.390528  0.166905
4  0.184502  0.807706  0.072960
```

Now, let us try to name the index and columns

```python
mymat = np.random.randn(5,3)
mydf = pd.DataFrame(data=mymat, index="M N X Y Z".split(), columns="C1 C2 C3".split())
print(mydf)
```

This will return


```markdown
	C1        C2        C3
M  0.386030  2.084019 -0.376519
N  0.230336  0.681209  1.035125
X -0.031160  1.939932 -1.005187
Y -0.741790  0.187125 -0.732845
Z -1.382920  1.482495  0.961458
```

### Extract Series from Pandas DataFrame

```python
print(mydf['C1'])
```

⇒

```markdown
M    0.386030
N    0.230336
X   -0.031160
Y   -0.741790
Z   -1.382920
Name: C1, dtype: float64
```

```python
columnList = ['C1', 'C2']
print(mydf[columnList])
```

⇒

```markdown
	C1        C2
M  0.386030  2.084019
N  0.230336  0.681209
X -0.031160  1.939932
Y -0.741790  0.187125
Z -1.382920  1.482495
```

### Add new column to the existing Pandas Dataframe

Now, let us add a new column to the existing dataframe.

{% include google-adsense-inarticle.html %}

```python
mydf['C12'] = mydf['C1'] + mydf['C2']
print(mydf)
```

```markdown
	C1        C2        C3       C12
M  0.386030  2.084019 -0.376519  2.470049
N  0.230336  0.681209  1.035125  0.911546
X -0.031160  1.939932 -1.005187  1.908772
Y -0.741790  0.187125 -0.732845 -0.554665
Z -1.382920  1.482495  0.961458  0.099575
```

### Remove the existing column or index from Pandas Dataframe

```python
mydf.drop('C12', axis=1, inplace=True) #by default axis=0
print(mydf.head())
```

```markdown
	C1        C2        C3
M  0.386030  2.084019 -0.376519
N  0.230336  0.681209  1.035125
X -0.031160  1.939932 -1.005187
Y -0.741790  0.187125 -0.732845
Z -1.382920  1.482495  0.961458
```

Two things to notice here. Pandas by default take the index names to drop and it does not permanently remove the index or column unless specified. If we want to remove the index then we provide `axis=0` with the index name.

```python
mydf.drop('Z', inplace=True) #by default axis=0
print(mydf.head())
```

⇒

```markdown
	C1        C2        C3
M  0.386030  2.084019 -0.376519
N  0.230336  0.681209  1.035125
X -0.031160  1.939932 -1.005187
Y -0.741790  0.187125 -0.732845
```

### `loc` and `iloc` method to extract values from the Pandas Dataframe

We can use `loc` or `iloc` method to extract the row from the DataFrame:

```python
mymat = np.random.randn(5,3)
mydf = pd.DataFrame(data=mymat, index="M N X Y Z".split(), columns="C1 C2 C3".split())
print(mydf.head())

print(mydf.loc['M']) #uses the column name

print(mydf.iloc[0]) #uses index
```

```python
	C1        C2        C3
M -0.971393 -1.522333  1.133703
N  0.528187  0.393461 -0.630507
X -1.398290 -0.219311 -0.045676
Y  0.012421  0.093628  1.240813
Z -1.097693 -1.908009 -0.380104

C1   -0.971393
C2   -1.522333
C3    1.133703
Name: M, dtype: float64

C1   -0.971393
C2   -1.522333
C3    1.133703
Name: M, dtype: float64
```

We can also extract multiple rows by using a list of rows:

```python
mymat = np.random.randn(5,3)
mydf = pd.DataFrame(data=mymat, index="M N X Y Z".split(), columns="C1 C2 C3".split())
print(mydf.head())

print(mydf.loc[['M', 'X']])

print(mydf.iloc[[0, 2]])
```

```markdown
	C1        C2        C3
M -1.666059 -2.736995  1.522562
N  0.178009 -0.626805 -0.391089
X  1.743477  1.130018  0.897796
Y  0.330866 -1.063049 -0.125381
Z -0.945588  2.029544 -1.046358

  C1        C2        C3
M -1.666059 -2.736995  1.522562
X  1.743477  1.130018  0.897796

  C1        C2        C3
M -1.666059 -2.736995  1.522562
X  1.743477  1.130018  0.897796
```

How can we extract the columns?

```python
mymat = np.random.randn(5,3)
mydf = pd.DataFrame(data=mymat, index="M N X Y Z".split(), columns="C1 C2 C3".split())
print(mydf.head())

print(mydf.loc[['M', 'N'],'C1'])

print(mydf.iloc[[0, 1],0])
```

```markdown
	C1        C2        C3
M -1.549671  0.435253  1.259904
N -0.447898  0.266207  0.412580
X  0.988773  0.513833 -0.928205
Y  0.846904 -0.298436  0.029141
Z  0.889031 -1.839261  0.863596

M   -1.549671
N   -0.447898
Name: C1, dtype: float64

M   -1.549671
N   -0.447898
Name: C1, dtype: float64
```

### Conditional Operations on Pandas DataFrames

{% include google-adsense-inarticle.html %}

```python
mymat = np.random.randn(5,3)
mydf = pd.DataFrame(data=mymat, index="M N X Y Z".split(), columns="C1 C2 C3".split())
print(mydf.head())
```

```python
	C1        C2        C3
M  1.035125 -0.031160  1.939932
N -1.005187 -0.741790  0.187125
X -0.732845 -1.382920  1.482495
Y  0.961458 -2.141212  0.992573
Z  1.192241 -1.046780  1.292765
```

Now, we want to find all the values in the DataFrame that are positive and mask all others. This can be easily done using:


```python
mydf = mydf[mydf>0]
print(mydf.head())
```

```python
	C1  C2        C3
M  1.035125 NaN  1.939932
N       NaN NaN  0.187125
X       NaN NaN  1.482495
Y  0.961458 NaN  0.992573
Z  1.192241 NaN  1.292765
```

We can do the same thing for just a particular column:

```python
mydf = mydf[mydf['C2']>0]
print(mydf.head())
```

```python
	C1        C2        C3
M  0.649148  0.358941 -1.080471
N  0.902398  0.161781  0.833029
Y -0.708954  0.586847 -1.621348
Z  0.677535  0.026105 -1.678284
```

We can use the `value_counts()` method (for series) for counting the number of C2>0. There are many other ways we can retrieve such information.

We can also use more than one condition. Please note that in this case I regenerated the `mydf` using the [numpy](/utilities/introduction-to-scientific-computing-using-numpy-python/) seed of 0.

```python
np.random.seed(0)
mymat = np.random.randn(5,3)
mydf = pd.DataFrame(data=mymat, index="M N X Y Z".split(), columns="C1 C2 C3".split())
print(mydf.head())
```

```python
  C1        C2        C3
M  1.764052  0.400157  0.978738
N  2.240893  1.867558 -0.977278
X  0.950088 -0.151357 -0.103219
Y  0.410599  0.144044  1.454274
Z  0.761038  0.121675  0.443863
```

```python
mydf2 = mydf[(mydf['C1']>0) & (mydf['C2']>1)]
print(mydf2.head())
```

```python
			C1        C2        C3
N  2.240893  1.867558 -0.977278
```

Pandas conditioning operations uses "&" for Python "and" and "|" for Python "or". 

### Create new index for the dataframe

```python
mymat = np.random.randn(5,3)
mydf = pd.DataFrame(data=mymat, index="M N X Y Z".split(), columns="C1 C2 C3".split())
print(mydf.head())
```

```python
	C1        C2        C3
M  1.764052  0.400157  0.978738
N  2.240893  1.867558 -0.977278
X  0.950088 -0.151357 -0.103219
Y  0.410599  0.144044  1.454274
Z  0.761038  0.121675  0.443863
```

Now, we create a new column with new index values

```python
my_new_idx = "MM NN XX YY ZZ".split()
mydf['newidx'] = my_new_idx
print(mydf.head())
```

```python
	C1        C2        C3 newidx
M  1.764052  0.400157  0.978738     MM
N  2.240893  1.867558 -0.977278     NN
X  0.950088 -0.151357 -0.103219     XX
Y  0.410599  0.144044  1.454274     YY
Z  0.761038  0.121675  0.443863     ZZ
```

Let's make the column "newidx" as the index (we will lose our original index):

```python
mydf.set_index('newidx', inplace=True)
print(mydf.head())
```

```python
newidx      C1        C2        C3                              
MM      1.764052  0.400157  0.978738
NN      2.240893  1.867558 -0.977278
XX      0.950088 -0.151357 -0.103219
YY      0.410599  0.144044  1.454274
ZZ      0.761038  0.121675  0.443863
```

## Pandas Common Methods and attributes

### `df.info`

```python
mydf.info()
```

```python
<class 'pandas.core.frame.DataFrame'>
Index: 5 entries, M to Z
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   C1      5 non-null      float64
 1   C2      5 non-null      float64
 2   C3      5 non-null      float64
dtypes: float64(3)
memory usage: 160.0+ bytes
```

### `df.dtypes`

```python
mydf.dtypes
```

```python
C1    float64
C2    float64
C3    float64
dtype: object
```

### `df.describe()`

{% include google-adsense-inarticle.html %}

```python
mydf.describe()
```

```python
	C1	  C2	     C3
count	5.000000	5.000000	5.000000
mean	1.225334	0.476415	0.359276
std	0.754437	0.801795	0.947389
min	0.410599	-0.151357	-0.977278
25%	0.761038	0.121675	-0.103219
50%	0.950088	0.144044	0.443863
75%	1.764052	0.400157	0.978738
max	2.240893	1.867558	1.454274
```

### Apply (`apply`) method

```python
np.random.seed(0)
mymat = np.random.randn(5,3)
mydf = pd.DataFrame(data=mymat, index="M N X Y Z".split(), columns="C1 C2 C3".split())
print(mydf.head())

def square(number):
    return number**2

print(mydf['C1'].apply(square))
```

```python
C1        C2        C3
M  1.764052  0.400157  0.978738
N  2.240893  1.867558 -0.977278
X  0.950088 -0.151357 -0.103219
Y  0.410599  0.144044  1.454274
Z  0.761038  0.121675  0.443863

M    3.111881
N    5.021602
X    0.902668
Y    0.168591
Z    0.579178
Name: C1, dtype: float64
```

### Sort DataFrame by columns


```python
np.random.seed(0)
mymat = np.random.randn(5,3)
mydf = pd.DataFrame(data=mymat, index="M N X Y Z".split(), columns="C1 C2 C3".split())
print(mydf.head())

print(mydf.sort_values(by='C2'))
```

```python
C1        C2        C3
M  1.764052  0.400157  0.978738
N  2.240893  1.867558 -0.977278
X  0.950088 -0.151357 -0.103219
Y  0.410599  0.144044  1.454274
Z  0.761038  0.121675  0.443863

  C1        C2        C3
X  0.950088 -0.151357 -0.103219
Z  0.761038  0.121675  0.443863
Y  0.410599  0.144044  1.454274
M  1.764052  0.400157  0.978738
N  2.240893  1.867558 -0.977278
```

## Pandas Groupby Operations

Sometimes in Pandas dataframe we want to combine some columns based on some criteria. Groupby method can do this task elegantly by performing "split", "apply", and "combine" operations under the hood. It will be more clear with some examples.

{% include google-adsense-inarticle.html %}

```python
np.random.seed(0)
mymat = np.random.randn(10,3)
mydf = pd.DataFrame(data=mymat, columns="C1 C2 C3".split())
mydf['names'] = "M N X Y Z".split() * 2
print(mydf)
```

```python
	C1        C2        C3   names
0  1.764052  0.400157  0.978738     M
1  2.240893  1.867558 -0.977278     N
2  0.950088 -0.151357 -0.103219     X
3  0.410599  0.144044  1.454274     Y
4  0.761038  0.121675  0.443863     Z
5  0.333674  1.494079 -0.205158     M
6  0.313068 -0.854096 -2.552990     N
7  0.653619  0.864436 -0.742165     X
8  2.269755 -1.454366  0.045759     Y
9 -0.187184  1.532779  1.469359     Z
```

```python
mydf.groupby('names').mean()
```

```python
names        C1        C2        C3                      
M      1.048863  0.947118  0.386790
N      1.276980  0.506731 -1.765134
X      0.801854  0.356539 -0.422692
Y      1.340177 -0.655161  0.750016
Z      0.286927  0.827227  0.956611
```

We can replace the "mean" method with any other aggregate method such as sum, max, std, etc.

Another example with the "describe" method:

```python
print(mydf.groupby('names').describe().transpose())
```

```python
names            M         N         X         Y         Z
C1 count  2.000000  2.000000  2.000000  2.000000  2.000000
   mean   1.048863  1.276980  0.801854  1.340177  0.286927
   std    1.011430  1.363178  0.209636  1.314622  0.670494
   min    0.333674  0.313068  0.653619  0.410599 -0.187184
   25%    0.691269  0.795024  0.727736  0.875388  0.049872
   50%    1.048863  1.276980  0.801854  1.340177  0.286927
   75%    1.406458  1.758937  0.875971  1.804966  0.523982
   max    1.764052  2.240893  0.950088  2.269755  0.761038

C2 count  2.000000  2.000000  2.000000  2.000000  2.000000
   mean   0.947118  0.506731  0.356539 -0.655161  0.827227
   std    0.773520  1.924500  0.718274  1.130246  0.997801
   min    0.400157 -0.854096 -0.151357 -1.454366  0.121675
   25%    0.673638 -0.173682  0.102591 -1.054763  0.474451
   50%    0.947118  0.506731  0.356539 -0.655161  0.827227
   75%    1.220599  1.187145  0.610488 -0.255559  1.180003
   max    1.494079  1.867558  0.864436  0.144044  1.532779

C3 count  2.000000  2.000000  2.000000  2.000000  2.000000
   mean   0.386790 -1.765134 -0.422692  0.750016  0.956611
   std    0.837141  1.114197  0.451803  0.995971  0.725135
   min   -0.205158 -2.552990 -0.742165  0.045759  0.443863
   25%    0.090816 -2.159062 -0.582428  0.397887  0.700237
   50%    0.386790 -1.765134 -0.422692  0.750016  0.956611
   75%    0.682764 -1.371206 -0.262955  1.102145  1.212985
   max    0.978738 -0.977278 -0.103219  1.454274  1.469359
```

## Read and Write Data with Pandas

For details on how to read and write tabular data with the help of Pandas, please refer to the Pandas documentation [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html).

The most common ones you would like to familiarize yourself are - `read_csv`, `to_csv`, 

Let us start by writing our dataframe into a file `myexample.csv`

{% include google-adsense-inarticle.html %}

```python
np.random.seed(0)
mymat = np.random.randn(5,3)
mydf = pd.DataFrame(data=mymat, index="M N X Y Z".split(), columns="C1 C2 C3".split())

mydf.to_csv('myexample.csv', index=False)
```

```bash
cat myexample.csv
```

```markdown
C1,C2,C3
1.764052345967664,0.4001572083672233,0.9787379841057392
2.240893199201458,1.8675579901499675,-0.977277879876411
0.9500884175255894,-0.1513572082976979,-0.10321885179355784
0.41059850193837233,0.144043571160878,1.454273506962975
0.7610377251469934,0.12167501649282841,0.44386323274542566
```

Now, lets read that file using the `read_csv`

```python
mydf2 = pd.read_csv('myexample.csv')
print(mydf2.head())
```

```python
	C1        C2        C3
0  1.764052  0.400157  0.978738
1  2.240893  1.867558 -0.977278
2  0.950088 -0.151357 -0.103219
3  0.410599  0.144044  1.454274
4  0.761038  0.121675  0.443863
```