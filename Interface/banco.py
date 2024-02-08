import sqlite3
from sqlite3 import Error

pastaApp = r'C:\desenvolvimento 2024\Projeto Banco de Dados\Códigos\banco\agenda.db'

def conexaoBanco():
    con = None
    try:
        con = sqlite3.connect(pastaApp)
    except Error as er:
        print(er)
    return con


def dql(query):
    vcon = conexaoBanco()
    c = vcon.cursor()
    c.execute(query)
    res = c.fetchall()
    vcon.close()
    return res


def dml(query):
    try:
        vcon = conexaoBanco()
        c = vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as er:
        print(er)


