# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in pharmacy/__init__.py
from pharmacy import __version__ as version

setup(
	name='pharmacy',
	version=version,
	description='A custom app to manage inventory and billing system for pharmacy',
	author='crio',
	author_email='criogroups@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
