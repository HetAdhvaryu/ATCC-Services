from pathlib import Path
from core.profile_loader import load_profile_with_rules


def test_load_valid_profile():
    profile, rules = load_profile_with_rules(
        Path("profiles/gujarati/bhasha_bharti.json")
    )

    assert profile["font"]["name"] == "Bhasha Bharti"
    assert isinstance(rules, dict)
