from guizero import App, Text, Combo, PushButton
from random import randint

def play_game_def():
	player_message.value = "Player Chose: " + player_choice.value

	chosen = randint(1,3)
	if chosen==1:
		computer = 'Rock'
	elif chosen ==2:
		computer = 'Paper'
	else:
		computer = 'Scissors'
	computer_message.value = "Computer Chose: " + computer

	if player_choice.value==computer:
		final_message.value = 'DRAW'
	elif player_choice.value =='Rock' and computer =='Scissors':
		final_message.value = 'Player LOSS'
	elif player_choice.value =='Rock' and computer =='Paper':
		final_message.value = 'DRAW'
	elif player_choice.value =='Paper' and computer =='Rock':
		final_message.value = 'Player LOSS'
	elif player_choice.value =='Paper' and computer =='Scissors':
		final_message.value = 'Player WINS!'
	elif player_choice.value =='Scissors' and computer =='Paper':
		final_message.value = 'DRAW'
	elif player_choice.value =='Scissors' and computer =='Rock':
		final_message.value = 'Player WINS!'

app = App(title="Scissors Rock Paper by Jayden on GuiZero",width=600, height=400, layout="grid", bg="black")

welcome = Text(app, text="Welcome to Scissors Rock Paper", grid=[0,2], align="bottom")
welcome1 = Text(app, text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", grid=[6,12], align="left")
player_choice = Combo(app, options=["Rock","Paper", "Scissors"], grid=[1,3], align="left")
player_choice_text = Text(app, text="Player Choice: ", grid=[2,9], align="left", color='blue')
player_message = Text(app, text="", grid=[0,6], align="left", color='blue')
computer_message = Text(app, text="", grid=[0,7], align="left", color='brown')
final_message = Text(app, text="", grid=[0,8], align="left", color='grey')
play_game = PushButton(app, command=play_game_def, text="PLAY GAME", grid=[1,15],align="left")

app.display()