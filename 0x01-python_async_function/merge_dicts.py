#how to merege two dicts
#using **kwargs in python function
def merge_dict(**kwargs):
    print(kwargs)
    return kwargs

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
merged_dict = merge_dict(**d1, **d2)
print("Merged Dict: ", merged_dict)

#output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

x = {"e": 5, "f": 7}
y ={"g": 9, "h": 11}
z = {**x, **y} #merge two dicts using ** operator
print("Z Dict: ", z)

#output: Z Dict: {'e': 5, 'f': 7, 'g': 9, 'h': 11}

#checking if a key is present in a dict or not.
key_present = "a" in d1
if key_present :
    print("Key is present in d1")
else:
    print("Key is not present in d1")
    
#output: Key is present in d1

#access the value of a particular key from a dict
value = d1["a"]
print("Value of a: ", value)
#output: Value of a:  1

