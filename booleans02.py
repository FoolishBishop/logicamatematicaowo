# trabajaremos especificamente con booleans
# que son los booleans?
# es la forma de referirse al True/False, verdadero/falso
# con booleans podemos hacer muchas cosas, hablaremos del and, or, not


# *** NOT ***
# es el equivalente a " - ", no hay mucha explicacion
# not True --> False
# not False --> True
#   Ejemplo:
print(not False)
# >>> True


# *** AND ***
# este seria el equivalente a conjuncion, para que sea verdadero dos o mas deben ser verdaderos
#   Ejemplo:
var1 = True
var2 = True
var3 = False
print(var1 and var2 and var3)  # <--- muestra el resultado de la conjuncion de estos
# >>> False
# como uno es falso, da falso como resultado. Si todos fueran verdaderos daria verdadero
# nota: se puede poner dos, o mas. No hay limite en general


# *** OR ***
# disyuncion inclusiva uno o mas debe ser verdadero para que salga verdadero
#   Ejemplo:
var4 = True
var5 = False
resultado = var4 or var5  # <--- tambien podemos guardar resultados en otra variable (o en una misma)
print(resultado)
# >>> True


# Bonus:
# podemos poner en parentesis para prioridad y dar mejores resultados. El programa lee de izquiera a derecha.
#   Ejemplo:
resultado2 = (True and False) or (True and True)
# ^^^ obviamente no vamos a escribir asi, pero puse asi para no confundir con mas variables
print(resultado2)
# >>> True

print("----\n EJERCICIO")  # <--- ignorar
# ****** EJERCICO ******
# guardar en una variable el resultado de -((PvQ)^-R)vN y despues mostrarlo en pantalla
# pueden reemplazar las letras por otros nombres, pero hay que tomar en cuenta que
#   P es falso
#   Q es verdadero
#   R es falso
#   N es verdadero
