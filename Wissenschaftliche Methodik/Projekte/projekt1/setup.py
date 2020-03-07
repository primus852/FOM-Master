from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='wm_p1',
    version='0.1.0',
    description='Projekt 1 - Wissenschaftliche MEthodik',
    long_description=readme,
    author='Torsten Wolter',
    author_email='tow.berlin@gmail.com',
    url='https://github.com/primus852/FOM-Master',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)