from reports import *

file = open('exports.txt', 'w')

print("1. How many games are in the file?\n2. Is there a game from a given year?\n3. Which was the latest game?\n" +
        "4. How many games do we have by genre?\n5. What is the line number of the given game?")

while True:
    starter = input("Which of the above ones are you interested in? (Press the number or hit the q key to exit):\n")
    if starter == '1':
        file.write(str(count_games('game_stat.txt')) + '\n')
    if starter == '2':
        file.write(str(decide('game_stat.txt', input("Please give me a year: "))) + '\n')
    if starter == '3':
        file.write(get_latest('game_stat.txt') + '\n')
    if starter == '4':
        file.write(str(count_by_genre('game_stat.txt', input("Please give me a genre: "))) + '\n')
    try:
        if starter == '5':
            file.write(str(get_line_number_by_title('game_stat.txt', input("Please give me a title: "))) + '\n')
    except ValueError:
        print("Sorry that's not a valid title!")
        continue
    if starter == 'q':
        break
    else:
        continue

file.close()