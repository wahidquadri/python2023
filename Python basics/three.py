# for loop Process

sizes = ['s','m','l','xl','xxl']
for x in sizes:
    print(x)

# while loop Process
    
sizes = ['s','m','l','xl','xxl'] 
i=0
while(i<=4):
    print(sizes[i])
    i=i+1 

# from above while loop method if we dont know the length this process is to be used
sizes = ['s','m','l','xl','xxl'] 
sizes[0]='WWW'
i=0
while(i<=len(sizes)-1):
    print(sizes[i])
    i=i+1

