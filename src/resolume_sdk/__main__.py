"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Resolume SDK."""


if __name__ == "__main__":
    main(prog_name="resolume_sdk")  # pragma: no cover
