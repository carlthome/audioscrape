# coding=utf-8
"""Install config."""
from setuptools import find_packages, setup

setup(
    name='audioscrape',
    version='0.0.3',
    description='Scrape audio from various websites with a simple command-line interface.',
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
    ],
    keywords='audio music sound',
    packages=find_packages(),
    install_requires=[
        'youtube-dl', 'pafy', 'tqdm', 'requests', 'soundcloud', 'six'
    ],
    entry_points={
        'console_scripts': ['audioscrape = audioscrape.__main__:main']
    },
    include_package_data=True,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'])
