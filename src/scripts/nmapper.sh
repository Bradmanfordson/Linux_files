#!/bin/bash

if [ $# -lt 2 ]; then
        echo "Usage: $0 <ipaddress> <outfile>"
        exit 1
fi

TARGET=$1
OUTFILE=$2
echo "####################"
echo "# ----- FAST ----- #"
echo "####################"
nmap -Pn -F $1 -o $2.fast

echo "#####################"
echo "# ----- NORMAL -----#"
echo "#####################"
nmap -Pn $1 -o $2.normal

echo "###################"
echo "# ----- ALL ----- #"
echo "###################"
nmap -Pn -p- --max-retries 1 $1 -o $2.all

echo "#######################"
echo "# ----- ALL sVsC -----#"
echo "#######################"
nmap -Pn -sV -sC -p $(get_ports $2.all) $1 -oA $2.sVsC.allports

echo "Done."
