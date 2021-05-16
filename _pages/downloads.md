---
title: "Downloads"
permalink: "/downloads/"
layout: archive
meta_val: nodisclaimer
sidebar:
  nav: "all_posts_list"
classes:
  - wide
---


{% assign entries1 = site["downloads"] %}
{% assign entries1 = entries1 | sort: 'date' | reverse %}


<section id="downloads" class="taxonomy__section">
<div class="entries-grid">
{%- for post in entries1 -%}
  {% include archive-single.html type='grid' %}
{%- endfor -%}
</div>
<a href="#page-title" class="back-to-top">{{ site.data.ui-text[site.locale].back_to_top | default: 'Back to Top' }}
    &uarr;</a>
</section>

