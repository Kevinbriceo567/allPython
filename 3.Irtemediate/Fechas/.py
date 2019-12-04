#ES NECESARIO IMPORTAR LAS DEPENDENCIAS NECESARIAS
from datetime import date
from datetime import datetime

# CREAR FECHA
new_date = datetime(2019, 2, 28, 10, 15, 00, 00000)

#Date
print("El día actual es {}".format(today.day))
print("El mes actual es {}".format(today.month))
print("El año actual es {}".format(today.year))


#MÉTODOS ÚTILES
print("El día actual es {}".format(now.day))
print("El mes actual es {}".format(now.month))
print("El año actual es {}".format(now.year))

print("La hora actual es {}".format(now.hour))
print("El minuto actual es {}".format(now.minute))
print("El segundo actual es {}".format(now.second))

#SUMAMOS DOS DÍAS A LA FECHA ACTUAL
now = datetime.now()
new_date = now + timedelta(days=2)
print(new_date)

#Comparación
if now < new_date:
    print("La fecha actual es menor que la nueva fecha")