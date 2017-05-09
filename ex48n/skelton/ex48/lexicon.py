def scan(line):
    ' scan a line and split into words '
    words = line.split(' ')
    # analyse words
    result = []
    # for each word, send it to the analyzer to analyse
    for word in words:
        # Make sure the scanner handles user input in any capitalization and case.
        type = analyse(word.lower())
        result.append((type, word))
    return result

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)
