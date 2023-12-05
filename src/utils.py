def lprint(l):
    """Pretty print a a list"""
    for row in l:
        print(row)


def lmap(f, *seqs):
    """Shorthand for `list(map())`"""
    return list(map(f, *seqs))
