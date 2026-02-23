tokenizer,idx_op = [],[]
for _ in range(len(words)):
    for y in words[_]:
        tokenizer.append(y)
    if x in tokenizer:
        idx_op.append(_)
    tokenizer.clear()
return idx_op
# words = ["abc","bcd","aaaa","cbc"], x = "a"