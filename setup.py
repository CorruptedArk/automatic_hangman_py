#!/usr/bin/env python3

# automatic_hangman_py is a program designed to play hangman better than any human and allow a human to play as well
#   Copyright (C) 2020  Noah Stanford <noahstandingford@gmail.com>

#   automatic_hangman_py is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   automatic_hangman_py is distributed in the hope that it will be interesting and fun,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""This module handles installation, packaging, and running of the automatic_hangman_py package"""
import os
import subprocess
from setuptools import setup
from setuptools import find_packages
from automatichangman.__main__ import get_version
# Set a reasonable umask.
os.umask(0o022)
# Make all local files readable and all directories listable.
subprocess.call(['chmod', '-R', 'a+rX', '.'])

setup(name='automatichangman',
      version=get_version(),
      description="A program designed to play hangman better than any human and allow a human to play as well",
      url="https://github.com/CorruptedArk/automatic_hangman_py",
      author='CorruptedArk',
      author_email='noahstandingford@gmail.com',
      license='GPLv3',
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.8',
          'Development Status :: 5 - Production/Stable',
          'Topic :: Game'
      ],
      packages=find_packages(),
      entry_points={'console_scripts': ['automatichangman = automatichangman.__main__:main']},
      zip_safe=False,
      platforms='any',
      package_data={'': ['*.txt']},
      include_package_data=True)
