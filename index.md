---
layout: basic
title: Arts & Metaphysics
description: This website contains my essays and notes about art, history, ethics, epistemology, and metaphysics.
---
<p>{{ page.description }}  Asterisks indicate essays that are incomplete or unedited.</p>

<h2>Essays</h2>

<ul class="index">
{% assign essays = site.essays | sort: 'order' %}
{% for e in essays %}
  {% if e.status != 'hidden' %}
  <li title="{{ e.description | xml_escape | normalize_whitespace }}">
    <a href="{{ e.url }}">{{ e.title }}</a>
    {% if e.status == 'incomplete' %}*{% endif %}
  </li>
  {% endif %}
{% endfor %}
</ul>

<h2>Notes</h2>

<p></p>

<ul class="index">
{% assign notes = site.notes | sort: 'order' %}
{% for n in notes %}
  {% if e.status != 'hidden' %}
  <li title="{{ n.description | xml_escape | normalize_whitespace }}">
    <a href="{{ n.url }}">{{ n.title }}</a>
  </li>
  {% endif %}
{% endfor %}
</ul>
