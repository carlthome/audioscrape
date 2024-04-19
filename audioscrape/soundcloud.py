"""Search SoundCloud playlists for audio."""

import json
import logging
import os
import string
import sys

import requests
from sclib import SoundcloudAPI, Track
from tqdm import tqdm

logger = logging.getLogger(__name__)


def sanitize(s):
    valid = f"-_.() {string.ascii_letters}{string.digits}"
    return "".join(c for c in s if c in valid)


if "SOUNDCLOUD_API_KEY" in os.environ:
    API_KEY = os.environ["SOUNDCLOUD_API_KEY"]
else:
    API_KEY = "81f430860ad96d8170e3bf1639d4e072"

SEARCH_URL = "https://api.soundcloud.com/search?q={query}&facet=model&limit={limit}&offset=0&linked_partitioning=1&client_id={client_id}"


def scrape(query, include, exclude, quiet, verbose, overwrite, limit):
    """Search SoundCloud and download audio from discovered playlists."""

    url = SEARCH_URL.format(query=query, limit=1, client_id=API_KEY)

    breakpoint()
    print(url)
    while url:
        response = requests.get(url)

        if response.status_code != 200:
            logger.error(
                "Failed to search SoundCloud.",
                extra={"response": response, "query": query},
            )

        try:
            doc = json.loads(response.text)
        except json.JSONDecodeError:
            logger.exception("Could not parse JSON.")

        for entity in doc["collection"]:
            if entity["kind"] == "track":
                yield entity["permalink_url"]

        url = doc.get("next_href")

    # Launch SoundCloud client.
    client = SoundcloudAPI()

    # Search SoundCloud for tracks.
    url = SoundcloudAPI.SEARCH_URL.format(
        query=query,
        client_id=client_id,
        limit=limit,
        offset=offset,
    )

    track = client.resolve("https://soundcloud.com/itsmeneedle/sunday-morning")

    assert type(track) is Track

    filename = f"./{track.artist} - {track.title}.mp3"

    with open(filename, "wb+") as file:
        track.write_mp3_to(file)

    # Generator for yielding all results pages.
    def pagination(x):
        yield x
        while x.next_href:
            x = client.get(x.next_href)
            yield x

    # Search SoundCloud for playlists.
    for playlists in pagination(
        client.get(
            "/playlists",
            q=query,
            tags=",".join(include) if include else "",
            linked_partitioning=1,
            representation="compact",
        )
    ):
        # Download playlists.
        for playlist in playlists.collection:
            # Skip playlists containing filter terms.
            metadata = [playlist.title]
            if playlist.description:
                metadata.append(playlist.description)
            haystack = " ".join(metadata).lower()
            if any(needle in haystack for needle in exclude):
                continue

            # Create directory for playlist.
            directory = sanitize(playlist.title)
            if directory == "":
                continue
            if not os.path.exists(directory):
                os.mkdir(directory)

            # Download tracks in playlist.
            for track in client.get(playlist.tracks_uri):
                file = os.path.join(directory, sanitize(track.title) + ".mp3")

                # Skip existing files.
                if os.path.exists(file) and not overwrite:
                    continue

                # Skip tracks that are not allowed to be streamed.
                if not track.streamable:
                    continue

                # Skip tracks named with filter terms.
                haystack = (track.title + " " + track.description + " " + track.tag_list).lower()
                if any(needle in haystack for needle in exclude):
                    continue

                # Download track.
                r = requests.get(client.get(track.stream_url, allow_redirects=False).location, stream=True)
                total_size = int(r.headers["content-length"])
                chunk_size = 1000000  # 1 MB chunks
                with open(file, "wb") as f:
                    for data in tqdm(
                        r.iter_content(chunk_size),
                        desc=track.title,
                        total=total_size / chunk_size,
                        unit="MB",
                        file=sys.stdout,
                    ):
                        f.write(data)
