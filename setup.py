# coding=utf-8
"""Install audio scraper."""
from setuptools import find_packages, setup

setup(
    name='audioscrape',
    version='0.0.0',
    description='Scrape audio from various websites.',
    license='MIT',
    author='Carl Thomé',
    author_email='carlthome@gmail.com',
    url='https://github.com/carlthome/audio-scraper',
    packages=find_packages(),
    install_requires=[
        'youtube-dl', 'pafy', 'tqdm', 'requests', 'soundcloud', 'six'
    ],
    entry_points={
        'console_scripts': ['audioscrape = audioscrape.__main__:main']
    })
