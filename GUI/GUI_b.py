from tkinter import *
from ..A_scripts import master_ppsw as p2
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
def get_text():
    text = Entry.get()
    p2.master_ppsw(text)

# Buttons
button = Button(ventana, text = 'Enviar', command='ejemplo')
button.pack()






ventana.mainloop()