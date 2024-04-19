"""Download audio."""

import argparse
import logging
import sys

from . import soundcloud, youtube

logger = logging.getLogger(__name__)


def download(query, include, exclude, quiet, verbose, overwrite, limit):
    """Scrape various websites for audio."""
    youtube.scrape(query, include, exclude, quiet, verbose, overwrite, limit)
    soundcloud.scrape(query, include, exclude, quiet, verbose, overwrite, limit)


def cli(args=None):
    """CLI for scraping audio."""

    parser = argparse.ArgumentParser()
    parser.add_argument("query", default="Cerulean Crayons", nargs="?", help="search terms")
    parser.add_argument("-i", "--include", default=[], action="append", help="only download audio with this tag")
    parser.add_argument("-e", "--exclude", default=[], action="append", help="ignore results with this tag")
    parser.add_argument("-q", "--quiet", default=False, action="store_true", help="hide progress reporting")
    parser.add_argument("-v", "--verbose", default=False, action="store_true", help="display debug information")
    parser.add_argument("-o", "--overwrite", default=False, action="store_true", help="overwrite existing files")
    parser.add_argument("-l", "--limit", default=10, type=int, help="limit number of downloads")
    args = parser.parse_args()

    logging.basicConfig(format="[%(name)s] %(message)s")
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    elif args.quiet:
        logger.setLevel(logging.ERROR)
    else:
        logger.setLevel(logging.INFO)

    logger.info(f'Downloading audio from "{args.query}" videos tagged {args.include} and not {args.exclude}.')
    download(args.query, args.include, args.exclude, args.quiet, args.verbose, args.overwrite, args.limit)
    logger.info("Finished downloading audio.")


if __name__ == "__main__":
    cli(sys.argv[1:])
