#este es un comentario de una sola linea
"""
este es un comentario
de multiple linea
"""
'''
este es un comentrio
de multiple linea

'''
#variables
nombre='kamata' #string
cantidadMaterias = 3 #integer
numeroDecimal=17.2 #float

diasSemana =['Lunes','Martes','Miercoles','Jueves','viernes'] #Listas=Array
listaDinamica=[0,'Hola',12.5,[0,1]]

print(diasSemana[2]) # miercoles
print(listaDinamica[3][1]) #1

esMayorEdad = False

#diccionarios - JSON - Object
persona = {
    'nombre': 'ice',
    'apellido': 'cube',
    'edad':16,
    'materia':['lenguaje de 4 generacion','bases de datos'],
}

print(persona['nombre'])
print(persona['materia'][1])
print(persona)

#lista de diccionarios
personas = [
    {
    'nombre': 'kamata',
    'apellido': 'ordoñez',
    'edad':16,
    'materia':['lenguaje de 4 generacion','bases de datos II'],
    },
    {
    'nombre': 'johana',
    'apellido': 'jajoy',
    'edad':19,
    'materia':['lenguaje orientado a objectos','bases de datos I'],
    },
    {
    'nombre': 'jeison',
    'apellido': 'calvache',
    'edad':25,
    'materia':['lenguaje orientado a eventos'],
    }
]

print(personas[2]['materia'][0]) #lenguaje orientado a eventos

#condicciones
esMayorEdad= True
if esMayorEdad:
    print('es mayor de edad')
    print('esto es del if')
else:
    print('no es mayor de edad')
    print('esto es parte del else')

print('mensaje de prueba')

for per in personas:
    print(per['nombre'])

#------------------------------------
verbo=input("ingrese un verbo a conjugar: \n")
letrafinal=verbo[len(verbo)-1]
letraAnteFinal=verbo[len(verbo)-2]
terminacion=letraAnteFinal+letrafinal
verboSinTerminacion=verbo.replace(terminacion,"")
#funciona con los verbos terminados en er
print("YO="+verboSinTerminacion+"o")
print("TU="+verboSinTerminacion+"es")
print("EL="+verboSinTerminacion+"e")
print("NOSOTROS="+verboSinTerminacion+"emos")
print("VOSOTROS="+verboSinTerminacion+"eis")
print("ELLOS="+verboSinTerminacion+"en")



