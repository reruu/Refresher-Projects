#By default, Python's %f formatting adds six decimal places.

mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

# The .2f tells Python to format it to 2 decimal places
print(f"My formatted float is: {myfloat:.2f}")\
# Notice the %.2f instead of just %f
print("Float: %.2f" % myfloat)
# round(variable, number_of_decimal_places)
my_rounded_float = round(myfloat, 2)


