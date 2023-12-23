import codecs
import os
from setuptools import setup, find_packages
import loggerjava

# these things are needed for the README.md show on pypi
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


VERSION = loggerjava.ver
DESCRIPTION = 'an easy logger outputs like java logs '
LONG_DESCRIPTION = 'an easy logger outputs like java logs '

# Setting up
setup(
    name="loggerjava",
    version=VERSION,
    author="HTony03",
    author_email="HTony03@foxmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python','logger'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)