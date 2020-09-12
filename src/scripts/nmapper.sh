#!/bin/bash

if [ $# -lt 2 ]; then
	echo "Usage: $0 <ipaddress> <outfile>"
	exit 1
fi

TARGET=$1
OUTFILE=$2

nmap -Pn -F $1 -o $2.fast
nmap -Pn -sV -sC $1 -o $2.sVsC
nmap -Pn -p- --max-retries 1 $1 -o $2.all
nmap -Pn -sV -sC -p $(get_ports $2.all) $1 -o $2.sVsC.allports

echo "Done."
