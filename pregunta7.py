

numeros = [4875,598861,988,453844,755,41211,11,547,5566,757144]

def funcion_principal(e):
    numero = e
    contador=0
    terminado = False
    list = []
    while terminado == False:
        digito = e % 10
    
        list.append(digito)
        if e<10:
            terminado = True
        else:
            e = e // 10
    
    for i in range(0,len(list)-2):
        if list[i] == list[i+1]:
            
            contador = contador + 1
        
    if contador >0:
        
        return numero
    
nombres_filtrados = list(filter(funcion_principal, numeros))
print(nombres_filtrados)


