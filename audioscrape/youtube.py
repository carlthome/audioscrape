# coding=utf-8
"""Rip audio from YouTube videos."""
import os
import re

import pafy

try:
    from urllib.parse import urlencode
    from urllib.request import urlopen
except ImportError:
    from urllib import urlencode, urlopen


def scrape(query, include, exclude, quiet, overwrite):
    """Search YouTube and download audio from discovered videos."""

    # Search YouTube for videos.
    url = 'http://youtube.com/results?' + urlencode({'search_query': query})
    html = urlopen(url).read().decode('utf-8')
    video_ids = re.findall(r'href=\"\/watch\?v=(.{11})', html)

    # Go through all found videos.
    for video_id in video_ids:

        # Fetch metadata and available streams.
        video = pafy.new(video_id)

        # Collect video metadata.
        metadata = video.keywords + [
            video.title, video.author, video.description, video.category
        ]
        haystack = ' '.join(metadata).lower()

        # Don't download audio if video lacks a required term in its metadata.
        if include:
            if all(w not in haystack for w in include):
                continue

        # Don't download audio if video has a forbidden term in its metadata.
        if exclude:
            if any(w in haystack for w in exclude):
                continue

        # Always prefer highest quality audio.
        audio = video.getbestaudio()

        # Skip existing files.
        if os.path.isfile(audio.filename) and not overwrite:
            continue

        # Download audio to working directory.
        audio.download(quiet=quiet)
