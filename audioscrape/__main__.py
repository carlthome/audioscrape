# coding=utf-8
"""Download audio."""
import argparse
import sys
import os

from . import soundcloud, youtube


def download(query, include=None, exclude=None, quiet=False,
             overwrite=False, fileformat=None):
    """Scrape various websites for audio."""
    # Create subdirectory for converted audio files if --fileformat tag set
    if fileformat:
        if not os.path.exists(fileformat):
                os.makedirs(fileformat)
    youtube.scrape(query, include, exclude, quiet, overwrite, fileformat)
    soundcloud.scrape(query, include, exclude, quiet, overwrite, fileformat)


def cli(args=None):
    """CLI for scraping audio."""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'query',
        default="Cerulean Crayons",
        nargs='?',
        help="search terms"
    )
    parser.add_argument(
        '-i',
        '--include',
        default=[],
        action='append',
        help="only download audio with this tag"
    )
    parser.add_argument(
        '-e',
        '--exclude',
        default=[],
        action='append',
        help="ignore results with this tag"
    )
    parser.add_argument(
        '-q',
        '--quiet',
        default=False,
        action='store_true',
        help="hide progress reporting"
    )
    parser.add_argument(
        '-o',
        '--overwrite',
        default=False,
        action='store_true',
        help="overwrite existing files"
    )
    parser.add_argument(
        '-ff',
        '--fileformat',
        default=None,
        action='store',
        help="file format to save audio file as (wav, mp3, ogg)"
    )
    args = parser.parse_args()

    if not args.quiet:
        print('Downloading audio from "{}" videos tagged {} and not {}.'.
              format(args.query, args.include, args.exclude))
    download(args.query,
             args.include,
             args.exclude,
             args.quiet,
             args.overwrite,
             args.fileformat)
    if not args.quiet:
        print("Finished downloading audio.")


if __name__ == "__main__":
    cli(sys.argv[1:])
