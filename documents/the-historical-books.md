---
title: Joshua, Judges, Samuel, and Kings
description: >
  Notes on the historical books of the Hebrew Bible
type: note
order: 5.101
---

<style>
main > ol{list-style-type:upper-roman}
ul:first-child{padding-left:1.4rem}
main > ul:first-child li{font-weight:normal}
main > ul:first-child > li{font-weight:bold}
.js main > ul:first-child li{cursor:pointer}
.js main > ul:first-child li li li{cursor:default}
.js .hidden-children > ul:first-child{display:none}
.hidden-no-js{display:none}
.js .hidden-no-js{display:block}
</style>

## Outline

<p class="hidden-no-js hidden-print">
  <span class="hidden-sm">Set outline depth: &nbsp;</span>
  <a href="#" onclick="setDepth(2,event)">Major Sections</a> ·
  <a href="#" onclick="setDepth(3,event)">Chapters</a>
</p>

- Joshua
  - Entrance into the land (1--5)
    - Joshua's commissioning; preparations; transjordan obligations (1)
    - Spies sent to Jericho; saved by Rahab (2)
    - Crossing the Jordan; the twelve stones (3--4
    - Circumcision; passover; cessation of manna; angel commander (5)
  - Conquest of the land (6--11)
    - Destruction of Jericho (6)
    - The sin of Achan (7)
    - Destruction of Ai; Mount Ebal offering and reading (8)
    - Gibeonites fool Joshua into forming a pact (9)
    - Destruction of the southern coalition (10)
    - Destruction of the northern coalition (11)
    - List of conquered kings (12)
  - Division of the land (13--19)
- Judges
- Samuel I
- Samuel II
- Kings I
- Kings II

## Thoughts

Josuha 5.30--35 is likely a late addition to the book, since it is placed in different parts of the story in different scrolls. A Dead Sea Scroll text places it after the second circumcisions in 5.2. The Septuagint places it after the gathering of kings in 9.2. Josephus, in _The Antiquities of the Jews_ places it after the division of land. R. Ishmael places it at the end of the book. This is concrete evidence that some edits were being made to the text after it was written. In this case, the addition makes sense since it fills in a "hole" in the story---without this passage Deuteronomy 27.3--8 is not fulfilled.

<script>
document.documentElement.classList.add('js')
ul=document.querySelectorAll('main > ul')[0]
ul.onclick=function(e){
  if(e.target.tagName === 'LI')
    e.target.classList.toggle('hidden-children')
}
function setDepth(d,e){
  e.preventDefault()
  var s=''
  while(d--){
    s+='li '
    ul.querySelectorAll(s).forEach(function(li){
      if(d!=0)
        li.classList.remove('hidden-children')
      else
        li.classList.add('hidden-children')
    })
  }
}
</script>
