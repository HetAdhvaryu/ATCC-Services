import json
from pathlib import Path
from core.exceptions import RuleNotFoundError


def load_rules(script_dir: Path) -> dict:
    rules_file = script_dir / "rules.json"
    if not rules_file.exists():
        return {}

    with open(rules_file, "r", encoding="utf-8") as f:
        rules = json.load(f)

    return rules


def validate_rule_ids(rule_ids: list, available_rules: dict):
    for rule_id in rule_ids:
        if rule_id not in available_rules:
            raise RuleNotFoundError(f"Rule not found: {rule_id}")
