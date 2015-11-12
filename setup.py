import os, shutil
from setuptools import setup, find_packages

if not os.path.exists('build/_scripts'):
    os.makedirs('build/_scripts')
shutil.copyfile('main', 'build/_scripts/fpl_reader')

setup(name='fpl_reader',
    url='https://github.com/rr-/fpl_reader',
    version='1.0',
    packages=find_packages(),
    test_suite='tests',
    scripts=['build/_scripts/fpl_reader'])
