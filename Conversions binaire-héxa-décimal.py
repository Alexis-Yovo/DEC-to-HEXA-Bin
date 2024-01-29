print("Écrire un programme pour convertir d'un décimal à une base")
decimal=input("Saisir la valeur décimale:")
decimal=int(decimal)
base=input("Saisir la base:")
base=int(base)
if base==2:
    print(bin(decimal)[2:])
elif base==16:
    print(hex(decimal))
