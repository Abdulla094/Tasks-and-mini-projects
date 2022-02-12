#binary search - 10 elements

list = [5, 1, 7, 9, 3, 4, 6, 8, 2 ,10]
list.sort()
print(list)

first = 0
last = len(list)-1
mid = (first+last) // 2
item = int(input("ENTER THE NUMBER you want to search for"))
found = False
while( first<=last and not found):
    mid = first + last // 2
    if list[mid] == item :
        print(f'Found at location {mid}')
        found = True
    else:
        if item < list[mid]:
            last = mid -1
        else:
            first = mid + 1 

if found == False:
    print("Number not found")

    


