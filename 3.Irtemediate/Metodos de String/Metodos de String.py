# STRING NOMBRE #
userName=input("User name --> ") # INGRESAMOS STRING NORMAL

print("El nombre es: ", userName.upper()) # LLEVA STRING A MAYUSCULAS

print("El nombre es: ", userName.lower()) # LLEVA STRING A MINUSCULAS

print("El nombre es: ", userName.capitalize()) # LLEVA PRIMERA LETRA A MAYUSCULA

print("El nombre es: ", userName.title()) # FORMATO DE TÍTULO

print("El nombre es: ", userName.swapcase()) # INICIALES EN MINUSCULA
#########################################################################

# STRING EDAD #
userAge=input("\nUser age --> ")

print(userAge.isdigit()) # COMPRUEBA SI ES DIGITO (TRUE O FALSE)

while(userAge.isdigit()==False): # COMPROBAMOS QUE ES VALOR NUMÉRICO

    print("Introduce valor numerico!")

    userAge=input("\nUser age --> ")

if (int(userAge)<18): # COMPROBAMOS SI ES MAYOR DE EDAD
    print("Puedes pasar")

else:
    print("No puedes pasar")

#########################################################################

cadena = "\nHola Mundo Desde Python 1313 "
print ( cadena.isalnum())# revisa si todos son n´u meros , isdecimal () , isdigit () o isnumeric
print ( cadena.isalpha())# revisa si todos son letras
print ( cadena.istitle())# revisa si las palabras como title
print ( cadena.isupper())# revisa si las palabras est ´an en may ´u sculas
print ( cadena.islower())# revisa si las palabras est ´an en min ´u sculas
print ( cadena.isspace())# revisa si el string es un espacio