---
layout: basic
title: Essays
description: A collection of my essays about epistemology, metaphysics, and ethics.
---
{{ page.description }}

{% for e in site.essays %}
- [{{ e.title }}]({{ e.url }})
{% endfor %}
