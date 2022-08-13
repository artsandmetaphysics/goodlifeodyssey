from pandoc.types import Link, Str, RawBlock, Format
import pandoc

from n2y.mentions import PageMention
from n2y.blocks import QuoteBlock


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
    },
}
