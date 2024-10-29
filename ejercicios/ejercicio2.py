import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect("EESTN5.db")
cursor = conn.cursor()

# Crear tabla alumnos
cursor.execute("""
CREATE TABLE IF NOT EXISTS alumnos (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    edad INTEGER
)
""")

alumnos_datos = [
    (1, "Alita", 18),
    (2, "Max", 17),
    (3, "Santi", 19),
    (4, "Ayrton", 20),
    (5, "Joaco", 16),
    (6, "Type", 18),
    (7, "Alsina", 21),
    (8, "Gadi", 17)
]

cursor.executemany("INSERT INTO alumnos VALUES (?, ?, ?)", alumnos_datos)
conn.commit()

cursor.execute("SELECT * FROM alumnos WHERE edad > 17")
resultados = cursor.fetchall()
for alumno in resultados:
    print(alumno)

conn.close()
