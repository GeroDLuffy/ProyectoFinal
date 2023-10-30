from tkinter import *

# Window
ventana = Tk()

ventana.title('Password Manager')
ventana.iconbitmap('Imagenes\llaves.ico')
ventana.geometry('600x600')

# Labels
label = Label(ventana, text='Ingrese la contraseña maestra', bg='white')
label.config(height=1, width=25)
label.pack()

# Entry
Entry = Entry(ventana, text='Hola Mundo', bg='white')
Entry.pack()

# Buttons
button = Button(ventana, text = 'Enviar', command='ejemplo')
button.pack()






ventana.mainloop()
