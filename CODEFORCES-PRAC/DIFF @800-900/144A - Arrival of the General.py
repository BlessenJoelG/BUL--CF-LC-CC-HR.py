n, soliders_parad = int(input()), []
swap = 0
soliders_parad.extend(map(int, input().split()))
max_val = max(soliders_parad)
initial_idx_max = soliders_parad.index(max_val)   
swap = swap + initial_idx_max
min_val = min(soliders_parad)
updated_idx = len(soliders_parad) - 1 - soliders_parad[::-1].index(min_val)
swap = swap + (len(soliders_parad) - 1 - updated_idx)
if initial_idx_max > updated_idx:
    swap -= 1
print(swap)
