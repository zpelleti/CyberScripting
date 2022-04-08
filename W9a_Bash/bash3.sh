#!/usr/bin/bash

while [[ $reply != 3 ]]             # watch spaces!!!
do
    echo "1) Write to file"
    echo "2) Read from file"
    echo "3) exit"
    
    read -p "Pick [1-3]" reply          # accepts user in
    
    #case = 'switch'
    case $reply in                      # $reply = user pick 
    
    # case 1: how to write on a file:
        1) echo -e '\nWriting the file\n'
            read -p "Filename?" fileName #nreads user in creates fileName 
                                         # NO spaces in filename.txt
            exec 3>> ${fileName}.txt    # exec = no subshell is created
                                        # exec 1 = descriptor (id) 
                                        # >> allows to append to file
                                        # > overwrites 
        #----------------------------------------------------------------------------------
            echo -e "\nProcess id (pid) of current process is $$" # has to be double quotes
            my_pid=$$                   # $$ = auto-generated process id
            echo "Currently following files are opened by $0 script: "
            ls -l /proc/$my_pid/fd      # fd = file descriptor
                                        # standard input (0) , display (1) , error (2) 
        #----------------------------------------------------------------------------------
            read -p "Enter your text:" text # saves text
            echo $text >&3              # writes on file 1
            date >&3                    # adds the date on file 1
            exec 3<&-                   # to close file 1
            
            ;;
        
        2) echo -e "\nReading from file\n"
            read -p "Filename?" fileName
            
            if [[ -f $fileName ]]
            then
                exec 3< ${fileName}   # < = from , > = to
                while IFS= read -r line # IFS = field separator
                do 
                    echo "$line"
                done < "$fileName"      # echo line (print line) 
                                        # done filename = from ...
                exec 3<&-           # close file
            else 
                echo "$fileName - doesn't exist"
            fi                  # fi = closes if statement
            ;;                  # ;; closes case statement
        
        3)  echo -e "\nGoodbye!"
            exit 2
        ;;
        4) echo -e "\nNo Idea"
    
    esac
done

