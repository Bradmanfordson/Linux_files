#!/bin/bash

# This needs work... but putting it here so I don't lose it.

if [ $# -lt 1 ]; then
	echo "Usage: $0 <file>"
	exit 1
fi

FILE=$1
grep "open" $1 | cut -d"/" -f1 | paste -sd,
