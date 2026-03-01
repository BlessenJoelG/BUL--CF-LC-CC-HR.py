yr = int(input())
yr_split = str(yr)
yr_split = list({yr_split[_] for _ in range(len(yr_split))})
yr_split.sort()
for x in range(yr+1,10001):
    dist_yr = str(x)
    dist_yr = list({dist_yr[_] for _ in range(len(dist_yr))})
    dist_yr.sort()
    if len(dist_yr)==4 and dist_yr!=yr_split:
        print(x)
        break
