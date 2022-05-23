#!/bin/sh

# Install Python version
pyenv install -l
echo 'Which python version do you want to install?'
read VERSION

echo 'Running "pyenv install '$VERSION'" press enter to continue'
read
pyenv install $VERSION
pyenv local $VERSION

# Setup Virtual Environment
python -m venv .venv

# Install pip
python -m ensurepip --upgrade
