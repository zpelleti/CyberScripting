from pythonRev_4_Circle import area, circumference
import pythonRev_4_Rectangle ## need to add 'rectangle.area' or ''.circumference' in the 
                             ## function call


## Menu choice constants:
AREA_CIRCLE = 1
CIRCUMFERENCE = 2
AREA_RECTANGLE = 3
PERIMETER_RECTANGLE = 4
QUIT = 5

def main():
    choice = 0
    
    while choice != 5:  ##QUIT
        ##Display the Menu:
        display_menu()
        
        choice = int(input("Enter your choice: "))
        ##Perform action:
        if choice == AREA_CIRCLE:
            radius = float(input("Enter circle's Area:"))
            print("The circle's Area is: ", area(radius)) ## function call to area() 
        elif choice == CIRCUMFERENCE:
            radius = float(input("Enter circle's RAdius:"))
            print("The circumference is: ", circumference(radius)) ## function call to circumference()
        elif choice ==   AREA_RECTANGLE:
            width = float(input("Enter witdh: "))
            length = float(input("Enter length: "))
            print("The rectangle's Area is: ", pythonRev_4_Rectangle.area(width, length)) ## call to rectangle area()
        elif choice == PERIMETER_RECTANGLE:
            width = float(input("Enter width: "))
            length = float(input("Enter length: "))
            print("The Perimeter is: ", pythonRev_4_Rectangle.perimeter(width, length))
        elif choice == QUIT:
            print("Exiting program...")
            exit(0)
        else:
            print("Error: invalid choice")
            display_menu()
            
            

def display_menu():
    print("Menu")
    print("1) Area Circle")
    print("2) Circumference Circle")
    print("3) Area Rectangle")
    print("4) Perimeter Rectangle")
    print("5) Quit")


#if __name__ == "__main()__":
main()
    
