from datetime import date
from Datos import diccionario
from Biblioteca import obtener_colaboradores, obtener_nombre_tema, convertir_vistas_numerico, convertir_duracion_numerico, obtener_codigo, formatear_fecha

def main():
    colaboradores = obtener_colaboradores(diccionario["Tema"])
    titulo = obtener_nombre_tema(diccionario["Tema"])
    numero_vistas = convertir_vistas_numerico(diccionario["Vistas"])
    duracion_en_segundos = convertir_duracion_numerico(diccionario["Duración"])
    codigo_url = obtener_codigo(diccionario["Link"])
    fecha_date = formatear_fecha(diccionario["Fecha de Lanzamiento"])

    print(f"""
    🎵 INFORMACIÓN DEL TEMA 🎵
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    🎤 Título: {titulo}
    👩‍🎤 Artista: Lady Gaga
    🤝 Colaboradores: {colaboradores}
    📅 Fecha de estreno: {fecha_date}
    👀 Vistas: {numero_vistas:,} 
    ⏱️  Duración: {duracion_en_segundos} segundos
    🔗 Código YouTube: {codigo_url}

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

if __name__ == "__main__":
    main()