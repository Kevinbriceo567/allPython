import re

list_names=['Kevin Briceño',
'Willians Briceño',
'Ingrid Linares',
'Honorio Briceño']

print("\nLOS QUE COMIENZAN EN KEVIN")
for name in list_names:
    if re.findall('^Kevin', name): # LOS QUE COMIENZAN EN KEVIN

        print(name)

print("\nLOS QUE TERMINAN EN BRICEÑO")
for name in list_names:
    if re.findall('Briceño$', name): # LOS QUE TERMINAN EN BRICEÑO

        print(name)

print("\nCON Ñ")
for name in list_names:
    if re.findall('[ñ]', name): # LOS QUE CONTIENEN ñ

        print(name)

list_genre=['Mujer',
'Hombre',
'Niño',
'Niña']

print("\nCON NIÑO O NIÑA")
for genre in list_genre:
    if re.findall('Niñ[oa]', genre): # LOS QUE CONTIENEN ñ

        print(genre)