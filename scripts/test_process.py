from process import translate_markdown

import pytest


def assert_translate(input, expected_output):
    actual_output = []
    translate_markdown(input, actual_output.append)
    assert actual_output == expected_output


def test_basic_quote():
    assert_translate([
        '> Hello',
    ], [
        '<blockquote>',
        '<p>Hello</p>',
        '</blockquote>',
    ])


def test_two_paragraph_quote():
    assert_translate([
        '> One',
        '> Two',
    ], [
        '<blockquote>',
        '<p>One</p>',
        '<p>Two</p>',
        '</blockquote>',
    ])


def test_two_paragraph_w_newline_quote():
    assert_translate([
        '> One',
        '>',
        '> Two',
    ], [
        '<blockquote>',
        '<p>One</p>',
        '<p>Two</p>',
        '</blockquote>',
    ])


def test_hidden_citation():
    assert_translate([
        '> One',
        '> - Hello',
    ], [
        '<blockquote>',
        '<p>One</p>',
        '<cite>— Hello</cite>',
        '</blockquote>',
    ])


def test_poetry_empty_citation():
    assert_translate([
        '> One',
        '> ~',
    ], [
        '<blockquote class="poetry">',
        '<p>One</p>',
        '</blockquote>',
    ])


def test_prose_empty_citation():
    assert_translate([
        '> One',
        '> =',
    ], [
        '<blockquote class="prose">',
        '<p>One</p>',
        '</blockquote>',
    ])


def test_indents():
    assert_translate([
        '> One',
        '>   Two',
    ], [
        '<blockquote>',
        '<p>One</p>',
        '<p class="indent">Two</p>',
        '</blockquote>',
    ])


def test_poetry_blank_lines():
    assert_translate([
        '> One',
        '> Two',
        '>',
        '> Three',
        '> ~',
    ], [
        '<blockquote class="poetry">',
        '<p>One</p>',
        '<p>Two</p>',
        '<br>',
        '<p>Three</p>',
        '</blockquote>',
    ])


def test_italics_in_quote():
    assert_translate([
        '> One *then* two',
    ], [
        '<blockquote>',
        '<p>One <em>then</em> two</p>',
        '</blockquote>',
    ])


def test_italics_in_prose_quote():
    assert_translate([
        '> One *then* two',
        '> =',
    ], [
        '<blockquote class="prose">',
        '<p>One <em>then</em> two</p>',
        '</blockquote>',
    ])


@pytest.mark.xfail
def test_italics_in_quote_w_asterisk():
    assert_translate([
        r'> One *then\* two*',
    ], [
        '<blockquote>',
        '<p>One <em>then* two</em></p>',
        '</blockquote>',
    ])
