
                    #####-#####-#####-#####-#####-#####-#####-#####-#####-#####

NOME_FILE_INPUT = "INPUT_OUTPUT_TEXT/Input.txt"

NOME_FILE_OUTPUT = "INPUT_OUTPUT_TEXT/Output.txt"

                    #####-#####-#####-#####-#####-#####-#####-#####-#####-#####

import LibStr

                    #####-#####-#####-#####-#####-#####-#####-#####-#####-#####

def Edita_CreateTable(NomeDataBase,StringaSql):
    Riferimento = "TABLE"
    IndiceBase = StringaSql.upper().find( Riferimento.upper() )
    if IndiceBase < 0:
        raise NameError("Stringa Di Comando Sql Non Valida")
    Indice = IndiceBase + len(Riferimento) + 1
    if NomeDataBase != "":
        return StringaSql[:Indice] + NomeDataBase + "." + StringaSql[Indice:]
    else:
        return StringaSql

def EditaGenerale(NomeDataBase,NomeTabella,StringaSql):
    if NomeDataBase != "":
        return LibStr.Anteponi_SottoStringa(StringaSql,NomeTabella,NomeDataBase+".",CaseInsensitive=True)
    else:
        return StringaSql

FileIn = open(NOME_FILE_INPUT,"r")
ComandoSql = FileIn.read()
FileIn.close()

#ComandoSql = "INSERT INTO tabella_lower values(1); INSERT INTO TABELLA_LOWER values(2);"

NuovoSql = EditaGenerale( NomeDataBase="COVID", NomeTabella="master_table_province", StringaSql = ComandoSql )

#print(NuovoSql)

FileOut = open(NOME_FILE_OUTPUT,"w")
FileOut.write(NuovoSql)
FileOut.close()

                    #####-#####-#####-#####-#####-#####-#####-#####-#####-#####
