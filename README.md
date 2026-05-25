# Guest The Word

Si tratta di un gioco in cui l'utente deve indivinare una parola che conosce solo il programma.
La parola viene scelta in maniera casuale dal programma. A quel punto l'utente ha 5 tentativi 
durante i quali può chiedere una lettera O provare ad indovinare la parola.

Ad ogni tentativo, se la lettera richiesta:
-  è presente nella parola vengono mostrare le posizioni di quella lettera
-  se non è presente viene mostrato un errore e si passa al prossimo tentantivo

Esempio:
- La parola misteriosa è "CATARRO"
- Al primo turno l'utente chiede la lettera "Z"
- Il programma dice che la lettara "Z" non è presente
- L'utente prova ugualmente ad indovinare la parola
- Se indovina il gioco finisce e l'utente ha vinto
- Se l'utente chiede la lettera "A" il programma mostra "_A_A___"
- Si procede finchè l'utente non finisce i tentativi e a quel punto perde
