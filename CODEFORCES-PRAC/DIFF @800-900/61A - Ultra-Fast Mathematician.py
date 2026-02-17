chck = str()
x,y = input(),input()
for _ in range(len(x)):
    if x[_]!=y[_]:
        chck = chck + str(1)
    else:
        chck = chck + str(0)
print(chck)