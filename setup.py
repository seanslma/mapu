import os
import sys
from setuptools import setup

# include versioneer.py path if build env does not install versioneer
sys.path.append(os.path.dirname(__file__))
import versioneer

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)
