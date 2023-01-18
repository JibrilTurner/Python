passwordKey = "47"
password = input("Enter Password:")
attempts = 0 

while passwordKey != password and attempts < 2: 
    password = input("Enter Password:")
    attempts = attempts + 1 

if attempts >= 2: 
    print("eat dick and die ")
else: 
    print("good job")