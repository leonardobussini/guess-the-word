import aiuto
import random

POSSIBILI_PAROLE = [
    "BALCONE", 
    "CACCA", 
    "CANE", 
    "GATTO", 
    "BULDOGHINO",
    "CARLINO",
    "MUSICISTA",
    "ESSEREINUTILE"
    "PAPPAGALLO",
    "PERSONA", 
    "GIRASOLE",
    "TELEVISIONE",
    "CACTUS",
    "LIBRI",
    "NONNA",
    "PELLICANO",
    "BALENA",
    "PRESA",
]

MISTERIOUS_WORD = random.choice(POSSIBILI_PAROLE)
TOTALE_TENTATIVI = len(MISTERIOUS_WORD)

print("*** GUEST THE WORD ***")
print("Benvenuto! In questo gioco devi indovinare una parola misteriosa.")
print(f"Hai {TOTALE_TENTATIVI} tentativi. Per ogni tentivo puoi chiedere una lettera OPPURE tentare di indovinare la parola.")

lunghezza_parola_misteriosa = len(MISTERIOUS_WORD)
parola_nascosta = aiuto.mostra_lettere_trovate(MISTERIOUS_WORD, "@")

print()
print(f"Ti faccio vedere la lunghezza della parola: {parola_nascosta}")

lettere_richieste :list = []

for i in range(TOTALE_TENTATIVI):

    tentativo_utente = input("Digita la lettera da chiedere oppure la parola da indovinare:")
    #print(f"[DEBUG] Tentativo utente: {tentativo_utente}")

    lunghezza_tentativo = len(tentativo_utente)
    #print(f"[DEBUG] Lunghezza tentativo: {lunghezza_tentativo}")

    if (lunghezza_tentativo == 1):
        lettere_richieste.append(tentativo_utente)
        #print(f"[DEBUG] Lettere già richieste (prima): {lettere_richieste}")
        parola_con_lettere_nascoste = aiuto.mostra_lettere_trovate(MISTERIOUS_WORD, lettere_richieste)
        print(f"Questa è la parola con le lettere che hai indovinato: {parola_con_lettere_nascoste}")        
        #print(f"[DEBUG] Lettere già richieste (dopo): {lettere_richieste}")
    else:
        # Questo è il caso dell'utente che cerca di indovinare
        if (MISTERIOUS_WORD == tentativo_utente):
            print("***********************************")
            print("*** BRAVISSIMO! Hai indovinato! ***")
            print("***********************************")        
            exit(0)
        else:
            print(":(")
            print(" Mi dispiace: hai sbagliato!")
            
    print()
    print(f"Ti sono rimasti ancora {TOTALE_TENTATIVI - (i + 1)} tentativi...")
    print()
            
print("Tentativi finiti!")
print(f"La parola nascosta era: {MISTERIOUS_WORD}")
print("GAME OVER!!!")
print("GAME OVER!!!")
print("GAME OVER!!!")
        