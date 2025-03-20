###  Higher Order Functions ####

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