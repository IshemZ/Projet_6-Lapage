import pandas as pd
import numpy as np

import pyarrow
import matplotlib.pyplot as plt
import scipy
import sklearn
import timeit
from datetime import datetime 


#Librairie de modules fonctionnelle


"""SPLIT une colonne en 2 en utilisant un espace dans la cellule

df = ton dataframe
new_col1 = contiendra les element avant l'espace
new_col2 = contiendra les element après l'espace
target_col = la colonne que tu veux couper en deux

"""
def split_column_using_space(df, new_col1, new_col2, target_col):
    df[[new_col1, new_col2]] = df[target_col].str.split(expand=True)
    return df


"""Charger et afficher un nouveau fichier ".csv"
Snippet qui permet de charger les fichier ".csv"

df      = nom du dataframe de base
path    = l'emplacement du fichier brut '../Source/customers.csv'
delim   = le séparateur

"""
def load_csv_files_as_df(df, path, delim):
    df = pd.read_csv(path, sep=delim)
    return df


"""Afficher des données statistiques de base
Snippet qui permet de charger les statistiques de base pour un dataframe

df      = nom du dataframe ou les statistiques sont souhaité

"""
def statistique_rapide_df(df):
    print(df.shape) 
    print(df.head())  
    print(df.describe())
    print(df.info())  
    return


"""Convertir une colonne dans un df en datetime en ajoutant une nouvelle colonne Timestamp

Snippet qui permet d'ajouter et convertir une colonne d'un df en datetime (Timestamp)

df              = nom du dataframe ou les statistiques sont souhaité
new_col         = nouveau nom de colonne
column_name     = la colonne que l'on souhaite convertir
format          = None

"""
def convert_column_to_datetime(df, column_name, format=None):
    df
    pd.to_datetime(df[column_name],format=format)
    return df


"""Convertir une colonne dans un df en datetime

module qui permet de convertir une colonne d'un df en datetime

df              = nom du dataframe ou les statistiques sont souhaité
column_name     = la colonne que l'on souhaite convertir

"""
def convert_column_to_date_only_Ymd(df, column_name):
    x = pd.to_datetime(df[column_name], format="%Y-%m-%d")
    return x


""" génère une colonne d'occurance des valeurs d'un colonnes

Snippet qui permet génère une colonne d'occurance des valeurs d'un colonnes

new_df          = nom du nouveau dataframe ou l'occurance se crée
df              = le dataframe analysé
col             = la colonne que l'on souhaite analyser

"""
def colonne_occurance_valeurs(df, col):
    x = df[[col]].value_counts(normalize=True)
    x.to_frame().reset_index(drop=False).sort_values(by='proportion', ascending=False)
    return x