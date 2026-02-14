have_to_buy_shoes = 4
had_shoes = set()
had_shoes.update(map(int,input().rstrip().split()))
print((have_to_buy_shoes)-(len(had_shoes)))