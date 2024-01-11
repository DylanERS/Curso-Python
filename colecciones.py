#Listas

#La lista es un tipo de colección ordenada. Sería equivalente a lo que en otros 
#lenguajes se conoce por arrays, o vectores.
#Las listas pueden contener cualquier tipo de dato: números, cadenas, booleanos, … y
#también listas.
l = [22, True, "una lista", [1, 2]]
print(l)

#Podemos acceder a cada uno de los elementos de la lista escribiendo el nombre de la
#lista e indicando el índice del elemento entre corchetes.
l = [11, False]
mi_var = l[0] # mi_var vale 11
print(mi_var)

#Si queremos acceder a un elemento de una lista incluida dentro de otra lista
#tendremos que utilizar dos veces este operador
l = ["una lista", [1, 2]]
mi_var = l[1][0] # mi_var vale 1
print(mi_var)

#También podemos utilizar este operador para modificar un elemento de la lista si lo
#colocamos en la parte izquierda de una asignación:
l = [22, True]
print(l)
l[0] = 99 # Con esto l valdrá [99, True]
print(l)

#Si
#en lugar de un número escribimos dos números inicio y fin separados por dos
#puntos (inicio:fin) Python interpretará que queremos una lista que vaya desde la
#posición inicio a la posición fin, sin incluir este último. Si escribimos tres números
#(inicio:fin:salto) en lugar de dos, el tercero se utiliza para determinar cada
#cuantas posiciones añadir un elemento a la lista
l = [99, True, "una lista", [1, 2]]
print(l)
mi_var = l[0:2] # mi_var vale [99, True]
print(mi_var)
mi_var = l[0:4:2] # mi_var vale [99, “una lista”]
print(mi_var)

#Hay que mencionar así mismo que no es necesario indicar el principio y el final del
#slicing, sino que, si estos se omiten, se usarán por defecto las posiciones de inicio y
#fin de la lista, respectivamente:
l = [99, True, "una lista"]
print(l)
mi_var = l[1:] # mi_var vale [True, “una lista”]
print(mi_var)
mi_var = l[:2] # mi_var vale [99, True]
print(mi_var)
mi_var = l[:] # mi_var vale [99, True, “una lista”]
print(mi_var)
mi_var = l[::2] # mi_var vale [99, “una lista”]
print(mi_var)

#También podemos utilizar este mecanismo para modificar la lista:
l = [99, True, "una lista", [1, 2]]
print(l)
l[0:2] = [0, 1] # l vale [0, 1, “una lista”, [1, 2]]
print(l)

#pudiendo incluso modificar el tamaño de la lista si la lista de la parte derecha de la
#asignación tiene un tamaño menor o mayor que el de la selección de la parte
#izquierda de la asignación
l[0:2] = [False] # l vale [False, “una lista”, [1, 2]]
print(l)

#Tuplas

#Todo lo que hemos explicado sobre las listas se aplica también a las tuplas, a
#excepción de la forma de definirla, para lo que se utilizan paréntesis en lugar de
#corchetes.
t = (1, 2, True, "python")
print(t)
print(type(t))

#Para referirnos a elementos de una tupla, como en una lista, se usa el operador []:
mi_var = t[0] # mi_var es 1
print(mi_var)
mi_var = t[0:2] # mi_var es (1, 2)
print(mi_var)

#Volviendo al tema de las tuplas, su diferencia con las listas estriba en que las tuplas
#no poseen estos mecanismos de modificación a través de funciones tan útiles de los
#que hablábamos al final de la anterior sección.
#Además son inmutables, es decir, sus valores no se pueden modificar una vez creada;
#y tienen un tamaño fijo.

#Diccionarios

#Los diccionarios, también llamados matrices asociativas, deben su nombre a que son
#colecciones que relacionan una clave y un valor
d = {"Love Actually" : "Richard Curtis",
"Kill Bill": "Tarantino",
"Amélie": "Jean-Pierre Jeunet"}
print(d)
print(type(d))

#La diferencia principal entre los diccionarios y las listas o las tuplas es que a los
#valores almacenados en un diccionario se les accede no por su índice, porque de
#hecho no tienen orden, sino por su clave, utilizando de nuevo el operador [].
print(d["Love Actually"]) # devuelve “Richard Curtis”

#Al igual que en listas y tuplas también se puede utilizar este operador para reasignar
#valores.
d["Kill Bill"] = "Quentin Tarantino"
print(d)

