from setuptools import setup, find_packages
import os

version = '0.1'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='ploneintranet.notifications',
      version=version,
      description="A package to provide a notifications backend",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Programming Language :: Python",
      ],
      keywords='plone intranet notifications',
      author='Plone Intranet Consortium',
      author_email='ploneintranet@netsight.co.uk',
      url='https://github.com/ploneintranet/ploneintranet.notifications',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['ploneintranet'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'test': [
              'plone.app.testing',
              'plone.browserlayer',
              'unittest2',
          ],
      },
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
