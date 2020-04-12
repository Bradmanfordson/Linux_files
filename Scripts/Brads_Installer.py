
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

whoami = os.popen("whoami").read().strip()


def header(message: str): 
    print()
    print("#" * (4+ len(message)))
    print("# {} #".format(message))
    print("#" * (4 + len(message)))


def initial_update():
    header("Setting up ~/Programs directory.")
    os.mkdir("/home/{}/Programs".format(whoami))
    os.mkdir("/home/{}/Programs/Scripts".format(whoami))

    header("Updating")
    os.system("sudo apt update")

    header("Upgrading")
    os.system("sudo apt upgrade")
    
    header("Setting up ~/Programs/Scripts/update.py for Aliases.")
    os.system("mv update.py /home/{}/Programs/Scripts/".format(whoami))


def install_applications():
    with open("programs.json", "r") as json_file:
        data = json.load(json_file)

        for apt in data.get("apt"):
            header("APT {}".format(apt))
            os.system("sudo apt install {} -y".format(apt))

        for snap in data.get("snap"):
            header("SNAP {}".format(snap))
            os.system("sudo snap install {} --classic".format(snap))

    msf = input("Want Metasploit (Y/n): ")
    if msf.lower == "y":
        header("Installing Metasploit")
        os.system("""
        curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
        chmod 755 msfinstall
        ./msfinstall
        rm msfinstall
        """)


def aliases():
    header("Setting up aliases")
    os.system("cp ../bash_aliases /home/{}/.bash_aliases".format(whoami))


def git_setup():
    header("Git setup")
    username = input("Enter your GitHub username: ")
    email = input("Enter your email address: ")

    os.system('git config --global user.name "{}"'.format(username))
    os.system('git config --global user.email "{}"'.format(email))

    header("Generating ssh key for GitHub")
    os.system('ssh-keygen -t rsa -b 4098 -C "{}"'.format(email))
    os.system("eval $(ssh-agent 0s)")
    os.system("ssh-add")
    print("Copy the contents of ~/.ssh/id_rsa.pub and add it to GitHub. This is your SSH Key")



if __name__ == "__main__":
    initial_update()
    install_applications()
    aliases()
    git_setup()
