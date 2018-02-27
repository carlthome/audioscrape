# coding=utf-8
"""Install config."""
from setuptools import find_packages, setup

setup(
    name='audioscrape',
    version='0.0.5',
    description='Scrape online audio with a simple command-line interface.',
    url='https://github.com/carlthome/audio-scraper',
    author='Carl Thomé',
    author_email='carlthome@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Sound/Audio',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='audio music sound',
    packages=find_packages(),
    install_requires=[
        'youtube-dl',
        'pafy',
        'tqdm',
        'requests',
        'soundcloud',
        'six',
    ],
    entry_points={
        'console_scripts': ['audioscrape = audioscrape.__main__:cli']
    })
