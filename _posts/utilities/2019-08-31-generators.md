---
title: "Why we should use generators? [Python]"
date: 2019-08-31
tags: [data science, python, generators, geophysics]
excerpt: "Generators don't hold the entire result in memory. It yields one result at a time."
classes:
  - wide
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/results_generators.png"
sidebar:
  nav: "all_posts_list"
category: utilities
---

{% include toc %}

Before we get into the idea of generators, we need to understand the difference between "iterables" and "iterators".

## Iterables and Iterators

Let me start by saying that the `list`, `tuples`,`strings`, `dictionaries`, etc are iterables. Let us see an example:

```python
testList = [1, 2, 3]
for val in testList:
    print(val)
```

This will output (as we can guess):

```
1
2
3
```

For an object to be an iterable, it needs to have a method `__iter__()`.
We can check if our list has this method by investigating using the built-in `dir` function:

{% include google-adsense-inarticle.html %}

```python
print(dir(testList))
```

This outputs a list:

```
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

This has a method `__iter__` as we can see.
Iterators, unlike iterables, has a state where it knows where it is during an iteration and knows how to get the next value.

In the above example of the list object, if we query its next value, then it will not know.

```python
print(next(testList))
```

This throws an error:

```
Traceback (most recent call last):
  File "iterables.py", line 7, in <module>
    print(next(testList))
TypeError: 'list' object is not an iterator
```

If we convert the list object into an iterator using the `__iter__` method, then we can apply the `next` function on it:

```python
testIter = testList.__iter__()
print(testIter)
```

or

```python
testIter = iter(testList)
print(testIter)
```

This will print:

```
<list_iterator object at 0x7fd6d6f2de90>
```

If we apply the next function now, it will work:

```python
print(next(testIter))
print(next(testIter))
print(next(testIter))
```

```
1
2
3
```

But if we print the next again then it will raise `StopIteration` error.

```python
print(next(testIter))
print(next(testIter))
print(next(testIter))
print(next(testIter))
```

```
1
2
3
Traceback (most recent call last):
  File "iterables.py", line 15, in <module>
    print(next(testIter))
StopIteration
```

This means that the iterators knows where to stop.

If we use the `for loop` to run this, then Python will automatically figure it out where to stop:

```python
for val in testIter:
    print(val)
```

```
1
2
3
```

To understand this, let us perform the same operation using the `while` loop.

```python
while True:
    try:
        item = next(testIter)
        print(item)
    except StopIteration:
        break
```

There are several built-in iterator functions in Python such as the `range` function we most often use. We can create our own class for iterators. Let us create the one similar to `range`:

```python
class rangeNew:
    def __init__(self, start, end, step=1):
        self.value = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration

        current = self.value
        self.value += self.step
        return current
rangeIter = rangeNew(1, 10, 2)

for val in rangeIter:
    print(val)

```

```
1
3
5
7
9
```

## Generators

- Generators don't hold the entire result in memory. It yields one result at a time.
- Ways of creating generators:

  1. Using a function

     ```python
     def squares_gen(num):
             for i in num:
                     yield i**2
     ```

     ```python
     def squares(num):
             results=[]
             for i in num:
                     results.append(i**2)
             return results
     ```

     - Elapsed time for list: `7.360722` Seconds

     - Elapsed time for generators: `5.999999999950489e-06` Seconds

     - Difference in time taken for the list and generators: `7.360716` Seconds for `num = np.arange(1,10000000)`

  2. Like a list comprehension

     ```python
     resl = [i**2 for i in num]
     ```

     ```python
     resg = (i**2 for i in num)
     ```

     - Elapsed time for list: `7.663468000000001` Seconds

     - Elapsed time for generators: `9.999999999621423e-06` Seconds

     - Difference in time taken: `7.663458000000001` Seconds for `num = np.arange(1,10000000)`

- Getting the results from the generator function:
  1. Using `next`
     ```python
     resg = squares_gen(num)
     print('res of generators: ',next(resg))
     print('res of generators: ',next(resg))
     print('res of generators: ',next(resg))
     ```
  2. Using `loop`:
     ```python
     for n in resg:
         print(n)
     ```

## Advantages of using generators:

1. The generator codes are more readable.
2. Generators are much faster and uses little memory.

## Results:

1. Using function is a faster way of creating values in Python than using loop or list comprehension for both lists and generators.
2. The difference between using list or generators is more pronounced when using a comprehension (though generators are still much faster.)
3. When we need the result of whole array at a time then the amount of time (or memory) taken to create a list or `list(generators)` are almost same.

<figure class="half">
    <img src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/results_generators.png" alt="How to used Generator">
    <img src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/Memory_usage.png" alt="Memory usage">
</figure>

Overall, generators gives a performance boost not only in execution time but with the memory as well.

## Appendix

### How I calculated the time taken by the process

- Calculate sum of the system and user CPU time of the current process.
  - `time.process_time` provides the system and user CPU time of the current process in seconds.
  - Use `time.process_time_ns` to get the result in nanoseconds

**NOTE:** The "time taken" shown in this study is subjective to different computers and varies each time depending on the state of the CPU. But each and everytime, the using generators are much faster.

## References:

1. [Python Tutorial: Iterators and Iterables - What Are They and How Do They Work?](https://youtu.be/jTYiNjvnHZY) by Corey Schafer

