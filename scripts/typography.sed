# em-dashes and en-dashes, except for YAML delimiters and horizontal rules
/^---$/!s/---/—/g
/^---$/!s/--/–/g

# vertically center ellipses on their own line; nice for long quotes
s/<p>\.\.\.<\/p>/<p>⋯<\/p>/g
