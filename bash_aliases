alias ..="cd .."
alias ...="cd ../.."

alias python="python3"
alias binja="/home/brad/Programs/Binja_x86/binaryninja"
alias cya="shutdown -f now"
alias hack="cmatrix -bs"
alias update="sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y && sudo apt autoclean -y"
alias sl="clear;echo \"Fucking moron...\" | cowsay -f tux.cow | lolcat; ls | lolcat"
alias sls="ls | cowsay -f duck | lolcat"
alias autorecon="python3 /home/brad/Programs/AutoRecon/autorecon.py"

alias ipa="ip -4 addr | grep -oP 'inet \K\w+.\w+.\w+.\w+.' | grep -v '127.0.0.1' | cowsay -f bud-frogs | lolcat"
alias serve="ip -4 addr | grep -oP 'inet \K\w+.\w+.\w+.\w+' | grep -v '127.0.0.1' | cowsay | lolcat; echo 'You should probably also turn off your firewall!' | lolcat; python3 -m http.server 8080"

