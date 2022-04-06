print("Inserte la palabra \"PERAS\" como primer solucion del Wordle.")
print("Si ya ingreso \"PERAS\" como primer palabra, aprete enter.")
input()

print("A continuacion debe escribir una cadena de texto describiendo el resultado de la primer palabra")
print("Esta cadena debe tener una longitud de 5 caracteres indicando si cada letra resulto verde (V), amarilla (A) o gris (G).")
print("Por ejemplo si la palabra PERAS tiene la letra P y la letra A de color amarillo, y el resto gris, \
la cadena de texto a introducir sera: aggag")

dic = open("fiveLettersWords.txt", "r", encoding="latin-1").read().splitlines() #leo el diccionario con palabras de 5 letras y lo guardo en dic en formato de lista

def returnCheckResponse(): #Esta funcion devuelve una cadena valida para tratar las soluciones al wordle
    while True:
        response = input().lower()  #Creo un input para ingresar la respuesta dentro de la variable response
        if len(response) != 5: #Compruebo que la cadena tiene 5 caracteres de longitud
            print("Introdujo la cadena de texto de forma erronea, vuelva a introducir el resultado de la palabra correctamente")
            continue
        else: #A partir de aca verifico que solo introduzcan letras las letras "a", "g" o "v" en la cadena
            if response[0] not in["a","g","v"]:
                print("La primera letra indicada no es \"a\" \"g\" o \"v\"")
                print("Vuelva a introducir el resultado de la palabra correctamente")
                continue
            if response[1] not in["a","g","v"]:
                print("La segunda letra indicada no es \"a\" \"g\" o \"v\"")
                print("Vuelva a introducir el resultado de la palabra correctamente")
                continue
            if response[2] not in["a","g","v"]:
                print("La tercera letra indicada no es \"a\" \"g\" o \"v\"")
                print("Vuelva a introducir el resultado de la palabra correctamente")
                continue
            if response[3] not in["a","g","v"]:
                print("La cuarta letra indicada no es \"a\" \"g\" o \"v\"")
                print("Vuelva a introducir el resultado de la palabra correctamente")
                continue
            if response[4] not in["a","g","v"]:
                print("La quinta letra indicada no es \"a\" \"g\" o \"v\"")
                print("Vuelva a introducir el resultado de la palabra correctamente")
                continue
        return response #Devuelvo la palabra verificada

print("Antes de comenzar a eliminar palabras, existen " + str(len(dic)) + " palabras posibles.")

firstResponse = returnCheckResponse()

#A partir de la primer devolucion, verifico que letras salieron en gris y elimino las palabras del diccionario que no poseen dichas letras
#print(dic)
if "g" in firstResponse:
    if firstResponse[0] == "g":
        for palabra in reversed(dic):
            if "p" in palabra:
                dic.remove(palabra)
    if firstResponse[1] == "g":
        for palabra in reversed(dic):
            if "e" in palabra:
                dic.remove(palabra)
    if firstResponse[2] == "g":
        for palabra in reversed(dic):
            if "r" in palabra:
                dic.remove(palabra)
    if firstResponse[3] == "g":
        for palabra in reversed(dic):
            if "a" in palabra:
                dic.remove(palabra)
    if firstResponse[4] == "g":
        for palabra in reversed(dic):
            if "s" in palabra:
                dic.remove(palabra)

#Ahora verifico las letras verdes y elimino las que no cumplen la condicion.
if "v" in firstResponse:
    if firstResponse[0] == "v":
        for palabra in reversed(dic):
            if palabra[0] != "p":
                dic.remove(palabra)
    if firstResponse[1] == "v":
        for palabra in reversed(dic):
            if palabra[1] != "e":
                dic.remove(palabra)
    if firstResponse[2] == "v":
        for palabra in reversed(dic):
            if palabra[2] != "r":
                dic.remove(palabra)                
    if firstResponse[3] == "v":
        for palabra in reversed(dic):
            if palabra[3] != "a":
                dic.remove(palabra)
    if firstResponse[4] == "v":
        for palabra in reversed(dic):
            if palabra[4] != "s":
                dic.remove(palabra)

#Finalmente reviso las letras amarillas
if "a" in firstResponse:
    if firstResponse[0] == "a":
        for palabra in reversed(dic):
            if "p" not in palabra:
                dic.remove(palabra)
    if firstResponse[1] == "a":
        for palabra in reversed(dic):
            if "e" not in palabra:
                dic.remove(palabra)
    if firstResponse[2] == "a":
        for palabra in reversed(dic):
            if "r" not in palabra:
                dic.remove(palabra)                
    if firstResponse[3] == "a":
        for palabra in reversed(dic):
            if "a" not in palabra:
                dic.remove(palabra)
    if firstResponse[4] == "a":
        for palabra in reversed(dic):
            if "s" not in palabra:
                dic.remove(palabra)

if "trone" in dic:
    print("No elimine TRONE en la primera vuelta 0.5")

#Ya revise en el diccionario que la letra indicada en amarillo se encuentre en todas las palabras del diccionario.
#Ahora reviso que en la posicion que marcamos en amarillo, no se encuentre la letra en cuestion.
    if firstResponse[0] == "a":
        for palabra in reversed(dic):
            if palabra[0] == "p":
                dic.remove(palabra)
    if firstResponse[1] == "a":
        for palabra in reversed(dic):
            if palabra[1] == "e":
                dic.remove(palabra)
    if firstResponse[2] == "a":
        for palabra in reversed(dic):
            if palabra[2] == "r":
                dic.remove(palabra)                
    if firstResponse[3] == "a":
        for palabra in reversed(dic):
            if palabra[3] == "a":
                dic.remove(palabra)
    if firstResponse[4] == "a":
        for palabra in reversed(dic):
            if palabra[4] == "s":
                dic.remove(palabra)

if "trone" in dic:
    print("No elimine TRONE en la primera vuelta")

#SEGUNDA VUELTA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for i in range(5):
    print("Actualmente, existen " + str(len(dic)) + " palabras posibles.")

    for palabra in dic: #Verifico que la palabra que voy a tomar de solucion, no tenga letras repetidas.
        secondSolution = palabra
        if len(set(palabra)) == 5:
            break

    print("Para continuar el juego, debe introducir la palabra \"" + secondSolution + "\" como segunda respuesta")
    print("Una vez introducida la respuesta, vuelva a escribir el resultado obtenido con A, V, o G segun corresponda.")

    firstResponse = returnCheckResponse()

    # verifico que letras salieron en gris y elimino las palabras del diccionario que no poseen dichas letras
    if "g" in firstResponse:
        if firstResponse[0] == "g":
            for palabra in reversed(dic):
                if secondSolution[0] in palabra:
                    dic.remove(palabra)
        if firstResponse[1] == "g":
            for palabra in reversed(dic):
                if secondSolution[1] in palabra:
                    dic.remove(palabra)
        if firstResponse[2] == "g":
            for palabra in reversed(dic):
                if secondSolution[2] in palabra:
                    dic.remove(palabra)
        if firstResponse[3] == "g":
            for palabra in reversed(dic):
                if secondSolution[3] in palabra:
                    dic.remove(palabra)
        if firstResponse[4] == "g":
            for palabra in reversed(dic):
                if secondSolution[4] in palabra:
                    dic.remove(palabra)

    #Ahora verifico las letras verdes y elimino las que no cumplen la condicion.
    if "v" in firstResponse:
        if firstResponse[0] == "v":
            for palabra in reversed(dic):
                if palabra[0] != secondSolution[0]:
                    dic.remove(palabra)
        if firstResponse[1] == "v":
            for palabra in reversed(dic):
                if palabra[1] != secondSolution[1]:
                    dic.remove(palabra)
        if firstResponse[2] == "v":
            for palabra in reversed(dic):
                if palabra[2] != secondSolution[2]:
                    dic.remove(palabra)                
        if firstResponse[3] == "v":
            for palabra in reversed(dic):
                if palabra[3] != secondSolution[3]:
                    dic.remove(palabra)
        if firstResponse[4] == "v":
            for palabra in reversed(dic):
                if palabra[4] != secondSolution[4]:
                    dic.remove(palabra)

    #Finalmente reviso las letras amarillas
    if "a" in firstResponse:
        if firstResponse[0] == "a":
            for palabra in reversed(dic):
                if secondSolution[0] not in palabra:
                    dic.remove(palabra)
        if firstResponse[1] == "a":
            for palabra in reversed(dic):
                if secondSolution[1] not in palabra:
                    dic.remove(palabra)
        if firstResponse[2] == "a":
            for palabra in reversed(dic):
                if secondSolution[2] not in palabra:
                    dic.remove(palabra)                
        if firstResponse[3] == "a":
            for palabra in reversed(dic):
                if secondSolution[3] not in palabra:
                    dic.remove(palabra)
        if firstResponse[4] == "a":
            for palabra in reversed(dic):
                if secondSolution[4] not in palabra:
                    dic.remove(palabra)


    #Ya revise en el diccionario que la letra indicada en amarillo se encuentre en todas las palabras del diccionario.
    #Ahora reviso que en la posicion que marcamos en amarillo, no se encuentre la letra en cuestion.
        if firstResponse[0] == "a":
            for palabra in reversed(dic):
                if palabra[0] == secondSolution[0]:
                    dic.remove(palabra)
        if firstResponse[1] == "a":
            for palabra in reversed(dic):
                if palabra[1] == secondSolution[1]:
                    dic.remove(palabra)
        if firstResponse[2] == "a":
            for palabra in reversed(dic):
                if palabra[2] == secondSolution[2]:
                    dic.remove(palabra)
        if firstResponse[3] == "a":
            for palabra in reversed(dic):
                if palabra[3] == secondSolution[3]:
                    dic.remove(palabra)
        if firstResponse[4] == "a":
            for palabra in reversed(dic):
                if palabra[4] == secondSolution[4]:
                    dic.remove(palabra)


#print(dic)
#Hay un problema cuando una letra se repite en la respuesta, por ejemplo si introduzo como respuesta OYERE
#El problema es que una e esta en amarillo y la otra en gris, sin embargo, el programa elimina a todas las palabras que tienen e
