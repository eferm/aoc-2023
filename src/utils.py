def lprint(lst):
    """Pretty print a list."""
    for row in lst:
        print(row)


def lmap(f, *seqs):
    """Shorthand for `list(map())`"""
    return list(map(f, *seqs))
