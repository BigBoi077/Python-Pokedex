import time
import os

class ProgressBar():
    def __init__(self, number_pokemon, length, command, app):
        self.app = app
        self.clear_command = command
        self.start = time.time()
        self.number_pokemon = number_pokemon
        self.number_space = ""
        self.length = length
        self.number_hashtag = ""
        self.bearings = 0
        self.loading = ""
        self.clear()
        self.init_spaces()

    def clear(self):
        os.system(self.clear_command)

    def init_spaces(self):
        for i in range(self.length):
            self.number_space += " "

    def update_bar(self, position):
        if not self.app.downloadEnabled:
            time.sleep(0.005)
        percent_loaded = self.calculate_percent(position)
        if self.can_update_bar(int(percent_loaded)):
            self.bearings += 100 / self.length
            self.number_space = self.number_space[1:]
            self.number_hashtag += "#"
            self.loading = f"|{self.number_hashtag}{self.number_space}|"
        self.clear()
        self.print_bar(self.loading, percent_loaded, position)

    def print_bar(self, loading, percent, position):
        print(f'{loading}{percent}%, Pokemon #{position + 1}')

    def calculate_percent(self, position):
        return round((position * 100) / self.number_pokemon, 2)

    def can_update_bar(self, percentage):
        return percentage == self.bearings and self.bearings != 100

    def end(self):
        stop = time.time()
        print('\n------------------------------------------------------------')
        print('Duration: [' + str(round(stop - self.start, 2)) + ' secs]\n\n')