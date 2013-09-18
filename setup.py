#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(

    name='nap-todos',
    version='0.0.2',
    description='Nap Todos',
    author='Virtusize AB',
    author_email='contact@virtusize.com',
    url='http://www.virtusize.com/',

    packages=find_packages(),

    install_requires=[
        'nap'
    ],
    dependency_links=[
        #'git+ssh://git@github.com/virtusize/nap.git@0.1.0#egg=nap-0.1.0'
        'git+ssh://git@github.com/virtusize/nap.git@develop#egg=nap'
    ]
)

