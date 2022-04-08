
from genericpath import exists
from os import path
from os import rename

import shutil   # for copying 
from shutil import make_archive
from zipfile import ZipFile

import python8_filename

def main():
    filename = input("Enter the source file name: ")
    print(filename)
    
    # if file doesn't exists, it gets created, 
    # but filename.txt opens by default
    if not(path.exists(filename)):
        print("Calling python8_filename.main()...")
        python8_filename.main(filename)
        

#=================================================
    # to make a duplicate of existing file: 
    # new file input (duplicate) duplicates 
#=================================================  Need explanation...

    # filename.txt exists, so terminal displays the path :
    if path.exists(filename):
        src = path.realpath(filename);

        print("src = {:10s}" .format(src))
    
    # to make abckup copy:   (adds .bak to original file)  
        dst = src + ".bak"
    # use shell to make a copy of the file (contents):
        shutil.copy(src, dst)
    # rename the original file:  
        rename(filename, "newFile " + filename)
    
    ## to put everything in a ZIP archive:
    #   source:
        root_dir, tail = path.split(src)
        print ("root_dir = {:10s}, tail = {:10s}" .format(root_dir,tail))
        shutil.make_archive("archive", "zip", root_dir)
    
    # destination:
        root_dir,tail = path.split(dst)
        with ZipFile("myFiles.zip", "w") as newzip:
            newzip.write("newFile " + filename)
            newzip.write(tail)
            
if __name__ == "__main__":
    main()
