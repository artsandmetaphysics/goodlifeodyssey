SHELL := /bin/bash -o pipefail -e
.SUFFIXES:

.PHONY: notion

notion: n2y.yml
	@mkdir -p _published
	n2y n2y.yml --verbosity=WARNING

.PHONY: clean cleannotion

clean:
	rm -rf _site

cleannotion:
	rm -rf _published index.md about.md  # update if new pages are added
