---
title: >
  _The Meditations_ of Marcus Aurelius
description: >
  Notes on _The Meditations_
---

<style>
.book:empty{display:none}
</style>

Marcus Aurelius was a Roman emperor and a philosopher. _The Meditations_, as they are commonly referred too, were his personal journal. He likely wrote them between 161 and 180 AD, and probably did not plan on publishing them. Thus, they provide a sincere view into the thoughts and daily struggles of a practicing stoic.

After the first chapter, which is a list of influential people in Marcus' life, _The Meditations_ are unstructured and repetitive. While it may be a foolish endeavor, since they were not meant to be systematic, I have attempted to identify and categorize Marcus' core beliefs. Many other divisions are possible.

Marcus writes little about how he knows what he knows (epistemology). His focus is how he should act (ethics), but often he explains why he should act a certain way, and in so doing he tells us how he viewed reality (metaphysics). I present his beliefs within these three domains.

All twelve books of George Long's translation of _The Meditations_ are presented below. (I have lightly modernized the English.) After each belief in parenthesis is listed the number of sections relating to this belief. Click on the number to filter out all unrelated sections. Many sections are connected to multiple beliefs. There are also links which show all the sections and (more interestingly) the sections which I was unable to categorize.

## Epistemological Beliefs

<ol>
{% for belief in site.data.meditations.epistemology -%}
<li>
  {{ belief.label }} (<a href="#top" onclick="showOnly([
{%- for j in belief.justification %}[{{ j[0]|minus:1 }}, {{ j[1]|minus:1 }},],{%- endfor -%}
])">{{ belief.justification|size }}</a>)
</li>
{%- endfor %}
</ol>

## Metaphysical Beliefs

<ol>
{% for belief in site.data.meditations.metaphysics -%}
<li>
  {{ belief.label }} (<a href="#top" onclick="showOnly([
{%- for j in belief.justification %}[{{ j[0]|minus:1 }}, {{ j[1]|minus:1 }},],{%- endfor -%}
])">{{ belief.justification|size }}</a>)
</li>
{%- endfor %}
</ol>

## Ethical Beliefs

<ol>
{% for belief in site.data.meditations.ethics -%}
<li>
  {{ belief.label }} (<a href="#top" onclick="showOnly([
{%- for j in belief.justification %}[{{ j[0]|minus:1 }}, {{ j[1]|minus:1 }},],{%- endfor -%}
])">{{ belief.justification|size }}</a>)
</li>
{%- endfor %}
</ol>

<p><a href="#top" onclick="showExcept([])">Show all sections.</a></p>
<p><a href="#top" onclick="showNonMapped()">Show sections not referring to any belief.</a></p>

<span id="top"></span>

{% for book in site.data.meditations.book %}
<h2 class="book-header">Book {{ forloop.index }}</h2>

<ol class="book">
{%- for section in book -%}
<li value="{{ forloop.index }}">{{ section|markdownify }}</li>
{% endfor %}
</ol>
{%- endfor %}

<script>
lists=document.getElementsByClassName("book")
headers=document.getElementsByClassName("book-header")
books=[]
for(i=0;i<12;i++)books.push(lists[i].children)
function showOnly(sections){
  for(b=0;b<books.length;b++)
    for(s=0;s<books[b].length;s++){
      sd='none'
      for(j=0;j<sections.length;j++)
        if(sections[j][0] == b && sections[j][1] == s)
          sd=null
      books[b][s].style.display=sd
    }
  hideEmptyLists()
}
function showExcept(sections){
  for(b=0;b<books.length;b++)
    for(s=0;s<books[b].length;s++){
      sd=null
      for(j=0;j<sections.length;j++)
        if(sections[j][0] == b && sections[j][1] == s)
          sd='none'
      books[b][s].style.display=sd
    }
  hideEmptyLists()
}
function hideEmptyLists() {
  for(b=0;b<books.length;b++){
    bd='none'
    for(s=0;s<books[b].length;s++)
      if(books[b][s].style.display!=='none')
        bd=null
    lists[b].style.display=bd
    headers[b].style.display=bd
  }
}
function showNonMapped() {
  nonMapped=[
    {%- for belief in site.data.meditations.epistemology -%}
    {%- for j in belief.justification -%}
    [{{ j[0]|minus:1 }}, {{ j[1]|minus:1 }},],
    {%- endfor -%}
    {%- endfor -%}
    {%- for belief in site.data.meditations.metaphysics -%}
    {%- for j in belief.justification -%}
    [{{ j[0]|minus:1 }}, {{ j[1]|minus:1 }},],
    {%- endfor -%}
    {%- endfor -%}
    {%- for belief in site.data.meditations.ethics -%}
    {%- for j in belief.justification -%}
    [{{ j[0]|minus:1 }}, {{ j[1]|minus:1 }},],
    {%- endfor -%}
    {%- endfor -%}
  ]
  showExcept(nonMapped)
}
</script>
