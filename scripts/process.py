#!/usr/bin/env python3

import sys
import html


def translate_markdown(lines, printer):
    in_quote = False
    quote = []
    for line in lines:
        line = line.rstrip()
        quote_line = line.startswith('> ') or line == '>'
        if not in_quote and quote_line:
            in_quote = True
        elif in_quote and not quote_line:
            in_quote = False
            translate_quote(quote, printer)
            quote = []

        if in_quote:
            quote.append(line)
        else:
            printer(line)

    if in_quote:
        translate_quote(quote, printer)


def translate_quote(lines, printer):
    assert len(lines) > 0
    pruned_lines = [strip_quoting(line) for line in lines]
    is_poetry = False
    if pruned_lines[-1][:3] in ['-- ', '== '] or pruned_lines[-1] == '==':
        last_line = pruned_lines.pop()
        citation = html.escape(last_line[3:].strip())
        if last_line[:3] == '-- ':
            printer('<blockquote title="{}">'.format(citation))
        elif last_line[:3] == '== ':
            printer('<blockquote title="{}" class="poetry">'.format(citation))
            is_poetry = False
        elif last_line == '==':
            printer('<blockquote class="poetry">')
            is_poetry = True
    else:
        printer('<blockquote>')
    for line in pruned_lines:
        if line.startswith('--- '):
            printer('<cite>' + line[len('--- '):] + '</cite>')
        elif line.startswith('  '):
            printer('<p class="indent">' + line[2:] + '</p>')
        elif line != '':
            printer('<p>' + line + '</p>')
        elif line == '' and is_poetry:
            printer('<br>')
    printer('</blockquote>')


def strip_quoting(line):
    if line.startswith('> '):
        return line[2:]
    elif line == '>':
        return line[1:]
    else:
        raise ValueError()


if __name__ == "__main__":
    input_filename = sys.argv[1]
    with open(input_filename, 'r') as f:
        translate_markdown(f, print)
