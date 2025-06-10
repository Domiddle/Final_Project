import random

class EAFC25_cards(object):
    def __init__(self, name, card_type, overall, pace, shooting, passing, dribbling, defending, physical):
        self.name=name
        self.card_type=card_type
        self.rating=overall
        self.pace= pace
        self.shooting=shooting
        self.passing=passing
        self.dribbling=dribbling
        self.defending=defending
        self.physical=physical

    def get_stat(self, stat_name):
        return getattr(self, stat_name)



if __name__=="__main__":
    #Attacker
    Cristiano_Ronaldo=EAFC25_cards("Cristiano Ronaldo","TOTS",97,92,99,90,96,45,91)
    Lionel_Messi=EAFC25_cards("Messi","TOTS",97,93,96,97,98,45,82)
    Kylian_Mbappe=EAFC25_cards("Mbappe","TOTS",97,99,96,90,98,45,87)
    Lamine_Yamal=EAFC25_cards("Lamine Yamal","TOTS",97,98,95,97,97,43,90)
    Thierry_Henry=EAFC25_cards("Henry","Immortals Icon", 95,96,95,95,94,65,92)
    Ronaldo_Nazario=EAFC25_cards("Ronaldo(R9)","Immortals Icon",96,96,98,81,96,45,80)
    Vinicius_Jr=EAFC25_cards("Vini Jr.","TOTY",97,99,91,90,98,38,78)
    Mohamed_Salah=EAFC25_cards("Salah","TOTS",97,97,95,92,97,60,85)
    Erling_Haaland=EAFC25_cards("Haaland","TOTS",96,94,98,81,90,52,94)
    Raphinha=EAFC25_cards("Raphinha","TOTS",97,99,94,96,95,70,92)
    Lautaro_Martínez=EAFC25_cards("Martínez","TOTS Honourable Mentions",95,92,95,86,94,61,92)
    Eusébio=EAFC25_cards("Eusébio","Immortals Icon",96,95,96,90,96,50,84)
    Johan_Cruyff=EAFC25_cards("Cruyff","Future Stars Icon",96,93,94,93,96,45,78)
    Ousmane_Dembélé=EAFC25_cards("Dembélé","TOTS",97,99,90,94,97,55,75)
    Harry_Kane=EAFC25_cards("Kane","TOTS",97,92,99,93,93,57,92)
    Robert_Lewandowski=EAFC25_cards("Lewandowski","Dreamchasers",95,90,95,88,92,51,91)
    Rodrygo=EAFC25_cards("Rodrygo","Fantasy",95,97,92,92,96,40,76)
    Bobby_Charlton=EAFC25_cards("Charlton","Future Stars Icon",94,92,94,90,93,52,76)
    Bukayo_Saka=EAFC25_cards("Saka","TOTS",93,93,91,90,95,70,85)
    Nicolas_Jackson=EAFC25_cards("Jackson","UECL RTTF",96,96,94,90,95,60,94)
    Omar_Marmoush=EAFC25_cards("Marmoush","Fantasy",95,98,92,89,95,48,86)
    Antoine_Griezmannn=EAFC25_cards("Griezmann","TOTS Highlights",96,92,93,95,96,65,87)
    Rafael_Leao=EAFC25_cards("Rafael Leao","Birthday",94,97,88,89,94,50,86)
    Viktor_Gyökeres=EAFC25_cards("Gyökeres","TOTS",96,96,95,89,95,50,97)
    Randal_Kolo_Muani=EAFC25_cards("Kolo Muani","Fantasy",93,97,93,84,93,49,78)
    Julian_Álvarez=EAFC25_cards("Álvarez","TOTS Highlights",95,93,95,88,92,66,91)
    Bradley_Barcola=EAFC25_cards("Barcola","UCL RTTF",96,98,93,93,95,57,85)
    Karim_Benzema=EAFC25_cards("Benzema","TOTS",96,92,96,95,95,50,92)
    Gareth_Bale=EAFC25_cards("Bale","Immortals Icon",94,99,94,92,95,75,86)
    Ronaldinho=EAFC25_cards("Ronaldinho","Birthday Icon",95,94,91,93,97,41,83)
    #Midfielder
    David_Ginola=EAFC25_cards("Ginola","Immortals Hero",94,94,93,92,94,75,92)
    Steven_Gerrard=EAFC25_cards("Gerrard","Immortals Icon",93,88,92,93,90,87,86)
    Pelé=EAFC25_cards("Pelé","Immortals Icon",97,99,97,93,96,61,82)
    Diego_Maradona=EAFC25_cards("Maradona","Grasroot Greats Icon",96,92,92,92,97,42,80)
    Lothar_Matthäus=EAFC25_cards("Matthäus","Immortals Icon",94,92,91,94,87,94,88)
    Kaká=EAFC25_cards("Kaká","Dreamchasers Icon",94,92,90,90,94,48,90)
    Federico_Valverde=EAFC25_cards("Valverde","TOTS",95,95,90,93,92,88,90)
    Blaise_Matuidi=EAFC25_cards("Matuidi","Fantasy Hero",95,92,82,99,89,99,96)
    Jamal_Musiala=EAFC25_cards("Musiala","TOTS",96,94,93,92,98,75,82)
    Rodri=EAFC25_cards("Rodri","TOTY",97,89,86,94,91,97,92)
    David_Beckham=EAFC25_cards("Beckham","Birthday Icon",94,92,92,97,91,82,86)
    Zico=EAFC25_cards("Zico","Immortals Icon",94,92,95,94,94,67,75)
    Ryan_Gravenberch=EAFC25_cards("Gravenberch","TOTS",95,91,90,95,97,92,92)
    Joao_Neves=EAFC25_cards("Joao Neves","TOTS", 96,94,87,92,96,91,94)
    Cole_Palmer=EAFC25_cards("Palmer","UECL RTTF",97,92,96,97,99,62,86)
    Pedri=EAFC25_cards("Pedri","TOTS",96,93,88,95,96,92,91)
    Florian_Wirtz=EAFC25_cards("Wirtz","TOTS",96,92,90,96,97,61,82)
    Dani_Olmo=EAFC25_cards("Dani Olmo","UCL RTTF",93,91,93,91,93,73,91)
    Jude_Bellingham=EAFC25_cards("Bellingham","TOTY",97,90,95,92,97,87,91)
    Tijjani_Reijnders=EAFC25_cards("Reijnders","TOTS",95,92,91,96,95,89,90)
    Zinedine_Zidane=EAFC25_cards("Zidane","Thunderstruck Icon",96,86,92,96,96,76,86)
    Franck_Ribery=EAFC25_cards("Ribery","Immortals Icon",96,96,92,94,97,53,80)
    Warren_Zaire_Emery=EAFC25_cards("Zaire-Emery","UCL RTTF",96,94,86,93,96,92,94)
    Kevin_De_Bruyne=EAFC25_cards("De Bruyne","Flashback",94,85,92,95,92,80,83)
    Ruud_Gullit=EAFC25_cards("Gullit","Dreamchasers Icon",94,90,92,94,91,87,91)
    Patrick_Vieira=EAFC25_cards("Vieira","Birthday Icon",94,88,85,88,90,94,96)
    #Defenders
    Franz_Beckenbauer=EAFC25_cards("Beckenbauer","Immortals Icon",96,87,77,93,88,97,90)
    Lilian_Thuram=EAFC25_cards("Thuram","Dreamchasers Icon",94,91,62,80,86,94,94)
    Franco_Baresi=EAFC25_cards("Baresi","On this day Icon",94,86,52,80,78,97,86)
    Jaap_Stam=EAFC25_cards("Stam","Grassroot Greats Hero",91,88,56,67,73,93,92)
    Jonathan_Tah=EAFC25_cards("Tah","TOTS",97,90,70,83,85,97,95)
    Dani_Carvajal=EAFC25_cards("Carvajal","TOTY",95,94,78,87,92,95,87)
    Vincent_Kompany=EAFC25_cards("Kompany","Winter Wildcard Hero",90,82,63,77,75,92,90)
    William_Saliba=EAFC25_cards("Saliba","TOTY",95,90,47,80,83,95,93)
    Joao_Cancelo=EAFC25_cards("Cancelo","TOTS",94,93,90,94,93,93,91)
    Maicon=EAFC25_cards("Maicon","Fantasy Hero",93,94,89,88,90,91,91)
    Pau_Cubarsí=EAFC25_cards("Pau Cubarsí","TOTS",93,91,48,86,90,93,87)
    Antonio_Rüdiger=EAFC25_cards("Rüdiger","TOTS",95,93,62,80,81,92,95)
    Virgil_van_Dijk=EAFC25_cards("Van Dijk","TOTS",97,89,68,81,80,97,96)
    Balde=EAFC25_cards("Balde","TOTS Honourable Mentions",94,99,60,88,90,93,88)
    Marquinhos=EAFC25_cards("Marquinhos","UCL RTTF",96,93,70,88,85,97,94)
    Lucio=EAFC25_cards("Lucio","Dreamchsers Hero",94,90,77,80,82,95,94)
    Philipp_Lahm=EAFC25_cards("Lahm","Dreamchaser Icon",92,90,80,88,90,92,80)
    Roberto_Carlos=EAFC25_cards("Roberto Caralos","TOTY Icon",92,92,87,88,85,90,91)
    Cafu=EAFC25_cards("Cafu","TOTY Icon",93,93,70,85,90,92,90)
    Paolo_Maldini=EAFC25_cards("Maldini","Immortals Icon",94,90,57,80,75,97,91)

all_players= [
    Cristiano_Ronaldo, Lionel_Messi, Kylian_Mbappe, Lamine_Yamal,
    Thierry_Henry, Ronaldo_Nazario, Vinicius_Jr, Mohamed_Salah,
    Erling_Haaland, Raphinha, Lautaro_Martínez, Eusébio, Johan_Cruyff,
    Ousmane_Dembélé, Harry_Kane, Robert_Lewandowski, Rodrygo,
    Bobby_Charlton, Bukayo_Saka, Nicolas_Jackson, Omar_Marmoush,
    Antoine_Griezmannn, Rafael_Leao, Viktor_Gyökeres, Randal_Kolo_Muani,
    Julian_Álvarez, Bradley_Barcola, Karim_Benzema, Gareth_Bale,
    Ronaldinho, David_Ginola, Steven_Gerrard, Pelé, Diego_Maradona,
    Lothar_Matthäus, Kaká, Federico_Valverde, Blaise_Matuidi,
    Jamal_Musiala, Rodri, David_Beckham, Zico, Ryan_Gravenberch,
    Joao_Neves, Cole_Palmer, Pedri, Florian_Wirtz, Dani_Olmo,
    Jude_Bellingham, Tijjani_Reijnders, Zinedine_Zidane, Franck_Ribery,
    Warren_Zaire_Emery, Kevin_De_Bruyne, Ruud_Gullit, Patrick_Vieira,
    Franz_Beckenbauer, Lilian_Thuram, Franco_Baresi, Jaap_Stam,
    Jonathan_Tah, Dani_Carvajal, Vincent_Kompany, William_Saliba,
    Joao_Cancelo, Maicon, Pau_Cubarsí, Antonio_Rüdiger,
    Virgil_van_Dijk, Balde, Marquinhos, Lucio, Philipp_Lahm,
    Roberto_Carlos, Cafu, Paolo_Maldini
]

def higher_lower_game():
    score = 0
    stats = ["rating", "pace", "shooting", "passing", "dribbling", "defending", "physical"]
    
    while True:
        stat = random.choice(stats)
        player1, player2 = random.sample(all_players, 2)

        print(f"\nWhich player has higher {stat}?")
        print(f"1: {player1.name}")
        print(f"2: {player2.name}")

        # get user guess
        guess = input("Enter 1 or 2 (Or 0 for a tie): ").strip()
        if guess not in ["1", "2","0"]:
            print("Invalid input. Please enter 1 or 2 (or 0 for a tie)")
            continue

        guess = int(guess)
        player1_stat = player1.get_stat(stat)
        player2_stat = player2.get_stat(stat)

        correct = (player1_stat > player2_stat and guess == 1) or (player2_stat > player1_stat and guess == 2) or (player1_stat == player2_stat and guess == 0)

        if correct:
            score += 1
            print(f"Correct! {player1.name} has {player1_stat} and {player2.name} has {player2_stat}. Your score: {score}")
        else:
            print(f"Wrong! {player1.name} has {player1_stat} and {player2.name} has {player2_stat}. Final score: {score}")
            score=0
            retry=input("Do you want to play another game? Enter y or n: ")
            if retry == "y":
                continue
            else:
                break
                

if __name__ == "__main__":
    print("Welcome to the EAFC25 Higher or Lower Game!")
    higher_lower_game()