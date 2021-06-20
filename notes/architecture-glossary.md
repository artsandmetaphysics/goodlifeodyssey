---
title: >
  Glossary of Architectural Terms
description: >
  Glossary of Architectural Terms
terms:
  balustrade: >-
    A railing supported by balusters, especially an ornamental parapet on a
    balcony, bridge, or terrace.
  baluster: >-
    A short pillar or column, typically decorative in design, in a series
    supporting a rail or coping.
  parapet: >-
    A low protective wall along the edge of a roof, bridge, or balcony.
  quoining: >-
    The stone or brick used to form the external angle of a wall or building.
  finial: >-
    A distinctive ornament at the apex of a roof, pinnacle, canopy, or similar
    structure in a building. From latin _finis_ "end".
  cupola: >-
    A small dome, especially a small dome on a drum on top of a larger dome,
    adorning a roof or ceiling.
  cresting: >-
    An ornamental decoration at the ridge of a roof or top of a wall or screen.
  dormer: >-
    A window that projects vertically from a sloping roof. From Old French
    _dormeor_ "dormitory", from _dormir_ "to sleep".
  pilaster: >-
    A rectangular column, especially one projecting from a wall.
  mullion: >-
    A vertical bar between the panes of glass in a window.
  transom: >-
    A strengthening crossbar, in particular one set above a window or door.
  cartouches: >-
    A carved tablet representing a scroll with rolled-up ends, used
    ornamentally. From Latin _carta_.
  spandrel: >-
    The almost triangular space between one side of the outer curve of an arch,
    a wall, and the ceiling or framework.
  putti: >-
    A represesentation of a naked child. Singular putto. From Italian "boy", from
    Latin _putus_.
  clerestory: >-
    A high section of wall that contains windows above eye level to admit light
    or fresh air. Historically, it denoted an upper level of a Roman basilica
    or the nave of a Romanesque or Gothic church.
---

One of life's joys is looking at the wonderful complexity around us. Living in New York City, you're surrounded by buildings---old and new, big and small, plain and ornate. I stumbled across the city's map of landmarks that includes a historical and architectural report of each designated building. These reports are fun to read and point out details we wouldn't have noticed otherwise. They also use many architectural terms, which we've begun collecting in this glossary.

Why bother, one may ask, learning these unusual words? While one can enjoy looking at the buildings without them, they help me notice and talk about the details. I notice _quoining_ now that I know the term.

<dl>
  {% for term in page.terms %}
  <dt>{{ term[0] | markdownify }}</dt>
  <dd>{{ term[1] | markdownify }}</dd>
  {% endfor %}
</dl>
