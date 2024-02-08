from tkinter import *
import os
import banco as bd

c = os.path.dirname(__file__)
nomeArquivo = c+'\\nomes.txt'
print(nomeArquivo)

app = Tk()
app.title('Interface Option Menus')
app.geometry('600x400')
app.configure(background='#dde')


def gravarDados():
    global tbobs, tbnome, tbfone, tbmail
    if tbnome.get() != "":
        vnome = tbnome.get()
        vfone = tbfone.get()
        vemail = tbmail.get()
        vobs = tbobs.get('1.0', END)
        vquery = f'''INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO, T_OBS)
                    VALUES ('{vnome}','{vfone}','{vemail}','{vobs}')'''
        bd.dml(vquery)
        tbmail.delete(0, END)
        tbfone.delete(0, END)
        tbnome.delete(0, END)
        tbobs.delete('1.0', END)
        print('Dados Gravados com Sucesso')
    else:
        print("ERRO")


Label(app, text='Nome:', background='#dde', foreground='#000', anchor=W).place(x=10, y=10, width=100, height=20)
tbnome = Entry(app)
tbnome.place(x=10, y=35, width=250, height=20)

Label(app, text='Telefone:', background='#dde', foreground='#000', anchor=W).place(x=10, y=60, width=100, height=20)
tbfone = Entry(app)
tbfone.place(x=10, y=85, width=150, height=20)

Label(app, text='Email:', background='#dde', foreground='#000', anchor=W).place(x=10, y=110, width=100, height=20)
tbmail = Entry(app)
tbmail.place(x=10, y=135, width=175, height=20)

Label(app, text='OBS', background='#dde', foreground='#000', anchor=W).place(x=10, y=160, width=100, height=20)
tbobs = Text(app)
tbobs.place(x=10, y=185, width=300, height=100)

btn = Button(app, text='Gravar', command=gravarDados)
btn.place(x=10, y=290, width=70, height=25)

app.mainloop()
