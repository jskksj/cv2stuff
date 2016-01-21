#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='cv2stuff',
    version='0.1.0',
    description="Command line scripts in Python Click",
    long_description=readme + '\n\n' + history,
    author="John Krumpotick",
    author_email='github@simplexapparati.com',
    url='https://github.com/jskksj/cv2stuff',
    packages=[
        'cv2stuff',
    ],
    package_dir={'cv2stuff':
                 'cv2stuff'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='cv2stuff',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={'console_scripts': ['cv2stuff=cv2stuff.cv2stuff:cli'], },
    test_suite='tests',
    tests_require=test_requirements
)
