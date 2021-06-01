#                                   Boolean Assignment by Rajalakshmi B
# Qn: Declare an int value and store it in a variable.
# Check the type and print the id of the same.
print("Qn1  : Declare an boolean value and store it in a variable. Check the type and print the id of the same.")
a = True
print("Ans1 : The value of Boolean variable is :", a, "; It's type is :", type(a), "; It's ID is :", id(a))

b = bool(34)
c = bool(34)
print("\nQn2 : Take one boolean value between 0 - 256. Assign it to two different variables.")
print("\tCheck the id of both the variables. It should come the same.")
print("Ans2 : The ID of first variable value which is between 0-256 is :", id(b), ".")
print("\t  The ID of second variable is :", id(c))
print("\t  Both the IDs are same") if id(b) == id(c) else print("Both the IDs are not same")

# Arithmetic Operator
g = bool(5)
h = bool(3)
print("\nQn3: Arithmetic Operations")
print("Ans3: The Sum of", g, "and", h, "is", g + h)
print("\t The Difference of", g, "and", h, "is", g - h)
print("\t The Product of", g, "and", h, "is", g * h)
print("\t The value after dividing", g, "with", h, "is", g / h)
print("\t The remainder after dividing", g, "with", h, "is", g % h)
print("\t The quotient after dividing", g, "with", h, "is", g // h)
print("\t The result of the", g, "to the power of the", h, "is", g ** h)

# Comparison Operator
g = bool(9)
h = bool(0)
print("\nQn4: Comparison Operations")
print("Ans4: Is", g, "greater than", h, "? : \t\t\t", bool(g > h))
print("\t Is", g, "lesser than", h, "? : \t\t\t", bool(g < h))
print("\t Is", g, "greater than or equal to", h, "? :", bool(g >= h))
print("\t Is", g, "lesser than or equal to", h, "? : ", bool(g <= h))

# Equality Operator
g = bool(6)
h = bool(0)
print("\nQn5: Equality Operations")
print("Ans5: Is", g, "equal to", h, "? :\t", bool(g == h))
print("\t Is", g, "not equal to", h, "? :", bool(g != h))

# Logical Operator
print("\nQn6: Logical Operations")
print("Ans6: ---And operator---")
print("\tTrue and True |", True and True)
print("\tFalse and True |", False and True)
print("\tTrue and False  |", True and False)
print("\tFalse and False  |", False and False)

print("\n\t---Or operator---")
print("\tTrue or True |", True or True)
print("\tFalse or True |", False or True)
print("\tTrue or False  |", True or False)
print("\tFalse or False  |", False or False)

print("\n\t---Not operator---")
print("\tnot True |", not True)
print("\tnot False  |", not False)

# Bitwise Operator
print("\nQn7: Bitwise Operations")
print('''Ans7: ''')
print("\t Bitwise and : True & False |", True & False)
print("\t Bitwise or  : True | False |", True | False)
print("\t Bitwise (^) : True ^ False |", True ^ False)
print("\t Bitwise (~) : ~True     |", ~True)
print("\t Bitwise (<<): True << 2 |", True << 2)
print("\t Bitwise (>>): True >> 2 |", True >> 2)

print("\nQn8: Check the output of expression")
print('''Ans8: ''')
a = True
b = True
print("a =", a, "; b =", b)
print("ID of a =", id(a), "; ID of b =", id(b))
print("a is b:", a is b)
print("a is not b:", a is not b)

a = False
b = False
print("\na =", a, "; b =", b)
print("ID of a =", id(a), "; ID of b =", id(b))
print("a is b:", a is b)
print("a is not b:", a is not b)

# Membership Operations
print("\nQn9: Membership Operations")
print('''Ans9: ''')
print("True in [ 10 , 10.20 , 10 + 20j , 'Python' , True ] : ", True in [ 10 , 10.20 , 10 + 20j , 'Python' , True ])
print('''False in ( 10 , 10.20 , 10 + 20j , 'Python' , False ) : ''', False in ( 10 , 10.20 , 10 + 20j , 'Python' , False ))
print('''True in { 1 , 2 , 3 , True } : ''', True in { 1 , 2 , 3 , True })
print('''True in { True : 100 , False : 200 , True : 300 } :''', True in { True : 100 , False : 200 , True : 300 })
print("False in { True : 100 , False : 200 , True : 300 } :", False in { True : 100 , False : 200 , True : 300 })

