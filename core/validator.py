from core.exceptions import ProfileValidationError


REQUIRED_TOP_LEVEL_KEYS = {
    "id", "font", "script", "encoding", "rules", "mapping"
}


def validate_profile_structure(profile: dict):
    missing = REQUIRED_TOP_LEVEL_KEYS - profile.keys()
    if missing:
        raise ProfileValidationError(
            f"Missing required fields: {', '.join(missing)}"
        )


def validate_font_section(font: dict):
    if "name" not in font or "type" not in font:
        raise ProfileValidationError("Font section requires name and type")

    if font["type"] not in ("legacy", "unicode"):
        raise ProfileValidationError("Font type must be legacy or unicode")


def validate_script_section(script: dict):
    if "name" not in script or "iso" not in script:
        raise ProfileValidationError("Script section requires name and iso code")


def validate_encoding(encoding: dict):
    if encoding.get("base") not in ("ascii", "unicode"):
        raise ProfileValidationError("Encoding base must be ascii or unicode")


def validate_mapping(profile: dict):
    font_type = profile["font"]["type"]
    mapping = profile["mapping"]

    if font_type == "legacy" and not mapping:
        raise ProfileValidationError("Legacy fonts must define a mapping table")

    if font_type == "unicode" and mapping:
        raise ProfileValidationError("Unicode fonts must not define mappings")


def validate_rules(profile: dict):
    if not isinstance(profile["rules"], list):
        raise ProfileValidationError("Rules must be a list of rule IDs")
