# Example file for Advanced Python by Joe Marini
# Understanding Python scope


# declare a variable within the global scope
x = 1

# define a local function with a variable "x"
def test():
    global x
    x = 10
    print(x)

# Run the test function and observe the two results
test()
print(x)

x = x + 5
print(x)
test()


# Nested functions create inner scopes. These are called closures:
def multiplier_maker(factor):
    def multiply(num):
        return num * factor
    def divide(num): # Never accessed
        return num / factor
    return multiply

doubler = multiplier_maker(2)
tripler = multiplier_maker(3)

print(doubler(10))
print(doubler(15))
print(tripler(10))
print(tripler(15))
