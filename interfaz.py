import tkinter as tk
from tkinter import messagebox
import subprocess

def abrir_excel():
    # Ruta del archivo de Excel
    ruta_excel = r"G:\ReadWriteFile\ReadWriteFile\template\FORMATO-COVID.xlsx"
    # Mostrar mensaje de éxito
    resultado_label.configure(text="Archivo abierto: " + ruta_excel)
    # Actualizar la variable global con la ruta del archivo
    global ruta_excel_global
    ruta_excel_global = ruta_excel
    # Abrir el archivo de Excel
    abrir_archivo_excel(ruta_excel)

def abrir_archivo_excel(ruta_excel):
    try:
        subprocess.run(["start", ruta_excel], shell=True)
    except:
        resultado_label.configure(text="Error: No se pudo abrir el archivo de Excel.")

def enviar_numero():
    # Obtener el número ingresado en la interfaz
    numero = entrada_numero.get()
    # Ejecutar el backend de Go con el número y la ruta del archivo como argumentos
    ejecutar_backend(numero, ruta_excel_global)
    

def salir():
    if messagebox.askokcancel("Salir", "¿Estás seguro que deseas salir?"):
        ventana.destroy()

def ejecutar_backend(numero, ruta_excel):
    if not ruta_excel:
        resultado_label.configure(text="Error: No se ha seleccionado un archivo de Excel.")
        return

    # Ruta del archivo de backend de Go
    ruta_backend = "main.go"

    # Ejecutar el backend de Go con el número y la ruta del archivo como argumentos
    comando = ["go", "run", ruta_backend, numero, ruta_excel]
    resultado = subprocess.run(comando, capture_output=True, text=True)

    if resultado.returncode == 0:
        mensaje = "La fila se ha copiado y pegado correctamente en la hoja REG.ODONTOLOGIA."
    else:
        mensaje = "Ha ocurrido un error al copiar y pegar la fila en la hoja REG.ODONTOLOGIA."

    # Mostrar mensaje en la etiqueta
    resultado_label.configure(text=mensaje)

# Crear la ventana de la interfaz
ventana = tk.Tk()
ventana.title("ReadWriteFile")
ventana.geometry("400x300")  # Establecer dimensiones de la ventana

# Obtener las dimensiones de la pantalla
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana
x = (screen_width - 400) // 2  # Ajustar el ancho de la ventana si es necesario
y = (screen_height - 300) // 2  # Ajustar el alto de la ventana si es necesario

# Establecer la geometría de la ventana
ventana.geometry(f"400x300+{x}+{y}")

# Configurar estilos
ventana.configure(bg="#f2f2f2")  # Cambiar el color de fondo de la ventana

# Estilo de fuente
estilo_fuente = ("Arial", 12, "bold")

# Configurar estilo para etiquetas
estilo_etiqueta = {
    "bg": "#f2f2f2",
    "fg": "#333333",
    "font": estilo_fuente,
    "pady": 10,
    "bd": 0,  # Grosor del borde
    "highlightthickness": 0  # Grosor del resaltado del borde
}


# Crear una etiqueta y un campo de entrada para el número
etiqueta_numero = tk.Label(ventana, text="Ingrese el número:", **estilo_etiqueta)
etiqueta_numero.pack()

entrada_numero = tk.Entry(ventana, font=estilo_fuente)
entrada_numero.pack(pady=(0, 10))

# Configurar estilo para botones
estilo_boton = {
    "bg": "#4caf50",
    "fg": "white",
    "font": estilo_fuente,
    "width": 20,
    "pady": 8,
    "bd": 0,  # Grosor del borde
    "highlightthickness": 0,  # Grosor del resaltado del borde
    "activebackground": "#57c24f",  # Color de fondo al hacer clic
    "highlightcolor": "#57c24f"  # Color del resaltado al hacer clic
}

# Crear un botón para abrir el archivo de Excel
boton_abrir = tk.Button(ventana, text="Abrir Excel", command=abrir_excel, **estilo_boton)
boton_abrir.pack(pady=(0, 10))

# Crear un botón para enviar el número
boton_enviar = tk.Button(ventana, text="Enviar Número", command=enviar_numero, **estilo_boton)
boton_enviar.pack(pady=(0, 10))

# Crear un botón para salir
estilo_boton_salir = dict(estilo_boton)
estilo_boton_salir["bg"] = "#f44336"  # Cambiar el color de fondo del botón de salir

boton_salir = tk.Button(ventana, text="Salir", command=salir, **estilo_boton_salir)
boton_salir.pack(pady=(20, 10))

# Configurar estilo para la etiqueta de resultado
estilo_resultado = {
    "bg": "#f2f2f2",
    "fg": "#333333",
    "font": estilo_fuente,
    "pady": 10,
    "wraplength": 380  # Ancho máximo antes de envolver el texto
}

# Crear una etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="", **estilo_resultado)
resultado_label.pack()

# Variable global para almacenar la ruta del archivo de Excel
ruta_excel_global = r"G:\ReadWriteFile\ReadWriteFile\template\FORMATO-COVID.xlsx"

# Iniciar el bucle principal de la ventana
ventana.mainloop()