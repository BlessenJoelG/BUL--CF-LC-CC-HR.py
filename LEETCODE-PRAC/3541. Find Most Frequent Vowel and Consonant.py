wstring = input()
word = [wstring[_] for _ in range(len(wstring))]
v_frq,c_frq = [],[]
for _ in word:
    if _ in ["a","e","i","o","u"]:
        v_frq.append(word.count(_))
    else:
        c_frq.append(word.count(_))
if v_frq == []:
    v_frq.append(0)
if c_frq == []:
    c_frq.append(0)
c = max(v_frq)+max(c_frq)
print(c)