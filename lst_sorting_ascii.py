lst=['Anubhav','Zoya','venkatesh']
lst.sort(key=lambda x:sum([ord(i) for i in x])
print(lst)
