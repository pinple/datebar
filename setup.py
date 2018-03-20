#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='datebar',
    version='0.0.7',
    author='neulana',
    author_email='fupinyou@gmail.com',
    description='Show a bar to display the progress of the year',
    url='https://github.com/Neulana/datebar',
    license='MIT Licence',
    packages=['datebar'],
    entry_points={
        'console_scripts': [
            'datebar=datebar:main'
        ]
    }
)
