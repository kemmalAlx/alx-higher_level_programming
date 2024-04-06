def safe_print_list(my_list = [], x = 0):
    try:
        len = 0
        for i, list in enumerate(my_list):
            if i < x:
                len+=1
                print(list, end="")
        print()
        return len
    except:
        return

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

