#write a program to remove duplicate from the string
s='aaaabbbccd'
l1=[]

for i in s:
    if i not in l1:
        l1.append(i)
output=''.join(l1)
print(output)
        
        