#!/usr/bin/env python3
import os
import subprocess

#install python and pyenv
#-------------------------
subprocess.run(["sudo", "dnf", "update", "-y"])
package=["epel-release","gcc","openssl-devel","bzip2-devel","libffi-devel","zlib-devel","wget","git","readline-devel","sqlite-devel","openssl-devel","python3-pip"]
for i in package:
    subprocess.run(["sudo", "dnf", "install", "-y", i])


os.system('git clone https://github.com/pyenv/pyenv.git $HOME/.pyenv')
os.system('echo "export PYENV_ROOT=\"$HOME/.pyenv\"" >> ~/.bashrc')
os.system('echo "export PATH=\"$PYENV_ROOT/bin:$PATH\"" >> ~/.bashrc')
os.system('echo "eval \"$(pyenv init -)\"" >> ~/.bashrc')
os.system('exec "$SHELL"')
