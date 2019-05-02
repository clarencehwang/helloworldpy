#Python 3
#This is my first piece of code in Python. 
#I take note of the syntax that I am unfamiliar with.

#Print includes new line; is a function in Python 3 but not previously.
#No semicolons.
print("Hello, World!") 

#Notice lack of declaration, every variable is an object.
myString = 'If you use quotation marks to set your strings, '
#print() includes 'end' parameter, default '\n'. 
#Change this to print on same line.
print(myString, end="") #Why doesn't end=None work?
#Semicolons CAN be used to delimit statements.
myString = "you don't need to worry about apostrophes!" ; print(myString)