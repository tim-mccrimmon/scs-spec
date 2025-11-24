"""Command-line interface for SCS Validator."""

import sys
from pathlib import Path
from typing import List

import click

from . import __version__
from .bundle_validator import BundleValidator
from .completeness_validator import CompletenessValidator
from .parser import Parser
from .relationship_validator import RelationshipValidator
from .reporter import Reporter
from .rules_loader import RulesLoader
from .schema_validator import SchemaValidator
from .semantic_validator import SemanticValidator
from .utils import ValidationError, ValidationResult


@click.command()
@click.argument("files", nargs=-1, type=click.Path(exists=True), required=False)
@click.option(
    "--bundle",
    "-b",
    type=click.Path(exists=True),
    help="Validate an SCD bundle file",
)
@click.option(
    "--schema-dir",
    "-s",
    type=click.Path(exists=True),
    help="Directory containing JSON schema files (default: ../../schema relative to CWD)",
)
@click.option(
    "--output",
    "-o",
    type=click.Choice(["text", "json"], case_sensitive=False),
    default="text",
    help="Output format (default: text)",
)
@click.option(
    "--strict",
    is_flag=True,
    help="Fail on warnings (exit code 2)",
)
@click.option(
    "--no-color",
    is_flag=True,
    help="Disable colored output",
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Verbose output",
)
@click.option(
    "--skip-completeness",
    is_flag=True,
    help="Skip Level 6 completeness validation",
)
@click.option(
    "--completeness-rules",
    type=click.Path(exists=True),
    help="Path to custom completeness rules file",
)
@click.version_option(version=__version__, prog_name="scs-validate")
def main(
    files: tuple,
    bundle: str | None,
    schema_dir: str | None,
    output: str,
    strict: bool,
    no_color: bool,
    verbose: bool,
    skip_completeness: bool,
    completeness_rules: str | None,
) -> None:
    """Validate SCS documents and bundles.

    Examples:

        \b
        # Validate a single SCD file
        scs-validate context/meta/roles.yaml

        \b
        # Validate multiple SCD files
        scs-validate context/meta/*.yaml

        \b
        # Validate a bundle
        scs-validate --bundle context/bundle.yaml

        \b
        # Strict mode (fail on warnings)
        scs-validate --bundle context/bundle.yaml --strict

        \b
        # JSON output
        scs-validate --bundle context/bundle.yaml --output json
    """
    try:
        # Determine schema directory
        if schema_dir:
            schema_path = Path(schema_dir)
        else:
            # Default: ../../schema relative to CWD
            schema_path = Path.cwd() / "schema"
            if not schema_path.exists():
                # Try relative to the validator location
                schema_path = Path(__file__).parent.parent.parent.parent.parent / "schema"

        if not schema_path.exists():
            click.echo(
                f"Error: Schema directory not found: {schema_path}\n"
                f"Use --schema-dir to specify the location",
                err=True,
            )
            sys.exit(4)

        # Initialize rules loader and validators
        parser = Parser()
        rules_loader = RulesLoader()
        schema_validator = SchemaValidator(schema_path)
        semantic_validator = SemanticValidator(rules_loader)
        bundle_validator = BundleValidator(rules_loader)
        relationship_validator = RelationshipValidator(rules_loader)

        # Initialize completeness validator with custom rules if provided
        completeness_rules_path = Path(completeness_rules) if completeness_rules else None
        completeness_validator = CompletenessValidator(rules_loader, completeness_rules_path)

        reporter = Reporter(use_color=not no_color)

        results: List[ValidationResult] = []

        if bundle:
            # Validate bundle
            results = validate_bundle(
                bundle,
                parser,
                schema_validator,
                semantic_validator,
                bundle_validator,
                relationship_validator,
                completeness_validator,
                verbose,
                skip_completeness,
            )
        elif files:
            # Validate individual files
            results = validate_files(
                files, parser, schema_validator, semantic_validator, verbose
            )
        else:
            click.echo("Error: No files or bundle specified\n", err=True)
            click.echo(click.get_current_context().get_help())
            sys.exit(3)

        # Generate report
        if output == "json":
            report = reporter.report_json(results, __version__, strict)
        else:
            report = reporter.report_text(results, __version__, strict)

        click.echo(report)

        # Determine exit code
        exit_code = determine_exit_code(results, strict)
        sys.exit(exit_code)

    except ValidationError as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(5)
    except Exception as e:
        click.echo(f"Unexpected error: {e}", err=True)
        if verbose:
            import traceback

            traceback.print_exc()
        sys.exit(5)


def validate_files(
    file_paths: tuple,
    parser: Parser,
    schema_validator: SchemaValidator,
    semantic_validator: SemanticValidator,
    verbose: bool,
) -> List[ValidationResult]:
    """Validate individual SCD files.

    Args:
        file_paths: Paths to SCD files
        parser: Parser instance
        schema_validator: Schema validator instance
        semantic_validator: Semantic validator instance
        verbose: Verbose output flag

    Returns:
        List of validation results
    """
    syntax_result = ValidationResult("syntax")
    schema_result = ValidationResult("schema")
    semantic_result = ValidationResult("semantic")

    files_checked = 0

    for file_path_str in file_paths:
        file_path = Path(file_path_str)

        if verbose:
            click.echo(f"Validating {file_path}...")

        try:
            # Parse file (syntax validation)
            scd = parser.load_scd(file_path)
            files_checked += 1

            # Schema validation
            result = schema_validator.validate_scd(scd, str(file_path))
            schema_result.errors.extend(result.errors)
            schema_result.warnings.extend(result.warnings)
            if not result.passed:
                schema_result.passed = False

            # Semantic validation
            result = semantic_validator.validate_scd(scd, str(file_path))
            semantic_result.errors.extend(result.errors)
            semantic_result.warnings.extend(result.warnings)
            if not result.passed:
                semantic_result.passed = False

        except ValidationError as e:
            syntax_result.add_error(e)

    syntax_result.details["files_checked"] = files_checked
    schema_result.details["files_checked"] = files_checked
    semantic_result.details["files_checked"] = files_checked

    return [syntax_result, schema_result, semantic_result]


def validate_bundle(
    bundle_path: str,
    parser: Parser,
    schema_validator: SchemaValidator,
    semantic_validator: SemanticValidator,
    bundle_validator: BundleValidator,
    relationship_validator: RelationshipValidator,
    completeness_validator: CompletenessValidator,
    verbose: bool,
    skip_completeness: bool,
) -> List[ValidationResult]:
    """Validate an SCD bundle.

    Args:
        bundle_path: Path to bundle file
        parser: Parser instance
        schema_validator: Schema validator instance
        semantic_validator: Semantic validator instance
        bundle_validator: Bundle validator instance
        relationship_validator: Relationship validator instance
        completeness_validator: Completeness validator instance
        verbose: Verbose output flag
        skip_completeness: Skip Level 6 completeness validation

    Returns:
        List of validation results
    """
    syntax_result = ValidationResult("syntax")
    bundle_schema_result = ValidationResult("bundle_schema")
    semantic_result = ValidationResult("semantic")
    bundle_result = ValidationResult("bundle")
    relationship_result = ValidationResult("relationships")
    completeness_result = ValidationResult("completeness")

    if verbose:
        click.echo(f"Validating bundle {bundle_path}...")

    try:
        # Level 1: Parse bundle (syntax validation)
        bundle = parser.load_bundle(Path(bundle_path))
        bundle_id = bundle.get('id', 'unknown')
        bundle_type = bundle.get('type', 'unknown')

        if verbose:
            click.echo(f"Bundle ID: {bundle_id}")
            click.echo(f"Bundle Type: {bundle_type}")

        # Level 2: Validate bundle schema
        bundle_schema_result = schema_validator.validate_bundle(bundle, bundle_path)
        if not bundle_schema_result.passed:
            # Stop here if schema validation fails
            return [syntax_result, bundle_schema_result]

        # Level 5: Validate bundle organization (XOR constraint, bundle type rules)
        bundle_result = bundle_validator.validate_bundle(bundle, bundle_path)

        # Load SCDs for further validation
        all_scds = []
        scd_refs = bundle.get("scds", [])

        if scd_refs and verbose:
            click.echo(f"Loading {len(scd_refs)} SCDs from bundle...")

        for scd_ref in scd_refs:
            # For now, we assume SCDs are referenced by ID
            # In a real implementation, you'd resolve these to file paths
            # This is a simplified version that works with in-bundle SCDs
            pass

        # Level 3: Semantic validation (for each SCD)
        # Level 4: Relationship validation
        if scd_refs:
            relationship_result = relationship_validator.validate_relationships(
                all_scds, bundle_type, bundle_path
            )

        # Level 6: Completeness validation (if not skipped)
        if not skip_completeness and bundle_type == "project":
            project_root = Path(bundle_path).parent
            completeness_result = completeness_validator.validate_completeness(
                bundle, all_scds, bundle_path, project_root
            )
        elif skip_completeness and verbose:
            click.echo("Skipping completeness validation (--skip-completeness)")

    except ValidationError as e:
        syntax_result.add_error(e)

    results = [syntax_result, bundle_schema_result, semantic_result, bundle_result]

    if relationship_result.errors or relationship_result.warnings:
        results.append(relationship_result)

    if not skip_completeness and (completeness_result.errors or completeness_result.warnings):
        results.append(completeness_result)

    return results


def determine_exit_code(results: List[ValidationResult], strict: bool) -> int:
    """Determine exit code based on validation results.

    Args:
        results: List of validation results
        strict: Whether strict mode is enabled

    Returns:
        Exit code (0=success, 1=errors, 2=warnings in strict mode)
    """
    has_errors = any(not r.passed for r in results)
    has_warnings = any(r.warning_count > 0 for r in results)

    if has_errors:
        return 1
    elif strict and has_warnings:
        return 2
    else:
        return 0


if __name__ == "__main__":
    main()
