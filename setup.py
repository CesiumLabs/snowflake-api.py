from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

VERSION = '1.0.3'

setup(
    name="snowflakeapi",
    version=VERSION,
    author="DevSynth",
    author_email="<synth@snowflakedev.org>",
    description='Easy API wrapper for https://api.snowflakedev.org/',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[],
    keywords=['snowflakedev', 'api-wrapper', 'snowflake-api'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)