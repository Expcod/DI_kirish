# Abdumutalipov Shaxzodbek
massiv = [4,3,2,10,43,12,34]
min_qiymat,max_qiymat = min(massiv) , max(massiv)

min_index = massiv.index(min_qiymat)
max_index = massiv.index(max_qiymat)

massiv[min_index] , massiv[max_index] = massiv[max_index], massiv[min_index]

print(massiv)