from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='Thesis_quer_tool_4guet',
      version=version,
      description="guet_1hz_cd_slx",
      long_description="""\
This program can also provide corresponding written interfaces for relevant use""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='guet_tools',
      author='linhuaizhou(1hz) from GUET',
      author_email='linhzz1015@163.com',
      url='https://github.com/linhuaizhou/',
      license='MIT license',
      packages=find_packages(exclude=['beautifulsoup4', 'requests', 'openpyxl','setuptools','urllib3','retrying','pdfminer3k']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
