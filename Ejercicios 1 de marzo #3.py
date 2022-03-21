peso=input("¿Cuálestupesoenkg?")
estatura=input("¿Cuálestuestaturaenmetros?")
imc=round(float(peso)/float(estatura)**2,2)
print("Tuíndicedemasacorporales"+str(imc))