---
title: "Introduction to Python for beginners"
date: 2017-12-22
last_modified_at: 2021-1-12
tags: [python, python3, anaconda, miniconda]
excerpt: "In this tutorial post, I give a quick demo of how to install Python (using anaconda) and then getting started with writing simple scripts."
mathjax: "true"
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/intro-python/python_webpage.jpeg"
classes:
  - wide
sidebar:
  nav: "all_posts_list"
category: techniques
---

{% include toc %}

<iframe width="420" height="315"
  src="https://www.youtube.com/embed/4eGbxJi01xA?autoplay=1&mute=1">
</iframe>

## Introduction

Python has become the most popular language for programming and its community is huge, active and ever-increasing. Before Python, MATLAB was the preferred language for the scientific community but now most of the researchers are migrating to Python. Like MATLAB, Python is quite easy to use but over that Python can be used for the system control, software developing, easy integration with other languages like FORTRAN, C , etc. This makes it extremely popular among all sorts of communities. Some P.Is want their students to work in Python because according to them, even when the students want to switch the field or simply leave the field, it could still be useful to them.

{% include google-adsense-inarticle.html %}

If you are familiar with other programming languages including MATLAB, then its very easy to switch to Python. Though, there are some issues the beginners and the MATLAB users face while making a move to Python. Here, let us deal with that issue and get started with Python.

## Getting started with Python

Currently, there are two versions of Python – 2.7, and 3.6. But we will stick with Python 3.6. The steps for the version 2.7 is very similar.

### Download

Python can be downloaded directly from its official website https://www.python.org/downloads/.

<p align="center">
 <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/intro-python/python_webpage.jpeg">
</p>

But, here, we will download Python from the Anaconda website. Download the installer for the [Windows](https://repo.continuum.io/miniconda/Miniconda3-latest-Windows-x86_64.exe), [Mac](https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh), or the [Linux](https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh) system. For Windows, you will get a `.exe` extension file, double-click the file and follow the installation procedure.For Mac and Linux system, the file will be with the extension `.sh` (a shell- script). You can open your favorite terminal, navigate to the directory containing the downloaded Miniconda installation file. Then, you can simply type `sh Miniconda*.sh` and follow the steps prompted. You will be asked to accept the license and enter your installation location. If you don’t have any preferred location then the installer will install Miniconda in your home directory.

<p align="center">
 <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/intro-python/mc1.jpeg">
</p>
<p align="center">
 <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/intro-python/mc2.jpeg">
</p>

{% include google-adsense-inarticle.html %}

<p align="center">
 <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/intro-python/mc3.jpeg">
</p>

### Miniconda Install

Now, Miniconda, as well as Python 3.6, has been installed on your machine. We need some more Python libraries to get going. We can easily install these now using Miniconda. Open your terminal and type `conda install jupyter notebook pandas numpy matplotlib`.

We now have all the necessary libraries to get started with Python. Let us open a terminal again and simply type `jupyter notebook` to launch jupyter notebook. Jupyter notebook is a very popular interface which makes using Python a fun experience. It has all the features to make things simpler and useful. You can even run the shell command in the notebook. Over that, you can write your notes using the Markdown language, which is a very straight-forward language for writing. I strongly recommend you to learn Markdown. It won’t take more than 10 minutes to learn and will be useful in so many other places.

## First Python Script

Now, that we have all the necessary tools to use Python then let’s use python to make a very simple plot.

<ol>
<li>First, start jupyter notebook by typing <code>jupyter notebook</code> on your terminal.</li>

<p align="center">
 <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/intro-python/jup1.jpeg">
</p>

<p align="center">
 <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/intro-python/jup2.jpeg">
</p>

It will open <code>Jupyter</code> in your default browser.

<li>Now, go to the “New” tab at the top right corner and then select “Python 3”. It will open a new page for you.</li>

<p align="center">
 <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/intro-python/jup3.jpeg">
</p>

<li>Let’s import some libraries which we have installed using the conda by typing the command as directed in the figure below. To execute the command, use the <code>Command/Ctrl + Enter</code> key.</li>

<p align="center">
 <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/intro-python/jup4.jpeg">
</p>

<li>We also need to execute the command <code>%matplotlib inline</code> to keep our plots inline in the notebook. This is one of the many features of jupyter notebook.</li>

<p align="center">
 <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/intro-python/jup5.jpeg">
</p>

<li>Let’s define our x and y values using the [numpy](/utilities/introduction-to-scientific-computing-using-numpy-python/) library which we have imported as <code>np</code> for short-form.</li>

<p align="center">
 <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/intro-python/jup6.jpeg">
</p>

<li>Let’s plot our data.</li>

<p align="center">
 <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/intro-python/jup7.jpeg">
</p>
</ol>

{% include google-adsense-inarticle.html %}
