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

ENTRIES_DB=94b4804111924eab834fd6f56a7964b9
.PHONY: notion notionpages notionessays notiondialogues notionmeditations notionpoems notionnotes

notion: notionpages notionessays notiondialogues notionmeditations notionpoems notionnotes

notionpages:
	@mkdir -p essays dialogues notes poems meditations img-orig
	n2y $(ENTRIES_DB) \
		--format=html \
		--output=. \
		--media-root=img-orig \
		--filename-property=slug \
		--plugin=n2y.plugins.removecallouts \
		--plugin=n2y.plugins.rawcodeblocks \
		--plugin=plugins \
		--database-config='{"$(ENTRIES_DB)":{"filter":{"and":[{"property":"type","select":{"equals":"Page"}},{"property":"status","select":{"equals":"Published"}}]}}}' \
		--media-url=./img \
		--verbosity=WARNING

notionessays:
	n2y $(ENTRIES_DB) \
		--format=html \
		--output=_published \
		--media-root=img-orig \
		--filename-property=slug \
		--plugin=n2y.plugins.removecallouts \
		--plugin=n2y.plugins.rawcodeblocks \
		--plugin=plugins \
		--database-config='{"$(ENTRIES_DB)":{"filter":{"and":[{"property":"type","select":{"equals":"Essay"}},{"property":"status","select":{"equals":"Published"}}]}}}' \
		--media-url=./img \
		--verbosity=WARNING

notiondialogues:
	n2y $(ENTRIES_DB) \
		--format=html \
		--output=_published \
		--media-root=img-orig \
		--filename-property=slug \
		--plugin=n2y.plugins.removecallouts \
		--plugin=n2y.plugins.rawcodeblocks \
		--plugin=plugins \
		--database-config='{"$(ENTRIES_DB)":{"filter":{"and":[{"property":"type","select":{"equals":"Dialogue"}},{"property":"status","select":{"equals":"Published"}}]}}}' \
		--media-url=./img \
		--verbosity=WARNING

notionmeditations:
	n2y $(ENTRIES_DB) \
		--format=html \
		--output=_published \
		--media-root=img-orig \
		--filename-property=slug \
		--plugin=n2y.plugins.removecallouts \
		--plugin=n2y.plugins.rawcodeblocks \
		--plugin=plugins \
		--database-config='{"$(ENTRIES_DB)":{"filter":{"and":[{"property":"type","select":{"equals":"Meditation"}},{"property":"status","select":{"equals":"Published"}}]}}}' \
		--media-url=./img \
		--verbosity=WARNING

notionpoems:
	n2y $(ENTRIES_DB) \
		--format=html \
		--output=_published \
		--media-root=img-orig \
		--filename-property=slug \
		--plugin=n2y.plugins.removecallouts \
		--plugin=n2y.plugins.rawcodeblocks \
		--plugin=plugins \
		--database-config='{"$(ENTRIES_DB)":{"filter":{"and":[{"property":"type","select":{"equals":"Poem"}},{"property":"status","select":{"equals":"Published"}}]}}}' \
		--media-url=./img \
		--verbosity=WARNING

notionnotes:
	n2y $(ENTRIES_DB) \
		--format=html \
		--output=_published \
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

cleannotion:
	make clean
	rm -rf index.md about.md  # update if new pages are added
	rm -f _published
