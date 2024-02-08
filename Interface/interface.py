from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import banco

def popular():
    tv.delete(*tv.get_children())
    vquery = "SELECT * FROM tb_nomes order by ID"
    linhas = banco.dql(vquery)
    for i in linhas:
        tv.insert('','end', values=i)

def inserir():
    if vnome.get() == '' or vfone.get()=='':
        messagebox.showinfo(title='ERRO', message="Digite todos os dados!")
        return
    try:
        vquery = f'INSERT INTO tb_nomes (nome, telefone) VALUES ("{vnome.get()}", "{vfone.get()}")'
        banco.dml(vquery)
    except:
        messagebox.showinfo(title='ERRO', message='Erro ao inserir' )
        return
    popular()
    vnome.delete(0,END)
    vfone.delete(0,END)
    vnome.focus()
    
def pesquisar():
    tv.delete(*tv.get_children())
    vquery = f"SELECT * FROM tb_nomes WHERE nome LIKE '%{vnomepesquisar.get()}%' order by ID"
    linhas = banco.dql(vquery)
    for i in linhas:
        tv.insert('', 'end', values=i)

app = Tk()
app.geometry('600x450')
app.title('TreeView BD')

##############################

quadroGrid= LabelFrame(app, text='Contatos')
quadroGrid.pack(fill='both', expand='yes', padx=10, pady=10)

tv = ttk.Treeview(quadroGrid, columns=('id','nome', 'telefone'), show='headings')
tv.column('id', minwidth=0, width=50)
tv.column('nome', minwidth=0, width=250)
tv.column('telefone', minwidth=0, width=100)
tv.heading('id', text='ID')
tv.heading('nome', text='NOME')
tv.heading('telefone', text='TELEFONE')
tv.pack()
popular()

###############################

quadroInserir = LabelFrame(app, text='Inserir Novos Contatos')
quadroInserir.pack(fill='both', expand='yes', padx=10, pady=10)

lbnome=Label(quadroInserir, text='Nome')
lbnome.pack(side='left')
vnome= Entry(quadroInserir)
vnome.pack(side='left', padx=10)
lbfone= Label(quadroInserir, text='Telefone')
lbfone.pack(side='left',padx=10)
vfone=Entry(quadroInserir)
vfone.pack(side='left', padx=10)
btn_inserir= Button(quadroInserir, text='Inserir', command=inserir)
btn_inserir.pack(side='left', padx=10)

################################

quadroPesquisar = LabelFrame(app, text='Pesquisar Contatos')
quadroPesquisar.pack(side='left')
vnomepesquisar= Entry(quadroPesquisar)
vnomepesquisar.pack(side='left', padx=10)
btn_pesquisar=Button(quadroPesquisar, text='Pesquisar', command=pesquisar)
btn_pesquisar.pack(side='left', padx=10)
btn_todos= Button(quadroPesquisar, text='Mostrar Todos', command = popular)
btn_todos.pack(side='left', padx=10)

app.mainloop()