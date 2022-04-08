import copy

def main():
    # create two-dim list:
    values = [[1, 2, 3,],
              [4, 5, 6],
              [7, 8, 9]]
    
    
    valueRef = values
    
    # to reuse 'values'
    valueCopy = copy.deepcopy(values)
    
    ## first brackets[ ] = indexes
    # [1] = second array, [2] = third index - change to 55
    valueRef[1][2] = 55
    # [2] = third array, [0] = first index - change to 216
    valueCopy[2][0] = 216
    
    # display first list of elements:
    for row in values:
        for element in row:
            print(f'[{element:0>3d}]', end='')
        print('\n')
    
    # display second list of elements:
    print('======================')
    for row in valueCopy:
        for element in row:
            print(f'[{element:0>3d}]', end='')
        print('\n')
        
## ===========================================================================


    list = ['cat', 'dog', 'fish', 'jumbo', 'steak', 'alt', 'courses', 'eat']
    # to print whole list:
    newList1 = list[:]
    # [2] = fish 
    newList2 = list[2:4] # [4] = jumbo???
    
    # index 1, stop means index 0 starts from index 1, [3] = 'steak', start from 
    # index [3], index [0] is now 'steak', plus 3 = 'eat'
    newList3 = list[1::3]  # start:stop:step
    # add to:
    newList1.append('shark')
    #newList2.append('foody')
    
    print(f'list = {list}')
    # print last element of list only:
    print(f'list[-1] = {list[-1]}')  # negative = works backwards
    
    print(f'newList1 = {newList1}')
    print(f'newList2 = {newList2}')
    print(f'newList3 = {newList3}')
    
    # [-2] = 'courses'
    word = list[-2]   # slice(start, end, step)
    # [1][3] = 'ou'
    x = slice(1, 3)   # 
    print(f'word = {word[x]}')
    
    ## slice text: 
    text = "Prog with Python"
    # [0] = P, end, [0] = 'r', [10] = 'y', end, [0] = 't', [10] = 'i' (starts over)
    x = slice(0, 10, 3) # slice(start, end, step)
    print(f'text = {text[x]}')
    
    list.sort()
    print(f'list.sort() = {list}')
    
    list.reverse()
    print(f'list.reverse() = {list}')
    
if __name__ == '__main__':
    main()
    

    