# coding=utf-8
"""Rip audio from YouTube videos."""
import os
import re
import subprocess
import pafy

try:
    from urllib.parse import urlencode
    from urllib.request import urlopen
except ImportError:
    from urllib import urlencode, urlopen


def scrape(query, include, exclude, quiet, overwrite, fileformat):
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

        # Since pafy.Stream object (audio) does not appear to grab audio content itself until Stream.download(), 
        #   we must convert the audio after download with ffmpeg. 
        # Convert to fileformat using ffmpeg
        if fileformat:
            audio_name = str(audio.title)
            audio_extension = str(audio.extension)
            command = ['ffmpeg', '-hide_banner', '-loglevel', 'panic', # quiet ffmpeg stdout
                       '-i', "./{0}.{1}".format(audio_name, audio_extension), # input file to convert
                       '-f', '{}'.format(fileformat), # output fileformat type
                       '-ac', '1', # mono channel
                       '-ar', '16000', # sampling rate 16000Hz
                       '-vn', # only want audio, no video
                       "./{0}/{1}.{0}".format(fileformat, audio_name.replace(" ","_"))] # output file 
            subprocess.call(command)
           