from core.rule_engine import RuleEngine


def test_regex_rule_application():
    rules = {
        "test_rule": {
            "description": "swap i",
            "pattern": "i(.)",
            "replace": "\\1i"
        }
    }

    engine = RuleEngine(rules)
    result = engine.apply("iA", ["test_rule"])

    assert result == "Ai"
