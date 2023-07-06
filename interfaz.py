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
ventana.title("Interfaz para abrir archivo de Excel")
ventana.geometry("400x300")  # Establecer dimensiones de la ventana

# Obtener las dimensiones de la pantalla
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana
x = (screen_width - 400) // 2  # Ajustar el ancho de la ventana si es necesario
y = (screen_height - 300) // 2  # Ajustar el alto de la ventana si es necesario

# Establecer la geometría de la ventana
ventana.geometry(f"400x300+{x}+{y}")

# Crear una etiqueta y un campo de entrada para el número
etiqueta_numero = tk.Label(ventana, text="Ingrese el número:")
etiqueta_numero.config(width=20)  # Ajustar el ancho de la etiqueta
etiqueta_numero.pack(anchor="center", pady=(40, 2))  # Agregar un padding vertical de 10 en la parte superior y 2 en la parte inferior

entrada_numero = tk.Entry(ventana)
entrada_numero.config(width=20)  # Ajustar el ancho del campo de entrada
entrada_numero.pack(anchor="center", pady=2)  # Agregar un padding vertical de 2 en la parte superior

# Crear un botón para abrir el archivo de Excel
boton_abrir = tk.Button(ventana, text="Abrir Excel", command=abrir_excel)
boton_abrir.config(width=20)  # Ajustar el ancho del botón
boton_abrir.pack(pady=(10, 2))  # Agregar un padding vertical de 10 en la parte superior y 2 en la parte inferior

# Crear un botón para enviar el número
boton_enviar = tk.Button(ventana, text="Enviar Número", command=enviar_numero)
boton_enviar.config(width=20)  # Ajustar el ancho del botón
boton_enviar.pack(pady=2)  # Agregar un padding vertical de 2 en la parte superior

# Crear un botón para salir
boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.pack(pady=(20,12))  # Agregar un padding vertical de 5 en la parte superior

# Crear una etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="")
resultado_label.config(width=50)  # Ajustar el ancho de la etiqueta
resultado_label.pack(anchor="center", pady=(5, 10))  # Agregar un padding vertical de 5 en la parte superior y 10 en la parte inferior

# Variable global para almacenar la ruta del archivo de Excel
ruta_excel_global = r"G:\ReadWriteFile\ReadWriteFile\template\FORMATO-COVID.xlsx"

# Iniciar el bucle principal de la ventana
ventana.mainloop()
