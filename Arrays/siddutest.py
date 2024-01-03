'''symbols=["{}()","({()})","{()}"]
for myvalue in symbols:
    print(myvalue)'''

symbols=["()","({()})","{()}"]
x=input("Enter a string :")

if (symbols[0]==x):
    print("correct")
elif(symbols[1]==x):
    print("correct")
elif(symbols[2]==x):
    print("correct")
else :
    print("wrong")

