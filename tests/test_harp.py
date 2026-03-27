"""Tests for harp library."""

import harp


class TestGenerateName:
    """Tests for generate_name function."""

    def test_returns_string(self):
        name = harp.generate_name()
        assert isinstance(name, str)

    def test_default_has_three_components(self):
        name = harp.generate_name()
        parts = name.split("-")
        assert len(parts) == 3

    def test_produces_different_results(self):
        names = {harp.generate_name() for _ in range(10)}
        assert len(names) > 1


class TestGenerateNameWithOptions:
    """Tests for generate_name_with_options function."""

    def test_two_components(self):
        name = harp.generate_name_with_options(components=2)
        parts = name.split("-")
        assert len(parts) == 2

    def test_four_components(self):
        name = harp.generate_name_with_options(components=4)
        parts = name.split("-")
        assert len(parts) == 4

    def test_sixteen_components(self):
        name = harp.generate_name_with_options(components=16)
        parts = name.split("-")
        assert len(parts) == 16

    def test_components_clamped_to_minimum(self):
        name = harp.generate_name_with_options(components=1)
        parts = name.split("-")
        assert len(parts) == 2

    def test_components_clamped_to_maximum(self):
        name = harp.generate_name_with_options(components=20)
        parts = name.split("-")
        assert len(parts) == 16

    def test_custom_separator(self):
        name = harp.generate_name_with_options(separator="_")
        assert "_" in name
        assert "-" not in name

    def test_max_element_length(self):
        name = harp.generate_name_with_options(max_element_length=4)
        for part in name.split("-"):
            assert len(part) <= 4


class TestVersion:
    """Tests for version function."""

    def test_returns_string(self):
        v = harp.version()
        assert isinstance(v, str)

    def test_is_semver_format(self):
        v = harp.version()
        parts = v.split(".")
        assert len(parts) >= 2
        assert all(p.isdigit() for p in parts[:2])


class TestWordLists:
    """Tests for word list loading."""

    def test_adjectives_loaded(self):
        adjectives = harp._load_adjectives()
        assert len(adjectives) > 1000

    def test_nouns_loaded(self):
        nouns = harp._load_nouns()
        assert len(nouns) > 4000

    def test_no_empty_words(self):
        adjectives = harp._load_adjectives()
        nouns = harp._load_nouns()
        assert all(adj.strip() for adj in adjectives)
        assert all(noun.strip() for noun in nouns)
