import re
from pandoc.types import Link, Str, RawBlock, Format, Para, Text, Span, Attr
import pandoc
import logging

from n2y.mentions import PageMention
from n2y.blocks import ParagraphBlock, QuoteBlock
from n2y.errors import UseNextClass


logger = logging.getLogger(__name__)


class DialogueBlock(ParagraphBlock):
    def __init__(self, client, notion_data, page, get_children=True):
        super().__init__(client, notion_data, page, get_children)
        if not self._is_dialogue():
            raise UseNextClass()

    def _is_dialogue(self):
        first_str = self.rich_text.to_plain_text().split(" ")[0]
        logger.warning(first_str)
        return bool(re.match(r"^[^ ]+:: ", first_str))

    def to_pandoc(self):
        content = self.rich_text.to_pandoc()
        first_text = content[0]
        logger.warning(first_text[0])
        assert type(first_text) == Text
        content[0] = Span(Attr("", ["sc"], []) , [first_text])
        if self.has_children:
            # Notion allows you to create child blocks for a paragraph; these
            # child blocks appear indented relative to the paragraph. There's
            # no way to represent this indentation in pandoc's AST, so we just
            # append the child blocks afterwards.
            result = [Para(content)]
            children = self.children_to_pandoc()
            result.extend(children)
        else:
            result = Para(content)
        return result


class LinkPageMention(PageMention):
    def to_pandoc(self):
        page = self.client.get_page(self.notion_page_id)
        url = "./" + page.filename  # assume the filename is the url
        return [Link(
            ('', [], []),
            [Str(self.plain_text)],
            (url, '')
        )]


class CustomQuoteBlock(QuoteBlock):
    def to_pandoc(self):
        rich_text_ast = self.rich_text.to_pandoc()
        rich_text_html = pandoc.write(rich_text_ast, format='html')
        # TODO: handle citations
        return RawBlock(Format('html'), "\n".join([
            '<blockquote><p>',
            rich_text_html.rstrip(),
            '</p></blockquote>',
            '',
        ]))


notion_classes = {
    "mentions": {
        "page": LinkPageMention,
    },
    "blocks": {
        "quote": CustomQuoteBlock,
        "paragraph": DialogueBlock,
    },
}
