---
title: ""
permalink: "/ei-collections/"
layout: archive
meta_val: nodisclaimer
sidebar:
  nav: "all_posts_list"
classes:
  - wide
---
 
{% assign entries1 = site["methods-algorithms"] %}
{% assign entries1 = entries1 | sort: 'date' | reverse %}

{% assign entries2 = site["plotting-tutorial"] %}
{% assign entries2 = entries2 | sort: 'date' | reverse %}

{% assign entries3 = site["obspycollection"] %}
{% assign entries3 = entries3 | sort: 'date' | reverse %}


<ul class="taxonomy__index">
  <li>
    <a href="#methods-algorithms">
      <strong>Methods and Algorithms</strong>
    </a>
  </li>

  <li>
    <a href="#plotting-tutorial">
      <strong>Mapping Tutorials</strong>
    </a>
  </li>
  <li>
    <a href="#obspy-tutorial">
      <strong>Obspy and Seismology</strong>
    </a>
  </li>
  
</ul>

<section id="methods-algorithms" class="taxonomy__section">
<h2 class="archive__subtitle" style="font-size: 1em;">Methods and Algorithms</h2>
<div class="entries-grid">
{%- for post in entries1 -%}
  {% include archive-single-collections.html type='grid' %}
{%- endfor -%}
</div>
<a href="#page-title" class="back-to-top">{{ site.data.ui-text[site.locale].back_to_top | default: 'Back to Top' }}
    &uarr;</a>
</section>



<section id="plotting-tutorial" class="taxonomy__section">
<h2 class="archive__subtitle" style="font-size: 1em;">Mapping Tutorials</h2>
<div class="entries-grid">
{%- for post in entries2 -%}
  {% include archive-single-collections.html type='grid' %}
{%- endfor -%}
</div>
<a href="#page-title" class="back-to-top">{{ site.data.ui-text[site.locale].back_to_top | default: 'Back to Top' }}
    &uarr;</a>
</section>



<section id="obspy-tutorial" class="taxonomy__section">
<h2 class="archive__subtitle" style="font-size: 1em;">Obspy and Seismology</h2>
<div class="entries-grid">
{%- for post in entries3 -%}
  {% include archive-single-collections.html type='grid' %}
{%- endfor -%}
</div>
<a href="#page-title" class="back-to-top">{{ site.data.ui-text[site.locale].back_to_top | default: 'Back to Top' }}
    &uarr;</a>
</section>


