from setuptools import setup
from setuptools import find_packages

setup(
    name='amnon_graphics',
    version='0.1',
    description='Package for creating the graphics of spotifish_example.py',
    author='Segel',
    packages=find_packages(),
    install_requires=[
        'pyqt5'
    ],
)
