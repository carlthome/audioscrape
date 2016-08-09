# coding=utf-8
"""
Install YouTube audio scraper.
"""
from setuptools import find_packages, setup

import youtube_audio_scraper

setup(
    name='youtube_audio_scraper',
    version=youtube_audio_scraper.__version__,
    long_description=open('README.md').read(),
    license=open('LICENSE').read(),
    author='Carl Thomé',
    author_email='carlthome@gmail.com',
    url='https://github.com/carlthome/youtube-audio-scraper',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': [
            'youtube-audio-scrape = youtube_audio_scraper.__main__:main'
        ]
    }, )
