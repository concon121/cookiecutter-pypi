from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    include_package_data=True,
    name='{{cookiecutter.project_slug}}',
    packages=['{{cookiecutter.project_slug}}'],
    version='{{cookiecutter.version}}',
    description='{{cookiecutter.project_short_description}}',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    install_requires=required
)
