---
layout: basic
title: Essays
description: This website contains my essays about art, ethics, epistemology, and metaphysics.
---
<p>{{ page.description }}  Asterisks indicate those which are incomplete or especially crude.</p>

<ul class="essay-list">
{% assign essays = site.essays | sort: 'order' %}
{% for e in essays %}
  <li>
    <a href="{{ e.url }}">{{ e.title }}</a>
    {% if e.status == 'incomplete' %}*{% endif %}
  </li>
{% endfor %}
</ul>
