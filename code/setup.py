"""
Build and install the package.
"""
from setuptools import setup, find_packages
from Cython.Build import cythonize
import numpy

NAME = 'tesseroid_density'
FULLNAME = NAME
AUTHOR = "Santiago Soler"
AUTHOR_EMAIL = 'santiago.r.soler@gmail.com'
LICENSE = "BSD License"
URL = "https://github.com/pinga-lab/tesseroid-density"
DESCRIPTION = ""
KEYWORDS = ''
LONG_DESCRIPTION = DESCRIPTION

VERSION = '0.1'

PACKAGES = find_packages(exclude=['tests', 'notebooks'])
SCRIPTS = []

# Prevent possible "numpy/arrayobject.h not found" error
INCLUDE_DIRS = [numpy.get_include()]

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Science/Research",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Topic :: Scientific/Engineering",
    "Topic :: Software Development :: Libraries",
    "Programming Language :: Python :: 2.7",
    # "Programming Language :: Python :: 3.5",
    # "Programming Language :: Python :: 3.6",
    "License :: OSI Approved :: {}".format(LICENSE),
]
PLATFORMS = "Any"
INSTALL_REQUIRES = [
]

if __name__ == '__main__':
    setup(name=NAME,
          fullname=FULLNAME,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          version=VERSION,
          author=AUTHOR,
          author_email=AUTHOR_EMAIL,
          license=LICENSE,
          url=URL,
          platforms=PLATFORMS,
          scripts=SCRIPTS,
          packages=PACKAGES,
          classifiers=CLASSIFIERS,
          keywords=KEYWORDS,
          install_requires=INSTALL_REQUIRES,
          include_dirs=INCLUDE_DIRS,
          ext_modules=cythonize("tesseroid_density/_tesseroid.pyx"))
