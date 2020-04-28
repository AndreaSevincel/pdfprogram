import PyPDF2
import re
import sys
import os
import string

# open the pdf file
object2 = input("The directory?: ")

object = PyPDF2.PdfFileReader(object2)

# get number of pages
NumPages = object.getNumPages()



# define keyterms
String = input("The Word you want to search?: ")

def Printing():
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        print("This is Page: ")
        print(i + 1) 
        Text = PageObj.extractText() 
        #print(Text)
        ResSearch = re.search(String, Text)
        print(ResSearch)
Printing()
print("--------------UpperCASE ------------ ")

if String.islower:
    String2 = String.capitalize()

      
Printing()
