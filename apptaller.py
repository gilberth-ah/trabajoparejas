from tkinter import *
from tkinter import messagebox, filedialog


root = Tk()
root.geometry('480x380')
root.config(bg= "black")
root.iconbitmap(bitmap='correo.ico')
root.resizable(0,0)
root.title('Correos')


checkbox_var = BooleanVar()
checkbox_var.set(True)


def guardar_datos():
    
   
       
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    correo = correo_entry.get()
        
    file = open("correos.txt", "a")
    file.write("Nombre: {}\n".format(nombre))
    file.write("Apellido: {}\n".format(apellido))
    file.write("Correo electrónico: {}\n".format(correo))
    if checkbox_var.get():
        file.write("Acepta recibir correos electrónicos\n")
    else:
        file.write("No acepta recibir correos electrónicos\n")
    file.close()
       
    messagebox.showinfo("Datos guardados", "Los datos se han guardado correctamente.")


menu_bar = Menu(root)
root.config(menu=menu_bar)


archivo_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Guardar", command=guardar_datos)


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

correo_label = Label(campos_marco, text="Correo electrónico")
correo_label.grid(row=2, column=0, padx=5, pady=5)
correo_entry = Entry(campos_marco)
correo_entry.grid(row=2, column=1, padx=5, pady=5)

checkbox = Checkbutton(campos_marco, text="Acepto recibir correos electrónicos", variable=checkbox_var)
checkbox.grid(row=3, columnspan=2, padx=5, pady=5)


guardar_boton = Button(root, text="Guardar", command=guardar_datos)
guardar_boton.pack(padx=10, pady=10)









