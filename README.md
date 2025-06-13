# Finales Projekt FSST geteilt 3AHEL
## Erstellt von: Dominic Pittl und Sebastian Konegger

### Idee: 
Wir wollen ein Higher or Lower game mit den Stats von FC25 machen. Dafür sollten wir eine Datenbank verwenden, die alle Spieler nach name, card_type, overall, pace, shooting, passing, dribbling, defending und physical sortieren und anschließend in die Liste all_players speichert. Aus dieser Liste sollen zwei zufällig ausgesuchte Spieler ausgewählt werden undder Nutzer soll raten ob entweder Spieler1 oder Spieler2 mehr pace beispielsweise hat. Beim Reveal soll der Counter neben dem Knopf raufzählen bis zum jeweiligen Stat. Je nach demwelchen Button man drückt wird der score um eins raufgezählt. Ziel des Spiels ist so weit wie möglich zu kommen. Die Grafikoberfläche soll in tkinter programmiert werden.

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
    
![image](https://github.com/user-attachments/assets/b945768e-b971-4be4-b3cf-714a9387f2a4)

![image](https://github.com/user-attachments/assets/cabc1341-b669-4334-8387-6e1d4750e79c) Die Überschriften müssen nochmals seperat konfiguriert werden. 

![image](https://github.com/user-attachments/assets/c586a09b-d1af-467f-827a-a24868aee1c1)


## Gameplay-Details

Es wird zufällig ein Stat (z. B. dribbling, shooting) ausgewählt.
- Zwei Spieler werden aus der Liste gezogen.
- Der Spieler wählt, welcher der beiden den höheren Wert im angezeigten Stat hat (oder ob es ein Gleichstand ist).
- Der Stat wird nach dem Klick animiert aufgedeckt.
- Bei korrekter Wahl erhöht sich der Punktestand um +1.
- Bei einem Fehler wird der Score auf 0 zurückgesetzt, das Spiel beginnt von vorn.






 
  
