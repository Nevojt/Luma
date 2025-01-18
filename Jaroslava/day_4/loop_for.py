mylist = [2, 4, 5, 6, 89, 99, 2, 4, 5, 6, 89, 99, 2, 4, 5, 6, 89, 99, 2, 4, 5, 6, 89, 99]

print(mylist)
# print(len(mylist))
#
# count = 0
# for i in mylist:
#     # print(i)
#     # count = count + 1
#     count += 1
#     # print("Iter: ", count)
#
# print("Count elements mylist: ", count)

for i in mylist:
    # if i % 2 == 0:
    #     print(i)
    if i % 3 == 1:
        print("Divide on 3 == 1 ",i)
    elif i % 3 == 2:
        print("Divide on 3 == 2 ", i)
    else:
        print("Last elements", i)


    # if i % 2 != 0:
    #     print(i)
