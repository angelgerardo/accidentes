#!/usr/bin/env python
from setuptools import setup
import os


with open("./eventos/__version__.py") as version_file:
    version = version_file.read().split("\"")[1]
	
with open("./WazeNotification/__version__.py") as version_file:
    version = version_file.read().split("\"")[1]

def read(fname):
    try:
        with open(os.path.join(os.path.dirname(__file__), fname)) as f:
            return f.read()
    except IOError:
        return ""


setup(
    name = 'eventos',
    version = version,
    author = 'Angel Martínez',
    author_email = 'angelgerardo@gmail.com',
    description = "Events with waze api.",
    url = 'https://github.com/angelgerardo/eventos',
    download_url="https://github.com/angelgerrdo/eventos/tarball/" + version,
    license = 'GNU GPL v3',
    keywords = ['waze', 'events', 'record'],
    packages = ['eventos'],
    long_description = read('readme.md')
)
