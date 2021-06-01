#                                   Float Assignment by Rajalakshmi B
# Qn: Declare an int value and store it in a variable.
# Check the type and print the id of the same.
print("Qn1  : Declare an float value and store it in a variable. Check the type and print the id of the same.")
a = 10.20
print("Ans1 : The value of Float variable is :", a, "; It's type is :", type(a), "; It's ID is :", id(a))

# Arithmetic Operator
g = 5.3
h = 2.6
print("\nQn2: Arithmetic Operations")
print("Ans2: The Sum of", g, "and", h, "is", g + h)
print("\t The Difference of", g, "and", h, "is", g - h)
print("\t The Product of", g, "and", h, "is", g * h)
print("\t The value after dividing", g, "with", h, "is", g / h)
print("\t The remainder after dividing", g, "with", h, "is", g % h)
print("\t The quotient after dividing", g, "with", h, "is", g // h)
print("\t The result of the", g, "to the power of the", h, "is", g ** h)

# Comparison Operator
g = 9.2
h = 3.5
print("\nQn3: Comparison Operations")
print("Ans3: Is", g, "greater than", h, "? : \t\t\t", bool(g > h))
print("\t Is", g, "lesser than", h, "? : \t\t\t", bool(g < h))
print("\t Is", g, "greater than or equal to", h, "? :", bool(g >= h))
print("\t Is", g, "lesser than or equal to", h, "? : ", bool(g <= h))

# Equality Operator
g = 6.5
h = 4.2
print("\nQn4: Equality Operations")
print("Ans4: Is", g, "equal to", h, "? :\t", bool(g == h))
print("\t Is", g, "not equal to", h, "? :", bool(g != h))

# Logical Operator
print("\nQn5: Logical Operations")
print("Ans5: ---And operator---")
print("\t10.20 and 20.30 |", 10.20 and 20.30)
print("\t0.0 and 20.30 |", 0.0 and 20.30)
print("\t20.30 and 0.0  |", 20.30 and 0.0)
print("\t0.0 and 0.0  |", 0.0 and 0.0)

print("\n\t---Or operator---")
print("\t10.20 or 20.30 |", 10.20 or 20.30)
print("\t0.0 or 20.30 |", 0.0 or 20.30)
print("\t20.30 or 0.0  |", 20.30 or 0.0)
print("\t0.0 or 0.0  |", 0.0 or 0.0)

print("\n\t---Not operator---")
print("\tnot 10.20 |", not 10.20)
print("\tnot 0.0  |", not 0.0)

print("\nQn6&7: Check the output of expression")
print('''Ans6&7: ''')
a = 10.20
b = 10.20
print('''Id of float values are different when the same value is assigned to two different variables''')
print("a =", a, "; b =", b)
print("ID of a =", id(a), "; ID of b =", id(b))
print("a is b:", a is b)
print("a is not b:", a is not b)


a = 10.20
b = a
print('''\nId of float values are same if we assign the variable having float e.g b=a''')
print("a =", a, "; b = a")
print("ID of a =", id(a), "; ID of b =", id(b))
print("a is b:", a is b)
print("a is not b:", a is not b)
print("Thus Object reusability concept is not applicable on float values.")


# Membership Operations
print("\nQn8: Membership Operations")
print('''Ans8: ''')
print("'2.7' in 'Python2.7.8' : ", '2.7' in 'Python2.7.8')
print('''10.20 in [ 10 , 10.20 , 10 + 20j , 'Python' ] : ''', 10.20 in [10, 10.20, 10 + 20j, 'Python'])
print('''10.20 in ( 10 , 10.20 , 10 + 20j , 'Python' ) : ''', 10.20 in (10, 10.20, 10 + 20j, 'Python'))
print('''20.30 in { 1 , 20.30 , 30 + 40j } :''', 20.30 in {1, 20.30, 30 + 40j})
print("2.3 in { 1 : 100 , 2.3 : 200 , 30 + 40j : 300 } :", 2.3 in {1: 100, 2.3: 200, 30 + 40j: 300})
print("10 in range ( 20 ) : ", 10 in range(20))
