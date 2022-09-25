#Convertir una frase en una lista de palabras:

texto = "La maestra empezí a enseñatnos las consonantes"
texto1 = texto.split()

def obtener_vocales(frase):
    
    frase = frase.lower()
    contador = 0
    contador2 = 0
    for i in ["a","e","i","o","u","á","é","í","ó","ú"]:
        contador = contador + frase.count(i)
        
    for i in ["q","w","r","t","y","p","s","d","f","g","h","j","k","l","ñ","z","x","c","v","b","n","m"]:
        contador2 = contador2 + frase.count(i)
       
    print("La palabra (",frase,") tiene",contador,"vocales y",contador2,"consonantes")
    diccionario = {"vocales":contador,"consonates":contador2}
    print(diccionario)
    diccionario = 0
    
def obtener_vocales_total(frase):
    
    frase = frase.lower()
    contador = 0
    contador2 = 0
    for i in ["a","e","i","o","u","á","é","í","ó","ú"]:
        contador = contador + frase.count(i)
        
    for i in ["q","w","r","t","y","p","s","d","f","g","h","j","k","l","ñ","z","x","c","v","b","n","m"]:
        contador2 = contador2 + frase.count(i)
        
    print("La frase (",frase,") tiene",contador,"vocales y",contador2,"consonantes")
    
    


    




obtener_vocales_total(texto)
funcionmap = list(map(obtener_vocales,texto1))





