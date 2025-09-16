# What will the following code output?

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)

# print(my_list1) will print the list with the "first" key value = 42 
# becaue copy() method copies the references to the mutable objects like a list