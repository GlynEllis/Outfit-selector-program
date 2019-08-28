#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

k = 10
num_list = [11,15,3,7]
new_list = []
current_num = 0

for item in num_list:
    current_num = item
    match_found = False
    new_list = num_list[:]
    new_list.remove(item)
    for items in new_list:
        if current_num + items == k:
            print('True')
            print(current_num,items)
            match_found = True
    if match_found == True:#We would want to break to avoid memory usage.
        break

        


