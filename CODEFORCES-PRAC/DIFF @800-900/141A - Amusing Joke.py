G_name,H_name,P_name,chk1,chk2= input(),input(),input(),[],[]
for _ in range(0,len(G_name)):
    chk1.append(G_name[_])
for _ in range(0,len(H_name)):
    chk1.append(H_name[_])
chk1.sort()
for _ in range(0,len(P_name)):
    chk2.append(P_name[_])
chk2.sort()
if chk1 == chk2:
    print("YES")
else:
    print("NO")