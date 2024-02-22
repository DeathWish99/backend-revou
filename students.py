
# try:
#     x = int(input("Enter a number: "))
# except ValueError:
#     print('Invalid Input')

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for item in lst:
#     print(item)

# if len(lst) > 10:
#     print('hi')
# elif len(lst) == 10:
#     print('hi')
# else:
#     print('hi')


# variable = 'test'

# x = lambda cash: cash * 100

# def x_func (cash):
#     return cash * 100

# print(x_func(10))

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_list = sum(filter(lambda number: number % 2 != 0, lst))

count = 0
for num in odd_list:
    count += num
print(count)