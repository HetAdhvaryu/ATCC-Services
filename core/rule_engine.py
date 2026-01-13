"""
Rule Execution Engine

This module applies script-specific transformation rules
to legacy font text in a deterministic and ordered manner.

Rules are defined in JSON and are data-driven.
"""

from __future__ import annotations

import re
from typing import Dict, List, Any

from core.exceptions import ProfileValidationError


class RuleEngine:
    """
    Executes ordered transformation rules on input text.

    This engine is:
    - Deterministic
    - Script-aware
    - Data-driven
    """

    def __init__(self, rules: Dict[str, dict], enable_debug: bool = False):
        """
        :param rules: Rule definitions loaded from rules.json
        :param enable_debug: Enables verbose rule tracing
        """
        self.rules = self._prepare_rules(rules)
        self.enable_debug = enable_debug

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def apply(self, text: str, rule_ids: List[str]) -> str:
        """
        Apply rules in strict order.

        :param text: Input text
        :param rule_ids: Ordered list of rule IDs
        :return: Transformed text
        """
        if not rule_ids:
            return text

        for rule_id in rule_ids:
            rule = self.rules.get(rule_id)
            if not rule:
                raise ProfileValidationError(
                    f"Rule not loaded: {rule_id}"
                )

            before = text
            text = self._apply_single_rule(text, rule)

            if self.enable_debug:
                self._debug(rule_id, before, text)

        return text

    # ---------------------------------------------------------
    # Internal helpers
    # ---------------------------------------------------------

    def _prepare_rules(self, raw_rules: Dict[str, dict]) -> Dict[str, dict]:
        """
        Pre-compiles regex patterns and validates rule structure.
        """
        prepared = {}

        for rule_id, rule in raw_rules.items():
            rule_type = self._get_rule_type(rule)

            if rule_type == "regex":
                prepared[rule_id] = self._prepare_regex_rule(rule, rule_id)

            elif rule_type == "replace":
                prepared[rule_id] = self._prepare_replace_rule(rule, rule_id)

            else:
                raise ProfileValidationError(
                    f"Unsupported rule type in {rule_id}"
                )

        return prepared

    def _apply_single_rule(self, text: str, rule: dict) -> str:
        """
        Dispatch rule execution based on rule type.
        """
        rule_type = rule["type"]

        if rule_type == "regex":
            return rule["compiled_pattern"].sub(
                rule["replace"], text
            )

        if rule_type == "replace":
            for src, tgt in rule["replacements"].items():
                text = text.replace(src, tgt)
            return text

        # Defensive programming: unreachable
        raise ProfileValidationError("Invalid rule execution state")

    # ---------------------------------------------------------
    # Rule preparation & validation
    # ---------------------------------------------------------

    def _get_rule_type(self, rule: dict) -> str:
        """
        Determines rule type based on keys.
        """
        if "pattern" in rule and "replace" in rule:
            return "regex"

        if "replacements" in rule:
            return "replace"

        raise ProfileValidationError(
            "Rule must define either regex or replacements"
        )

    def _prepare_regex_rule(self, rule: dict, rule_id: str) -> dict:
        """
        Validates and compiles regex rules.
        """
        try:
            compiled = re.compile(rule["pattern"])
        except re.error as exc:
            raise ProfileValidationError(
                f"Invalid regex in rule {rule_id}: {exc}"
            )

        return {
            "type": "regex",
            "description": rule.get("description", ""),
            "compiled_pattern": compiled,
            "replace": rule["replace"]
        }

    def _prepare_replace_rule(self, rule: dict, rule_id: str) -> dict:
        """
        Validates simple replacement rules.
        """
        replacements = rule.get("replacements")
        if not isinstance(replacements, dict):
            raise ProfileValidationError(
                f"Rule {rule_id} replacements must be a dictionary"
            )

        return {
            "type": "replace",
            "description": rule.get("description", ""),
            "replacements": replacements
        }

    # ---------------------------------------------------------
    # Debugging
    # ---------------------------------------------------------

    def _debug(self, rule_id: str, before: str, after: str):
        """
        Debug output for rule application.
        """
        if before != after:
            print(f"[RULE APPLIED] {rule_id}")
