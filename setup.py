#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 08:34:16 2019

@author: abhijithneilabraham
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyorganise",
    version="0.0.3",
    author="Vishnu Prakash",
    author_email="visheh10@gmail.com",
    description="A lightweight solution to organise your folders and files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bat-fleck/pyOrganize",
    packages=setuptools.find_packages(),
      install_requires=[         
          'watchdog',
      ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)