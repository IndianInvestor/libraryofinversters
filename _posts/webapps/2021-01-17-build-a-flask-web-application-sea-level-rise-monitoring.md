---
title: "Build a Flask Web Application: Sea Level Rise Monitoring (codes included)"
date: 2021-1-17
tags: [flask, python, webapp, deploy, heroku, slrm]
excerpt: "This post gives a quick introduction on how to build a web application using Flask and deploy on Heroku server. Then, I share my codes for building advanced web application for sea-level rise monitoring."
mathjax: "true"
header:
  teaser: "https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/slrm/SLRM-webapp/slrm_webApp.png"
classes:
  - wide
sidebar:
  nav: "all_posts_list"
category: webapps
redirect_from:
  - /webapps/build-a-flask-app-slrm/
---

{% include toc %}

## Video

<iframe width="420" height="300"
 src="https://www.youtube.com/embed/3qPQRxO9s2k?autoplay=1&mute=1">
</iframe>

## Introduction

In this post, I will give a quick introduction of how to build a web app using Flask. [Flask](https://flask.palletsprojects.com/en/1.1.x/) is a web framework written in Python. It is not as mature as Django (the other popular Python web framework) as it lacks database abstraction layer, form validation, or direct integration with the pre-existing third party libraries. But, it is very easy to learn for beginners and can be made to work with third party libraries with some easy tweaks. As, this post is not about the differences between Flask and Django, so I will skip this part.

{% include google-adsense-inarticle.html %}

For more details on how to use Flask, visit [Flask Tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/).

Or for the detailed tutorial, visit [miguelgrinberg.com](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

## Build your first flask application

```
python -m venv venv
source venv/bin/activate
pip install flask
```

{% include google-adsense-inarticle.html %}

### Create a package

In Python, a directory that contains `__init__.py` is considered a package and can be imported to build an app (in this case).

`app/__init__.py`

```python
from flask import Flask
app = Flask(__name__) #the name of the module and necessary to configure Flask
from app import routes
```

Then you need to create the files:

`app/routes.py`

```python
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
```

`run.py`

```python
from app import app

if __name__=="__main__":
    app.run(debug=True)
```

At this level, your project directory should look like this:

```
hello-world-app
├── app
│   ├── __init__.py
│   ├── __pycache__
│   └── routes.py
├── run.py
└── venv

```

{% include google-adsense-inarticle.html %}

### Execute the app

So, your first app is ready. You can run the app by simply executing

```
python run.py
```

This will return:

```
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 124-492-379
```

You can copy and paste the `http://127.0.0.1:5000/` into your preferred browser to view the return of this application. In this case, it will simply print `Hello, World`. Next, we structure this application with some html templates with the help of Jinja2. Jinga is a template engine for the Python and handles templates in a [sandbox](<https://en.wikipedia.org/wiki/Sandbox_(computer_security)>).

## Preview of SLRM application

<p align="center">
    <a href="https://slrm.herokuapp.com/" style="text-decoration: none;"><img width="80%" src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/slrm/SLRM-webapp/slrm_webApp.png"></a>
  </p>

{% include google-adsense-inarticle.html %}
  
## Download SLRM Codes

Source Code: <a href="https://github.com/earthinversion/Sea-Level-Rise-Monitoring-Web-Application-Source-Code" download="Codes" onclick="ga('send','pageview','/webapps/build-a-flask-app-slrm/');">
<img src="https://img.icons8.com/carbon-copy/100/000000/download-2.png" alt="slrm" width="40" height="40">

```
git clone https://github.com/earthinversion/Sea-Level-Rise-Monitoring-Web-Application-Source-Code.git
```

Please note that SLRM application uses several other libraries inclduing the `boto3` API (for storing data into AWS-S3). This post do not deal with the description of the installation and use of the `boto3` API. But a look into the SLRM project directory may help you in building advanced apps.

## How to deploy the app

Let us deploy the app on [Heroku](https://www.heroku.com/) using `git`.

Heroku is a cloud platform supporting several programming languages. It allows a developer to build, run, and scale different applications. Heroku hosts its services on the Amazon’s EC2 cloud computing platform. The Heroku applications have a unique domain name “appname.herokuapp.com” which routes the run requests to the correct application containers or “dynos”.

For deploying an app on the Heroku server, we first need to install Heroku on the local computer. On Mac, just install using the Heroku and Git installer and it should do the job.

### Change directory to the Sea-Level-Rise-Monitoring-Web-Application-Source-Code

```
cd Sea-Level-Rise-Monitoring-Web-Application-Source-Code/
```

### Initialize the git and create virtual environment locally

```
git init
python -m venv venv #create a virtual environent
source venv/bin/activate #activate the virtual environment
```

`virtualenv` creates a fresh Python instance. You need to install all the Python dependencies. The dependencies are listed in the `requirements.txt` file.

```
arrow==0.15.2
asn1crypto==1.1.0
beautifulsoup4==4.8.1
bibtexparser==1.1.0
boto3==1.9.248
botocore==1.12.248
certifi==2019.9.11
cffi==1.12.3
chardet==3.0.4
Click==7.0
cryptography==2.7
docutils==0.15.2
Flask==1.1.1
future==0.18.0
gunicorn==19.9.0
idna==2.8
itsdangerous==1.1.0
Jinja2==2.10.3
jmespath==0.9.4
MarkupSafe==1.1.1
numpy==1.17.2
pandas==0.25.1
pycparser==2.19
pyOpenSSL==19.0.0
pyparsing==2.4.2
python-dateutil==2.8.0
pytz==2019.3
requests==2.22.0
s3transfer==0.2.1
scholarly==0.2.5
six==1.12.0
soupsieve==1.9.4
urllib3==1.25.6
Werkzeug==0.16.0
```

All these dependencies can be quickly installed using the command:

```
pip install -r requirements.txt
```

### Prepare the folder

For the app to be deployed, you need the following file:

<ul>
    <li><code>run.py</code>: this file reads the `slrm` app that exists in the directory `app`</li>
    <li><code>.gitignore</code>: to ignore all the files you don't want to deploy on the server</li>
    <li>
    <code>Procfile</code>:
    <pre>
      <code>
       web: gunicorn run:app
      </code>
    </pre>
    </li>
    <li>
    <code>requirements.txt</code>:
    <pre>
      <code>
        pip freeze > requirements.txt
      </code>
    </pre>
    </li>
</ul>

### Deploy on Heroku

```
heroku create slrm-app # change slrm-app to a unique name
git add . # add all files to git
git commit -m 'Initial app boilerplate'
git push heroku master # deploy code to heroku
heroku ps:scale web=1  # run the app with a 1 heroku "dyno"
```

Then, you should be able to view the app on `https://slrm-app.herokuapp.com`.

## Edit the app

You can edit and redeploy the app, following:

```
git status # view the changes
git add .  # add all the changes
git commit -m 'a description of the changes'
git push heroku master
```
