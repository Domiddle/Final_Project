# Finales Projekt FSST geteilt 3AHEL
## Erstellt von: Dominic Pittl und Sebastian Konegger

### Idee: 
Wir möchten ein Higher or Lower Game entwickeln, basierend auf den Spielerstatistiken von EA FC25.
Dazu verwenden wir eine Datenbank, die Informationen über die Spieler enthält – darunter
- name
- card-type
- pace
- shooting
- passing
- dribbling
- defending
- physical

Diese Spieler werden in die Liste all_players geladen. Zwei zufällige Spieler werden ausgewählt, und der Benutzer soll raten, welcher von beiden z. B. mehr pace hat.
Nach der Auswahl wird der jeweilige Stat animiert (hochgezählt) angezeigt. Je nach Entscheidung des Nutzers wird der Score um +1 erhöht oder zurückgesetzt.
Das Ziel des Spiels: so viele richtige Entscheidungen wie möglich treffen. Die grafische Oberfläche wird mit Tkinter erstellt.

### Benötigte Libraries:
- random: wir brauchen random um die Spieler aus der aus der Datenbank ausgelesenen zufällig rauszusuchen
- tkinter: wir brauchen tkinter um die Grafikoberfläche stilvoll und einfach zu gestalten
- my-sql-connecters: wird gebraucht um die Daten von der MariadB Datenbank auszulesen
- alle anderen Libraries sollte schon in Python vorinstalliert sein

### Benötigte Installationen:
- my-sql-connecters: installiert mit 'pip install mysql-connector-python'
- Alle anderen Libraries sollten schon vorinstalliert sein

### Datenbankdetails:
- Am Anfang mussten wir ein Excel-tabelle mit allen Details von den Fußballspieler machen. Diese Datei muss als .csv Datei abgespeichert werden. 
    
![image](https://github.com/user-attachments/assets/5e1a39fc-bfa5-456a-b9e2-719bb5a66b55)

![image](https://github.com/user-attachments/assets/cabc1341-b669-4334-8387-6e1d4750e79c) 
Die Überschriften müssen nochmals seperat konfiguriert werden. 

![image](https://github.com/user-attachments/assets/c586a09b-d1af-467f-827a-a24868aee1c1)


## Gameplay-Details

Es wird zufällig ein Stat (z. B. dribbling, shooting) ausgewählt.
- Zwei Spieler werden aus der Liste gezogen.
- Der Spieler wählt, welcher der beiden den höheren Wert im angezeigten Stat hat (oder ob es ein Gleichstand ist).
- Der Stat wird nach dem Klick animiert aufgedeckt.
- Bei korrekter Wahl erhöht sich der Punktestand um +1.
- Bei einem Fehler wird der Score auf 0 zurückgesetzt, das Spiel beginnt von vorn.

##Quellen:
- [StackedOverflow](https://stackoverflow.com/questions)
- ChatGPT
- https://docs.python.org/3/






 
  
