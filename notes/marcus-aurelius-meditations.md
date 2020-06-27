---
title: >
  _The Meditations_ of Marcus Aurelius
description: >
  Notes on _The Meditations_
---

<style>
.book:empty{display:none}
</style>

## Epistemeology

{% for belief in site.data.meditations.epistemology %}
{{ forloop.index }}. {{ belief.label }} (<a href="#top" onclick="justify([
{%- for j in belief.justification %}[{{ j[0]|minus:1 }}, {{ j[1]|minus:1 }},],{%- endfor -%}
])">view {{ belief.justification|size }} related sections</a>)
{%- endfor %}

## Metaphysics

{% for belief in site.data.meditations.metaphysics %}
{{ forloop.index }}. {{ belief.label }} (<a href="#top" onclick="justify([
{%- for j in belief.justification %}[{{ j[0]|minus:1 }}, {{ j[1]|minus:1 }},],{%- endfor -%}
])">view {{ belief.justification|size }} related sections</a>)
{%- endfor %}

## Ethics

{% for belief in site.data.meditations.ethics %}
{{ forloop.index }}. {{ belief.label }} (<a href="#top" onclick="justify([
{%- for j in belief.justification %}[{{ j[0]|minus:1 }}, {{ j[1]|minus:1 }},],{%- endfor -%}
])">view {{ belief.justification|size }} related sections</a>)
{%- endfor %}

<a href="#top" onclick="showAll()">Show all sections</a>

<span id="top"></span>

{% for book in site.data.meditations.book %}
<h2 class="book-header">Book {{ forloop.index }}</h2>

<ol class="book">
{%- for section in book -%}
<li value="{{ forloop.index }}">{{ section }}</li>
{% endfor %}
</ol>
{%- endfor %}

<script>
lists=document.getElementsByClassName("book")
headers=document.getElementsByClassName("book-header")
books=[]
for(i=0;i<12;i++)books.push(lists[i].children)
function justify(justification){
  for(b=0;b<books.length;b++){
    bd='none'
    for(s=0;s<books[b].length;s++){
      sd='none'
      for(j=0;j<justification.length;j++){
        if(justification[j][0] == b && justification[j][1] == s){
          sd=null
          bd=null
        }
      }
      books[b][s].style.display=sd
    }
    lists[b].style.display=bd
    headers[b].style.display=bd
  }
}
function showAll() {
  for (b=0;b<books.length;b++) {
    lists[b].style.display=null
    headers[b].style.display=null
    for (s=0;s<books[b].length;s++)
      books[b][s].style.display=null
  }
}
</script>
