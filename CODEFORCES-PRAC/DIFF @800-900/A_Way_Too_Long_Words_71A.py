n = int(input())
str = []
for i in range(n):
    str.append(input())
print(str)
for i in str:
    if(len(i)>=10):
        mid = len(i)
        print(i[0]+str(mid-2)+i[-1])
    else:
        print(i)