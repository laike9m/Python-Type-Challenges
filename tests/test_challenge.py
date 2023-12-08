from views.challenge import ChallengeManager


def test_run_not_modified_user_code(random_q_challenge):
    ret = ChallengeManager().run_challenge(random_q_challenge.key, random_q_challenge.user_code)
    assert ret.passed is False
    assert "make some changes" in ret.message


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
    result = ChallengeManager._type_check_with_pyright(user_code="", test_code=code)
    assert result.passed is False
    assert result.message == (
        '4:error: Expression of type "Literal[4]" cannot be assigned to declared type "str"\n'
        "2: error: Expected type error but instead passed\n\n"
        "Found 2 errors"
    )
