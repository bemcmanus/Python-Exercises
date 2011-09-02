def add (a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def subtract (a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Mulutiplying %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Dividing %d / %d" % (a, b)
    return a / b


print "Let's do some match with just functions."

age = add(20, 4)
height = subtract(69, 9)
weight = multiply(100, 2)
iq = divide (50, 5)

print "Age: %d, Height: %d, Weight: %d, iq: %d" % (age, height, weight, iq)


print "Here's a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes:", what


