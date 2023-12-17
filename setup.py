from setuptools import setup
from setuptools import find_packages

setup(
    name='spotifish_graphics',
    version='0.1',
    description='Package for creating the graphics of spotifish',
    author='Segel',
    packages=find_packages(),
    install_requires=[
        'pyqt5'
    ],
)
