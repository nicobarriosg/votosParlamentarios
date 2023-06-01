votoApruebo = 0
votoRechazo = 0
votoAbstencion = 0
p = int(input("Ingrese el numero de parlamentarios: "))
for i in range(p):
    voto = input("¿Cual fue su voto A=Apruebo R=Rechazo B=Abstencion? ").upper()
    if voto == "A":
        votoApruebo += 1
    elif voto == "R":
        votoRechazo += 1
    else:
        votoAbstencion += 1

porcentajeA = int((votoApruebo / p) * 100)
porcentajeR = int((votoRechazo / p) * 100)
porcentajeB = int((votoAbstencion / p) * 100)

tercio = 0
if votoApruebo >= (p / 3):
    tercio = "Aprobada"
else:
    tercio = "Rechazada"



print("Parlamentarios que votaron Apruebo: {} que equivale al %{}".format(votoApruebo, porcentajeA))
print("Parlamentarios que votaron Rechazo: {} que equivale al %{}".format(votoRechazo, porcentajeR))
print("Parlamentarios que votaron Abstecion: {} que equivale al %{}".format(votoAbstencion, porcentajeB))
print("La medida fue {}".format(tercio))

