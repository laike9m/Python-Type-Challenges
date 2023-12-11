from pathlib import Path

import pytest

from views.challenge import ChallengeKey, ChallengeManager


class TestLoadChallenges:
    def test_load_empty_dir(self, tmpdir):
        assert ChallengeManager(Path(tmpdir)).get_challenge_cnt() == 0

    def test_defaults(self):
        assert ChallengeManager().get_challenge_cnt() > 0

    def test_load_tests_assets(self, assets_dir):
        mgr = ChallengeManager(assets_dir / "challenges")
        assert mgr.get_challenge_cnt() > 0


class TestChallengeWithHints:
    @pytest.fixture()
    def challenge_mgr(self, assets_dir):
        return ChallengeManager(assets_dir / "challenges")

    def test_misc(self, challenge_mgr):
        c_foo = challenge_mgr.get_challenge(ChallengeKey.from_str("basic-foo"))
        assert c_foo.hints is None

        # Get the challenge with hints
        c_foo_hints = challenge_mgr.get_challenge(
            ChallengeKey.from_str("basic-foo-hints")
        )
        assert c_foo_hints.hints
        assert isinstance(c_foo_hints.hints, str)
