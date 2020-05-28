

                    #####-#####-#####-#####-#####-#####-#####-#####-#####-#####

HOST_NAME = "localhost"
USER_NAME = "root"
PASSWORD = ""
DATABASE_NAME = "COVID_19"
              
                    #####-#####-#####-#####-#####-#####-#####-#####-#####-#####
 
import SQL_CreateTable, SQL_Insert

Stringa_CreateTable = SQL_CreateTable.EseguiScript( ScritturaFile=True )
Stringa_Insert = SQL_Insert.EseguiScript( ScritturaFile=True )

                    #####-#####-#####-#####-#####-#####-#####-#####-#####-#####
"""
import MySQLdb

Conn = MySQLdb.connect( HOST_NAME, USER_NAME, PASSWORD, DATABASE_NAME )
Curs = Conn.cursor()

Curs.execute( Stringa_CreateTable )
Conn.commit()

Curs.execute( CreaStringa_Insert(NOME_TABELLA,Tupla,CHIAVE_AGGIUNTIVA,AutoIncremento) )
Conn.commit()

Conn.close()
"""
                    #####-#####-#####-#####-#####-#####-#####-#####-#####-#####

