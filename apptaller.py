from tkinter import *
from tkinter import messagebox, filedialog


root = Tk()
root.title("Mi Aplicación")


checkbox_var = BooleanVar()
checkbox_var.set(True)


def guardar_datos():
    
    filename = filedialog.asksaveasfilename(defaultextension=".txt")
    if filename:
       
        nombre = nombre_entry.get()
        apellido = apellido_entry.get()
        correo = correo_entry.get()
        
        with open(filename, "w") as f:
            f.write("Nombre: {}\n".format(nombre))
            f.write("Apellido: {}\n".format(apellido))
            f.write("Correo electrónico: {}\n".format(correo))
            if checkbox_var.get():
                f.write("Acepta recibir correos electrónicos\n")
            else:
                f.write("No acepta recibir correos electrónicos\n")
        
        messagebox.showinfo("Datos guardados", "Los datos se han guardado correctamente.")


menu_bar = Menu(root)
root.config(menu=menu_bar)

# Menu
archivo_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Guardar", command=guardar_datos)

# 
campos_marco = LabelFrame(root, text="Datos Personales")
campos_marco.pack(padx=10, pady=10)

nombre_label = Label(campos_marco, text="Nombre")
nombre_label.grid(row=0, column=0, padx=5, pady=5)
nombre_entry = Entry(campos_marco)
nombre_entry.grid(row=0, column=1, padx=5, pady=5)

apellido_label = Label(campos_marco, text="Apellido")
apellido_label.grid(row=1, column=0, padx=5, pady=5)
apellido_entry = Entry(campos_marco)
apellido_entry.grid(row=1, column=1, padx=5, pady=5)


#Radio buttons
def seleccionGenero():
   selection = "You selected the option " + str(genero.get())
   label.config(text = selection)


genero = StringVar()
label = Label(campos_marco, text = "Genero")

generoM_boton = Radiobutton(campos_marco, text="Option 1", variable=genero, value="Masculino", command=seleccionGenero)
generoM_boton.grid(row=5, column=0, padx=5, pady=5)

generoF_boton = Radiobutton(campos_marco, text="Option 2", variable=genero, value="Femenino", command=seleccionGenero)
generoM_boton.grid(row=5, column=0, padx=5, pady=5)

generoO_boton = Radiobutton(campos_marco, text="Option 3", variable=genero, value="Otro", command=seleccionGenero)
generoM_boton.grid(row=5, column=0, padx=5, pady=5)


# label correo
correo_label = Label(campos_marco, text="Correo electrónico")
correo_label.grid(row=2, column=0, padx=5, pady=5)
correo_entry = Entry(campos_marco)
correo_entry.grid(row=2, column=1, padx=5, pady=5)


checkbox = Checkbutton(campos_marco, text="Acepto recibir correos electrónicos", variable=checkbox_var)
checkbox.grid(row=3, columnspan=2, padx=5, pady=5)


guardar_boton = Button(root, text="Guardar", command=guardar_datos)
guardar_boton.pack(padx=10, pady=10)


root.mainloop()





