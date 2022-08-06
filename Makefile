SHELL := /bin/bash -o pipefail -e
.SUFFIXES:

CSSMIN_BIN := node_modules/clean-css-cli/bin/cleancss
IMGMIN_BIN := node_modules/imagemin-cli/cli.js imagemin --plugin=pngquant --plugin=svgo

essays=$(patsubst essays/%.md,_essays/%.md,$(wildcard essays/*.md))
dialogues=$(patsubst dialogues/%.md,_dialogues/%.md,$(wildcard dialogues/*.md))
meditations=$(patsubst meditations/%.md,_meditations/%.md,$(wildcard meditations/*.md))
poems=$(patsubst poems/%.md,_poems/%.md,$(wildcard poems/*.md))
notes=$(patsubst notes/%.md,_notes/%.md,$(wildcard notes/*.md))
stylesheets=_includes/stylesheet.min.css _includes/stylesheet.email.min.css

all: $(stylesheets) $(essays) $(meditations) $(poems) $(notes) $(dialogues)

_includes/stylesheet.min.css: _includes/stylesheet.css
	$(CSSMIN_BIN) $< -o $@

_includes/stylesheet.email.min.css: _includes/stylesheet.email.css
	$(CSSMIN_BIN) $< -o $@

_essays/%.md: essays/%.md ./scripts/process.py
	 cat $< | ./scripts/process.py > $@

_dialogues/%.md: dialogues/%.md ./scripts/process.py
	 cat $< | ./scripts/process.py > $@

_meditations/%.md: meditations/%.md ./scripts/process.py
	 cat $< | ./scripts/process.py > $@

_poems/%.md: poems/%.md ./scripts/process.py
	 cat $< | ./scripts/process.py > $@

_notes/%.md: notes/%.md ./scripts/process.py
	 cat $< | ./scripts/process.py > $@

ENTRIES_DB=94b4804111924eab834fd6f56a7964b9
.PHONY: notion
notion:
	@mkdir -p essays dialogues notes poems meditations img-orig
	. .env && n2y $(ENTRIES_DB) \
		--format=markdown \
		--output=. \
		--media-root=img-orig \
		--filename-property=slug \
		--plugin=n2y.plugins.removecallouts \
		--plugin=n2y.plugins.rawcodeblocks \
		--plugin=plugins \
		--database-config='{"$(ENTRIES_DB)":{"filter":{"and":[{"property":"type","select":{"equals":"Page"}},{"property":"status","select":{"equals":"Published"}}]}}}' \
		--media-url=./img \
		--verbosity=WARNING
	. .env && n2y $(ENTRIES_DB) \
		--format=markdown \
		--output=essays \
		--media-root=img-orig \
		--filename-property=slug \
		--plugin=n2y.plugins.removecallouts \
		--plugin=n2y.plugins.rawcodeblocks \
		--plugin=plugins \
		--database-config='{"$(ENTRIES_DB)":{"filter":{"and":[{"property":"type","select":{"equals":"Essay"}},{"property":"status","select":{"equals":"Published"}}]}}}' \
		--media-url=./img \
		--verbosity=WARNING
	. .env && n2y $(ENTRIES_DB) \
		--format=markdown \
		--output=dialogues \
		--media-root=img-orig \
		--filename-property=slug \
		--plugin=n2y.plugins.removecallouts \
		--plugin=n2y.plugins.rawcodeblocks \
		--plugin=plugins \
		--database-config='{"$(ENTRIES_DB)":{"filter":{"and":[{"property":"type","select":{"equals":"Dialogue"}},{"property":"status","select":{"equals":"Published"}}]}}}' \
		--media-url=./img \
		--verbosity=WARNING
	. .env && n2y $(ENTRIES_DB) \
		--format=markdown \
		--output=meditations \
		--media-root=img-orig \
		--filename-property=slug \
		--plugin=n2y.plugins.removecallouts \
		--plugin=n2y.plugins.rawcodeblocks \
		--plugin=plugins \
		--database-config='{"$(ENTRIES_DB)":{"filter":{"and":[{"property":"type","select":{"equals":"Meditation"}},{"property":"status","select":{"equals":"Published"}}]}}}' \
		--media-url=./img \
		--verbosity=WARNING
	. .env && n2y $(ENTRIES_DB) \
		--format=markdown \
		--output=poems \
		--media-root=img-orig \
		--filename-property=slug \
		--plugin=n2y.plugins.removecallouts \
		--plugin=n2y.plugins.rawcodeblocks \
		--plugin=plugins \
		--database-config='{"$(ENTRIES_DB)":{"filter":{"and":[{"property":"type","select":{"equals":"Poem"}},{"property":"status","select":{"equals":"Published"}}]}}}' \
		--media-url=./img \
		--verbosity=WARNING
	. .env && n2y $(ENTRIES_DB) \
		--format=markdown \
		--output=notes \
		--media-root=img-orig \
		--filename-property=slug \
		--plugin=n2y.plugins.removecallouts \
		--plugin=n2y.plugins.rawcodeblocks \
		--plugin=plugins \
		--database-config='{"$(ENTRIES_DB)":{"filter":{"and":[{"property":"type","select":{"equals":"Notes"}},{"property":"status","select":{"equals":"Published"}}]}}}' \
		--media-url=./img \
		--verbosity=WARNING


.PHONY: clean cleannotion

clean:
	rm -rf _includes/stylesheet.min.css
	rm -rf _site
	rm -f _essays/* _meditations/* _poems/* _notes/* _dialogues/*

cleannotion:
	make clean
	rm -rf index.md about.md  # update if new pages are added
	rm -f essays/* meditations/* poems/* notes/* dialogues/*
