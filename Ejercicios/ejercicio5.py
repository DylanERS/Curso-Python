#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
#Después debe mostrar por pantalla la paga que le corresponde.

print("Escribe numero de horas trabajadas")
horasTrabajadas = input()
print("Escribe el costo de la hora")
costoHora = input()
paga = int(costoHora) * int(horasTrabajadas)

print("Se te debera pagar la cantidad de: $",paga)