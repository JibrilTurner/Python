passwordKey = "42"
password = input("Enter The Password: ")
attempts = 0

while passwordKey != password and attempts < 2:
    password = input("Enter The Password")
    attempts = attempts + 1

if attempts >= 2:
    print("Your password is wrong go to hell.")
else:
    print("Your password is right have a very nice day.")


