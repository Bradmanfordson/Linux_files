#!/usr/bin/bash

RED="\e[31m"
GREEN="\e[32m"
BOLDGREEN="\e[1;32m"
ENDCOLOR="\e[0m"

print(){
    echo -e "${BOLDGREEN}>>>>>>> $1 ${ENDCOLOR}"
}

# Updating and Upgrading
print "Updating"
sudo apt upgrade

print "Upgrading"
sudo apt full-upgrade -y

# Setting up Home directory
for USER in $(ls /home); do
    print "Creating ${USER}/Projects"
    mkdir /home/${USER}/Projects

    print "Creating ${USER}/.ovpn"
    mkdir /home/${USER}/.ovpn
done

# Installing apt packages
for APT in $(cat apt.config); do
    print "Installing ${APT}.apt"
    sudo apt install $APT -y
done

# Installing snap packages
for SNAP in $(cat snap.config); do
    print "Installing ${SNAP}.snap"
    sudo snap install $SNAP --classic
done

# Installing VSCode Extensions
print "Installing VSCode Extensions"
for EXT in $(cat vscode_extensions.config); do
    echo test
    code --install-extension $EXT
done

# Installing Metasploit
print "Installing Metasploit"
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
chmod 755 msfinstall
./msfinstall
rm msfinstall

# Installing Searchsploit
print "Installing Searchsploit"
sudo git clone https://github.com/offensive-security/exploitdb.git /opt/exploit-database
sudo ln -sf /opt/exploit-database/searchsploit /usr/local/bin/searchsploit
cp -n /opt/exploit-database/.searchsploit_rc ~/

# Downloading SecLists
print "Downloading SecLists"
sudo git clone https://github.com/danielmiessler/SecLists.git /usr/share/seclists

# Add IPA
print "Adding IPA"
sudo cp ipa.py /usr/local/sbin/ipa
sudo chmod +x /usr/local/sbin/ipa
