# coding=utf-8
"""Testing module for the audio scraper."""
import numpy as np
import librosa as lr

import audioscrape

def test():
    # A basic system test.
    audioscrape.download(query='Cerulean Crayons', 
                         include=['guitar'],
                         exclude=['remix'],
                         quiet=True)
