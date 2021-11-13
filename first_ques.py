"""Sort a given dictionary based on its value. Try to minimise the complexity."""

d = {'x':72, 'y': 67, 'z':88}
sorted_values = sorted(d.values()) # sorts values
sorted_dict = dict() # empty dict to store sorted dict
for i in sorted_values:
    for item in d:
        if d.get(item) == i:
            sorted_dict[item] = i

print(sorted_dict)