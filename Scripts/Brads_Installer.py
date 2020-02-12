
# ###
# 1. Gather information
#     - Username (Git)
#     - email (Git)
#     - screen height/width

# 2. System Update
# 3. Application Install
# 4. Create SSH keys
# 5. create xprofile
# 6. create bash_aliases
# 7. add welcome to bashrc


# ###

import os

answer = ["y", "Y"]

apt_list = [ "nmap", "gdb", "curl", "vim", "nikto ", "docker.io", "john", "python3", "libreoffice", "git", "virtualbox", "lolcat", "cowsay", "dtrx", "radare2"]
snap_list = ["insomnia", "pycharm-community"]

alias_dict = {"..":"cd ..", 
              "...": "cd ../..",
              "update": "sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y && sudo apt autoclean -y",
              "sl":"clear;echo \"You moron...\" | cowsay -f tux.cow | lolcat; ls | lolcat",
              "sls":"ls | cowsay -f duck | lolcat",
              "autorecon":"python3 /home/brad/Programs/AutoRecon/autorecon.py",
              "ipa":"ip -4 addr | grep -oP 'inet \K\w+.\w+.\w+.\w+.' | grep -v '127.0.0.1' | cowsay -f bud-frogs | lolcat",
              "serve":"ip -4 addr | grep -oP 'inet \K\w+.\w+.\w+.\w+' | grep -v '127.0.0.1' | cowsay | lolcat; echo 'You should probably also turn off your firewall!' | lolcat; python3 -m http.server 8080",
}


def header(message: str):
    print("##########################################################################################")
    print("                                      {}".format(message))
    print("##########################################################################################")


def system_update():
    header("Updating")
    os.system("sudo apt update")

    header("Upgrading")
    os.system("sudo apt upgrade -y")

    header("Autocleaning")
    os.system("sudo apt autoclean -y")

    header("Autoremoving")
    os.system("sudo apt autoremove -y")


def install_applications():
    with open("programs.json", "r") as json_file:
        data = json.load(json_file)

        for apt in data.get("apt"):
            header("Apt {}".format(apt))
            os.system("sudo apt install {} -y".format(apt))

        for snap in data.get("snap"):
            header("Snap {}".format(snap))
            os.system("sudo snap install {} --classic".format(snap))

    msf = input("Want Metasploit (Y/n): ")
    if msf in ["y", "Y"]:
        header("Installing Metasploit")
        os.system("""
        curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
        chmod 755 msfinstall
        ./msfinstall
        rm msfinstall
        """)
    
    peda = input("Want Python Exploit Development Addon for GDB: ")
    if msf in answer:
        header("Installing Peda")
        os.system("""
        git clone https://github.com/longld/peda.git ~/peda
        echo "source ~/peda/peda.py" >> ~/.gdbinit
        """)


def create_bash_aliases():
    with open("/home/{}/.bash_aliases".format(hostname), "w") as file:
        for key, value in alias_dict.items():
            file.write("alias {}=\"{}\"\n".format(key, value))


def create_xprofile(): 
    # w = input("Screen Width (ex. 1920) : ")
    # h = input("Screen Height (ex. 1080): ")
    # TODO
    pass
   

def edit_bashrc():
    # TODO
    pass

def create_ssh_key():
    os.system("ssh-keygen -t rsa -b 4096 -C {}".format(email))
    os.system("eval $(ssh-agent -s)")
    os.system("ssh-add /home/{}/.ssh/id_rsa".format(hostname))

def set_git_global_config():
    os.system("git config --global user.name \"{}\"".format(username))
    os.system("git config --global user.email \"{}\"".format(email))


if __name__ == "__main__":
    hostname = os.popen("whoami").read().strip()
    # usename = input("What is your GitHub username: ")
    # email = input("What is your email: ")
    
    # system_update()
    # install_applications()
    create_bash_aliases()
    # create_xprofile()
    # edit_bashrc()
    # create_ssh_key()
    # set_git_global_config()
