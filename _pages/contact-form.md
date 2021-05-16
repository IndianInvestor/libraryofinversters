---
title: "Get in Touch"
permalink: "/contact-form/"
layout: archive
classes: wide
sidebar:
  nav: "all_posts_list"
---

<h3>Please note that</h3>
<p>I do blogging as a hobby along with full-time research job. So, I may not be able to give you personal tutoring. I apologize for delayed or no reply to your valuable emails. I hope you understand. </p>

<p>However, I love to read your emails, especially new ideas and suggestions for improvements</p>

<br><br>


<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css'>

<div class="container-cf" style="margin: 0;">
  <form onsubmit="sendEmail(event)" style="padding: 0;">
    <div id="alert-field" class="alert hidden">
      <p>Uh oh! Something went wrong!</p>
    </div>    
    <div class="contact-container">
    <div class="form-group col-xs-6">
      <label for="name-field">Name</label>
      <input type="text" class="form-control" id="name-field" name="name-field" placeholder="Your name" style="transition: all 0.5s;" required>
    </div>
    
  <div class="form-group col-xs-6">
    <label for="email-field">Email</label>
    <input type="email" class="form-control" id="email-field" name="email-field" style="transition: all 0.5s;" placeholder="Email address" required>
  </div>
  
  <div id="subject-select" class="form-group col-xs-12">
    <label for="subject-field">Subject</label>
    <select class="form-control" name="subject-field" onchange="changeSubject(event)"  required>
      <option value="Questions">Suggestions or ideas?</option>
      <option value="ResearchOpportunity">Research Opportunity</option>
      <option value="Other">Other</option>
    </select>
  </div>
  
  <div id="hidden-other-subject" class="form-group col-xs-6 hidden">
    <label for="other-subject-field">Other</label>
    <input type="text" class="form-control" id="other-subject-field" name="other-subject-field" style="transition: all 0.5s;" placeholder="Other subject" />
  </div>
  
  <div class="form-group col-xs-12">
    <label for="body-field">Message</label>
    <textarea id="body-field" name="body-field" class="form-control" placeholder="Type your message here" required></textarea>
  </div>
  
  <div class="form-group col-xs-12">
    <button type="submit" class="btn btn-primary btn-lg btn-block">Submit</button>  
  </div>
  </div>
    
  </form>
</div>
<!-- partial -->
<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>
<script  src="{{ site.url }}{{ site.baseurl }}/custom-js/contactForm.js"></script>
