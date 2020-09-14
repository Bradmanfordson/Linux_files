#!/usr/bin/python3

import os, json, getpass

whoami = getpass.getuser()
home = f"/home/{whoami}"


def header(message: str): 
    print()
    print("#" * (4 + len(message)))
    print(f"# {message} #")
    print("#" * (4 + len(message)))


def initial_update():
    header("Updating")
    os.system("sudo apt update")

    header("Upgrading")
    os.system("sudo apt upgrade -y")

    
def setup():
    os.system(f"echo \"PATH={home}/.local/bin:$PATH\" >> {home}/.bashrc")

    with open("settings.json", "r") as json_file:
        data = json.load(json_file)

        header("Setting up directories")
        for directory in data.get("directories"):
            try:
                header(f"Creating {directory}")
                os.mkdir(f"{home}/{directory} -p")
            except Exception as e:
                print(f"Skipping {directory} because it already exists.")

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

    header("Downloading SecLists")
    os.system(f"sudo git clone https://github.com/danielmiessler/SecLists.git {home}/Tools/SecLists")
    
    header("Downloading and Installing Joplin")
    os.system("wget -O - https://raw.githubusercontent.com/laurent22/joplin/master/Joplin_install_and_update.sh | bash")


def add_scripts():
    header("Setting up aliases")
    os.system(f"cp bash_aliases.txt {home}/.bash_aliases")
    
    header("Setting up IPA")
    os.system(f"cp scripts/ipa.py {home}/.local/bin/ipa")
    os.system(f"chmod +x {home}/.local/bin/ipa")

    
def git_setup():
    header("Git setup")
    username = input("Enter your GitHub username: ")
    email = input("Enter your email address: ")

    os.system(f'git config --global user.name "{username}"')
    os.system(f'git config --global user.email "{email}"')

    header("Generating ssh key for GitHub")
    os.system(f'ssh-keygen -t rsa -b 4098 -C "{email}"')
    os.system("eval $(ssh-agent -s)")
    os.system("ssh-add")
    print("Copy the contents of ~/.ssh/id_rsa.pub and add it to GitHub. This is your SSH Key")


if __name__ == "__main__":
    if whoami == "root":
        header("Don't run this as root.")
        exit(1)
        
    initial_update()
    setup()
    add_scripts()
    
    ans = input("Do you need to set up git? (Y/n): ")
    if ans.lower()[0] == "y":
        git_setup()
        
    hakr_toolz()
    os.system("sudo updatedb")
    header("Finished")
