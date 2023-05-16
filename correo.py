from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

# VARIABLES
# ========================================== #

color1 = "#e3e3e3"
color2 = "#c7c7c7"
color3 = "#d94848"
fuenteActual = "Calibri"
tamanoActual = 11

# FUNCIONES
# ========================================== #

def cambiarTema():
    ventana.config(bg="black")

def CambiarFuente(fuente=fuenteActual):
    # Obtencion de Variables
    global tamanoActual, fuenteActual
    fuenteActual = fuenteMensaje.get()
    tamanoActual = tamano.get()

    # Modificacion a interfaz
    mensajeArea.config(font = (fuenteActual, int(tamanoActual)))

def enviar():
    # Obtencion de variables
    de = entradaDe.get()
    para = entradaPara.get()
    cc = entradaCC.get()
    mensaje = mensajeArea.get("1.0",'end-1c')
    
    # Validaciones
    if de == "":
        messagebox.showerror(title="Error", message='"De:" no puede estar vacio')
        pass
    if para == "":
        messagebox.showerror(title="Error", message='"Para:" no puede estar vacio')
        pass

    # Escritura
    archivo = open("enviados.txt", "a", encoding="utf-8")
    archivo.write("De: {}\n".format(de))
    archivo.write("Para: {}\n".format(para))
    archivo.write("CC: {}\n".format(cc))
    archivo.write("Mensaje: {}\n\n".format(mensaje))
    archivo.close()
    messagebox.showinfo(title="Exito", message='El mensaje se ha enviado correctamente')


def guardarBorrador():
    # Obtencion de variables
    de = entradaDe.get()
    para = entradaPara.get()
    cc = entradaCC.get()
    mensaje = mensajeArea.get("1.0",'end-1c')

    # Escritura
    archivo = filedialog.asksaveasfile()
    archivo.write("De: {}\n".format(de))
    archivo.write("Para: {}\n".format(para))
    archivo.write("CC: {}\n".format(cc))
    archivo.write("Mensaje: {}\n\n".format(mensaje))
    archivo.close()
    messagebox.showinfo(title="Exito", message='El borrador se ha guardado correctamente')

# INTERFAZ
# ========================================== #

# Ventana
ventana = Tk()
ventana.geometry("720x540")
ventana.config(bg = "white")
ventana.iconbitmap(bitmap='correo.ico')
ventana.resizable(0,0)
ventana.title("Correo - Nuevo correo")

# Menu
menu = Menu()
menuConfig = Menu(menu, tearoff=0,)
menu.add_cascade(menu=menuConfig, label="Configuracion")
menuConfig.add_command(label="Guardar Borrador", command=guardarBorrador)
menuConfig.add_radiobutton(label="Modo Oscuro", command=cambiarTema)
ventana.config(menu = menu)

# Marco de Herramientas
# ===================================== #
marcoHerramientas = LabelFrame(ventana, text="Barra de herramientas", font=("Bahnschrift",10), bg=color1,  bd=0)
marcoHerramientas.pack(padx = 20, pady = 5, fill="x")

# Boton Enviar
botonEnviar = Button(marcoHerramientas, text = "ENVIAR", font=("Bahnschrift",11), bg = color3, fg="white", bd=0, command=enviar)
botonEnviar.grid(row=0, column=0, rowspan=2, padx=5, pady=5, sticky="news")

# Label "Fuente:"
labelFuente = Label(marcoHerramientas, text ="Fuente: ", bg=color1, font=("Bahnschrift",10))
labelFuente.grid(row=0, column=1, pady=0)
# ComboBox importancia
fuenteMensaje = StringVar()
fuenteEntry = ttk.Combobox(marcoHerramientas, font=("Bahnschrift", 11), textvariable=fuenteMensaje, )
fuenteEntry['values'] = ("Calibri", "Arial", "Consolas", "Bahnschrift", "Bauhaus 93", "Comic Sans MS")
fuenteEntry.grid(row=1, column=1, pady=5, sticky="news")
fuenteEntry.bind("<<ComboboxSelected>>", CambiarFuente)

# Label "Tamaño:"
labelTamano = Label(marcoHerramientas, text ="tamaño: ", bg=color1, font=("Bahnschrift",10))
labelTamano.grid(row=0, column=2, pady=0)
# SpinBox "Tamaño:"
tamanoVar= StringVar()
tamanoVar.set("11") # Para el valor por default
tamano = ttk.Spinbox(marcoHerramientas, font=("Bahnschrift", 11), from_=5, to=90, width=5, state="readonly", command=CambiarFuente, textvariable=tamanoVar)
tamano.grid(row=1, column=2, pady=5, sticky="news")

# Marco de informacion
# ===================================== #
marcoDatos = LabelFrame(ventana, text="información", font=("Bahnschrift",10), bg=color1,  bd=0)
marcoDatos.pack(padx = 20, pady = 5, fill="x")

# Label "de:"
labelDe = Label(marcoDatos, text ="De: ", bg=color1, font=("Bahnschrift",11))
labelDe.grid(row=0, column=0, pady=5)
# Entrada "de:"
entradaDe = Entry(marcoDatos, bg= color2, bd=0, font=("Bahnschrift",11))
entradaDe.grid(row=0, column=1, pady=5, sticky="news")

# Label "Para: "
labelPara = Label(marcoDatos, text ="Para: ", bg=color1, font=("Bahnschrift",11))
labelPara.grid(row=1, column=0, pady=5)
# Entrada "Para: "
entradaPara = Entry(marcoDatos, bg= color2, bd=0, font=("Bahnschrift",11))
entradaPara.grid(row=1, column=1, pady=5, sticky="news")

# Label "CC: "
labelCC = Label(marcoDatos, text ="CC: ", bg=color1, font=("Bahnschrift",11))
labelCC.grid(row=2, column=0, pady=5)
# Entrada "CC: "
entradaCC = Entry(marcoDatos, bg= color2, bd=0, font=("Bahnschrift",11))
entradaCC.grid(row=2, column=1, pady=5, sticky="news")

# Marco de Texto
# ===================================== #
marcoTexto = LabelFrame(ventana, text="Mensaje: ", font=("Bahnschrift",10), bg=color1,  bd=0)
marcoTexto.pack(padx = 20, pady = 5, fill="x")

# Scroll Bar
scrollBar = Scrollbar(marcoTexto, bd=0)
scrollBar.pack( side = RIGHT, fill = Y )

# Area de texto
mensajeArea = Text(marcoTexto, bg=color2, bd=0, font=("Bahnschrft", 11), yscrollcommand = scrollBar.set)
mensajeArea.pack(padx=5, pady=5, fill=BOTH)

scrollBar.config( command = mensajeArea.yview )

# PRINCIPAL
# ========================================== #

fuenteEntry.current(0)
ventana.mainloop()