"""
Conversion Engine

Single orchestration point for font conversion.
"""

from __future__ import annotations
from typing import Dict

from core.rule_engine import RuleEngine
from core.exceptions import ProfileValidationError


class ConversionEngine:
    """
    Orchestrates font conversion using profiles and rules.
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

    # =========================
    # Public API
    # =========================

    def convert(self, text: str) -> str:
        if not text:
            return text

        # 1. Apply source rules
        text = self.rule_engine.apply(
            text=text,
            rule_ids=self.source["rules"]
        )

        # 2. Source → intermediate mapping
        text = self._apply_mapping(
            text=text,
            profile=self.source,
            reverse=False
        )

        # 3. Unicode bridge (future-safe)
        if self._requires_unicode_bridge():
            text = self._unicode_normalize(text)

        # 4. Intermediate → target mapping
        text = self._apply_mapping(
            text=text,
            profile=self.target,
            reverse=True
        )

        # 5. Target rules (rare, but supported)
        if self.target["rules"]:
            text = self.rule_engine.apply(
                text=text,
                rule_ids=self.target["rules"]
            )

        return text

    # =========================
    # Internal helpers
    # =========================

    def _validate_profiles(self):
        if self.source["script"]["iso"] != self.target["script"]["iso"]:
            raise ProfileValidationError(
                "Source and target scripts do not match"
            )

        if (
            self.source["font"]["type"] == "unicode"
            and self.target["font"]["type"] == "unicode"
        ):
            raise ProfileValidationError(
                "Unicode to Unicode conversion is not supported"
            )

    def _requires_unicode_bridge(self) -> bool:
        return (
            self.source["font"]["type"] == "legacy"
            and self.target["font"]["type"] == "legacy"
        )

    def _apply_mapping(
        self,
        text: str,
        profile: dict,
        reverse: bool
    ) -> str:
        mapping = profile.get("mapping", {})
        if not mapping:
            return text

        if reverse:
            mapping = self._reverse_mapping(mapping)

        return "".join(mapping.get(ch, ch) for ch in text)

    def _reverse_mapping(self, mapping: dict) -> dict:
        reversed_map = {}
        for src, tgt in mapping.items():
            if tgt in reversed_map:
                raise ProfileValidationError(
                    f"Ambiguous reverse mapping for value: {tgt}"
                )
            reversed_map[tgt] = src
        return reversed_map

    def _unicode_normalize(self, text: str) -> str:
        # Placeholder for future NFC/NFD normalization
        return text
