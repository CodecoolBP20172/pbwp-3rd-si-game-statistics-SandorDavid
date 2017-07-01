import math


def get_most_played(file_name):
    most_played = 0
    most_played_game = ""
    
    with open(file_name) as file:
        for line in file:
            line = line.split("\t")
            if float(line[1]) > most_played:
                most_played = float(line[1])
                most_played_game = line[0]
    return most_played_game


def sum_sold(file_name):
    sold_copies = 0

    with open(file_name) as file:
        for line in file:
            line = line.split("\t")
            sold_copies += float(line[1])
    return sold_copies


def get_selling_avg(file_name):
    sum_of_lines = 0

    with open(file_name) as file:
        for line in file:
            sum_of_lines += 1

    return sum_sold(file_name) / sum_of_lines


def count_longest_title(file_name):
    max_len = 0

    with open(file_name) as file:
        for line in file:
            line = line.split("\t")
            if len(line[0]) > max_len:
                max_len = len(line[0])
    return max_len


def get_date_avg(file_name):
    sum_of_years = 0
    sum_of_lines = 0

    with open(file_name) as file:
        for line in file:
            line = line.split("\t")
            sum_of_years += int(line[2])
            sum_of_lines += 1
    return math.ceil(sum_of_years / sum_of_lines)


def get_game(file_name, title):
    with open(file_name) as file:
        for line in file:
            line = line.split("\t")
            if line[0] == title:
                line[1] = float(line[1])
                line[2] = int(line[2])
                line[4] = line[4].replace('\n', '')
                return line
