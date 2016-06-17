from hypothesis.strategies import characters, text
from hypothesis import given
from unicodedata import category


names = text(
    characters(max_codepoint=1000, blacklist_categories=('Cc', 'Cs')),
    min_size=1).map(lambda s: s.strip()).filter(lambda s: len(s) > 0)

@given(names)
def test_names_match_our_requirements(name):
    assert len(name) > 0
    assert name == name.strip()
    for c in name:
        assert 1 <= ord(c) <= 1000
        assert category(c) not in ('Cc', 'Cs')

    print(name)


if __name__ == '__main__':
    test_names_match_our_requirements()
