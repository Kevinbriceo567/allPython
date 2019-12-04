import re

nombres = ["Kevin", "Pedro", "Xavier"]

for nombre in nombres: # RANGO DE LETRAS DESDE O HASTA T

    if re.findall('[o-t]', nombre):
        
        print(nombre)
    
# PEDIDOS

pedidos = ["Stgo1", "ConceA", "SereB", "Stgo2", "StgoA"]

for pedido in pedidos: # DOBLE RANGO DE PEDIDOS CON NUMEROS Y LETRAS

    if re.findall('Stgo[0-3A-B]', pedido):
        
        print(pedido)
    
