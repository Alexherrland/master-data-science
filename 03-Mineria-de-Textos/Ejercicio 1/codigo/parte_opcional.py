import spacy
from spacy.tokens import Doc
import os

INSTITUCIONES = {
    'España', 'China', 'Francia', 'Alemania', 'Italia', 'Rusia', 
    'EEUU', 'Brasil', 'Argentina', 'Colombia', 'México', 'Portugal',
    'Estado', 'Comunidad'
}

ORGANIZACIONES = {
    'Gobierno', 'Ministerio', 'Ayuntamiento', 'Comisión', 'Consejo', 
    'Cámara', 'Policía', 'Jefatura', 'Unión', 'Federación', 'Asociación', 
    'Banco', 'Caja', 'Universidad', 'Instituto', 'Hospital', 'Fundación', 
    'Organización', 'Empresa', 'Grupo', 'Partido', 'Generalitat', 'Xunta',
    'Consellería', 'Consejería', 'Diputación'
}

STOP_WORDS = {'El', 'La', 'Los', 'Las', 'Un', 'Una', 'En', 'De', 'Por', 'Para'}


DATOS_MANUALES = [
    ("Google", "B-ORG"), ("ha", "O"), ("comprado", "O"), ("la", "O"), 
    ("empresa", "O"), ("de", "O"), ("inteligencia", "O"), ("artificial", "O"),
    ("DeepMind", "B-ORG"), ("por", "O"), ("400", "O"), ("millones", "O"),
    ("de", "O"), ("libras", "O"), (".", "O"),
    
    ("La", "O"), ("operación", "O"), ("fue", "O"), ("confirmada", "O"),
    ("por", "O"), ("Larry", "B-PER"), ("Page", "I-PER"), (",", "O"),
    ("fundador", "O"), ("de", "O"), ("la", "O"), ("compañía", "O"), (",", "O"),
    ("en", "O"), ("una", "O"), ("conferencia", "O"), ("en", "O"),
    ("Londres", "B-LOC"), (".", "O"),
    
    ("Microsoft", "B-ORG"), ("y", "O"), ("Facebook", "B-ORG"), ("también", "O"),
    ("estaban", "O"), ("interesadas", "O"), ("en", "O"), ("la", "O"),
    ("adquisición", "O"), ("según", "O"), ("el", "O"), ("diario", "O"),
    ("The", "B-MISC"), ("New", "I-MISC"), ("York", "I-MISC"), ("Times", "I-MISC"), (".", "O")
]


def procesar_archivo_conll(archivo_salida):
    """
    carga el modelo de spacy y procesa los datos manuales generando las predicciones.
    """
    try:
        nlp = spacy.load("es_core_news_lg")
        print("modelo cargado")
    except OSError:
        print("error al cargar el modelo")
        return

    oraciones_palabras = []
    oraciones_gold = []

    palabras_actuales = []
    gold_actuales = []

    # modificación para que se procesen los datos manuales terminados en un . en vez de un salto de linea
    for palabra, etiqueta in DATOS_MANUALES:
        if palabra == ".":
            palabras_actuales.append(palabra)
            gold_actuales.append(etiqueta)

            oraciones_palabras.append(palabras_actuales)
            oraciones_gold.append(gold_actuales)

            palabras_actuales = []
            gold_actuales = []
        else:
            palabras_actuales.append(palabra)
            gold_actuales.append(etiqueta)

    print("generando predicciones")

    with open(archivo_salida, "w", encoding="utf-8") as salida:

        for i in range(len(oraciones_palabras)):
            palabras = oraciones_palabras[i]
            etiquetas_gold = oraciones_gold[i]

            doc = Doc(nlp.vocab, words=palabras)

            for nombre, proceso in nlp.pipeline:
                doc = proceso(doc)

            etiquetas_pred = []
            correccion_activa = None

            for token in doc:
                iob = token.ent_iob_
                tipo = token.ent_type_
                texto = token.text

                # si es inicio de identidad aplicamos los filtros
                if iob == 'B':
                    if texto in ORGANIZACIONES:
                        etiquetas_pred.append("B-ORG")
                        correccion_activa = 'ORG'
                    elif texto in STOP_WORDS:
                        etiquetas_pred.append("O")
                        correccion_activa = None
                    elif texto in INSTITUCIONES and tipo == "LOC":
                        etiquetas_pred.append("B-ORG")
                        correccion_activa = 'ORG'
                    else:
                        etiquetas_pred.append(f"B-{tipo}")
                        correccion_activa = None
                # si se activa una correccion propagamos I-correcion a los siguientes tokens
                elif iob == "I":
                    if correccion_activa:
                        etiquetas_pred.append(f"I-{correccion_activa}")
                    else:
                        etiquetas_pred.append(f"I-{tipo}")
                else:
                    etiquetas_pred.append("O")
                    correccion_activa = None

            for palabra, etiqueta_gold, etiqueta_pred in zip(palabras, etiquetas_gold, etiquetas_pred):
                salida.write(f"{palabra} {etiqueta_gold} {etiqueta_pred}\n")
            salida.write("\n")

    print("Resultados guardados")


if __name__ == "__main__":
    archivo_salida = "salida_opcional.txt"
    procesar_archivo_conll(archivo_salida)
