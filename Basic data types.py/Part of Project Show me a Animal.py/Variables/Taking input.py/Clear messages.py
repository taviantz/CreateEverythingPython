#It is highly recommended to state clearly what type of input we expect from our users. 
# To do so, the input() function may take an optional argument, that is, a message
user_name = input('Please, enter your name: ')
print('Hello, ' + user_name)

#Another way to do this is to print the message separately:
print('Enter your name: ')
user_name = input()
print('Hello, ' + user_name)