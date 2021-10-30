from random import *

def find_missing_nums(nums):
    n = int(input("Введите длину списка: "))
    for i in range(n):
        nums.append(randint(1, n))
    print("Изначальный список:", nums)
    notfill = []
    for _ in range(1, n):
        if _ not in nums:
            notfill.append(_)

    return (notfill)

print("Список отсутствующих чисел:", find_missing_nums([]))
