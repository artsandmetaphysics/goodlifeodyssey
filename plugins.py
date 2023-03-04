import re
from pandoc.types import Link, Str, Para, Span, Space, LineBlock, LineBreak
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
        return bool(re.match(r"^[^ ]+::", first_str))

    def to_pandoc(self):
        content = self.rich_text.to_pandoc()
        content = [Str('&nbsp;') if isinstance(n, Space) else n for n in content]
        first_text = content[0]
        content[0] = Span(("", ["sc"], []) , [Str(first_text[0][:-1])])
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
    @classmethod
    def transform(klass, original_ast):
        lines = [[]]
        for inline in original_ast:
            if isinstance(inline, LineBreak):
                lines.append([])
            else:
                lines[-1].append(inline)
        for line in lines:
            num_spaces = 0
            for inline in line:
                if isinstance(inline, Space):
                    num_spaces += 1
                else:
                    break
            for i in range(num_spaces):
                line.pop(0)
            if isinstance(line[0], Str):
                line[0] = Str(" "*num_spaces + line[0][0])

        logger.warning(repr(lines))
        return lines


    def to_pandoc(self):
        rich_text_ast = self.rich_text.to_pandoc()
        lines = self.transform(rich_text_ast)
        return LineBlock(lines)


notion_classes = {
    "mentions": {
        "page": LinkPageMention,
    },
    "blocks": {
        "quote": CustomQuoteBlock,
        "paragraph": DialogueBlock,
    },
}
