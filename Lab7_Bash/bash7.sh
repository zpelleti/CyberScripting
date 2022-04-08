#!/usr/bin/bash


while [[ $reply != 2 ]]            
do
   
    echo "1) Read from file"
    echo "2) exit"
    
    read -r -p "Pick [1-2]" userIn           
    
    #case = 'switch'
    case $userIn in                      # $reply = user pick 

        1) echo -e "\nReading from file\n"
            read -r -p "Search File?" fileName
            read -r -p "Enter Keyword: " keywd
            
            if [[ -f $fileName ]]
            then
                if result=$(grep -w "$keywd" $fileName)
                then
                    echo -e "\n$result\n" 
                    
                    echo "Line count: " 
                    grep $keywd $fileName | wc -l
                    
                else
                    echo -e "\n$keywd not found in $fileName\n"
                fi
                # echo Total lines: 
            else
                echo "$fileName - doesn't exist"
            fi                  
            ;;                 
        
        2)  echo -e "\nGoodbye!"
            exit 0  
        # add an exit()
        ;;
        
    
    esac
done


   
    

    
    


