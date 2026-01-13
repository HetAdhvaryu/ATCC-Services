"""
Conversion Engine

This module orchestrates the full font conversion pipeline:
- Profile loading
- Rule execution
- Character mapping
- Optional Unicode bridging

This is the SINGLE entry point for all conversions.
"""

from __future__ import annotations

from typing import Dict

from core.rule_engine import RuleEngine
from core.exceptions import ProfileValidationError


class ConversionEngine:
    """
    Orchestrates font conversion using profiles and rules.

    Responsibilities:
    - Apply script rules in correct order
    - Apply character mappings
    - Support legacy ↔ legacy and legacy ↔ unicode
    - Fail fast on invalid configurations
    """

    def __init__(
        self,
        source_profile: dict,
        target_profile: dict,
        rules: Dict[str, dict],
        enable_debug: bool = False
    ):
        self.source = source_profile
        self.target = target_profile
        self.rules = rules
        self.enable_debug = enable_debug

        self._validate_profiles()

        self.rule_engine = RuleEngine(
            rules=self.rules,
            enable_debug=enable_debug
        )

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def convert(self, text: str) -> str:
        """
        Convert text from source font to target font.

        :param text: Input text (plain string)
        :return: Converted text
        """
        if not text:
            return text

        # Step 1: Apply source rules (normalize structure)
        text = self.rule_engine.apply(
            text=text,
            rule_ids=self.source["rules"]
        )

        # Step 2: Apply source → intermediate mapping
        text = self._apply_mapping(
            text,
            self.source,
            direction="forward"
        )

        # Step 3: If Unicode bridge required, normalize
        if self._requires_unicode_bridge():
            text = self._unicode_normalize(text)

        # Step 4: Apply intermediate → target mapping
        text = self._apply_mapping(
            text,
            self.target,
            direction="reverse"
        )

        # Step 5: Apply target rules (rare but supported)
        if self.target["rules"]:
            text = self.rule_engine.apply(
                text=text,
                rule_ids=self.target["rules"]
            )

        return text

    # ---------------------------------------------------------
    # Internal logic
    # ---------------------------------------------------------

    def _validate_profiles(self):
        """
        Ensures source and target profiles are compatible.
        """
        if self.source["script"]["iso"] != self.target["script"]["iso"]:
            raise ProfileValidationError(
                "Source and target scripts do not match"
