from views.utils import ChallengeManager


def test_run_type_check_with_pyright():
    code = """\
a: int = 1
b: str = "2"  # expect-type-error
c: int = "3"  # expect-type-error
d: str = 4
e: list[str] = [
    i  # expect-type-error
    for i in range(10)
]
"""
    result = ChallengeManager._type_check_with_pyright(code)
    assert result.passed is False
    errors = [line for line in result.stdout.splitlines() if line]
    assert len(errors) == 3
    assert errors[0].startswith("4: error: Incompatible types in assignment")
    assert errors[1].startswith("2: error: Expected type error")
