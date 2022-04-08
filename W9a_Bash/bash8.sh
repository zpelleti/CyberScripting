#!/usr/bin/bash


 # to search emp.lst for "director": 

read -p "Enter...:" pattern
echo -e "\n\n"

declare -i count=0

 while IFS= read -r line;
           
 do
  #   if [[ "$line" == *"sales"* ]];
       if [[ "$line" =~ "$pattern" ]];
     then
 echo $line
 count+=1
     fi
  done < emp.lst
   
  echo "num rows" $count
  

   # get the search pattern from user input with the read command like you did the file name, and then

   # you can call grep "$pattern" "$filename" to search within the file.
  