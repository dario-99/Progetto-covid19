

                    #####-#####-#####-#####-#####-#####-#####-#####-#####-#####

    #   Input Relativi Al Comando Di Creazione Della Tabella

NOME_FILE_OUTPUT_CREATE = "OUTPUT_TEXT/SQL_CreateTable.txt"

RIMPIAZZA_TABELLA = False

                    #####-#####-#####-#####-#####-#####-#####-#####-#####-#####

    #   Input Relativi Al Comando Di Inserimento Di Dati Letti Da File CSV Nella Tabella

NOME_FILE_OUTPUT_INSERT = "OUTPUT_TEXT/SQL_Insert.txt"

PERCORSO_NOME_FILE_CSV = r"INPUT_CSV/dpc-covid19-ita-province___DATE_FORMATTATE.csv" 

NOMI_CAMPI = False

                    #####-#####-#####-#####-#####-#####-#####-#####-#####-#####

        #   Input Comuni

CHIAVE_AGGIUNTIVA = False

NOME_CHIAVE_AGGIUNTIVA = "Id"

PREFISSO_DATABASE = ""

NOME_TABELLA = "MASTER_TABLE"

COLONNE = [
                ('data', 'DATE'),  #PRIMARY KEY
                ('stato', 'CHAR(3)'),
                ('codice_regione', 'NUMBER(2)'),
                ('denominazione_regione', 'VARCHAR2(200)'),
                ('codice_provincia','NUMBER(3) NOT NULL'),
                ('denominazione_provincia','VARCHAR2(200)'),
                ('sigla_provincia','CHAR(2)'),
                ('latitudine', 'NUMBER'),
                ('longitudine', 'NUMBER'),
                ('totale_casi', 'INTEGER'),
                ('note_it', 'CLOB'),
                ('note_en', 'CLOB')
            ]

#  CONSTRAINT PK_COVID primary key(data,codice_provincia)

                    #####-#####-#####-#####-#####-#####-#####-#####-#####-#####


