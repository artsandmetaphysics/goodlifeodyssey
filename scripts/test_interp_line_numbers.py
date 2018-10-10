from interp_line_numbers import interp_line_numbers


def test_exact_match():
    assert interp_line_numbers(1, 10, 1, 10, 2, 6) == (2, 6)
    assert interp_line_numbers(1, 10, 1, 10, 1, 10) == (1, 10)


def test_full_range():
    assert interp_line_numbers(1, 10, 5, 10, 5, 10) == (1, 10)
    assert interp_line_numbers(1, 10, 103, 105, 103, 105) == (1, 10)
