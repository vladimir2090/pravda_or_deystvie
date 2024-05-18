import random

list_of_question = [
    "Do you have a word that you invented yourself?",
    "Have you ever lied about your age?",
    "What's the biggest joke you've ever made?",
    "Do you have a weird/special talent?",
    "Do you sing in the bathroom?", "How do you cheat by trying to avoid helping with the housework?",
    "Are you afraid of ghosts?", "Have you ever watered a plant with milk?",
    "Have you ever broken something without telling anyone about it?",
    "If you had 1 minute to quickly get out of the house, what would you take with you?"
]
list_of_action = [
    "Can't blink for a minute", "Run around the house three times",
    "Hug your letterbox (or tree/lawn decoration) for 20 seconds",
    "Speak with your tongue sticking out",
    "Take an action as the next player to select the Action category",
    "Send someone a message using just your nose",
    "Pretend like you're playing air guitar",
    "Sing a nursery rhyme", "Speak and behave like a robot",
    "After everything you say, add the words 'Wow… I'm good!' within the next 15 minutes"
]
gamer_list = []


def gamers(list):
    while True:
        name = input("Enter a Player name – ")
        if 0 < len(name) <= 2:
            continue
        list.append(str.capitalize(name))
        if len(list) >= 2:
            need_next_player = input("More players? – Y/N ")
            if need_next_player == str.lower("y") or need_next_player == str.lower("yes"):
                continue
            else:
                break


gamers(gamer_list)


def game(list_of_question, list_of_action, *args):
    while True:
        next_step = None
        for gamer in args:
            print(gamer)
            user_choise = input("Question or Action? ")
            if user_choise == str.lower("q") or user_choise == str.lower("question"):
                question_index = random.randint(0, len(list_of_question) - 1)
                print(list_of_question[question_index])
                list_of_question.pop(question_index)
            elif user_choise == str.lower("a") or user_choise == str.lower("action"):
                action_index = random.randint(0, len(list_of_action) - 1)
                print(list_of_action[action_index])
                list_of_action.pop(action_index)
            else:
                print("Do and answer")
                question_index = random.randint(0, len(list_of_question) - 1)
                print(list_of_question[question_index])
                list_of_question.pop(question_index)
                action_index = random.randint(0, len(list_of_action) - 1)
                print(list_of_action[action_index])
                list_of_action.pop(action_index)
            if args[-1] == gamer:
                break
            next_step = input("Next player? – Y/N ")
            if next_step == str.lower("y") or next_step == str.lower("yes"):
                continue
            else:
                print("Game is over")
                break
        if next_step == str.lower('y') or next_step == str.lower('yes'):
            pass
        else:
            break
        select = input("New round? – Y/N ")
        if select == str.lower("y") or select == str.lower("yes"):
            continue
        else:
            break


game(list_of_question, list_of_action, *gamer_list)