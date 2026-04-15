def missingNumber(nums):
    n = len(nums)
    esperado = n * (n + 1) // 2
    real = sum(nums)
    return esperado - real

print(missingNumber([9,6,4,2,3,5,7,0,1]))
