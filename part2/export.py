from reports import *

file = open('exports.txt', 'w')

print("1. What is the title of the most played game (i.e. sold the most copies)?\n2. How many copies have been sold total?\n3. What is the average selling?\n" +
        "4. How many characters long is the longest title?\n5. What is the average of the release dates?\n6. What properties has a game?")

while True:
    starter = input("Which of the above ones are you interested in? (Press the number or hit the q key to exit):\n")
    if starter == '1':
        file.write(get_most_played('game_stat.txt') + '\n')
    if starter == '2':
        file.write(str(sum_sold('game_stat.txt')) + '\n')
    if starter == '3':
        file.write("{:.2f}\n".format(get_selling_avg('game_stat.txt')))
    if starter == '4':
        file.write(str(count_longest_title('game_stat.txt')) + '\n')
    if starter == '5':
        file.write(str(get_date_avg('game_stat.txt')) + '\n')
    if starter == '6':
        file.write(str(get_game('game_stat.txt', input('Please name a game: '))) + '\n')
    if starter == 'q':
        break
    else:
        continue

file.close()