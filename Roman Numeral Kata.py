 # This function converts Roman Numerals to Numbers#
def RomanNumeralConv():
    # assign the input to as a list to a variable 'numeral'
    numeral=list(input("Type in the Roman Numeral in uppercase and hit enter: "))
    #  uncomment the print below to  see the numeral variable returns as a list-- testing perposes
    #  print(numeral)
    #preassign a dictionary to hold the major Roman Numeral as key and the number equivalent as values
    dicta={'M':1000,'C':100,'L':50,'X':10,'V':5,'I':1}
    #use the map function to  iterate through the numeral list and pass to dicta.get 
    # this then maps each value from the dictionary to the values in the numeral list 
    # as returns the  mapped values to a list 'lst'
    lst=list(map(dicta.get,numeral))
    ##ignore#for i in lst: 
    # create two other variables to perform operations 'sm' sum up list 'lst' a
    # nd is returned when the if condition below if met 
    sm=(sum(lst))
    #'diff'  holds the value of the sm  - the lst the index location of the first 
    # value in the list'lst  multiplied by 2 this is returned when the if condition is not met
    diff= sm - (lst[0]*2)
    # if the value in the first index of the list'lst is gretaer than the  
    # value in the second second index place  then erform function  
    if lst[0]>=lst[1]:
        print(sm)
    else:
        print(diff)
