#!/usr/bin/env python
import os
from setuptools import setup


def run_setup():
    setup(
        name='writing_style',
        version='0.0.2',
        description='Analyze text',
        keywords = '',
        url='https://github.com/sergeio/writing_style',
        author='Sergei Orlov',
        author_email='pypi@sergeiorlov.com',
        license='BSD',
        packages=['writing_style'],
        install_requires=[''],
        test_suite='tests',
        long_description='',
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: POSIX',
            'Programming Language :: Python',
        ],
    )

if __name__ == '__main__':
    run_setup()
