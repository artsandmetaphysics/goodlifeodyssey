from process import translate_markdown


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
        '> -- Hello',
    ], [
        '<blockquote title="Hello">',
        '<p>One</p>',
        '</blockquote>',
    ])


def test_visible_citation():
    assert_translate([
        '> One',
        '> --- Hello',
    ], [
        '<blockquote>',
        '<p>One</p>',
        '<cite>Hello</cite>',
        '</blockquote>',
    ])


def test_poetry_empty_citation():
    assert_translate([
        '> One',
        '> ==',
    ], [
        '<blockquote class="poetry">',
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
