alumnos = ["Alita", "Max", "Santi", "Ayrton", "Joaco", "Type", "Alsina", "Gadi"]

notas = {
    "Alita": [6, 7, 6, 9, 8, 6],
    "Max": [9, 8, 7, 8, 9, 8],
    "Santi": [7, 6, 8, 7, 7, 8],
    "Ayrton": [8, 9, 9, 9, 7, 8],
    "Joaco": [9, 9, 8, 3, 8, 9],
    "Type": [6, 7, 7, 8, 9, 6],
    "Alsina": [8, 6, 9, 8, 6, 9],
    "Gadi": [7, 8, 9, 9, 4, 8]
}

for alumno, calificaciones in notas.items():
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"{alumno}: {promedio:.2f}")
