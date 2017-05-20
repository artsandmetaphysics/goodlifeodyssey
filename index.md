---
layout: basic
title: Essays
description: My essays about art, ethics, epistemology, and metaphysics.
---
{{ page.description }}  Asterisks indicate those which are incomplete or especially crude.

<ul class="essay-list">
{% assign essays = site.essays | sort: 'order' %}
{% for e in essays %}
  <li>
      <a href="{{ e.url }}">{{ e.title }}</a>
      {% if e.status == 'incomplete' %}*{% endif %}
  </li>
{% endfor %}
</ul>

<footer>
  <a href="mailto:wei.ge.thoughts@gmail.com">Contact Me</a>
</footer>
