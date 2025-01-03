"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd
import numpy as np

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";", index_col=0)
    df = df.copy()

    columnas=["sexo", "tipo_de_emprendimiento", "idea_negocio", "monto_del_credito", "línea_credito"]

    for col in columnas:
        df[col] = df[col].str.lower().str.strip()
        df[col] = df[col].str.replace("_", " ").str.replace("-", " ")
        df[col] = df[col].str.replace(",", "").str.replace("$", "")
        df[col] = df[col].str.replace(".00", "") 
        df[col] = df[col].str.strip()

    df["barrio"]=df["barrio"].str.lower()
    df["barrio"]=df["barrio"].str.replace("_", " ")
    df["barrio"]=df["barrio"].str.replace("-", " ")
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
    df["monto_del_credito"].astype(int)
    df['monto_del_credito'] = df['monto_del_credito'].astype(float)
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce").combine_first(pd.to_datetime(df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce"))
    
 
    df = df.drop_duplicates()
    df = df.dropna()

    df.to_csv("files/output/solicitudes_de_credito.csv", sep=";", index=False) 
    # print(df.columns)
    # print(df.shape))
    # print(df.iloc[70:75])
    # print(df.tipo_de_emprendimiento.value_counts())
    # print(df.idea_negocio.value_counts())
    

pregunta_01()