f = open("demo.txt","w+")
str = input("Enter a string: ")
f.write(str)

f = open("demo.txt","r")
words = f.read().split()
print(words)

#task - 1 count the number of words
print("Number of words in file are : ",len(words))

# task - 2 count the number unique words and display the words

unique_words = set(words)
print("Number of unique words are : ",len(unique_words))
print("Unique words are : ",unique_words)

#task - 3 display words starting with 'a' or 'A'

words_with_a = [] 
for word in unique_words:
    if word[0].lower() == 'a':
        words_with_a.append(word)

print("Words starting with 'a' are : ",words_with_a)
print("Number of words starting with 'a' or 'A' are : ", len(words_with_a) )


