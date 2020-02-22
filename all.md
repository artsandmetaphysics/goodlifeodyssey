---
layout: basic
title: Arts & Metaphysics
description: Here is the full list of my writings, most of them are incomplete.
---
{{ page.description }}

## All Writings

{% for d in site.documents %}
<ul class="index">
  {% include li.html id=d.url %}
<ul>
{% endfor %}
