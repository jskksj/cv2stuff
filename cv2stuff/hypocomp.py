from hypothesis.strategies import composite, integers, lists


@composite
def list_and_index(draw, elements=integers()):
    xs = draw(lists(elements, min_size=1))
    i = draw(integers(min_value=0, max_value=len(xs) - 1))
    return (xs, i)
