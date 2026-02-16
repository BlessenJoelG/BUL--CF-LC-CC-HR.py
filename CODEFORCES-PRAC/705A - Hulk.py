n = int(input())
feel_str = str()
x = 1
while x <= n:
    if x == n:
        if x%2 != 0:
            feel_str = feel_str + "I hate it "
        elif x%2 ==0:
            feel_str = feel_str + "I love it "
    else:  
        if x%2!=0:
            feel_str = feel_str + "I hate that "
        else:
            feel_str = feel_str + "I love that "
    x = x+1
print(feel_str.strip())