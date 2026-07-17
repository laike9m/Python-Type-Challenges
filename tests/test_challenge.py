from pathlib import Path

from views.challenge import ChallengeKey, ChallengeManager


class TestLoadChallenges:
    def test_load_empty_dir(self, tmpdir):
        assert ChallengeManager(Path(tmpdir)).challenge_count == 0

    def test_defaults(self):
        assert ChallengeManager().challenge_count > 0

    def test_load_tests_assets(self, mgr: ChallengeManager):
        assert mgr.challenge_count > 0

    def test_partition_test_code(self, mgr: ChallengeManager):
        pyright_config_test = mgr.get_challenge(
            ChallengeKey.from_str("basic-foo-pyright-config")
        ).test_code

        _, pyright_basic_config = mgr._partition_test_code(pyright_config_test)
        assert pyright_basic_config.endswith("pyright: reportGeneralTypeIssues=error\n")


class TestChallengeWithHints:
    def test_misc(self, mgr: ChallengeManager):
        c_foo = mgr.get_challenge(ChallengeKey.from_str("basic-foo"))
        assert c_foo.hints is None

        # Get the challenge with hints
        c_foo_hints = mgr.get_challenge(ChallengeKey.from_str("basic-foo-hints"))
        assert c_foo_hints.hints
        assert isinstance(c_foo_hints.hints, str)
