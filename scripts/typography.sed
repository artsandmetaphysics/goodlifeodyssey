# skip over script tags
/<script>/,/<\/script>/ {
    p
    d
}

/<p.*>/,/<\/p>/ {
    p
    d
}

# em-dashes and en-dashes, except for YAML delimiters and horizontal rules
/^---$/ !{
    s/---/—/g
    s/--/–/g
}

# vertically center ellipses on their own line; nice for long quotes
s/^> \.\.\.$/> ⋯/g

# ellipses
s/\.\.\./…/g

# fancy quotes
s/(^|[-/(\[{" ])'/\1‘/g
s/'/’/g
s/(^|[/(\[{‘ ])"/\1“/g
s/(^|[^=])"([^>]|$)/\1”\2/g

# make fancy quotes within html tags back
# this doesn't work if there are 3 attributes
s/(<[^>]*)(“|”)/\1"/g
s/(<[^>]*)(‘|’)/\1'/g
