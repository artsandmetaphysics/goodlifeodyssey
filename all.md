---
layout: basic
title: All Pieces
description: Here is the full list of my writing, most of them are incomplete.
---
{{ page.description }}

## All Writings

{% assign groups = site.documents | group_by: 'type' | sort: 'name' %}
{% for group in groups %}
  <h2>{{ group.name | capitalize }}s</h2>
  <ul class="index">
  {% assign documents = group.items | sort: 'title' %}
  {% for d in documents  %}
    <li>
      <a title="{{ d.description | xml_escape | normalize_whitespace }}"
         href="{{ d.url }}">{{ d.title }}</a>
    </li>
  {% endfor %}
  </ul>
{% endfor %}
