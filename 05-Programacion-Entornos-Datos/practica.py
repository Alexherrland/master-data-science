import pandas as pd

column_names = ['Dia', 'Mes', 'Lector', 'Titulo', 'Autor', 'Genero', 'Duracion', 'Renovacion']

def createDF(file):
    # parsear el df con el formato correcto y concatenarlo de vuelta
    with open(file, 'r', encoding='utf-8') as f:
        year = int(f.readline().strip())
    
    temp_df = pd.read_csv(
        file,
        skiprows=1,
        header=None,
        names=column_names)
    
    # diccionario de tipos para procesarlos todos al mismmo tiempo
    dtypes_config = {
    "Año": "int16",
    "Dia": "int8",
    "Mes": "category",
    "Lector": "category",
    "Autor": "category",
    "Genero": "category",
    "Duracion": "int16",
    "Titulo":"object"
    }
    
    # añadimos el año y el tipo de renovación
    temp_df["Año"] = year
    temp_df["Renovacion"] = temp_df["Renovacion"].eq("Si")

    temp_df = temp_df.astype(dtypes_config)

    return temp_df

def loadData(file_paths):

    list_dfs = []
    for file in file_paths:
        chunk = createDF(file)
        list_dfs.append(chunk)
    full_df = pd.concat(list_dfs, ignore_index=True)
    
    #print(full_df.info)
    #print(full_df.dtypes)
    return full_df

#
# Ejercicio 3
#

# funciones auxiliares para el ejercicio 3
def filter_year(df, y):
    return df[df["Año"] == int(y)]

def groupByColumn(df, column):
    return df.groupby(column, observed=True).size().sort_values(ascending=False).index[0]


# a) Libro mas prestado
def bestBook(df):
    return groupByColumn(df, ["Titulo", "Autor", "Genero"])

def bestBookYear(df,y):
    return bestBook(filter_year(df, y))


# b) Genero mas prestado
def bestGenre(df):
    return groupByColumn(df, "Genero")

def bestGenreYear(df, y):
    return bestGenre(filter_year(df, y))


# c) Lector con mas prestamos
def bestReader(df):
    lector_top = groupByColumn(df, "Lector")
    df_lector = df[df["Lector"] == lector_top]
    
    genero_fav = groupByColumn(df_lector, "Genero")
    autor_fav = groupByColumn(df_lector, "Autor")
    return (lector_top, genero_fav, autor_fav)

def bestReaderYear(df, y):
    return bestReader(filter_year(df, y))


# d) Lector con mas dias acumulados
def mostAccumulatedDays(df):
    suma_dias = df.groupby("Lector", observed=True)["Duracion"].sum()
    lector_ganador = suma_dias.idxmax()
    num_prestamos = len(df[df["Lector"] == lector_ganador])
    
    return (lector_ganador, num_prestamos)

def mostAccumulatedDaysYear(df, y):
    return mostAccumulatedDays(filter_year(df, y))


# e) Informacion de usuario
def userInfo(df, u):
    df_usuario = df[df["Lector"] == u]
    prestamos = len(df_usuario)
    
    if prestamos == 0:
        return {
            "Prestamos": 0, "Media duración préstamos": 0, 
            "Géneros": {}, "Mes más lector": None
        }
    mes_top = groupByColumn(df_usuario, "Mes")
    
    return {
        "Prestamos": prestamos,
        "Media duración préstamos": df_usuario["Duracion"].mean(),
        "Géneros": df_usuario["Genero"].value_counts().to_dict(),
        "Mes más lector": mes_top
    }

def userInfoYear(df, u, y):
    return userInfo(filter_year(df, y), u)



#
# Ejercicio 4
#

# funciones auxiliares para el ejercicio 4
def get_most_renewed(df):
    # obtenemos solo las renovaciones
    df_renewed = df[df["Renovacion"]] 
    if df_renewed.empty:
        return None
    # reusamos la logica del ejercicio 3
    return groupByColumn(df_renewed, ["Titulo", "Autor", "Genero"])

def get_duration_stats(df, group_cols, method='min'):
    # obtenemos la media
    series_mean = df.groupby(group_cols, observed=True)["Duracion"].mean()
    
    if series_mean.empty:
        return None

    # para no tener dos funciones, con el parametro method elegimos si queremos obtener el maximo o el minimo
    if method == 'min':
        idx = series_mean.idxmin()
        val = series_mean.min()
    else:
        idx = series_mean.idxmax()
        val = series_mean.max()

    if isinstance(idx, tuple):
        return (*idx, val)
    
    return (idx, val)


# a) Libro más renovado
def mostRenewedBook(df):
    return get_most_renewed(df)

def mostRenewedBookYear(df, y):
    return get_most_renewed(filter_year(df, y))

# b) Libro más rápido
def fastestBook(df):
    return get_duration_stats(df, ["Titulo", "Autor"], method='min')

def fastestBookYear(df, y):
    return get_duration_stats(filter_year(df, y), ["Titulo", "Autor"], method='min')

# c) Libro más lento 
def slowestBook(df):
    return get_duration_stats(df, ["Titulo", "Autor"], method='max')

def slowestBookYear(df, y):
    return get_duration_stats(filter_year(df, y), ["Titulo", "Autor"], method='max')

# d) Género más rápido
def fastestGenre(df):
    return get_duration_stats(df, "Genero", method='min')

def fastestGenreYear(df, y):
    return get_duration_stats(filter_year(df, y), "Genero", method='min')

# e) Género más lento
def slowestGenre(df):
    return get_duration_stats(df, "Genero", method='max')

def slowestGenreYear(df, y):
    return get_duration_stats(filter_year(df, y), "Genero", method='max')



#
# Ejercicio 5
#

# a)
def addAlerts(df):
    df["Avisos"] = df["Duracion"] > 30
    return df
 # b)
def showAlerts(dfe):
    alerts_df = dfe[dfe["Avisos"]]
    if alerts_df.empty:
        return []
    
    # Contamos alertas por lector y ordenamos por cantidad
    counts = alerts_df.groupby("Lector", observed=True).size()
    counts = counts[counts > 0]
    result = list(counts.items())
    result.sort(key=lambda x: x[1], reverse=True)

    return result

def showAlertsYear(dfe, y):
    return showAlerts(filter_year(dfe, y))



#
# Ejercicio 6
# 


def tooLate(dfe):
    late_loans = dfe[dfe["Avisos"]].copy()
    
    if late_loans.empty:
        return (0, 0, 0)
        
    late_loans["DiasExceso"] = late_loans["Duracion"] - 30
    
    media_total = late_loans["DiasExceso"].mean()

    sum_exceso_lector = late_loans.groupby("Lector", observed=True)["DiasExceso"].sum()
    sum_exceso_lector = sum_exceso_lector[sum_exceso_lector > 0]
    
    if sum_exceso_lector.empty:
         return (media_total, 0, 0)

    top_user = sum_exceso_lector.idxmax()
    media_top_user = late_loans[late_loans["Lector"] == top_user]["DiasExceso"].mean()
    
    bottom_user = sum_exceso_lector.idxmin()
    media_bottom_user = late_loans[late_loans["Lector"] == bottom_user]["DiasExceso"].mean()
    
    return (media_total, media_top_user, media_bottom_user)
