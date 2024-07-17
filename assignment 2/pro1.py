def swap_first_last(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

my_list = [12, 35, 9, 56, 24]
result = swap_first_last(my_list)
print(result)
