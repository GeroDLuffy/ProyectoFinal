from tkinter import *
ventana = Tk()

screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()


# ventana.attributes('-fullscreen', True)

# ventana.geometry()

# Ventana Master Password
ventana.title('Password Manager')
# ventana.geometry('600x600')
# ventana.config()

label_mp = Label(ventana, text='Ingrese contraseña maestra: ')
label_mp.grid(row=0, column=0, sticky='n', padx=5)

entry_mp = Entry(ventana, bg='white')
entry_mp.config(show='*', justify='center')
entry_mp.grid(row=1, column=0, sticky='n', padx=5)

button_mp_q = Button(ventana, text='Salir', command=ventana.destroy).grid(row=2, column=0)

button_mp_e = Button(ventana, text='Acceder').grid(row=2, column=1)

# Frame Master Password
# frame_mp = Frame(ventana, bg='blue')
# # frame_mp.grid()
# frame_mp.pack(fill='both')

# label_mp = Label(frame_mp, text='Ingrese contraseña maestra: ')
# label_mp.grid(row=0, column=0, sticky='n', padx=5)


# entry_mp = Entry(frame_mp, bg='white')
# entry_mp.grid(row=0, column=1, sticky='n', padx=5)
# entry_mp.config(show='*', fg='black', justify='center')

# button_mp = Button(frame_mp, text='Salir', command=ventana.destroy).grid(row=1, column=1)




# # Frame Menu
# frame_menu = Frame()

# # Frame Datos
# frame_data = Frame()

ventana.mainloop()