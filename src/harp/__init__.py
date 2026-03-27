"""Generate random names from adjectives and nouns.

Pure Python implementation of harp-names.
"""

from __future__ import annotations

import random
from functools import lru_cache
from pathlib import Path

try:
    from ._version import __version__
except ImportError:
    __version__ = "0.0.0"

_DATA_DIR = Path(__file__).parent


@lru_cache(maxsize=1)
def _load_adjectives() -> tuple[str, ...]:
    """Load adjectives from bundled text file."""
    path = _DATA_DIR / "adjectives.txt"
    return tuple(line.strip() for line in path.read_text().splitlines() if line.strip())


@lru_cache(maxsize=1)
def _load_nouns() -> tuple[str, ...]:
    """Load nouns from bundled text file."""
    path = _DATA_DIR / "nouns.txt"
    return tuple(line.strip() for line in path.read_text().splitlines() if line.strip())


def generate_name() -> str:
    """Generate a random name from two adjectives and a noun.

    Returns:
        A name like "bright-clever-fox"
    """
    return generate_name_with_options()


def generate_name_with_options(
    components: int = 3,
    max_element_length: int | None = None,
    separator: str = "-",
) -> str:
    """Generate a random name with custom options.

    Args:
        components: Number of components (2-16). Default: 3
        max_element_length: Maximum length per element. None means no limit.
        separator: Separator between components. Default: "-"

    Returns:
        A name like "bright-clever-fox" (with default options)
    """
    adjectives = _load_adjectives()
    nouns = _load_nouns()

    if max_element_length is not None:
        adjectives = tuple(w for w in adjectives if len(w) <= max_element_length)
        nouns = tuple(w for w in nouns if len(w) <= max_element_length)

    components = max(2, min(16, components))
    parts: list[str] = []

    # Add adjectives (components - 1)
    for _ in range(components - 1):
        if adjectives:
            parts.append(random.choice(adjectives))

    # Add noun
    if nouns:
        parts.append(random.choice(nouns))

    return separator.join(parts)


def version() -> str:
    """Get the library version."""
    return __version__
