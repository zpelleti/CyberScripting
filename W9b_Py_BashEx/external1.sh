#!/usr/bin/bash

function f1(){
    echo "You give me $# arguments"     # num of arguments on f1 call
    echo "First value: $1"              # first argument f1 (3) 
    echo "Second value $2"
    echo "Third val $3"
    echo "Fourth: $4"
}

function f2(){
    echo $(($1 + $2))
}

f1 $((3)) $(($y+2)) $((8))

echo -e "\n"

f1 $((1)) X $((Z)) 8

echo "==========================="
echo "This is External"
x=10
y=25

f1 x $(($y+2))                      # calling f1 and passing it x as 1st value
                                    # 25+2 as 2nd

result=$( f2 x $(($y+2)) )          # f2 = (first + second)
                                    # where y is 25+2 and x is 10 
echo "Result: $result"              

