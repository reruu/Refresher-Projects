'''
A char is a single character (e.g., 1, 6, %, b, p, ., T).
A str (string) is a sequence of multiple characters.
To create a string variable, enclose the text in single or double quotes:
'''
string = "you're words po baby"
char = 'A'
print(f'string = "{string}"')
print(f'char = "{char}"')
print(char)
print(string)

#If you want to print multiple words on the same line, you can use the end parameter:
print("Hello World!", end=" ")
print("I will print on the same line.")

x = y = z = "Hello World"
x, y, z = "Orange", "Banana", "Cherry"

fruits = ['apple', 'banana', 'cherry']
a, b, c = fruits
print(a)