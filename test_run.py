from pathlib import Path

from core.profile_loader import load_profile_with_rules
from core.engine import ConversionEngine


def main():
    source_profile, rules = load_profile_with_rules(
        Path("profiles/gujarati/bhasha_bharti.json")
    )

    target_profile, _ = load_profile_with_rules(
        Path("profiles/gujarati/terafont_varun.json")
    )

    engine = ConversionEngine(
        source_profile=source_profile,
        target_profile=target_profile,
        rules=rules,
        enable_debug=True
    )

    input_text = "ABAB"
    output_text = engine.convert(input_text)

    print("INPUT :", input_text)
    print("OUTPUT:", output_text)


if __name__ == "__main__":
    main()
