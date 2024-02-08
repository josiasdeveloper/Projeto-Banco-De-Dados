from tkinter import *
import banco as bd

caminho = r'\banco\agenda.db'


def novoContato():
    exec(open(caminho).read())


def teste():
    pass


app = Tk()
app.title('Agenda')
app.geometry('500x300')
app.configure(background='#dde')

barraDeMenus = Menu(app)

menuContatos = Menu(barraDeMenus, tearoff=0)
menuContatos.add_command(label='Novo', command=novoContato)
menuContatos.add_command(label='Pesquisar', command=teste)
menuContatos.add_command(label='Deletar', command=teste)
menuContatos.add_separator()
menuContatos.add_command(label='Fechar', command=app.quit)
barraDeMenus.add_cascade(label='Contatos', menu=menuContatos)
app.configure(menu=barraDeMenus)

menuManutencao = Menu(barraDeMenus, tearoff=0)
menuManutencao.add_command(label='Banco de dados', command=teste)
barraDeMenus.add_cascade(label='Manutenção', menu=menuManutencao)




app.mainloop()
