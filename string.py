
## WAP to print the most repeated charecters in a given string??

s="tuushaar"
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
mx=max(d.values())
for j in d:
    if d[j]==mx:
        print(j)

