---
layout: basic
title: Arts & Metaphysics
description: This website contains my essays about art, history, ethics, epistemology, and metaphysics.
---
<p>{{ page.description }}  Asterisks indicate essays that are incomplete or unedited.</p>

<ul id="essays">
{% assign essays = site.essays | sort: 'order' %}
{% for e in essays %}
  <li title="{{ e.description | xml_escape | normalize_whitespace }}">
    <a href="{{ e.url }}">{{ e.title }}</a>
    {% if e.status == 'incomplete' %}*{% endif %}
  </li>
{% endfor %}
</ul>
