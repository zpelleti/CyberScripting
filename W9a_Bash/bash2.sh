#!/usr/bin/bash

function f1() {
    declare x
    x=7
    y=8
}

function f2() {
     
    declare string="ABCdef"
    echo string = $string                 # quote marks are not necessary after echo
    
    declare -r readonly="A value"
    echo readonly = $readonly
    # readonly="New Value" won't work 
    
    declare -a Myarray
  
    Myarray[2]="Second Value"                           # value of [2] is "second value"
    echo 'Myarray[2]' = ${Myarray[2]}       
    
    Myarray2[3]=4                                       # value of 3 is now 4
    echo 'Myarray2[3]'= ${Myarray2[3]}
    
    Myarray3["hotdog"]="baseball"
    echo Myarray3[hotdog]= ${Myarray3["hotdog"]}        # value of hotdog is now baseball  

    
    declare -i myIvar=1                                 # -i will increase values not add character
    myIvar+=2
    echo myIvar+2= ${myIvar}
    
    declare myVar=1                                     # without -i we get 12 output
    myVar+=2
    echo myVar + 2 = ${myVar}
    
    # All that's happening inside a function has to be called
    # or it won't display
    
   
}

f2

x=1
y=2
echo x is $x
echo y is $y

echo Calling f1
f1
echo x is $x
echo y is $y


    # declare -l lstring="ABCdef"     # to convert NAMEs to lower case on assignment
    # declare -u ustring="ABCdef"     # to convert NAMEs to upper case on assignment
    # declare -r readonly="A Value"   # to make NAMEs readonly
    # declare -a Myarray              # to make NAMEs indexed arrays (if supported)
    # declare -A Myarray2             # to make NAMEs associative arrays (if supported)
    # declare -i myIvar=1             # to make NAMEs have the `integer' attribute
    # declare    myVar=1