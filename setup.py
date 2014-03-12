import re
import os
from setuptools import setup, find_packages


def read_file(file_name):
    f = open(os.path.join(os.path.dirname(__file__), file_name))
    return f.read()


def get_version():
    meta_filedata = read_file('fbads/__init__.py')
    re_version = re.compile(r'VERSION\s*=\s*\((.*?)\)')
    group = re_version.search(meta_filedata).group(1)
    version = filter(None, map(lambda s: s.strip(), group.split(',')))
    return '.'.join(version)


setup(
    name='fbads',
    version=get_version(),
    description=u'Python client for the Facebook Ads API',
    long_description=read_file('README.rst'),
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='facebook ads api',
    author='Renato Pedigoni',
    author_email='renatopedigoni@gmail.com',
    url='http://fbads.readthedocs.org/en/latest/',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[d for d in read_file('requirements.txt').split('\n') if d],
)
