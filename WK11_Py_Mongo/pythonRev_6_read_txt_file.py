
def main():
    ## initialize counter:
    total = 0.0
    try:
        ## open file: 
        infile = open('sales_data.txt', 'r')
        ## read file + accumulate values count: 
        for line in infile:
            amount = float(line)
            total += amount
        ## close file:
        infile.close()
        
        ## print total: Sum all from sales_data figures
        print(f"{total:,.2f}")
        
    ## intro to exceptions in python: 
    except IOError:
        print("An error occured trying to read the file")
        
    except ValueError:
        print("Non-Numeric data found in file")

    except:
        print("An unknown error occured")
    

if __name__ == "__main__":
    main()
    