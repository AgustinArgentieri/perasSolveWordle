#Defino una funcion para eliminar letras con acentos
def normalize(s):     
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ä", "a"),
        ("ë", "e"),
        ("ï", "i"),
        ("ö", "o"),
        ("ü", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

# Abro el archivo allSpanishWords.txt y selecciono las palabras de 5 letras para agregarlas al listado fiveLetters
allWords = open("allSpanishWords.txt", "r", encoding='utf-8')
fiveLetters = []
for i in allWords:
    if len(i) == 6:
        fiveLetters.append(normalize(i))
    else:
        continue

#Elimino los duplicados del listado fiveLetters
fiveLetters = set(fiveLetters)

#Abro o creo el archivo fiveLettersWords.txt y escribo en ese archivo las palabras del listado fiveLetters
fileFiveLetters = open("fiveLettersWords.txt", "w")
for i in fiveLetters:
    fileFiveLetters.write(i)