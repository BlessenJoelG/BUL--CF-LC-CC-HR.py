t = int(input())
for _ in range(t):
    W = input()
    if W == "us":
        print("i")
    else:
        print(W[0:len(W)-2]+"i")