# Overall set methods


'''set = {}  #if you give empty set then it will be in dict type
print(type(set)) 
set = {10,20,30,40}  #if you kept values in set it will be in set type only
print(type(set))'''


# in set process the output will get like no order guarenty and no duplicates allowed
a = {10,20,10,30,"vahid",True,False,'siddu','vk'}
#a.add(27)
#print(a)
#a.clear()
#print(a)
#a.copy()
#print(a)
a.update(range(1,10,1))
print(a)

'''b = {10,20,10,30,"vahid",True,False}
print(type(b))
print(a|b)  # OR symbol gives output as all elements
print(a&b)  # and symbol prints only common elements
print(a-b)  # - this symbol print only not having common elements
print(a^b)  # ^ this symbol print only not having common elements'''





