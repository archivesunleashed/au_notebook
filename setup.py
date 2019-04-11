from setuptools import setup

description = \
    """
    This module is intended for use with Archives Unleashed Cloud
    derivative data and the Archives Unleashed Cloud notebooks.
    For more information, please visit https://archivesunleashed.org/.
    """

setup(
    name = 'au_notebook',
    version = '0.0.1',
    url = 'https://github.com/archivesunleashed/au_notebook',
    install_requires=['matplotlib', 'networkx', 'nltk', 'numpy', 'pandas', ],
    author = 'Ryan Deschamps, Nick Ruest',
    author_email = 'mjordan@sfu.ca, ruestn@gmail.com',
    license = 'Apache 2.0',
    py_modules = ['au_notebook'],
    scripts = ['au_notebook.py'],
    description = description,
    long_description = open('README.md').read(),
    package_data = { '': ['README.md'] },
    platforms = ['POSIX'],
    test_suite = 'test',
    classifiers = [
      'License :: Apache 2.0',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'Topic :: Utilities',
      'Programming Language :: Python :: 3.7',
    ],
)
