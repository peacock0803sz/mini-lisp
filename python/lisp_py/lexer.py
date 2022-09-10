from collections.abc import Generator

from lisp_py.tokens import Tokens


def lexer(s: str) -> Generator[Tokens | str, None, None]:
    for w in s.split():
        match w:
            case Tokens.PLUS.value:
                yield Tokens.PLUS
            case Tokens.MINUS.value:
                yield Tokens.MINUS
            case Tokens.TIMES.value:
                yield Tokens.TIMES
            case Tokens.DIV.value:
                yield Tokens.DIV
            case _:
                yield w
