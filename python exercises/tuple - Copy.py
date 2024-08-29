#finding max number in tuple

a=(1,2,3)

for i in range(len(a)):  #iterating through tuple
    max=a[0]           
    if(a[i]>max):         #checking the condition
        max=a[i]
print(max)

