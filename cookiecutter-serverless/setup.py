from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='ccookiecutter-serverless',
    packages=['cookiecutter_serverless'],
    version='0.0.1',
    description='Cookiecutter sample for sls development with python3',
    author='Connor Bray',
    author_email='connor.bray@icloud.co.uk',
    url='https://github.com/concon121/cookiecutter-serverless',
    download_url='https://github.com/concon121/cookiecutter-serverless.git',
    keywords=['sls', 'python3'],
    classifiers=[],
    install_requires=required
)
