def lprint(seq):
    """Pretty print an iterable."""
    for val in seq:
        print(val)


def mprint(seqseq):
    """Pretty print an iterable of iterables."""
    for seq in seqseq:
        for val in seq:
            print(val)


def lmap(f, *seqs):
    """Shorthand for `list(map())`"""
    return list(map(f, *seqs))
