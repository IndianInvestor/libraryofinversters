---
title: "Getting familiar with PyTorch data structures (codes included)"
date: 2021-04-23
tags:
  [PyTorch, Tensors]
excerpt: "In this introduction to the concepts of Pytorch data structures, we will learn about how to create and reshape tensors using Pytorch and compare it with the Numpy data structures."
mathjax: "true"
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/pytorch-teaser.png"
classes:
  - wide
sidebar:
  nav: "all_posts_list"
category: machinelearning

---

{% include toc %}

PyTorch is a popular Python library for deep learning. We will learn the basics of Pytorch and Pytorch tensor a, how to create it, and perform some operations. 

A tensor can be thought of as a generalized matrix. So, we can have a 1-D, 2D, or N-dimensional matrix. We generally call them scalar (single number), vector (1-D array), matrix (2-D array), and then higher ones can be simply called a tensor.

If you have done some theoretical mathematics, then you must be aware that tensors are an easy expression of our dataset and we don't need to design our equations around the dimensions. Similarly, in data science, if we use tensors then we can use our code for the single number, matrix, or complex data forms such as image data.


{% include image.html url="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/pytorch-teaser.png" description="Tensors in PyTorch" %}

{% include google-adsense-inarticle.html %}

## Import PyTorch and Numpy
Let us start by importing the libraries:

```python
import torch
import numpy as np
print(torch.__version__)
```

```python
1.1.0
```

The last command is to check the installation of PyTorch in the current environment.

## Creating a tensor

Now, let us create a Numpy array to obtain the `Tensor` object.

```python
myarr = np.arange(1,6)
print(myarr)
print(myarr.dtype)
print(type(myarr))
```

```python
[1 2 3 4 5]
int64
<class 'numpy.ndarray'>
```

If we want to convert the Numpy array to tensor, we do

```python
tt = torch.from_numpy(myarr)
print(tt)
print(tt.type())
```

```python
tensor([1, 2, 3, 4, 5])

torch.LongTensor
```

This one will create a link between the original (`myarr`) and `tt`. The better way to create an array will be

```python
tt = torch.tensor(myarr)
print(tt)
print(tt.type())
```

```python
tensor([1, 2, 3, 4, 5])
torch.LongTensor
```

Now, let us create a 2D tensor:

```python
my2darr = np.arange(0.,12.).reshape(4,3) #get a numpy array and reshape it to obtain 2d
print(my2darr)
tt2 = torch.tensor(my2darr)
print(tt2)
print(tt2.type())
```

```python
[[ 0.  1.  2.]
 [ 3.  4.  5.]
 [ 6.  7.  8.]
 [ 9. 10. 11.]]

tensor([[ 0.,  1.,  2.],
        [ 3.,  4.,  5.],
        [ 6.,  7.,  8.],
        [ 9., 10., 11.]], dtype=torch.float64)

torch.DoubleTensor
```

## Three main ways of defining Tensor in PyTorch

```python
mydata = np.arange(1,5)

mytensor1 = torch.Tensor(mydata)  # Equivalent to cc = torch.FloatTensor(data)
print(mytensor1, mytensor1.type())
```

```python
tensor([1., 2., 3., 4.]) torch.FloatTensor
```

```python
mytensor2 = torch.tensor(mydata)
print(mytensor2, mytensor2.type())
```

{% include google-adsense-inarticle.html %}

```python
tensor([1, 2, 3, 4]) torch.LongTensor
```

```python
mytensor3 = torch.tensor(mydata, dtype=torch.long)
print(mytensor3, mytensor3.type())
```

```python
tensor([1, 2, 3, 4]) torch.LongTensor
```

{% include image.html url="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/pytorch-basics/ways-tensor-create.png" description="Create different tensors in Pytorch" %}


## Common Numpy methods are available

{% include google-adsense-inarticle.html %}


```python
## Random Numbers
x = torch.rand(4, 3)
print(x)

x = torch.randn(4, 3)
print(x)

x = torch.randint(0, 5, (4, 3))
print(x)

x = torch.empty(4, 3)
print(x)


## Initialization
x = torch.zeros(2,5)
print(x)
```

```python
tensor([[0.2137, 0.1635, 0.0262],
        [0.5090, 0.6493, 0.2037],
        [0.3697, 0.9471, 0.7771],
        [0.1593, 0.9452, 0.0312]])

tensor([[-0.8143, -2.0780,  0.5173],
        [ 0.1504, -0.2943,  0.4080],
        [ 1.0094,  1.9406,  0.5446],
        [ 0.2792, -1.6270, -0.4240]])

tensor([[3, 1, 2],
        [4, 1, 3],
        [0, 1, 4],
        [1, 4, 4]])

tensor([[7.1664e-10, 4.5630e-41, 4.4871e+20],
        [3.0938e-41, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 1.8788e+31, 1.7220e+22]])

tensor([[0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0.]])
```

We can also define random number seed just like [numpy](/utilities/introduction-to-scientific-computing-using-numpy-python/):

```python
torch.manual_seed(42)
x = torch.rand(2, 3)
print(x)

print(x.shape)
```

```python
tensor([[0.8823, 0.9150, 0.3829],
        [0.9593, 0.3904, 0.6009]])
```

## PyTorch uses multiple devices

{% include google-adsense-inarticle.html %}


```python
print(x.device) #'cpu' or 'cuda'
```

PyTorch is able to harness the power of GPUs in addition to the CPU. For details, check [here](https://pytorch.org/docs/stable/tensor_attributes.html#torch-device).

## PyTorch Object Memory Layout

```python
x = torch.Tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(x.layout) #strided as default
```

```python
torch.strided
```

Currently, PyTorch support `torch.strided` (dense Tensors) and have beta support for `torch.sparse_coo` (sparse COO Tensors).

## View or Reshape

```python
x = torch.linspace(1,5, 10)
print(x)
print(x.view(2,5))
print(x)
print(x.reshape(2,5))
print(x)
```

```python
tensor([1.0000, 1.4444, 1.8889, 2.3333, 2.7778, 3.2222, 3.6667, 4.1111, 4.5556,
        5.0000])

tensor([[1.0000, 1.4444, 1.8889, 2.3333, 2.7778],
        [3.2222, 3.6667, 4.1111, 4.5556, 5.0000]])

tensor([1.0000, 1.4444, 1.8889, 2.3333, 2.7778, 3.2222, 3.6667, 4.1111, 4.5556,
        5.0000])

tensor([[1.0000, 1.4444, 1.8889, 2.3333, 2.7778],
        [3.2222, 3.6667, 4.1111, 4.5556, 5.0000]])

tensor([1.0000, 1.4444, 1.8889, 2.3333, 2.7778, 3.2222, 3.6667, 4.1111, 4.5556,
        5.0000])
```

`View` method do not changes the original tensor. This is similar to the `reshape` method. `View` method has been in PyTorch for a long time and `reshape` have been added recently. 

The main thing we need to care about is whether we modify the original tensor. But we ensure that we alter the original by using the reassignment.

```python
## With reshape
x = torch.linspace(1,5, 10)
print(x)
x = x.reshape(2,5)
print(x)
```

```python
tensor([1.0000, 1.4444, 1.8889, 2.3333, 2.7778, 3.2222, 3.6667, 4.1111, 4.5556,
        5.0000])

tensor([[1.0000, 1.4444, 1.8889, 2.3333, 2.7778],
        [3.2222, 3.6667, 4.1111, 4.5556, 5.0000]])
```

```python
## With view
x = torch.linspace(1,5, 10)
print(x)
x = x.view(2,5)
print(x)
```

```python
tensor([1.0000, 1.4444, 1.8889, 2.3333, 2.7778, 3.2222, 3.6667, 4.1111, 4.5556,
        5.0000])

tensor([[1.0000, 1.4444, 1.8889, 2.3333, 2.7778],
        [3.2222, 3.6667, 4.1111, 4.5556, 5.0000]])
```


```python
x = torch.linspace(1,5, 10)
print(x)
z = x.view(2,5)
x[0]=234
print(z) #z changed
print(x) #x changed
```

```python
tensor([1.0000, 1.4444, 1.8889, 2.3333, 2.7778, 3.2222, 3.6667, 4.1111, 4.5556,
        5.0000])

tensor([[234.0000,   1.4444,   1.8889,   2.3333,   2.7778],
        [  3.2222,   3.6667,   4.1111,   4.5556,   5.0000]])

tensor([234.0000,   1.4444,   1.8889,   2.3333,   2.7778,   3.2222,   3.6667,
          4.1111,   4.5556,   5.0000])
```

From the above code, we can see that `view` (also `reshape`) does not generate a copy of the array but point to the original array. This can be a convenience or inconvenience depending on the usage.

{% include google-adsense-inarticle.html %}


## Arithmetic with tensors

```python
a = torch.tensor([1,2,3], dtype=torch.float)
b = torch.tensor([4,5,6], dtype=torch.float)
print(a + b)
print(torch.add(a, b))
```

```python
tensor([5., 7., 9.])

tensor([5., 7., 9.])
```

We can also output the result into predefined tensor:

```python
result = torch.empty(3)
torch.add(a, b, out=result) 
print(result)
```

```python
tensor([5., 7., 9.])
```

We can also compute the dot product using the `dot` method:

```python
a = torch.tensor([1,2,3], dtype=torch.float)
b = torch.tensor([4,5,6], dtype=torch.float)
print(a, b)
print(a.mul(b)) 

print(a.dot(b))
```

```python
tensor([1., 2., 3.]) tensor([4., 5., 6.])

tensor([ 4., 10., 18.])

tensor(32.)
```

Unlike [numpy](/utilities/introduction-to-scientific-computing-using-numpy-python/) `dot` method, tThe Pytorch `dot` method only accepts the 1D array. For higher dimensional tensor array, we can do the matrix multiplication:

{% include google-adsense-inarticle.html %}


```python
a = torch.tensor([[0,2,4],[1,3,5]], dtype=torch.float)
b = torch.tensor([[6,7],[8,9],[10,11]], dtype=torch.float)
print(a)
print(b)

print('a: ',a.shape)
print('b: ',b.shape)

print(torch.mm(a,b)) #also a @ b or a.mm(b)

print('a x b: ',torch.mm(a,b).shape)
```

```python
tensor([[0., 2., 4.],
        [1., 3., 5.]])

tensor([[ 6.,  7.],
        [ 8.,  9.],
        [10., 11.]])

a:  torch.Size([2, 3])

b:  torch.Size([3, 2])

tensor([[56., 62.],
        [80., 89.]])

a x b:  torch.Size([2, 2])
```