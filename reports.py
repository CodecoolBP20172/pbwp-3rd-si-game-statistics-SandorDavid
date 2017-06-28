def count_games(file_name):
    with open(file_name) as file:
        game_list = file.readlines()
    return len(game_list)

def decide(file_name, year):
    with open(file_name) as file:
        for line in file:
            line = line.split("\t")
            if str(year) == line[2]:
                return True
    return False

def get_latest(file_name):
    latest_date = 0
    latest_game = ""
    
    with open(file_name) as file:
        for line in file:
            line = line.split("\t")
            if int(line[2]) > latest_date:
                latest_date = int(line[2])
                latest_game = line[0]
    return latest_game

def count_by_genre(file_name, genre):
    genre_counter = 0
    with open(file_name) as file:
        for line in file:
            line = line.split("\t")
            if genre == line[3]:
                genre_counter += 1
    return genre_counter

def get_line_number_by_title(file_name, title):
    line_counter = 0
    with open(file_name) as file:
        for line in file:
            line = line.split("\t")
            if title == line[0]:
                line_counter += 1
                return line_counter
            line_counter += 1
        raise ValueError
