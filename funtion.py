def voidFuntion( ):
    print("a")

def returnFunction( ):
    x = 5
    return x

def sayHi( ):
    y = "Hello"
    return y

def name(name):
    print ("Hello your name is " + name )

# originally supposed to be name plus age like in my c program where it asks for your name and age,
# but I keep getting TypeError: can only concatenate str (not "int") and its proving to be a waste
# of time to figure it out
def sqaure(num):

    return num * num

voidFuntion()
print (returnFunction())
print (sayHi())
print (sqaure(3))
name('Jibril')

