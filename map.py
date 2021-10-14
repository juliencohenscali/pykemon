from colorama import init
from termcolor import colored

# colorama initialisation
init()


class Map:
    decorpix = []

    def __init__(self, filename, decorpix):
        self.filename = "Map.txt"
        self.decorpix = []
        for i in range(20):
            decorpix.append([])
        self.MapWFile()

    # initialise la map avec le fichier Map.txt(que je dois remplir)
    def MapWFile(self):
        file = open(self.filename, 'r')
        l = file.readline()
        while l:
            lst = l.split(' ')
            a = Objects(lst[0], lst[1], lst[2], lst[3])
            self.decorpix[lst[0]][lst[1]] = a
            l = file.readline()

    def __Print__(self):
        Up = colored("████████████████████████████████████████████████████████████████████████████████\n", 'green')
        lines = ""
        for i in range(20):
            lines += colored("█" + self.decorpix[i] + "█\n", 'green')
        return Up + lines + Up


class Objects:
    def __init__(self, Xpos, Ypos, asci, color):
        self.Xpos = Xpos
        self.Ypos = Ypos
        self.asci = asci
        self.color = color

    def __Print__(self):
        return colored(self.asci, self.color)
