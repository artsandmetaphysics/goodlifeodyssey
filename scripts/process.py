#!/usr/bin/env python3

import sys
import re
import html


def translate_markdown(lines, printer):
    in_quote = False
    in_poem = False
    quote = []
    for line in lines:
        line = line.rstrip()
        quote_line = line.startswith('> ') or line == '>'
        dialogue_line = re.match(r'^\S+:: ', line)
        if not in_quote and quote_line:
            in_quote = True
        elif in_quote and not quote_line:
            in_quote = False
            translate_quote(quote, printer)
            quote = []

        if line == '~~~':
            in_poem = not in_poem
            continue

        if in_quote:
            quote.append(line)
        elif in_poem:
            printer(line + '<br>')
        elif dialogue_line:
            name, remainder, *other = line.split('::')
            assert len(other) == 0
            printer(f'<span class="sc">{name}:</span>{remainder}')
        else:
            printer(line)

    if in_quote:
        translate_quote(quote, printer)


def translate_quote(lines, printer):
    assert len(lines) > 0
    pruned_lines = [strip_quoting(line) for line in lines]
    last_line = pruned_lines[-1]
    is_poetry = last_line.startswith('~')
    is_prose = last_line.startswith('=')

    if any(last_line.startswith(q) for q in ['- (', '= (', '~ (']):
        pruned_lines.pop()
        pruned_lines[-1] += ' <cite>' + process_line(last_line[2:]) + '</cite>'
        citation = None
    elif any(last_line.startswith(q) for q in ['- ', '= ', '~ ']):
        citation = process_line(last_line[2:])
        pruned_lines.pop()
    elif any(last_line == q for q in ['-', '=', '~']):
        pruned_lines.pop()
        citation = None
    else:
        citation = None

    if is_poetry:
        printer('<blockquote class="poetry">')
    elif is_prose:
        printer('<blockquote class="prose">')
    else:
        printer('<blockquote>')

    for line in pruned_lines:
        if line.startswith('  '):
            printer('<p class="indent">' + process_line(line[2:]) + '</p>')
        elif line != '':
            printer('<p>' + process_line(line) + '</p>')
        elif line == '' and is_poetry:
            printer('<br>')

    if citation:
        printer('<cite>— ' + citation + '</cite>')
    printer('</blockquote>')


def strip_quoting(line):
    if line.startswith('> '):
        return line[2:]
    elif line == '>':
        return line[1:]
    else:
        raise ValueError()


def process_line(line):
    line = re.sub(r'\*\*([^*]*)\*\*', r'<strong>\1</strong>', line)
    line = re.sub(r'\*([^*]*)\*', r'<em>\1</em>', line)
    line = re.sub(r'_([^_]*)_', r'<em>\1</em>', line)
    return line


if __name__ == "__main__":
    translate_markdown(sys.stdin, print)
