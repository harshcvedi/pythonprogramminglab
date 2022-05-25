n = 4
filename = 'code.py'
with open(filename) as my_file:
    head = [next(my_file) for x in range(n)]
    
print(head)
