from Datos import diccionario
from datetime import date

def obtener_colaboradores(titulo: str) -> list:
    colaboradores = titulo.split("-")[0]
    prelista_colab = colaboradores.split("|")
    lista_colab = []  
    for i in prelista_colab:
        lista_colab += [(i.strip())] 
    return lista_colab

def obtener_nombre_tema(titulo: str) -> str:
    pretema = titulo.split("-")
    tema = pretema[1]
    return tema

def convertir_vistas_numerico(vistas: str) -> int:
    numero_vistas_str = ""
    for i in vistas:
        if i.isdecimal():
            numero_vistas_str += i
    numero_vistas_entero = int(numero_vistas_str)
    numero_vistas =  numero_vistas_entero * 1000000
    return numero_vistas

def convertir_duracion_numerico(duracion: str) -> int:
    tiempo_separado = duracion.split(":")
    minutos = int(tiempo_separado[0])
    segundos = int(tiempo_separado[1])
    tiempo_total_segundos = (minutos * 60) + segundos

    return tiempo_total_segundos

def obtener_codigo(url: str) -> str:
    preurl = url.split("=")
    link = preurl[1]
    return link

def formatear_fecha(fecha: str) -> date:
    separador = "/"
    prefecha = fecha.split("-")
    anio = prefecha[0]
    mes = prefecha[1]
    dia = prefecha[2]
    lanzamiento = fecha = separador.join([dia, mes, anio])
    return lanzamiento

