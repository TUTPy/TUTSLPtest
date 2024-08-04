# Problem 1

s = 'fullstackslp'

print(s[0])

print(s[-1])

print(s[4:9])

print(s[-3:])

print(s[7:10])

print(s[::-1])

# Problem 2
l = [3, 7, [5, [1, 4, 'hello']]]
l[2][1][2] = 'goodbye'
print(l)

# Problem 3
d1 = {'simple_key':'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 = {'k1':[{'knest_key':['this is deep',['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['knest_key'][1][0])

# Problem 4

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
unique_values = set(mylist)
print(unique_values)

# Problem 5
age = 45
name = "kyle"

print(f"Hello my dog's name is {name.capitalize()} and he looks {age} years old")