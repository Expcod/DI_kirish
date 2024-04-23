def hosil_qil_matritsa(rows, cols):
    matritsa = [[i * cols + j for j in range(cols)] for i in range(rows)]
    return matritsa

rows = 5
cols = 4
matritsa = hosil_qil_matritsa(rows, cols)
i = int(input())
j = int(input())
print("Indekslar (i, j) bilan qiymatlar:")
print(f"({i}, {j}): {matritsa[i][j]}")
