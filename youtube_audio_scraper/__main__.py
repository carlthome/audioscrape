# coding=utf-8
"""
Download audio from YouTube.
"""
import argparse
import re
import sys
try:
    from urllib.parse import urlparse
    from urllib.request import urlopen
except ImportError:
    from urllib import urlencode, urlopen

import pafy


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    # Parse program arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument('query', default="", nargs='?', help="search YouTube")
    parser.add_argument(
        '-i',
        '--include',
        default=[],
        action='append',
        help="only rip audio from videos with this tag (this flag can be used multiple times)")
    parser.add_argument(
        '-e',
        '--exclude',
        default=[],
        action='append',
        help="ignore videos with this tag (this flag can be used multiple times)")
    args = parser.parse_args()
    query = args.query
    include = args.include
    exclude = args.exclude

    print('Downloading audio from "{}" videos tagged {} (and not {}).'.format(
        query, include, exclude))

    # Search YouTube for videos.
    html = urlopen("http://youtube.com/results?" + urlencode(
        {'search_query': query})).read().decode()
    video_ids = re.findall(r'href=\"\/watch\?v=(.{11})', html)

    # Go through all found videos.
    for video_id in video_ids:
        video = pafy.new(video_id)

        # Video metadata.
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

        # Download audio.
        video.getbestaudio().download()

    print("Finished downloading audio from YouTube.")


if __name__ == "__main__":
    main()
