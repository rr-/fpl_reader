import os
from setuptools import setup, find_packages


setup(
    name='fpl_reader',
    url='https://github.com/rr-/fpl_reader',
    version='1.0',
    packages=find_packages(),
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'fpl_reader = fpl_reader.__main__:main'
        ]
    })
