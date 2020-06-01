
#  ANDREBBERO MIGLIORATI I CONTROLLI

                    #####-#####-#####-#####-#####-#####-#####-#####-#####-#####

def Indici_SottoStringa(Stringa,SottoStringa):
    Indici = []
    for I in range(len(Stringa)):
        if Stringa[I:(I+len(SottoStringa))] == SottoStringa:
            Indici += [I]
    return Indici

def Split_Indici(Stringa,ListaIndici):
	ListaStringhe = []
	Inizio, Fine  =  0, ListaIndici[0]
	for I in range(len(ListaIndici)-1):
		ListaStringhe += [Stringa[Inizio:Fine]]
		Inizio = Fine
		Fine = ListaIndici[I+1]
	ListaStringhe += [Stringa[Inizio:Fine]]
	ListaStringhe += [Stringa[Fine:]]
	return ListaStringhe


def Anteponi_SottoStringa(Stringa,SottoStringa,StringaInser,CaseInsensitive=False):
    if CaseInsensitive:
        Indici = Indici_SottoStringa(Stringa.upper(),SottoStringa.upper())
    else:
        Indici = Indice_SottoStringa(Stringa,SottoStringa)
    Stringhe = Split_Indici(Stringa,Indici)
    #print(Stringhe)
    NuovaStr = Stringhe[0]
    for I in range(1,len(Stringhe)):
        NuovaStr += StringaInser + Stringhe[I]
    return NuovaStr

                    #####-#####-#####-#####-#####-#####-#####-#####-#####-#####
