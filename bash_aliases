alias ..="cd .."
alias ...="cd ../.."

alias python="python3"
alias cya="shutdown -f now"
alias hack="cmatrix -bs"
alias update="sudo /bin/bash /home/brad/Programs/Scripts/update.sh"
alias sl="clear;echo \"You moron...\" | cowsay -f tux.cow | lolcat; ls | lolcat"

alias ipa="ip -4 addr | grep -oP 'inet \K\w+.\w+.\w+.\w+.' | grep -v '127.0.0.1' | cowsay -f bud-frogs | lolcat"

alias serve="ip -4 addr | grep -oP 'inet \K\w+.\w+.\w+.\w+' | grep -v '127.0.0.1' | cowsay | lolcat; echo 'You should probably also turn off your firewall!' | lolcat; python3 -m http.server 8080"

# Template for making more complex aliases
# alias <name>="sudo /bin/bash <path_to_your_bash_script>"
