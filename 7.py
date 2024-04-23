#Abdumutalipov Shaxzodbek
def qurilma_tugmachalar_soni(X, Y):
    tugmachalar_soni = 0
    x = X
    
    while x != Y:
        tugmachalar_soni += 1
        if x % 2 == 1:
            x -= 1
        else:
            x //= 2
    
    return tugmachalar_soni

X = 9
Y = 16
tugmachalar_soni = qurilma_tugmachalar_soni(X, Y)
print("Qurilma tugmachalar soni:", tugmachalar_soni)
