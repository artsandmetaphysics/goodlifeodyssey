SHELL := /bin/bash -o pipefail -e
.SUFFIXES:

.PHONY: notion

notion: n2y.yml
	@mkdir -p docs
	n2y n2y.yml --verbosity=WARNING

.PHONY: clean

clean:
	rm -rf docs/*.html
