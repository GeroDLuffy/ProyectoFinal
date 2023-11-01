from tkinter import *
ventana = Tk()

screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()

# Frame Master Password
frame_mp = Frame(ventana, bg='blue', width=screen_width, height=screen_height)
frame_mp.pack(fill='both')

label_mp = Label(frame_mp, text='Ingrese contraseña maestra: ')
label_mp.grid(row=0, column=0, sticky='n', padx=5)


entry_mp = Entry(frame_mp, bg='white')
entry_mp.grid(row=0, column=1, sticky='n', padx=5)
entry_mp.config(show='*', fg='black', justify='center')




# # Frame Menu
# frame_menu = Frame()

# # Frame Datos
# frame_data = Frame()

ventana.mainloop()