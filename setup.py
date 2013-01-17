#!/usr/bin/env python

from distutils.core import setup

setup(name='Html2Shpaml',
      version='0.2.0',
      description='A forgiving html to shpaml converter.',
      author='Timothy Crosley',
      author_email='timothy.crosley@gmail.com',
      url='http://www.simpleinnovation.org/',
      download_url='https://github.com/timothycrosley/Html2Shpaml/blob/master/dist/Html2Shpaml-0.2.0.tar.gz?raw=true',
      license = "GNU GPLv2",
      scripts=['scripts/html2Shpaml',],
      install_requires=['webelements>=1.0.0-alpha.1',],)
