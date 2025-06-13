import random
import tkinter as tk
import mysql.connector
from mysql.connector import Error

class EAFC25_cards(object):
    def __init__(self, name, card_type, overall, pace, shooting, passing, dribbling, defending, physical):
        self.name = name
        self.card_type = card_type
        self.rating = overall
        self.pace = pace
        self.shooting = shooting
        self.passing = passing
        self.dribbling = dribbling
        self.defending = defending
        self.physical = physical

    def get_stat(self, stat_name):
        return getattr(self, stat_name)

def load_players_from_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',       # <-- Ersetze hier
            password='',   # <-- Ersetze hier
            database='footballers-higher-or-lower-game'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT name, card_type, overall, pace, shooting, passing, dribbling, defending, physical FROM player_table_import")

        all_players = []
        for row in cursor.fetchall():
            player = EAFC25_cards(*row)
            all_players.append(player)

        cursor.close()
        connection.close()
        return all_players

    except Error as e:
        print(f"Fehler beim Laden der Spieler aus der DB: {e}")
        return []

class HigherLowerGUI:
    def __init__(self, master):
        self.master = master
        master.title("EAFC25 Higher or Lower Game")

        self.stats = ["rating", "pace", "shooting", "passing", "dribbling", "defending", "physical"]
        self.score = 0
        self.high_score = 0

        self.all_players = load_players_from_db()
        if not self.all_players:
            # Falls keine Spieler geladen wurden, Programm abbrechen oder Meldung anzeigen
            self.stat_label = tk.Label(master, text="Fehler beim Laden der Spieler aus DB.", font=("Helvetica", 16), fg="red")
            self.stat_label.pack(pady=20)
            return

        self.stat = None
        self.player1 = None
        self.player2 = None

        self.stat_label = tk.Label(master, text="", font=("Helvetica", 16))
        self.stat_label.pack(pady=10)

        self.frame_p1 = tk.Frame(master)
        self.frame_p1.pack(pady=5)
        self.player1_button = tk.Button(self.frame_p1, text="", font=("Helvetica", 14), width=20, command=lambda: self.check_guess(1))
        self.player1_button.pack(side=tk.LEFT)
        self.player1_stat_label = tk.Label(self.frame_p1, text="", font=("Helvetica", 14), width=6, fg="blue")
        self.player1_stat_label.pack(side=tk.LEFT, padx=10)

        self.frame_p2 = tk.Frame(master)
        self.frame_p2.pack(pady=5)
        self.player2_button = tk.Button(self.frame_p2, text="", font=("Helvetica", 14), width=20, command=lambda: self.check_guess(2))
        self.player2_button.pack(side=tk.LEFT)
        self.player2_stat_label = tk.Label(self.frame_p2, text="", font=("Helvetica", 14), width=6, fg="blue")
        self.player2_stat_label.pack(side=tk.LEFT, padx=10)

        self.tie_button = tk.Button(master, text="Tie", font=("Helvetica", 14), width=20, command=lambda: self.check_guess(0))
        self.tie_button.pack(pady=5)

        self.score_label = tk.Label(master, text=f"Score: {self.score}", font=("Helvetica", 14))
        self.score_label.pack(pady=5)

        self.high_score_label = tk.Label(master, text=f"High Score: {self.high_score}", font=("Helvetica", 14))
        self.high_score_label.pack(pady=5)

        self.next_round()

    def animate_stat_reveal(self, label, target_value, current_value=0, step=1):
        if current_value >= target_value:
            label.config(text=str(target_value))
            return
        label.config(text=str(current_value))
        diff = target_value - current_value
        if diff > 20:
            step = max(1, diff // 10)
        else:
            step = 1
        self.master.after(30, lambda: self.animate_stat_reveal(label, target_value, current_value + step, step))

    def next_round(self):
        self.stat = random.choice(self.stats)
        self.player1, self.player2 = random.sample(self.all_players, 2)
        self.stat_label.config(text=f"Which player has higher {self.stat}?")

        self.player1_button.config(text=self.player1.name)
        self.player2_button.config(text=self.player2.name)

        self.player1_stat_label.config(text="")
        self.player2_stat_label.config(text="")

        self.score_label.config(text=f"Score: {self.score}")
        self.high_score_label.config(text=f"High Score: {self.high_score}")

        self.player1_button.config(state=tk.NORMAL)
        self.player2_button.config(state=tk.NORMAL)
        self.tie_button.config(state=tk.NORMAL)

    def check_guess(self, guess):
        p1_stat = self.player1.get_stat(self.stat)
        p2_stat = self.player2.get_stat(self.stat)

        self.animate_stat_reveal(self.player1_stat_label, p1_stat)
        self.animate_stat_reveal(self.player2_stat_label, p2_stat)

        self.player1_button.config(state=tk.DISABLED)
        self.player2_button.config(state=tk.DISABLED)
        self.tie_button.config(state=tk.DISABLED)

        correct = (p1_stat > p2_stat and guess == 1) or \
                  (p2_stat > p1_stat and guess == 2) or \
                  (p1_stat == p2_stat and guess == 0)

        if correct:
            self.score += 1
            if self.score > self.high_score:
                self.high_score = self.score
            self.master.after(2000, self.next_round)
        else:
            final_score = self.score
            self.score = 0
            self.stat_label.config(text=f"Wrong! Final score: {final_score}")
            self.master.after(2000, self.next_round)

        self.score_label.config(text=f"Score: {self.score}")
        self.high_score_label.config(text=f"High Score: {self.high_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = HigherLowerGUI(root)
    root.mainloop()
