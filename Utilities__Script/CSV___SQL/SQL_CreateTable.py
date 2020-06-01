

                    #####-#####-#####-#####-#####-#####-#####-#####-#####-#####

from INPUT import *
NOME_FILE_OUTPUT = NOME_FILE_OUTPUT_CREATE

                    #####-#####-#####-#####-#####-#####-#####-#####-#####-#####

def SqlStr_CreateTable(NomeTabella,Colonne,Rimpiazza,Indirizzamento=False,NomeChiave="",PrefissoDataBase=""):
    if PrefissoDataBase != "":
        NomeTabella = PrefissoDataBase + "." + NomeTabella
    if Rimpiazza:
        Sql = "CREATE OR REPLACE TABLE " + NomeTabella + "\n("
    else:
        Sql = "CREATE TABLE " + NomeTabella + "\n("
    if Indirizzamento:
        Sql += "\n\t" + NomeChiave + " " + "INT PRIMARY KEY" + ","
    for (Nome,Tipo) in Colonne:
        Sql += "\n\t" + Nome + " " + Tipo + ","
    Sql = Sql[:-1]    #  Rimozione Dell'Ultima Virgola
    Sql += "\n);"
    return Sql

                    #####-#####-#####-#####-#####-#####-#####-#####-#####-#####

def EseguiScript(ScritturaFile=True):
    Stringa_CreateTable = SqlStr_CreateTable(NOME_TABELLA,COLONNE,RIMPIAZZA_TABELLA,CHIAVE_AGGIUNTIVA,NOME_CHIAVE_AGGIUNTIVA,PREFISSO_DATABASE)
    #print( Stringa_CreateTable )
    if ScritturaFile:
        File_Out = open( NOME_FILE_OUTPUT ,"w")
        File_Out.write( "\n" + Stringa_CreateTable + "\n" )
        File_Out.close()
    return Stringa_CreateTable

#EseguiScript(True)

                    #####-#####-#####-#####-#####-#####-#####-#####-#####-#####




