positivos=0
sumatoria=0
n=int(input("Número (0 para terminar): "))
while n!=0:
    if n>0:
        positivos+=1
    sumatoria+=n
    n=int(input("Número (0 para terminar): "))
print("La sumatoria de los positivos es:", sumatoria)
