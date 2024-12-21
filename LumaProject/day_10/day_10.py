#
# #  Закодовані дані
# name = "Jon"
# password = "password123"
#
# #  Запит у користувача
# input_name = input("Your name: ")
# input_password = input("Your password: ")
#
# #  Перевірка введених даних
# # if input_name == name:
# #     if input_password == password:
# #         print("Access granted")
#
# if input_name == name and input_password == password:
#     print("Access granted")
# else:
#     print("Access denied")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

par_list = []
not_par_list = []
three_par_list = []

for num in my_list:
    if num % 2 == 0:
        par_list.append(num)
    elif num % 3 == 0:
        three_par_list.append(num)
    else:
        not_par_list.append(num)

print(par_list)
print(not_par_list)
print(three_par_list)