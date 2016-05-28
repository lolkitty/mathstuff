while True:
    n = input(' Give me a number: ') # gets two numbers
    if n.isdigit():
        n = int(n)
    else:
        print("Not A NUMBER")
        
    w = input(' Give me another a number: ')
    
    if w.isdigit():
        w = int(w)
    else:
        print("Not A NUMBER")

    def addfac(x,y): # defines function
        result = 0 # defines result
        list = range(x,y+1) # generates list includng x and y.
        #list = range(x,y)
        #list.append(y)
        for i in range(0,len(list)): # generates for loop from 0 to the length of the list.
            result = result + list[i] # adds all the indexes together
        return str(result) #returns result as string.

    #explains and prints result.
    print ("This is all the numbers from " + str(n) + " to " + str(w) + " added up INCLUDING the two numbers. So, 1 and 3 =1 + 2 + 3" )
    print (addfac(n,w))


