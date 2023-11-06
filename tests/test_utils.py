from views.utils import ChallengeManager


def test_run_type_check_with_pyright():
    code = """\
a: int = 1
b: str = "2"  # expect-type-error
c: int = "3"  # expect-type-error
d: str = 4
e: list[str] = [  # expect-type-error
    i for i in range(10)
]
"""
    result = ChallengeManager._type_check_with_pyright(code)
    assert result.passed is False
    assert result.stdout == (
        '4:error: Expression of type "Literal[4]" cannot be assigned to declared type "str"\n'
        "2: error: Expected type error but instead passed\n\n"
        "Found 2 errors"
    )
