import os
from setuptools import setup, find_packages
from fbads import __version__


def READFILE(file_name):
    f = open(os.path.join(os.path.dirname(__file__), file_name))
    return f.read()

setup(
    name='fbads',
    version=__version__,
    description=READFILE('README.rst'),
    long_description='',
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='facebook ads',
    author='Renato Pedigoni',
    author_email='renatopedigoni@gmail.com',
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[d for d in READFILE('requirements.txt').split('\n') if d],
)
