
print("Problem 4: Count multiples in list")
nums = [1,2,8,9,12,46,76,82,15,20,30]
result = {}
for d in range(1, 10):
    c = 0
    for n in nums:
        if n % d == 0:
            c += 1
    result[d] = c
print(result)