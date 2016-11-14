# coding=utf-8
"""Download audio from YouTube."""
import argparse
import re
import sys

import pafy

try:
    from urllib.parse import urlparse, urlencode
    from urllib.request import urlopen
except ImportError:
    from urllib import urlencode, urlopen


def scrape(query, include, exclude, quiet):
    """Search YouTube and download audio from discovered videos."""

    # Search YouTube for videos.
    html = urlopen("http://youtube.com/results?" + urlencode({
        'search_query': query
    })).read().decode('utf-8')
    video_ids = re.findall(r'href=\"\/watch\?v=(.{11})', html)

    # Go through all found videos.
    for video_id in video_ids:
    
        # Ignore broken videos for any reason and fail silently.
        try:
            video = pafy.new(video_id)
        except:
            continue

        # Collect video metadata.
        haystack = " ".join([video.title, video.description, video.category] +
                            video.keywords).lower()

        # Don't download audio if video lacks a required term in its metadata.
        if include:
            if all(w not in haystack for w in include):
                continue

        # Don't download audio if video has a forbidden term in its metadata.
        if exclude:
            if any(w in haystack for w in exclude):
                continue

        # Download audio to working directory.
        video.getbestaudio().download(quiet=quiet)


def main(args=None):
    """CLI for scraping YouTube audio."""
    if args is None:
        args = sys.argv[1:]

    # Parse program arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'query', default="Cerulean Crayons", nargs='?', help="search YouTube")
    parser.add_argument(
        '-i',
        '--include',
        default=[],
        action='append',
        help="only rip audio from videos with this tag (this flag can be used multiple times)"
    )
    parser.add_argument(
        '-e',
        '--exclude',
        default=[],
        action='append',
        help="ignore videos with this tag (this flag can be used multiple times)"
    )
    parser.add_argument(
        '-q',
        '--quiet',
        default=False,
        action='store_true',
        help="ignore videos with this tag (this flag can be used multiple times)"
    )
    args = parser.parse_args()

    # Search YouTube and download audio from videos.
    if not args.quiet:
        print('Downloading audio from "{}" videos tagged {} and not {}.'.
              format(args.query, args.include, args.exclude))
    scrape(args.query, args.include, args.exclude, args.quiet)
    if not args.quiet:
        print("Finished downloading audio from YouTube.")


if __name__ == "__main__":
    main()
