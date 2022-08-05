from pandoc.types import Link, Str

from n2y.mentions import PageMention


class LinkPageMention(PageMention):
    def to_pandoc(self):
        page = self.client.get_page(self.notion_page_id)
        url = "./" + page.filename  # assume the filename is the url
        return [Link(
            ('', [], []),
            [Str(self.plain_text)],
            (url, '')
        )]


notion_classes = {
    "mentions": {
        "page": LinkPageMention,
    },
}
