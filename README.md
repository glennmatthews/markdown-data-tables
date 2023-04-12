# Markdown Data Tables

A simple extension for the [`Markdown` Python library](https://python-markdown.github.io) to permit importing YAML files and rendering their contents inline as Markdown tables. Intentionally very simple and lightweight; for a heavier but more full-featured alternative, consider using [`mkdocs-table-reader-plugin`](https://github.com/timvink/mkdocs-table-reader-plugin).

This plugin was originally developed for use with the [Nautobot](https://docs.nautobot.com/) project's documentation but should be reusable.

## Usage

Install this plugin with `pip install markdown_data_tables`. You can use it directly from the Markdown library with a call such as:

```python
output = markdown.Markdown(extensions=["markdown_data_tables"].convert(input_string)
```

or, if using [`MkDocs`](https://www.mkdocs.org/), enable it in your `mkdocs.yml` as follows:

```yaml
markdown_extensions:
  - "markdown_data_tables"
```

or, to specify the file path that contains the YAML data files:

```yaml
markdown_extensions:
  - "markdown_data_tables":
      base_path: "path/to/files/"
```

In your Markdown file or other documentation, you can then use the following macro:

```markdown
{data-table my_filename.yaml}
```

Note the following requirements:

- This macro must appear on a line by itself; leading whitespace is permitted (`    {data-table ...`) but no other text may appear on this line.
- No spaces between the opening `{` and `data-table` or between the filename/path and the closing `}`
- The specified filename must either be an absolute path or a path relative to the configured `base_path` (which defaults to the current directory if unset)
- The specified file must be in YAML format and contain a list of dicts, where in each dict the keys are the columns of the table and the values are the values to display in each such column.

For example:

```yaml
---
- Alphabet: "A"
  Greek: "ɑ"
- Alphabet: "B"
  Greek: "β"
```

would be a valid data-table file, and would be rendered into Markdown as the table:

```markdown
| Alphabet   | Greek   |
|------------|---------|
| A          | ɑ       |
| B          | β       |
```

## Development

The development environment for this plugin is based on [invoke](http://www.pyinvoke.org/) and [Poetry](https://python-poetry.org/). After installing Poetry itself, you can run `poetry shell` followed by `poetry install` to set up a Python virtual environment populated with this plugin's development tool dependencies. You can then use the installed `invoke` command to execute various development tasks:

```shell
$ invoke --list
Available tasks:

  bandit       Run bandit to validate basic static code security analysis.
  black        Run black to check that Python files adherence to black standards.
  flake8       Run flake8 code analysis.
  pydocstyle   Run pydocstyle to validate docstring formatting adheres to standards.
  pylint       Run pylint code analysis.
  pytest       Run pytest test cases.
  tests        Run all linters and tests for this repository.
  yamllint     Run yamllint to validate formatting adheres to YAML standards.
```

After making any code change, it is recommended to run `invoke tests` before committing your code.
