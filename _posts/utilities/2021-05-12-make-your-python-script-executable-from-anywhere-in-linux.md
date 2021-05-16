---
title: "Make your Python script executable from anywhere in Linux"
date: 2021-05-12
tags: [python, executable]
excerpt: "Follow the instructions to make your python script executable from anywhere in Linux system."
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/convert-python-scripts-to-executable-file.jpg"
classes:
  - wide
sidebar:
  nav: "all_posts_list"
category: utilities
---

{% include toc %}
Python makes life so easy to write scripts for our desired outputs. Sometimes, we simply write a Python utility program that we want access from anywhere in the whole system. I will go through the series of steps you can follow to make your Python script executable in Linux (or Unix-like) system. 


## Define the shebang as the python path
We use shebang (or `#!`) a lot in computing. When a text file with a shebang is used as if it is an executable in a Linux, the program loader mechanism parses the rest of the file's initial line as an interpreter directive.

We can make use of this concept. I added the path to the anaconda python (for the specific environment) as the first line of my Python script. The python script will look like below:

```python
#!/home/utpal/miniconda3/envs/stadenv/bin/python
import os, glob
### rest of the script
```

In addition to this, you will have to make the script executable in linux:
```
chmod +x myscript.py
```

## Create environment in the home directory
In your terminal, type:

```
cd ~/ #navigate to the home directory
mkdir bin
```

Now, open the `~/.bashrc` file in your favourite editor.
```
code ~/.bashrc #to open the bashrc file using vscode
```

Now, add your bin directory to the system `PATH`.
```
export PATH="$HOME/bin:$PATH"
```

## Bring the python script in the system path
Finally, all we have to do is to copy the script to the system path (the bin directory).

```
cp myscript.py ~/bin/
```

Now, restart your terminal and you should have access to the Python script from any location on your system.

