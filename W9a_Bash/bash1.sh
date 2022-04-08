#!/usr/bin/bash

FRUITS=(Mango Banana Apple "Red Grapes")        # quotes don't make difference, same result

echo ${FRUITS[*]}                                   # echo [*] = print all 
echo ${FRUITS[@]}                                   # echo [@] = print all 

FRUITS[1]="Crab Apple"                              # replaces banana for Crab Apple index 1 
FRUITS[40]="Dragon Fruit"                           # adds ... index 30 (end)

echo '----------------------------------------------------------------'
echo -e '\n using "${FRUITS[*]}"\n'                  # -e = allows backlash escapes

for fruit in "${FRUITS[*]}"                         # [*] prints all on same line
do
    echo $fruit
done
echo '----------------------------------------------------------------'
echo -e '\n using "${FRUITS[@]}"\n'                  # -e = allows backlash escapes

for fruit in "${FRUITS[@]}"                         # [@] prints all in new lines
do
    echo $fruit
done

echo '---------------------------------------------------------------'

echo -e '\n using "${FRUITS[@]} + $i (index)"\n' 
for ((i=0; i<${#FRUITS[@]}; i++))       # prints all on new lines
do                                      # but i++ counter adds index number and " , "
    echo $i " , " ${FRUITS[$i]}         # $i = index#
done

echo '---------------------------------------------------------------'

echo -e '\n using "${FRUITS[@]} + $key"\n'
for key in "${!FRUITS[@]}"
do  
    echo $key " , " ${FRUITS[$key]}     # 'key' adds whatever number we assing the value to
done                                    # unlike index which is sequential
