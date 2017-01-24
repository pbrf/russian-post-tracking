from setuptools import setup, find_packages

setup(
    name='russian-post-tracking',
    version='1.0.2',
    packages=find_packages(),
    author='Dmitry Kalinin',
    author_email='vladimirovich@pbrf.ru',
    install_requires=[
        'suds',
    ],
    url='https://github.com/pbrf/russian-post-tracking',
)
