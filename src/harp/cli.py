"""Command-line interface for harp."""

from __future__ import annotations

import argparse
import sys

from . import __version__, generate_name_with_options


def main(argv: list[str] | None = None) -> int:
    """Main entry point for the harp CLI."""
    parser = argparse.ArgumentParser(
        prog="harp",
        description="Generate human-readable random names",
    )
    parser.add_argument(
        "-c", "--components",
        type=int,
        default=3,
        help="Number of components (2-16, default: 3)",
    )
    parser.add_argument(
        "-s", "--separator",
        default="-",
        help="Separator between components (default: -)",
    )
    parser.add_argument(
        "-m", "--max-length",
        type=int,
        default=None,
        help="Maximum length per element",
    )
    parser.add_argument(
        "-n", "--count",
        type=int,
        default=1,
        help="Number of names to generate (default: 1)",
    )
    parser.add_argument(
        "-V", "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    args = parser.parse_args(argv)

    for _ in range(args.count):
        name = generate_name_with_options(
            components=args.components,
            max_element_length=args.max_length,
            separator=args.separator,
        )
        print(name)

    return 0


if __name__ == "__main__":
    sys.exit(main())
