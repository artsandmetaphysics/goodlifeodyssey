---
layout: basic
title: Good Life Odyssey
description: My search for the good life in philosophy, religion, literature, and history.

---
We are on a long journey to find and live the _good life_. For most of us, our destination is behind a haze, and we must navigate while traveling.

This website is my logbook of landings within philosophy, religion, literature, and history.

<h2 id="essays">Essays</h2>
<ul class="index">
  {% for p in site.data.index.essays %}
  {% include li_by_id.html id=p %}
  {% endfor %}
</ul>

<h2 id="dialogues">Dialogues</h2>
<ul class="index">
  {% for p in site.data.index.dialogues %}
  {% include li_by_id.html id=p %}
  {% endfor %}
</ul>

<h2 id="meditations">Meditations</h2>
<ul class="index">
  {% for p in site.data.index.meditations %}
  {% include li_by_id.html id=p %}
  {% endfor %}
</ul>

<h2 id="poems">Poems</h2>
<ul class="index">
  {% for p in site.data.index.poems %}
  {% include li_by_id.html id=p %}
  {% endfor %}
</ul>

<h2 id="notes">Notes, Quotes, and Commentary</h2>
<ul class="index">
  {% for p in site.data.index.notes %}
  {% include li_by_id.html id=p %}
  {% endfor %}
</ul>
