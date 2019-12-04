import sqlite3
# INSTANCIANDO BASE Y CURSOR#
conexion1 = sqlite3.connect("GestionProductos")

cursor=conexion1.cursor()

###########################
# CREATE #
'''
cursor.execute(
    CREATE TABLE PRODUCTOS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT, # SE INCREMENTA EL VALOR AUTOMATICAMENTE
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE, # UNIQUE PARA NO TEENER DATOS REPETIDOS
    PRECIO INTEGER,
    SECCION VARCHAR(20))
)

productos=[
    ("Pelota", 20, "Juguetes"),
    ("Pantalon", 15, "Confección"),
    ("Destornillador", 25, "Ferreteria"),
    ("Jarrón", 45, "Cerámica")
]
'''
# cursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

###########################
# READ #
# cursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='Juguetes'")

# productosC=cursor.fetchall()

#for producto in productosC:

#    print(producto)

###########################
# UPDATE #
# cursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='Pelota'")

###########################
# DELETE #
cursor.execute("DELETE FROM PRODUCTOS WHERE ID=4")

conexion1.commit()

conexion1.close()
