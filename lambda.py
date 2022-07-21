#without lambda function
"""def calculate_cube_root(x):
    return x**(1/3)
print(calculate_cube_root(3))
"""


#with lambda function
"""cube_root=lambda x: x**(1/3)
print(cube_root(3))
"""



#without lambda function
"""
alphabets=["a","b","c","d","e","f"]
def check_alphabets(x):
    if x in alphabets:
     return True
    else:
     return False
print(check_alphabets("a"))
"""
#output
#True

#with lambda function
"""
alphabets=["a","b","c","d","e","f"]
check_alphabets=lambda x : true if x in alphabets else False
print(check_alphabets("z"))
"""
#output
#False
