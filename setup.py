#!/usr/bin/env python
# encoding: utf-8

from __future__ import with_statement
from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="colab-a11y-utils",
    version="0.0.3",
    description="Tools to improve Google Colab experience for screen reader users",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="hassaku",
    author_email="hassaku.apps@gmail.com",
    url="https://github.com/hassaku/colab-a11y-utils",
    py_modules=["colab_a11y_utils"],
    include_package_data=True,
    install_requires=["pydub", "ipython", "tqdm"],
    tests_require=["nose", "mock"],
    license="MIT",
    keywords="accessibility google-colab screen-reader visually-impaired",
    zip_safe=False,
    classifiers=[]
)
