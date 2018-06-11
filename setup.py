#!/usr/bin/env python
import os

from setuptools import setup, find_packages

setup(
    name="privvy",
    version='0.1',
    description='Syncing private files gitignored in git repositories',
    author='Chris Lee',
    author_email='chris@indico.io',
    packages=find_packages(),
    scripts=[ "bin/privvy-pull", "bin/privvy-push", "bin/privvy-init" ],
    include_package_data=True,
    package_data={ "": [ "hooks/pre-push", "hooks/pre-receive" ] },
    install_requires=[
        open(os.path.join(
                os.path.dirname(__file__),
                "requirements.txt"), "r").readlines()
    ]
)
