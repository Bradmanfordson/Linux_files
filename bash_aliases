alias ..="cd .."
alias ...="cd ../.."
alias python="python3"
alias cya="shutdown -f now"
alias hack="cmatrix -bs"
alias sl="clear;echo \"Fucking moron...\" | cowsay -f tux.cow | lolcat; ls | lolcat"

alias serve="ip -4 addr | grep -oP 'inet \K\w+.\w+.\w+.\w+' | grep -v '127.0.0.1' | cowsay | lolcat; echo 'You should probably also turn off your firewall!' | lolcat; python3 -m http.server 8080"

