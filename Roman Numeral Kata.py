 
def RomanNumeralConv():
    numeral=list(input("Type in the Roman Numeral and hit enter: "))
    print(numeral)
    dicta={'M':1000,'C':100,'L':50,'X':10,'V':5,'I':1}
    lst=list(map(dicta.get,numeral))
    #for i in lst:
    sm=(sum(lst))
    diff= sm - (lst[0]*2)
    if lst[0]>=lst[1]:
        print(sm)
    else:
        print(diff)
##finalcopy