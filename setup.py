# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 <ahref Foundation -- All rights reserved.
# Author: Daniele Pizzolli <daniele@ahref.eu>
#
# This file is part of the identity manager project.
#
# This file can not be copied and/or distributed without the express
# permission of <ahref Foundation.
#
###############################################################################


from setuptools import setup

with open('requirements/base.txt') as f:
    requirements_base = f.read().splitlines()

with open('requirements/test.txt') as f:
    requirements_test = f.read().splitlines()

setup(
    name='IdentityManager',
    version=open('version.txt').read().strip(),
    author='Daniele Pizzolli',
    author_email='daniele@ahref.eu',
    packages=['IdentityManager', 'IdentityManager.test'],
    # namespace_packages=['IdentityManager'],
    keywords='identity manager',
    url='http://gitlab.ahref.eu/misc/identity manager.git',
    license='Proprietary License',
    long_description=open('README.rst').read(),
    description=('identity manager is a backend service for user managment'),
    entry_points='''
        [console_scripts]
        im = IdentityManager.manage:main
        ''',
    # To skip problems of local eggs we make fat requirements:
    # http://stackoverflow.com/questions/1843424/setup-py-test-egg-install-location  # NOQA
    install_requires=requirements_base + requirements_test,
    include_package_data=True,
    test_suite='nose.collector',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
