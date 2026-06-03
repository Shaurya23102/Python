hash = [0]*11
n = [1,2,3,4,4,5,5,6,5,5,5,8]
m = [1,3,2,4,5,8,10]
for num in n:
    hash[num]+=1
for num in m:
    if num < 1 or num > 10:
        print("0")
    else:
        print(hash[num])
print(hash)
