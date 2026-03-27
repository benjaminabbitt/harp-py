"""Tests for harp CLI."""

from harp.cli import main


class TestCli:
    """Tests for the harp CLI."""

    def test_default_output(self, capsys):
        result = main([])
        assert result == 0
        captured = capsys.readouterr()
        # Default: 3 components with dash separator
        parts = captured.out.strip().split("-")
        assert len(parts) == 3

    def test_two_components(self, capsys):
        result = main(["-c", "2"])
        assert result == 0
        captured = capsys.readouterr()
        parts = captured.out.strip().split("-")
        assert len(parts) == 2

    def test_custom_separator(self, capsys):
        result = main(["-s", "_"])
        assert result == 0
        captured = capsys.readouterr()
        assert "_" in captured.out
        assert "-" not in captured.out.strip()

    def test_multiple_names(self, capsys):
        result = main(["-n", "5"])
        assert result == 0
        captured = capsys.readouterr()
        lines = captured.out.strip().split("\n")
        assert len(lines) == 5

    def test_max_length(self, capsys):
        result = main(["-m", "4"])
        assert result == 0
        captured = capsys.readouterr()
        for part in captured.out.strip().split("-"):
            assert len(part) <= 4

    def test_combined_options(self, capsys):
        result = main(["-c", "2", "-s", "_", "-n", "3"])
        assert result == 0
        captured = capsys.readouterr()
        lines = captured.out.strip().split("\n")
        assert len(lines) == 3
        for line in lines:
            parts = line.split("_")
            assert len(parts) == 2
