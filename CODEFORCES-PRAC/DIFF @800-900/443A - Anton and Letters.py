alpha,alphia  = input(),set()
list_alpha = list(alpha)
for _ in list_alpha:
    if "a"<= _ <= "z":
        alphia.add(_) 
print(len(alphia))