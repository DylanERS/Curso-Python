#type(entero) devolveria int
entero = 23
print(type(entero))

#Se puede indicar que un numero se almacene como long añadiendo L al final
#type(entero) devolveria long
""" enteroL = 23L
print(type(enteroL)) """

#Se puede expresar como un octal anteponiendo un 0
#027 octal = 23 en base 10
""" enteroO = 027
print(enteroO)
print(type(enteroO)) """

#Se puede expresar como un hexadecimal anteponiendo un 0x
#0x17 hexadecimal = 23 en base 10
enteroH = 0x17
print(enteroH)
print(type(enteroH))

""" Para representar un número real en Python se escribe primero la parte entera, seguido 
de un punto y por último la parte decimal. """
real = 0.2703
print(real)
print(type(real))

""" También se puede utilizar notación científica, y añadir una e (de exponente) para
indicar un exponente en base 10. Por ejemplo: """
real = 0.1e-3
print(real)
print(type(real))

#Los números complejos en Python se representan de la siguiente forma:
complejo = 2.1 + 7.8j
print(complejo)
print(type(complejo))

#Operadores aritmeticos
#Suma (+)
r = 3 + 2
print(r)

#Resta (-)
r = 4 - 7
print(r)

#Negacion (-)
r = -7
print(r)

#Multiplicacion (*)
r = 2 * 6 
print(r)

#Exponente (**)
r = 2 ** 6
print(r)

#Division (/)
r = 3.5 / 2
print(r)

#Division entera (//)
r = 3.5 // 2
print(r)

#Modulo (%)
r = 7 % 2
print(r)