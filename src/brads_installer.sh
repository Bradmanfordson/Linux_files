#!/usr/bin/bash

RED="\e[31m"
GREEN="\e[32m"
BOLDGREEN="\e[1;32m"
ENDCOLOR="\e[0m"

USER=$(whoami)

print(){
    echo -e "${BOLDGREEN}>>>>>>> $1 ${ENDCOLOR}"
}

print "Updating"
sudo apt upgrade

print "Upgrading"
sudo apt full-upgrade -y

for APT in $(cat apt.config); do
    print "Installing ${APT}.apt"
    sudo apt install $APT -y
done

for SNAP in $(cat snap.config); do
    print "Installing ${SNAP}.snap"
    sudo snap install $SNAP --classic
done

print "Installing VSCode Extensions"
for EXT in $(cat vscode_extensions.config); do
    echo test
    code --install-extension $EXT
done

print "Creating $USER/Projects"
mkdir /home/$USER/Projects

print "Creating $USER/.ovpn"
mkdir /home/$USER/.ovpn

print "Setting up zsh"
sudo chsh --shell /bin/zsh $USER
sudo chsh --shell /bin/zsh 
sudo cp ../misc/zshrc.sh /home/$USER/.zshrc
sudo cp ../misc/zsh_aliases.sh /home/$USER/.zsh_aliases

print "Add IPA"
print "Adding IPA"
sudo cp ../misc/ipa.py /usr/local/sbin/ipa
sudo chmod +x /usr/local/sbin/ipa

print "Add venvy"
print "Adding venvy"
sudo cp ../misc/venvy.sh /usr/local/sbin/venvy
sudo chmod +x /usr/local/sbin/venvy

print "Install Chrome"
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
rm google-chrome-stable_current_amd64.deb

print  "Set to dark theme + set background"
cp ../misc/dark_debian.png ~/Pictures/
gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita-dark'
gsettings set org.gnome.desktop.background picture-uri file:////home/$USER/Pictures/dark_debian.png
gsettings set org.gnome.login-screen logo /home/$USER/Pictures/dark_debian.png
gsettings set org.gnome.desktop.session idle-delay 0

print "Setup dock"
gsettings set org.gnome.shell favorite-apps "['org.gnome.Terminal.desktop', 'org.gnome.Nautilus.desktop', 'google-chrome.desktop', 'code_code.desktop']"
gsettings set org.gnome.shell.extensions.dash-to-dock dock-position BOTTOM
gsettings set org.gnome.shell.extensions.dash-to-dock dash-max-icon-size 16
gsettings set org.gnome.shell.extensions.dash-to-dock extend-height false

# Hacker Tools
# ------------
# # Installing Metasploit
# print "Installing Metasploit"
# curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
# chmod 755 msfinstall
# ./msfinstall
# rm msfinstall

# # Installing Searchsploit
# print "Installing Searchsploit"
# sudo git clone https://github.com/offensive-security/exploitdb.git /opt/exploit-database
# sudo ln -sf /opt/exploit-database/searchsploit /usr/local/bin/searchsploit
# cp -n /opt/exploit-database/.searchsploit_rc ~/

# # Downloading SecLists
# print "Downloading SecLists"
# sudo git clone https://github.com/danielmiessler/SecLists.git /usr/share/seclists