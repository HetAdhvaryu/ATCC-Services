import json
from pathlib import Path

from core.validator import (
    validate_profile_structure,
    validate_font_section,
    validate_script_section,
    validate_encoding,
    validate_mapping,
    validate_rules
)
from core.rule_loader import load_rules, validate_rule_ids
from core.exceptions import ProfileNotFoundError


def load_profile(profile_path: Path) -> dict:
    if not profile_path.exists():
        raise ProfileNotFoundError(f"Profile not found: {profile_path}")

    with open(profile_path, "r", encoding="utf-8") as f:
        profile = json.load(f)

    # Structural validation
    validate_profile_structure(profile)
    validate_font_section(profile["font"])
    validate_script_section(profile["script"])
    validate_encoding(profile["encoding"])
    validate_rules(profile)
    validate_mapping(profile)

    return profile


def load_profile_with_rules(profile_path: Path) -> tuple[dict, dict]:
    profile = load_profile(profile_path)

    script_dir = profile_path.parent
    rules = load_rules(script_dir)

    validate_rule_ids(profile["rules"], rules)

    return profile, rules
