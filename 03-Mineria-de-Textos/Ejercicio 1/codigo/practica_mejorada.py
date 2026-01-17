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


def procesar_archivo_conll(archivo_entrada, archivo_salida):
    """
    carga el modelo de spacy y procesa el archivo esp.testb generando las predicciones.
    """
    try:
        nlp = spacy.load("es_core_news_lg")
        print("modelo cargado")
    except OSError:
        print("error al cargar el modelo")
        return

    if not os.path.exists(archivo_entrada):
        print("error al cargar el archivo testb")
        return
    
    oraciones_palabras = []
    oraciones_gold = []
    
    palabras_actuales = []
    etiquetas_actuales = []

    with open(archivo_entrada, 'r', encoding='utf-8', errors='ignore') as f:
        for linea in f:
            linea = linea.strip()

            if not linea:
                if palabras_actuales:
                    oraciones_palabras.append(palabras_actuales)
                    oraciones_gold.append(etiquetas_actuales)
                    palabras_actuales = []
                    etiquetas_actuales = []
                continue

            partes = linea.split()
            if len(partes) >= 2:
                palabra = partes[0]
                etiqueta = partes[-1]
                
                palabras_actuales.append(palabra)
                etiquetas_actuales.append(etiqueta)

        if palabras_actuales:
            oraciones_palabras.append(palabras_actuales)
            oraciones_gold.append(etiquetas_actuales)

    print(f"generando predicciones")

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
                        etiquetas_pred.append('B-ORG')
                        correccion_activa = 'ORG'   
                    elif texto in STOP_WORDS:
                        etiquetas_pred.append('O')
                        correccion_activa = None 
                    elif texto in INSTITUCIONES and tipo == 'LOC':
                         etiquetas_pred.append('B-ORG')
                         correccion_activa = 'ORG'
                    else:
                        etiquetas_pred.append(f"B-{tipo}")
                        correccion_activa = None
                # si se activa una correccion propagamos I-correcion a los siguientes tokens
                elif iob == 'I':
                    if correccion_activa:
                        etiquetas_pred.append(f"I-{correccion_activa}")
                    else:
                        etiquetas_pred.append(f"I-{tipo}")
                
                else:
                    etiquetas_pred.append('O')
                    correccion_activa = None

            for palabra, etiqueta_gold, etiqueta_pred in zip(palabras, etiquetas_gold, etiquetas_pred):
                salida.write(f"{palabra} {etiqueta_gold} {etiqueta_pred}\n")
            salida.write("\n")

    print("Resultados guardados")

if __name__ == "__main__":
    archivo_entrada = "esp.testb.txt" 
    archivo_salida = "salida_final_es_core_news_lg.txt"
    procesar_archivo_conll(archivo_entrada, archivo_salida)