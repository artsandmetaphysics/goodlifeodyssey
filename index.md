---
layout: basic
title: Good Life Odyssey
description: My search for the good life in philosophy, religion, literature, and history.
---
{{ page.description }}

<h2 id="essays">Essays</h2>
<ul class="index">
  {% include li.html id='definitions' %}
  {% include li.html id='justification-via-others-beliefs' %}
  {% include li.html id='beauty-and-truth' %}
  {% include li.html id='my-epistemology' %}
  {% include li.html id='universal-historical-laws' %}
  {% include li.html id='meaning-and-purpose' %}
  {% include li.html id='a-definition-of-faith' %}
  {% include li.html id='faith-and-reason' %}
  {% include li.html id='faith-and-righteousness' %}
  {% include li.html id='fear-of-death' %}
  {% include li.html id='ethical-progress' %}
  {% include li.html id='justice' %}
  {% include li.html id='love-thy-neighbor-as-thyself' %}
</ul>

<h2 id="meditations">Meditations</h2>
<ul class="index">
  {%- for p in site.posts -%}
  <li>
    <a title="{{ p.description | xml_escape | normalize_whitespace }}"
       href="{{ p.url }}">{{ p.title | replace_first: "_", "<em>" | replace: " _", " <em>" | replace: "_", "</em>" | normalize_whitespace }}</a>
  </li>
  {%- endfor -%}
</ul>

<h2 id="notes">Notes and Commentary</h2>
<ul class="index">
  {% include li.html id='ancient-greece' %}
  {% include li.html id='the-epic-of-gilgamesh' %}
  {% include li.html id='hesiod' %}
  {% include li.html id='the-iliad' %}
  {% include li.html id='the-odyssey' %}
  {% include li.html id='homeric-hymns' %}
  {% include li.html id='the-histories-herodotus' %}
  {% include li.html id='metamorphoses' %}
  {% include li.html id='seneca' %}
</ul>
