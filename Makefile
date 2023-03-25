SHELL := /bin/bash -o pipefail -e
.SUFFIXES:

CSSMIN_BIN := node_modules/clean-css-cli/bin/cleancss
IMGMIN_BIN := node_modules/imagemin-cli/cli.js imagemin --plugin=pngquant --plugin=svgo

stylesheets=_includes/stylesheet.min.css _includes/stylesheet.email.min.css

all: $(stylesheets)

_includes/stylesheet.min.css: _includes/stylesheet.css
	$(CSSMIN_BIN) $< -o $@

_includes/stylesheet.email.min.css: _includes/stylesheet.email.css
	$(CSSMIN_BIN) $< -o $@

.PHONY: notion

notion: n2y.yml
	@mkdir -p _published
	n2y n2y.yml --verbosity=WARNING

.PHONY: clean cleannotion

clean:
	rm -rf _includes/stylesheet.min.css
	rm -rf _site

cleannotion:
	make clean
	rm -rf _published index.md about.md  # update if new pages are added
