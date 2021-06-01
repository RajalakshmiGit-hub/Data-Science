#                                   Complex Number Assignment by Rajalakshmi B
# Qn: Declare an int value and store it in a variable.
# Check the type and print the id of the same.
print("Qn1  : Declare an complex number and store it in a variable. Check the type and print the id of the same.")
a = 10+20j
print("Ans1 : The value of Complex number is :", a, "; It's type is :", type(a), "; It's ID is :", id(a))

# Arithmetic Operator
g = 50+30j
h = 20+70j
print("\nQn2: Arithmetic Operations")
print("Ans2: The Sum of", g, "and", h, "is", g + h)
print("\t The Difference of", g, "and", h, "is", g - h)
print("\t The Product of", g, "and", h, "is", g * h)
print("\t The value after dividing", g, "with", h, "is", g / h)
print("\t The result of the", g, "to the power of the", h, "is", g ** h)

# Equality Operator
g = 60+50j
h = 40+20j
print("\nQn3: Equality Operations")
print("Ans3: Is", g, "equal to", h, "? :\t", bool(g == h))
print("\t Is", g, "not equal to", h, "? :", bool(g != h))

# Logical Operator
print("\nQn4: Logical Operations")
print("Ans4: ---And operator---")
print("\t10+20j and 20 + 30j |", 10+20j and 20 + 30j)
print("\t0 + 0j and 20 + 30j |", 0 + 0j and 20 + 30j)
print("\t20 + 30j and 0 + 0j  |", 20 + 30j and 0 + 0j)
print("\t0 + 0j and 0 + 0j  |", 0 + 0j and 0 + 0j)

print("\n\t---Or operator---")
print("\t10+20j or 20 + 30j |", 10+20j or 20 + 30j)
print("\t0 + 0j or 20 + 30j |", 0 + 0j or 20 + 30j)
print("\t20 + 30j or 0 + 0j  |", 20 + 30j or 0 + 0j)
print("\t0 + 0j or 0 + 0j  |", 0 + 0j or 0 + 0j)

print("\n\t---Not operator---")
print("\tnot 10+20j |", not 10+20j)
print("\tnot 0 + 0j  |", not 0 + 0j)

print("\nQn5: Check the output of expression")
print('''Ans5: ''')
a = 10 + 20j
b = 10 + 20j
print("a =", a, "; b =", b)
print("a is b:", a is b)
print("a is not b:", a is not b)


# Membership Operations
print("\nQn6: Membership Operations")
print('''Ans6: ''')
print("'2.7' in 'Python2.7.8' : ", '2.7' in 'Python2.7.8')
print('''10+20j in [ 10 , 10.20 , 10 + 20j , 'Python' ] : ''', 10+20j in [10, 10.20, 10 + 20j, 'Python'])
print('''10+20j in ( 10 , 10.20 , 10 + 20j , 'Python' ) : ''', 10+20j in (10, 10.20, 10 + 20j, 'Python'))
print('''30 + 40j in { 1 , 20.30 , 30 + 40j } :''', 30 + 40j in { 1 , 20.30 , 30 + 40j })
print("30 + 40j in { 1 : 100 , 2.3 : 200 , 30 + 40j : 300 } :", 30 + 40j in { 1 : 100 , 2.3 : 200 , 30 + 40j : 300 })
print("10 in range ( 20 ) : ", 10 in range(20))
