t,food_items = int(input()),[]
for _ in range(t):
    n = int(input())
    food_items.extend(map(int,input().split()))
    print(food_items.count(max(food_items)))
    food_items.clear()
