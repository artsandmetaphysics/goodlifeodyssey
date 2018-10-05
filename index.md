---
layout: basic
title: Arts & Metaphysics
description: This website contains my essays and notes about art, history, ethics, epistemology, and metaphysics.
---
<p>{{ page.description }}</p>

{% assign groups = site.documents | group_by: 'type' | sort: 'name' %}
{% for group in groups %}
  <h2>{{ group.name | capitalize }}s</h2>
  <ul class="index">
  {% assign documents = group.items | sort: 'order' %}
  {% for d in documents  %}
    <li title="{{ d.description | xml_escape | normalize_whitespace }}">
      <a href="{{ d.url }}">{{ d.title }}</a>
    </li>
  {% endfor %}
  </ul>
{% endfor %}
