#!/usr/bin/env python
# coding: utf8

from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

setup(name='PyBioC',
      version='2.0',
      author='Hernani Marques',
      author_email='h2m@access.uzh.ch',
      description='Python library for working with BioC XML data',
      long_description=readme,
      packages=['bioc', 'bioc.meta', 'bioc.compat'],
      package_dir={'bioc': 'src/bioc'})
