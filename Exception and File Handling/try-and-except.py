#no error in code here
try:
    print("This executes first.")
except:
    print("This executes if and only if there is an error.")

#error in code here
try:
    print("This executes first.")
    x = 4 / 0 #zero division - error
except:
    print("Oops!! something bad happened.")

#error before print line
try:
    x = 4 / 0 #zero division - error
    print("This executes first.")
    
except:
    print("Oops!! something bad happened.")

#return error code
def addition(a, b):
    try:
        return a + b
    except TypeError:
        return 10 ** 2


c = addition(2, '4')
print(c)


