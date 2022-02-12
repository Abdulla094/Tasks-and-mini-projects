#WAP TO FIND LINEAR SEARCH

#WAP TO CREATE AN ALARM CLOCK


list = [2, 6, 1, 7, 8, 3, 4, 5, 10, 9]
list.sort()
print(list)
n = int(input("ENTER THE NUMBER YOU WANT TO SEARCH : "))
pos = -1
def search (a, b) :
        for i in range(len(list)) :
                 if list[i]== n:
                       globals( )["pos"]=i
                       return True
       

if search(list, n) :
         print("found at", pos) 
else:
        print("not found")
    

