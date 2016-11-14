# coding=utf-8
"""Install YouTube audio scraper."""
from setuptools import find_packages, setup

setup(
    name='youtube_audio_scraper',
    version='1.0.1',
    description='Download audio from YouTube with a simple command-line interface.',
    license='MIT',
    author='Carl Thomé',
    author_email='carlthome@gmail.com',
    url='https://github.com/carlthome/youtube-audio-scraper',
    packages=find_packages(),
    install_requires=['youtube-dl', 'pafy'],
    entry_points={
        'console_scripts':
        ['youtube-audio-scrape = youtube_audio_scraper.__main__:main']
    })
