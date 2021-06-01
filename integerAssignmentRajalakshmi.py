#                                   Integer Assignment by Rajalakshmi B
# Qn: Declare an int value and store it in a variable.
# Check the type and print the id of the same.
print("Qn1  : Declare an int value and store it in a variable. Check the type and print the id of the same.")
a = 10
print("Ans1 : The value of Integer variable is :", a, "; It's type is :", type(a), "; It's ID is :", id(a))

# Take one int value between 0 - 256. Assign it to two different variables.
# Check the id of both the variables. It should come the same. Check why?

b = 35
c = 35
print("\nQn2 : Take one int value between 0 - 256. Assign it to two different variables.")
print("\tCheck the id of both the variables. It should come the same.")
print("Ans2 : The ID of first variable value which is between 0-256 is :", id(b), ".")
print("\t  The ID of second variable is :", id(c))
print("\t  Both the IDs are same as Python caches integer values between -5 and 256, to gain performance.") if id(
    b) == id(c) else print("Both the IDs are not same")

del b, c

# Take one int value either less than -5 or greater than 256.
# Assign it to two different variables.
# Check the id of both the variables. It should come different.Check why?
d = 1000
e = 1000
print("\nQn3: Take one int value either less than -5 or greater than 256. Assign it to two different variables.")
print("\tCheck the id of both the variables. It should come different.")
print("Ans3 : The ID of first variable value is :", id(d), ".")
print("\t  The ID of second variable is :", id(e))
print("\t  Both the IDs are same. ") if id(d) == id(e) else print("\t Both the IDs are different")
print("\t Python caches integer values between -5 and 256 only")

# Arithmetic Operator
g = 9
h = 5
print("\nQn4: Arithmetic Operations")
print("Ans4: The Sum of", g, "and", h, "is", g + h)
print("\t The Difference of", g, "and", h, "is", g - h)
print("\t The Product of", g, "and", h, "is", g * h)
print("\t The value after dividing", g, "with", h, "is", g / h)
print("\t The remainder after dividing", g, "with", h, "is", g % h)
print("\t The quotient after dividing", g, "with", h, "is", g // h)
print("\t The result of the", g, "to the power of the", h, "is", g ** h)

# Comparison Operator
g = 9
h = 5
print("\nQn5: Comparison Operations")
print("Ans5: Is", g, "greater than", h, "? : \t\t\t", bool(g > h))
print("\t Is", g, "lesser than", h, "? : \t\t\t", bool(g < h))
print("\t Is", g, "greater than or equal to", h, "? :", bool(g >= h))
print("\t Is", g, "lesser than or equal to", h, "? : ", bool(g <= h))

# Equality Operator
g = 9
h = 6
print("\nQn6: Equality Operations")
print("Ans6: Is", g, "equal to", h, "? :\t", bool(g == h))
print("\t Is", g, "not equal to", h, "? :", bool(g != h))

# Logical Operator
print("\nQn7: Logical Operations")
print("Ans7: ---And operator---")
print("\t10 and 20 |", 10 and 20)
print("\t0  and 20 |", 0 and 20)
print("\t20 and 0  |", 20 and 0)
print("\t0  and 0  |", 0 and 0)

print("\n\t---Or operator---")
print("\t10 or 20 |", 10 or 20)
print("\t0  or 20 |", 0 or 20)
print("\t20 or 0  |", 20 or 0)
print("\t0  or 0  |", 0 or 0)

print("\n\t---Not operator---")
print("\tNot 10 |", not 10)
print("\tNot 0  |", not 0)

# Bitwise Operator
print("\nQn8: Bitwise Operations")
print('''Ans8: ''')
print("\t Bitwise and : 10 & 20 |", 10 & 20)
print("\t Bitwise or  : 10 | 20 |", 10 | 20)
print("\t Bitwise (^) : 10 ^ 20 |", 10 ^ 20)
print("\t Bitwise (~) : ~10     |", ~10)
print("\t Bitwise (<<): 10 << 2 |", 10 << 2)
print("\t Bitwise (>>): 10 >> 2 |", 10 >> 2)

print("\nQn9: Check the output of expression")
print('''An9: ''')
a = 10
b = 10
print("a =", a, "; b =", b)
print("a is b:", a is b)
print("a is not b:", a is not b)

a = 1000
b = 1000
print("\na =", a, "; b =", b)
print("a is b:", a is b)
print("a is not b:", a is not b)

print('''\nQn10: Check the output of expression: 10 +( 10 * 32 )// 2 ** 5 & 20 +(~( -10 ))<< 2 ''')
print('''An10: ''', 10 + (10 * 32) // 2 ** 5 & 20 + (~(-10)) << 2)

# Membership Operations
print("\nQn11: Membership Operations")
print('''Ans11: ''')
print("'2' in 'Python2.7.8' : ", '2' in 'Python2.7.8')
print('''10 in [ 10 , 10.20 , 10 + 20j , 'Python' ] : ''', 10 in [10, 10.20, 10 + 20j, 'Python'])
print('''10 in ( 10 , 10.20 , 10 + 20j , 'Python' ) : ''', 10 in (10, 10.20, 10 + 20j, 'Python'))
print('''2 in { 1 , 2 , 3 } :''', 2 in {1, 2, 3})
print("3 in { 1 : 100 , 2 : 200 , 3 : 300 } :", 3 in {1: 100, 2: 200, 3: 300})
print("10 in range ( 20 ) : ", 10 in range(20))

print('''\nQn12: Declare one binary, one octal and one hexadecimal value and store them in three 
different variables. Convert 9876 to its binary, octal and hexadecimal equivalent and print
their corresponding value.''')
print('''An12: ''')
a=0b10011010010100
b=0o23224
c=0x2694
print("Decimal value of 0b10011010010100 is :", a)
print("Decimal value of 0o23224 is :", b)
print("Decimal value of 0x2694 is :", c)

print('\nBinary value of 9876 is :', bin(9876))
print ("Octal value of 9876 is :", oct (9876))
print ("Hexadecimal value of 9876 is :", hex (9876))

# Check the Output
print("\nQn13: Binary, Octal and Hexadecimal Conversion 1")
print('''An13: ''')
a = 0b1010000
print("Decimal value of 0b1010000 is :", a)
b = 0o7436
print("Decimal value of 0o7436 is :", b)
c = 0xfade
print("Decimal value of 0xfade is :", c)
print('\nBinary value of 80 is :', bin(80))
print ("Octal value of 3870 is :", oct (3870))
print ("Hexadecimal value of 64222 is :", hex ( 64222 ))

print("\nQn14: Binary, Octal and Hexadecimal Conversion 2")
print('''An14: ''')
print ('Binary value of 0b1010000 is :', bin ( 0b1010000))
print ('Binary value of 0xfade is :',bin ( 0xfade ))
print ("Octal value of 0xfade is :",  oct ( 0xfade ))
print ("Octal value of 0o7436 is :", oct ( 0o7436))
print ("Hexadecimal value of 0b1010000 is :",hex ( 0b1010000))
print ( "Hexadecimal value of 0xfade is :",hex ( 0xfade ))