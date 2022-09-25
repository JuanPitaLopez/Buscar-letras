
from asyncio.base_subprocess import ReadSubprocessPipeProto
from tkinter import *
from math import factorial



def respuesta1():
    r1.set(factorial(int(n1.get())))
    
    Label(root,text=("El factorial de "+ str(n1.get())+" es "+str(factorial(int(n1.get()))))).pack()

def getSortedNumber():

  
    # Convert to equivalent string
    number = str(int(n1.get()))
  
    # Sort the string
    number = ''.join(sorted(number))
  
    # Convert to equivalent integer
    number = int(number)
  
    # Return the integer
    r2.set(number)
  
def respuesta3():
    entero = int(n1.get())
    hexadecimal = hex(entero)
    hexadecimal = format(entero, "0x")
    r3.set(hexadecimal)



root = Tk()
root.title("Principal")

root.resizable(1,1) 
root.iconbitmap("NTema6/Apple.ico")

n1 = StringVar()
n2 = StringVar()
r1 = StringVar()
r2 = StringVar()
r3 = StringVar()

Label(root,text="Introduce un número").pack()
Entry(root,justify="center",textvariable=n1).pack()

Label(root,text="Factorial").pack()
Entry(root,justify="center",textvariable=r1).pack()


Label(root,text="Ordenar").pack()
Entry(root,justify="center",textvariable=r2).pack()

Label(root,text="Hexadecimal").pack()
Entry(root,justify="center",textvariable=r3).pack()


Button(root, text="Factorial",command=(respuesta1)).pack()
Button(root, text="Ordenar",command=(getSortedNumber)).pack()
Button(root, text="Hexadecimal",command=(respuesta3)).pack()

#Button(root, text="Boton",command=respuesta1).pack()


root.mainloop()










