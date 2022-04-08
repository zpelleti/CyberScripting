#!/usr/bin/bash

mess="Executing second Bash..."

version="Bash2"
numeric=10

printf "%20s version %5s %-1d\n" "$mess" "$version" $numeric

echo "==================="

echo -e "\nCalling external1...."
./external1.sh

