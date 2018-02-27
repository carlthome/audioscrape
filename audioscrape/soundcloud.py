# coding=utf-8
"""Search SoundCloud playlists for audio."""
from __future__ import absolute_import

import os
import string
import sys

import requests
import soundcloud
from tqdm import tqdm


def sanitize(s):
    valid = '-_.() {}{}'.format(string.ascii_letters, string.digits)
    return ''.join(c for c in s if c in valid)


if 'SOUNDCLOUD_API_KEY' in os.environ:
    API_KEY = os.environ['SOUNDCLOUD_API_KEY']
else:
    API_KEY = "81f430860ad96d8170e3bf1639d4e072"


def scrape(query, include, exclude, quiet, overwrite):
    """Search SoundCloud and download audio from discovered playlists."""

    # Launch SoundCloud client.
    client = soundcloud.Client(client_id=API_KEY)

    # Generator for yielding all results pages.
    def pagination(x):
        yield x
        while x.next_href:
            x = client.get(x.next_href)
            yield x

    # Search SoundCloud for playlists.
    for playlists in pagination(
            client.get(
                '/playlists',
                q=query,
                tags=','.join(include) if include else '',
                linked_partitioning=1,
                representation='compact')):

        # Download playlists.
        for playlist in playlists.collection:

            # Skip playlists containing filter terms.
            metadata = [playlist.title]
            if playlist.description:
                metadata.append(playlist.description)
            haystack = ' '.join(metadata).lower()
            if any(needle in haystack for needle in exclude):
                continue

            # Create directory for playlist.
            directory = sanitize(playlist.title)
            if directory == '':
                continue
            if not os.path.exists(directory):
                os.mkdir(directory)

            # Download tracks in playlist.
            for track in client.get(playlist.tracks_uri):
                file = os.path.join(directory, sanitize(track.title) + '.mp3')

                # Skip existing files.
                if os.path.exists(file) and not overwrite:
                    continue

                # Skip tracks that are not allowed to be streamed.
                if not track.streamable:
                    continue

                # Skip tracks named with filter terms.
                haystack = (track.title + ' ' + track.description + ' ' +
                            track.tag_list).lower()
                if any(needle in haystack for needle in exclude):
                    continue

                # Download track.
                r = requests.get(
                    client.get(track.stream_url,
                               allow_redirects=False).location,
                    stream=True)
                total_size = int(r.headers['content-length'])
                chunk_size = 1000000  # 1 MB chunks
                with open(file, 'wb') as f:
                    for data in tqdm(
                            r.iter_content(chunk_size),
                            desc=track.title,
                            total=total_size / chunk_size,
                            unit='MB',
                            file=sys.stdout):
                        f.write(data)
