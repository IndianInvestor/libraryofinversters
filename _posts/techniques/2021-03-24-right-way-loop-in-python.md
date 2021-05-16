---
title: "The right way to loop in Python (codes included)"
date: 2021-03-24
tags: [python, looping, while loop, for loop, speedup]
excerpt: "What is the fastest and most efficient way to loop in Python. We found that the numpy is fastest and python builtins are the most memory efficient."
mathjax: "true"
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/right-loops.webp"
classes:
  - wide
sidebar:
  nav: "all_posts_list"
category: techniques
---

{% include toc %}



## Introduction

Since, Python by itself is slow, it becomes import to know the nitty-gritty of different components of our code to efficienty code. In this post, we will look into most common ways we loop in Python using a simple summing example. We will also compute the memory profile to inspect which way is the most memory efficient for analyzing huge datasets.

{% assign postTitle0 = "Speed-up your codes by parallel computing in Python" %}
{% assign postLink0 = "/techniques/parallel-computing-in-python/" %}
{% assign postExcerpt0 = "Parallel computing is quickly becoming a necessity. Modern computers comes with more than one process and we most often only use single process to do most of our tasks. Parallel computing is a way of diving the tasks into all the processes available on the system and achieve speed ups." %}

{% include single-post-ad.html postTitle=postTitle0 postLink=postLink0 postExcerpt=postExcerpt0 %}

<p align="center">
 <img width="2308" height="1148" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/right-loops.webp">
</p>

{% include google-adsense-inarticle.html %}

## The `while` loop

```python
import timeit
import numpy as np

nval = 1000000

# usual while loop


def while_loop(n=nval):
    i, sumval = 0, 0
    while i < n:
        sumval += 1
        i += 1

    return sumval

if __name__ == "__main__":

    print(
        f"while_loop: {timeit.timeit(while_loop, number = 10):.6f}s")
   
```

This returns `while_loop: 0.727578s`.  We can also do the memory profiling of this function.

```python
import timeit
import numpy as np
from memory_profiler import profile

nval = 1000000

# usual while loop
@profile(precision=4)
def while_loop(n=nval):
    i, sumval = 0, 0
    while i < n:
        sumval += 1
        i += 1

    return sumval


if __name__ == "__main__":
    while_loop()
  

```

This returns:

```
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    10  25.8984 MiB  25.8984 MiB           1   @profile(precision=4)
    11                                         def while_loop(n=nval):
    12  25.8984 MiB   0.0000 MiB           1       i, sumval = 0, 0
    13  25.9727 MiB   0.0000 MiB     1000001       while i < n:
    14  25.9727 MiB   0.0625 MiB     1000000           sumval += 1
    15  25.9727 MiB   0.0117 MiB     1000000           i += 1
    16                                         
    17  25.9727 MiB   0.0000 MiB           1       return sumval
```

In total, the while loop took `0.0743`Mb of the memory usage for the above task.

## The `for` loop

{% include google-adsense-inarticle.html %}

```python
import timeit
import numpy as np

nval = 1000000


# usual for loop


def for_loop(n=nval):
    sumval = 0
    for i in range(n):
        sumval += i
    return sumval

if __name__ == "__main__":

    print(
        f"for_loop: {timeit.timeit(for_loop, number = 10):.6f}s")
```

This returns `for_loop: 0.490051s`.  Now, we do the memory profiling of this function.

```
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    22  25.9922 MiB  25.9922 MiB           1   @profile(precision=4)
    23                                         def for_loop(n=nval):
    24  25.9922 MiB   0.0000 MiB           1       sumval = 0
    25  26.0273 MiB   0.0117 MiB     1000001       for i in range(n):
    26  26.0273 MiB   0.0234 MiB     1000000           sumval += i
    27  26.0273 MiB   0.0000 MiB           1       return sumval
```

In total, the for loop took `0.0351`Mb of the memory usage for the above task.

## The builtin python function

```python
import timeit
import numpy as np

nval = 1000000


# using built in sum
def builtinsum(n=nval):
    return sum(range(n))

if __name__ == "__main__":

    print(
        f"builtinsum: {timeit.timeit(builtinsum, number = 10):.6f}s")
```

This returns `builtinsum: 0.175238s`.



```
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    46  25.8867 MiB  25.8867 MiB           1   @profile(precision=4)
    47                                         def builtinsum(n=nval):
    48  25.8906 MiB   0.0039 MiB           1       return sum(range(n))
```

In total, the "builtin function" based function took `0.0039`Mb of the memory usage for the above task.

{% include google-adsense-inarticle.html %}

## The `numpy` function

```python
import timeit
import numpy as np

nval = 1000000


# using numpy sum
def numpysum(n=nval):
    return np.sum(np.arange(n))

if __name__ == "__main__":

    print(
        f"numpysum: {timeit.timeit(numpysum, number = 10):.6f}s")
```

This returns `numpysum: 0.017640s`.

```
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    53  25.9766 MiB  25.9766 MiB           1   @profile(precision=4)
    54                                         def numpysum(n=nval):
    55  33.6172 MiB   7.6406 MiB           1       return np.sum(np.arange(n))
```

In total, the [numpy](/utilities/introduction-to-scientific-computing-using-numpy-python/) based function took `7.6407`Mb of the memory usage for the above task.

## Conclusions

Please note that these values of run time and memory usage may differ from system to system but the ratio of these values between different methods will stay very similar. 

We found that the numpy is fastest (`0.017640`s) and while loop sum is the slowest (`0.727578`s). The reason for the while loop to be slow is that each step of the task is completed in the native Python. Since `numpy` is written in `C`, it runs quite fast.

In terms of the memory usage, the [numpy](/utilities/introduction-to-scientific-computing-using-numpy-python/) is the worst. It took `~7`Mb of the memory usage. In contrast, the "builtin python function" based function is the most memory efficient as it does not store all the data into memory but does it in steps.

{% include google-adsense-inarticle.html %}

If we compare the while and for loop, then for loop is fast and also more memory efficient. Hence, for loop should always be our first choice (and usually is) unless we don't know the total number of runs. 

<p align="center"><iframe src="https://assets.pinterest.com/ext/embed.html?id=794744665493240237" height="295" width="345" frameborder="0" scrolling="no" ></iframe></p>

## References

<ol>
<li><a href="https://youtu.be/Qgevy75co8c">The fastest way to loop in Python - An Unfortunate truth</a></li>
</ol>

