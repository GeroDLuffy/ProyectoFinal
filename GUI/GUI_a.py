from tkinter import *
from A_scripts import practica2 as p2
# Window
ventana = Tk()

ventana.title('Password Manager')
ventana.iconbitmap('Imagenes\llaves.ico')
ventana.geometry('600x600')

# Frames
frame = Frame()
frame.pack(fill='both')
frame.config(bg='white')

# Labels
label = Label(frame, text='Ingrese la contraseña maestra', bg='white')
label.config(height=1, width=25)
label.pack()

# Entry
Entry = Entry(frame, bg='white')
Entry.pack()
def get_text():
    text = Entry.get()
    p2.master_ppsw(text)
    

# Buttons
button = Button(frame, text = 'Enviar', command='ejemplo')
button.pack()






ventana.mainloop()
