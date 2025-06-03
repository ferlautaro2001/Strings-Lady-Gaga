# 🎵 Análisis de Lista de Reproducción - Lady Gaga

## 📝 Descripción
Proyecto desarrollado para procesar y normalizar datos de canciones de Lady Gaga, aplicando conceptos fundamentales de **manipulación de cadenas** y **programación modular** en Python.

## 🎯 Objetivo
Crear funciones especializadas para extraer, convertir y formatear información musical desde datos en formato texto a tipos de datos apropiados para análisis posterior.

## 📊 Datos de Entrada
```python
diccionario = {
    "Tema": "Bradley Cooper | Lukas Nelson - Shallow",
    "Vistas": "1900 millones",
    "Duración": "3:37",
    "Link": "https://www.youtube.com/watch?v=bo_efYhYU2A",
    "Fecha de Lanzamiento": "2018-09-27"
}
```

## 🚀 Funciones Implementadas

### 🔹 `obtener_colaboradores(titulo: str) -> list`
Extrae colaboradores del título del tema.
- **Entrada:** `"Bradley Cooper | Lukas Nelson - Shallow"`
- **Salida:** `["Bradley Cooper", "Lukas Nelson"]`

### 🔹 `obtener_nombre_tema(titulo: str) -> str`
Obtiene el nombre real del tema eliminando colaboradores.
- **Entrada:** `"Bradley Cooper | Lukas Nelson - Shallow"`
- **Salida:** `"Shallow"`

### 🔹 `convertir_vistas_numerico(vistas: str) -> int`
Convierte vistas textuales a número entero.
- **Entrada:** `"1900 millones"`
- **Salida:** `1900000000`

### 🔹 `convertir_duracion_numerico(duracion: str) -> int`
Transforma duración MM:SS a segundos totales.
- **Entrada:** `"3:37"`
- **Salida:** `217` segundos

### 🔹 `obtener_codigo(url: str) -> str`
Extrae código único de video de YouTube.
- **Entrada:** `"https://www.youtube.com/watch?v=bo_efYhYU2A"`
- **Salida:** `"bo_efYhYU2A"`

### 🔹 `formatear_fecha(fecha: str) -> str`
Reformatea fecha de YYYY-MM-DD a DD/MM/YYYY.
- **Entrada:** `"2018-09-27"`
- **Salida:** `"27/09/2018"`

## 💻 Estructura del Proyecto
```
proyecto/
├── main.py           # Programa principal
├── Biblioteca.py     # Funciones de procesamiento
├── Datos.py          # Diccionario con información
└── README.md         # Documentación
```

## 🎨 Salida del Programa
```
🎵 INFORMACIÓN DEL TEMA 🎵
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎤 Título: Shallow
👩‍🎤 Artista: Lady Gaga
🤝 Colaboradores: ['Bradley Cooper', 'Lukas Nelson']
📅 Fecha de estreno: 27/09/2018
👀 Vistas: 1,900,000,000 
⏱️  Duración: 217 segundos
🔗 Código YouTube: bo_efYhYU2A

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 🛠️ Conceptos Aplicados

### 📚 Manipulación de Cadenas
- **`.split()`** - Separación por delimitadores
- **`.strip()`** - Eliminación de espacios
- **`.join()`** - Unión de elementos
- **`.isdecimal()`** - Validación numérica

### 🏗️ Programación Modular
- Separación de responsabilidades
- Funciones con propósito específico
- Importación entre módulos
- Tipado de parámetros y retorno

### 🔄 Estructuras de Control
- Bucles `for` para iteración
- Condicionales `if` para validación
- Manipulación de listas y diccionarios

### 📅 Manejo de Datos
- Conversión de tipos de datos
- Procesamiento de formatos temporales
- Extracción de información específica

## 🚀 Ejecución
```bash
python main.py
```

## 📋 Requisitos
- Python 3.7+
- Módulo `datetime` (incluido en Python)

## 👨‍💻 Autor
Desarrollado como práctica de **Programación I** - UTN
