calificaciones = []

while True:
    calificacion = input("Ingresa una calificación (o 'fin' para terminar): ")
    if calificacion.lower() == 'fin':
        break
    try:
        calificaciones.append(float(calificacion))
    except ValueError:
        print("Por favor, ingresa un número válido.")

if calificaciones:
    calificacion_max = max(calificaciones)
    calificacion_min = min(calificaciones)
    promedio = sum(calificaciones) / len(calificaciones)

    print(f"Calificación más alta: {calificacion_max}")
    print(f"Calificación más baja: {calificacion_min}")
    print(f"Promedio de calificaciones: {promedio:.2f}")
else:
    print("No se ingresaron calificaciones.")
