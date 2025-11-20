"""Semantic validation module for SCDs."""

import re
from datetime import datetime
from typing import Any, Dict

import semver

from .utils import ValidationError, ValidationResult, ValidationWarning, get_tier_from_id


class SemanticValidator:
    """Validator for semantic consistency of SCDs."""

    @staticmethod
    def validate_scd(scd: Dict[str, Any], file_path: str | None = None) -> ValidationResult:
        """Validate semantic consistency of an SCD.

        Args:
            scd: SCD data as dictionary
            file_path: Optional file path for error messages

        Returns:
            ValidationResult with errors and warnings
        """
        result = ValidationResult("semantic")

        scd_id = scd.get("id", "unknown")
        scd_type = scd.get("type")

        # Validate type matches tier in ID
        SemanticValidator._validate_type_tier_match(scd_id, scd_type, result, file_path)

        # Validate version is valid semver
        version = scd.get("version")
        if version:
            SemanticValidator._validate_version(version, scd_id, result, file_path)

        # Validate provenance
        provenance = scd.get("provenance", {})
        SemanticValidator._validate_provenance(provenance, scd_id, result, file_path)

        # Validate ID format
        SemanticValidator._validate_id_format(scd_id, result, file_path)

        # Validate required string fields are not empty
        SemanticValidator._validate_required_strings(scd, scd_id, result, file_path)

        return result

    @staticmethod
    def _validate_type_tier_match(
        scd_id: str,
        scd_type: str | None,
        result: ValidationResult,
        file_path: str | None,
    ) -> None:
        """Validate that type field matches tier in ID."""
        tier = get_tier_from_id(scd_id)
        if not tier:
            # Already caught by schema validation
            return

        if not scd_type:
            result.add_error(
                ValidationError(
                    "Missing 'type' field",
                    scd_id=scd_id,
                    file_path=file_path,
                )
            )
            return

        if tier != scd_type:
            result.add_error(
                ValidationError(
                    f"Type '{scd_type}' does not match tier '{tier}' in ID '{scd_id}'",
                    scd_id=scd_id,
                    file_path=file_path,
                )
            )

    @staticmethod
    def _validate_version(
        version: str, scd_id: str, result: ValidationResult, file_path: str | None
    ) -> None:
        """Validate version follows semantic versioning."""
        try:
            # Try to parse as semver
            semver.VersionInfo.parse(version)
        except ValueError as e:
            result.add_error(
                ValidationError(
                    f"Version '{version}' is not valid semantic versioning: {e}",
                    scd_id=scd_id,
                    file_path=file_path,
                )
            )

    @staticmethod
    def _validate_provenance(
        provenance: Dict[str, Any],
        scd_id: str,
        result: ValidationResult,
        file_path: str | None,
    ) -> None:
        """Validate provenance section."""
        if not provenance:
            result.add_warning(
                ValidationWarning(
                    "Provenance section is empty",
                    level="semantic",
                    scd_id=scd_id,
                    file_path=file_path,
                )
            )
            return

        # Check created_by
        created_by = provenance.get("created_by")
        if not created_by or not created_by.strip():
            result.add_error(
                ValidationError(
                    "Provenance 'created_by' is required and must not be empty",
                    scd_id=scd_id,
                    file_path=file_path,
                )
            )

        # Check created_at timestamp
        created_at = provenance.get("created_at")
        if created_at:
            SemanticValidator._validate_timestamp(
                created_at, "created_at", scd_id, result, file_path
            )

        # Check updated_at timestamp if present
        updated_at = provenance.get("updated_at")
        if updated_at:
            SemanticValidator._validate_timestamp(
                updated_at, "updated_at", scd_id, result, file_path
            )

        # Warn if rationale is missing
        rationale = provenance.get("rationale")
        if not rationale or not rationale.strip():
            result.add_warning(
                ValidationWarning(
                    "Provenance 'rationale' is recommended but missing",
                    level="semantic",
                    scd_id=scd_id,
                    file_path=file_path,
                )
            )

    @staticmethod
    def _validate_timestamp(
        timestamp: str, field_name: str, scd_id: str, result: ValidationResult, file_path: str | None
    ) -> None:
        """Validate timestamp is ISO8601 format."""
        try:
            datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        except (ValueError, AttributeError) as e:
            result.add_error(
                ValidationError(
                    f"Provenance '{field_name}' is not valid ISO8601 format: {e}",
                    scd_id=scd_id,
                    file_path=file_path,
                )
            )

    @staticmethod
    def _validate_id_format(scd_id: str, result: ValidationResult, file_path: str | None) -> None:
        """Validate ID follows proper format."""
        # Pattern: scd:<tier>:<name>
        # tier: meta, project, standards
        # name: alphanumeric, dots, underscores, hyphens
        pattern = r"^scd:(meta|project|standards):[a-zA-Z0-9._-]+$"

        if not re.match(pattern, scd_id):
            result.add_error(
                ValidationError(
                    f"ID '{scd_id}' does not match required pattern 'scd:<tier>:<name>'",
                    scd_id=scd_id,
                    file_path=file_path,
                )
            )

    @staticmethod
    def _validate_required_strings(
        scd: Dict[str, Any], scd_id: str, result: ValidationResult, file_path: str | None
    ) -> None:
        """Validate required string fields are not empty."""
        required_fields = ["title", "description"]

        for field in required_fields:
            value = scd.get(field)
            if value is not None and isinstance(value, str):
                if not value.strip():
                    result.add_error(
                        ValidationError(
                            f"Field '{field}' must not be empty",
                            scd_id=scd_id,
                            file_path=file_path,
                        )
                    )
