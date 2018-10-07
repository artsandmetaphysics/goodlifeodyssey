# Arts and Metaphysics

## Design Goals

- Minimal styling so that myself (and other readers) can focus on the content
- Optimize reading the documents:
  - on a laptop
  - on a phone
  - printed copy of the document
- Allow me to write in a version of markdown that is tailored for my needs

## Building

Run `make` to compile static assets.

Start a test server using `run`.

## Typographical Substitutions

- `---` is replaced with an "em dash"
- `--` is replaced with an "en dash"
- `...` at the start of a line is replaced with "centered triple dots"
- Straight quotes are replaced with curly quotes everywhere, except in the YAML front matter.

## Citations

The final line of a quote indicates whether it is poetry and may contain a citation:

- Quote with citation: `-- This is a non-poetry quote`
- Poetry with citation: `== This is poetry`
- Poetry without a citation `==`

## References

References are in pseudo form of the Oxford Style.  I prune some stuff that isn't necessary (e.g. who cares about the publisher these days, lots of books are self-published).  See [this site](http://guides.library.uwa.edu.au/c.php?g=325241&p=2177430) for examples.

## Open Issues

- Italics inside markdown blockquotes

## Known Issues

- Quoted poetry has extra new lines in Safari "Reader Mode."
