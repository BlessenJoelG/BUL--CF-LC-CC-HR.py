num = []
fsum = []
ran_som = input()
num = ran_som.split("+")
num.sort()
fsum = num[0]
for x in range(len(num)-1):
    fsum = fsum+"+"+num[x+1]
print(fsum)