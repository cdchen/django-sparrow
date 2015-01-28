# -*- coding: utf-8 -*-

import os
import sys


project_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(project_dir, 'src'))

import django_sparrow

version = django_sparrow.version

install_requires = [
    'django',
]

setup_requires = [
]

dependency_links = [
]

long_description = '''
'''

from setuptools import setup, find_packages

setup(
    name='django-sparrow',
    version=version,
    description='Django Bootstrap Carousel Component',
    long_description=long_description,
    author='cdchen',
    author_email='cdchen@nicestudio.com.tw',
    url='https://github.com/cdchen/django-bootstrap-carousel',
    download_url='https://github.com/cdchen/django-bootstrap-carousel/tarball/%s' % version,
    license='GPL License',
    packages=find_packages('src', exclude=['docs', 'tests']),
    package_dir={
        '': 'src'
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    setup_requires=setup_requires,
    dependency_links=dependency_links,
    classifiers=['Development Status :: 4 - Beta',
                 'Development Status :: 5 - Production/Stable',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Utilities'],
)
