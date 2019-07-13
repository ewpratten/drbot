from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='drbot',
    version='1.0',
    packages=['drbot'], 
    install_requires = ["requests"],
    description='A Python3 library for easily building devRant bots',
    url='https://github.com/Ewpratten/drbot',
    author='Evan Pratten',
    author_email='ewpratten@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
    )
    )