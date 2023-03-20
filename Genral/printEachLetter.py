# Python program to Print Characters in a String
 
str1 = input("Please Enter your Own String : ")
i = 0

while(i < len(str1)):
    print("The Character at %d Index Position = %c" %(i, str1[i]))
    i = i + 1