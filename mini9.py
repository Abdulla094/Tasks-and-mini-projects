ship=[]
counter=0

print("welcome to my game!")
for i in range(0,5):
    sea=[0,0,0,0,1,1,1,0,0,0,0,0]
    bomb=int(input("enter the location to bomb(0-11): "))
    location=sea[bomb]
    if location==1:
        counter=counter+1
        if counter==3:
            print("you won!")
            quit()
    else:
        print("you lose!")



