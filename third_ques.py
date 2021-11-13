'''Given a list of dictionaries, try to sort the dictionary based on values.

Example-
Input- [{1:4,2:6,9:5},{2:3,4:6,3:8},{6:0,9:11,3:1}]

Output: [{6:0,9:11,3:1},{2:3,4:6,3:8},{1:4,2:6,9:5}]
Explanation- as third dictionary has maximum value 11 so it comes first, then second dictionary
with value 8 and last dictionary with value 6.'''

l2=[{1:4,2:6,9:5},{2:3,4:6,3:8},{6:0,9:11,3:1}]
l2.sort(reverse = False)
print(l2) 