#current working directory

import os

#will give you complete file path of this file
# os.getcwdb()

#read file from same directory
f= open(r'File Paths and Functions\demo.txt')#relative path
f1= open(r'C:\Users\udita\OneDrive\Desktop\Python\File Paths and Functions\demo.txt')#absolute path

#read from outside of working directory
f2= open(r'C:\Users\udita\OneDrive\Desktop\Python\demo2.txt')#absolute path
f3 = open(r'demo2.txt')#relative path

# text = f.read()
text=f.readlines()
f.close()
print(text)
