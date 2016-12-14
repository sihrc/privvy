#!/usr/bin/env python
import os

from setuptools import setup, find_packages
from pip.req import parse_requirements

setup(
    name="privvy",
    version='0.1',
    description='Indico private files sync service',
    author='indico',
    author_email='contact@indico.io',
    url='https://indico.io',
    packages=find_packages(),
    scripts=["bin/privvy-pull", "bin/privvy-push"],
    install_requires=[
        str(item.req) for item in
        parse_requirements(os.path.join(
                os.path.dirname(__file__),
                "requirements.txt"
        ), session=False)
    ]
)

import privvy

privvy.setup()
