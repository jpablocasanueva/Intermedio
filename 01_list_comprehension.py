### List Comprehension ###

my_ori_list = [0,1,2,3,4,5,6,7]
print(my_ori_list)

my_list = [i for i in range (8)]
print(my_list)

my_list = [i+1 for i in range (8)]
print(my_list)

my_list = [i*2 for i in range (8)]
print(my_list)
my_list = [i*i for i in range (8)]
print(my_list)

def sum_five(num):
    return num + 5 

my_list = [sum_five(i) for i in range (8)]
print(my_list)