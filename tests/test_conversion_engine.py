from pathlib import Path
from core.profile_loader import load_profile_with_rules
from core.engine import ConversionEngine


def test_basic_conversion_pipeline():
    source, rules = load_profile_with_rules(
        Path("profiles/gujarati/bhasha_bharti.json")
    )
    target, _ = load_profile_with_rules(
        Path("profiles/gujarati/terafont_varun.json")
    )

    engine = ConversionEngine(source, target, rules)

    assert engine.convert("AB") == "કખ"
