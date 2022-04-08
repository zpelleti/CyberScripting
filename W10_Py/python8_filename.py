
from random import seed
from random import randint

def main(filename):  

#============Create File ==================
    #filename = input("Enter the filename: ")
    print (len(filename))
    if len(filename) == 0:
        filename = "filename.txt"
    # Open a file for writing and create it if it doesn't exist
    file = open(filename, "a")  # a = append, w = overwrite
    
#===========File Created ==================
#===========Write on file:
    string = randint(1,5)
    num = randint(string+1, string+10)
    
#===========Print contents:
    print ('string = [{:0>5d}], num = [{:<5}]'.format(string, num))
                    # [00002]         [7     ]     
                    #e.g: string +2, 5 spaces]
                    #e.g: num = string + 5, 5 spaces padding after (<) 
    for i in range(string, num):
        file.write("Data: %d\n" % (i+1))
    file.write("========================\n")
    
#==========Read contents:
    file = open(filename, "r")
    if file.mode == "r":            # check that the file is opened
    # use read() function to read the entire file:
        contents = file.read()
        print(contents)
        
        for x in file:
            print(x)
    file.close()
  

print("python8.py, __name__ = " + __name__)
if __name__ == "__main__":
    main("")
