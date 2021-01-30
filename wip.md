---
layout: basic
title: All Writings
description: The full list of my written works, many incomplete or off topic.
---
{{ page.description }}

{% assign collections = site.collections | sort: 'name' %}
{%- for collection in collections -%}
{%- assign name = collection.label -%}
{%- unless name contains 'posts' %}
<h2>{{ name | capitalize }}</h2>
<ul class="index">
{%- for d in collection.docs -%}
{% include li.html doc=d %}
{%- endfor -%}
{%- endunless -%}
{%- endfor -%}
