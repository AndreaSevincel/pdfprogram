import PyPDF2
import re
import glob
import string

#your full path of directory
PDFpath = input("The Folder Of The PDF Here: ")

input_String = input("The Word You Want to Search?: ")

for file in glob.glob(PDFpath + "/*.pdf"):
    if file.endswith('.pdf'):
        fileReader = PyPDF2.PdfFileReader(open(file, "rb"))

    NumPages = fileReader.getNumPages()

#C:\Users\user\OneDrive\Masaüstü\pdfler

    def PdfWrite():
        for i in range(0, NumPages):
            PageObj = fileReader.getPage(i)
            #get pages as i, so Numpages times
            print("This is Page: ")
            print(i + 1)
            Text = PageObj.extractText()
            ResSearch = re.search(input_String, Text)
            print(file)
            print(ResSearch)

    PdfWrite()



    if input_String.islower:
        print("--------------UpperCASE --------------")
        String2 = input_String.capitalize()
        #if string is lowercase capitalize the string then continue.
        def OzetPdfWrite2():
            for i in range(0, NumPages):
                PageObj = fileReader.getPage(i)
                Text = PageObj.extractText()
                ResSearch = re.search(String2, Text)
                #Ressearch is the word

                if not ResSearch:
                    pass
                else:
                    print("This is Page: ")
                    print(i + 1)
                    print(file)
                    print(ResSearch)

        PdfWrite()
        #ozet kisminda none yok
    def OzetWriting():
        print("---------Ozet----------")
        for i in range(0, NumPages):
            PageObj = fileReader.getPage(i)
            Text = PageObj.extractText()
            ResSearch = re.search(input_String, Text)
            #ressearch null ise bir sey yazma

            if not ResSearch:
                pass
            else:
                print("This is Page: ")
                print(i + 1)
                print(file)
                print(ResSearch)

    OzetWriting()

    print("--------------Ozet but Uppercase--------------")#Uppercase is the func PdfWrite2

    OzetPdfWrite2()# line 29 (ozetin buyuk harflisi)
