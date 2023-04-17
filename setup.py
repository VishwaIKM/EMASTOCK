# ** Project Setup Manage the Version of Application and Other details**

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    License = f.read()

setup(
    name='back_test_project',
    version='1.0.0.0',
    description='This Project will present the analysis for stock Market historical data',
    long_description=readme,
    author='IKM',
    author_email='vishwasinghikm@outlook.com',
    url='ProjectGitServerPath',  # will add when a git repo create in Server
    license=License,
    packages=find_packages(exclude='tests_package')
)
