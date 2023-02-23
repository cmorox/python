# Variables

my_string_variable = 'My string variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)


#Concatenacion  de variables en un print
print(my_string_variable, my_int_variable , my_bool_variable)
print('Este es el valor de:',my_bool_variable)

# Some Functions of system

print(len(my_string_variable))

#Variables in the same line   -  dont use this sintaxis a lot - be carefully

name, surname, alias, age = 'Cristian', 'Moro', 'MoroX', 19

print('Me llamo:', name, surname,'.  My apodo es:', alias, '. Mi edad es:', age)



# Inputs

first_name = input('What is ur name: ')
age = input('How old r u: ')

print(first_name)
print(age)


# We change its type
name = 19
age = 'Cristian'
print(name)
print(age)

# do We force the type?

address: str = 'My adress'
address = 32

print(type(address))