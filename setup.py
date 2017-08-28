from setuptools import find_packages
from setuptools import setup

setup(
    name="dotinstall",
    packages=find_packages(exclude=['tests*']),
)
