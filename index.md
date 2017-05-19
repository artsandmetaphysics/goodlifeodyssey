---
layout: basic
title: Essays
description: My essays about art, ethics, epistemology, and metaphysics.
---
{{ page.description }}

{% for e in site.essays %}
- [{{ e.title }}]({{ e.url }})
{% endfor %}

<a href="mailto:wei.ge.thoughts@gmail.com">Contact Me</a>
