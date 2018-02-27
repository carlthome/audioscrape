# coding=utf-8
"""Testing module for the audio scraper."""
import audioscrape


def test():
    audioscrape.download(
        query='Cerulean Crayons',
        include=['guitar'],
        exclude=['remix'],
        quiet=False)
