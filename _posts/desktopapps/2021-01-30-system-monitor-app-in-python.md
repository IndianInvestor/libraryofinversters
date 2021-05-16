---
title: "A simple system monitor app in Python (codes included)"
date: 2021-1-30
tags: [python, desktopApp, PyQt5, pyqtgraph]
excerpt: "A simple Python app for system CPU and RAM usage monitoring in real time. The app is build mainly using the PyQt5, pyqtgraph and psutil."
mathjax: "true"
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/systemMonitorApp_screenShot1.jpg"
classes:
  - wide
sidebar:
  nav: "all_posts_list"
category: desktopapps
---

{% include toc %}

<iframe width="420" height="300"
 src="https://www.youtube.com/embed/vfFv6BceAes?autoplay=1&mute=1">
</iframe>

## Introduction

In this post, I built a simple python application for system CPU and RAM usage monitoring in real time. The app is built mainly using the `PyQt5`, `pyqtgraph` and `psutil`. Similar application comes by default in Windows (Task Manager) and Mac (Activity Monitor). System Monitor is cross-platform compatible so you can run it on all platforms. It offers a new visualization tool for Linux, Windows and Mac. 

{% include google-adsense-inarticle.html %}

The starting window design has been borrowed from the github repo [Python_PySide2_Circular_ProgressBar_Modern_GUI](https://github.com/Wanderson-Magalhaes/Python_PySide2_Circular_ProgressBar_Modern_GUI). For more details on how to design the window, please watch [Modern GUI - Python, Qt Designer and PySide2](https://youtu.be/zUnrLHbYmKA).

## Install libraries

```
python -m venv systemApp
source systemApp/bin/activate
pip install PyQt5 pyqtgraph psutil
```

### Download codes

You can download the windows installer from: [Downloads Page]("{{ site.url }}{{ site.baseurl }}/downloads/#systemMonitorApp")

Download source code from my GitHub Repo:
<a href="https://github.com/earthinversion/SystemMonitorApp" download="Codes">
<img src="https://img.icons8.com/carbon-copy/100/000000/download-2.png" alt="systemMonitor" width="40" height="40">

<p align="center">
 <img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/systemMonitorApp_screenShot1.jpg">
</p>

{% include google-adsense-inarticle.html %}
