SHELL := /bin/bash -o pipefail -e
.SUFFIXES:

CSSMIN_BIN := node_modules/clean-css-cli/bin/cleancss
IMGMIN_BIN := node_modules/imagemin-cli/cli.js imagemin --plugin=pngquant --plugin=svgo

documents=$(patsubst documents/%.md,_documents/%.md,$(wildcard documents/*.md))

all: _includes/stylesheet.min.css $(documents)

_includes/stylesheet.min.css: _includes/stylesheet.css
	$(CSSMIN_BIN) $< -o $@

_documents/%.md: documents/%.md ./scripts/process.py ./scripts/typography.sed
	./scripts/process.py $< | sed -E -f ./scripts/typography.sed > $@

.PHONY: clean

clean:
	rm -rf _includes/stylesheet.min.css
	rm -rf _site
	rm _documents/*
