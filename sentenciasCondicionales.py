#if
fav = "mundogeek.net"
print(fav)
# si (if) fav es igual a “mundogeek.net”
if fav == "mundogeek.net":
    print ("Tienes buen gusto!")
    print ("Gracias")

if fav == "mundogeek.net":
    print ("Tienes buen gusto!")
print ("Gracias")

#if... else
if fav == "mundogeek.net":
    print ("Tienes buen gusto!")
    print ("Gracias")
else:
    print ("Vaya, que lástima")

#if … elif … elif … else
numero = -2
print(numero)
if numero < 0:
    print ("Negativo")
elif numero > 0:
    print ("Positivo")
else:
    print ("Cero")

#A if C else B
#También existe una construcción similar al operador ? de otros lenguajes, que no es
#más que una forma compacta de expresar un if else
num = 4
print(num)
var = "par" if (num % 2 == 0) else "impar"
print(var)