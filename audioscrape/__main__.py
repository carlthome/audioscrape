# coding=utf-8
"""Download audio."""
import argparse
import sys


def scrape(query, include, exclude, quiet):
    youtube(query, include, exclude, quiet)
    soundcloud(query, include, exclude, quiet)


def main(args=None):
    """CLI for scraping audio."""
    if args is None:
        args = sys.argv[1:]

    # Parse program arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'query', default="Cerulean Crayons", nargs='?', help="search terms")
    parser.add_argument(
        '-i',
        '--include',
        default=[],
        action='append',
        help="only download audio with this tag (this flag can be used multiple times)"
    )
    parser.add_argument(
        '-e',
        '--exclude',
        default=[],
        action='append',
        help="ignore results with this tag (this flag can be used multiple times)"
    )
    parser.add_argument(
        '-q',
        '--quiet',
        default=False,
        action='store_true',
        help="hide progress reporting")
    args = parser.parse_args()

    # Search YouTube and download audio from videos.
    if not args.quiet:
        print('Downloading audio from "{}" videos tagged {} and not {}.'.
              format(args.query, args.include, args.exclude))
    scrape(args.query, args.include, args.exclude, args.quiet)
    if not args.quiet:
        print("Finished downloading audio.")


if __name__ == "__main__":
    main()
