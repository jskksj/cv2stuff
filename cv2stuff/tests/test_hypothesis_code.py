from hypothesis import given
from hypothesis.strategies import text
from cv2stuff.hypothesis_code import encode, decode


@given(text())
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s
