x=0
n = int(input())
if(n==1):
    print(1)
elif(2<=n<=150):
    split = n/2
    if(n%2==0):
        for i in range(int(split)):
            x = x+1
        for i in range(int(split)):
            x = x-1
    elif(n%2!=0):
        for i in range(int(split)):
            x = x+1
        for i in range(int(split+1)):
            x = x-1
print(x)