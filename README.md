# YouTube Audio Scraper [![Build Status](https://travis-ci.org/carlthome/youtube-audio-scraper.svg?branch=master)](https://travis-ci.org/carlthome/youtube-audio-scraper)
Download audio from YouTube with a simple command-line interface.

# Install
First make sure Python and pip are installed, then run:
```sh
pip install git+https://github.com/carlthome/youtube-audio-scraper.git
```

# Usage
```sh
youtube-audio-scrape "acoustic guitar"
```

See `youtube-audio-scrape --help` for more details.

## Python API
You could also use the scraper directly in Python, as:

```sh
from youtube_audio_scraper import scrape

scrape(query='Cerulean Crayons', 
       include=['guitar'],
       exclude=['remix'],
       quiet=True)
```

# Uninstall
After having downloaded some audio, remove the scraper by running:
```sh
pip uninstall youtube-audio-scraper
```
