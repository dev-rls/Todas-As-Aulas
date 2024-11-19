import customtkinter as ctk

janela = ctk.CTk()
janela.geometry('000 x 000')
ctk.set_appearance_mode('black')

texto = ctk.CTkLabel(janela ,text='Olá')
texto.pack()

janela.mainloop()