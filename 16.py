my_dict = {'c': [3], 'b': [12, 10], 'a': [19, 4]}

sorted_dict = {}

for k in sorted(my_dict):
    sorted_values = sorted(my_dict[k])
    sorted_dict[k] = sorted_values

print("Sorted dictionary:", sorted_dict)