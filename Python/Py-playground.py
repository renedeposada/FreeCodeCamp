print('My favorite programming languages are', 'Python', 'JavaScript', 'and', 'React')

my_integer_var = 10
print(type(my_integer_var))  # <class 'int'>

account_balance = '12'
print(isinstance(account_balance, int)) # False

my_str_3 = """Multiline
string"""
print(my_str_3, type(my_str_3))

msg = "It's a sunny day"
quote = 'She said, "Hello World!"'

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}')

my_str = 'Hello world'
print(my_str[1:4]) # ell

my_str = 'Hello world'
print(my_str[::-1]) # dlrow olleH

my_str = 'hello world'

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD

my_int = 56
my_float = 5.4

sum_int_and_float = my_int + my_float

print(sum_int_and_float) # 61.4
print(type(sum_int_and_float)) # <class 'float'>

# Augmented assignments
greet = 'Hello'
greet *= 3

print(greet) # HelloHelloHello