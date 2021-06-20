import itertools


def align_iterables(*inputs, missing=None, key=None):
    end = object()
    iterators = [itertools.chain(i, [end]) for i in inputs]
    values = [next(i) for i in iterators]

    def index(value):
        if key is None:
            return value
        if not hasattr(value, key):
            return value
        return getattr(value, key)

    while not all(v is end for v in values):
        smallest = min(index(v) for v in values if v is not end)
        yield tuple(v if index(v) == smallest else missing for v in values)
        values = [next(i) if index(v) == smallest else v for i, v in zip(iterators, values)]
