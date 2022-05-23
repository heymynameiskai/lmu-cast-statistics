#!/bin/sh

# install dependencies for pyenv and pyenv itself
echo 'Installing pyenv and dependencies...'
brew install openssl readline sqlite3 xz zlib
brew update
brew install pyenv

# add pyenv to $PATH file of your shell
echo 'Adding pyenv to PATH-file...'
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# restart current shell
exec "$SHELL"
