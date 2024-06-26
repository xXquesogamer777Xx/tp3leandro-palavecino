
edades = {
    "Alice": 30,
    "Bob": 25,
    "Charlie": 35
}


edades["David"] = 28


del edades["Bob"]


nombre = "Alice"
if nombre in edades:
    print(f"La edad de {nombre} es {edades[nombre]}")
else:
    print(f"{nombre} no se encuentra en el registro")


print("Registro de edades actualizado:", edades)

def contar_frecuencia_letras(texto):
    frecuencia = {}
    for letra in texto:
        if letra.isalpha():  # Contar solo letras
            letra = letra.lower()
            if letra in frecuencia:
                frecuencia[letra] += 1
            else:
                frecuencia[letra] = 1
    return frecuencia


inscripcion = "Inscripción antigua en un templo"
frecuencia_letras = contar_frecuencia_letras(inscripcion)
print("Frecuencia de cada letra:", frecuencia_letras)


def palabra_mas_comun(texto):
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        palabra = palabra.lower().strip(".,!?;:")  # Normalizar la palabra
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
   
    palabra_comun = max(frecuencia, key=frecuencia.get)
    return palabra
