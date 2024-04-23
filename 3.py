#Abdumutalipov Shaxzodbek
import random

def random_massiv(N, start, end):
    A = [random.randint(start, end) for _ in range(N)]
    return A

N = int(input())

start = 1996
end = 2023

A = random_massiv(N, start, end)

print("Hosil qilingan massiv:")
print(A)
