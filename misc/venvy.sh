#!/usr/bin/bash

# This script pairs like a glass of Gentleman Jack and a Cohiba Nicaraguan cigar - it's perfect together:
# alias von="source venvy on"
# alias voff="source venvy off"

if [ $# -eq 0 ]; then
    echo "Well... do you want your env ON or OFF?"
else
    if [ $1 == "on" ]; then
        if ! [[ $(ls) == *"venvy"* ]]; then
            python3 -m venv venvy
	    . venvy/bin/activate
        else
            . venvy/bin/activate
        fi
    else
        if [ $1 == "off" ]; then
            deactivate
        else
            echo "Invalid input"
        fi
    fi
fi
