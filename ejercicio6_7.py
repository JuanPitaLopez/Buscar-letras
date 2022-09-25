from asyncio.base_subprocess import ReadSubprocessPipeProto
from tkinter import *
from math import factorial
import sqlite3
conexion = sqlite3.connect("Nusuarios.db")

cursor = conexion.cursor()
#cursor.execute("CREATE TABLE Nusuarios (nombre VARCHAR(100),apellido VARCHAR(100), DNI INTEGER, genero VARCHAR(100))")


def respuesta1():
    n1.get()
    n2.get()
    n3.get()
    n4.get()

    conexion = sqlite3.connect("Nusuarios.db")
    cursor = conexion.cursor()
    print(n1.get())
    #cursor.execute("INSERT INTO Nusuarios (n1,n2,n3,n4)" "VALUES (%s,%s,%s,%s)")
    usuarios = [(n1.get(),n2.get(),n3.get(),n4.get())]
    print(usuarios)
    cursor.executemany("INSERT INTO Nusuarios VALUES (?,?,?,?)",usuarios)
    conexion.commit()

def getSortedNumber():
    cursor.execute("SELECT * FROM Nusuarios")
    usuarios= cursor.fetchall()
    print(usuarios)
    for user in usuarios:
        Label(root,text=(user)).pack()



def respuesta3():
    entero = int(n1.get())
    hexadecimal = hex(entero)
    hexadecimal = format(entero, "0x")
    r3.set(hexadecimal)



root = Tk()
root.title("Principal")

root.geometry("500x500")
root.resizable(1,1) 
root.iconbitmap("NTema6/Apple.ico")

n1 = StringVar()
n2 = StringVar()
n3 = StringVar()
n4 = StringVar()
n5 = StringVar()
r1 = StringVar()
r2 = StringVar()
r3 = StringVar()

Label(root,text="Nombre").pack()
Entry(root,justify="center",textvariable=n1).pack()

Label(root,text="Apellido").pack()
Entry(root,justify="center",textvariable=n2).pack()

Label(root,text="DNI").pack()
Entry(root,justify="center",textvariable=n3).pack()

Label(root,text="Género").pack()
Entry(root,justify="center",textvariable=n4).pack()



Button(root, text="Registrar",command=(respuesta1)).pack()
Button(root, text="Ver Usuarios",command=(getSortedNumber)).pack()




root.mainloop()









