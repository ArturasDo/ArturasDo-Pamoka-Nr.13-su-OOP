import json

class Player():
    def __init__(self, type, first_name, last_name, height_cm, weight_kg):
        self.type = type
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

class BasketballPlayer(Player):
    def __init__(self, type, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(type=type, first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(type=type, first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

# Enter of data to the data_list
data_list = open("data_list.txt", "w")
while True:
    selection = input("Enter 'B' for entering BasketBallPlayer, 'F' - FootBallPlayer and 'C' - to cancel: ")

    if selection.upper() == "B":
        type = "BasketBall"
    elif selection.upper() == "F":
        type = "FootBall"
    elif selection.upper() == "C":
        break
    first_name = input("Enter first name: ")
    last_name = input("Enter Last name: ")
    x = dict(type=type, first_name=first_name, last_name=last_name)
#    with open("data_list.txt", "w") as data_list:
    data_list.write(json.dumps(x))
data_list.close()