# Audioscrape

Scrape audio from various websites with a simple command-line interface.

## Usage

First make sure Python is installed, then run:

```sh
pip install audioscrape
```

Then you can use the program as:

```sh
audioscrape "acoustic guitar"
```

See `audioscrape --help` for more details.

### Python API

You can also use the scraper directly in Python, as:

```python
import audioscrape

audioscrape.download(
    query="Cerulean Crayons",
    include=["guitar"],
    exclude=["remix"],
    quiet=True,
)
```

## Develop

First clone the repo and set it as working directory. Then install the package in development mode (preferably within its own virtual environment):

```sh
pip install -e ".[tests]"
```

If you have `direnv` installed, you can run `direnv allow` to automatically create and activate a Python virtual environment when you enter the directory.

### Test

```sh
pytest
```

### Lint

```sh
pre-commit run --all-files
```

Or `pre-commit install` to run automatically on `git commit`.

### Publish

```sh
gh release create
```
