# coding=utf-8
"""Testing module for the audio scraper."""
import audioscrape


def test():
    # A basic system test.
    audioscrape.download(
        query='Cerulean Crayons',
        include=['guitar'],
        exclude=['remix'],
        quiet=True)
