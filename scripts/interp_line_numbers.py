#!/usr/bin/env python3

import sys


def interp_line_numbers(y1, y2, x1, x2, qx1, qx2):
    dx = x2 - x1
    dy = y2 - y1
    assert dx > 0
    assert dy > 0
    assert qx1 >= x1
    assert qx2 <= x2
    assert qx2 >= qx1
    slope = float(dy)/float(dx)
    intercept = y1 - slope*x1
    qy1 = int(round(slope*qx1 + intercept))
    qy2 = int(round(slope*qx2 + intercept))
    return qy1, qy2


if __name__ == "__main__":
    if len(sys.argv) != 7:
        print('USAGE: interp_line_numbers ORIG1 ORIG2 TRANS1 TRANS2 QUOTE1 QUOTE2')
        sys.exit(1)
    first_original_lineno_page = int(sys.argv[1])
    last_original_lineno_page = int(sys.argv[2])
    first_translation_lineno_page = int(sys.argv[3])
    last_translation_lineno_page = int(sys.argv[4])
    first_translation_lineno_quote = int(sys.argv[5])
    last_translation_lineno_quote = int(sys.argv[6])

    first_original_lineno_quote, last_original_lineno_quote = interp_line_numbers(
        first_original_lineno_page,
        last_original_lineno_page,
        first_translation_lineno_page,
        last_translation_lineno_page,
        first_translation_lineno_quote,
        last_translation_lineno_quote)

    print("{}--{}".format(first_original_lineno_quote, last_original_lineno_quote), end='')
