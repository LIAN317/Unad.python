# ==========================================
# PROBLEMA 5: Control de Horas Semanales
# autoria propia
# nombre estudante: Anderosn Julian Vargas Valero
# 
# ==========================================

# 1. Definición de la matriz de datos
matriz_horas = [
    ["Antonia Gómez", 8, 9, 8, 9, 9],       # 43 horas -> Sobretiempo
    ["Carolina Pérez", 8, 7, 7, 8, 8],    # 38 horas -> Horario Estándar
    ["Miriam López", 9, 11, 8, 9, 9],    # 46 horas -> Sobretiempo
    ["Jhon Torres", 8, 8, 8, 8, 8]      # 40 horas -> Horario Estándar
]

# 2. Módulo / Función para procesar los datos de cada recurso
def procesar_jornada(fila_recurso):
    nombre = fila_recurso[0]
    # Extrae solo los valores numéricos de las horas
    horas_diarias = fila_recurso[1:]
    total_horas = sum(horas_diarias)
    
    # Lógica de negocio (Umbral de 40 horas)
    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"
        
    return nombre, total_horas, clasificacion

# 3. Salida de datos (Impresión de resultados)
print(f"{'Recurso':<16} | {'Horas Semanales':<16} | {'Clasificación'}")
print("-" * 52)

for recurso in matriz_horas:
    nombre, total, tipo_jornada = procesar_jornada(recurso)
    print(f"{nombre:<16} | {total:<16} | {tipo_jornada}")