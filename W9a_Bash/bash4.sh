#!/bin/bash

myString="Ubuntu;Linux mint;Debian;Arch;Fedora"

# to take the var myString and transform it in an array called myArray
# so that we can separate it with ';' and print only chosen values by index:
IFS=';'
read -ra myArray <<< "$myString"        # -a stores words in file to be separated in
                                        # an array - index starts at 0
                                        # -r causes 'read' to interpret symbols '\' litterally
                                        # no escape char.
                                        # <<< means: 
                                        # myArray = destination, myString = source
echo "Number of entries: using [@]: ${#myArray[@]}"  # '#' prints count of  
echo "Number of entries: using [*]: ${#myArray[*]}"  # without '#' prints array elements

echo -e "==============\n"

# now to print the whole array with @ or * :
for i in "${myArray[@]}"
do  
    echo $i
done

echo -e "==============\n"

for i in "${myArray[*]}"
do  
    echo $i
done

