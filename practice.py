# starting with Hello World!!
print('Hello World!')

# looking into data types
num = 10
print('Type of num is : ', type(num))

word = 'hello'
print('Type of word is : ', type(word))

price = 99.99
print('Type of price is : ', type(price))

complex_num = 10+5j
print('Type of complex_num is : ', type(complex_num))

flag = True
print('Type of flag is : ', type(flag))

my_list = ['Friends', 'big bang theory', 2099, 'How i met your ', 2099]
print('my_list : ', my_list)
print('Type of my_list is : ', type(my_list))

my_list2 = ('Friends', 'big bang theory', 2099, 'How i met your ', 2099)
print('my_list2 : ', my_list2)
print('Type of my_list2 is : ', type(my_list2))

my_list3 = {'Friends', 'big bang theory', 2099, 'How i met your ', 2099}
print('my_list3 : ', my_list3)
print('Type of my_list3 is : ', type(my_list3))

my_list4 = ({'Friends', 'big bang theory', 2099, 'How i met your ', 2099})
print('my_list4 : ', my_list4)
print('Type of my_list4 is : ', type(my_list4))

my_range = range(1, 30, 2)
print('my_range : ', my_range)
print('Type of my_range is : ', type(my_range))

my_range = range(1, 30, 2)
print('my_range : ', my_range)
print('Type of my_range is : ', type(my_range))

my_dict = {'key1':'value1', 'key1':'value2', 'key3':'value3', 'key4':'value5'}
print('my_dict : ', my_dict)
print('Type of my_dict is : ', type(my_dict))

my_var = None
print('Type of my_var is : ', type(my_var))

x = b"Hello"  #bytes	
y = bytearray(5)  #bytearray	
z = memoryview(bytes(5))  #memoryview
print('Type of x is : ', type(x))
print('Type of y is : ', type(y))
print('Type of z is : ', type(z))

# diving deep into lists
# access items
print('first element of my_list : ', my_list[0])
print('last element of my_list : ', my_list[-1])

# modify items
my_list[0] = 'F.R.I.E.N.D.S'
print('after modifying first element of my_list : ', my_list[0])

# add new items
my_list.append('The Family')
print('now the last element of my_list : ', my_list[-1])
# there are also insert(), extend()

# removing item
my_list.pop()  #removing last item
print('now the last element of my_list : ', my_list[-1])
my_list.pop(0)  #removing last item
print('now my_list : ', my_list)
# also there are remove(), del, clear()