# Final_Project
Finales Projekt FSST geteilt 3AHEL von Dominic Pittl und Sebastian Konegger

Idee: Wir wollen ein Higher or Lower game mit den Stats von FC25 machen. Dafür sollten wir eine Datenbank verwenden, die alle Spieler nach name, card_type, overall, pace, shooting, passing, dribbling,       defending und physical sortieren und anschließend in die Liste all_players speichert. Aus dieser Liste sollen zwei zufällig ausgesuchte Spieler ausgewählt werden undder Nutzer soll raten ob            entweder Spieler1 oder Spieler2 mehr pace beispielsweise hat. Beim Reveal soll der Counter neben dem Knopf raufzählen bis zum jeweiligen Stat. Je nach demwelchen Button man drückt wird der score       um eins raufgezählt. Ziel des Spiels ist so weit wie möglich zu kommen. Die Grafikoberfläche soll in tkinter programmiert werden.

Benötigte Libraries:
    random: wir brauchen random um die Spieler aus der aus der Datenbank ausgelesenen zufällig rauszusuchen
    tkinter: wir brauchen tkinter um die Grafikoberfläche stilvoll und einfach zu gestalten
    my-sql-connecters: wird gebraucht um die Daten von der MariadB Datenbank auszulesen

Benötigte Installationen:
    my-sql-connecters: installiert mit 'pip install mysql-connector-python'
    Alle anderen Libraries sollten schon vorinstalliert sein

Datenbankdetails:
    Am Anfang mussten wir ein Excel-tabelle mit allen Details von den Fußballspieler machen. Diese Datei muss als .csv Datei abgespeichert werden. 
    ![image](https://github.com/user-attachments/assets/b6345518-b41c-4b43-8f4d-365be33484be)



 
  
