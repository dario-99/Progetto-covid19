

                    #####-#####-#####-#####-#####-#####-#####-#####-#####-#####

from INPUT import *
NOME_FILE_OUTPUT = NOME_FILE_OUTPUT_INSERT
                  
                    #####-#####-#####-#####-#####-#####-#####-#####-#####-#####
    
import pandas
from math import isnan as Valore_Nan

def DuplicaApostrofi(Str):
    NuovaStr = ""
    for C in Str:
        NuovaStr += C
        if C == "\'":
            NuovaStr += "\'"
    return NuovaStr

def TrovaTabellaCsv(NomeCompleto_FileCsv,Colonne):
    Tabella_Base = pandas.read_csv(NomeCompleto_FileCsv)
    Tabella = pandas.DataFrame( Tabella_Base )
    return Tabella.values.tolist()

def SqlStr_Insert(NomeTabella,Tupla,Indirizzamento=False,NomeId=0,NomiCampi=""):
    #print(Tupla)
    Sql = "INSERT INTO " + NomeTabella + NomiCampi + " VALUES ("
    if Indirizzamento:
        Sql += str(NomeId) + ", "
    for Campo in Tupla:
        if type(Campo) == str:
            Campo = DuplicaApostrofi(Campo)
            Sql += "\'" + Campo + "\'"
        elif (type(Campo)==None) or (Valore_Nan(Campo)):
            Sql += "NULL"
        else:
            Sql += str(Campo)
        Sql += ", "
    Sql = Sql[:-2]   #  Rimozione Dell'Ultima Virgola E Dell'Ultimo Spazio 
    Sql += ");"
    return Sql

def SqlStr_Insert_Multipli(TabellaCsv,NomeTabella,Indirizzamento=False,NomiCampi=""):
    AutoIncremento = 0
    Sql = ""
    for Tupla in TabellaCsv:
        AutoIncremento += 1
        Sql += SqlStr_Insert(NomeTabella,Tupla,Indirizzamento,AutoIncremento,NomiCampi) + "\n"
        #print(Tupla)
        #print( CreaStringa_Insert(NOME_TABELLA,Tupla,True,AutoIncremento)+"\n\n" )
    Sql = Sql[:-1]  #  Rimozione Dell'Ultimo A Capo
    return Sql

def SqlStr_Insert_Controlli(TabellaCsv,PrefissoDataBase,NomeTabella,Colonne,Indirizzamento=False,NomeChiave="",Campi=False):
    if Campi:
        NomiCampi = " ("
        if Indirizzamento:
            NomiCampi += NomeChiave + ", "
        for (Nome,Tipo) in Colonne:
            NomiCampi += Nome + ", "
        NomiCampi = NomiCampi[:-2] + ") "  #  Rimozione Dell'Ultima Virgola E Dell'Ultimo Spazio
    else:
        NomiCampi = ""
    if PrefissoDataBase != "":
        NomeTabella = PrefissoDataBase + "." + NomeTabella
    return SqlStr_Insert_Multipli(TabellaCsv,NomeTabella,Indirizzamento,NomiCampi)

                    #####-#####-#####-#####-#####-#####-#####-#####-#####-#####

def EseguiScript(ScritturaFile=True):
    #   Uso Implicito Delle Variabili Globali
    TabellaCsv = TrovaTabellaCsv( PERCORSO_NOME_FILE_CSV, COLONNE )
    Stringa_Insert = SqlStr_Insert_Controlli(TabellaCsv,PREFISSO_DATABASE,NOME_TABELLA,COLONNE,CHIAVE_AGGIUNTIVA,NOME_CHIAVE_AGGIUNTIVA,NOMI_CAMPI)
    print(Stringa_Insert)
    if ScritturaFile:
        File_Out = open( NOME_FILE_OUTPUT ,"w")
        File_Out.write( "\n" + Stringa_Insert + "\n" )
        File_Out.close()
    return Stringa_Insert

EseguiScript(True)

                    #####-#####-#####-#####-#####-#####-#####-#####-#####-#####




