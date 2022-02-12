#read a file line by line in python 
#ensure the word count is less than 250 words and character count should be less than 1250


file = open("demo.txt", 'r')
list = file.read()
x = len(list)
words = list.split()
l = len(words)
file = open("demo.txt", 'r')
listlines = file.readlines()

if (l>250 and x>1250 ):
    print("Words should be less than 250 and the characters should be less than 1250")
    print("You have ",l,"words")
    print("you have",x,"characters")

else:
    print("words=",words)
    print("Number of charachters=",x)
    print("Number of words = ",l)
    print("lines")
    for line in listlines:
        print(line)


