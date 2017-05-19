---
layout: basic
title: Essays
description: A collection of my essays about epistemology, metaphysics, ethics, and art.
---
{{ page.description }}

{% for e in site.essays %}
- [{{ e.title }}]({{ e.url }})
{% endfor %}
