#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import setup  # pylint: disable=deprecated-module

with open("version", encoding="utf8") as version_file:
    version = version_file.read().strip()

with open("requirements.txt", "r", encoding="utf8") as requirement_file:
    requires = [line for line in requirement_file.readlines() if not line.startswith("-")]

setup_args = {
    "name": "span-ranking-coding-test",
    "version": version,
    "description": "SPAN Back-End coding challenge solution",
    "long_description": "This is my solution to the Back-End coding challenge as part of SPAN's interview process",
    "author": "Charl Ritter",
    "author_email": "charlritter@hotmail.com",
    "url": "https://github.com/CharlRitter/span-ranking-coding-test",
    "packages": find_packages(),
    "install_requires": requires,
    "python_requires": ">=3.10",
}

setup(**setup_args)
