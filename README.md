# Audio Scraper
[![Build Status](https://travis-ci.org/carlthome/audio-scraper.svg?branch=master)](https://travis-ci.org/carlthome/audio-scraper)
[![PyPI](https://img.shields.io/pypi/v/audioscrape.svg)](https://pypi.python.org/pypi/audioscrape)
[![PyPI](https://img.shields.io/pypi/pyversions/audioscrape.svg)](http://py3readiness.org/)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

Scrape audio from various websites with a simple command-line interface.

# Install
First make sure Python and pip are installed, then run:
```sh
pip install audioscrape
```

# Usage
```sh
audioscrape "acoustic guitar"
```

See `audioscrape --help` for more details.

## Python API
You could also use the scraper directly in Python, as:

```python
import audioscrape

audioscrape.download(query='Cerulean Crayons', 
                     include=['guitar'],
                     exclude=['remix'],
                     quiet=True)
```

## SoundCloud API key and download limits
This program uses SoundCloud's official Python API which requires a registered API key. SoundCloud says an API key can be used for 15,000 requests per any 24-hour time window, and a key has been included in the program. However, in case the key stops working, register another one [as described by SoundCloud here](https://github.com/soundcloud/soundcloud-python#basic-use), and use the scraper after setting the environment variable `SOUNDCLOUD_API_KEY`, as `SOUNDCLOUD_API_KEY="your_key" audioscrape "piano music"`.
