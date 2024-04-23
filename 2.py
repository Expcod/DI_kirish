# Abdumutalipov Shaxzodbek
A = [5, 2, 8, 3, 1, 9, 4, 6, 7]

n=len(A)

juft_yigindi = sum(A[i] for i in range(0, n, 2))
toq_yigindi = sum(A[i] for i in range(1, n, 2))
    

print("Juft indeksli elementlar yig'indisi:", juft_yigindi)
print("Toq indeksli elementlar yig'indisi:", toq_yigindi)


