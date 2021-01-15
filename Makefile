SHELL := /bin/bash -o pipefail -e
.SUFFIXES:

CSSMIN_BIN := node_modules/clean-css-cli/bin/cleancss
IMGMIN_BIN := node_modules/imagemin-cli/cli.js imagemin --plugin=pngquant --plugin=svgo

essays=$(patsubst essays/%.md,_essays/%.md,$(wildcard essays/*.md))
meditations=$(patsubst meditations/%.md,_meditations/%.md,$(wildcard meditations/*.md))
poems=$(patsubst poems/%.md,_poems/%.md,$(wildcard poems/*.md))
notes=$(patsubst notes/%.md,_notes/%.md,$(wildcard notes/*.md))
stylesheets=_includes/stylesheet.min.css _includes/stylesheet.email.min.css

all: $(stylesheets) $(essays) $(meditations) $(poems) $(notes)

_includes/stylesheet.min.css: _includes/stylesheet.css
	$(CSSMIN_BIN) $< -o $@

_includes/stylesheet.email.min.css: _includes/stylesheet.email.css
	$(CSSMIN_BIN) $< -o $@

_essays/%.md: essays/%.md ./scripts/process.py ./scripts/typography.sed
	 cat $< | sed -E -f ./scripts/typography.sed | ./scripts/process.py > $@

_meditations/%.md: meditations/%.md ./scripts/process.py ./scripts/typography.sed
	 cat $< | sed -E -f ./scripts/typography.sed | ./scripts/process.py > $@

_poems/%.md: poems/%.md ./scripts/process.py ./scripts/typography.sed
	 cat $< | sed -E -f ./scripts/typography.sed | ./scripts/process.py > $@

_notes/%.md: notes/%.md ./scripts/process.py ./scripts/typography.sed
	 cat $< | sed -E -f ./scripts/typography.sed | ./scripts/process.py > $@

.PHONY: clean

clean:
	rm -rf _includes/stylesheet.min.css
	rm -rf _site
	rm _essays/* _meditations/* _poems/* _notes/*
