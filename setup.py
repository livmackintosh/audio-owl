#!/usr/bin/env python3

from setuptools import setup

setup(
    name='AudioOwl',
    version='0.1.0',
    description='A very relaxing audio player.',
    author='Olivia Mackintosh',
    author_email='livvy@base.nu',
    packages=['audioowl'],
    entry_points={
        'console_scripts': [
            'audioowl = audioowl.gui:run',
        ]
    }
)
