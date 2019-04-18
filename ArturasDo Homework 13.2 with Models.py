import datetime
import json
import random


class Result():
    def __init__(self, score, player_name, date):
        self.score = score
        self.player_name = player_name
        self.date = date

# Function for playing the game
def play_game():
    secret = random.randint(1, 30)
    score_list = get_score_list()
    score = 0

    player_name = input("Enter player name: ")
    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        score += 1
        if guess == secret:
            score_list.append({"attempts": score, "player_name": player_name, "date": str(datetime.datetime.now())})
            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(score))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")


# Get a list of all scores
def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


# Return top 3 scores
def get_top_scores():
    score_list = get_score_list()
    top_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]
    return top_score_list


# Run the game
def main():
    while True:
        selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

        if selection.upper() == "A":
            play_game()
        elif selection.upper() == "B":
            for score_dict in get_top_scores():
                print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
        else:
            break


if __name__ == "__main__":
    main()