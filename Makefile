SHELL := /bin/bash -o pipefail -e
.SUFFIXES:

CSSMIN_BIN := node_modules/clean-css-cli/bin/cleancss
IMGMIN_BIN := node_modules/imagemin-cli/cli.js imagemin --plugin=pngquant --plugin=svgo

all: _includes/stylesheet.min.css _includes/squares.min.svg

_includes/squares.min.svg: _includes/squares.svg
	$(IMGMIN_BIN) $< > $@

_includes/stylesheet.min.css: _includes/stylesheet.css
	$(CSSMIN_BIN) $< -o $@

.PHONY: clean

clean:
	rm -rf _includes/stylesheet.min.css _includes/squares.min.svg
	rm -rf _site
