
numeros=[10,15,25,85,12,-85,-85,12,35,36,38,105]

par=[]
impar=[]

for i in numeros:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f"Los numeros pares son: {par}")
print(f"Los numeros impares son: {impar}")

print (par+impar)
