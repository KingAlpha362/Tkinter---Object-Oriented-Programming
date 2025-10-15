def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors: )")
    player_choice = "rock"
    computer_choice = "paper"
    choices = {"player": player_choice, "computer": computer_choice}
    return computer_choice

choices = get_choices()
print(choices)

