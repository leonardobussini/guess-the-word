import time

def mostra_lettere_trovate(parola_misteriosa, gruppo_di_lettere_richieste: list):
    
    # Iniziamo con una stringa vuota
    parola_con_lettere_nascoste = ""
    
    # Separo la parola in ingresso in lettere separater
    lettere_parola_misteriosa = crea_lista_lettere(parola_misteriosa)
    
    # Scorro tutte le lettere della parola misteriosa
    for i in range(len(parola_misteriosa)):
        
        # Recupero la lettera corrente
        lettera_corrente = lettere_parola_misteriosa[i]
        
        # Se la lettera corrente è comprensa nella lista delle lettere richieste 
        # aggiungo la lettera "in chiaro" alla stringa finale
        if (lettera_corrente in gruppo_di_lettere_richieste):
            parola_con_lettere_nascoste = parola_con_lettere_nascoste + lettera_corrente
        
        # Altrimenti metto un "-"
        else:
            parola_con_lettere_nascoste = parola_con_lettere_nascoste + "-"
    
    # Mando in uscita la parola con le lettere mostrate
    return parola_con_lettere_nascoste


def crea_lista_lettere(parola_da_separare):
    
    # Preparo una lista vuota
    lettere_parola_misteriosa =[]
    
    # Scorro tutte le lettere della parola
    for i in range(len(parola_da_separare)):        
        
        # Calcolo il punto di inizio e il punto di fine della
        # parola da separare per avere solo una lettere alla volta
        parti_da = i
        togline_n = len(parola_da_separare) - (parti_da + 1)
        
        # Se siamo alla fine della parola non posso dare alla 
        # funzione che taglia la parola una "fine", quindi ho 
        # solo il punto da dove inizio a tagliare ma non la fine
        if (togline_n > 0):
            lettera_corrente = parola_da_separare[parti_da:-togline_n]
        else:
            lettera_corrente = parola_da_separare[parti_da:]        
        
        #print(f"[DEBUG] lettera_corrente: {lettera_corrente}")
        
        # Aggiungo la lettera trovata alla lista di uscita
        lettere_parola_misteriosa.append(lettera_corrente)        
        
    # Mando fuori la lista con tutte le lettere trovate
    return lettere_parola_misteriosa

def animate():
    animation = [
    "[        ]",
    "[=       ]",
    "[===     ]",
    "[====    ]",
    "[=====   ]",
    "[======  ]",
    "[======= ]",
    "[========]",
    "[ =======]",
    "[  ======]",
    "[   =====]",
    "[    ====]",
    "[     ===]",
    "[      ==]",
    "[       =]",
    "[        ]",
    "[        ]"
    ]

    notcomplete = True

    i = 0

    while notcomplete:
        print(animation[i % len(animation)], end='\r')
        time.sleep(.1)
        i += 1