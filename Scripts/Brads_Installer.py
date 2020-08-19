import os
import json


whoami = os.popen("whoami").read().strip()

def header(message: str): 
    print()
    print("#" * (4+ len(message)))
    print(f"# {message} #")
    print("#" * (4 + len(message)))


def initial_update():
    header("Updating")
    os.system("sudo apt update")

    header("Upgrading")
    os.system("sudo apt upgrade")

def setup():
    os.system(f'PATH="/home/{whoami}/.local/bin:$PATH')

    with open(f"/home/{whoami}/.bashrc", "a") as bashrc:
        bashrc.write(rc)

    with open("setup.json", "r") as json_file:
        data = json.load(json_file)

        header("Setting up directories")
        for directory in directories.get("directories"):
            header(f"Creating {directory}")
            os.mkdir(f"/home/{whoami}/{directory}")

        header("Installing Programs")
        for apt in data.get("apt"):
            header(f"APT {apt}")
            os.system(f"sudo apt install {apt} -y")

        for snap in data.get("snap"):
            header(f"SNAP {snap}")
            os.system(f"sudo snap install {snap} --classic")


def hakr_toolz():
    header("Installing Metasploit")
    os.system("""
    curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
    chmod 755 msfinstall
    ./msfinstall
    rm msfinstall
    """)

    header("Installing Searchsploit")
    os.system("sudo git clone https://github.com/offensive-security/exploitdb.git /opt/exploit-database")
    os.system("sudo ln -sf /opt/exploit-database/searchsploit /usr/local/bin/searchsploit")
    os.system("cp -n /opt/exploit-database/.searchsploit_rc ~/")

    header("Installing SecLists")
    os.system(f"sudo git clone https://github.com/danielmiessler/SecLists.git /home/{whoami}/Tools/SecLists")


def aliases():
    header("Setting up aliases")
    os.system(f"cp ../bash_aliases /home/{whoami}/.bash_aliases")


def git_setup():
    header("Git setup")
    username = input("Enter your GitHub username: ")
    email = input("Enter your email address: ")

    os.system(f'git config --global user.name "{email}"')
    os.system(f'git config --global user.email "{username}"')

    header("Generating ssh key for GitHub")
    os.system(f'ssh-keygen -t rsa -b 4098 -C "{email}"')
    os.system("eval $(ssh-agent -s)")
    os.system("ssh-add")
    print("Copy the contents of ~/.ssh/id_rsa.pub and add it to GitHub. This is your SSH Key")


if __name__ == "__main__":
    if whoami is "root":
        print("Don't run this as root.")
        exit(1)
    initial_update()
    setup()
    aliases()
    git_setup()
    hakr_toolz()
    header("Finished")

