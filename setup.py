#!/usr/bin/env python

import sys
from setuptools import setup
import pyuml2

packages = ['pyuml2',
            'pyuml2.uml',
            'pyuml2.types']


if sys.version_info < (3, 3):
    required_packages = ['pyecore-py2']
else:
    required_packages = ['pyecore']


setup(
    name='pyuml2',
    version=pyuml2.__version__,
    description=('A Python(ic) implementation of the UML2 metamodel'),
    long_description=open('README.rst').read(),
    keywords='model metamodel MDE UML',
    url='https://github.com/pyecore/pyuml2',
    author='Vincent Aranega',
    author_email='vincent.aranega@gmail.com',

    packages=packages,
    package_data={'': ['README.rst', 'LICENSE', 'CHANGELOG.rst']},
    include_package_data=True,
    install_requires=required_packages,
    tests_require=['pytest'],
    license='BSD 3-Clause',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: BSD License',
    ]
)
