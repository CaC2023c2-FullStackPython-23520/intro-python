numeritos = [1,2,3,4]
nombres = ["juan", "pedro", "maria"]

los_dobles = list(map( lambda x : x * 2 ,numeritos))
print(los_dobles)

print(list(map(lambda nom : nom.upper(),nombres)))