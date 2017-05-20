---
layout: basic
title: Essays
description: My essays about art, ethics, epistemology, and metaphysics.
---
{{ page.description }}

<ul class="list-unstyled">
{% for e in site.essays %}
  <li><a href="{{ e.url }}">{{ e.title }}</a></li>
{% endfor %}
</ul>

<footer>
  <a href="mailto:wei.ge.thoughts@gmail.com">Contact Me</a>
</footer>
