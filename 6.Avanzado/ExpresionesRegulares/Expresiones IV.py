import re

nombre1 = "Sandra Lopez"

nombre2 = "Maria Jesus"

nombre3 = "Hugo Savinovich"

nombre4 = "Lara Savinovich"

if re.match("Sandra", nombre1, re.IGNORECASE):

    print("Nombre Sandra encontrado en variable")

if re.match(".ara", nombre4, re.IGNORECASE):

    print("Final con ara encontrado en variable", nombre4)

if re.search("ria", nombre2, re.IGNORECASE):

    print("Letras aria encontradas en variable", nombre2)

    