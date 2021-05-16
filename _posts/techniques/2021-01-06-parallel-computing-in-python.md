---
title: "Speed-up your codes by parallel computing in Python (codes included)"
date: 2021-01-06
tags: [python, multiprocessing, threading, joblib]
excerpt: "Parallel computing is quickly becoming a necessity. Modern computers comes with more than one process and we most often only use single process to do most of our tasks. Parallel computing is a way of diving the tasks into all the processes available on the system and achieve speed ups."
mathjax: "true"
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/parallel_computing.jpg"
classes:
  - wide
sidebar:
  nav: "all_posts_list"
category: techniques
---

{% include toc %}

## Introduction

With the increasing amount of data, parallel computing is quickly becoming a necessity. Modern computers come with more than one cores, but we most often only use a single process to do most of our tasks. Parallel computing is a way of dividing the tasks into all or selected number of the system cores and achieving speedups.

{% include google-adsense-inarticle.html %}

Python by itself is slow. But fortunately there are several libraries in Python that can help in performing parallel computations and some to just speed up the single thread job. This post will discuss the basics of the parallel computing libraries, such as multiprocessing (and Threading), and joblib. After reading this article, I hope that you would be able to feel more confident on this topic.

{% assign postTitle0 = "The right way to loop in Python" %}
{% assign postLink0 = "/techniques/right-way-loop-in-python/" %}
{% assign postExcerpt0 = "What is the fastest and most efficient way to loop in Python. We found that the numpy is fastest and python builtin is the most memory efficient" %}

{% include single-post-ad.html postTitle=postTitle0 postLink=postLink0 postExcerpt=postExcerpt0 %}

## Threading Module

Python comes with the threading API, that allows us to have different parts of the program run concurrently. Many people confuse threading with multiprocessing. To make things simples, we can remember that threading is not strictly parallel computation as it appears to (though it will definitely give speed up to your program). The threading maybe running on your multiple processes but only one task will be done at a time. One may think that in that case, multiprocessing sounds better. But multiprocessing always comes with some extra overhead as your system needs to spawn different processes and make it ready for the task. But threading also has limitation because of the GIL in Python that limits it to run only one thread at a time.

{% include google-adsense-inarticle.html %}

<p align="center"><iframe src="https://assets.pinterest.com/ext/embed.html?id=794744665493242106" height="295" width="345" frameborder="0" scrolling="no" ></iframe></p>

Now, let us see an example that uses threading to speedup the task.

<script src="https://gist.github.com/earthinversion/f1925adc2f74fb12596bcffd18bdc2c9.js"></script>

### Using `concurrent.futures`

<script src="https://gist.github.com/earthinversion/1d2c929a42978c1e0b32367b5ba9740d.js"></script>

## Multiprocessing Module

Python has an in-built parallel computing module `multiprocessing` to allow us to write parallel codes by spawning processes on our system. The multiprocessing package offers both local and remote concurrency, effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads. It offers a convenient means of parallelizing the execution of a function across multiple input values, distributing the input data across processes. For details, visit [python docs](https://docs.python.org/3/library/multiprocessing.html). The notable things to remember are: [how to start a process](https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods), [how to exchange objects between processes](https://docs.python.org/3/library/multiprocessing.html#exchanging-objects-between-processes) (includes queuing and piping for communication between processes).

{% include google-adsense-inarticle.html %}

There is a difference between `multiprocessing` and `threading`. `threading` run the tasks concurrently, however, `multiprocessing` run the tasks parallely at the same time. Both of them can achieve significant improvement in the speed and one is preferable over other depending on the nature of the tasks.

In this post, we will have a look at the essentials of this module. Before getting into the nitty-gritty of this module, let us import it and check the number of cores on your computer.

```python
import multiprocessing

print("Number of CPUs : ", multiprocessing.cpu_count())
```

This outputs `Number of CPUs : 12`.

```python
import time
import multiprocessing

def my_awesome_function(sleepTime):
    time.sleep(sleepTime)


Stime = time.perf_counter()
my_awesome_function(0.1)
my_awesome_function(1)
my_awesome_function(0.3)
print(f"Finished in {time.perf_counter()-Stime:.2f}")
```

The above code shows the sequential run of a dummy function named `my_awesome_function`. All this function does is sleep for a specified number of seconds. This kind of function is simply a representation of a function that takes `sleepTime` amount of time to achieve the computation. The run time for the above code is `1.40` seconds as expected.

The problem with sequential kind of coding (also called running the function synchronously) is that with more number of computations or tasks, the amount of time required to finish it is linearly increasing. We can mitigate such issues by employing the other CPUs in our computer.

{% include google-adsense-inarticle.html %}

For parallel computing, we can break these three tasks into 3 processes. And unlike running sequentially in the previous case, multiprocessing run all the tasks at the same time.

```python
import time
import multiprocessing

def my_awesome_function(sleepTime=0.1):
    time.sleep(sleepTime)
    print(f"function with {sleepTime} time finished")


Stime = time.perf_counter()
p1 = multiprocessing.Process(target=my_awesome_function)
p2 = multiprocessing.Process(target=my_awesome_function)
p3 = multiprocessing.Process(target=my_awesome_function)

## start the process
p1.start()
p2.start()
p3.start()

## script will continue while the process starts...

print(f"Finished in {time.perf_counter()-Stime:.2f}")
```

This will output:

```
Finished in 0.01
function with 0.1 time finished
function with 0.1 time finished
function with 0.1 time finished
```

In the above script, we may think the output is strange. But the script finished first while the three processes were starting. We can avoid this by using the `join` method.

```python
import time
import multiprocessing


def my_awesome_function(sleepTime=0.1):
    time.sleep(sleepTime)
    print(f"function with {sleepTime} time finished")


Stime = time.perf_counter()
p1 = multiprocessing.Process(target=my_awesome_function)
p2 = multiprocessing.Process(target=my_awesome_function)
p3 = multiprocessing.Process(target=my_awesome_function)

## start the process
p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()

print(f"Finished in {time.perf_counter()-Stime:.2f}")
```

This will output:

```
function with 0.1 time finished
function with 0.1 time finished
function with 0.1 time finished
Finished in 0.11
```

Great!! Now we are able to make our script run in parallel and achieve speedups. But what if our script gives some output that we want to store or use, or what if the script takes one or more arguments. How can we deal with such cases?

### Using process

<script src="https://gist.github.com/earthinversion/e4cdaf47b38e1a3043426157a3434b03.js"></script>

If you compare the time taken by this script with that of the threading, you can notice that the time taken by both are almost same.

### Using concurrent.futures with submit

{% include google-adsense-inarticle.html %}

<script src="https://gist.github.com/earthinversion/5a0f609de91e2341c2ed87a096954413.js"></script>

The above call of the `ProcessPoolExecutor` with the context manager will use all the threads on the system. This leaves the system completely occupied until the assigned tasks are finished. I found that using only 80% of the threads works great for performance as well as it leaves some memory for other tasks. We can specify 80% of the thread using `max_workers=int(0.8*multiprocessing.cpu_count())` as argument for the `ProcessPoolExecutor` .

### Using concurrent.futures with map

The `executor.map` function works just like the Python [`map` ](https://www.geeksforgeeks.org/python-map-function/) function. The takes in a function as first argument and an iterable as second argument.

<script src="https://gist.github.com/earthinversion/1099c971836c0cb0060e244db0148a27.js"></script>

The results obtained using `executor.map` function is synchronous.

## Threading vs Multiprocessing

We now have a basic understanding of the two ways to speedup our programs. However, the question arises, which is the better way. There is no one answer to that. It depends strictly on your program. If your program spend much of its time waiting for external events are generally good candidates for threading (I/O bound tasks). Programs that require heavy CPU computation (CPU bound tasks) and spend little time waiting for external events might not run faster at all. In such cases, multiprocessing is a good alternative.

<p align="center"><iframe src="https://assets.pinterest.com/ext/embed.html?id=794744665493242131" height="272" width="345" frameborder="0" scrolling="no" ></iframe></p>

## Joblib Module

[Joblib](https://joblib.readthedocs.io/en/latest/) provides a set of tools for lightweight pipelining in Python. It is fast and is optimized for the numpy arrays. So, we can employ it for several applications of data science. The main focus of joblib is to reduce repetitive computation and persist to disk; hence it has significant advantages for large data computation.

{% include google-adsense-inarticle.html %}

Here, we can have a look at the parallel computation functionality of the `joblib` library. We use a simple function, `function_to_test`, and made it to sleep for 0.1 sec to imitate functions that take longer to compute. We made this dummy function more complex by adding two required arguments. We use the number of CPUs in the system for the number of parallel processes. In my case, the `cpu_count` is 12.

<script src="https://gist.github.com/earthinversion/801c775bbe559324af87af949cdf98d0.js"></script>

We used the `time.perf_counter()` to compute the time taken by the parallel computation and by the sequential computation.

```
Joblib finished in 2.98 secs
Numpy finished in 30.95 secs
```

The total number of computations for this example is `30*10=300`, and each function takes `~0.1` seconds to run. So, it is expected for the sequential computation to take around `300*0.1=30` seconds. But the parallel algorithm can achieve this much faster. Since I have 12 CPUs, `joblib` divided the task into 12 processes, hence the speed jump of `30/12=2.5`. The difference in the expected time of `2.5 sec` and the actual time taken (`2.98 sec`) comes because of the overhead associated with the parallel computation. This overhead is the reason parallel computation is not recommended for smaller sets of data.

## References

<ol>
<li><a href="https://www.youtube.com/watch?v=IEEhzQoKtQU&t=1833s">Python Threading Tutorial: Run Code Concurrently Using the Threading Module</a></li>
</ol>
