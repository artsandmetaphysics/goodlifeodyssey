# Arts and Metaphysics

## Design Goals

- Minimal styling so that myself (and other readers) can focus on the content
- Make it possible to read the documents:
  - on a laptop
  - on a phone
  - in "reader mode"
  - printed copy of the document
- Allow me to write in a version of markdown that is tailored for my needs
- Provide detailed citations of quoted material in the most minimally invasive way possible

## Building

Run `make` to compile static assets.

Start a test server using `run`.

## Typographical Substitutions

- `---` is replaced with an "em dash"
- `--` is replaced with an "en dash"
- `...` at the start of a line is replaced with "centered triple dots"

## Citations

Invisible citations are only displayed when the user hovers over the quote with their mouse or prints the material.

The final line or two of a quote should contain the citation:

- Poetry with a visible citation: `===`
- Poetry with a invisible citation: `==`
- Quote with a invisible citation: `---`
- Quote with a visible citation: `--`

You can include both a visible and invisible citation, e.g. if you want to include more details in the invisible citation.  If both an invisible and visible citation are present, the printed form of the document will have "Visible, Hidden" as its citation.

## References

References are in pseudo form of the Oxford Style.  I prune some stuff that isn't necessary (e.g. who cares about the publisher these days, lots of books are self-published).  See [this site](http://guides.library.uwa.edu.au/c.php?g=325241&p=2177430) for examples.

## Open Issues

- Make blockquotes look good in safari reader mode
- Mechanism to insert smart quotes, instead of straight ones
- Deal with visible and invisible citations when you print a document
- Italics inside markdown blockquotes
- Simplify blockquote CSS
- Means to view citations on mobile
