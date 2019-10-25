#!/bin/bash

# Apt packages
sudo apt install nmap gdb curl vim nikto docker.io john python3 libreoffice git virtualbox lolcat cowsay -y 

# Snap packages
sudo snap install insomnia --classic -y

# Metasploit
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
chmod 755 msfinstall
./msfinstall
rm msfinstall

# Python Exploit Development Addon for GDB
git clone https://github.com/longld/peda.git ~/peda
echo "source ~/peda/peda.py" >> ~/.gdbinit
echo "Peda - done."



