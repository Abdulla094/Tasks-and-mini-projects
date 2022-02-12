#WAP TO CREATE A URL SHORTENER IN PYTHON
import pyshorteners

link = input("ENTER THE LINK : ")

shortener = pyshorteners.Shortener()

x = shortener.tinyurl.short(link)

print(x)
