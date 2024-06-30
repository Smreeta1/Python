from setuptools import setup, find_packages #  find_packages:find and list all python packages __init__.py files

setup(
    name="Demo project",
    author="Smreeta",
    version="1.0",
    packages=find_packages(),
    install_requires=[],  #no external dependencies currently
    description="A demo project to show setuptools usage",
    
)