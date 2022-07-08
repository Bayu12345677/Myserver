 #!/usr/bin/env python
 # -*- coding: utf-8 -*-

from cmath import pi
from setuptools import setup, find_packages
from setuptools.command.install import install
from distutils.command.install import INSTALL_SCHEMES
from distutils.core import Command
from distutils.command.build_py import build_py
from distutils.command.install_scripts import install_scripts
from distutils.command.install_data import install_data
from distutils.command.install_lib import install_lib

Install = ['flask', 'flask-cors']
setup(
    name='My server',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=Install,
    scripts=['server.py'],
    author='Bayu Rizky A.M',
    author_email='bayuriski558@gmail.com',
    description='My server',
    keywords='SERVER HOME',
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: CGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Static',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Dynamic',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Dynamic',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Static',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Dynamic :: CGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Dynamic :: PHP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Dynamic :: Perl',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Dynamic :: Python',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Dynamic :: Ruby',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Dynamic :: Swift',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Static :: Apache',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Static :: Apache :: mod_wsgi',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Static :: Apache :: mod_wsgi :: mod_wsgi',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Static :: Apache :: mod_wsgi :: mod_wsgi :: mod_wsgi',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Static :: Apache :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Static :: Apache :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Static :: Apache :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Static :: Apache :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Static :: Apache :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Static :: Apache :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Static :: Apache :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Static :: Apache :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Static :: Apache :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Static :: Apache :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Static :: Apache :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Static :: Apache :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Static :: Apache :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Static :: Apache :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Static :: Apache :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Static :: Apache :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application :: Web :: Static :: Apache :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi :: mod_wsgi',
    ]
)
# This field adds keywords for your project which will appear on the
# project page. What does your project relate to?
#
# Note that this is a string of words separated by whitespace, not a list.
keywords='web wsgi apache mod_wsgi',  # Optional