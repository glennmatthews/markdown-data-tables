"""Tests for the MarkdownDataTablesPreprocessor."""

import os.path

import markdown

from markdown_data_tables import MarkdownDataTablesPreprocessor


def test_no_includes():
    """A file without the magic data-table string should be left unmodified."""
    source = """\
Hello world!

Nothing to see here.
"""
    lines = source.split("\n")
    processed_lines = MarkdownDataTablesPreprocessor(markdown.Markdown(), {"base_path": os.path.dirname(__file__)}).run(
        lines
    )
    for line, processed_line in zip(lines, processed_lines):
        assert line == processed_line


def test_simple_include():
    """Simplest data-table include case."""
    source = """\
{data-table simple.yaml}
"""
    lines = source.split("\n")
    processed_lines = MarkdownDataTablesPreprocessor(markdown.Markdown(), {"base_path": os.path.dirname(__file__)}).run(
        lines
    )
    assert (
        "\n".join(processed_lines)
        == """\
| Alphabet   | Greek   |
|------------|---------|
| A          | ɑ       |
| B          | β       |
"""
    )


def test_indented_include():
    """Indented include results in an indented table."""
    source = """\
!!! info "Here's a table"
    {data-table simple.yaml}
"""
    lines = source.split("\n")
    processed_lines = MarkdownDataTablesPreprocessor(markdown.Markdown(), {"base_path": os.path.dirname(__file__)}).run(
        lines
    )
    assert (
        "\n".join(processed_lines)
        == """\
!!! info "Here's a table"
    | Alphabet   | Greek   |
    |------------|---------|
    | A          | ɑ       |
    | B          | β       |
"""
    )
