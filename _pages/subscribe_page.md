---
title: ""
permalink: "/subscribe-page/"
meta_val: nodisclaimer
sidebar:
  nav: "all_posts_list"
classes:
  - wide
---

<p align="center">
  <img src="https://raw.githubusercontent.com/earthinversion/earthinversion-images/main/images/boy-with-board-sign-subscribe-illustration.png" alt="Subscribe" style="width:90%">
</p>

<div class="container-cf">
    <form onsubmit="sendEmail(event)" style="background-color: rgba(126,211,33,.5);">
        <div id="alert-field" class="alert hidden">
            <p>Uh oh! Something went wrong!</p>
        </div>
        <div class="newsletter-container">
            <input type="text" class="form-control" id="name-field" name="name-field" placeholder="Your name" style="background: #fafafa;" required>
            <input type="email" class="form-control" id="email-field" name="email-field" style="background: #fafafa;" placeholder="Email address" required>
			{% if page.title %}
	        <input type="hidden" value="{{ site.url }}{{ site.baseurl }}/{{ page.title }}" name="page-field"/>
			{% else %}
			<input type="hidden" value="{{ site.url }}{{ site.baseurl }}/{{ page.layout }}" name="page-field"/>
			{% endif %}
			
            <input id="subsc" type="submit" style="float: right; background: #3b9cba;"  value="Subscribe"/>
        </div>
        
    </form> 
</div>

Hi There,

My name is Utpal Kumar, PhD. I write blog articles that teach beginner/intermediate programming related to mainly geosciences and data science, in general.

Topics included in my blog:

- Introduction to programming languages such as Python, MATLAB, Bash, and more (coming soon).
- Techniques and methods used in geophysics
- Tutorials for plotting publication-quality maps and figures

Your subscription to this blog will motivate me to work on more high-quality educational articles faster. I promise not to spam you with a lot of emails.

Thank You!

<p align="center" style="margin-top: 0;"><a href="https://www.earthinversion.com/contact-form/" class="btn btn--success btn--small" style="font-size:1.0em; background: #3b9cba; padding: 5px;">Get in Touch</a></p>

<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>
<script  src="{{ site.url }}{{ site.baseurl }}/custom-js/subscribeForm.js"></script>
