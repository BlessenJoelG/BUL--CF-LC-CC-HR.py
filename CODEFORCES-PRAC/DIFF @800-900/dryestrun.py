x_pass,y_pass,chk = set(),set(),set()
n = int(input())
for lvls in range(1,n+1):
      chk.add(lvls)
x_ip = list(map(int,input().split()))
y_ip = list(map(int,input().split()))
x_pass.update(x_ip[1:])
y_pass.update(y_ip[1:])
cooperate_pass = x_pass.union(y_pass)
if chk == cooperate_pass:
      print("I become the guy.")
else:
      print("oh, my keyboard!")