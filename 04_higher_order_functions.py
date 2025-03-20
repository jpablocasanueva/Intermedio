###  Higher Order Functions ####
from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_tow_values_and_add_value(first_value, second_value,f_sum_one):
    return f_sum_one(first_value + second_value)


# print(sum_tow_values_and_add_value(4,4,sum_one))
# print(sum_tow_values_and_add_value(4,4,sum_five))


### Clousres ###

def sum_tem():
    def add(value):
        return value + 10
    return add


addClosure = sum_tem()
print(addClosure(10))

numbers = [2,5,10,21]

#map

def multiply_two(number):
    return number * 2

print(list(map(multiply_two,numbers)))

print(list(map(lambda number: number * 2,numbers)))

#filter
def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter( filter_greater_than_ten,numbers)))
print(list(filter( lambda number: number > 10,numbers)))

#reduce

def sum_two_values(first_value, second_value):
    return first_value + second_value
    

print(reduce(sum_two_values,numbers))