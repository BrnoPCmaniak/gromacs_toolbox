# -*- coding: utf-8 -*-

'''
Created on 13. 12. 2015

@author: Tomas Dobrovolny
'''

from setuptools import setup
from gromacs_toolbox import __version__
import os
import io

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

setup(
    name='gromacs_toolbox',
    version=__version__,
    platforms=['OS Independent'],
    description='Toolbox for gromacs.',
    # long_description=read('README.txt', 'CHANGES.txt'),
    keywords='gromacs tools',
    url='https://github.com/BrnoPCmaniak/gromacs_toolbox',
    author='Filip Dobrovolny',
    author_email='brnopcman@gmail.com',
    license='MIT',
    maintainer='Filip Dobrovolny',
    maintainer_email='brnopcman@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: Utilities',
    ],
    packages=['gromacs_toolbox'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    ],
)
