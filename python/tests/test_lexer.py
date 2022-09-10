import pytest

from lisp_py.lexer import lexer
from lisp_py.tokens import Tokens

testdata = [
    ("1 + 3", ("1", Tokens.PLUS, "3")),
    ("9 - 5", ("9", Tokens.MINUS, "5")),
    ("4 * 8", ("4", Tokens.TIMES, "8")),
    ("2 / 3", ("2", Tokens.DIV, "3")),
    ("10 undef 42", ("10", "undef", "42")),
]


@pytest.mark.parametrize(("given", "expected"), testdata)
def test_lexer(given, expected):
    tokens = tuple(lexer(given))
    assert expected == tokens
