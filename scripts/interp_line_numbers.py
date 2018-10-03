#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    first_original_lineno_page = int(sys.argv[1])
    last_original_lineno_page = int(sys.argv[2])
    first_translation_lineno_page = int(sys.argv[3])
    last_translation_lineno_page = int(sys.argv[4])
    first_translation_lineno_quote = int(sys.argv[5])
    last_translation_lineno_quote = int(sys.argv[6])
    
    dx = last_translation_lineno_page - first_original_lineno_page
    dy = last_original_lineno_page - first_original_lineno_page
    assert dx > 0
    assert dy > 0
    slope = float(dy)/float(dx)
    intercept = first_original_lineno_page - slope*first_translation_lineno_page

    first_original_lineno_quote = int(round(slope*first_translation_lineno_quote + intercept))
    last_original_lineno_quote = int(round(slope*last_translation_lineno_quote + intercept))

    print("{}--{}".format(first_original_lineno_quote, last_original_lineno_quote), end='')
