'''Given a list of dictionaries, try to sort the dictionary based on values.

Example-
Input- [{1:4,2:6,9:5},{2:3,4:6,3:8},{6:0,9:11,3:1}]

Output: [{6:0,9:11,3:1},{2:3,4:6,3:8},{1:4,2:6,9:5}]
Explanation- as third dictionary has maximum value 11 so it comes first, then second dictionary
with value 8 and last dictionary with value 6.'''

l2=[{1:4,2:6,9:5},{2:3,4:6,3:8},{6:0,9:11,3:1}]
max_list = list()
for i in l2:    # loop to find max value from each dictionary
    max_list.append(max(list(i.values())))
max_list.sort(reverse=True) # sort max values of each dict to descending order
solution = []
inserted_value = list()
for i in max_list:
    for j in l2:
        if i in list(j.values()):   
            if not inserted_value:  # if value unique
                solution.append(j)
            elif i not in inserted_value:
                solution.append(j)
            inserted_value.append(i)
print(solution)
