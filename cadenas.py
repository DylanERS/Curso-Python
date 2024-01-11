unicode = u"äóè"
raw = r"\n"
print (unicode)
print(raw)

#También es posible encerrar una cadena entre triples comillas (simples o dobles). De
#esta forma podremos escribir el texto en varias líneas, y al imprimir la cadena, se
#respetarán los saltos de línea
triple = """primera linea
esto se vera en otra linea"""
print(triple)

a = "uno"
b = "dos"
print(a , b)

#(+) Funciona realizando una concatenación de las cadenas
c = a + b # c es "unodos"
print(c)

#(*) Se repite la cadena tantas veces como lo indique el número utilizado como segundo operando
c = a * 3 # c es "unounouno"
print(c)
