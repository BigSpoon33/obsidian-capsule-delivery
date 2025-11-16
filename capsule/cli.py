"""Main CLI application using Typer framework"""

import typer
from capsule import __version__

app = typer.Typer(
    name="capsule",
    help="Obsidian Capsule Delivery System - AI-powered content generation",
    add_completion=False,
)


def version_callback(value: bool) -> None:
    """Display version information"""
    if value:
        typer.echo(f"Obsidian Capsule CLI v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Show version and exit",
    ),
) -> None:
    """
        Obsidian Capsule Delivery System

        AI-powered content generation and distribution for Obsidian knowledge bases.

        For detailed documentation, visit: https://github.
    com/<username>/obsidian-capsule-delivery
    """
    pass


if __name__ == "__main__":
    app()
