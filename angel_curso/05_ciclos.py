'''

1. Hacer un programa que imprima toda la lista

2. Hacer un programa que cuente cuantos perros y gatos hay en la lista
'''

mi_lista = [
    'perro',
    'hormiga',
    'gato',
    'abeja',
    'perro',
    'gato',
    'aguila',
    'gato',
    'cocodrilo',
    'gato',
    'conejo',
    'gato',
]

# 1.
for animalito in mi_lista:
    print( animalito )

# 2.
cont_perros = 0
cont_gatos  = 0

for animalito in mi_lista:

    if animalito == 'perro':
        cont_perros = cont_perros + 1

    elif animalito == 'gato':
        cont_gatos = cont_gatos + 1

print( 'numero de perros: ', cont_perros )
print( 'numero de gatos: ', cont_gatos )


