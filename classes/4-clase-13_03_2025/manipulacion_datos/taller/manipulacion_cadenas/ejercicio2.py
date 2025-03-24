"""
Enunciado:
    Pida al usuario una frase y reemplace todas las ocurrencias de una palabra por otra.

Pseudocódigo:
    // Función para reemplazar todas las ocurrencias
    str replace_ocurrencie(phrase: str, ocurrence: str, new_word: str){
        // Lista de palabras extraídas de la frase
        list_words <- splitter(phrase, " ")
        // Re-Inicializar variable (para luego reconstruirla)
        phrase <- ""
        // Recorrer lista de palabras
        PARA i <- 1 HASTA list_words.length() CON PASO 1 HACER
            SI list_words[i] = ocurrence THEN
                list_words[i] <- new_word
            FIN SI
            // Se agrega nuevamente cada palabra y un espacio separador
            phrase += list_words[i] + " "
        FIN PARA
        // Retornar frase "reconstruida"
        RETURN phrase 
    }

    ------
    // Función que simula ser "split"
    list[str] splitter(string_: str, serparator: str){
        // Inicalizar lista de palabras
        words <- []
        word <- "" 
        PARA i <- 1 HASTA string_.length() CON PASO 1 HACER
            // Verificar si el caracter actual es diferente de "espacio"
            SI string_[i] != separator:
                // Agregar cada caracter hasta formar una palabra
                word <- word + string_[i]
            SINO
                // Se encontró un "espacio"
                //se procede a agregar la palabra a la lista de palabras
                words.push(word)
                // Se inicializa la variable nuevamente (nueva palabra)
                word <- ""
            FIN SI
        FIN PARA
        // Se agrega la última palabra formada
        words.push(word)
        // Retornar la lista de palabras extraídas
        RETURN words
    }
    ------
    // main()
    ESCRIBIR "Ingrese una frase: "
    LEER phrase
    ESCRIBIR "Ingrese la palabra a buscar: "
    LEER word
    ESCRIBIR "Ingrese la palabra nueva palabra: "
    LEER new_word
    ESCRIBIR "Se desea reemplazar la palabra (", word, ") en la frase (", phrase, ")"
    // Reemplazar todas las ocurrencias de la palabra en la frase
    phrase <- replace_ocurrencie(phrase, word, new_word)
    ESCRIBIR "Nueva frase: ", phrase

Estrategia:
    Se busca "recortar/separar" la frase en una lista de palabras, para consecuentemente
    recorrer esta lista y compar cada palabra con la ocurrencia que se busca, por cada ocurrencia encontrada,
    la palabra en la posición actual (dentro del ciclo) será reemplazada por la "nueva palabra".
    Una vez recorrida la lista de palabras, se debe "reconstruir" la "nueva frase" con las ocurrencias ya
    reemplazadas
"""

def replace_ocurrencie(phrase: str, ocurrence: str, new_word: str) -> str:
    """Función para reemplazar todas las ocurrencias

    Args:
        phrase (str): Frase con la cual se trabajará
        ocurrence (str): Palabra que se buscará en la frase
        new_word (str): Nueva palabra que reemplazará cada ocurrencia en la frase

    Returns:
        str: Nueva frase, con la nueva palabra en cada ocurrencia
    """
    # Lista de palabras extraídas de la frase
    list_words:list = splitter(phrase, " ")
    print(list_words)
    # Re-Inicializar variable (para luego reconstruirla)
    phrase:str = ""
    # Recorrer lista de palabras
    for i in range(len(list_words)):
        if list_words[i] == ocurrence:
            list_words[i] = new_word
        # Se agrega nuevamente cada palabra y un espacio separador
        phrase += list_words[i] + " "
    # Retornar frase "reconstruida"
    return phrase 

def splitter(string_to_split: str, separator: str) -> list:
    """Función que simula ser "split"

    Args:
        string_to_split (str): String que se quiere "recortar/separar"
        separator (str): String que representa el separador mediante el cual se cortará el String

    Returns:
        list: Lista de palabras extraídas/separadas del String
    """
    # Inicalizar lista de palabras
    words:list = []
    word:str = "" 
    for char in string_to_split:
        # Verificar si el caracter actual es diferente que el "separador" indicado
        if char != separator:
            # Agregar cada caracter hasta formar una palabra
            word += char
        else:
            # Se encontró un "espacio"
            #se procede a agregar la palabra a la lista de palabras
            words.append(word)
            # Se inicializa la variable nuevamente (nueva palabra)
            word:str = ""
    # Se agrega la última palabra formada
    words.append(word)
    # Retornar la lista de palabras extraídas
    return words

# Se reutilizará código, por tanto
# Solo se ejecutará esta parte si se ejecuta este archivo principal
if __name__ == "__main__":
    # Ingreso de información
    phrase:str = input("Ingrese una frase: ")
    word:str = input("Ingrese la palabra a buscar: ")
    new_word:str = input("Ingrese la nueva palabra: ")

    print(f'Se desea reemplazar la palabra "{word}" en la frase "{phrase}"')

    # Reemplazar todas las ocurrencias de la palabra en la frase
    phrase:str = replace_ocurrencie(phrase, word, new_word)
    print(f"Nueva frase: {phrase}")