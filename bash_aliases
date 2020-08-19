alias ..="cd .."
alias ...="cd ../.."

alias gadd="git add"
alias gcom="git commit -m"
alias gstat="git status"

alias python="python3"
alias hak="cmatrix -bs"
alias sl="clear;echo \"You moron...\" | cowsay -f tux.cow | lolcat; ls | lolcat"

alias update="sudo apt update && sudo apt full-upgrade -y && sudo apt autoclean -y && sudo apt autoremove -y"

alias ipa="ip -4 addr | grep -oP 'inet \K\w+.\w+.\w+.\w+.' | grep -v '127.0.0.1' | cowsay -f bud-frogs | lolcat"
