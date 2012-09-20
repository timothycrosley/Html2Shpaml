#!/usr/bin/env python

from distutils.core import setup

setup(name='Html2Shpaml',
      version='0.1',
      description='A forgiving html to shpaml converter.',
      author='Timothy Crosley',
      author_email='timothy.crosley@gmail.com',
      url='http://www.simpleinnovation.org/',
      download_url='https://github.com/timothycrosley/CleanHTML/blob/master/dist/Html2Shpaml-0.1.tar.gz?raw=true',
      license = "GNU GPLv2",
      scripts=['scripts/html2Shpaml',],
      requires = ['webelements',],)
