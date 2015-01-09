#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pyfuzzy_toolbox',
    version='0.1.0',
    description='This project aims to provide matlab fuzzy toolbox f functionalities in python',
    long_description=readme + '\n\n' + history,
    author='Matheus Cardoso',
    author_email='matheus.mcas@gmail.com',
    url='https://github.com/matheuscas/pyfuzzy_toolbox',
    packages=[
        'pyfuzzy_toolbox',
    ],
    package_dir={'pyfuzzy_toolbox':
                 'pyfuzzy_toolbox'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='pyfuzzy_toolbox',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
